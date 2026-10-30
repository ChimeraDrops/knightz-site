---
title: Dev Log #37: The wolf learns to hunt
date: 2026-10-30
---

The wolf is the second animal through the pipeline and the first predator. In two days it went from a raw model to a reviewed mesh, a canine skeleton, a full face rig and a set of 47 animation clips. By the end of the day 42 of them were approved. The set covers moving, resting, calling, threatening, fighting and dying.

![The wolf animation set by group](assets/img/gallery/devlog37_wolf_clip_set_chart_1029.png)

## Cleaning up the model

The wolf model went through review before any rigging:

- The normal map had about half its faces pointing the wrong way. It was re-baked.
- Specks in the fur colour were cleaned out and the painted eyes restored.
- The throat and chest were smoothed.
- The tail was cut away and rebuilt as a new bushy tail that hangs free of the hind legs and joins the rump cleanly.
- The head had been turned about 39 degrees to one side in the source model. It was straightened onto the centre line before the eyes and mouth were built.

## A canine skeleton

Dogs and wolves get their own skeleton, as cattle did. It started from a hand sketch and has a pelvis, three spine bones, two neck bones, a head, five tail bones and four legs. There is no shoulder blade bone. The upper arm slides instead, which gives the same glide at the shoulder in the run.

The skin was weighted and tested by posing every joint. The ears were fixed so they no longer fold when the neck and head turn different ways.

## Eyes, mouth and face

The wolf has real eyeballs with amber irises, set so both eyes focus on a point 20 metres ahead. The lids close to a slit for a blink with nothing poking through.

The mouth was built from scratch, because the source model had almost no lower jaw:

- A new lip line with black lips and a deeper lower jaw.
- A mouth interior, gums, a tongue and 42 teeth placed to real wolf dentition, including the long canines and the shearing carnassial teeth.
- The upper and lower teeth close without overlapping.

The face rig follows DogFACS, a published system for coding dog facial movements. Bones handle the jaw, tongue, eyes, lids and ears. Shape keys handle soft movements such as the snarl, the nose wrinkle, the lip corners and the brows. A full snarl test shows the canines and upper gums with the ears pinned back.

## Moving like a wolf

The walk and trot were built from a wolf biomechanics reference and approved. The gallop is a rotary gallop with the spine flexing hard on each stride. There are two speeds, a pursuit at about 6.9 m/s and a slower acceleration, each with a left and a right lead.

The head carriage for the run was posed by hand: the chest drops at the withers and the head is held low and forward, so the teeth lead.

## Turning

Calm turns on the spot were left out on purpose. A wolf turns while it moves. Two kinds of turn were built:

- **Flee turns.** A scared wolf spins 90 or 180 degrees, left or right, and runs. These were timed from footage of a real wolf. The head turns first, the front legs splay wide and brace, the forequarters swing round, and the hind paws pivot and drive off into the gallop.
- **Turn-bend layers.** A left and a right bend layer on top of the walk, trot and gallop. The game blends them in by how fast the wolf is turning. Only the spine, neck, head and tail bend, so the feet of the base gait stay planted.

![How the turn-bend layer spreads across the body](assets/img/gallery/devlog37_wolf_turn_bend_chart_1029.png)

## Rest, calls and the hunt

**Rest.** Standing idle, sitting down and getting up, lying down alert, and sleeping curled nose to tail.

**Calls.** A standing howl, a sitting howl, a warning bark and a whine. The howls still need sound to time them to.

**Threat.** A growl with the head held low at the same height as the run, a snarl with the lips pulled back, and a threat idle that can hold between them. A slow stalk was rebuilt after review: slower, with a pause at the end of every step and the head lowered to the growl height.

**Combat.** Bites that release or hold, a head shake, a pin, a drag, a retreat, a hit reaction and an approach.

## The leap attack

The old lunge was replaced by a leap attack that covers more ground and goes for the throat. The wolf coils, launches and rolls its head 80 degrees in the air with the jaw open, then snaps shut at the top of the leap. The hind feet land first and the forelegs absorb the drop. The wolf then turns its body away while its head stays on the target, hops back half the distance and returns to a snarl.

A running version was then built to come straight out of the pursuit gallop at full speed. Only the start changes. The wolf pushes off from the gallop and reuses the same flight and ending.

![Running leap attack, frame by frame](assets/img/gallery/devlog37_wolf_leap_run_timeline_1029.png)

## Death

There is one death, built for a right-handed killing blow. The hit lands on the left front quarter and throws the wolf back and to the right. The whole body turns away from the blow and lands on its right side. Each leg kicks on its own rhythm while the head lifts as if trying to rise. Then the head drops, the upper legs sag toward the ground and the body lies still.

## Investigating

Sniffing the ground, testing the air, scanning for danger, tearing at food, a greeting, a play bow and digging. The first dig was rejected because it did not look like digging. It was rebuilt from footage of a real wolf: head down at the hole, front end low, rump high and fast alternating forepaw strokes. That version is in review.

## The Lore page

The site has a new Lore page on the history behind the game: the volcanic winters of the 530s and 540s, the famine and plague that followed, and the old stories of the north.

## Changes to the plan

- **Animals that turn do it on the move.** There are no calm turn-in-place clips. Only a frightened animal spins on the spot.
- **Turning is a layer.** One left and one right bend sit on top of every gait, instead of separate turn clips for each speed.
- **Attacks chain from locomotion.** The running leap enters straight from the gallop at full speed. Other attacks will follow the same rule.
- **Behaviour clips use real footage where it exists.** The flee turns and the dig were both timed from video of real wolves.

## Next

- Review of the new dig, and a decision on whether the old lunge is kept.
- Hit reactions from the front, sides and back, and a heavy stagger.
- Transitions between lying down and sleeping curled.
- A mirrored running leap for the right-lead gallop.
- Clean-up of root motion across the set, then export to Unreal with face curves, footstep and bite events.
- The rules for paired attacks on the player and how the AI picks between them.
- A lower-detail rebuild of the wolf model to bring it inside its triangle budget.
