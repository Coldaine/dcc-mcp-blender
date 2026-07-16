# Coldaine fork of dcc-mcp-blender — Broadside adoption

This is a **fork of `dcc-mcp/dcc-mcp-blender`** (MIT), adopted as the Project
Broadside Blender MCP substrate. We did not design a framework or port code; we
**forked the working MCP server and augmented our own copy** with Broadside
skill packages and the selection rationale that decided which upstream tools
and skills survive the cut.

## Fork posture

- Upstream: `dcc-mcp/dcc-mcp-blender` (sync from upstream regularly; this is an
  adoption, not a throwaway).
- Runtime dependency: `dcc-mcp-core` — also forked at `Coldaine/dcc-mcp-core`
  so we own the gateway/CLI/loader supply chain and can pin a known-good version.
- Branch protection is **on** for `main`; changes land via PR. Issues enabled.
- Treat this like a maintained project, not a docs repo.

## Where the Broadside work lives

- `docs/broadside/SELECTION.md` — the authoritative tool/skill selection
  decision: every kept tool, every rejected source, the reason each survives.
- `docs/broadside/mcp-tools.yaml` — machine-readable inventory of every kept
  MCP tool, grouped by source/family/workflow stage.
- `docs/broadside/skills.yaml` — Tier 1 / Tier 2 / discard donor skills plus
  the six consolidated Broadside skills.
- `docs/broadside/upstream-sources.md` — wiring doc: each upstream repo pinned
  with what's kept, what's rejected, and status.
- `src/dcc_mcp_blender/skills/broadside-spatial-truth` — the one functional
  Broadside skill package (the others are documented targets, not yet built).

## Broadside skill packages — status

| Skill | Status | Notes |
|---|---|---|
| `broadside-spatial-truth` | **functional** | 10 conformant tools, real bpy implementation, compiles. Patryk-derived measurement + assertion layer (the differentiated capability). |

`broadside-spatial-truth` is the only Broadside skill package in-tree. The six
consolidated Broadside skills (component-modeling, ship-assembly,
materials-and-texturing, articulation-and-rigging, visual-review,
validation-and-publish) are a **design target only** — their donor→target
mapping lives in `docs/broadside/skills.yaml` and `docs/broadside/SELECTION.md`.
Empty placeholder directories for them were removed rather than left as dead
`tools: []` skills; author each as a real package (per the pattern below) when
it is actually built.

The bundled upstream skills (e.g. `blender-scene`, `blender-objects`,
`blender-mesh`, `blender-validation`, `blender-scene-assembly`, …) are already
functional and map almost 1:1 onto the DCC selection in
`docs/broadside/mcp-tools.yaml` — those are **kept as-is**. Until the
consolidated Broadside skills are built, compose those bundled skills directly
and add the Broadside-specific spatial-truth layer.

## Conventions

- New Broadside tools conform to the format proven in
  `broadside-spatial-truth`: `SKILL.md` (dcc-mcp frontmatter) + `tools.yaml`
  + `scripts/<tool>.py` using `from dcc_mcp_core.skill import run_main, skill_entry`.
- Do not commit empty placeholder skills (`tools: []`). A Broadside skill lands
  only when it has a real `tools.yaml` and scripts; until then it stays a
  documented target in `docs/broadside/`.
- Do not silently delete or rewrite upstream bundled skills; compose them.
