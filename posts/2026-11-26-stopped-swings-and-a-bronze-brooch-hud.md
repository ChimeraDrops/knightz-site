---
title: Dev Log #62: Stopped swings and a bronze brooch HUD
date: 2026-11-26
---

Two things moved this time. The brigand now has approved reactions for when Owain parries his attacks, and the plan for blocked attacks is set. The game's HUD also got a new design direction to replace the current bars.

## Parry recoils approved

When Owain parries, the brigand's blade is knocked aside and he is thrown off balance. Three recoils from the motion capture set cover all seven of his attacks:

- **Right recoil.** Light 1, the second strike of Light 3, Heavy 1 and Heavy 2. He staggers back about 75 cm.
- **Left recoil.** Light 2, the first strike of Light 3 and Heavy 3. He staggers back about 86 cm.
- **Kick recoil.** When the kick is parried he is pushed back about 96 cm.

Each pairing was reviewed on video, attack into contact and then the recoil, and all were approved.

![Parry recoils and the pause after a stopped swing](assets/img/gallery/devlog62_stopped_swings_1126.png)

## Block recoils, built by hand

A block should look different from a parry. When Owain blocks, the brigand's blade bounces off the shield and he goes back to guard. There is no stumble and no steps, and his feet stay planted.

The capture set has nothing that fits, so these seven clips will be built by hand, one per attack. Each starts at the moment of contact and sends the blade back along its own path, fast at first and then slowing. The upper body moves while the legs hold still, with a small rock back on the heavy swings. It then blends into the guard stance. Light recoils will run about half a second and heavy ones under a second. A blocked kick sends the foot back down with a small rock of the torso.

## A pause before he strikes again

Enemies will no longer swing straight back into a guard that just stopped them:

- **Chains break.** A blocked or parried attack ends the combo. No follow-up step plays.
- **Short wait after a block.** Starting range 0.6 to 1.0 seconds after the recoil ends.
- **Longer wait after a parry.** Starting range 1.0 to 1.6 seconds.
- **Random within the range,** so the rhythm does not feel mechanical. Repeated blocks or parries do not stack the wait.
- **Still defending.** During the wait he holds guard and can still block or dodge. He cannot start a new attack.

All values will be tuned in play.

## A new HUD direction

The current health and stamina bars were rejected as too plain. After a round of concepts, one direction was chosen: a bronze brooch in the lower left corner, in the style of period metalwork, with a raised, three-dimensional look.

- **Health** is a garnet orb. The liquid level shows how much is left.
- **Recent damage** shows as a pale band above the liquid that drains after a short delay.
- **Stamina** is a gold inlay ring around the orb that fills clockwise from the top. It goes dark when empty.
- **Infection** spreads as dark veins through the garnet, with a small green gem that fills.
- **Weapon and shield wear** each get a small bronze gem with an icon and a wear arc. The shield arc turns red when low.
- **Low health** makes the bronze rim glow red.
- **No numbers** are shown on screen.

![Concept layout for the bronze brooch HUD and enemy display](assets/img/gallery/devlog62_hud_brooch_1126.png)

Enemies get a minimal display. A thin break line sits above the head. When an enemy is broken, gold brackets frame the torso and a BROKEN label appears. Small labels at the head, each arm and the legs show the odds and input for each sever. The best odds are lit in gold.

The HUD will be built in Unreal's widget system with animated UI materials. An HTML overlay was considered and dropped for performance. The brooch art will be modelled and rendered in Blender first, and that render has to be approved before any engine work starts.

## Changes to the plan

- **Break ring retired.** The break ring under the enemy's feet is replaced by the line above the head. The ring was often hidden by crawlers, bodies and grass.
- **Defence now costs the attacker time.** Blocks and parries end enemy chains and add a pause before the next attack.
- **Separate parry and block sets.** Every enemy attack gets its own parry recoil and its own block recoil, chosen by the attack that was stopped.

## Next

- Build and review the seven block recoils.
- Export the parry and block recoils to Unreal and choose the recoil by attack in code, with the new pause and chain break.
- Test with Owain set to always block, then always parry, and record a fight.
- Model and render the brooch for the first HUD review.
