---
title: Dev Log #28: The women start to move
date: 2026-10-21
---

The female body now has its own movement set in production. Every clip is generated fresh for her build, then cut, checked and fixed by the same rules that shaped the men's set. The first two weapon sets are through the pipeline, and generation for the rest is running.

## Her own motion

The women could have borrowed the men's clips through retargeting. That keeps the timing and weight of a larger man, so the plan changed: every movement clip for the female body is generated new from a written prompt, and a retargeted male clip is used only when no generated take passes the checks.

Each prompt opens with "A graceful, light-footed woman" and then describes the movement. The set covers seven weapon sets: unarmed, sword and shield, sword, axe and shield, seax, spear and bow.

| Per weapon set | Clips |
|---|---|
| Idle and guard idle | 2 |
| Walk in 8 directions | 8 |
| Jog in 8 directions | 8 |
| Guard walk in 8 directions | 8 |
| Turns in place, 90 and 180 degrees each way | 4 |
| **Total** | **30** (21 for the bow) |

That is 201 clips. Attacks, blocks, dodges and hits are left for a later pass.

![Generated walk forward for the female body, side view](assets/img/gallery/devlog28_hf1_walk_strip_1020.png)

## Scaled to her body

Every distance rule from the men's set was measured against her body and scaled.

- Shoulders 0.85 of the healthy male width, arms 0.86, legs 0.885, hip height 0.92.
- Game speeds follow her stride: walk 143, run 295 and guard walk 65 cm per second (men 155, 320 and 70).
- Stance capped at about 50 cm, so a shield or blade never cuts into her legs on side steps.
- Hand and elbow targets for sword, shield, spear and bow were shrunk to her arm length, and the shield checks include her chest.

Weapon sockets were fitted to her hand before any arm work. Close-ups confirmed the grip on the sword, shield, spear, axe and seax: handle inside the fist, thumb over, blade continuing the line of the forearm.

## Generate, cut, check

Each clip is generated with eight random seeds, and the four best are kept. Source takes run long (6 seconds for walks, 8 for idles) so the cleanest stretch can be picked. From there:

1. One gait cycle is cut from each take and the loop seam is crossfaded to 0.0 cm.
2. An audit measures direction, speed, hip turn, lean, ground height and foot slide.
3. Any take that steps the wrong way, even for half a step, is rejected.
4. If no take passes, the motion is borrowed from another set, regenerated with new wording, or, last of all, taken from the matching male clip.

By the evening of 20 October about 50 of the 201 clips were generated. The sword set and the sword and shield set have 42 loops cut and checked. 28 pass on her own takes, 10 fall back to retargeted male clips, and 4 turns are flagged for another pass.

![Clip status for the first two weapon sets](assets/img/gallery/devlog28_hf1_clip_status_1020.png)

## Lessons from the men's run

Before this run started, every note from the men's animation review was written up as a numeric check. That covers 19 points, from a floating stance and hunched shoulders to a shield swinging into the knee and an elbow sinking into the body. Each one now runs on every clip by script. Clips that pass are then reviewed by hand in the animation review level, with the women dressed and holding their weapons.

## Next

- Finish generation for the unarmed, axe and shield, seax, spear and bow sets.
- Arm passes per weapon set: guard, casual carry and shield arm.
- Blend spaces and an in-game motion test for a playable woman.
- Review of every clip in the review level.
