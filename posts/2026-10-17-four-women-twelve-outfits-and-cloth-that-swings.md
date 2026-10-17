---
title: Dev Log #25: Four women, twelve outfits and cloth that swings
date: 2026-10-17
---

The new female body from the last entry now has company. Four women of the cast got their heads, faces, skin, hair and eyelashes in one push. Three outfits each followed, cloaks and shawls started moving as real cloth in Unreal, and the test level got a new player character.

## Four heads on one seam

Rhiannon, Elen, Hild and Nest each started from front and side reference sheets of their faces. A shared base head was fitted to each sheet by measuring the eyes, nose, lip line, mouth width and profile, then warping the head to match. The neck seam, ears and back of the skull stay fixed, so every head fits the female body at the same 64-vertex seam and the heads swap freely.

- Each head has a real eye socket with lids that roll over the eyeball, a cut mouth with a lip roll, a mouth interior, textured teeth and a tongue.
- All four share one face layout of about 13,000 vertices, so animation and face data carry from one head to the next.
- Each face has the full set of 52 facial shapes for speech and expression, plus a small face rig for the jaw and eyes.
- The blink closes the lids fully without touching the eyeball. A rebuilt nose matches the sculpted shape to within half a millimetre on most of the surface.

## Skin, hair and lashes

The skin colour comes from the reference sheets projected onto each head. Lighting in the photos is removed first, so only colour, freckles, under-eye tone and small marks are kept, and the engine supplies the light. Fine pore detail sits on top. Body and heads share one colour correction, and the shading normals at the neck seam are averaged, so the join does not show.

Hair is a solid cap with layered cards on top. Rhiannon wears a low twisted knot with grey streaks, Elen a high ponytail tied with linen, Hild a crown braid with long loose hair, and Nest a single long braid wound with red wool. Loose locks have a soft curl that grows toward the tips. Elen's ponytail and Nest's braid each ride a chain of bones so they can swing with physics.

Eyelashes are short strips bound to the lid edges. They follow every blink and expression.

![Hair triangles before and after the game budget](assets/img/gallery/devlog25_hair_budget_1017.png)

The first pass of hair ran from 23,000 to 35,000 triangles. That was too heavy for gameplay, so the hair was rebuilt with fewer, wider cards and simpler braids, down to about 9,000 to 10,000 triangles per woman.

## Levels of detail

Each woman now has a gameplay head of 17,700 triangles, the same size as the male heads, with all 52 facial shapes carried over. The full head stays for close-up scenes. Three lower levels of detail cut the head, eyes and hair further, and the mouth parts and lashes drop out at distance. The neck seam stays closed at every level.

![Whole character triangles per level of detail](assets/img/gallery/devlog25_character_lods_1017.png)

A complete woman comes in at about 57,000 to 58,000 triangles at full detail, under the 65,000 budget for a story character.

## Twelve outfits

Each woman has three outfits: work clothes, travel or winter clothes, and formal dress. The pieces include undergowns and gowns, a Saxon peplos with saucer brooches and a bead festoon, aprons, trousers and boots, leg wraps, capelets, mantles and shawls, hoods, head cloths, belts with knives, pouches and keys, satchels, a drawstring sack on rope straps, necklaces and bracelets. Garments are shared between outfits, with colour set per outfit.

Hoods were rebuilt after review. The first version sat on the head like a hat. The new hood is a loose cowl with a deep face opening that falls back and rests on the cloak below it. Cloaks, mantles, shawls and hoods use a new soft twill cloth texture.

## Cloth that follows the body

Every cape, cloak and shawl in the game, male and female, now simulates as cloth in Unreal. The shoulders are pinned, and the fabric is free to move more the lower it hangs. That limit is set from height on the garment, so no painting is needed. In a spin test a cloak flares and trails while the shoulders stay in place. Shawls and mantles drape onto the arms under gravity. Other garments stay skinned to the body.

## A new test player

The test level had grown slow with dozens of characters standing in rows. They were cleared out. The player is now Nest in her riding outfit: gown, trousers, boots, belt, brooch and a long green riding cloak that simulates as cloth. She uses the standard movement set retargeted onto the female skeleton. Skin under the clothes is hidden so it never pokes through.

## Detail levels that switch together

The third-person camera sat outside full detail, and small parts such as the head, hair and brooches dropped detail before the body did. Two fixes went in. The switch distances were pushed out, so the body stays at full detail to about 8 metres. Every character with more than one mesh now has the body drive the detail level and all other parts follow it. In game every part is at full detail at 4 metres, one step down at 10 metres and two steps down at about 16 metres.

## Changes to the plan

The campaign now runs over five years, from spring 548 to winter 552, with an epilogue in 553. The story plays from spring to autumn, with quieter seasons between the acts for building and recovery, and every winter is a siege season against the dead. The main path is planned at 60 hours or more. The front page has been updated to match.

## Next

Physics on Elen's ponytail and Nest's braid in Unreal, and linking the lashes to the blink there. The other eleven outfits go to Unreal after review, with texture work for borders and hems. A frame rate check with the new player in the test level.
