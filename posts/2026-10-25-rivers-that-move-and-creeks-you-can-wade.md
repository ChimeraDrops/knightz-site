---
title: Dev Log #32: Rivers that move, and creeks you can wade
date: 2026-10-25
---

Last time the rivers were reset to zero. This week the river and creek look was rebuilt, starting with the stretch where the Rea Brook joins the Severn. The water now reacts to the player, every river in the test area is filled, and the ground under the water is real creek bed.

![Wading the Rea Brook. The water reacts to the player and the creek bed shows through.](assets/img/gallery/devlog32_wading_creek_1024.jpg)

## The look

Several rounds of review shaped the water. Early versions blinked like traffic lights, showed a milky glare everywhere, ran in slow motion, looked like sheet metal and striped like a racetrack.

The approved version carries ripples and shapes downstream, so they change as they travel. On a river scale they move like slow lava lamp blobs. The brook runs faster, over rocks, with riffles. Where it pours into the Severn, the foam fans out downstream.

![Where the Rea Brook meets the Severn](assets/img/gallery/devlog32_confluence_1024.jpg)

## Three ways to make water move

Three test maps were built on the same real terrain:

- Plain animated water.
- Animated water plus a live simulation around the player.
- Water baked from a full offline flow simulation.

Each map was flown along the same camera path and its cost was recorded frame by frame. The live simulation won on looks. The baked version lost.

## Every river filled

All rivers and streams in the test area are now filled: the Severn bends, the Rea Brook upstream with more rocks, and a small stream. They join onto the approved stretch with no visible seams. Filling them added 0.05 ms per frame.

The water covers about 66,000 m2 of the test map.

![Every river and stream in the test area, built to follow the terrain](assets/img/gallery/devlog32_water_map_1024.jpg)

## You can walk in it

An invisible wall around the water was found and removed. The player now wades in knee deep, and the water pushes and foams around them.

![First wading test, before the creek bed was added](assets/img/gallery/devlog32_wake_first_test_1024.jpg)

## Making it cheap

The live simulation covers 64 by 64 m around the player in 25 cm cells, 256 by 256 in all. It was rewritten to run on the graphics card. Its cost dropped from 0.39 ms to 0.04 ms per frame, about 90% less.

With live water on, the test map ran at 189.6 FPS in the editor. With it off, 191.1 FPS.

![Extra time per frame for the live water simulation, before and after the rewrite](assets/img/gallery/devlog32_water_sim_cost_1024.png)

## Creek beds

The ground under the water is now creek or river bed, about 70,000 m2 in the test area.

- Gravel where the water runs fast, silt where it is slow.
- A damp margin reaches 0.5 to 1 m past the waterline. Its width changes as it goes, so the banks do not look ruled.
- The creek water was darkened a little so it reads less glassy.

![The creek bed follows the water, with a damp margin past the waterline](assets/img/gallery/devlog32_creek_bed_1024.jpg)

These shots are from the water test maps. Trees and grass are not dressed there yet.

## Tools

Play mode now has keyboard camera keys on the number pad: turn, look up and down, and raise or lower the camera. Mouse look still works alongside.

## Changes to the plan

- The live simulation around the player is the chosen method for moving water. Baked flow is dropped.
- The player can wade into rivers and creeks.

## Next

- Roll the new water and creek beds out to the region maps.
- Swimming depth and current for gameplay.
- Splashes and a full dressing pass on the river banks.
