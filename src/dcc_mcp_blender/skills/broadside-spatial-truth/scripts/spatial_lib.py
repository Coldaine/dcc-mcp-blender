"""Geometric truth primitives for Project Broadside.

Self-contained bpy + mathutils helpers backing the broadside-spatial-truth skill.
These are the Broadside-specific spatial assertions (the Patryk-derived
differentiated layer). They reason over world-space bounding boxes, object
origins, and local axis directions so the agent can verify warship assembly
facts: turret-on-barbette seating, barrel parallelism/equal-length, director
centering, superstructure containment, port/starboard mirror match, armor gaps.

All functions return plain dicts suitable for the dcc-mcp skill_entry contract.
"""
from __future__ import annotations

import json
import math
from typing import Iterable, List, Optional, Sequence, Tuple

try:
    import bpy
    from mathutils import Vector
except Exception:  # not running inside Blender / no bpy
    bpy = None
    Vector = None  # type: ignore


Vec = Tuple[float, float, float]


def _err(message: str, **context) -> dict:
    return {"success": False, "message": message, "context": context}


def _ok(message: str, **context) -> dict:
    return {"success": True, "message": message, "context": context}


def _require_bpy() -> Optional[dict]:
    if bpy is None:
        return _err("bpy not available: spatial tools require a Blender runtime")
    return None


def _get_object(name: str) -> Tuple[Optional[object], Optional[dict]]:
    err = _require_bpy()
    if err:
        return None, err
    obj = bpy.data.objects.get(name)
    if obj is None:
        return None, _err(f"object not found: {name!r}", object_name=name)
    return obj, None


def _world_bbox(obj) -> Tuple[Vector, Vector]:
    """World-space AABB from the object's local bound_box transformed by matrix_world."""
    corners = [obj.matrix_world @ Vector(c) for c in obj.bound_box]
    xs = [c.x for c in corners]
    ys = [c.y for c in corners]
    zs = [c.z for c in corners]
    return Vector((min(xs), min(ys), min(zs))), Vector((max(xs), max(ys), max(zs)))


def _dims(bmin: Vector, bmax: Vector) -> Vector:
    return bmax - bmin


def _overlap(bmin1: Vector, bmax1: Vector, bmin2: Vector, bmax2: Vector) -> Optional[Tuple[Vector, Vector]]:
    """Overlapping AABB region, or None if disjoint on any axis."""
    bmin = Vector((max(bmin1.x, bmin2.x), max(bmin1.y, bmin2.y), max(bmin1.z, bmin2.z)))
    bmax = Vector((min(bmax1.x, bmax2.x), min(bmax1.y, bmax2.y), min(bmax1.z, bmax2.z)))
    if bmax.x <= bmin.x or bmax.y <= bmin.y or bmax.z <= bmin.z:
        return None
    return bmin, bmax


def _min_gap(bmin1: Vector, bmax1: Vector, bmin2: Vector, bmax2: Vector) -> float:
    """Smallest non-negative axis-aligned separation between two AABBs (0 if touching/overlap)."""
    gap_x = max(bmin2.x - bmax1.x, bmin1.x - bmax2.x, 0.0)
    gap_y = max(bmin2.y - bmax1.y, bmin1.y - bmax2.y, 0.0)
    gap_z = max(bmin2.z - bmax1.z, bmin1.z - bmax2.z, 0.0)
    # If they overlap on an axis, that axis contributes 0; the real gap is the
    # smallest positive separation, but for "are these touching" semantics we
    # return the minimum across axes (0 means touching or overlapping).
    return min(gap_x, gap_y, gap_z)


def _axis_vector(obj, axis: str) -> Vector:
    """World-space direction of one of the object's local axes (x/y/z)."""
    cols = obj.matrix_world.to_3x3().transposed()
    idx = {"x": 0, "y": 1, "z": 2}[axis.lower()]
    return Vector((cols[idx][0], cols[idx][1], cols[idx][2])).normalized()


def measure_distance(a: str, b: str) -> dict:
    obj_a, err = _get_object(a)
    if err:
        return err
    obj_b, err = _get_object(b)
    if err:
        return err
    pa = obj_a.matrix_world.translation
    pb = obj_b.matrix_world.translation
    dist = (pb - pa).length
    return _ok(
        f"distance {dist:.6f} between {a!r} and {b!r}",
        a=a, b=b, distance=dist,
        a_origin=[pa.x, pa.y, pa.z], b_origin=[pb.x, pb.y, pb.z],
    )


