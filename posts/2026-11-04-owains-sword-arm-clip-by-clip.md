---
title: Dev Log #42: Owain's sword arm, clip by clip
date: 2026-11-04
---

Work on the combat demo moved to Owain himself. Every animation he plays with sword and shield was listed, wired into the game and moved into Blender for a hand audit, one clip at a time. The first rule from that audit sets how he carries his sword and shield when he walks.

![What Owain plays in the combat demo](assets/img/gallery/devlog42_owain_clip_wiring_1103.png)

## What he was really playing

Owain uses 76 of our generated clips in the demo: 26 for movement and guard, and 50 for actions such as attacks, blocks, parries, dodges, hits and recovery.

The list turned up a gap. Movement and guard already played our own clips, but none of the 51 action slots did. 39 still played borrowed stock mannequin moves as stand-ins, and 12 played nothing at all, among them death, getting up from the ground, bandaging a wound and resting at a fire.

All 51 slots now point at Owain's own clips. The shared moves (dodges, hit reactions, stuns and getting up) now also play for every other weapon set on the same body.

## Into Blender and back

Until now these clips were only corrected by scripts inside Unreal. Blender gives us the graph editor, inverse kinematics, onion skinning and pose tools, and the body was built there in the first place, so no retarget is needed.

Before any edit, the path was tested:

- All 76 clips were backed up in Unreal.
- Each clip was exported and brought into a Blender audit scene with Owain's body, head, hair, outfit, sword and shield. The sword and shield sit at the same hand positions the game uses.
- The import was checked against Unreal at 2,660 sample points. The largest difference was 0.00088 cm.
- Two clips, the idle and the first light attack, went from Unreal to Blender and back with no edits. Root, pelvis, hands, feet and head were compared on every frame. The largest difference was 0.00084 cm and 0.001 degrees.

A small panel in Blender steps through the clips in order. It sets the camera and frame range, shows what each clip is meant to do, draws the path of the sword hand and records a verdict: OK, fine-tune or regenerate, with a note.

The raw clips run 2 to 8 seconds. The game stretches each one to the timing of the move it plays, so any dead time at the end slows the strike down. The panel has a trim tool, and trimming is part of the fine-tune pass. Timing itself is set in the combat tuning settings.

## How Owain carries his sword

![Owain's walk carry measured against the raw takes](assets/img/gallery/devlog42_walk_carry_checks_1103.png)

The first rule from the audit covers every sword and shield walk. The aim is a relaxed, natural carry, with joints neutral and muscles working only where the weight of the gear needs them:

- **Wrists neutral.** The angle of the sword and the shield follows from a relaxed hand. The raw takes bent the sword wrist 55 to 88 degrees past rest. The new carry brings it to 46.
- **Sword elbow bent.** The sword has weight, so the arm carries it with a bend of about 24 degrees instead of hanging straight.
- **Shoulders down.** The raw takes looked hunched. The shoulder raise drops from 21 to 25 degrees to 16, and the shoulder joint now sits at or below the base of the neck.
- **Shield at the front left.** It is carried at mid torso, 13 cm in front of the hip and turned about 18 degrees forward. It is a relaxed carry. The raised guard has its own set of clips.
- **One carry for every direction**, so the walks blend together without the sword or shield wobbling.

The raw walks also held the upper arm almost still against the chest while the elbow pumped, so the shoulder looked like it slid in its socket. The new swing comes from a fixed shoulder: the upper arm swings 8 degrees each way once per stride, the forearm follows by 3 degrees a few frames later, and the wrist stays locked. It is used on the six side and diagonal walks.

Out of combat Owain faces where he is going, so only the idle, forward walk and forward jog play. With an enemy within 9 m, or when he locks on, he strafes to face the enemy and every walk and jog direction plays. That is why every direction needs the same carry.

## Changes to the plan

- **Owain's combat clips are now fine-tuned by hand in Blender** before the demo, instead of being corrected only by scripts in Unreal.
- **Every edit must pass a round trip check** back into Unreal before it is used.
- **Timing changes stay in the combat tuning settings.** Clips carry poses, arcs, contact and weight.
- **The paired finishers will also be built in Blender**, now that Owain's clips are there.

## Next

- Finish the audit of all 76 clips, with trims and fine-tuning.
- Export the edited clips back into Unreal and check them in a choreographed fight in the demo clearing.
- Possibly audit the enemy seax clips the same way.
- Animal hand pass, review and batch import into Unreal.
