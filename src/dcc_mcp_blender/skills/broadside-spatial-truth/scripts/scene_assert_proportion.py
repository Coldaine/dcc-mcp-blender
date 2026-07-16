"""Broadside spatial-truth tool: scene_assert_proportion."""

from __future__ import annotations

from dcc_mcp_core.skill import run_main, skill_entry

from spatial_lib import assert_proportion


@skill_entry
def main(**kwargs) -> dict:
    """Entry point; delegates to spatial_lib.assert_proportion."""
    object_name = kwargs.get('object_name')
    dim_a = kwargs.get('dim_a')
    dim_b = kwargs.get('dim_b')
    expected_ratio = kwargs.get('expected_ratio')
    tolerance = kwargs.get('tolerance')
    return assert_proportion(object_name=object_name, dim_a=dim_a, dim_b=dim_b, expected_ratio=expected_ratio, tolerance=tolerance)


if __name__ == "__main__":
    run_main(main)
