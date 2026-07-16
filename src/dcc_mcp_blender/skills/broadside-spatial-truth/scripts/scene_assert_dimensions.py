"""Broadside spatial-truth tool: scene_assert_dimensions."""

from __future__ import annotations

from dcc_mcp_core.skill import run_main, skill_entry

from spatial_lib import assert_dimensions


@skill_entry
def main(**kwargs) -> dict:
    """Entry point; delegates to spatial_lib.assert_dimensions."""
    object_name = kwargs.get('object_name')
    expected = kwargs.get('expected')
    tolerance = kwargs.get('tolerance')
    return assert_dimensions(object_name=object_name, expected=expected, tolerance=tolerance)


if __name__ == "__main__":
    run_main(main)
