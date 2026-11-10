---
title: Dev Log #48: A grapple built for two bodies
date: 2026-11-10
---

Owain's grapple is rebuilt and approved. A grappling enemy grabs him from the front and goes for his neck. He holds it off with his shield while the player mashes the attack button, then shoves it away. Both parts are synced pairs: Owain and the enemy each have their own clip on one shared timeline. The audit now stands at 51 of Owain's 76 original clips approved, plus two matching enemy clips.

![The grapple, beat by beat](assets/img/gallery/devlog48_grapple_beats_1109.png)

## The struggle

The struggle is a seamless 40-frame loop. It plays for as long as the player is mashing. Other enemies can still hit Owain while he is held.

- **Owain.** His feet stay planted in his guard stance. The shield rim is jammed under the enemy's jaw for the whole loop. His sword fist pushes forward with the blade raised out to his right, and his head is turned away.
- **Two shoves.** On frames 8 and 28 he leans in and drives the shield out to about 45 cm in front of him. His hips and shoulders twist into each shove. The first is stronger than the second.
- **Two lunges.** On frames 16 and 35 the enemy lunges with its whole body. Owain is driven back to a lean of about 16 degrees, braces lower and the shield is pushed in to about 26 cm.

The loop was built two cycles long and the second cycle kept, so the seam has no jump.

![Push and pull inside the struggle loop](assets/img/gallery/devlog48_struggle_push_pull_1109.png)

## The enemy side

The enemy clip was authored against Owain's, frame by frame.

- **Chin on the rim.** The chin stays within 1.6 cm of the shield rim on every frame. Lunges push the pelvis and torso forward and bring the head over the rim.
- **Jaw.** The jaw opens two or three frames before each lunge and snaps shut at the peak. There is a double snap on frames 19 and 20 and chatter in between.
- **Right hand.** It reaches over the top corner of the shield and grips Owain's left shoulder, palm down. The grip pose was set by hand and is held within 1.5 cm on every frame while both bodies move.
- **Left hand.** It clamps Owain's sword forearm.

The heads stay at least 38 cm apart. Two small contacts were accepted at approval: the forearms graze the shield edge on the shove frames, and the chest stops 6 to 8 cm short of the shield on the lunges.

## The escape

When the mash succeeds, both bodies switch to their escape clips on the same frame. The first frame of each matches the struggle exactly.

- **Wind-up.** Owain shifts his weight to the rear foot, crouches and leans back. The shield holds still so the enemy's arm stays clear.
- **Step and drive.** The front foot steps in 25 cm. His hips and shoulders drive the rim up and forward into the jaw. Contact lands on frame 11 with the rim 79 cm in front of him. The rear foot follows.
- **Recover.** He reaches the exact first frame of his guard loop on frame 36. Block and dodge can cancel from there.

The enemy rides the rim until contact. On frame 11 its head snaps back, the grips tear loose and both arms fly up and out. It staggers back three steps, about 1.1 m, and ends hunched forward facing Owain, arms low and reaching. It takes control again on frame 40. Owain's blade stays at least 4.7 cm clear of it on every frame.

## How it was checked

- **Same tools as the single clips.** The joint check ran on every frame of all four clips. No joint bends the wrong way.
- **Whole-chain arm solve.** The enemy's gripping arm is solved from spine to wrist on every frame, with the elbow kept over the shield corner and away from its own body.
- **Hand-set pose first.** The grip pose was matched before any other frame was built: 0.02 cm and 0.24 degrees.
- **Balance flags reviewed.** The remaining balance flags fall on the step-in and the stagger, where the body is meant to be off balance.

## Changes to the plan

- **Grapples use paired clips.** Takedown victims go to rag doll, but grapples keep a matching enemy clip on both the hold and the release.
- **Enemy clips are built on a stand-in body.** They will be retargeted onto the enemy bodies when those are built.

## Next

- The downed struggle and escape, hazards, death, get-up, item use, parry, guard break, block and hit reactions. 25 of 76 remain.
- Combo windows and hit timing, then one export pass of every edited clip to Unreal and a fight test in the demo clearing.
- Animal hand pass, review and batch import into Unreal.
