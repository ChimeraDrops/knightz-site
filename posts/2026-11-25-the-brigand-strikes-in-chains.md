---
title: Dev Log #61: The brigand strikes in chains
date: 2026-11-25
---

The seven motion capture attacks from the last log passed review and are now in game. The brigand chains them into three-step light and heavy combos, the same shape as Owain's own. Work has moved on to the clips for when his swings are stopped, his own defence, dodges and deaths.

## Seven clips approved

All seven retargeted clips were approved. Each one was then fitted to a new guard stance:

- **New guard.** The capture set's own one-handed sword idle is now the brigand's guard loop. Every attack starts and ends within 3 cm of it, so no extra steps were needed to join them.
- **Planted feet.** Feet are locked to the ground wherever they stand still, which removes the 2 to 4 cm sway seen in review.
- **Smooth joins.** Each attack blends in from the guard and back out to it. The captured root motion is kept, so the heavy swings and the kick still carry him forward.

## Chains for the enemy

Enemies can now chain attacks. When an attack recovers, the brigand may go straight into the next step if Owain is still in reach and not down or held in a grapple. Light 2, Light 3, Heavy 2 and Heavy 3 only ever play as part of a chain. Light 1, Heavy 1 and the kick open on their own.

![Brigand attack chains in game](assets/img/gallery/devlog61_brigand_chains_1125.png)

Each clip plays at its captured speed. The wind-up, strike and recovery times were set to match each clip, so nothing is sped up or slowed down. Each attack also has a set strike distance, measured at the moment of contact. The heavy chain closes from about 1.5 m to 1.1 m as he steps in.

## Tested in the fight level

In the one-on-one test level every chain ran in full. The heavy chain landed Heavy 1, 2 and 3 each time, and the light chain landed all three steps in every run. The distance at each strike matched the set value to within 1 cm. Owain played a hit reaction on every blow. A fight recording of four chained sequences went out and was approved.

## Next clips in review

Five review videos cover the brigand's remaining needs, all from the same capture set:

- **Stopped swings.** What he does when Owain blocks or deflects his attack.
- **Defence.** His own blocks and parries.
- **Dodges.** Full, short and skip back.
- **Deaths.** Six falls by direction.
- **Fear and idle.** A surrender, a step back and several guard and idle loops.

![Next brigand clips under review](assets/img/gallery/devlog61_next_candidates_1125.png)

The one-handed set has no bounce-back clip for a stopped single blade. The options are two bounce-backs from the longsword set, which use both hands, and four hit reactions. The candidates were split into one video per clip so each can be judged on its own.

## Changes to the plan

- **Enemy chains are in.** Any enemy with chain clips can now run multi-step combos. Shield-carrying living enemies still use single attacks until they get their own chain clips.
- **Tells follow the clip.** The brigand's wind-ups now come from the captured motion and are shorter than the tells set earlier in the rework. They will be judged in play.
- **New guard stance.** The capture set's sword idle replaces the old seax guard for the brigand.

## Next

- Pick a clip for each stopped swing, block, parry, dodge, death and fear step.
- Retarget, fit and review the picks, then wire them in and record a fight.
- Switch the brigand's standing guard in game to the new guard loop.
- Recheck Owain's blocks, parries and hit reactions against the new attacks.
