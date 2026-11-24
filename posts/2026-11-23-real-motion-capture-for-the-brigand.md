---
title: Dev Log #60: Real motion capture for the brigand
date: 2026-11-23
---

The brigand's seax attacks from the last log did not pass review. Two rounds of AI-generated motion did not pass either. The brigand's attacks now come from real motion capture. Seven sword clips were picked, retargeted onto the brigand and sent for review.

## What did not work

Three sources were tried for the four seax attacks and rejected:

- **Owain's swings, retimed.** The brigand looked past Owain's shoulder instead of facing him square, and the free left arm moved stiffly.
- **AI motion, knife prompts.** The takes came out as small dagger slices.
- **AI motion, sword prompts.** Each take held several loose swings in place of one complete attack. The long take length pushed the model to add extra swings.

![Where the brigand attacks came from](assets/img/gallery/devlog60_attack_sources_1123.png)

## Free sword pack first

A free sword motion capture pack went in first. It has one attack clip: a 5.5 second combo with four swings. The swings were measured one by one: a one-handed forehand, a two-handed backhand, a diagonal cut over the right shoulder and an overhead chop. Its ready idle keeps the left hand low, which fits the planned fix for the brigand's guard. One clip could not cover three attack types and a kick, so the search went wider.

## Three motion capture sets

A survey of sword, sword and shield, axe and spear animation sets on Fab compared clip counts, reviews and capture type. Three motion capture sets from the same studio were added to the library, all on one skeleton:

- **One-handed sword (178 clips).** Attacks, two-hit combos, parries, hit reactions by body part, deaths, kicks, dodges and idles. This set covers most of the brigand's remaining groups.
- **Longsword (about 200 clips).** For enemies with two-handed swords.
- **Spear and halberd (176 clips).** Spear, pike, poleaxe and great axe.

## Seven picks for the brigand

From the one-handed set, seven clips were picked to form two three-step chains like Owain's own light and heavy combos, plus a kick:

- **Light 1 to 3.** A fast forehand, a snap backhand and a double strike, backhand then forehand. All three stay in place.
- **Heavy 1 to 3.** A big forehand in place, then two-handed forehand and backhand swings that step 1.3 m and 1.5 m forward.
- **Kick.** A high front kick with the left leg that carries him 2.1 m forward.

![Brigand attack picks from motion capture](assets/img/gallery/devlog60_mocap_picks_1123.png)

The clips were retargeted onto the brigand with a new transfer tool. It copies each bone's rotation from the capture skeleton and corrects the arm and leg directions so the brigand's rest pose lines up with the actor's. Both arms keep their captured motion. Nothing is added by hand.

Each clip was set up against Owain at its own distance so the blade or foot reaches about 15 cm into him at contact. Seven review videos went out, one per clip, at full and half speed from the side and over Owain's shoulder.

## Changes to the plan

- **Brigand attacks come from motion capture.** The retimed Owain swings and the AI-generated takes are dropped.
- **Chains for the enemy.** The brigand may get three-step light and heavy chains like Owain, which needs combo support on the enemy side.
- **New guard candidate.** The capture set's own sword idle may replace the brigand's seax guard. It matches the stance of every pick and keeps the left hand down.
- **Library for later enemies.** The longsword and spear sets give two-handed sword, spear and great axe enemies a source from the start.

## Next

- Review of the seven raw clips.
- Decide how the chains map into the game, the guard stance, the timing against the enemy tells and how much forward travel to keep.
- Foot lock on the in-place clips, which sway 2 to 4 cm.
- Export, wire in and record a fight.
- Then the brigand's blocked and parried swings, his own blocks and parries, and deaths, from the same capture set.
