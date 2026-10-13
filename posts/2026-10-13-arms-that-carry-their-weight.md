---
title: Dev Log #21: Arms that carry their weight
date: 2026-10-13
---

Today was a full review pass over basic movement for every weapon set on both male bodies. The legs from yesterday held up. The arms did not. Most of the work went into making the arms look like they belong to a man holding a weapon, then wiring the approved set into the game.

## Closed fists

The unarmed clips had loose fingers that moved on their own. Every unarmed clip now uses the closed hand from the sword grip, so the fighter carries two fists. The large body copies the same hand pose so the thumbs sit the same way.

![Unarmed guard walk with closed fists](assets/img/gallery/devlog21_unarmed_guard_1013.jpg)

## A free wrist on the sword arm

The sword hand used to be locked to a fixed angle, which twisted the forearm on some frames. A new arm solver places the hand, then picks the elbow and wrist angles inside natural limits: the elbow bends like a hinge, the wrist stays close to neutral, and the forearm does not roll past what a real arm allows. The guard walks keep the sword hand under the elbow at the hip with about 60 degrees of bend.

![Sword guard walk with a relaxed wrist](assets/img/gallery/devlog21_sword_guard_walk_1013.jpg)

The spear moved to a two-hand guard. The rear hand now sits 40 cm lower on the shaft for a longer, steadier grip.

![Two-hand spear guard](assets/img/gallery/devlog21_spear_guard_1013.jpg)

## Square shoulders

Many clips showed one collarbone angled down, so that shoulder looked low and out of its socket. A pass measured both shoulders against the neck on every clip and rotated the low, forward side up until it mirrored the other. The hand keeps its exact position and angle, so shields and weapons stay where they were. 176 clips were corrected.

![Axe and shield guard after the shoulder fix](assets/img/gallery/devlog21_axe_shoulder_1013.jpg)

The axe set also got a neutral wrist on every arm and a slight forward lean on the forward walks.

## Arms that swing with the legs

The source walks often swung the arms across the body. The new swing is driven by the legs: when the right foot goes forward, the left arm goes forward, and the swing follows the direction of travel. On the side and diagonal walks the chest now turns part of the way toward travel, so the arms swing along the path the character is moving on.

![Walk with the arm swing tied to the stride](assets/img/gallery/devlog21_walk_swing_1013.jpg)

The jog arms were rebuilt twice. The final version keeps the hand in front of the shoulder with the forearm pointing forward and the elbow clear of the hip. The side jog was also too slow for its stride and now plays a third faster.

![Jog with the hands in front of the shoulders](assets/img/gallery/devlog21_jog_arms_1013.jpg)

The large body uses the same rules with a little more room for its build.

![Large body jog](assets/img/gallery/devlog21_large_body_jog_1013.jpg)

## The bow comes along

The bow jogs had no bow. The yew bow from the props set is now in Unreal and rides in the left hand on every bow walk and jog, carried forward and up so it clears the legs.

![Bow jog with the bow in the left hand](assets/img/gallery/devlog21_bow_jog_1013.jpg)

## Into the game

All standard movement clips are tentatively approved for the movement state machines. Each weapon set on each body now has two blend spaces built from the reviewed clips:

- **Free:** idle, eight walk directions and eight jog directions, placed at the measured travel speeds so the feet do not slide.
- **Guard:** guard idle and eight guard walk directions.

The character swaps blend spaces when the weapon changes or the guard goes up, inside the same animation blueprint.

New controls:

- **Walk by default.** Tap **Shift** to toggle run. Tap again to walk.
- **Right mouse** raises the guard. The character slows to a guard walk, faces where the camera looks and strafes in eight directions. Release to drop the guard.

## Hidden seams

The dismemberment bodies are split into pieces at the cut lines. Before any cut, those lines showed as a faint shading seam on skin and cloth. Two causes:

- The engine rebuilt the body normals on import and treated each cut line as a hard edge. It now keeps the smooth normals from the source file.
- On the clothes, each edge at a cut leaned toward the hidden strip that closes the cut, so the two sides of every sleeve and trouser leg disagreed. The edge normals are now rebuilt from the cloth on both sides of the cut.

The cut lines are now invisible on intact characters at every level of detail.

## Next

Attacks for every weapon set, and the first undead body models.
