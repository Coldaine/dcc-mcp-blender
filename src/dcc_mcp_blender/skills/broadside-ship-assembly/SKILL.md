---
name: broadside-ship-assembly
description: "Modular ship assembly from linked/appended sub-assemblies."
license: "MIT"
allowed-tools: ["Bash", "Read"]
metadata:
  dcc-mcp:
    dcc: blender
    version: "0.1.0"
    tags: [blender, broadside]
    intent: "Modular ship assembly from linked/appended sub-assemblies."
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

# broadside-ship-assembly

**Status: scaffold — port per docs/broadside/SELECTION.md and docs/broadside/skills.yaml.**

Rewrites Arjun scene-assembly + ProfRino blender-assembly for Broadside. Composes blender-scene-assembly, blender-collection, blender-interchange, blender-import-to-scene, plus broadside-spatial-truth for seating/contact verification. Enforces the hull/superstructure/turrets/boats/aircraft/materials/hero-scene .blend split.

This skill is a consolidation target, not yet a concrete tool package. To make it
functional, author `tools.yaml` (referencing bundled skill tools via composition
or thin `@skill_entry` wrappers) per the format proven in
`broadside-spatial-truth`, and record the kept tool set from
`docs/broadside/mcp-tools.yaml`.
