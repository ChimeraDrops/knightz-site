---
title: Dev Log #19: A motion library written in plain English
date: 2026-10-11
---

Today the combat system got its animations. Every move in the combat design was written as a short plain-English description and turned into body motion by an open text-to-motion model running on the studio's own GPU. By the evening there were 865 clips, each in four takes, for the player, the allies, the dead and the brigands.

## Describing a move

Each animation starts as one or two sentences: who moves, what they carry, what the body does and how it ends. For example: "A tall man with a round shield on his left forearm draws his sword high over his right shoulder, pauses for a moment, then steps in and brings a powerful overhead chop straight down with his full weight, ending low, then recovers to guard."

The model returns that as motion on a standard human skeleton, four times with different random seeds, so the best take can be picked later. The clips are then retargeted onto our own character skeletons in Unreal, so one source library serves every body.

![Owain with spatha and round shield: heavy chop, push-kick and stealth kill](assets/img/gallery/devlog19_owain_attacks_1011.png)

## Running it at home

The first clips came from the model's public web demo, and its free daily GPU allowance ran out after about twenty. The model (Tencent's HY-Motion 1.0) is open source, so it now runs locally on an RTX 5090: a 4 GB motion model plus an 8-billion-parameter text encoder that reads the prompts. Getting it running on Windows took three fixes: a newer PyTorch build for the card, a newer YAML library, and reading the 4 GB checkpoint straight from disk, because copying it into memory crashed Python.

Once running, a clip with four takes takes about eight seconds, with no daily limit and no cost per clip.

## The library

- Owain and the standard-build allies: spatha and shield, spatha alone, axe and shield, spear, seax, unarmed and bow. Each weapon set covers idle, walk and jog in eight directions, a guarded walk, turns, draw and sheathe, a three-hit combo, a heavy, a kick or bash, four limb strikes, finishers, a stealth kill, and parry, block and break-parry for every enemy attack type.
- Shared moves for everyone: dodges, hit reactions, grapple and ground struggles, death, getting up, bandaging, drinking the cure and resting at a fire.
- The large-build allies get their own versions, written to move heavier.
- Brigands and deserters get a living-human set with blocks, parries and bleeding out.

![Shared moves: death, getting up and resting at the fire](assets/img/gallery/devlog19_shared_moves_1011.png)

## The dead

The dead come in four bodies: peasant men and women, and Neanderthal men and women. They share the same action list, but the prompts give each body its own language. The design calls for every attack to have a readable tell and bans the arms-out zombie pose, so the grab is a squat followed by a lunge you can learn to read.

![Undead grab-bite, hammer blow and legless crawl](assets/img/gallery/devlog19_undead_attacks_1011.png)

Measured on the walks, the difference shows: the Neanderthal man stoops almost three times as far as the peasant man and takes the slowest steps, while the Neanderthal woman takes the quickest.

![The same walk for four undead bodies](assets/img/gallery/devlog19_undead_bodies_1011.png)

## Checking every clip

Each clip also saves its joint positions. A script draws them as stick figures and measures what the body actually did: how far it turned, which way it travelled, how wide the feet were and how far the hands reached.

Attacks, falls, struggles and utility moves read well on the first pass. Three kinds of movement did not:

- Side-steps often turned into a turn and a walk.
- Dodges turned the body as much as 130 degrees.
- The 180-degree turn reached its target on time, then kept turning to fill the length of the clip and finished a full circle.

![How far the body turned in the turn-in-place clips](assets/img/gallery/devlog19_turn_audit_1011.png)

The fix is a second pass over about 400 clips: every walk, jog, turn, dodge and idle, plus the spear and unarmed attacks. Prompts are tighter ("keeping his hips, chest and face pointed straight ahead the whole time"), turns get shorter clips and are told to stop, and each clip is generated eight times. A script scores every take on direction, turn, hand spacing or reach and keeps the best four.

## Next

Run the second pass, retarget the library onto the game skeletons in Unreal and replace the stand-in clips in the combat prototype. Paired moves such as finishers, grapples and the stealth kill then get synced between attacker and victim.
