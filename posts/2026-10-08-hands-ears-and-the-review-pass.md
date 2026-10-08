---
title: Dev Log #15: Hands, ears, and the review pass
date: 2026-10-08
---

Today was about details: a seam at the wrist, hair around the ears, and a checklist so every character gets the same review before it goes into Unreal.

![Triangle budget before and after the reduction pass](assets/img/gallery/lp_budget_1008.png)

## Wrist blend fix

The join between forearm and hand read like a bracelet on both male bodies. Three textures had a hard step at the seam: a tone change in the colour map, a ring of tilt in the normal map, and a jump in roughness. All three were rebuilt with a smooth crossfade from forearm to hand across about 11 cm. Renders from six views show no step on either body. A faint diagonal line remains on the thumb side of the standard body and is on the list. Meshes are unchanged, so only the body textures need re-importing in Unreal.

## Hair rules

Two rules now apply to every hair cap:

- **Ears.** The hairline hugs the ear within 0 to 3 mm and never covers it. Edges rest on the skin, and the nape edge is jagged with transparency.
- **Volume.** Caps follow the skull with natural variation. Straight slopes and uniform thickness are rejected.

## Review checklist

Each hero now goes through ten steps: head, hair, beard, mouth and eyes, body, Blender sign-off, FBX export, Unreal import, an in-level check with idle, walk and emotes, and final approval. Owain passed all ten today. Bedwyr is open in Blender for review.

## Unreal test level

The test level was cleared of all characters. Characters are placed one at a time for review and removed afterward.

## Next

Re-import the three body textures in Unreal, review hair across the cast, and re-import the reduced characters with LODs.
