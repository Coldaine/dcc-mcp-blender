# Upstream sources — wiring

This is the "wiring": each repo the Broadside Blender toolkit draws from, what we keep,
what we reject, and the verification status of the upstream reference. The tool/skill
selections themselves live in [`../SELECTION.md`](../SELECTION.md) and the
machine-readable inventories in [`../portfolio/`](../portfolio/).

Verification status legend:

- **verified** — upstream repo located and confirmed by name/tooling match during the
  2026-07-16 audit.
- **characterized** — identified by its distinguishing tool/skill set; exact canonical
  code repo to be confirmed by the original audit author (the selection does not depend
  on the URL).

---

## MCP tool sources

### DCC-MCP — primary authoring substrate
- **Upstream:** https://github.com/loonghao/dcc-mcp-blender
- **Status:** verified
- **Keep:** scene & object management; hard-surface/topology + `execute_python` escape
  hatch; materials & shader graphs; UVs & baking; Geometry Nodes; rigging/constraints/
  animation; cameras/lighting/render; validation & publishing; scene assembly &
  external refs; import/export. (Full per-family lists in
  [`../portfolio/mcp-tools.yaml`](../portfolio/mcp-tools.yaml).)
- **Reject:** do not blindly load all ~242 tools into context at once. Progressively
  expose coherent families by workflow stage.
- **Role:** the broad, consistently typed surface for routine work. The official server
  is NOT the primary authoring runtime; DCC is.

### Patryk — geometric truth layer
- **Upstream:** https://github.com/PatrykIti/blender-ai-mcp
- **Status:** verified
- **Keep:** measurements (`scene_measure_*`), assertions (`scene_assert_*`), supporting
  inspection (`scene_get_bounding_box`, `scene_get_origin_info`, `scene_get_hierarchy`,
  `scene_view_diagnostics`, `scene_snapshot_state`, `scene_compare_snapshot`), and
  relative placement macros (`macro_relative_layout`,
  `macro_place_supported_pair`, `macro_align_part_with_contact`).
- **Reject:** do not adopt the entire ~185-tool legacy surface. Keep only the spatial,
  assertion, snapshot, and guided-repair tools — its differentiated strengths.
- **Role:** the strongest differentiated capability in the audit. "Are these parts
  spatially correct?"

### Official Blender Lab MCP — documentation & .blend inspection
- **Upstream:** Blender Lab official MCP server (Blender Foundation / Blender Lab
  project). Reference: https://www.blender.org?p=96198 — "MCP Server — Blender". Q1 2026
  activity report: https://www.blender.org?p=96267
- **Status:** characterized (official Blender Lab MCP; exact code distribution
  path/clone URL to confirm — install is via the Blender Lab repo + add-on per the
  blender.org page).
- **Keep:** `search_api_docs`, `get_python_api_docs`, `search_manual_docs`; potentially
  `get_blendfile_summary_datablocks`, `get_blendfile_summary_missing_files`,
  `get_blendfile_summary_of_linked_libraries`, `get_blendfile_summary_path_info`.
- **Reject:** do not use it as the primary authoring runtime.
- **Role:** reduce hallucinated `bpy` APIs; valuable whenever we fall back to custom
  Python. Bundles/searches Blender docs + file-level inspection.

### Seehiong — record/replay (selective)
- **Upstream:** https://github.com/seehiong/blender-mcp-n8n
- **Status:** verified (record/replay mechanism; general tool wrappers NOT used as
  authoritative).
- **Keep:** the session recording/replay mechanism only — record commands, save
  session, reset scene, replay commands, inspect the recorded sequence.
- **Reject:** general tool wrappers are not authoritative due to the explicit
  `None → success` defect.
- **Role:** deterministic reproduction. **Gating TODO:** adopt its replay only after
  confirming replay detects command failures.

### Ahujasid — optional external asset providers only
- **Upstream:** https://github.com/ahujasid/blender-mcp
- **Status:** verified
- **Keep (evaluate as asset-source tools, not modeling tools):** Poly Haven
  search/download, Sketchfab search/download, Hyper3D, Hunyuan3D.
- **Reject:** do not select its generic authoring layer as the foundation.
- **Role:** optional asset sourcing when those providers are actually needed.

### Sandraschi — deferred specialist features
- **Upstream:** https://github.com/sandraschi/blender-mcp
- **Status:** verified
- **Keep:** nothing now.
- **Mine later (only when relevant):** VSE/video tooling, VRM tooling, Gaussian-splat
  tooling, dashboard/monitoring ideas.
- **Reject:** do not adopt the broad ~48-tool composite surface as the default — too
  many operations packed into large composite tools, and the process architecture is
  still stabilizing.

---

## Skill sources

### Arjun skills — Tier 1 + Tier 2 donors
- **Upstream:** characterized — the donor skill set (hard-surface, vehicle-artist,
  prop-artist, scene-assembly, materials, texture-workflow, procedural-modeling,
  rigging, animation, lighting, camera-cinematography, rendering, lookdev, qa-review,
  export-pipeline, environment-artist, asset-optimization, lod-pipeline, set-dressing,
  compositing). Exact upstream skill-collection repo to be confirmed by the original
  audit author.
- **Status:** characterized
- **Keep & rewrite:** the Tier 1 and Tier 2 skills listed in
  [`../portfolio/skills.yaml`](../portfolio/skills.yaml), each rewritten to call the
  selected DCC + Patryk tools and de-scoped of character/wheeled-vehicle assumptions.
- **Discard/defer:** all style wrappers and the deferred categories listed in
  `skills.yaml` — they do not contribute to realistic, production-grade historical
  warship construction.
- **Role:** the human-authored production know-how that gets consolidated into the six
  Broadside skills.

### ProfRino — blender-assembly
- **Upstream:** https://github.com/ProfRino/Blender-MCP-Assemply-Skill
  (note: upstream repo name is spelled "Assemply")
- **Status:** verified
- **Keep:** explicit connection map before geometry; deliberate overlap/contact
  planning; full-dimension vs half-extent awareness; verification of visible gaps;
  construction helpers for parts spanning two known points.
- **Reject:** absolute rules that every directional cylinder must use `bmesh` or every
  cube must use `size=2`.
- **Role:** consolidates into `broadside-ship-assembly`.

---

## Net wiring

| Source | Repo | Role | Selection |
| --- | --- | --- | --- |
| DCC-MCP | `loonghao/dcc-mcp-blender` | primary authoring substrate | keep families, progressive exposure |
| Patryk | `PatrykIti/blender-ai-mcp` | geometric truth layer | keep spatial/assert/snapshot/placement |
| Blender Lab (official) | blender.org Blender Lab MCP | docs + .blend inspection | keep search/summary tools |
| Seehiong | `seehiong/blender-mcp-n8n` | deterministic reproduction | replay only, gated on failure detection |
| Ahujasid | `ahujasid/blender-mcp` | optional asset sourcing | providers only, evaluate-on-demand |
| Sandraschi | `sandraschi/blender-mcp` | deferred specialists | mine VSE/VRM/splats later |
| Arjun skills | (skill-collection repo — confirm) | production know-how | keep & rewrite Tier 1/2 |
| ProfRino | `ProfRino/Blender-MCP-Assemply-Skill` | assembly discipline | keep connection-map discipline |
