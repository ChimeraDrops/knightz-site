---
title: Dev Log #59: The brigand fights back
date: 2026-11-22
---

All eight brigand hit reactions were approved and are now in the game. Each of Owain's attacks gets its own reaction, and the heavier blows knock the brigand back several steps. Work then moved to the second group of Phase 3: four seax attacks for the brigand, built from Owain's own approved swings.

## Hit reactions in game

The eight reactions from the last log passed review as a group. Since then several were reworked so the big hits move him:

- **Light 1 to 3 and Heavy 1.** Short reactions with both feet planted: twists, leans and a fold forward.
- **Heavy 2.** The shield smash to the chest jolts him back three steps, about 0.7 m.
- **Heavy 3.** The spinning slash from his right sends him five steps back and to the side. He puts a hand on his thigh, takes two deep breaths and straightens back to guard.
- **Kick and shield bash.** Each one drives him back four steps before he recovers.

![The approved hit reactions in game](assets/img/gallery/devlog59_reactions_in_game_1122.png)

The game side was changed to match:

- The game now tells the enemy which step of the combo landed, so each attack plays its own reaction.
- A reaction lasts as long as its clip. The old short reaction state no longer cuts it off or speeds it up.
- Kick and bash use the stumble clips in place of the old launch. The brigand moves by the clip's own motion.
- A new hit during a reaction restarts it.

A test in the editor showed every reaction playing for its own attack, then a recorded fight against the brigand AI with the new reactions in place. The foot check came back clean on all eight clips.

## Seax attacks for the brigand

The brigand's old seax attacks were early copies of Owain's moves from before the animation audit. The light swipe had no windup and the kick reached too far. They have been replaced.

The four new clips start from Owain's approved attacks with the seax in the same hand, then are retimed to the enemy tells:

- **Light.** A single slash. The hit lands at the end of a 0.6 s windup.
- **Two-hit combo.** Two blows 0.3 s apart, with a 64 degree body turn between them. His feet pivot on the balls during the turn.
- **Heavy.** A chop with a full second of windup, so the player has time to read it.
- **Shove kick.** A short kick with the foot landing at 88 cm.

![Brigand seax attacks, timing](assets/img/gallery/devlog59_seax_attacks_1122.png)

Details that apply to all four:

- The brigand's seax guard leads with the right foot and Owain's attacks lead with the left. Each attack steps into the new stance during the windup and steps back to the guard during the recovery.
- His left arm swings free with a small counter-motion to the blade arm. It no longer holds the shield-carry pose during attacks.
- In the test scene, the blade or foot comes within 8 cm of Owain at the hit frame on every attack, and the bodies never overlap.
- Feet stay exactly on their marks.

Owain plays his matching hit reaction in each review video. The four clips are waiting for review. Nothing of this group is in the game yet.

## Changes to the plan

- **Phase 3, group 1 done.** All eight hit reactions approved, wired in and tested in a fight.
- **Seax attacks rebuilt from Owain's moves.** The old brigand attack clips are dropped.
- **Free left arm for brigand attacks.** His guard and reactions keep the current pose for now.

## Next

- Review of the four seax attacks.
- Enemy aim angles, so the brigand turns his body for each swing the way Owain does.
- Export the attacks to Unreal, wire them in and record a fight.
- Then the attack-defended group: his deflected and blocked swings.
- The seax guard pose still holds the left hand up as if it carried a shield. It is on the list for the idle and guard check.
