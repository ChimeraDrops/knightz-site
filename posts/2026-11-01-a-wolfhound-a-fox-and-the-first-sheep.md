---
title: Dev Log #39: A wolfhound, a fox and the first sheep
date: 2026-11-01
---

Four more animals were rigged and animated in one day. A wolfhound and a red fox joined the canine skeleton. A ewe and a ram became the first animals on a new small herd skeleton, which the goat will share. The sheep set is approved. The goat model review has started.

![Animation clips per animal](assets/img/gallery/devlog39_clip_counts_1031.png)

## The wolfhound

The wolfhound is the largest dog so far, scaled to 84 cm at the shoulder. That sits inside the breed standard's ideal range.

The source model needed more repair than any canine before it:

- The muzzle was turned about 32 degrees to one side. It was straightened.
- The coat was modelled as loose flaps over a hollow body with holes in it. The body was rebuilt as one solid, clean surface.
- A crater in one haunch was filled from the other side.
- The tail was fused to the buttocks. A new long tail was built with a low carriage and a slight upsweep at the tip.
- New eyes, a sealed mouth with 42 teeth, and the same 13 face shapes as the wolf.

The finished model is about 24,800 triangles, inside the budget for story animals.

The wolfhound has 57 clips. They cover walk, trot, canter and gallop on both leads, starts, stops, turns and side steps. There are rest clips from sitting to sleeping on its side, a scent set, calls (bark, bay, growl, whine) and a threat set with bite and hold. Timing was scaled from the hound by leg length, since no wolfhound gait data exists. Every clip passed the ground check after head-down poses were lifted clear.

Still to do: the lips read as a dark rim under the muzzle from the front. A dedicated lip pass is planned.

## The fox

The fox stands 40 cm at the shoulder with a 37.5 cm brush. Its model had a bent body, a turned head and a tail fused into one haunch, replacing the thigh. The haunch was rebuilt from the mirrored side and a new brush was made with a white tip.

The fox reuses the wolfhound's movement solvers. The fox was scaled up to wolfhound size, animated, then scaled back down and retimed for its shorter legs.

![Fox gaits, speed and stride](assets/img/gallery/devlog39_fox_gaits_chart_1031.png)

Its 49 clips include fox behaviour:

- **Sneak.** A slow stalk, low to the ground, with a freeze on each step and ears pricked.
- **Mouse pounce.** Listen, crouch, a high arc, a forefeet-first dive, pin, then alert.
- **Ground sniffing** at a slow walk.
- **Sleeping curled** with the brush laid over the ground.
- **Calls.** A bark and a two-part scream.

The trot is the fox's travel gait, with a narrow track as observed in the wild.

## Sheep on a new skeleton

The ewe and ram are a primitive brown type with curled horns. They were scaled to medieval sheep: about 58 cm at the shoulder for the ewe and 62 cm for the ram. Both models were turned at the head, had stub tails fused to the rump and badly inverted normal maps. All three were fixed. The ram's coat was a double shell, one surface inside another. It was rebuilt as a single surface with new textures.

![Shoulder heights set for the animals](assets/img/gallery/devlog39_animal_heights_1031.png)

The new small herd skeleton has 33 bones and comes from the ox and cow skeleton. Two changes make it work for smaller animals:

- The front legs hang from the middle of the back, as on the dogs.
- The neck starts low in the chest. With the neck on top of the shoulders, the sheep could not reach the grass.

Each sheep has 22 clips: walk, trot, run, turns in place, flee turns, idles, an alert, a full grazing set with a step forward, and lying down and getting up. The walk timing comes from published sheep gait measurements. The run is a prototype, since no sheep gallop data exists.

A fix pass removed small hoof skids at touchdown, stopped feet sliding while lying down, and smoothed a stretch at the top of the neck in the grazing pose.

## Changes to the plan

- **Small animals share a skeleton.** Sheep and goats use the new small herd skeleton in Unreal. Cattle keep the bovine skeleton.
- **Canine movement can be scaled.** Movement solved for one canine can carry to another of a different size when it is rescaled by leg length. The wolfhound and fox were built this way. The herding dog and hound keep their own breed-specific solutions.
- **Grazing animals get a low neck base.** The same fix used on the cow is now standard for grazing animals.

## Next

- Finish the goat: rebuild its double-shell coat, add a tail, rig it on the small herd skeleton and animate it.
- Lip pass on the wolfhound.
- Review of the wolfhound and fox sets.
- Update the canine skeleton in Unreal, then import the dogs, wolfhound and fox together. Add the small herd skeleton and import the sheep.
