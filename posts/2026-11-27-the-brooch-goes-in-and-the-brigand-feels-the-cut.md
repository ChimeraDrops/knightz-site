---
title: Dev Log #63: The brooch goes in and the brigand feels the cut
date: 2026-11-27
---

Three pieces of combat work landed. The bronze brooch HUD is now in the game. The brigand's block recoils are approved and wired to each of his attacks. Losing an arm now plays its own reaction, with blood that pumps in time with his heart.

## Block recoils approved and in game

All eight hand-built block recoils were approved: three light, a second one for the two-strike light attack, three heavy and the kick. When Owain blocks, the brigand's blade bounces off the shield and he goes back to guard with his feet planted. Light recoils run half a second and heavy ones about three quarters of a second.

The parry and block recoils are now chosen by the attack that was stopped. The chain break and the pause before his next attack are also in. Two test runs checked it:

- **Owain always blocking.** 13 attacks, all blocked. No combo step followed a block.
- **Owain always parrying.** 7 attacks, all parried. The brigand was pushed back 75, 86 and 95 cm, matching the clips. No combo step followed a parry.

A block on the first strike of a two-strike attack now stops the second strike as well. Before this change the second strike still came through.

## The bronze brooch HUD in game

The brooch render was approved and the HUD is now built in Unreal. It sits in the lower left corner and fades out when nothing is happening.

- **Garnet health orb** with a pale band for recent damage that drains after a short hold.
- **Gold stamina ring** around the orb.
- **Infection** spreads dark veins through the orb and fills a green gem.
- **Weapon and shield wear** gems, with the weapon icon following what Owain holds.
- **Two count dials** were added at the top left of the brooch for bandages and arrows. They always show a number and turn red at zero.
- **No health numbers** anywhere on screen.

The enemy display is in as well. The break line shows above the lock-on target and above any enemy winding up or striking at Owain. It hides a few seconds after the threat passes. Broken enemies get gold brackets and a BROKEN label, and the sever odds appear at the head, each arm and the legs. Labels are for keyboard and mouse for now.

![What the new HUD showed in real fights, and what waits for hands-on play](assets/img/gallery/devlog63_hud_in_game_1127.png)

Checks in real fights confirmed the low-health glow around the rim, infection from a real bite, the recent-damage band and brackets on two broken enemies at once. With nine enemies on the test map the frame time matched the old HUD. The old bar HUD stays as a fallback until the new one is signed off.

## Losing an arm

Severing an arm used to drop the brigand straight into a rag doll. Each arm now has its own reaction of about four seconds. He looks at the stump, reaches for it with the other hand, opens his mouth with his brows raised, stumbles back about 2.3 m and falls. The body then holds its final pose. Starting the rag doll at the end of the clip kicked the body and stretched the mesh, so it was left out for this case. After a left arm sever he keeps his seax in his right hand through the fall.

The stump no longer sprays at a constant rate. Blood comes out in spurts with a thin trickle between beats. The pulse starts at 150 beats a minute and slows to 85, and each spurt gets weaker over an eight second bleed.

![Heartbeat blood flow after an arm sever, and the brigand's reaction](assets/img/gallery/devlog63_heartbeat_blood_1127.png)

A bug was also fixed. A weapon dropped at the moment of a sever could land under Owain and throw him into the air. Dropped weapons can no longer be stepped on.

## Changes to the plan

- **Cures leave combat.** Curing is now a between-battles action at a campfire. The cure input was removed from fights, and the HUD has no cure element.
- **Count dials added** to the brooch for bandages and arrows.
- **Leg and head sever reactions** are deferred until the playable demo is complete.
- **Melee rework order.** The brigand's own parries, dodges and deaths resume once the HUD is signed off.

## Known issues

- In close camera views the brigand's head and hair can vanish once he bends over or falls. A fix is planned.
- Sever labels can overlap the bodies when the two fighters stand close.
- HUD icons are first pass and the numerals use a stand-in font.

## Next

- Hands-on play of the new HUD and enemy display.
- Fix the vanishing head in close views.
- Final icons and font, then retire the old bar HUD.
- The brigand's own parries, dodges and deaths.
