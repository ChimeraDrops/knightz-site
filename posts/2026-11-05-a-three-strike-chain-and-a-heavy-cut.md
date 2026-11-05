---
title: Dev Log #43: A three-strike chain and a heavy cut
date: 2026-11-05
---

The hand audit of Owain's sword and shield clips in Blender reached its first attacks. 33 of his 76 clips are now approved: all 26 movement and guard clips, the four dodges and the three light attacks. The light attacks now chain into a three-strike combo. The heavy attack was rebuilt from key poses, and its downswing is approved.

![Owain's light attack chain](assets/img/gallery/devlog43_light_chain_timing_1104.png)

## The light chain

Each light attack used to play on its own and return to guard. They now link into one combo:

- **Light 1** is a diagonal slash from the right shoulder to the left hip. The middle of the cut was re-angled so the blade stays at an angle through the slice and does not punch forward.
- **Light 2** is a rising backhand. The heel of the hand leads the blade up.
- **Light 3** is a full vertical cut downward that recovers to guard.

Each clip starts on the exact pose where the one before it branches. The seams were measured at 0.000 degrees on every bone, so the chain plays as one move with no blend. Light 2 and Light 3 are now chain-only moves. The full chain runs 81 frames, under three seconds.

## When a click counts

A click opens a window. The branch always fires on the same frame, so the pose seam stays exact:

- **Light 1** branches at frame 31. Clicks count from frame 24 to frame 34, a window of about a third of a second.
- **Light 2** branches at frame 18. Clicks count from frame 12 to frame 21.
- **Early clicks are ignored.** A click before the window is not stored, so mashing during a swing does not chain.
- **Late clicks still work** for up to three frames after the branch frame. The next attack starts at once with a short 0.1 second blend.

The early side of each window is the one to tune first. The late side stays at three frames or less, since a longer late branch would show the blend.

## The heavy attack

![Blade speed through the heavy downswing](assets/img/gallery/devlog43_heavy_swing_speed_1104.png)

The heavy attack had good footwork and a good shield arm, but the sword stroke was too upright and did not read as a heavy blow. The goal is one powerful downward cut that passes from the opponent's head to the groin, with the blade held in a single plane the whole way.

The first rework was rejected. It solved the body frame by frame to keep the shoulder on the cut plane. The hips slid about 44 cm sideways during the cut, so the body drifted instead of driving the blade, and a locked knee followed. The numbers passed, but the motion did not look like a real strike.

The second rework went back to the original clip and worked pose to pose:

- Key poses for the arm and spine were set by hand for the first frames of the cut and for the end of the strike.
- The path between them is a smooth curve through those poses. On every frame the arm and wrist are turned so the blade sits on the cut plane.
- Feet and hips stay planted for the whole cut.
- The elbow stays bent between 115 and 156 degrees. No joint locks straight.

The first version of this pass took 19 frames. It looked solid but too slow, with a top blade speed of 16.5 degrees per frame. Frames were then removed through the middle of the downswing while the top and bottom of the cut were kept. The approved swing runs 13 frames. The blade speeds up on every frame to a peak of 29.4 degrees per frame and then slows into the follow-through. It stays on the plane with no measurable error, and the shoulder stays within 1.2 cm of it. The closest the blade comes to the legs at the end of the cut is 7.5 cm.

## Changes to the plan

- **The light attacks are now a three-strike combo** with fixed branch frames and click windows. Early clicks are not buffered.
- **The heavy attack will open a new three-swing combo** of its own. The second swing in that combo is still to be designed.
- **Hand-edited attacks start from agreed key poses** for the whole body before any in-between frames are made. Each change is reviewed by eye from the review cameras, not only by the numbers.

## Next

- Build the recovery after the heavy cut, or the transition into the heavy combo.
- Continue the audit with the shield bash and the rest of the 76 clips.
- Return the edited clips to Unreal, add the combo windows to the attacks and test them in a fight in the demo clearing.
- Animal hand pass, review and batch import into Unreal.
