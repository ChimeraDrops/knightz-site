---
title: Dev Log #45: Severing cuts and a stricter joint check
date: 2026-11-07
---

Owain's severing attacks are rebuilt and approved: two arm cuts, a leg cut and two ways the cut can fail. The push kick is approved too. A stricter joint check now runs on every frame before a clip goes to review, and every approved clip was checked again with it. 42 of Owain's original 76 clips are approved, plus the two new heavy combo clips.

![Owain's arm cut, blade angle and body turn by frame](assets/img/gallery/devlog45_arm_cut_1106.png)

## The arm cut

The original arm cut take swung a two-handed sword while Owain held a shield, and his body barely moved. It was rebuilt by hand as a one-handed downward chop, matched to the downward slice in the light combo.

- **Step and load.** Owain steps 22 cm forward with the lead foot. His weight goes back and the shoulders wind about 25 degrees past the hips.
- **Wind-up over the top.** The blade rises over his head and ends level behind him, pointing back.
- **Whip through.** Hips and shoulders turn through together and impact lands on frame 13 of 36. The blade keeps cutting down through the arm for four more frames, then he rises back to guard.

The first passes forced a fixed blade angle onto the old hand path. That bent the wrist too far and in some frames pushed the elbow backward. The fix was to pose the sword by hand at three key frames (top of the wind-up, top of the swing, impact) and then solve a natural arm around each pose. That is now the standard method for sword clips.

## The full severing set

- **Right arm cut:** the one-handed chop above.
- **Left arm cut:** built from the right arm cut, with the cut plane turned 22 degrees to reach the other arm. Impact on frame 13 of 36.
- **Leg cut:** the sword arm extends and the blade stays level at knee height. It reaches the leg on frames 14 to 15 of 59.
- **Failed cut, disarmed:** an upward chop that the opponent dodges. Owain's shoulder, elbow and forearm were corrected.
- **Failed cut, stuck blade:** starts on the exact frame where the leg cut lands. Owain tugs twice, steps in and push kicks the opponent off the blade, then returns to guard. Rebuilt from 90 frames down to 55.
- **Head cut:** approved as it was.

## The push kick

The straight push kick from the last log is approved. Contact lands on frame 14 of 34, and the move carries Owain 28 cm forward.

## A stricter joint check

The old check measured knee and elbow bend and little else. It passed a thigh twisted over 100 degrees and a sword hand sitting behind the elbow. The new check runs on every frame shown for review:

![The joint check limits](assets/img/gallery/devlog45_joint_check_1106.png)

- Twist around each bone's own long axis, against the guard idle pose.
- Knees and elbows bend the natural way, and the kneecap points over the foot.
- Shoes stay above the floor.
- Balance stays over the planted foot when the other foot is lifted.
- Shield and blade stay clear of the body.

Every flagged frame is also checked by eye from two angles before anything changes, since a strike can pass a limit on purpose. All approved clips were checked again. Only the shield bash needed changes: the rear foot now stays on its toes with the heel up during the lunge, the shield is loaded further forward so it clears the neck, and the rear foot slides forward on the recovery instead of hovering.

## Changes to the plan

- **Every animation clip passes the joint check before review.** No exceptions for key poses.
- **Sword clips start from hand-posed swords** at the key frames. The arms are solved around them.
- **The severing set is rebuilt.** The failed stuck-blade cut now chains straight off the leg cut.

## Next

- Finishers, stealth kills and the rest of Owain's 76 clips.
- Set combo windows and hit timing, then export every edited clip to Unreal in one pass and test the fights in the demo clearing.
- Animal hand pass, review and batch import into Unreal.
