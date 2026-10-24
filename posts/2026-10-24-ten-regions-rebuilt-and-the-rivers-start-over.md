---
title: Dev Log #31: Ten regions rebuilt, and the rivers start over
date: 2026-10-24
---

One overnight run rebuilt every region map outside the hub from real elevation data and planted them with our own plants. The hub got the planting that was proven on the test map. Water on the hub was cleared out and a new river system was started from a single test stretch.

## Ten region maps from real ground

All ten region maps around the hub were built again in Unreal. Nine replace the old gray-box maps. Salinae, the salt town on the Salwarpe, is a new 1.5 km map.

Each map uses the same method as the hub: satellite elevation data opened to bare ground, real rivers and lakes, regraded banks with runoff gullies, and flat pads under every building.

Some maps fit more real land than their window holds. The open ground between story sites is squeezed and the sites themselves stay at true size. Height is never scaled. Steep slopes made by the squeeze are smoothed back below 33 degrees. No map window changed size, so crossing times stay at 10 to 15 minutes at a jog, and 5 minutes on Salinae.

![The ten rebuilt region maps, shaded terrain with rivers and lakes](assets/img/gallery/devlog31_region_terrain_1023.jpg)

Ground heights were checked against the real hills. The Long Mynd tops out at 512 m against a real 516 m. Abdon Burf on the Clee Hills reads 532 m against 540 m. Summits sit 4 to 14 m low because the pass that strips trees and buildings from the data also trims narrow hilltops. A summit restore pass is on the list.

Modern water was left out: canals, reservoirs and fish pools.

## Biomes and planting

Every map now has its own biome map built from the terrain, the water and the building plan. Slope, height above the nearest water and altitude decide where moor, woodland, bog, pasture and wet ground go. Edges are soft and broken up.

- The Wrekin is hanging woods below 330 m with open ground on the crest.
- The Long Mynd is 58% heather and bilberry moor with woods in the steep valleys.
- The Long Forest is 80% woodland.
- Salinae is pasture, strip fields and a working town on the river.

![Biome maps for the Wrekin, the Long Mynd and Salinae](assets/img/gallery/devlog31_region_biomes_1023.jpg)

The plants follow the region lists from Dev Log #30. Only our own plants are used. Every building has a clear ring of 8 m with no trees, shrubs or tall plants, and short grass starts 2 m outside the walls. Rocks were placed on tors, outcrops and scree.

In total the ten maps hold about 338,000 trees and shrubs and an estimated 59 million ground plants. All ten built with no step errors in about two hours.

![Trees, shrubs and ground plants placed on each region map](assets/img/gallery/devlog31_plants_per_region_1023.png)

## The hub gets the new planting

The planting approved on the environment test map was rebuilt on the hub itself.

- 11,346 old plant actors were removed.
- 33,681 trees and shrubs went back on the same positions.
- 48 ground layers placed 5.28 million plants.
- 249,300 crop and kitchen garden tiles went into the fields.
- The landscape grass now draws only from our own plants.

An audit found no third-party plants left on the hub. A grounding check found no floating trees. Seven trees rest on logs, driftwood or a river rock, which is correct.

## What the regions still need

A full list of buildings and scene sets for the ten region maps was drawn up from the building plans. The maps need 160 unique pieces. Ten are already in Unreal. 150 are still to make.

The list covers Roman ruins for Viroconium (town walls, gates, the bath house, the forum and Watling Street), brine pits and boiling houses for Salinae, a lime kiln and quarry, charcoal and iron working, shepherd huts, a fisher hamlet, waystations along the roads, camps and halls. Every place on the maps already has a placeholder block on its pad.

## The rivers start over

All earlier water on the hub was removed. The new water starts with one test stretch: the meeting of the River Severn and the Rea Brook, about 110 m below the ford.

New rules for water:

- The terrain is final. Water fits the channels that are already there. A check of 14,308 points found no change to the ground.
- Water is period correct for the 6th century. No culverts or fantasy rapids.
- One map is finished and checked before the rest are built.

The surfaces are built as ribbon meshes that follow the river bed. Each one carries the flow speed and direction, the depth and where foam forms. The Severn falls 0.7 m over 812 m. The Rea Brook falls about 3% and pools behind bumps in its bed before it drops into the Severn.

A new water material moves two layers of ripples along the flow and stretches them with the current. Foam gathers at the waterline, over riffles and in the mixing plume below the brook mouth.

The built-in Unreal water system was also tested. Its surface never rendered, so it was set aside for now.

## Website

The site now has a RoadMap with ten checklists: heroes, heroines, animations, regions, trees, shrubs and climbers, ground plants, world effects, buildings and props. Each item shows its steps as done, in progress or not started. The Episode 4 page for world, plants and sky is also up, with the video to follow.

## Changes to the plan

- Salinae is now a full region map.
- Terrain on every map is locked. No more carving or regrading.
- Water is being rebuilt from scratch, one test stretch first.

## Next

- Swimming, wading depth and current for gameplay. The ford is 1.5 to 1.8 m deep at the current river level, too deep to wade.
- Riffle shapes, wet banks, splashes and a performance check on the test stretch.
- Summit restore pass and distance meshes for the region maps.
- Autumn colours for the large oak, ash and alder canopies.
