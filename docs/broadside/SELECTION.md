# Broadside Blender toolkit — selection

Authoritative selection of the MCP tools and skills kept for Project Broadside's
Blender-based warship construction pipeline. This is the answer to two questions:

1. Which existing MCP tools do we actually keep?
2. Which skills do we cherry-pick?

And the reason each survives the cut.

The problem this resolves: a **selection** problem, not an architecture project. We do
not need to design a framework, port code, or debate composability. We keep the
specific tools and skills, and state why each is the best choice for Broadside.

- Tool inventory (machine-readable): [`portfolio/mcp-tools.yaml`](portfolio/mcp-tools.yaml)
- Skill inventory (machine-readable): [`portfolio/skills.yaml`](portfolio/skills.yaml)
- Upstream source wiring (repos, keep/reject/status): [`docs/upstream-sources.md`](docs/upstream-sources.md)

---

## Part 1 — MCP tool portfolio

### 1. Scene and object management — DCC-MCP

Keep: `new_scene`, `open_scene`, `save_scene`, `get_scene_info`, `get_session_info`,
`list_objects`, `create_object`, `delete_object`, `duplicate_object`, `rename_object`,
`parent_object`, `group_objects`, `set_visibility`, `get_object_info`,
`get_bounding_box`, `get_selection`, `set_selection`, `find_by_pattern`,
`create_collection`, `link_to_collection`, `list_collections`.

**Why:** this is a coherent, typed object-management surface. Broadside models will
have hundreds or thousands of named components, assemblies, collections, weapon
systems, superstructure sections, and LOD variants. We need predictable hierarchy
operations — not raw `bpy` for routine scene management.

### 2. Hard-surface modeling and topology — DCC-MCP

Keep: `add_modifier`, `apply_modifier`, `list_modifiers`, `get_mesh_info`,
`get_poly_count`, `cleanup_mesh`, `triangulate_mesh`, `separate_mesh`,
`combine_meshes`, `merge_vertices`, `extract_faces`, `mirror_mesh`,
`select_by_material`.

Also keep the arbitrary escape hatch: `execute_python`, `execute_script_file`.

**Why:** DCC provides the best broad typed substrate here. These tools cover ordinary
modifier and topology work, while `execute_python` handles operations that are too
specialized for the typed surface.

Do not require every modeling operation to have its own MCP tool. Complex hull plating,
curved deck sheer, turret housings, gun barrels, and procedural detailing will often be
better implemented as reviewed Blender Python called through the escape hatch.

### 3. Spatial measurement and geometric truth — Patryk

These are the most important tools Patryk contributes:

`scene_measure_distance`, `scene_measure_dimensions`, `scene_measure_gap`,
`scene_measure_alignment`, `scene_measure_overlap`, `scene_assert_contact`,
`scene_assert_dimensions`, `scene_assert_containment`, `scene_assert_symmetry`,
`scene_assert_proportion`.

Keep supporting inspection tools: `scene_get_bounding_box`, `scene_get_origin_info`,
`scene_get_hierarchy`, `scene_view_diagnostics`, `scene_snapshot_state`,
`scene_compare_snapshot`.

**Why:** this is the strongest differentiated capability found anywhere in the audit.

These tools let the agent verify things that matter for a warship:

- Does the turret sit on the barbette?
- Are both barrels the same length?
- Are the barrels parallel?
- Is the director centered?
- Is the superstructure contained within the deck footprint?
- Do mirrored port and starboard assemblies match?
- Is there an unintended gap between armor sections?
- Are components overlapping rather than merely appearing adjacent?

This is not generic validation. It is explicit geometric reasoning.

### 4. Relative placement helpers — Patryk

Keep: `macro_relative_layout`, `macro_place_supported_pair`,
`macro_align_part_with_contact`.

**Why:** these directly address assembly problems. They are more useful for Broadside
than generic "create object" macros because they encode relationships between
components.

