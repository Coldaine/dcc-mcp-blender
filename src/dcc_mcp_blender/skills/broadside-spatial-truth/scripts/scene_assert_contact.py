"""Broadside spatial-truth tool: scene_assert_contact."""

from __future__ import annotations

from dcc_mcp_core.skill import run_main, skill_entry

from spatial_lib import assert_contact


@skill_entry
def main(**kwargs) -> dict:
    """Entry point; delegates to spatial_lib.assert_contact."""
    a = kwargs.get('a')
    b = kwargs.get('b')
    tolerance = kwargs.get('tolerance')
    return assert_contact(a=a, b=b, tolerance=tolerance)


if __name__ == "__main__":
    run_main(main)
