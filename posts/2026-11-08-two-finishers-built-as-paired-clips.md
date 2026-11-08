---
title: Dev Log #46: Two finishers, built as paired clips
date: 2026-11-08
---

Owain's first two finishers are rebuilt and approved. One ends a crawling enemy on the ground. The other is a beheading cut on a standing opponent. Each finisher is built together with the enemy's own clip on one timeline, so the blade and the body meet on the exact frame. The audit now stands at 44 of Owain's 76 original clips approved, plus two new heavy combo clips and six new enemy clips.

![Both finishers, beat by beat](assets/img/gallery/devlog46_finisher_beats_1107.png)

## The ground finisher

Owain flips his sword into a reverse grip, walks in and drives it straight down through the skull of an enemy crawling at his feet. The clip went from 90 frames to 71.

- **Toss and catch.** A wrist flick tosses the sword on frame 9. It flips and lands in a reverse grip on frame 19.
- **Two steps in.** His weight shifts and he leans before the first step. A left step, then a right half step. The hips turn into the step and square up as the trailing leg arrives.
- **Wind-up.** The back arches, the right shoulder pulls back and the weight goes back.
- **Drive.** The whole body drives down. Hips drop 18 cm, knees bend to about 97 degrees and the trunk folds about 50 degrees. The tip reaches the skull on frame 43 and the ground on frame 45.
- **Pull and recover.** He pulls the blade straight up while still leaning in, rises, and flips the sword back to a normal grip on frame 66.

The shield arm is never locked. It moves against the weight shift, swings with the stride and lags slightly behind the body.

## Five ways to meet it

The enemy has five clips, one for each direction Owain can come from. In each, it turns toward him while crawling and lifts its head into the strike. All five are identical from the stab onward.

![The enemy's clip is picked by approach angle](assets/img/gallery/devlog46_approach_angles_1107.png)

The turning crawls looked mechanical when built in code. They now come from the local motion model: eight takes per prompt, scored on turn angle, body tilt and hip height, with the best two shown side by side for review. The game picks the clip from the approach angle, and Owain's two steps stretch in Unreal to meet the skull where it ends up.

## The beheading finisher

The original take was replaced with a hand-built horizontal cut. The neck is struck on frame 31 of 67.

- **Step and load.** Owain shifts onto his right leg, pivots the left foot on the ball and strides. The sword rises to a load with the elbow out to the side and the hand by his temple.
- **Circle.** The blade circles behind his head. The hips fire first and turn about 90 degrees. The shoulders follow and turn about 100.
- **Draw cut.** The palm faces up, the pommel leads and the blade trails through the neck.
- **Step through.** The hand carries on across. He steps through, lands beside the body and returns to guard.

The opponent raises its arms in defence, kept below and clear of the blade. After the cut it goes limp, sinks to its knees on frame 46, falls forward and lies still. The loose arms are simulated: gravity, the floor, both bodies, and limits on how far each shoulder and elbow can move.

## What changed in the method

- **Walking steps check reach first.** A long step out of the wide guard stance forced a split and a dragged trailing leg. Foot targets are now checked against leg length before a step is built.
- **Owain walks tall.** The hips sit 6 to 8 cm higher while walking and drop only for the strike.
- **Turn the body more.** When an arm cannot reach a pose naturally, the hips and shoulders turn further instead of twisting the arm.
- **Arms are blended by direction.** Blending raw joint rotations between very different poses produced a flip in the shoulder.

## Changes to the plan

- **Finishers are built as pairs.** Owain and the enemy share one timeline. The contact point and frame are fixed; everything else is free.
- **Hard human motions come from the motion model.** Crawls, grapples and falls get generated reference takes before any hand work.
- **Six new enemy clips** join the export list for Unreal.

## Next

- The next finisher, a stealth kill, and the parry and block reactions, then the rest of the 76 clips.
- Combo windows and hit timing, then one export pass of every edited clip to Unreal and a fight test in the demo clearing.
- Animal hand pass, review and batch import into Unreal.
