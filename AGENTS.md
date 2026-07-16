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
- `src/dcc_mcp_blender/skills/broadside-*` — the Broadside skill packages.

## Broadside skill packages — status

| Skill | Status | Notes |
|---|---|---|
| `broadside-spatial-truth` | **functional** | 10 conformant tools, real bpy implementation, compiles. Patryk-derived measurement + assertion layer (the differentiated capability). |
| `broadside-component-modeling` | scaffold | Consolidates Arjun hard-surface + vehicle-artist + prop-artist; composes bundled `blender-mesh`/`blender-mesh-ops`/`blender-geometry`/`blender-geometry-nodes`/`blender-scripting`. Author `tools.yaml` per `broadside-spatial-truth`. |
| `broadside-ship-assembly` | scaffold | Consolidates Arjun scene-assembly + ProfRino blender-assembly; composes bundled `blender-scene-assembly`/`blender-collection`/`blender-objects` + Patryk relative-placement macros. |
| `broadside-materials-and-texturing` | scaffold | Consolidates Arjun materials + texture-workflow; composes bundled `blender-materials`/`blender-shader-nodes`/`blender-material-library`/`blender-uv-ops`/`blender-texture-bake`. |
| `broadside-articulation-and-rigging` | scaffold | Consolidates Arjun rigging + animation (rewritten off character assumptions); composes bundled `blender-rigging`/`blender-animation`/`blender-pose-library`. |
| `broadside-visual-review` | scaffold | Consolidates Arjun lighting + camera-cinematography + rendering + lookdev; composes bundled `blender-lighting`/`blender-light-rig`/`blender-camera`/`blender-render`. |
| `broadside-validation-and-publish` | scaffold | Consolidates Arjun qa-review + export-pipeline; composes bundled `blender-validation`/`blender-pipeline`/`blender-interchange` + `broadside-spatial-truth`. |

The bundled upstream skills (e.g. `blender-scene`, `blender-objects`,
`blender-mesh`, `blender-validation`, `blender-scene-assembly`, …) are already
functional and map almost 1:1 onto the DCC selection in
`docs/broadside/mcp-tools.yaml` — those are **kept as-is**. The Broadside
scaffold skills compose them and add the Broadside-specific spatial-truth layer.

## Conventions

- New Broadside tools conform to the format proven in
  `broadside-spatial-truth`: `SKILL.md` (dcc-mcp frontmatter) + `tools.yaml`
  + `scripts/<tool>.py` using `from dcc_mcp_core.skill import run_main, skill_entry`.
- Honest status labels in each `SKILL.md`: `scaffold` vs `functional`.
- Do not silently delete or rewrite upstream bundled skills; compose them.