Use them for: seating turrets on barbettes; aligning gun barrels with trunnions;
positioning rangefinders relative to bridges; mounting boats on davits; aligning
directors, masts, and radar arrays; placing repeated secondary batteries.

### 5. Materials and shader graphs — DCC-MCP

Keep: `create_material`, `assign_material`, `set_material_color`, `list_materials`,
`delete_material`, `list_material_nodes`, `set_principled_input`, `list_node_trees`,
`list_nodes`, `create_node`, `delete_node`, `list_node_sockets`, `connect_nodes`,
`disconnect_nodes`, `list_node_links`, `set_node_input`, `get_node_value`,
`create_material_with_nodes`, `assign_texture_node`, `set_principled_inputs`.

Also: `get_shader_assignment`, `get_material_connections`, `assign_texture`,
`list_images`, `reload_image`, `set_color_management`.

**Why:** DCC's tool family is more complete and consistently typed than the
alternatives. Broadside needs reusable steel, painted steel, wood decking, glass,
brass, canvas, weathering masks, rust, soot, and emissive/navigation-light materials.

### 6. UVs and texture baking — DCC-MCP

Keep: `list_uv_maps`, `create_uv_map`, `delete_uv_map`, `copy_uv_map`, `get_uv_info`,
`get_uv_islands`, `project_uvs`, `unwrap_uvs`, `pack_uvs`, `normalize_uvs`.

And: `list_bake_targets`, `bake_textures`, `bake_ambient_occlusion`, `bake_lighting`,
`transfer_maps`.

**Why:** this is complete enough to support actual asset preparation rather than merely
assigning procedural colors.

### 7. Geometry Nodes — DCC-MCP

Keep: `add_geometry_nodes_modifier`, `list_geometry_nodes_modifiers`,
`create_geometry_node_group`, `assign_geometry_node_group`,
`set_geometry_node_modifier_input`, `evaluate_geometry_nodes_info`.

**Why:** Geometry Nodes is likely essential for repeated warship detail: portholes,
rivets, railings, ladders, deck fittings, ventilation grilles, antenna arrays,
repeated secondary armament, procedural plating seams. We should prefer procedural
instancing over manually creating thousands of repeated objects.

### 8. Rigging, constraints, and movable components — DCC-MCP

Keep: `create_armature`, `create_bone`, `mirror_bones`, `add_constraint`,
`set_constraint_properties`, `bind_mesh_to_armature`, `add_shape_key`, `set_driver`.

For non-character mechanical animation, also keep: `set_keyframe`, `set_frame_range`,
`get_frame_range`, `set_current_frame`, `get_keyframes`, `delete_keyframes`,
`bake_animation`.

**Why:** Project Broadside needs movable assemblies, not merely static meshes: turret
traverse, barrel elevation, rangefinder rotation, crane movement, radar rotation, gun
directors, folding aircraft wings, boat davits, doors and hatches. Armatures may not
always be the ideal mechanism; parenting, constraints, drivers, and object animation
will often be more appropriate. These tools cover both approaches.

### 9. Cameras, lighting, and rendering — DCC-MCP

Keep: `create_camera`, `set_active_camera`, `set_camera_properties`, `list_cameras`,
`create_light`, `set_light_properties`, `list_lights`, `set_world_background`,
`create_three_point_light_rig`, `create_area_softbox`, `create_hdri_world`,
`aim_light_at_object`, `set_render_view_transform`, `get_lighting_summary`,
`set_render_settings`, `get_render_info`, `capture_viewport`, `render_scene`.

**Why:** this is the strongest complete look-development and render family. For
Broadside, visual review is part of verification. The agent must repeatedly produce:
orthographic side/top/front reviews; hero-angle renders; silhouette checks; material
previews; lighting-neutral geometry inspections; close-up turret and superstructure
reviews.

### 10. Validation and publishing — DCC-MCP

Keep: `run_scene_checks`, `validate_mesh`, `validate_materials`, `validate_animation`,
`validate_export_readiness`, `get_validation_report`.

