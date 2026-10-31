---
title: Dev Log #38: Two dogs and a wolf in Unreal
date: 2026-10-31
---

Two dogs joined the wolf on the canine skeleton: a herding dog and a hound. Each went from a raw model to a reviewed, rigged and animated animal in about a day. The herding dog has 37 approved clips and the hound has 58. The wolf was rebuilt inside its triangle budget, exported to Unreal with all 64 clips, and given its first sounds.

![Herding dog and hound animation sets by group](assets/img/gallery/devlog38_dog_hound_clip_sets_1030.png)

## The wolf in Unreal

The wolf model was rebuilt from about 24,000 triangles to 14,000. The face, lips, teeth and eyes were protected during the reduction, so the snarl looks the same as before. A side-by-side check matched the old and new models in silhouette, face and pose.

The export carries:

- The model with three materials and 13 face shapes.
- 64 animation clips. Face clips carry their facial curves.
- Root motion on 21 clips, such as the leap attacks, flee turns, hit reactions and death.
- Turn-bend layers set up to add on top of the gaits.
- Foot sync markers on all 20 movement clips, plus footstep, bite, death and howl events.

Unreal builds four levels of detail from the one model. A test compared more than 6,000 bone positions in Unreal against Blender. The largest difference was 0.036 cm. A review level shows nine wolves side by side, each looping a clip.

## First wolf sounds

Fifteen game sounds were cut from two recordings: a field recording of a howling pack and a studio session of snarls and growls. Each cut was trimmed, faded and cleaned of hiss. The set covers a solo howl, pack howls, a distant pack, snarls, growls, attack snarls and short bite grunts. Each one is matched to a clip and a frame, so the howl starts as the head lifts and a grunt lands on the bite.

![Spectrograms of the 15 wolf sound cuts](assets/img/gallery/devlog38_wolf_sound_cuts_1029.jpg)

Still missing: teeth snapping shut, yelps, real barks, panting and footsteps on dirt, snow and grass.

## The herding dog

The herding dog is a rough collie type. Its model needed the same review as the wolf:

- The normal map was re-baked. Most of the blotches in the coat came from it.
- The head was turned about 25 degrees to one side. It was straightened.
- The tail was fused to the inside of a thigh. It was cut away and rebuilt with a low carriage and an upward swirl at the tip.
- New eyeballs, lids that close for a blink, a mouth interior and 42 teeth.
- The jaw was deepened so the mouth can open.
- A face rig with the same 13 shapes as the wolf, so snarls and panting work the same way.

The dog was scaled to the breed standard, 63.5 cm at the shoulder.

A test with the wolf's walk scaled down did not work. The wolf's stride was too long for the dog and the paws slid. The dog's clips were solved fresh from its own breed data instead.

The set covers walk, trot, canter and gallop on both leads, wide outrun arcs, turns and a stop. There are rest clips from standing to sleeping, a working set (holding the eye on stock, a crouched stalk, the drop and a gathering trot), and social clips: bark, pant, head tilt, play bow, sniffing, a shake-off, heeling and a tail wag layer.

## The hound

The hound is a foxhound type, scaled to 61 cm at the shoulder. It needed a re-baked normal map, a straightened head and a new tail. The tail is carried high and joins the rump with a flare so it blends into the body on all sides. The mouth seam was placed under the flews, so the hanging lips stay whole.

![Hound gaits, speed and stride](assets/img/gallery/devlog38_hound_gaits_chart_1030.png)

The hound has the largest set so far, at 58 clips:

- **Movement.** Walk, trot, canter, a rotary gallop on both leads, a start, a stop, turns, a back-up and side steps.
- **Rest.** Sitting, lying, rolling onto the side, sleeping curled, a stretch and a shake.
- **Scent work.** A tracking walk with the nose 2 to 4 cm off the ground, casting arcs left and right, air scenting, freezing on a scent and investigating an object.
- **Calls and social.** A long bay, bark, growl, whine, pant, yawn, head tilt, play bow, greeting, a submissive lowering and two tail wag layers.
- **Gameplay extras.** Jump and land, bite and hold, a threat idle, a retreat, drinking, eating and a scratch.

The resting tail now lies on the ground under its own weight. Earlier versions bent it down from the base, which looked forced.

## One skeleton, three canines

Work on the hound showed that the shoulders were attached one spine bone too far forward. Every head-down pose dragged the shoulders with it. The front legs now hang from the middle of the back, and the neck can stretch.

The same change was made on the herding dog and the wolf. Every approved clip was re-baked so it moves exactly as before. The neck weighting from the hound was carried over to both. All three animals still share one skeleton in Unreal.

## Changes to the plan

- **Each dog gets its own movement.** Clips are solved from each breed's data. Wolf clips are not reused on dogs.
- **Domestic dogs turn on the spot.** Calm turns in place were left out for the wolf. The dogs have them.
- **Resting tails follow gravity.** Tails are raised only when standing, walking or trotting.
- **Animals go into Unreal in batches.** The dogs will be imported together once the shared canine skeleton is updated in Unreal.

## Next

- A wolfhound on the same skeleton, followed by a fox.
- Update the canine skeleton in Unreal, then import both dogs.
- Wire the wolf sounds into Unreal and add the missing sounds.
- Paired attacks with the player and the rules the AI uses to pick them.
- Animation blueprints for the wolf and dogs.
