---
title: Dev Log #20: From motion library to fighting stance
date: 2026-10-12
---

Yesterday's motion library moved into Unreal today. All 883 clips now play on the game skeletons, and the first full pass over basic movement is done for every weapon set on both male bodies. Most of the day went into one question: does the character look like a fighter when he holds a sword and shield?

## Into Unreal

The generated clips use a standard research skeleton. Two retargeters map them onto our standard male and large male skeletons, and root motion is rebuilt from the pelvis so every walk, jog and turn carries its own travel. 726 clips landed on the standard body and 157 on the large body.

The first batch crashed the editor. The batch ran from an editor tick, and source control re-entered that tick while it copied assets until the stack overflowed. Plain batches of 11 clips with a save after each fixed it.

## Standing on the floor

Every generated clip stood about 7 cm above the ground. The ball of the foot sat at 10 cm, where Unreal's own grounded idle sits at 1.5 cm. Lowering the pelvis alone did nothing in game, because the leg solver aims the feet at separate foot targets. Both the pelvis and the foot target root now drop 7 cm on every key of every clip.

![Ball of the foot above the floor, before and after the ground fix](assets/img/gallery/devlog20_ground_fix_1012.png)

## A review room in the editor

A new review level shows eight copies of one character on a diamond, one clip per direction, so a full eight-way set reads at a glance. A toolbar pages through the library eight clips at a time. Any clip can be tagged as approved, needs an edit or bad, with a short note. The tags are saved, and fixes are worked from that list.

Characters play in place, the way the movement capsule will drive them in game, with weapons and shield attached through their sockets.

## The stance problem

The review showed one problem on every weapon clip: the arms. The model knows how people walk. It does not know how a man holds a round shield. In the sword and shield guard, the shield arm sat over the head.

The fix keeps the motion and replaces the pose:

- The start frame is re-posed with inverse kinematics.
- The change is applied as a constant offset on every frame, so timing and weight stay the same.
- The shield arm is held fixed to the chest. The source walk swung the arm, and that swing drove the shield 14 cm into the thigh.

The approved guard: head forward with the chin slightly up, sword hand off the right hip with the point forward and a little up, shield boss out over chest, stomach and left side, eyes over the rim.

![Shield clearance after the fix, measured on every frame](assets/img/gallery/devlog20_shield_clearance_1012.png)

## One step cycle per clip

Long multi-step clips do not blend well. Each directional walk and jog is now cut to exactly one gait cycle, left step and right step, with the last frame matching the first. Foot-strike markers on every clip let the blend space keep the feet in phase when the player changes direction mid-stride.

Some directions came out wrong. The back-right guard walk travelled back-left. One side-step started with a half step the wrong way. Those clips were trimmed, slowed or swapped for a cleaner take from another weapon set, then checked again. The sword and shield set now has a first blend space built from the measured speeds.

![Travel direction and speed of each looping clip](assets/img/gallery/devlog20_locomotion_cycles_1012.png)

## Two ways to walk

Movement is now split into two sets:

- **Free movement:** upright, shield lowered at the side, sword arm relaxed, normal stride. The character turns to face where he walks.
- **Combat lock-on:** shield up, sword ready, facing the enemy while he strafes in eight directions.

The guard is reserved for lock-on. A knight who walks to the well in full guard looks wrong.

## The whole set, first pass

The same rules then went across every set on both bodies:

- Sword and shield, axe and shield, sword alone, seax, spear, unarmed and bow.
- Brigands and the three undead bodies on the standard skeleton, plus the large undead.
- Turn-in-place clips now carry their rotation in the root, so the capsule turns with the feet.

Every clip is checked by script: direction of travel, loop seam, weapon clearance against legs, body and shield, and joint limits for twisted forearms or locked elbows.

## Wrists set free

The hand grip layer used to override the whole wrist with one fixed grip, so the blade direction could only come from the forearm. It now drives the fingers only. Each clip owns its wrist, and a new arm solver rebuilds the arm on every frame: it keeps the blade direction, keeps the elbow low and close to the body, and holds the wrist inside natural limits.

On 150 sword clips the blade lands within 1 degree of its target and stays at least 9 cm clear of the body. The spear grip moved 40 cm down the shaft for a two-handed guard. Unarmed characters now make fists.

## Still open

- The forward dodge and all undead crawls need new takes.
- The large body still needs weapon sockets and the grip layer.
- A relaxed jog for free movement is not built yet.

## Next

Review the first pass in the review room, regenerate the flagged clips, give the large body its weapons, and start on attacks.
