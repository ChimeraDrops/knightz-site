---
title: Dev Log #12: Every head is Unreal-ready, Geraint and Custennin, eyelashes, and a live link to the editor
date: 2026-10-07
---

Every finished head now exists as an Unreal Engine package. Geraint is complete, Custennin has a reworked face, and every character has eyelashes.

## Unreal-ready packages

Owain, Bedwyr, Brother Caddoc, Brother Tysilio, Cynan, Geraint, Iddon and Einion Goch are now at the same stage.

- **Head on body.** Each head welds to its body at a 64-vertex neck seam with zero gap. The gap stays under 0.002 mm with the head turned 50 degrees, the neck tilted and the jaw open.
- **Face.** 52 ARKit facial shapes on every head. Owain received his set in this pass.
- **Mouth.** Teeth, gums and tongue have their own textures on every head, with a yellowed set for Tysilio.
- **Export.** Each character has a skeletal mesh package for the head, hair and body. Re-import checks passed with 142 bones, no unweighted vertices and no more than four influences per vertex.
- **Scale fix.** Shape keys did not scale with the mesh on export, which left a 183 cm error on the first run. The export script now scales them directly.

## Eyelashes on every head

Each eye gets an upper and lower lash card shaped to that eye's own opening. The lashes follow the lid, so a blink folds them down. Colours match each character: auburn for Einion, grey-white for Tysilio, near black for Owain and Geraint. The cards cost 136 quads per head.

## Geraint, complete

Geraint's head is finished with skin, 52 facial shapes and a shaggy brown hair cut of about 9,950 quads. He was approved with no touch-ups.

## Custennin

Custennin is a stocky, ruddy older man built on the large male body. His face rig is approved. During hair fitting the face read too small for the skull, so it was widened by about 8 percent across the front and the sides were filled in front of the ears. Eye spacing went from 58.0 to 62.6 mm. Two creases created by the edit were smoothed out. His hair is being regrown on the new shape.

## Body fix

The underside of the upper arm on the standard male body was pulled toward the torso. Weights were changed and the body was re-baked from the A-pose. The armpit now keeps a clean shape and the arm raises and lowers 50 degrees without tearing.

## Unreal connected to Claude

Unreal Engine 5.8 now runs a local server that Claude Desktop connects to. The editor can be inspected and driven from a session, which will speed up importing the character packages and building materials.

## Lessons recorded

- A weight fix on an already baked body does not show at rest. The bake has to be redone.
- Check face width against skull width on every new head before building the rig.
- Show shape changes live in the Blender viewport.

## Next

Custennin's hair, then his body bind and export. After that, Unreal import of the finished characters, materials, and hair level-of-detail meshes.
