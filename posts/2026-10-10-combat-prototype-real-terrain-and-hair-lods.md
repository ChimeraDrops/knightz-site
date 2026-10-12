---
title: Dev Log #18: Combat prototype, real terrain and hair level of detail
date: 2026-10-10
---

Three jobs landed today: the first playable combat system, a world rebuilt from real elevation and river data, and level-of-detail versions of the new hair for every hero, now imported into Unreal.

## Combat prototype

Combat is now written in C++ inside the Unreal project. It follows a written design built around weight and timing: a defender reads when an attack lands, and attack direction plays no part. The player and allied fighters share one fighter component, and enemies run their own AI state machine. Every tunable number lives in one data asset so balance can be changed without touching code.

- Stamina: every action costs it, and it only recovers while not attacking or guarding. Running dry leaves the fighter stunned and open.
- Parry and block are separated by timing. A well-timed press deflects, a late press blocks. Parrying a worn-down enemy pins it in place and opens a short window for a limb strike.
- Limb strikes are dice rolls with odds that improve as a fight wears on, and each failed roll has its own consequence.
- Enemy attacks come in tiers (single swipe, double swipe, heavy, grab) with damage and stamina cost scaled to match, and the choice is weighted by how much stamina the target has left.
- Crowds take turns. At most two enemies attack at once, with rolled gaps between them and one or two flankers working around the back.
- Weapons wear down, can break mid-fight and are repaired at a fire. Shields have a cover arc, a bash and their own durability.
- Allies use the same moves and read the same tells as the player.

A test level runs six enemy types against Owain with Bedwyr as an ally. The full animation list needed for the system is written out, with stand-in clips in place until the real animations arrive.

## A world built from real terrain

The earlier map builds were scrapped. Each region is now a window of real elevation data with rivers and streams copied from current mapping, centred on its main location at its true position. Buildings, fields and woods are then placed where the ground and water make sense.

![Region windows at their real positions](assets/img/gallery/devlog18_region_windows_1010.png)

Ten regions are built, from 3 to 4 km across. Travel between them is by thresholds and fast travel over realistic distances. The manor stands on a hill inside a loop of the Severn, and its level is a gray box with more than 49,000 placeholder props placed by authored rules: coppice woods cut in rotating panels, alder and willow along the banks, strip fields, a mill site and a fish weir. The Roman city of Viroconium is joined to the manor map with an identical seam and carries a 3.4 km wall.

## Hair level of detail, imported

The new hair method has a full set of level-of-detail versions for all 15 heroes. The closest version is a textured shell plus strand cards. Distant versions drop the cards first, then thin the shell. A typical hero goes from about 8,000 triangles of hair up close to a few hundred at the far end.

![Hair and beard triangles per hero at each level of detail](assets/img/gallery/devlog18_hair_lod_triangles_1010.png)

All 16 heroes, with beards, were then imported into Unreal over the old assets, with new hair and card materials for each slot.

## Plan changes

- World: real topography replaces the earlier hand-built maps. The story is edited to fit the geography where needed.
- Combat: the written design is now the reference, and mounted combat is dropped.
- Characters: the new hair is the shipping method for all heroes.

## Next

Real combat animations in priority order, final art to replace the placeholder props, and the remaining hair review notes.
