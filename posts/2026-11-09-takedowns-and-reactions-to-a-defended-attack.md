---
title: Dev Log #47: Takedowns and reactions to a defended attack
date: 2026-11-09
---

Five more of Owain's original clips are rebuilt and approved, now as nine clips. Two are takedowns: a pommel strike that knocks an opponent out and a stealth thrust from behind. Two cover an enemy parrying or blocking his attack. The last is a stun for when his stamina runs out. The audit now stands at 49 of Owain's 76 original clips approved. Each original take was replaced by a new hand-built clip.

![The new clips, beat by beat](assets/img/gallery/devlog47_clip_beats_1108.png)

## Pommel strike

Owain knocks an opponent out with the bottom of the sword. No blade is used. The clip runs 45 frames.

- **Load.** His weight shifts onto the right foot and the left foot pivots on the ball. A left step lands on frame 13. The hand cocks by his right ear with the blade hanging behind his back.
- **Drive.** The hips and shoulders turn, he leans in and the pelvis dips. The pommel drives forward and down.
- **Hit.** The pommel meets the forehead on frame 19 at about 5.4 m/s. The blade tip stays 75 to 88 cm clear of the head.
- **Recover.** A short follow-through, then a step back. He ends in his exact idle pose with no net travel.

The opponent has no matching clip. It goes to rag doll on the hit, pushed along the line of the pommel. This works from any approach angle.

## Stealth thrust

The single stealth kill became two clips of 49 frames each. The game picks one by enemy type.

- **Head thrust.** A high-guard chamber with the hand above the right shoulder. The blade drives 12 degrees downward into the back of the skull.
- **Chest thrust.** A low chamber at the right hip and a deeper lunge. The blade drives 32 degrees upward under the shoulder blade.

Both share one timeline. Owain steps in from frame 8 to 13. The hips and shoulders drive the thrust from frame 13, and full depth is reached on frame 20. He holds, pulls the blade out on the same line from frame 26 to 29, then plays his step-in backwards to return to idle. The entry point moves less than 0.3 cm while the blade is in. The victim goes to rag doll as the blade comes out.

## When an enemy parries

Three clips replace one. The reaction scales with the attack.

- **Light attack parried.** The sword is knocked out wide to his right. The rear foot steps back, then the front foot, with a heel rock. He reaches guard on frame 36.
- **Heavy attack parried.** One clip per swing direction. He is thrown the way the swing was travelling and slightly back, then scrambles through four quick steps. He reaches guard on frame 44.

## When an enemy blocks

Two clips replace one, split by attack weight only.

- **Light.** The blade rebounds up and to his right in four frames. He rocks back and takes two half steps of 20 cm. Guard on frame 24.
- **Heavy.** The blow is stopped overhead and the sword arm is jarred out to his right with the elbow still high. The blade swings level at shoulder height, then rises and comes down to guard. Two steps of 30 cm. Guard on frame 32.

![Where a defended attack sends Owain](assets/img/gallery/devlog47_reaction_travel_1108.png)

All five reactions start on the blade contact frame and end in the exact first frame of the guard loop. Block and dodge can cancel from that frame.

## Stamina stun

When Owain's stamina hits zero he doubles over with his guard dropped. He leans 36 degrees forward over 10 frames. The sword arm hangs beside his thigh and the shield sags in front of the other leg. He takes four heavy breaths while his eyes lift toward the enemy, then straightens to guard on frame 56. His feet stay planted. He is open to attack for the first 50 frames.

## What changed in the method

- **Arms are solved as a whole chain.** Spine, collarbone, shoulder, elbow, forearm roll and wrist are solved together toward the contact point, like an IK rig. Moving one joint and leaving the rest caused errors.
- **Hand-set poses are a contract.** A pose set by hand is stored as a world position and must match within 0.5 cm and 2 degrees before any other frame is built.
- **Real socket spin is measured between keys.** The old twist measure hid flips of up to 180 degrees near overhead poses.
- **Blade clearance from the head is checked on every frame.** The joint check does not cover it.
- **Withdrawals reverse the body with the blade.** Pulling straight back while still lunged forward put the hand at the shoulder.

## Changes to the plan

- **Victims of takedowns use rag doll.** Paired enemy clips stay for the two finishers. Other takedowns hand the victim to physics.
- **Three clips became seven.** The stealth kill and the parried and blocked reactions each split into variants. Combat logic picks the variant by enemy type, attack weight and swing direction.
- **Grapples are synced pairs.** Both bodies share one timeline. The first grapple clip is in progress.

## Next

- Grapple and downed clips, hazards, death, get-up, item use, parry, guard break, block and hit reactions. 27 of 76 remain.
- Combo windows and hit timing, then one export pass of every edited clip to Unreal and a fight test in the demo clearing.
- Animal hand pass, review and batch import into Unreal.
