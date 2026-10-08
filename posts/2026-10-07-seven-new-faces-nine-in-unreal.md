---
title: Dev Log #13: Seven new faces, and nine characters standing in Unreal
date: 2026-10-07
---

Seven more heads were built overnight, bringing the finished count to sixteen. Nine of the characters now stand and move in Unreal Engine on skeletons rebuilt to match Unreal's own mannequin.

## Seven new heads

Wulfstan, Gwalchmai, Hrothmund, Morfran, Madog, Bleddyn and Tudwal were built in one batch on the same pipeline as the earlier heads: seam fit, expressive topology, skin, 52 facial shapes, hair, eyelashes and mouth parts.

## Nine characters in Unreal

- Owain, Bedwyr, Brother Caddoc, Brother Tysilio, Cynan and Geraint stand on the standard male body. Iddon, Einion Goch and Custennin stand on the large male body.
- Each has his head with 52 facial shapes, hair, beard where he has one, eyelashes, mouth parts and his own textures and materials.
- All nine stand in a review line in the test level and run the unarmed set: idle, walk, jog, jump, three attacks, a charged attack and hit reactions.

## Skeletons rebuilt to match Unreal's mannequin

- The first import used the skeleton from Blender. Unreal's animations played with twisted arms and stiff legs because the bone directions differ from the mannequin.
- Each body now gets a skeleton built from the mannequin's own bones, moved to fit the character. Bone directions match within 8 degrees, so the mannequin animations transfer with default settings.
- The face, skirt and cloak bones from the Blender rig stay on top, so facial shapes and future clothing physics still work.
- Feet and hands drive the foot and hand IK bones during the transfer. Without that, the legs froze in place while walking.

## Faster pipeline

- One script per body sets up the skeleton, animations and character blueprint. One script per character imports head, hair, beard and textures and builds the materials. A head takes about 30 seconds.
- Two corrupted texture files were found, and the import now checks every image before using it.

## Tools

- Epic's Unreal MCP plugin (UE 5.8) runs with the All Toolsets plugin, about 50 toolsets covering assets, skeletal meshes, materials, Blueprints, animation and Play-In-Editor.
- A project plugin adds Python in the editor through the same link and moves with the project drive between computers.
- Project conventions are stored inside the editor as an agent skill, now updated with the skeleton rules.

## Source control

The Unreal project is under private version control with Git LFS. Every batch of automated changes is committed before and after, so any batch can be rolled back. File locking made every asset read-only and stopped Unreal from saving, so locking was turned off for this solo project.

## Plugins enabled

- Mutable, for swappable heads, hair and garments. To be tested against the current setup.
- Live Link Face Importer, for iPhone facial capture onto the 52-shape heads.

## Next

Owner review of all nine characters, beard and eyelash shapes driven from the face, a better eye material, and a Mutable test.
