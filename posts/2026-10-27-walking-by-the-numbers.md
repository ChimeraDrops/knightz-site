---
title: Dev Log #34: Walking by the numbers
date: 2026-10-27
---

Three pieces of work landed this time. Every walk cycle on the three main bodies was measured against clinical gait averages and rebuilt to match. The ground cover on all eleven regions was reshaped and set down onto the land. And a design session settled how the player grows stronger over the game.

![Walk cycles before and after the gait fix, per body](assets/img/gallery/devlog34_gait_checks_chart_1026.png)

## A walk you can measure

Telling an animator to "make it look natural" does not get far. Measurable targets do. We built a reference table from published human gait research: steps per minute, stride length, step width, time on each foot, hip, knee and ankle angles through the step, pelvis twist and drop, head bob, and arm swing. Men and women have their own ranges.

A new check reads every walk clip and scores it on 35 measures against that table. The first run was not kind. Not one of the 144 walks passed. The common faults:

- A crouched walk. The knee never straightened, and the hip was bent too far at heel strike.
- Too few steps per minute, so the legs looked slow for the speed.
- Narrow steps, with feet crossing on some directions.
- Side and back walks that moved far slower than the game speed.
- Small pops at the loop point.

## The fix

The legs and pelvis of every walk were rebuilt from the foot contacts. The upper body keeps its own motion, so each weapon set still carries its sword, shield, spear or bow the same way, now in time with the new steps.

- **One clean cycle.** Each walk is one loop at the right pace: 120 steps per minute for the men, about 129 for the women, who take shorter and quicker steps. The body moves at the game walk speed in the exact direction named.
- **Planted feet.** Each foot rolls from heel to flat to ball with no sliding, and clears the ground in swing.
- **A natural knee.** A small bend as the foot takes weight, a big bend in swing. The pelvis rises and falls with it, and twists and drops a little more on the women.
- **Counter turn.** The chest turns against the pelvis, and the head stays steady.
- **Diagonals and backs.** On diagonal walks the hips turn toward the line of travel so the legs never cross. Back walks are the forward walks played in reverse.
- **Side steps.** Short, slow steps with the feet kept apart. These only play when locked on to an enemy.
- **Arms.** With empty hands the arms swing about 17 degrees forward and 12 back, opposite the leg, with a soft elbow.

Results across the three bodies:

| Body | Walks | Average failed checks before | After | Passing every check after |
|---|---|---|---|---|
| Healthy male | 64 | 17.2 | 3.0 | 25% |
| Large male | 24 | 16.4 | 2.5 | 25% |
| Healthy female | 56 | 14.4 | 0.7 | 66% |

What is left is small, one to three degrees or about a centimetre: a bit too much head bob on the men and a slightly high knee lift on some diagonals. A test in play confirmed each body walks at its game speed with a one-second cycle. The new walks are in for review now. The same check will run on every walk and jog clip before anyone looks at it.

## Ground cover that fits the ground

Two problems showed up on the slopes. Some plants floated above the ground, and the patches of leaf litter, clover, moss and lichen were perfect circles.

All 22 ground cover patch shapes were redrawn with ragged, uneven edges, slightly stretched, and made larger. Then a new tool set every plant back onto the land. Flat patches tilt to follow the slope and sit just into the soil. Upright plants drop to the lowest ground under their base.

The first try sank the clover out of sight, so the depth was cut back. The final pass set more than 45 million plants across all eleven regions.

![Ground cover before and after the reshape](assets/img/gallery/devlog34_groundcover_before_after_1026.jpg)

![After: patches follow the ground, and no two are the same shape](assets/img/gallery/devlog34_groundcover_after_1026.jpg)

## How the player grows

A design session set the rules for progression. Changes to the overall plan:

- **No magic and no skill trees.** Every upgrade changes a number you feel in a fight: stamina, the parry window, the chance to sever a limb on a staggered enemy, stamina cost per swing, and the chance of a bite getting through armour.
- **Upgrades come from fighting the dead** and are spent at the manor chapel. Tougher dead give more. Costs climb in even steps across about 30 upgrades.
- **The smithy runs on barter.** Iron, charcoal, goods and hack-silver. No coin. Weapons are built from parts (blade, guard, grip, pommel) that upgrade one at a time.
- **The manor matters.** Bigger buildings open better upgrades, and sieges are fought with what has been built.
- **People.** Six manor people each get one personal mission per year.
- **Places, not multipliers.** The dead do not get damage boosts. Deeper and more distant places hold stronger kinds of dead.
- **Your own pack.** A 12-slot pack, kept apart from the manor stores, with four quick slots. It grows with a satchel, belt pouches, a pack frame and saddlebags.
- **No respawn.** Death reloads the last checkpoint.
- **Cold is the only survival need.** No hunger or thirst. Winter, nights outdoors or a fall into a river slow stamina recovery until you warm up at a fire.
- **First build target.** A vertical slice of one spring day at Pengwern: the weir, spear fishing, a road event, one real fight, a smithy upgrade and a scare at night.

Two pipeline decisions came with it. Paired moves such as finishers and grabs will be animated in Blender on one shared origin and only assembled in Unreal. Faces in cutscenes will be captured with a phone on the existing face rigs.

## Next

- Review the new walks in the editor, then rerun the men with the final settings.
- The same checks for jogs and runs.
- Upgrade tiers for spears, axes, armour and the pack.
- Carried over: short dry stream stretches, two road and river meetings with no crossing, swimming, and autumn colours for oak, ash and alder.
