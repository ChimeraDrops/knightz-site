---
title: Dev Log #57: Every swing lands on the brigand
date: 2026-11-20
---

Phase 2 of the melee rework is built and measured. Each of Owain's attacks now has a set strike distance. Before the hit, he slides to that distance and turns to face the enemy, so the blade meets the target. In a test of twelve swings from close and from 3 m away, every hit landed within 10 degrees of the target line.

![Distance to the brigand at the hit frame](assets/img/gallery/devlog57_strike_distance_1120.png)

## Distance and facing

- **Strike distance.** Each attack was measured in Blender at its hit frame. The strike distance is how far from Owain the middle of the blade sits at that moment. It runs from 92 cm on Heavy 3 to 152 cm on Light 3.
- **The slide.** On every frame before the hit, the game predicts where the clip's own forward travel will put Owain. It then moves him along the line to the enemy so the enemy ends up at the strike distance. The slide finishes just before the hit.
- **Both ways.** He slides back as well as forward, so an enemy standing too close is still hit with the middle of the blade.
- **Limits.** A slide covers at most 1.5 m per attack at up to 9 m per second. Walls and bodies stop it, and the attack then plays in place.
- **Targets.** The slide uses the lock-on target, or the enemy in front of him when there is no lock-on. The arm sever uses the enemy it was opened on.
- **Brigands.** Brigands slide to their own strike distance during their wind-up. Their values are estimates for now (95 cm for seax swings, 85 cm for the kick) until their new clips are made.

## Turning the root in the clips was dropped

The plan was to turn the root inside each attack clip in Blender. Measurements showed it would change nothing on screen.

- **Same result.** At the hit frame, the blade direction matches the turn the game already applies within a few degrees.
- **Root motion.** The attack clips carry their own forward travel. A turn on the root would be taken out of the clip and replaced by the game's facing turn anyway.
- **Result.** The per-attack turn values stay in game data. No clip was changed or exported.

## Turn values corrected

- **Light 2.** The turn was 35 degrees. In play it put the blade 22 degrees right of the target at the hit. It is now 14 degrees, which matches the blade angle measured in Blender.
- **Arm severs.** The left sever now turns 0 degrees and the right sever 24 degrees. Both were 11.

## Test results

The test brigand was held in place while Owain ran full light and heavy chains from 1 m and from 3 m. The game was paused at each hit frame and the positions read back.

![Blade angle against the target line at the hit frame](assets/img/gallery/devlog57_blade_angle_1120.png)

- **Distance.** Every hit landed within 2 cm of its set strike distance.
- **Angle.** Light 2, Heavy and Heavy 2 land within 3 degrees. Light 1 and Light 3 land within 6. Heavy 3 lands within 9. It sweeps about 45 degrees per frame through the hit, so a small timing offset shows as a larger angle.
- **From 3 m.** The first swing closed about 1.6 m and still landed on target.

## Input fix

A light or heavy pressed early in an attack was sometimes dropped when a hit-stop followed. The hit-stop slows the attack's own timer, so the press looked older than it was. Presses are now timed against world time.

## Not tested yet

- The two arm severs. They open only after a broken parry, which the test setup cannot produce yet. They use the same slide.
- The brigand slide against Owain.
- A slide stopped by a wall or another body.

## Changes to the plan

- **No root turn in the attack clips.** The game turn stays as the facing method. The slide handles distance.

## Next

- Gate 2 play test: every swing landing from close and from range, whether the slide reads as a step or as skating, the new Light 2 turn, both arm severs and the brigand closing in.
- Phase 3: about 24 brigand reaction clips timed to Owain's hit frames.
