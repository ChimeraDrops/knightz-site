---
title: Dev Log #14: Lighter characters, same faces
date: 2026-10-08
---

The editor ran slowly with several characters in a level on the laptop, so the characters were audited and rebuilt lighter. The faces are unchanged and all 52 facial shapes are kept.

## What was slow

Triangle count was only part of it. Alpha hair cards that overlap on screen, shadows, heavy materials and missing levels of detail cost more. The audit found no LODs, hair cards well over budget and large unique head textures.

## Hair and beards are now textured shells

Hair and beards were compared three ways on Wulfstan: shell plus cards, shell plus a bottom fringe, and shell only. Shell only looked best and cost least, so it is the new method for every character.

- Wulfstan's hair and beard went from 36,492 to about 4,000 triangles, a drop of 89 percent.
- Beards render fully opaque. Hair is masked only along its bottom fade, which removes the overlapping alpha cards.
- Budget per character: hair shell about 2,000 to 2,500 triangles, beard shell about 1,500 to 2,000.

## Lighter bodies and heads

- The large male body went from 34,778 to 22,952 triangles, using a reduction weighted toward joints, the face and the neck seam.
- Heads were reduced while keeping every facial shape.
- A typical story character fell from about 93,000 to about 45,000 triangles.
- Background character sets were reduced to about 66 percent of their previous count. Their clothing was reduced with them.

## Next

Re-import everything into Unreal, set LOD levels at 100, 50, 25 and 10 percent, and build a 20-character test map to measure the editor and a packaged build on the laptop.
