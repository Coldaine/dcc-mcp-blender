# Broadside Augment Plan

**Date:** 2026-07-16
**Posture:** Fork `dcc-mcp/dcc-mcp-blender` (MIT) and `dcc-mcp/dcc-mcp-core` into
the `Coldaine` account, adopt the code, and augment with Project Broadside skill
packages. This is *not* a framework design or a code port — it is selecting which
existing MCP tools and skills we keep, why, and wiring them into our own fork.

## What changed from the original framing

The first attempt built a documentation-only repo (`broadside-blender-toolkit`)
that catalogued the selection but shipped no functional server and no functional
skills. The corrected shape: **fork the working MCP server and augment our own
copy.** The catalog/selection docs are preserved here as the design rationale for
the augments rather than as the deliverable itself.

## Why dcc-mcp is the right substrate

`dcc-mcp-blender` ships a real, working Blender MCP server with a typed skill
composition mechanism: a skill is a `SKILL.md` (frontmatter) + sibling
`tools.yaml` + `scripts/*.py` tool implementations using
`from dcc_mcp_core.skill import run_main, skill_entry`. New tools require **no
Python registration code** — the loader discovers `tools.yaml` per skill. This is
exactly the mechanism the Broadside selection needs: compose the bundled skills
that match our kept-tool set, and add Broadside-specific skill packages on top.

## Upstream sources (pinned)

| Source | Repo | What we keep | Status |
|---|---|---|---|
| DCC-MCP (runtime) | `dcc-mcp/dcc-mcp-core` → `Coldaine/dcc-mcp-core` | gateway, CLI, skill loader, runner contract | forked, adopted |
| DCC-MCP (Blender) | `dcc-mcp/dcc-mcp-blender` → `Coldaine/dcc-mcp-blender` | broad authoring/topology/UV/materials/nodes/animation/rigging/render/validation/assembly/interchange | forked, adopted; bundled skills kept as-is |
| Patryk | measured/assertion tools | ported into new `broadside-spatial-truth` skill (this fork) | **functional** (10 tools) |
| Official Blender Lab | `search_api_docs` / `get_python_api_docs` / `search_manual_docs` + `.blend` inspection | run alongside (separate MCP server); referenced from Broadside skills when custom Python is needed | external, not forked |
| Seehiong | record/replay mechanism only | deferred — port after confirming replay detects command failures | deferred |
| Ahujasid | optional external asset providers (Poly Haven / Sketchfab / Hyper3D / Hunyuan3D) | deferred — evaluate as asset-source tools when needed | deferred |
| Sandraschi | VSE / VRM / Gaussian-splat specialist features | deferred — only when those become relevant | deferred |

Full per-tool and per-skill detail: `SELECTION.md`, `mcp-tools.yaml`,
`skills.yaml`.

## Delivered in this augment (PR #1)

1. `docs/broadside/` — the selection rationale (folded from the abandoned
   docs-only repo): `SELECTION.md`, `mcp-tools.yaml`, `skills.yaml`,
   `upstream-sources.md`.
2. `broadside-spatial-truth` — **functional** Broadside skill package: 10
   conformant tools (5 measure + 5 assert), real `bpy`/`mathutils`
   implementation with no-bpy fallback, compiles clean. This is the
   Patryk-derived differentiated layer.
3. Six scaffold Broadside skill packages (`broadside-component-modeling`,
   `broadside-ship-assembly`, `broadside-materials-and-texturing`,
   `broadside-articulation-and-rigging`, `broadside-visual-review`,
   `broadside-validation-and-publish`) — conformant `SKILL.md` frontmatter,
   honest `scaffold` status, composition map to bundled skills, no `tools.yaml`
   yet.
4. `AGENTS.md` — adoption posture, skill status table, conventions.

## Functional vs scaffold — honest

- **Functional today:** the forked server builds and runs (it is the upstream
  working MCP server); all bundled skills matching the DCC selection are
  present and working; `broadside-spatial-truth` is a complete, conformant,
  compiling skill package with real implementations.
- **Scaffold (structure complete, tools not yet authored):** the six
  consolidated Broadside skills. Each names the bundled skills it composes and
  the donor skills it consolidates; authoring their `tools.yaml` (composing
  bundled tools or thin `@skill_entry` wrappers) is the remaining work, bounded
  by `SELECTION.md`.

## Next steps

1. Author `tools.yaml` for `broadside-component-modeling` first (highest-value
   composition: meshes, modifiers, geometry nodes, scripting escape hatch).
2. Port Patryk relative-placement macros (`macro_relative_layout`,
   `macro_place_supported_pair`, `macro_align_part_with_contact`) into
   `broadside-ship-assembly`.
3. Wire the Official Blender Lab doc-search server alongside and reference it
   from Broadside skills that fall back to custom Python.
4. Sync upstream periodically; keep branch protection + PR flow.
