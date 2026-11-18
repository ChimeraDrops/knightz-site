---
title: Dev Log #55: Rag doll, aim and lock-on
date: 2026-11-18
---

Combat work continued in Unreal. Owain's clips now carry markers for sound, blood and props. He drops his weapons when he dies and falls into a rag doll that stays on the ground. His hits land on the frame the blade arrives, every strike is aimed at the enemy, and the lock-on can switch targets.

![Blade direction at the hit, before and after the aim fix](assets/img/gallery/devlog55_attack_aim_1118.png)

## Markers on the clips

- **124 markers on 56 clips.** They mark the moments the game needs to hear about: combo windows, impacts, parry and block clangs, footfalls, knee and body impacts, kicks, bites, grabs, kills and breaths.
- **Hooks only for now.** Each marker fires an event. Sound, blood and dust will listen to those events later.

## Sword and shield leave his hands

- **Cure.** The sword goes into the ground on frame 10 and back to his hand on frame 114.
- **Rest at the fire.** The sword goes down as he sits, the shield is set aside, and both return as he gets up.
- **Bandage.** Both weapons are put down at frame 45 and picked up at frame 175.
- **Cut short.** If a hit interrupts one of these clips, the weapons go straight back to his hands.
- **Accuracy.** At every swap the weapon moves 2.2 cm or less.
- **Shield fix.** The shield sat 11 cm off its mount for the first moments after spawn. It now snaps to the right place half a second in.

## Rag doll after death

The first try failed. At the hand-off to physics the body slid 60 cm to 1.6 m across the floor.

- **New physics body.** It has 18 parts sized from Owain's body and clothes, with hinged elbows, knees and hips.
- **Foot bug.** In 55 of the clips reimported last time, the foot targets did not follow the feet. In game this pulled his feet toward the wrong spots. The death poses ended with the legs folded under him, and kicks fell short. The targets were baked onto the feet on every frame. The kick now reaches 99.5 cm against 102 cm in the clip. The Blender export now does the same bake, so a reimport will not bring the bug back.
- **Hand-off on the ground.** The death clips ended with parts of the body floating 5 to 14 cm above the floor. The rag doll now takes over on the frame the body hits the ground, so the floating end is never shown.
- **Result.** At the hand-off the body slides 0.5 to 3.9 cm. No bone moves more than 2 cm on the first physics step. He comes to rest within about a second.
- **Weapons drop.** Sword and shield fall from his hands on the first frame of the death. They tip over and lie flat 0.6 to 1.1 s later, 47 to 67 cm from the body.

## Hits land on the impact frame

![When the hit registers in each attack, before and now](assets/img/gallery/devlog55_hit_moment_1118.png)

The attacks keep their tuned speed. Before, every light attack registered its hit at one fixed time and every heavy at another. The blade speed and reach were measured on every frame to find the real moment of contact.

- **Heavy.** The hit now registers at 0.94 s, when the blade arrives. Before, it landed 0.35 s early.
- **Heavy 2.** The shield-side thrust now registers at 0.32 s. Before, it landed 0.27 s late.
- **Light 2 and 3.** The first reading picked the wind-up and the follow-through. Reach and height put the real contact at frame 18 and frame 3.
- **Head sever.** The cut now lands on frame 19. Frame 25 was the follow-through behind the head.
- **Heavy swing jump.** One frame after the heavy swing, the sword hand jumped 75 cm. The recovery now blends in over 12 frames. The largest move between frames is 25 cm.

## Strikes aimed at the enemy

Play testing showed Owain's attacks landing about 15 degrees left of the enemy he faced. The clips turn his body left while his facing stays fixed.

- **Body turn.** Each attack now turns him a set amount to the right as it winds up and back by the end. The amount is set per clip, up to 48 degrees for the heavy.
- **Result.** The measured strikes now land within a few degrees of the line to the enemy. The heavy went from 48.5 degrees off to 0.1.
- **Arm severs.** The two arm cuts aim 12 degrees either side of the enemy's centre, so the blade meets the arm.

## Lock-on

- **Lock.** Tab locks the enemy nearest the middle of the view. With nobody in view it locks the nearest enemy in the fight.
- **Switch.** Mouse wheel up moves the lock to the next enemy on the right, down to the left.
- **Target dies.** The lock moves to the nearest enemy still fighting. With nobody left it releases.
- **Marker.** The locked enemy is marked on screen.
- **Defence.** A parry or block against any attacker now turns Owain to face that attacker for the reaction. Then he turns back to his locked target.

## Stealth

- **Walking** is heard only inside 1.1 m. Running is still heard at 4 m.
- **Test.** He walked up from 5.5 m behind an idle enemy and finished the stealth kill with no alert.

## Changes to the plan

- **Weapons drop at death** so the rag doll falls free of them.
- **The rag doll starts when the body hits the ground.** It no longer waits for the end of the death clip. Some of the last acting in three death clips is now done by physics.
- **The rag doll settles freely.** It does not try to hold the final pose.
- **Attacks keep their tuned speed.** Only the hit moment moved. The first heavy now connects later, so an enemy swipe can land before it.
- **Attacks follow the target** for their whole length. Before, they tracked it only until the strike.

## Next

- Judge the later heavy hit and the new body turn in play.
- Aim for the kick and shield bash, and line up finishers and the stealth kill on their targets.
- Test target switching and the defence turn against two attackers.
- Rag dolls for the female and large male bodies.
- Sound, blood and dust on the new markers.
