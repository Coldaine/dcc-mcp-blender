"""Broadside spatial-truth tool: scene_assert_symmetry."""

from __future__ import annotations

from dcc_mcp_core.skill import run_main, skill_entry

from spatial_lib import assert_symmetry


@skill_entry
def main(**kwargs) -> dict:
    """Entry point; delegates to spatial_lib.assert_symmetry."""
    a = kwargs.get('a')
    b = kwargs.get('b')
    mirror_axis = kwargs.get('mirror_axis')
    tolerance = kwargs.get('tolerance')
    return assert_symmetry(a=a, b=b, mirror_axis=mirror_axis, tolerance=tolerance)


if __name__ == "__main__":
    run_main(main)