Also: `get_asset_metadata`, `tag_asset_metadata`, `clear_asset_metadata`,
`set_project_context`, `create_publish_manifest`, `prepare_publish_package`.

**Why:** Patryk's geometric assertions and DCC's production validation solve different
problems. Patryk: "Are these parts spatially correct?" DCC: "Is this asset technically
ready to export or publish?" We want both.

### 11. Scene assembly and external references — DCC-MCP

Keep: `merge_scene`, `append_blend`, `link_blend`, `list_view_layers`,
`create_view_layer`, `set_active_view_layer`, `list_external_references`.

**Why:** the final ships should not live as one monolithic `.blend` built by one endless
agent session. We need modular assemblies: `hull.blend`, `superstructure.blend`,
`turrets.blend`, `boats.blend`, `aircraft.blend`, `materials.blend`, `hero-scene.blend`.
These tools support that architecture.

### 12. Import/export — DCC-MCP

Keep: `import_file`, `import_fbx`, `import_obj`, `import_usd`, `export_gltf`,
`export_usd`, `export_alembic`, `export_fbx`, `export_obj`, `batch_export`,
`import_to_scene`.

**Why:** broad format coverage and typed options. Adequate for Blender-centered
production and downstream rigging/render workflows.

### 13. Blender API and manual search — Official Blender Lab MCP

Keep: `search_api_docs`, `get_python_api_docs`, `search_manual_docs`.

Potentially also keep: `get_blendfile_summary_datablocks`,
`get_blendfile_summary_missing_files`, `get_blendfile_summary_of_linked_libraries`,
`get_blendfile_summary_path_info`.

**Why:** this is the official implementation's strongest unique value. It bundles or
searches Blender documentation and provides useful file-level inspection. These tools
reduce hallucinated `bpy` APIs and are valuable whenever we fall back to custom Python.
We do not need the official server as the primary authoring runtime.

### 14. Record/replay — Seehiong, selectively

Keep the session recording and replay mechanism, not necessarily its entire tool
catalog. The useful ideas are: record commands; save a session; reset the scene; replay
commands; edit or inspect the recorded sequence.

**Why:** deterministic reproduction is extremely useful.

However, because Seehiong has the explicit `None → success` defect, we would not rely on
its general tool wrappers as authoritative. Use its replay mechanism only after
confirming replay detects command failures.

---

## Part 2 — What we would NOT select

**From Ahujasid** — do not select its generic authoring layer as the foundation.
Potentially keep only specialized integrations if we need them: Poly Haven
search/download, Sketchfab search/download, Hyper3D, Hunyuan3D. These should be
evaluated as asset-source tools, not modeling tools.

**From Sandraschi** — do not adopt its broad 48-tool surface as the default. Too many
operations are packed into large composite tools, and the process architecture is still
stabilizing. Potentially mine: VSE/video tooling, VRM tooling, Gaussian-splat tooling,
dashboard and monitoring ideas — only when those become relevant.

**From Patryk** — do not select its entire 185-tool legacy surface merely because the
truth layer is excellent. Select the spatial, assertion, snapshot, and guided-repair
tools. Those are its differentiated strengths.

**From DCC** — do not blindly load all 242 tools into the agent context at once. Select
the coherent skill families above and progressively expose them by workflow stage. That
is not "composability architecture." It is simply avoiding a 242-tool context dump.

---

## Part 3 — Skills to cherry-pick

### Tier 1 — definitely keep

**hard-surface (Arjun)** — directly relevant to turrets, armor, superstructures, guns,
directors, vents, and mechanical assemblies. Keep its: modifier sequencing;
non-destructive construction; bevel and normal discipline; panel and recess workflows;
topology review; hard-surface validation. Rewrite its MCP references to use the selected
DCC and Patryk tools.

**vehicle-artist (Arjun)** — ships are large mechanical vehicles with repeated
assemblies, functional hierarchy, manufactured surfaces, and scale-sensitive detailing.
Keep: primary/secondary/tertiary form planning; functional component hierarchy;
mechanical articulation; repeated-detail discipline; exterior material breakup. Remove
assumptions specific to wheeled vehicles.

