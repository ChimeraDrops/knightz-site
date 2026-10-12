---
title: Dev Log #17: Outfits, cloaks and textured hair for the whole cast
date: 2026-10-09
---

Today the cast got clothes. Casual and work outfits are in Unreal for 15 characters, each with its own colour palette, and Owain is now the playable test character wearing his casual outfit, cloak and sword.

![Casual outfits in Unreal, first half of the cast](assets/img/gallery/devlog17_outfits_lineup_a_1009.jpg)

Every outfit is built from one shared garment kit and recoloured per character.

![Casual outfits, second half of the cast, including the larger body type](assets/img/gallery/devlog17_outfits_lineup_b_1009.jpg)

## Shared garment kit

The kit was built in Blender for both body types: under-tunic, tunic, padded tunic, trousers, leg wraps, turnshoes, belts and cloak. Garments are shaped from the body surface and skinned to the same skeleton, so one piece fits every character of that body type.

![The shared garment kit in Blender, front and back](assets/img/gallery/devlog17_garment_kit_blender_1009.jpg)

## Cloaks

Hanging cloaks run on Kawaii Physics with five bone chains. Arm collision capsules keep the arms from cutting through the cloak while moving.

![Cloaks from behind](assets/img/gallery/devlog17_cloaks_back_1009.jpg)

## Hidden under clothes

Anything fully covered by clothing is masked out in the shader: the body and the lower layers between the knee and the chest. This stops legs and trousers poking through the cloth while running and saves a little overdraw. On the left, the outfit as seen in game. On the right, the same character with the outer layers removed.

![The outfit in game, and the same character with outer layers removed](assets/img/gallery/devlog17_hidden_under_clothes_1009.jpg)

## Steel for swords

Swords now use a steel material: a metallic blade with a brighter, smoother band along the sharpened edge.

## Hair method for all heroes

Every hero has a new review build of the hair method: a textured shell for the scalp plus layered strand cards for the loose hair. Short and shaggy styles are grown procedurally on the shell with a part, a fringe and trimmed ears and sideburns. Long styles use cards from the original flows with an outer loose layer. Beards are trimmed behind the jaw line. Total triangle counts, shells included, run from about 4,000 to about 9,000 per character. Known gaps: long styles still read slightly sleeker than the references, some shags look helmet-like from behind, and level-of-detail versions are not built yet. Nothing is exported to Unreal until the hair is approved.

## Next

An audit pass on the garment kit covering skirt movement, cloak shape and triangle counts, then dedicated pieces such as habits, aprons and mail.
