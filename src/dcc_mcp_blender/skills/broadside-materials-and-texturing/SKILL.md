---
name: broadside-materials-and-texturing
description: "PBR materials and texture baking for steel, wood decking, brass, canvas, weathering."
license: "MIT"
allowed-tools: ["Bash", "Read"]
metadata:
  dcc-mcp:
    dcc: blender
    version: "0.1.0"
    tags: [blender, broadside]
    intent: "PBR materials and texture baking for steel, wood decking, brass, canvas, weathering."
    recall-context:
      app_type: blender
      domain: broadside
      workflow_stage: scaffold
      task_category: composition
    side-effects:
      modifies: true
      creates: true
      targets: [scene, asset]
    produces: [asset, scene_state]
    requires: []
    tools: tools.yaml
---

# broadside-materials-and-texturing

**Status: scaffold — port per docs/broadside/SELECTION.md and docs/broadside/skills.yaml.**

Rewrites Arjun materials + texture-workflow for Broadside. Composes blender-materials, blender-material-library, blender-shader-nodes, blender-node-graph, blender-uv-ops, blender-texture-bake.

This skill is a consolidation target, not yet a concrete tool package. To make it
functional, author `tools.yaml` (referencing bundled skill tools via composition
or thin `@skill_entry` wrappers) per the format proven in
`broadside-spatial-truth`, and record the kept tool set from
`docs/broadside/mcp-tools.yaml`.