**prop-artist (Arjun)** — many ship components are effectively complex props: gun
mounts, searchlights, rangefinders, boats, cranes, AA mounts, radar assemblies, anchors
and capstans. Useful for component-level asset production.

**scene-assembly (Arjun)** — directly relevant to modular ship construction and final
scene integration. Keep: reference/link/append strategy; collection organization;
naming and ownership; assembly validation; avoiding monolithic files.

**materials and texture-workflow (Arjun)** — needed for disciplined PBR construction,
texel consistency, material reuse, and texture verification.

**lighting, camera-cinematography, rendering, lookdev (Arjun)** — collectively provide
the hero-image workflow rather than merely technical scene output. These should probably
become one Broadside-specific review/render skill rather than four separate agent
activations.

**rigging and animation (Arjun)** — useful for movable turrets, guns, directors,
cranes, and radar assemblies. Rewrite away from character-centric assumptions.

**qa-review (Arjun)** — use it as the outer quality-review workflow, calling: Patryk
spatial assertions; DCC technical validators; rendered visual checks.

**blender-assembly (ProfRino)** — keep the good parts: explicit connection map before
geometry; deliberate overlap/contact planning; full-dimension versus half-extent
awareness; verification of visible gaps; construction helpers for parts spanning two
known points. Do not preserve its absolute rules that every directional cylinder must
use `bmesh` or every cube must use `size=2`.

### Tier 2 — useful with rewriting

- **environment-artist** — ocean, docks, shipyard, sky, haze, and hero-scene context —
  not for core ship geometry.
- **procedural-modeling** — repeated fittings, plating, railings, ladders, rivets, and
  vents.
- **asset-optimization** — later, for viewport performance, render complexity, and
  export optimization.
- **lod-pipeline** — useful when we need multiple ship representations or real-time
  deployment.
- **export-pipeline** — useful, but should be rewritten specifically around our required
  deliverables.
- **set-dressing** — crew-scale objects, deck equipment, ropes, crates, boats, aircraft,
  and shipyard scenes.
- **compositing** — final hero renders, atmospheric effects, muzzle flashes, ocean haze,
  and presentation.

### Skills to discard or defer

Do not cherry-pick dozens of style wrappers merely because they exist: horror variants,
anime, chibi, voxel, pixel art, manga, cozy, dreamcore, mascot horror, retro-console
styles, genre-game wrappers. They do not contribute to realistic, production-grade
historical warship construction.

Also defer: character-artist, creature-artist, hair-groom, facial animation, most
gameplay-genre skills, VR-specific skills, Unreal/Unity/Godot export skills — unless
those targets become real requirements.

---

## Part 4 — The final selected set

### MCP tool sources

| Source | What we keep |
| --- | --- |
| DCC-MCP | Broad authoring, topology, UV, materials, nodes, animation, rigging, render, validation, assembly, interchange |
| Patryk | Measurements, geometric assertions, snapshots, comparison, relative placement |
| Official Blender Lab | API/manual documentation search and `.blend` inspection |
| Seehiong | Record/replay mechanism only, subject to failure detection |
| Ahujasid | Optional external asset providers only |
| Sandraschi | Deferred specialist features such as VSE, VRM, or Gaussian splats |

### Skills — keep and rewrite, then consolidate

Keep and rewrite: hard-surface, vehicle-artist, prop-artist, scene-assembly, materials,
texture-workflow, procedural-modeling, rigging, animation, lighting,
camera-cinematography, rendering, lookdev, qa-review, export-pipeline, ProfRino's
blender-assembly.

Consolidate into approximately six Broadside skills:

1. `broadside-component-modeling`
2. `broadside-ship-assembly`
3. `broadside-materials-and-texturing`
4. `broadside-articulation-and-rigging`
5. `broadside-visual-review`
6. `broadside-validation-and-publish`

That is the answer: these exact tools, these exact skills, and the specific reason each
survives the cut.
