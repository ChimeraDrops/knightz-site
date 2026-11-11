---
title: Dev Log #49: Kicked free from the ground
date: 2026-11-11
---

Two more of Owain's clips are approved: the downed struggle and the escape from it. The struggle is a synced pair with a matching clip for the crawling enemy. The audit now stands at 53 of Owain's 76 original clips. Work also started on the Restless themselves: 16 body variants across three base bodies and nine generic heads are built, textured and reviewed in Blender.

![The downed struggle and escape, beat by beat](assets/img/gallery/devlog49_downed_beats_1111.png)

## The downed struggle

Owain has been pulled down. He lies on his back while a crawling enemy grips his left ankle and climbs his leg toward his throat. The clip is a 4 second loop, and the enemy clip runs on the same 120 frames.

- **Owain's pose.** He is reclined about 70 degrees with his head raised. His sword fist is planted on the ground with the blade flat out to his right. The shield covers his chest.
- **Three kicks.** His free right foot kicks the enemy in the face on frames 14, 68 and 105. Each kick has a chamber, a thrust and a retract. The shield lifts slightly during each kick so it clears his shin.
- **Tug of war.** The enemy drags his leg away on frames 44 and 98. Owain yanks it back on frame 56.
- **Hand-built ground pose.** The generated reference bent his chest and neck out of shape, so the pose was built by hand.

## The enemy side

- **Climbing.** The enemy kneels and climbs the shin hand over hand, from the ankle to mid-shin, chest rising. Then it lunges for the throat with its jaw snapping.
- **Kicked off.** On each kick its head snaps back, its hands are knocked loose and it slides back to the ankle. It regrabs and yanks the leg.
- **Crawling legs.** The knees alternate four times per loop. Feet point back along the ground and the ankles only hinge, with no spin.
- **Grips.** Each palm is solved onto the leg with limits on wrist bend and forearm roll. A few frames after each kick leave the hands a few centimetres off the leg, which reads as being knocked loose.

## The escape

When the player wins the struggle, Owain kicks the enemy off and gets back to his feet.

- **Kick.** The first 16 frames match the struggle loop, so the switch is seamless. The kick lands on frame 14.
- **Back roll.** He rolls back over his shoulders with the shield held to his chest and the sword hand tucked.
- **Up to guard.** He comes onto his right knee, crouches, steps with his left foot and then his right. He ends in the exact first frame of his guard loop on frame 124, about 55 cm closer to the enemy. Block and dodge can cancel from frame 110.
- **Checks.** The joint check is clean on every frame. Feet stay within half a centimetre of the floor, and the sword and shield clear the floor and his body on every frame.

## The Restless take shape

![Sixteen Restless body variants and how each was built](assets/img/gallery/devlog49_restless_variants_1111.png)

The Restless are built on the same three base bodies as the living cast: the healthy male, the large male and the healthy female. Every variant keeps the living body's rig, UVs and vertex order. Any Restless body can swap in for a living one and play every animation.

- **Seven conditions.** Recent, Possessed, Drowned, Starved, Flayed, Half skeletal and Old Dead. Not every body gets every condition: the healthy male has seven, the healthy female five and the large male four.
- **Texture variants.** Recent, Possessed and some others reuse the living mesh with new skin. Possessed adds glowing veins.
- **Reshaped variants.** Drowned bodies bloat, Starved bodies thin out, and the Old Dead shrink into dry, leathery husks. The same displacement is applied to the body, its levels of detail and its severed parts, so cuts still line up.
- **Half skeletal.** Skin is cut away by mask and bone pieces are added: a rib cage section, a forearm and a shin.
- **Red eyes.** Every Restless head gets glowing red eyes, set to read like a red LED in the dark.

### How the skin was made

- Each living body is rendered front, back and sides with fixed cameras. An image editor repaints each view in the chosen condition while keeping our pose and proportions.
- The edited views are aligned to the renders and projected straight onto our UVs, then de-lit and colour matched.
- Fine veins are added in 3D so they cross UV seams without breaks.
- A shared neck band means any Restless head fits any Restless body of the same type with no visible seam.

### Nine generic heads

Three new heads per body type, each built from a generated face image, turned into a 3D model and wrapped onto the existing head topology. That keeps the face rig and all 52 facial shapes working. The three female heads carry thinned, ash-grey hair.

## Changes to the plan

- **Restless assets stay in Blender until reviewed.** No export to Unreal until every body and head has been inspected.
- **Each body variant ships with a generic head** in the matching condition as its default.
- **The crawler gets back up.** After the escape kick, the crawling enemy is thrown back and crawls in again, so the fight continues.

## Next

- The enemy's kicked-off clip for the escape, then hazards, death, get-up, item use, parry, guard break, block and hit reactions. 23 of 76 remain.
- Review the generic heads on each body variant, then levels of detail for the new heads and hair.
- Combo windows and hit timing, then one export pass of every edited clip to Unreal and a fight test in the demo clearing.
