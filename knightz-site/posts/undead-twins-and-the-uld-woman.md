---
title: Dev Log #2: Undead twins and the Uld woman
date: 2026-09-26
---

Three characters landed today: an undead Uld male (UMN1), an Uld woman (FN1) and her undead twin (UFN1).

## Two paths to a character

- **Rebuild (Path B).** A fresh retopology of the source sculpt. Slower, used when a new body has different proportions.
- **Conform (Path A+).** A finished character's mesh is pulled onto the new sculpt with a coarse-to-fine displacement field. The new model inherits the UV layout, eye and mouth openings, weights and garments. The undead woman conformed with a 95th percentile error of about 1.2 mm.

The conform route is the big win. It is how one base body becomes a whole crowd.

## Gore as a material layer

The undead carry their wounds as separate gore variants with their own masks for dried and fresh blood, so the same base asset can be shown clean or ruined.

## Lessons logged

AI-generated sources often come as double-walled shells, and open faces leave hollow pockets inside the head. Both are now detected and fixed by script before retopology.
