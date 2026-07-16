---
name: broadside-component-modeling
description: "Component-level modeling for warship parts (turrets, directors, boats, cranes, AA mounts)."
license: "MIT"
allowed-tools: ["Bash", "Read"]
metadata:
  dcc-mcp:
    dcc: blender
    version: "0.1.0"
    tags: [blender, broadside]
    intent: "Component-level modeling for warship parts (turrets, directors, boats, cranes, AA mounts)."
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

# broadside-component-modeling

**Status: scaffold — port per docs/broadside/SELECTION.md and docs/broadside/skills.yaml.**

Rewrites Arjun hard-surface + vehicle-artist + prop-artist for Broadside. Composes the blender-mesh, blender-mesh-ops, blender-geometry, blender-geometry-nodes, and blender-scripting bundled skills; MCP references point at the selected DCC tools (see docs/broadside/mcp-tools.yaml).

This skill is a consolidation target, not yet a concrete tool package. To make it
functional, author `tools.yaml` (referencing bundled skill tools via composition
or thin `@skill_entry` wrappers) per the format proven in
`broadside-spatial-truth`, and record the kept tool set from
`docs/broadside/mcp-tools.yaml`.
