---
title: Dev Log #36: The ox walks and the Roman city falls
date: 2026-10-29
---

The farm animals have started to move. The ox is the first animal through the full pipeline: reviewed, rigged on a new bovine skeleton, animated from published livestock studies and imported into Unreal. The cow followed on the same skeleton the same day. On the world side, the old Roman city got a ruin kit that replaced more than 15,000 grey stand-ins, and an overnight run built every prop and building left on the tracker.

![The ox walk, trot and gallop prototype](assets/img/gallery/devlog36_ox_gaits_1028.jpg)

## 36 animals in 3D

Reference images were made for all 36 animals in the game, leaving out bees. The best image of each was picked by hand. All of them were turned into 3D models overnight at real-world size, with birds modelled with their wings open. Each one has game levels of detail. The ox is about 14,400 triangles close up and drops to about 1,500 at distance over four levels.

The ox went through review first:

- The horn tips were trimmed and specks cleaned out of the texture.
- The underside was reshaped to look natural.
- The tail was rebuilt so it hangs free but joins the rump cleanly at the root.
- The throat crease was smoothed.

## A skeleton built for cattle

Animals do not share the human or horse skeleton. Each family gets its own, and cattle came first. The bovine skeleton has 33 bones: spine, neck, head and jaw, a six-bone tail, and four legs. Each front leg has a shoulder blade, upper arm, forearm, knee, fetlock and hoof. Each hind leg has a thigh, stifle, hock, fetlock and hoof. It started from a hand sketch and real cattle anatomy, then was adjusted by hand on the model.

The skin follows a few simple rules, tested by posing every leg:

- The ribcage and brisket follow the spine.
- Each leg moves on its own without stretching the body.
- The outside of the shoulders and haunches moves with the legs.
- Only the joins blend between bones.
- Tail bones move only the tail.

## Gaits from the science

**Walk.** The timing comes from a published study of walking dairy cattle. Each hoof is on the ground for about two thirds of the stride, in a four-beat order: left hind, left front, right hind, right front. The poses were checked against Muybridge's 1887 photographs of a walking ox. Hooves stay planted with no sliding, and the front knee folds deep in the swing as it does in the photographs. The pace is an unhurried ox walk of about 0.75 m/s.

<img src="assets/img/gallery/devlog36_ox_walk_1028.gif" alt="Ox walk cycle, side view" loading="lazy">

**Trot.** The timing comes from a published study of trotting cows: a 0.75 second stride with each hoof down for 58 percent of it. Diagonal pairs of legs move together. After a side-by-side check against Muybridge's trotting ox, the hind feet were lifted higher.

<img src="assets/img/gallery/devlog36_ox_trot_1028.gif" alt="Ox trot cycle, side view" loading="lazy">

**Gallop.** There is no measured gallop data for adult cattle, so this one is marked as a prototype. Its timing follows the general gallop pattern of large animals. It has a left and a right lead and one gathered moment in the air. It will be refined if good footage of galloping cattle turns up.

<img src="assets/img/gallery/devlog36_ox_gallop_1028.gif" alt="Ox gallop prototype, side view" loading="lazy">

## Standing and grazing

An ox spends most of its day standing or eating, so those got the most clips.

The **idle set** is a calm standing loop with slow breathing. Short variations fire at random on a timer: shifting weight, resting a hind leg, lifting a front hoof, looking around and lowering the head. Each one starts and ends on the same pose, so any of them can follow any other. Tail swats at flies play on top of whatever the body is doing.

<video autoplay loop muted playsinline preload="metadata" style="width:100%;border-radius:6px;border:1px solid #3a4146;margin:8px 0 24px"><source src="assets/video/devlog36_ox_idle_1028.mp4" type="video/mp4"></video>

For the **grazing set**, the neck was rigged again so the muzzle reaches the grass. The neck now bends from its base at the chest, as a real ox's does, and every earlier clip was rebuilt on the new neck. The set lowers the head, grazes with slow sweeps, steps to fresh grass, lifts the head to look around, then raises the head and steps back.

<video autoplay loop muted playsinline preload="metadata" style="width:100%;border-radius:6px;border:1px solid #3a4146;margin:8px 0 24px"><source src="assets/video/devlog36_ox_graze_1028.mp4" type="video/mp4"></video>

![Frames from the idle and grazing sets](assets/img/gallery/devlog36_ox_idle_graze_1028.jpg)

