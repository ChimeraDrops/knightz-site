---
title: Dev Log #40: Pigs, horses and deer
date: 2026-11-02
---

Nine more animals were finished in one long run. The goat completed the small herd. A pig and a wild boar, a pony, a horse and a mule, and three red deer were rigged and animated on three new family skeletons. All eighteen animals built so far now carry 615 clips between them.

![Animation clips per animal](assets/img/gallery/devlog40_clip_counts_1101.png)

## One process for every animal

Each animal now goes through the same ten steps: scale, a measured mesh review, texture bakes, rig, weights, levels of detail, animation, automatic checks, review renders and a cleanup pass. Every step is measured. Nothing is judged by eye alone.

Every clip has to pass the same checks before an animal counts as built:

- Hooves stay at the ground and do not sink.
- Planted feet do not slide.
- No joint bends the wrong way and no leg is asked to reach farther than it can.
- Loops join with no visible seam.
- The skin does not stretch past a set limit in any pose, at any level of detail.

The source models carried the same faults seen on the sheep and the fox. Heads were turned to one side, tails were fused to the hind legs, bodies were hollow or made of two shells, and normal maps were partly inverted. Each one was found by measurement and fixed before rigging.

## The goat

The goat finished on the small herd skeleton with 28 clips. On top of the herd set it has a high browse into branches, a headbutt and a rearing threat. It has its own eyes and eyelids, and its double-shell coat was rebuilt as one solid surface.

## Pig and wild boar

The pig and the boar share a new skeleton with a snout bone. The pig is a medieval type at about 0.71 m at the shoulder. The boar stands about 0.89 m to the top of its bristle crest.

- The pig's walk timing comes from published gait data for small pigs.
- Both have a rooting set: the snout shoves into the ground while the head sweeps from side to side.
- Both have a charge with the head low.
- The boar adds a tusk head toss and a foreleg scrape.

The pig has 27 clips. The boar has 29.

The boar's front legs sit close together under the chest, which pulled the skin between them in every gait. Spreading the body's weight a short way down the inner forearm fixed it.

## Pony, horse and mule

The three horses share a new skeleton with a longer neck and ear bones. Each has walk, trot, canter and gallop, the last two on both leads. Footfall patterns follow published horse gait studies and are scaled to each body.

- **Pony.** 1.24 m at the shoulder. Rear, buck and a hoof paw.
- **Horse.** 1.47 m, a medieval riding horse. The source body was a thin hollow skin with holes. It was filled and rebuilt as a solid body, and its head was turned straight.
- **Mule.** 1.32 m with long ears. Its tail was joined to one hind leg and was rebuilt. It brays with the neck stretched out, the jaw pumping and the ears laid back. It also has an ear flick, a tail flick and a double kick.

The pony and horse have 27 clips each. The mule has 29.

![Stride length per gait for horses and deer](assets/img/gallery/devlog40_equine_cervid_strides_1101.png)

## Three red deer

A red deer stag, a hind and a white hart share a new deer skeleton. Their walk order follows red deer field data. The antlers move with the head as one rigid piece.

- **Stag.** 1.26 m at the shoulder, inside the measured range for red deer stags. It has a rut roar, an antler threat and a hoof scrape.
- **Hind.** 1.15 m with no antlers. It has an alarm bark and independent ear turns. Its head and neck were turned about 35 degrees in the source and were straightened.
- **White hart.** A red deer with a white coat, built at a higher detail level than the other deer. It has a slower composed walk, a roar and a look over each shoulder.

The stag has 27 clips, the hind 26 and the white hart 28.

![Shoulder heights set for the animals](assets/img/gallery/devlog40_animal_heights_1101.png)

## A bug caught on the white hart

A few short one-off clips, such as the mule's bray and the stag's roar, were keyed in a different rotation format from the rest of the set. In game they would have played as a plain idle. The white hart build caught it. The clips were converted on the mule, stag and hind, every check was run again and all of them were rendered again.

## Changes to the plan

- **One skeleton per animal family.** Cattle, small herd, pigs, horses, deer and dogs each get one shared skeleton in Unreal. Otters and beavers, birds and fish get theirs next.
- **One import at the end.** All animals finish in Blender first. Then they go into Unreal in a single batch, with the first animal of each family creating its skeleton.
- **Strides follow the rig.** Where a measured stride needed more reach than the rig has, the stride was shortened and the timing scaled to body size.

## Next

- Roe buck, otter and beaver.
- Birds: goshawk, crows and ravens, waterfowl, farm hens and geese, heron and crane.
- Fish: eel, trout and pike.
- Review of the nine new animal sets.
- Batch import of every animal into Unreal.