def measure_dimensions(object_name: str) -> dict:
    obj, err = _get_object(object_name)
    if err:
        return err
    bmin, bmax = _world_bbox(obj)
    d = _dims(bmin, bmax)
    return _ok(
        f"dimensions {d.x:.6f} x {d.y:.6f} x {d.z:.6f} for {object_name!r}",
        object_name=object_name,
        dimensions=[d.x, d.y, d.z],
        bbox_min=[bmin.x, bmin.y, bmin.z], bbox_max=[bmax.x, bmax.y, bmax.z],
    )


def measure_gap(a: str, b: str) -> dict:
    obj_a, err = _get_object(a)
    if err:
        return err
    obj_b, err = _get_object(b)
    if err:
        return err
    amin, amax = _world_bbox(obj_a)
    bmin, bmax = _world_bbox(obj_b)
    ov = _overlap(amin, amax, bmin, bmax)
    gap = 0.0 if ov is not None else _min_gap(amin, amax, bmin, bmax)
    return _ok(
        f"min gap {gap:.6f} between {a!r} and {b!r} ({'overlapping' if ov else 'separated'})",
        a=a, b=b, gap=gap, overlapping=ov is not None,
    )


def measure_alignment(a: str, b: str, axis_a: str = "z", axis_b: str = "z") -> dict:
    obj_a, err = _get_object(a)
    if err:
        return err
    obj_b, err = _get_object(b)
    if err:
        return err
    try:
        va = _axis_vector(obj_a, axis_a)
        vb = _axis_vector(obj_b, axis_b)
    except KeyError as exc:
        return _err(f"invalid axis: {exc}")
    dot = max(-1.0, min(1.0, va.dot(vb)))
    angle_rad = math.acos(dot)
    angle_deg = math.degrees(angle_rad)
    # "parallel" allows antiparallel (180) too; parallel_deg is the acute angle
    parallel_deg = min(angle_deg, 180.0 - angle_deg)
    return _ok(
        f"angle {angle_deg:.4f} deg between {a}.{axis_a} and {b}.{axis_b} (parallel={parallel_deg:.4f} deg)",
        a=a, b=b, axis_a=axis_a, axis_b=axis_b,
        angle_deg=angle_deg, parallel_deg=parallel_deg,
    )


def measure_overlap(a: str, b: str) -> dict:
    obj_a, err = _get_object(a)
    if err:
        return err
    obj_b, err = _get_object(b)
    if err:
        return err
    amin, amax = _world_bbox(obj_a)
    bmin, bmax = _world_bbox(obj_b)
    ov = _overlap(amin, amax, bmin, bmax)
    if ov is None:
        return _ok(f"no overlap between {a!r} and {b!r}", a=a, b=b, overlapping=False, overlap_volume=0.0)
    omin, omax = ov
    od = _dims(omin, omax)
    vol = od.x * od.y * od.z
    return _ok(
        f"overlap {od.x:.6f} x {od.y:.6f} x {od.z:.6f} (vol {vol:.6f}) between {a!r} and {b!r}",
        a=a, b=b, overlapping=True, overlap_dimensions=[od.x, od.y, od.z], overlap_volume=vol,
    )


def assert_contact(a: str, b: str, tolerance: float = 1e-4) -> dict:
    res = measure_overlap(a, b)
    if not res["success"]:
        return res
    if res["context"]["overlapping"]:
        return _ok(f"{a!r} and {b!r} overlap (contact confirmed)", a=a, b=b, passed=True, contact=True)
    gap_res = measure_gap(a, b)
    gap = gap_res["context"]["gap"]
    passed = gap <= tolerance
    return _ok(
        f"gap {gap:.6f} <= tol {tolerance} -> {'CONTACT' if passed else 'NO CONTACT'}",
        a=a, b=b, gap=gap, tolerance=tolerance, passed=passed, contact=passed,
    )


