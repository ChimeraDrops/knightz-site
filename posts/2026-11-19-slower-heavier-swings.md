---
title: Dev Log #56: Slower, heavier swings
date: 2026-11-19
---

Work started on a rework of the melee for the combat demo. The aim is slower fights where every swing has weight. Owain's six sword and shield attacks now play at the speed they were animated, chains start on set combo frames, and the body turn that aims his strikes was measured again on the full reach of the blade. The test arena now uses a demo brigand, and the camera no longer gets pulled in by enemies.

![Full length of each attack, before and now](assets/img/gallery/devlog56_attack_length_1119.png)

## A plan for the melee

The rework runs in phases. Each phase ends at a gate where the fight is played and approved before the next one starts.

- **Attacks at clip speed.** Swings play as animated, with a clear wind-up and follow-through.
- **Soft sync for open exchanges.** Attacks keep their own timing. Distance and facing snap into place, and the enemy's reactions are timed to the hit frames.
- **Paired clips for two moments only.** The broken parry and the arm sever play as true paired animations.
- **One attacker at a time.** Other enemies hold back while a paired clip plays.
- **Demo opponents.** Six brigands in waves of one, two and three, armed with a seax and no shield.

## Attacks at the animated speed

Before, every light attack was squeezed into the same 0.67 s and every heavy into 1.37 s. Light 1 played almost three times faster than it was animated.

- **Speed.** The three lights now play at 1.0x. The three heavies play at 1.2x after the first play test asked for a little more pace.
- **Done frames.** Each attack ends on the first frame where the body has settled near guard. The slow tail into guard is cut by the game, so no clip needed trimming.
- **Hit times.** The light hits now land at 0.70, 0.60 and 0.30 s. The heavy hits land at 1.56, 0.36 and 0.72 s.
- **Chains.** A full light chain lands its third hit 1.97 s after the first press. A full heavy chain lands its third hit at 3.09 s.
- **Clip scan.** Hands, feet, pelvis and head were tracked on every frame of eight clips. Only the first heavy has a slow lead-in (frames 0 to 9). It stays for now as a trim candidate.

## Combo frames

- **Built-in matches.** The attacks were animated as chains. The first pose of each follow-up matches a frame in the attack before it exactly.
- **Combo frame.** A press during an attack is held and the next swing starts on that matching frame. Before, a press was dropped after a quarter of a second.
- **Cancels.** Guard and dodge cancel from the same frame.

## Body turn, second pass

Play testing with a lock-on showed the blade still sweeping about 45 degrees left of the enemy. The first fix had aimed the frame where the blade tip crosses the line to the enemy. In a slash the hand leads and the blade trails, so the sword reaches full extension later and much further left.

![Body turn per attack, first fix and now](assets/img/gallery/devlog56_body_turn_1119.png)

- **New measure.** The blade angle and its distance from the body were read on every frame. The strike direction is where the blade sits at 97 percent of its reach or more.
- **New turn.** Light 1 now turns 50 degrees, Light 2 35 and Light 3 84. Light 3 is a downward chop far to the left of his facing.
- **Chains.** A chained attack eases its turn on from where the last one left off, with no snap back between swings.
- **Result with a lock-on.** Light 2, Heavy and Heavy 2 land within 1 degree of the target. Heavy 3 lands within 5. The Light 1 sweep crosses the enemy at full reach.
- **Later.** The lasting fix is to turn the root inside the clips in Blender. The game turn can then go back to zero.

## Retuning around the slower pace

- **Break damage.** Light swings land less often in a chain, so each one now adds 13 to the guard break meter (was 8). Each heavy adds 30 (was 22). The meter breaks at 80.
- **Brigand tells.** Brigand wind-ups are longer: 0.60 s for light attacks, 1.0 s for heavies and 0.55 s for the kick.
- **Gaps.** Brigands now wait 2.5 to 4.5 s between attacks and 1.5 to 3.0 s before their first.
- **Stamina.** Unchanged. A test at higher costs emptied the bar on one heavy chain and caused a stamina stun.

## Camera

- **Problem.** The camera sometimes moved in close behind Owain and the view was lost.
- **Cause.** Enemy bodies blocked the camera's collision test. An enemy between the camera and Owain pulled it in.
- **Fix.** Enemies are now ignored by the camera. In a test with a brigand placed on the camera line, the distance held at 4 m.

## Changes to the plan

- **Slower melee.** Attacks play at their animated speed and the brigands get longer wind-ups to match.
- **Soft sync for most of the fight.** Full paired clips are kept for the broken parry and the arm sever.
- **One attacker at a time** in the demo.
- **The demo uses brigands only,** in three waves, with the arm sever as the one sever move.
- **The brigand's shield bash becomes a shove kick,** since demo brigands carry no shield.

## Next

- Finish the Gate 1 play test of tempo, chains, tells and break damage.
- Phase 2: turn the root inside the clips, set a strike distance per attack, and snap distance and facing.
- Brigand reaction clips timed to Owain's hit frames.
