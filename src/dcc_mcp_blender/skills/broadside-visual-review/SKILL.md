---
name: broadside-visual-review
description: "Hero-image and orthographic review renders as part of verification."
license: "MIT"
allowed-tools: ["Bash", "Read"]
metadata:
  dcc-mcp:
    dcc: blender
    version: "0.1.0"
    tags: [blender, broadside]
    intent: "Hero-image and orthographic review renders as part of verification."
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

# broadside-visual-review

**Status: scaffold — port per docs/broadside/SELECTION.md and docs/broadside/skills.yaml.**

Consolidates Arjun lighting + camera-cinematography + rendering + lookdev into one Broadside review/render skill. Composes blender-camera, blender-lighting, blender-light-rig, blender-render.

This skill is a consolidation target, not yet a concrete tool package. To make it
functional, author `tools.yaml` (referencing bundled skill tools via composition
or thin `@skill_entry` wrappers) per the format proven in
`broadside-spatial-truth`, and record the kept tool set from
`docs/broadside/mcp-tools.yaml`.
