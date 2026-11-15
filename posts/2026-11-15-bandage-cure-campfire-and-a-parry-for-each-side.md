---
title: Dev Log #52: Bandage, cure, campfire and a parry for each side
date: 2026-11-15
---

Four more of Owain's original clips are approved: using a bandage, drinking a cure, resting at a fire and the single swipe parry. The fire rest is now three clips and the parry is now two. The audit stands at 61 of Owain's 76 original clips.

![The bandage, cure and fire rest clips, beat by beat](assets/img/gallery/devlog52_field_care_1115.png)

## Using a bandage

The old clip pushed his shoulders out of place. The new one is 7.1 seconds.

- **Weapons down.** He steps back, kneels on his left knee and bows forward. The sword goes flat on the ground with the blade forward. The shield goes face down beside it.
- **Bandage.** He sits up, holds his left forearm across his front and winds the bandage around it with his right hand.
- **Weapons up.** He bows again, takes both, stands and steps forward into his idle pose.
- **Shoulders.** Shoulder width stays within half a centimetre of his idle pose on every frame.
- **In game.** The weapons leave his hands while they rest on the ground and return when he picks them up.

## Drinking a cure

No kneel this time. It runs 4.3 seconds.

- **Sword in the ground.** He chops the sword down and lets go. It turns upright and sticks in the ground, about 36 cm from his nearest foot.
- **Drink.** His sword hand goes to the pocket at his right hip with the elbow out to the side. He raises the bottle, tips his head back and drinks, then tosses the bottle to his right.
- **Back in hand.** He bends, takes the hilt in a reverse grip, pulls the sword straight up, flips it to a normal grip and returns to idle.
- **Shoulder fix.** An early version wrung the shoulder during the reach to the pocket. The elbow now swings away from the body and the forearm bends and turns instead.

## Resting at a fire

Resting at a fire heals Owain, repairs his weapons and lets him make cures and field items. A fire is always safe. The rest is split into three clips that chain together: sit down (3.4 s), rest loop (4 s) and get up (3.7 s).

- **Sit down.** The same sword throw as the cure. He kneels and swings the shield round in front of him, standing on its rim between him and the fire.
- **Rest.** Both wrists rest on the top rim with the hands hanging relaxed over the front. The loop has slow breathing and a small turn of the head.
- **Get up.** His left hand goes back to the shield grip. He leans over the shield, takes the hilt from above in a normal grip and pulls it free before he stands.
- **Hands.** The relaxed hands took several rounds. Fingers lie side by side with a natural curl and the hand droops only a little from the forearm.
- **Dropped idea.** A cross-legged sit while sharpening the sword was the first choice. The transitions down to and up from the ground did not hold up, so it became a kneel.

## A parry for each side

![The left and right parries: shield contact points and shoulder turn](assets/img/gallery/devlog52_parry_sides_1115.png)

A parry is a block pressed just before a hit lands. The shield knocks the attack aside, wears down the enemy's guard and sends the enemy stumbling. Owain is back in guard and can act at once.

The single swipe parry is now two clips, picked by the arm the enemy swings with.

- **From his right.** The shield snaps across his body to meet the swipe on frame 5, then pushes out. His shoulders turn 28 degrees into it.
- **From his left.** The shield is already on that side, so this is a short outward punch. His shoulders turn 13 degrees the other way.
- **Timing.** Both are 22 frames. Owain is back in his guard pose on frame 18 and can act from about frame 12.
- **Checks.** Both pass the joint check and the mesh scan with no hits.

## Changes to the plan

- **Rest at a fire** is now three chained clips, sit down, rest loop and get up, with a kneel in place of a cross-legged sit.
- **The parry set is five clips:** single swipe from the right, single swipe from the left, double swipe, heavy and grab or bite. Unreal will pick the side from the enemy's swinging arm.
- **Weapons in the ground.** For the cure and the fire rest, Owain sticks his sword upright in the ground and takes it back after.

## Next

- The double swipe parry is in review. The heavy and the grab or bite parries come next.
- After the parries: broken parries, blocks and hit reactions. 15 clips remain.
- All edited clips go back to Unreal in one pass when the audit is done.
