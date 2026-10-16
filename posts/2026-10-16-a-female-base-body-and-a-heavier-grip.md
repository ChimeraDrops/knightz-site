---
title: Dev Log #24: A female base body and a heavier grip
date: 2026-10-16
---

This entry is about characters. A new healthy female base body went from a raw sculpt to a rigged, textured game mesh in one day. The large male body also learned to hold its weapons properly, and two swords lost a see-through ring at the pommel.

## A new female base body

The cast needs a healthy adult woman's body to sit beside the healthy male and large male bodies. Like them, it takes a swappable head on the shared 64-vertex neck seam, so every female head built later fits it.

The starting sculpt was a dense, double-walled shell. It was welded into one clean skin first. The fingers were separated, the toes were joined into one creased block (the same choice made for the male bodies), and a hidden skin fin joining the inner thighs was cut away so the legs move freely up to the hip.

## From 70,000 to 25,000 triangles

The body was reduced to about 25,000 triangles. Each region got a protection weight so the joints keep enough detail to bend cleanly. Joints and silhouette areas keep the most detail, and flat areas such as the belly and thighs give up the most.

![Share of detail kept by region during the reduction](assets/img/gallery/devlog24_body_detail_regions_1016.png)

Joint positions were found by placing coloured markers along each limb and reading the crease and outline bend in a render. This caught an elbow guess sitting 4 cm low on the forearm and a knee guess sitting below the kneecap.

## Rig, skin and levels of detail

The final game mesh was made by fitting the healthy male body's low-poly mesh onto the new shape. That keeps the same vertex layout and lets the rig weights carry over. Hands use a per-finger fit, so a different finger spread does not break them. The body stands 1.65 m tall.

- The rig is the same mannequin-compatible skeleton the other bodies use, refit bone by bone, plus two chest bones for secondary motion.
- The skin texture is built from the male body's skin detail with the male muscle shading removed, at 4096 pixels.
- The body is now fully symmetric. The better-modelled side was mirrored onto the other.
- Pose tests (arms raised, elbows and knees bent, wrists turned) show no tearing.

![Triangles at each level of detail](assets/img/gallery/devlog24_body_lods_1016.png)

Three lower levels of detail drop to 11,474, 5,736 and 2,292 triangles. Each level keeps the neck seam intact, so a head never shows a gap at distance. The body is in review in Blender now. After approval it goes to Unreal.

## The large male body holds its weapons

Until now, the large male body borrowed the weapon sockets of the healthy male body. Its hand is bigger and its knuckle row is tilted, so a sword sat about 8 degrees off the fist. The sockets were rebuilt by fitting the healthy male grip onto the large male hand, finger joint by finger joint. The fit lands within 0.4 cm on average.

- Sword, axe, shield and spear now each have their own socket on the large male body.
- A grip layer closes the fingers around whatever is in each hand, checked in game with the weapon sitting exactly on its socket.
- Shields now ride their own shield socket in game. Before, they used the off-hand weapon socket.
- The first large male worker character now carries weapon slots, ready for combat.

The full set of 30 movement clips for sword and shield and for axe and shield was checked frame by frame. No blade crosses the shield. The closest pass is an axe shaft 1.8 cm from the body on one walk clip, which will be watched in review.

## A see-through pommel

Close-up captures of the large male sword grip showed a transparent ring just above the pommel on two swords. The collar dome there had its triangles facing inward, so the engine culled them. Those triangles were flipped in place with materials and UVs kept. A scan of every weapon mesh now finds no more inside-out faces on any sword.

## Changes to the plan

No changes to the overall plan. The healthy female body joins the base body set.

## Next

Review of the female body, then export to Unreal and retargeting the animation set onto it. After that comes the first female head on the new seam. Weapon slots go on the other large male characters as they become fighters.
