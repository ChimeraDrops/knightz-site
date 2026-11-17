---
title: Dev Log #54: The audit is done and the clips are in the fight
date: 2026-11-17
---

The hand audit of Owain's animations is finished. All 76 of his original clips are approved, along with the new variants built along the way. All 90 edited clips are back in Unreal, the combat code now picks the right variant for each moment, and every clip plays at the speed it was animated.

![The last blocks and the hit reactions, beat by beat](assets/img/gallery/devlog54_hits_blocks_beats_1117.png)

## The last two blocks

A block is the shield held up early, outside the parry window. It costs stamina and stops the damage. The shield meets the blow and is driven back toward his body.

- **Heavy.** The shield goes up over his head and to the left. The blow lands on frame 6 and drives the shield down 40 cm. His knees buckle and he gives up 40 cm of ground in two steps, then rises back to guard on frame 26.
- **Grab or bite.** The shield drops low and tips down. The enemy rams it on frame 4 and drives it into his chest. He is pushed back two steps, braces, then shoves the shield forward 29 cm on frames 15 to 17 to break the grip. Back in guard on frame 24.

## Hit reactions

A hit is what happens when Owain has no defence up. In every hit clip the shield swings out to his left in the first four frames, so the blow lands on his chest.

- **Single swipe.** The blow crosses his chest on frame 4. His right shoulder is thrown back, his head snaps back and the sword arm flies out. Two steps back, 15 cm in all.
- **Double swipe.** The first hit lands on the chest on frame 4 and the second on the left shoulder on frame 11, turning his head the other way. Three steps back, 30 cm.
- **Heavy.** The overhead blow lands on frame 5 and throws him back with both arms flung wide. Three steps back, 60 cm, and he needs about a metre of room behind him. He catches his balance and is back in guard on frame 36.
- **Grab or bite, two versions.** He is grabbed by the shoulders on frame 5, pulled forward and down, and bitten on frame 10. In one version he is driven into the grapple crouch, and the player must struggle out. In the other he wrenches free, steps back and returns to guard. The game picks the version.
- **Damage.** A single swipe deals one share of damage, a double swipe two, a heavy three, and a bite two plus infection.
- **Checks.** All five pass the joint check and the mesh scan.

## Back in Unreal

- **90 clips in one pass.** Every edited clip went from Blender to Unreal in batches. Each one was checked against Blender on eight key bones, every third frame. The worst difference was under a tenth of a millimetre. Frame counts match on all 90.
- **23 new clips** joined the set: the four deaths, the rest at the fire, the side-split parries, broken parries and blocks, the heavy combo swings, the stealth kill variants and the parried and blocked reactions.

## The game picks the variant

The fighter code now chooses between clip variants as the fight plays out.

- **Side.** Parries, broken parries and blocks against a single swipe play the left or right clip to match the arm the enemy swings with. The first test showed the sides reversed, so they were flipped and tested again.
- **Weight.** Parried and blocked enemies play a light or heavy reaction to match the attack.
- **Target.** The stealth kill goes to the chest of a living target and to the head of the undead.
- **Room.** On death, the game checks for walls in front, to the left and behind, then picks at random among the deaths that have space to play.
- **Heavy combo.** Pressing heavy again in the window plays the shield smash, then the jumping spin.

Every path played in the combat test level with no missing clips.

## Clips play at their own speed

![Time each move holds Owain, before and now](assets/img/gallery/devlog54_clip_timing_1117.png)

Before this change every action had a fixed time, and clips were sped up to fit it. Parries ran at about 2.4 times speed and the bandage was cut off.

- **New rule.** Each clip plays at its authored speed. The game event lands on the authored frame: the moment the shield bash connects, the kick lands, a limb is severed or the bandage takes effect.
- **Results.** A parry against a single swipe now takes 0.60 s, a heavy hit 1.20 s and a shield bash 1.13 s. The bash connects at 0.43 s.
- **Unchanged.** The light and heavy attack combos keep their tuned timing.
- **Double swipe.** One block or hit clip now covers both blows. The second blow no longer restarts it.

## Changes to the plan

- **Heavy block** steps back 40 cm in two steps. The earlier plan had a half-metre slide.
- **Hits are not split by side.** One clip per hit, with the shield swung aside first.
- **Grab or bite hit** has two endings: into the grapple or breaking free.
- **Living enemies now parry heavy attacks** as well as light ones. Before, they could only block or dodge a heavy.
- **Rest at the fire** now includes sitting down and getting up in the rest time. A rest takes about 7 seconds.
- **Death** holds the last frame for now. The hand-off to rag doll comes later.

## Next

- Sound, blood and footfall markers on the clips, and the moments the sword and shield leave and return to his hands during the cure, bandage and rest.
- Rag doll after the death clips.
- Lining up finishers and the stealth kill on their targets.
- Judging the new timing in play. The bandage now holds Owain for 7 seconds and the cure for 4.
