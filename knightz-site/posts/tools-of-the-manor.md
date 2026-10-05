---
title: Dev Log #7: Tools of the manor
date: 2026-10-01
---

A manor runs on hand tools, and every job in the simulation needs a prop the folk can be seen using.

## Batch one

Four tools, each in three conditions:

- **A, new.** Clean iron and fresh wood.
- **B, worn.** Ground-back edges, polish where hands grip, grime.
- **C, mended.** Riveted plates over cracks, cord and rawhide bindings, replacement wedges.

Sizes come from Roman and early medieval finds: a Stantonbury-type sickle, a socketed billhook, a lugged work axe on a bowed ash haft, and a one-piece oak spade with an iron shoe.

## Weathering pass

A second texture pass made the wear much clearer: layered rust, dark grime in the cavities, hand grease on the grips, soil on the spade and grain checks in old wood.

## Swappable heads

A new pipeline turns an AI-generated head into a game head that snaps onto a shared base body at a 64-vertex neck seam. One rigged body can now carry many faces, which is how the named cast will be built.
