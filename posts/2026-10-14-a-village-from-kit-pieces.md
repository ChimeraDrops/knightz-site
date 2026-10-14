---
title: Dev Log #22: A village from kit pieces
date: 2026-10-14
---

Today the work moved from characters to buildings. The hub needs a hall, houses, workshops, a chapel and defences, and each one has to be built, burned, rebuilt and weathered over the seasons. Hand-modelling every building would not scale. So the buildings are now made from shared kit pieces that snap together on one grid.

## The plan

The full environment list now has 455 components in 22 kits, plus 85 sites that use them. Every piece follows the same rules:

- 1 unit is 1 metre, on a 0.5 m grid with 2.5 m wall bays.
- Building spans of 4, 5, 6 and 9 metres.
- Eaves at 3 m, or 4 m for the hall and the chapel.
- Roofs at 45 degrees, so the ridge height always follows from the span.

This is a change to the overall plan. The first art pass on the hub now starts from these kits, and the roadmap phase for it has started.

## Reference images on a local generator

A local image generator now runs on the desktop GPU. It makes a form sheet and a flat material sheet for each kit piece from a written prompt. Only a model licensed for commercial use is in the pipeline. A fast four-step mode makes four images in about 16 seconds with the same quality as a full 30-step run.

Two lessons from the first rounds. Proportions have to be written as ratios. Roof pieces come out as whole huts unless the prompt asks for a loose component with no walls.

Material sheets are turned into 2K tileable textures by a script that crops, flattens the lighting and blends the edges.

## Timber and daub

The first kit covers posts, beams, trusses, wattle and daub panels, doors, shutters and thatch, shingle and turf roofs. That is 116 meshes and about 38,000 triangles for the whole kit.

![All timber, wall, door and roof pieces](assets/img/gallery/devlog22_kit_pieces_1014.jpg)

A small longhouse, 12.5 by 6 metres with a hipped thatch roof, is the test building. It uses 88 pieces built from 20 meshes and comes to about 15,600 triangles.

![Small longhouse built from kit pieces in Blender](assets/img/gallery/devlog22_longhouse_blender_1014.jpg)

The inside is built too, with the roof frame and doors visible from the floor.

![Longhouse interior with the roof frame](assets/img/gallery/devlog22_longhouse_interior_1014.jpg)

## Into Unreal

All 116 pieces are in Unreal with Nanite, a lower level of detail and simple collision shapes. The engine's newer import path ignored the old collision settings, so the import script now sets them through the new pipeline.

![Longhouse wall and door in Unreal](assets/img/gallery/devlog22_longhouse_unreal_1014.jpg)

One master material drives every building surface. Sliders add weathering, rot, scorch and char, and snow that settles only on upward faces. Five states are ready for each material: weathered, snow, burned, charred and rotten. Swapping a building's state is a material swap with no new meshes.

![The same longhouse in new, weathered, snow, rotten and charred states](assets/img/gallery/devlog22_longhouse_states_1014.jpg)

The thatch hip end was over budget at up to 4,608 triangles. The rebuilt version is 268 triangles and now shows the hip rafters from inside.

## Palisade

The palisade kit has 13 pieces: straight runs, corners, ends, a hurdle repair, a walkway with a ladder, a double gate with separate leaves that can open, a gate tower, a watch tower, a stake row, a ditch and bank, a ditch bridge and a barricade. Breached runs and broken gate leaves are separate meshes so they can be swapped in after an attack.

![Palisade enclosure test in Unreal](assets/img/gallery/devlog22_palisade_1014.jpg)

## Build stages

Buildings will go up in front of the player, so there is a kit for the work itself: a staked outline, postholes with spoil heaps, scaffolds, timber stacks, wattle bundles, a daub pit, thatch stacks, shear legs for lifting, a carpenter's bench, trestles and a mortar trough. Dug features sit slightly above ground so they read on any terrain.

![A build site with outline, postholes, scaffold and materials](assets/img/gallery/devlog22_build_site_1014.jpg)

## Stone and reused Roman masonry

The stone kit uses old Roman stone and tile in new walls. The masonry pattern is real geometry: sandstone blocks sit proud of the mortar and bands of thin red tile run every third course. Arches have radiating tile voussoirs. The kit covers walls with doors and splayed windows, gables with a bellcote, a chancel arch, plinths, steps, a gatehouse passage, ruined walls in three heights and dry stone field walls.

![Stone chapel walls with tile bands and an arched door](assets/img/gallery/devlog22_stone_chapel_1014.jpg)

## Sixteen buildings

A layout script now writes a complete building from a short description: size, eave height, which bays have doors or windows, wall type, floor type and roof ends. Each building is saved as its own level instance in Unreal, ready to place.

The first set:

- An aisled hall, 25 by 9 metres, with carved door lintel and smoke vents
- Three longhouses, 12.5, 17.5 and 22.5 metres long
- A stone chapel with chancel and bellcote
- A smithy with an open front
- Two granaries raised on stone staddles
- Two byres with bare wattle walls
- A storehouse, salting house, bakehouse, brewhouse and infirmary

![Aisled hall and longhouse in Unreal](assets/img/gallery/devlog22_hall_longhouses_1014.jpg)

![Chapel, granaries, byres and workshops placed as level instances](assets/img/gallery/devlog22_chapel_village_1014.jpg)

## Next

The watermill, the patched and damaged mesh variants, and prop kits for the forge, oven, vats and racks that fill these shells. Attacks for every weapon set are still queued on the animation side.
