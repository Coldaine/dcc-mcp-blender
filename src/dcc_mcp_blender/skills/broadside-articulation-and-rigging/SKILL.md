---
name: broadside-articulation-and-rigging
description: "Mechanical rigging and movable assemblies (turret traverse, barrel elevation, directors, davits)."
license: "MIT"
allowed-tools: ["Bash", "Read"]
metadata:
  dcc-mcp:
    dcc: blender
    version: "0.1.0"
    tags: [blender, broadside]
    intent: "Mechanical rigging and movable assemblies (turret traverse, barrel elevation, directors, davits)."
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

# broadside-articulation-and-rigging

**Status: scaffold — port per docs/broadside/SELECTION.md and docs/broadside/skills.yaml.**

Rewrites Arjun rigging + animation away from character assumptions. Composes blender-rigging, blender-pose-library, blender-animation; prefers parenting/constraints/drivers/object animation over armatures where appropriate.

This skill is a consolidation target, not yet a concrete tool package. To make it
functional, author `tools.yaml` (referencing bundled skill tools via composition
or thin `@skill_entry` wrappers) per the format proven in
`broadside-spatial-truth`, and record the kept tool set from
`docs/broadside/mcp-tools.yaml`.
