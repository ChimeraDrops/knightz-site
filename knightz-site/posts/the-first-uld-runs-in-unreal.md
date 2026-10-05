---
title: Dev Log #1: The first Uld runs in Unreal Engine 5
date: 2026-09-25
---

The first finished character for KnightZ is MN1, a male of the Uld, the heavy-boned people of the high country. As of today he imports into Unreal Engine 5.8 and runs around a test level with working hair and cloth physics.

## What was built

- **Body.** An AI-generated source sculpt cleaned up, retopologised to about 37,000 triangles and baked down to game textures (base colour, normal and a packed occlusion/roughness/metal map).
- **Face interior.** Eyes, teeth, gums, tongue and a mouth cavity built by hand, since the source had none.
- **Skeleton.** The Unreal Mannequin bone layout, so standard animations retarget cleanly, plus extra bones for dreadlocks, a hide skirt and a fur cloak.
- **Swappable clothing.** A deer-hide skirt, a second hide skirt and a fur cloak, each its own asset on shared slot bones.
- **Physics.** Dreads, skirts and cloak swing with Kawaii Physics, computed once on the body and copied to every attached piece.

## Why this matters

Every later character follows this route. The whole procedure is now written down as a step-by-step pipeline with the scripts saved alongside it, so the next build starts from a known recipe instead of from scratch.

## Next

An undead variant of the Uld and the first female body.
