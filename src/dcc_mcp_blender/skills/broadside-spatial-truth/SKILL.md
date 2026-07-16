---
name: broadside-spatial-truth
description: "Geometric measurement and assertion tools for warship assembly verification"
license: "MIT"
allowed-tools: ["Bash", "Read"]
metadata:
  dcc-mcp:
    dcc: blender
    version: "0.1.0"
    tags: [blender, broadside, spatial, measurement, assertion, validation, assembly]
    search-hint: "measure distance, dimensions, gap, overlap, alignment; assert contact, dimensions, containment, symmetry, proportion"
    search-aliases: [barbette seating, barrel parallelism, director centering, mirror match, armor gap, containment check, geometric truth]
    intent: "Verify warship assembly facts in world space — turret-on-barbette seating, barrel parallelism and equal length, director centering, superstructure containment, port/starboard mirror match, unintended armor gaps."
    recall-context:
      app_type: blender
      domain: geometric-truth
      workflow_stage: validation
      task_category: assertion
    preconditions:
      - type: software
        name: blender
        version: ">=4.0"
      - type: scene_state
        predicate: has_open_scene
    side-effects:
      modifies: false
      creates: false
      targets: []
    produces: [measurement, assertion_result]
    requires: []
    tools: tools.yaml
---

# broadside-spatial-truth

The differentiated geometric-truth layer for Project Broadside. These tools
reason over world-space bounding boxes, object origins, and local axis
directions so the agent can verify assembly facts that matter for a warship:

- Does the turret sit on the barbette? (`assert_contact`)
- Are both barrels the same length? (`assert_dimensions`)
- Are the barrels parallel? (`measure_alignment`)
- Is the director centered? (`measure_distance` / `assert_containment`)
- Is the superstructure within the deck footprint? (`assert_containment`)
- Do mirrored port/starboard assemblies match? (`assert_symmetry`)
- Is there an unintended gap between armor sections? (`measure_gap`)
- Are components overlapping rather than merely appearing adjacent? (`measure_overlap`)

This is the Patryk-derived spatial layer. It complements `blender-validation`
(technical export readiness) rather than duplicating it: `blender-validation`
asks "is this asset ready to export?"; `broadside-spatial-truth` asks "are
these parts spatially correct relative to each other?".

All tools are read-only and idempotent. Implementation lives in
`scripts/spatial_lib.py`; each tool script is a thin `@skill_entry` wrapper.
