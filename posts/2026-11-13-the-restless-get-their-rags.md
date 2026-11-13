---
title: Dev Log #50: The Restless get their rags
date: 2026-11-13
---

All 16 Restless body variants and their nine generic heads are approved in Blender. The line at the neck where head meets body is gone. The male clothing kit was refit closer to the body, and every garment on the three base bodies now has a torn and soiled version. The Restless also get worn hairstyles and beards, ragged trousers for the Starved and Drowned, and three sets of damaged Roman armour for the Old Dead.

![The Restless wardrobe by item and base body](assets/img/gallery/devlog50_restless_wardrobe_1113.png)

## Closing the neck seam

The heads and bodies already met with no gap in the mesh. A faint line still showed in renders. It came from the textures, and three causes were found and fixed in order.

- **Thin texture padding.** Colour only extended a few pixels past each texture island. At a distance the renderer blended in the dark area beyond it, which drew a dashed line. Every empty texel is now filled from the nearest painted one.
- **Mismatched skin detail.** The head carried much stronger pore detail than the body's neck. Head detail now fades out toward the seam over the last 7 cm.
- **A thin rim.** A step of a few millimetres on each side remained. Texels on both sides of the seam are now stitched to the same colour.

Colour lines along the body's own texture cuts, such as one down the back, were matched the same way. The average colour jump at the seam is now very small on all 16 bodies.

A ridge around the mouth and nose on the generic heads was also smoothed out on all nine. Each face moved by 1.5 cm or less, and the face rig and its 52 shapes still work.

## Approved

- **Healthy female:** five variants approved.
- **Large male:** four variants approved.
- **Healthy male:** seven variants approved.
- Each body type has a display file with every variant standing in a row for review.

## Tighter male clothes

![Gap between cloth and skin before and after the male refit](assets/img/gallery/devlog50_male_refit_1113.png)

The female outfits were refit closer to the body last month. The male kit now gets the same treatment on both male bodies: under-tunic, tunic, padded tunic, trousers and cloak, with belts following their tunic.

- **Only vertex positions move.** Topology, texture layout, weights and materials are unchanged, and the levels of detail follow.
- **Tunic skirts** flare from the hip in an A-line and keep about half their folds.
- **The cloak** is now a fitted cape that hangs from the shoulder blades.
- **Layer order is kept.** Each layer is pushed out past the one beneath it.

The refit kit is now the master for both male bodies, and all 56 garment files were exported again for Unreal.

## Torn and soiled garments

Every garment on the three base bodies has a damaged version with levels of detail: 10 kit pieces on each male body and 62 pieces on the female body, including capes, hoods, belts, jewellery and shoes.

- **Damage.** Ragged edges, round holes and vertical slashes. Fully cut faces are removed. Partly cut faces are trimmed by an alpha mask, so torn edges are smooth curves inside a face.
- **Grime.** Three colour channels paint mud rising from the hem and along torn edges, dried blood and rot. A fourth channel holds the cut mask.
- **Cloth colour.** Darker and less saturated than the living version.
- **Same skeleton and weights.** A damaged garment swaps in for its living version one to one.

### Ragged trousers

The Starved and Drowned bodies go shirtless. Their trousers are moved onto the reshaped body, torn off raggedly around mid-calf and caked in mud. The Drowned version uses a wet material.

## Worn hair and beards

20 hairstyles and 7 beards and moustaches have Restless versions. Each was moved from its original head onto the default generic head of its body type.

- About a third of the hair cards are removed in patches, with a few bald patches on the scalp.
- The colour shifts to dusty grey and ash with dirt and rot, and the shine is gone.

## Damaged Roman armour

The Old Dead get three Roman armour outfits on each body type, all worn over a torn red tunic.

- **Segmented plate.** Iron hoops around the body, chest and back plates, banded shoulder guards and a skirt of hanging leather strips.
- **Mail shirt.** Mail to the hip with short sleeves.
- **Scale shirt.** Bronze and iron scales with leather strips at the waist and shoulders.

Damage includes dents, rust, holes, ragged edges, missing plates and blood. Rusted metal loses its shine. Each armour piece has three levels of detail at about 65, 38 and 20 percent of the full mesh. Helmets and greaves come later.

## Changes to the plan

- **The refit male clothing kit replaces the old fit** on both male bodies in Blender and Unreal.
- **Restless clothing reuses the living garment set.** Every outfit gets a damaged version on the same skeleton instead of separate clothing.

## Next

- Unreal materials that read the grime and cut mask channels, then export and import of the Restless bodies, heads, clothes and hair.
- Levels of detail for the new heads, and the last texture fixes at the neck on the female and large male heads.
- Reimport the refit male garments in Unreal.
- Owain's animation audit resumes with 23 of 76 clips to go.
