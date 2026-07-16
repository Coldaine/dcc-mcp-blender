"""Broadside spatial-truth tool: scene_measure_alignment."""

from __future__ import annotations

from dcc_mcp_core.skill import run_main, skill_entry

from spatial_lib import measure_alignment


@skill_entry
def main(**kwargs) -> dict:
    """Entry point; delegates to spatial_lib.measure_alignment."""
    a = kwargs.get('a')
    b = kwargs.get('b')
    axis_a = kwargs.get('axis_a')
    axis_b = kwargs.get('axis_b')
    return measure_alignment(a=a, b=b, axis_a=axis_a, axis_b=axis_b)


if __name__ == "__main__":
    run_main(main)
