"""Broadside spatial-truth tool: scene_assert_containment."""

from __future__ import annotations

from dcc_mcp_core.skill import run_main, skill_entry

from spatial_lib import assert_containment


@skill_entry
def main(**kwargs) -> dict:
    """Entry point; delegates to spatial_lib.assert_containment."""
    inner = kwargs.get('inner')
    outer = kwargs.get('outer')
    tolerance = kwargs.get('tolerance')
    return assert_containment(inner=inner, outer=outer, tolerance=tolerance)


if __name__ == "__main__":
    run_main(main)
