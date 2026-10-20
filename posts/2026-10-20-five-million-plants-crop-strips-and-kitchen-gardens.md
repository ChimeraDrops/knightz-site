---
title: Dev Log #27: Five million plants, crop strips and kitchen gardens
date: 2026-10-20
---

The hub got a test copy for ground cover. On it, every patch of land now carries the plants that belong there: grazed turf, hay meadow, reed beds, woodland flowers and fields of real period crops. Over five million plants were placed by script in one session, and a lighting bug that turned leaves black was found and fixed across the project.

## A test copy of the hub

The environment test map is a full copy of the hub, 3 km by 3 km, with the terrain, rivers, trees and buildings left in place. The original map is untouched. Old ground dressing was cleared from the copy so the new system starts from bare earth.

The ash sky was swapped out on this map for plain white sunlight and a standard cloud layer. Under neutral light the colour of each plant can be judged on its own. The ash sky stays on the hub itself.

A free flying camera sits at the gate, looking south over the manor, so the whole map can be toured with mouse and keys.

## Ten biomes

The land was split into biomes using the masks the hub already had for forest, wood edge, wet ground, river banks, meadow, fields, roads and settlement. Edges are blurred and broken up with noise, so one biome bleeds into the next instead of stopping at a line. Each biome is marked in the level with a floating label for review.

![Biome map of the test area, 3 km by 3 km](assets/img/gallery/devlog27_biome_map_1019.png)

| Biome | Area | Main plants |
|---|---|---|
| Grazed pasture | 507 ha | Short turf, clover, rank patches, thistle, dock |
| Woodland interior | 142 ha | Leaf litter, bluebell, wood anemone, dog's mercury, ramsons, fern |
| Wood edge | 17 ha | Nettle, cow parsley, foxglove, fern |
| Hay meadow | 10 ha | Foxtail, fescue, buttercup, knapweed |
| Wet grassland | 17 ha | Rush, sedge, meadowsweet |
| River bank | 39 ha | Reed, reedmace, iris, sedge |
| Fallow field | 40 ha | Grazed turf, thistle, dock, tussock |
| Crop field, east | 49 ha | Winter corn |
| Crop field, south | 34 ha | Spring sown crops |
| Manor gardens | 1.3 ha | Vegetable beds only |

## How the plants are placed

A generator written in Python builds density maps for 44 plant layers. Each layer has its own meshes, spacing, scale and random seed. Density is the biome weight times two layers of noise: a clump noise of 8 to 45 metres and a broad noise of 160 metres. The result is dense drifts, thin grazed patches and woodland carpets of a single flower, with natural blends between them.

- **5,244,259 plants** in 44 layers, grouped into one batch per mesh per 256 metre cell.
- **Plant sources:** the 54 plants built in Blender for KnightZ, plus bought meadow, foliage and weed packs. Trees are placed separately.
- **No collision** on ground cover. Only tall plants such as reed, nettle, foxglove, fern, thistle and dock cast shadows, plus the crops.
- **Draw distances by size:** litter and moss 30 to 60 m, short herbs 60 to 110 m, tall herbs and tussocks 140 to 200 m, reeds 320 m, crops 650 m.
- **Streaming:** short ground cover loads within 200 m of the player. Reeds and crops load within 700 m.

![Ground cover instances by biome on the test map](assets/img/gallery/devlog27_groundcover_biomes_1019.png)

Pasture and woodland hold almost three quarters of all plants between them, because they cover most of the land.

![Grazed pasture with an oak and the tree line beyond](assets/img/gallery/devlog27_pasture_1019.jpg)

![Woodland floor with hazel, ferns and leaf litter](assets/img/gallery/devlog27_woodland_floor_1019.jpg)

![Hay meadow running down to the river](assets/img/gallery/devlog27_hay_meadow_1019.jpg)

## Fields and gardens

The fields follow early medieval practice.

- **East field, winter corn.** Spelt in the north part and rye in the south, with a 5 metre grass balk between. A shallow furrow every 22 metres marks the strips. Rows run east to west inside a 6 metre grass headland.
- **South field, spring sown.** Five blocks from west to east: six-row barley, oats, peas, field beans and flax. Each block is separated by a 6 metre balk, with rows running north to south and the lanes kept clear.
- **Balks and headlands** carry short turf, ribwort plantain and a scatter of poppy, cornflower and chamomile. No crop mixes into another block.
- Almost 250,000 field tiles were laid and traced onto the ground.

Inside the palisade, four kitchen gardens sit in the free yard space, clear of buildings, the well and the gate lane. Beds are 1.5 metres wide, one crop per bed: onions, leeks, garlic and brassicas. No grass, weeds or wheat grow inside the manor walls.

![A field of grain under open sky](assets/img/gallery/devlog27_grain_field_1019.jpg)

![Pasture rising to the crop fields](assets/img/gallery/devlog27_pasture_fields_1019.jpg)

## Black leaves fixed

Many plants showed dark or black patches when seen from the side facing away from the sun. The cause was the same in every case. The plants are two-sided cards, and the back face received a flipped normal that pointed down into the ground, so it lit almost black.

The fix replaces that normal with one in world space that always leans upward. It went into the master material for the 54 KnightZ plants, five master materials from the bought plant packs and the material used by the hazel saplings and bushes. Measured brightness on the dark side rose from between a fifth and two thirds of the base colour to slightly above it, from all four directions. The fix applies to every level that uses those materials, not only the test map.

## Other findings

- The 54 KnightZ plants were imported at one hundredth of their size. The test map scales them up by 100 to compensate. The proper fix is to correct the import scale at the source.
- Draw distances for each plant still need tuning.
- Pale discs in the pasture come from older landscape grass that was already on the hub. They will be cleaned up.
- Performance in a packaged build has not been measured yet. The instance counts above are the baseline for that test.

## Changes to the plan

- Ground cover is now generated by script from the land masks, with a separate test copy of the hub used to tune it before it goes onto the real map.
- Fields are laid out as strips and blocks of single crops with grass balks between them, and the manor yard holds vegetable beds only.

## Next

Fix the plant import scale, tune draw distances per plant and profile a packaged build. Then bring the tuned ground cover onto the hub under the ash sky. The base animation set for the four women is still queued.