def assert_dimensions(object_name: str, expected: Sequence[float], tolerance: float = 1e-3) -> dict:
    res = measure_dimensions(object_name)
    if not res["success"]:
        return res
    dims = res["context"]["dimensions"]
    if len(expected) != 3:
        return _err("expected must be [x, y, z]", object_name=object_name)
    diffs = [abs(d - e) for d, e in zip(dims, expected)]
    passed = all(d <= tolerance for d in diffs)
    return _ok(
        f"dim diffs {diffs} vs tol {tolerance} -> {'PASS' if passed else 'FAIL'}",
        object_name=object_name, dimensions=dims, expected=list(expected),
        diffs=diffs, tolerance=tolerance, passed=passed,
    )


def assert_containment(inner: str, outer: str, tolerance: float = 0.0) -> dict:
    obj_i, err = _get_object(inner)
    if err:
        return err
    obj_o, err = _get_object(outer)
    if err:
        return err
    imin, imax = _world_bbox(obj_i)
    omin, omax = _world_bbox(obj_o)
    contained = (
        imin.x >= omin.x - tolerance and imin.y >= omin.y - tolerance and imin.z >= omin.z - tolerance
        and imax.x <= omax.x + tolerance and imax.y <= omax.y + tolerance and imax.z <= omax.z + tolerance
    )
    return _ok(
        f"{inner!r} {'CONTAINED IN' if contained else 'NOT CONTAINED IN'} {outer!r}",
        inner=inner, outer=outer, tolerance=tolerance, passed=contained, contained=contained,
    )


def assert_symmetry(a: str, b: str, mirror_axis: str = "x", tolerance: float = 1e-3) -> dict:
    obj_a, err = _get_object(a)
    if err:
        return err
    obj_b, err = _get_object(b)
    if err:
        return err
    if mirror_axis.lower() not in ("x", "y", "z"):
        return _err(f"invalid mirror_axis: {mirror_axis}")
    idx = {"x": 0, "y": 1, "z": 2}[mirror_axis.lower()]
    pa = obj_a.matrix_world.translation
    pb = obj_b.matrix_world.translation
    # mirrored: position on mirror axis is negated; off-axis positions equal
    pos_ok = abs((pa[idx] + pb[idx])) <= tolerance
    off_axes = [i for i in range(3) if i != idx]
    pos_ok = pos_ok and all(abs(pa[i] - pb[i]) <= tolerance for i in off_axes)
    # dimensions must match
    amin, amax = _world_bbox(obj_a)
    bmin, bmax = _world_bbox(obj_b)
    da = _dims(amin, amax)
    db = _dims(bmin, bmax)
    dim_ok = all(abs(da[i] - db[i]) <= tolerance for i in range(3))
    passed = bool(pos_ok and dim_ok)
    return _ok(
        f"mirror({mirror_axis}) pos_ok={pos_ok} dim_ok={dim_ok} -> {'PASS' if passed else 'FAIL'}",
        a=a, b=b, mirror_axis=mirror_axis, tolerance=tolerance,
        passed=passed, position_match=pos_ok, dimensions_match=dim_ok,
    )


def assert_proportion(object_name: str, dim_a: str = "x", dim_b: str = "z",
                      expected_ratio: float = 3.0, tolerance: float = 0.05) -> dict:
    res = measure_dimensions(object_name)
    if not res["success"]:
        return res
    dims = res["context"]["dimensions"]
    if dim_a.lower() not in "xyz" or dim_b.lower() not in "xyz":
        return _err(f"invalid dim axis: {dim_a!r}/{dim_b!r}")
    ax = {"x": 0, "y": 1, "z": 2}[dim_a.lower()]
    bx = {"x": 0, "y": 1, "z": 2}[dim_b.lower()]
    if dims[bx] == 0:
        return _err(f"reference dim {dim_b} is zero", object_name=object_name)
    ratio = dims[ax] / dims[bx]
    passed = abs(ratio - expected_ratio) <= tolerance
    return _ok(
        f"ratio {dim_a}/{dim_b} = {ratio:.4f} vs {expected_ratio} ±{tolerance} -> {'PASS' if passed else 'FAIL'}",
        object_name=object_name, dim_a=dim_a, dim_b=dim_b,
        ratio=ratio, expected_ratio=expected_ratio, tolerance=tolerance, passed=passed,
    )