The ox has 29 clips in all. Every moving clip comes in two forms: one that carries the animal through the world, and one that stays in place for the game to drive.

## The cow, on the same skeleton

The cow reuses the ox skeleton and the whole clip set. Its model was reviewed first. The head was turned slightly off line, so it was straightened. Both horns were rebuilt as a matching pair, the face and nose were cleaned up, and a few texture faults were fixed. The skeleton was then fitted to the cow's smaller frame, and all 29 clips were rebuilt to her size. Her strides are 88 percent of the ox's, and her grazing neck bends a little less so the muzzle stops just above the grass. Every clip passed the same checks as the ox: no hoof sliding and every planted hoof on the ground.

![Ox and cow speed and stride per gait](assets/img/gallery/devlog36_bovine_gaits_chart_1028.png)

## In Unreal

Both animals are in Unreal on one shared bovine skeleton, each with four levels of detail and its own material on a new animal master material. Every clip was checked against the Blender original by sampling the hips, head, hooves and tail tip across the whole set. The largest difference was under a tenth of a millimetre. Toe tips sit at the same height as in Blender in every clip, and the distance each clip carries the animal matches its stride. The ox also got a review level where seven copies play the walk, trot, gallop, idle, resting leg, grazing and tail swat side by side, textured and standing on the ground.

## The ruined Roman city

The old Roman city had been laid out in grey blocks. A Roman ruin kit of 33 pieces now stands in their place:

- **Ruined walls** in six height classes, from knee high to 3.5 m. Each has a rubble core with a ragged, grassed top, sandstone facing on both sides, bands of red tile, and patches where the facing was robbed so the core shows.
- **Town wall sections** with a plinth on the outer face, collapsed stretches with rubble spilling to one side, and hollow tower stumps.
- **Rubble mounds**, column stumps on their bases, and the tile pillars that held up a bath house floor.

A script matched each grey block to the nearest wall height and swapped it, keeping its line, width and length. Over 15,000 pieces went into the city, and the Roman villa walls on the hub maps were swapped the same way.

![Ruin pieces placed in the old Roman city](assets/img/gallery/devlog36_ruin_kit_swap_chart_1028.png)

## Every prop on the list

An overnight run built every remaining prop and building on the props tracker: 164 entries, each built in Blender, imported to Unreal and marked done. It covers Roman ruins, cairns, standing stones and barrows, charcoal clamps, iron bloomeries and slag heaps, mine entrances and bell pits, peat cuttings and a timber causeway, camp shelters, pigsties, hen coops, a corn drier, a hay shelter, round huts, sunken huts for weaving and storage, and a salt boiling house. Twenty-six small buildings were assembled from kit pieces as ready-made sets, from a five-stage gatehouse to a privy. Fifteen more materials were added, such as ochre, charcoal, silver, gold, flint, green glass, fur, peat, salt and embers, plus snow-cap and Roman mosaic decals.

The swaps then ran on every region. Grey stand-ins for lean-tos, lookout platforms, eel traps, net frames, benches, querns, archery targets, carts, fences and ford gravel bars were replaced on all eleven regions and the hub maps. A rough palisade of 348 sections went up in one region, 36 of them breached.

## Changes to the plan

- **Animals get skeletons by family.** Cattle came first. Horses, sheep and goats, dogs, deer, birds and fish follow, each on its own rig.
- **Gaits come from published livestock studies and historic photo sequences** where they exist. Anything without data is marked as a prototype until real reference turns up.
- **Idle and grazing are small clips picked at random**, so a herd never moves in step.
- **Cattle have no ear or mouth animation.** This keeps them simple on purpose.
- **One skeleton per family is shared.** The cow runs the ox clips scaled to her size, and later cattle will do the same.

## Next

- The cow review level in Unreal.
- Herd logic for cattle: speed-based blending from idle to gallop, random idle and grazing picks, tail swats on their own layer, and feet that follow the terrain.
- Gallop refinement if real footage of galloping cattle is found.
- Rigs for horses, sheep and goats, dogs, deer, birds and fish.
- A review pass on the overnight props: sunken features such as pits need holes cut in the ground, the assembled buildings need a visual check in Unreal, and a few new materials need proper textures.
- The rest of the Roman city pieces: gates, the bath walls and vaults, the forum paving and the streets.
