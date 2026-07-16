---
name: broadside-validation-and-publish
description: "Outer quality gate: spatial truth + technical readiness + visual checks + publish package."
license: "MIT"
allowed-tools: ["Bash", "Read"]
metadata:
  dcc-mcp:
    dcc: blender
    version: "0.1.0"
    tags: [blender, broadside]
    intent: "Outer quality gate: spatial truth + technical readiness + visual checks + publish package."
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

# broadside-validation-and-publish

**Status: scaffold — port per docs/broadside/SELECTION.md and docs/broadside/skills.yaml.**

Rewrites Arjun qa-review + export-pipeline for Broadside. Composes broadside-spatial-truth, blender-validation, blender-pipeline, blender-export-preset, blender-shot-export. Patryk spatial assertions + DCC technical validators + rendered visual checks together.

This skill is a consolidation target, not yet a concrete tool package. To make it
functional, author `tools.yaml` (referencing bundled skill tools via composition
or thin `@skill_entry` wrappers) per the format proven in
`broadside-spatial-truth`, and record the kept tool set from
`docs/broadside/mcp-tools.yaml`.
