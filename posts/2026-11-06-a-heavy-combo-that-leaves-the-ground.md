---
title: Dev Log #44: A heavy combo that leaves the ground
date: 2026-11-06
---

Owain's heavy attack now opens a three-swing combo. The downward cut flows into a shield smash and ends in a jumping spin with a backhand cut. All three swings are approved. The shield bash was rebuilt by hand, and a push kick is in progress. 34 of the original 76 clips are approved, plus two new clips for the combo.

![Owain's heavy attack chain](assets/img/gallery/devlog44_heavy_chain_timing_1105.png)

## The heavy combo

- **Heavy 1** is the downward cut approved in the last log. It branches into the next swing at frame 59.
- **Heavy 2** is a shield smash. The back leg steps a full stride past the front foot and the hips turn almost 200 degrees. The shield arm cocks back, then drives about 150 cm in six frames into the opponent's chest. The sword hand ends palm down with the blade trailing, set up for the backhand. It branches at frame 25.
- **Heavy 3** is a jumping spin. Owain pushes off the lead leg, lifts both knees and turns clockwise in the air with the heel of the hand leading the blade. He lands in the same stance the combo started from and recovers to guard.

Each swing starts on the exact pose where the one before it branches. The full chain runs 140 frames, under five seconds. Each clip also has its own recovery to guard, so the combo can stop after any swing.

## The jump

![Hips and shoulders through the jumping spin](assets/img/gallery/devlog44_heavy3_spin_1105.png)

The spin carries the clockwise turn from the shield smash. There is no wind-up in the other direction and no turn before the jump.

- **In the air, the hips lead.** The shoulders trail the hips by about 50 degrees, which loads the swing.
- **Past three quarters of the turn, the shoulders catch up.** They speed up from 25 to 45 degrees per frame and finish 30 degrees ahead of the hips at touchdown. The second half of the turn is faster than the first, so the move lands with weight.
- **The legs follow the hips.** The thighs stay square to the hip facing through the spin, so the legs never look splayed to the camera.
- **The head spots like a dancer.** It stays square with the shoulders until halfway, then snaps to the target before touchdown.
- **The landing is absorbed.** The pelvis drops 9 cm through the knees, then returns to stance height. One foot stays planted while the other steps back into guard.

The first pass stopped the blade dead right after touchdown. A follow-through was added to the sword arm so the blade keeps turning after the landing and slows over five frames before it returns to guard.

## Shield bash and kick, rebuilt

The original shield bash take was a sword swing, and the original kick was a side kick with a sliding support foot. Both are being rebuilt by hand in Blender. Key poses are set first and checked by eye, then the in-between frames are built.

- **Shield bash:** a hard shove with the shield arm and shoulder while stepping in with the left foot, then back to guard. Impact lands on frame 13 of 34. The shield face stays square to the target from the wind-up through the hold. The key poses are approved and the in-between frames are in review.
- **Kick:** a straight push kick. The right knee chambers high, the sole drives out at stomach height with the hips thrusting forward and the body leaning back, then the foot re-chambers and returns to its start spot. The shield comes up to the chest and the sword cocks high beside the head. Key poses are in review.

## Changes to the plan

- **The heavy attack is now a three-swing combo** with two new clips, a shield smash and a jumping spin.
- **No clips go back to Unreal until the whole audit is done.** All edited clips will be exported in one pass, with combo windows and hit timing added at that point.
- **New arm rules for every clip.** The wrist stays neutral, and the arm pose is chosen so the blade lands where it should. Every frame is checked for elbow bend, arm twist and blade clearance before review.

## Next

- Approve the shield bash in-betweens and finish the push kick.
- Continue the audit through the rest of Owain's 76 clips.
- Set the click windows for the heavy combo, then export every edited clip to Unreal in one pass and test the combos in the demo clearing.
- Animal hand pass, review and batch import into Unreal.
