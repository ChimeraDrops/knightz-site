---
title: Dev Log #29: All 201 clips generated
date: 2026-10-22
---

The female movement set is fully generated. One overnight run produced all 201 clips across the seven weapon sets, and six of those sets are now cut into loops and checked.

## One overnight run

The run started on the evening of 20 October and finished the next morning, just under 15 hours later. Every clip was generated with eight random seeds and the four best takes were kept, so each one has spare takes to fall back on. Single clips took from about half a minute to several minutes. Some side steps were run with a second prompt wording, and the better takes from both were kept.

| Weapon set | Clips generated |
|---|---|
| Unarmed | 30 |
| Sword and shield | 30 |
| Sword | 30 |
| Axe and shield | 30 |
| Seax | 30 |
| Spear | 30 |
| Bow | 21 |
| **Total** | **201** |

![Clips generated over the overnight run, by weapon set](assets/img/gallery/devlog29_hf1_generation_run_1021.png)

## Cut and checked

Each kept take goes through the same steps as before: one gait cycle is cut, the loop seam is closed, and an audit measures direction, speed, hip turn, lean, ground height and foot slide. Any take that steps the wrong way is rejected.

163 clips have been through those checks so far.

- 149 pass. 97 use her own generated take and 52 fall back to the matching male clip, retargeted and scaled to her stride.
- 14 are flagged for another pass. 12 are turns in place that drift too far while turning. 2 are seax idles that lean too far forward.
- The axe and shield set passed all 30 clips with no flags.
- The seax and spear sets lean most on male fallbacks, 13 clips each.
- The bow set and the rest of the sword and shield set are generated and wait to be cut.

![Clip status for all seven weapon sets](assets/img/gallery/devlog29_hf1_clip_status_1021.png)

## Arms

A first arm pass has run on 153 of the checked clips. It adjusts arm and hand positions per weapon set on top of the leg motion, with the weapon sockets confirmed last time.

## Next

- Cut and check the bow set and the remaining 17 sword and shield clips.
- Rework the 14 flagged clips, mainly the turns in place.
- Try new wording on the seax and spear sets to replace some male fallbacks with her own takes.
- Blend spaces and an in-game motion test for a playable woman.
- Review of every clip in the animation review level.
