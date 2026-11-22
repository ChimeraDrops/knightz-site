---
title: Dev Log #58: Sparks, blood and a flinching brigand
date: 2026-11-21
---

The Phase 2 demo of the melee rework was accepted, so Gate 2 is passed. Two new pieces went in on top of it. Blocked blows now throw sparks and landed hits draw blood. In Blender, the brigand got eight hit reactions, one for each of Owain's attacks.

## Sparks and blood, first pass

- **Sparks.** A block or parry throws 26 short bright streaks at shield and blade height between the two fighters.
- **Hits.** A landed hit sprays 26 droplets from the chest, 46 on a heavy hit. Droplets fall with gravity and drag, and most leave a splat where they land. Ground splats are capped at 160, oldest removed first.
- **Build-up.** Each hit leaves a stain on the victim's clothes, up to 9 per fighter. The attacker sometimes gets a smaller stain too. Blood also builds up along the blade, up to 10 marks.
- **Severs.** A severed limb gets a burst, a pulsing stream from the stump, drips from the cut piece and three pools that spread over time.

![Blood timing after a sever](assets/img/gallery/devlog58_sever_blood_1121.png)

It was checked in a recorded fight against the brigand AI. Sparks showed on a parry, splats on hits to both fighters, a stain on Owain's cloak and a trail of blood at an arm sever.

Weak points found in the same fight:

- Sparks are small and pale at play distance.
- Every splat and pool uses the same ragged decal, so a pool reads as one big splat.
- Stains sit at a rough chest position, not where the blade touched.
- Blood on the blade was not seen in the frames checked.
- Blood does not fade out yet.

## Shield flip in the side-view video

In one test video filmed from the side, Owain's shield faced the wrong way for the whole fight. The cause was the recording setup. It changed the player's camera arm during play, and that rebuilt his components and sent the shield back to a default socket. The game itself was not at fault. The recording camera now turns without touching the player, and a new take showed the shield held correctly.

The check turned up a separate detail. During parts of the six attack swings, the arm side of the shield turns toward the opponent (18 to 61 percent of frames, Light 2 the most). Guard, idle, parry, block and sever clips are fine. No change has been made.

## Phase 3: brigand hit reactions

Phase 3 makes the brigand's clips match Owain's timing. The first group is eight hit reactions: Light 1 to 3, Heavy 1 to 3, the kick and the shield bash.

- **Set up.** A brigand stand-in with a seax was placed in Owain's audit scene at each attack's strike distance, facing him.
- **Contact.** For each attack, the blade path through the brigand's body was measured at the hit frame. Light 1 crosses the upper chest from his left shoulder. Light 3 and Heavy chop straight down. Heavy 2 rises from the right hip. Heavy 3 slashes across at chest height.
- **Push.** Each reaction moves the body the way that blow pushes it. Light 1 twists him right. Heavy 3 twists him 40 degrees left. The kick and bash drive him back.
- **Feet.** Both feet stay planted in every clip. Each one starts on the frame of contact, peaks two to five frames later and ends back in the guard pose.

![The eight brigand hit reactions](assets/img/gallery/devlog58_brigand_reactions_1121.png)

The first reaction, to Light 1, was reviewed and approved. All eight were then rendered into one review video with a side view and a view from Owain's sword side. That group is waiting for review.

## Open questions before wiring

- **How many reactions.** The game has one light and one heavy reaction slot for enemies. Using all eight clips needs the game to know which attack landed. The other choice is four slots: light, heavy, kick and bash.
- **Clip speed.** The light reaction state lasts 0.35 s. A 0.67 s clip would play almost twice as fast unless the state time changes.
- **Kick and bash aim.** At the hit frame, Owain's kick foot lands 36 cm to the side of his forward line, and the shield 15 cm. A small aim angle may be needed for both.
- **Seax guard.** The brigand's seax guard holds the left hand up as if it carried a shield. It is on the list for the idle and guard check.

## Changes to the plan

- **Gate 2 passed.** The Phase 2 demo was accepted.
- **Blood and sparks added to the melee rework.** A first pass is in. Better pool and splat looks and blood that fades come later.
- **Phase 3 order.** Hit reactions first, then a seax attack group (light, two-hit combo, heavy and a shove kick).

## Next

- Review of the eight reactions and answers to the wiring questions.
- Export the reactions to Unreal, wire them in and record a fight video.
- Seax attack clips for the brigand.
