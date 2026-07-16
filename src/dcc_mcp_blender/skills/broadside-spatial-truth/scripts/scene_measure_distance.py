"""Broadside spatial-truth tool: scene_measure_distance."""

from __future__ import annotations

from dcc_mcp_core.skill import run_main, skill_entry

from spatial_lib import measure_distance


@skill_entry
def main(**kwargs) -> dict:
    """Entry point; delegates to spatial_lib.measure_distance."""
    a = kwargs.get('a')
    b = kwargs.get('b')
    return measure_distance(a=a, b=b)


if __name__ == "__main__":
    run_main(main)
