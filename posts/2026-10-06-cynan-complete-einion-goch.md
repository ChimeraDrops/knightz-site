---
title: Dev Log #11: Cynan complete, Einion Goch's head, and shared rules for every head
date: 2026-10-06
---

Cynan is finished and bound to the body skeleton. Einion Goch, the second head on the large male body, now has a face rig and is in hair review. A few build rules also changed so that every head stays interchangeable.

![Named cast, head pipeline status](assets/img/gallery/roster_status_1006.jpg)

## Cynan, complete

The captain of the garrison now has every step of the head pipeline behind him.

- **Skin.** Weathered tan with ruddy cheeks and nose, heavy dark brows with grey in them, deep frown lines and a scar across the bridge of the nose.
- **Hair.** A shaggy, layered brown and grey cut built from 10,991 quads and swappable like every other hairstyle.
- **Face rig.** 52 ARKit facial shapes. The chipped upper tooth is real geometry and shows when he talks.
- **Neck seam.** The weld between head and body was smoothed in shape, normals and colour, so no line shows in the viewport or in renders.
- **Body bind.** Head, eyes, teeth, tongue and hair are weighted to the shared body skeleton. A test with the head turned 50 degrees, the neck tilted and the jaw open left the seam gap at zero.

## A bug found and fixed

Blender 5.2 adds new shape keys at full strength. Several finished heads had all 52 expression keys active at once when saved. Every key is now set to zero in the master file and in the saved head assets for Cynan, Cadoc and Tysilio, and the pipeline now checks the count of non-zero keys after every install.

## Einion Goch

Einion is a heavy man of about 45 with a thick neck, a broken nose, a missing lobe on one ear and pale green eyes. His head is the second one built for the large male body.

- **Fit.** His neck sits differently from Iddon's, so the head was cut lower on the neck and bridged back to the body seam.
- **Nose.** The source nose was too large for the standard nostril topology, so a template nostril was placed by similarity and smoothed in.
- **Ear.** The right lobe is shortened in the mesh itself, and the left ear is untouched.
- **Skin.** Heavy brows, a reddened nose bridge, a pink healed edge on the damaged ear and a shaved shadow where the beard will go.
- **Face rig.** 52 ARKit facial shapes, with a check that the teeth and gums never come through the cheek on any shape.

His red beard, going grey, is in review as hair cards that follow the jaw.

## Shared rules

- **Matching head dimensions.** Every new head is compared against the existing ones on the same body for width, crown height and back of the skull, then scaled toward them. Helmets and clothing then fit any character. Einion's head was narrowed by about 3 percent across the temples for this.
- **Hair budget.** Long hair with a full beard is about 16,000 quads. A short cut with a beard is about 10,000. One character at the highest detail level is about 50,000 quads.
- **Armour regions.** The hero body will be split into regions such as head, torso, arms, hands, legs and feet. A piece of armour hides the region under it, which saves rendering cost and stops skin poking through plates.

![Head pipeline, per character](assets/img/gallery/head_pipeline_steps.jpg)

## Tooling

The head pipeline is now documented step by step with the failures recorded next to the fixes, which is cutting the time per character. A capture tool also renders a still for each pipeline step from the saved files. It is producing the first video episode on how a character head is built from one reference image.

## Next

Einion's hair review, then his body pass. After that, the next heads from the cast sheets on the manor, and the Unreal Engine export of the finished characters.
