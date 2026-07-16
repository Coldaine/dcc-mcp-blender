"""Broadside spatial-truth tool: scene_measure_dimensions."""

from __future__ import annotations

from dcc_mcp_core.skill import run_main, skill_entry

from spatial_lib import measure_dimensions


@skill_entry
def main(**kwargs) -> dict:
    """Entry point; delegates to spatial_lib.measure_dimensions."""
    object_name = kwargs.get('object_name')
    return measure_dimensions(object_name=object_name)


if __name__ == "__main__":
    run_main(main)
