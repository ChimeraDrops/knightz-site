---
title: Dev Log #51: Five ways to fall and one way back up
date: 2026-11-14
---

Four more of Owain's clips are approved: a death on a spike wall, a set of four random combat deaths, a knockout shared by every character and a get-up that follows it. The audit now stands at 57 of Owain's 76 original clips.

![The spike wall death and the four combat deaths, beat by beat](assets/img/gallery/devlog51_death_beats_1114.png)

## The spike wall

Owain is shoved back into a wall of spikes. The spikes kill him.

- **Shoved back.** He stumbles about 1.5 m in three steps with his arms thrown up and out for balance. The last step fails and he topples back.
- **Impaled.** He is pinned through the upper back on frame 54, leaning back 24 degrees with his heels dug in.
- **Three push-offs.** His sword fist and his shield press flat against the wall. His elbows extend and his upper body strains away from the spikes, then collapses back. Each attempt is weaker than the last.
- **Still.** His arms go slack and slide down. His head rolls toward his right shoulder and drops a little. The body stays pinned.
- **Built by hand.** The generated reference could not hold a body pinned in place. It supplied the shove and the stumble. The pinned part was posed from a fixed point on his upper back outward: torso first, then hips, legs and arms.
- **In game.** The stumble stretches to fit, so he always lands on the wall. He holds the last frame.

## Four random deaths

The old single death clip is replaced by four full deaths. One is picked at random when his health runs out. After the last frame the body switches to rag doll physics.

- **A.** Staggers, drops and falls face down. His sword arm is thrown forward and the blade lies flat past his head.
- **B.** A longer stagger, down on one knee, then face down with his sword hand planted on the floor.
- **C.** Drops his shield, doubles over clutching his middle, goes down on his right knee and curls onto his side.
- **D.** Staggers back 2.7 m and falls on his back. The game only picks this one when there is room behind him.

### What the checks caught

- **Blade and skull.** The joint check tests bones only. A new scan of the sword against the body mesh found the blade passing through the head in the lying poses of A and B. The sword arm was re-posed so the blade rests 30 to 54 cm clear of the skull.
- **Elbow in the ribs.** In C the right elbow sat inside the torso while he clutched his middle. The elbow now swings out with the hand kept in place. On his side, the sword arm is laid over his hip. Every clip now gets an elbow distance check against the spine.

## Knocked out

![The knockout and the get-up, beat by beat](assets/img/gallery/devlog51_knockout_getup_1114.png)

The knockout is shared by all characters. One blow to the head, a dazed step and a collapse onto the back, turned onto the right side.

- **One hit.** The generated reference snapped the head one way and then back the other, which read as two hits. The neck was re-timed as a single arc.
- **At rest.** The head, the sword hand, the blade and the shield rim all rest on the floor. The reference lifted the head and hands again after landing, so the clip holds the settled pose instead.
- **3.2 seconds.** The last frame holds until the character wakes.

## Back on his feet

The get-up starts on the exact last pose of the knockout. Owain stirs, curls up, turns onto his front, rests on all fours with his left hand on the shield, rises and takes two small steps into his idle pose. He turns 90 degrees to his right on the way up. It runs 5.7 seconds.

The sword arm swings wide to his right while he turns over so the blade stays clear of his head. A few prop clearance flags remain during the turnover and were accepted as they are for now.

## Changes to the plan

- **Four random deaths replace the single death clip,** each ending in rag doll physics.
- **The knockout and get-up are shared by every character.** Owain keeps his sword and shield in hand through both.

## Next

- Owain's audit continues with using a bandage, using a cure and resting at a fire, then the parry, broken parry, block and hit reactions. 19 clips remain.
- All edited clips go back to Unreal in one pass when the audit is done.
