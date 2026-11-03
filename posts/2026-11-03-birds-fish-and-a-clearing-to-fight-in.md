---
title: Dev Log #41: Birds, fish and a clearing to fight in
date: 2026-11-03
---

The last eighteen animals on the list were rigged and animated. A roe buck joined the red deer, an otter and a beaver got a skeleton of their own, and twelve birds and three fish were built on new bird and fish skeletons. All 36 animals planned for the game now move in Blender, with 898 clips between them. Work also started on a small combat demo level in Unreal.

![Animation clips per animal family](assets/img/gallery/devlog41_clips_by_family_1102.png)

## Roe buck, otter and beaver

![Roe buck, otter and beaver](assets/img/gallery/devlog41_roe_otter_beaver_1102.jpg)

- **Roe buck.** 0.70 m at the shoulder, inside the published range for roe deer. It shares the deer skeleton with the stag, hind and white hart. On top of the deer set it has a bounding run, a bark, a hoof scrape, ear turns and a look over each shoulder. 31 clips.
- **Otter.** 1.16 m nose to tail tip. The source body was hollow and the tail lay on the ground in torn strips. The body was filled, the gaps were closed and a new tail was built. On land it walks, scurries, lopes and bounds, sniffs for food and shakes off water. In water it paddles at the surface, swims underwater at 0.89 m/s and dives at a 70 degree pitch, values taken from otter field studies. 25 clips.
- **Beaver.** 1.11 m including the paddle tail. It shares the otter's skeleton. It gnaws, grooms its flank, swims, dives and slaps its tail on the water. 28 clips.

Water clips keep the animal at a fixed height. In Unreal the water surface sets where it swims, and land and water use separate controllers.

## Twelve birds

![The twelve birds](assets/img/gallery/devlog41_twelve_birds_1102.jpg)

Crow, raven, rook, goshawk, hen, cockerel, farm goose, greylag goose, mallard, herring gull, grey heron and common crane all share one 32-bone bird skeleton. Each has the same base set of 13 clips:

- Idle, alert and peck.
- Walk in place and with root motion.
- Turns of 90 and 180 degrees on the spot, with the feet re-planted.
- Take-off, flapping flight, gliding and landing.

Each species then adds its own calls and moves. The crows and the goshawk rouse their feathers. The hen and cockerel scratch the ground. The ducks, geese and gull swim. The heron and crane strike at prey with the beak. The goshawk strikes with its feet from a glide.

Wingbeat speed comes from a published formula that uses each bird's mass, wingspan and wing area. For the goshawk that gives 4.29 beats per second.

Every bird body was checked and repaired first. Each is now one closed surface with no holes, and feet that were fused together in the source models were cut apart. The goshawk arrived at almost 24,000 triangles and was reduced to about 2,600 to match the other small birds.

The bird clips are a first pass. Three pecks still stretch or bend the legs too far and will be reworked by hand.

## Three fish

![Eel, brown trout and pike](assets/img/gallery/devlog41_three_fish_1102.jpg)

The eel, brown trout and pike each have their own skeleton, because their bone counts differ (16, 18 and 20). Each has an idle hover, a slow swim, a fast swim and a turn each way. The pike adds a strike.

## A combat demo level

A small demo level was started in Unreal for testing a single fight. It is a forest clearing cut out of a copy of the hub map:

- Only the trees, logs and rocks within 120 m of the centre were kept. More than 50,000 other plants and 6,500 other objects were removed.
- A wrecked ox cart and scattered cargo sit in the middle of the clearing.
- The distant forest is a ring of eight painted panels made from captures of the real map, so the view still looks deep with almost nothing loaded.
- An invisible wall rings the clearing at 33 m. Six spawn points around the edge are set up for three waves of attackers.
- Owain spawns facing the cart as the player.

## An editor crash traced

One Unreal crash this week came from our own editor scripts. A script still held references to the old map when the editor switched levels, and Unreal's leak check stopped the editor. Scripts now clear those references before any map change. Two other crashes happened in the graphics driver with the editor idle and are being checked against a driver update.

## Changes to the plan

- **Every planned animal is now built in Blender.** The batch import into Unreal is next, one skeleton per family.
- **A combat demo comes before the full vertical slice.** It tests one fight in a small, light level before the larger manor slice.
- **Bird animation gets a second, hand-led pass.** The first-pass bird clips will be refined before import.
- **The RoadMap has a new Animals checklist** with a still of every animal and its progress through model, rig, skin, animation, checks, review and Unreal.

## Next

- Hand pass on the bird animations.
- Review of every new animal set.
- Batch import of all 36 animals into Unreal.
- Enemies, waves and combat tuning in the demo clearing.
