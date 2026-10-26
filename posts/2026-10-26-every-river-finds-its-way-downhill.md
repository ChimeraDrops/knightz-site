---
title: Dev Log #33: Every river finds its way downhill
date: 2026-10-26
---

Two pieces of work landed this time. The new water now runs through all eleven regions, and the land along every creek and river was cut so the water always flows one way and can always be seen. The four women also got all twelve outfits rebuilt, with real capes, fitted gowns and proper footwear.

![The river at Salinae under the willows, one continuous channel](assets/img/gallery/devlog33_salwarpe_flowing_1025.jpg)

## Water on every region

The water approved on the test maps was placed on all eleven regions: rivers, creeks, lakes, rocks with wakes in the creeks, and the bed texture under the water. It keeps the moving water around the player, the darker creek water and the creek and river bed.

## What the survey found

A flight along the creeks turned up problems. At Salinae the water showed only in sections, the river ran in two directions, and a slab with straight edges sat across the river at the ford.

![Before: the slab at the Salinae ford, a placeholder sitting above floating water](assets/img/gallery/devlog33_salinae_ford_before_1024.jpg)

A check of every region measured how much river length had its water hidden below the ground. It ranged from 16% to 49% depending on the region.

The causes were simple. Each stream piece picked its own direction. Water levels were not tied to a steady downhill line. Wherever the ground bumped up along a creek, the water ended up under it.

## The fixes

- **One direction per river system.** Every connected set of streams now drains to a single lowest exit: the map edge, a wider river or a lake. At Salinae the whole river now flows west, as the real river does.
- **A steady fall.** The water level never rises downstream. Creek water is 35 to 60 cm deep. River water is 60 cm to 1.8 m deep. The surface stays below the banks.
- **The land is cut to carry the water.** Channels are carved along every creek and river, with a curved bed and banks that ease back into the land. Creek lines are first moved onto the real valley floor nearby, so most cuts are under a metre. Plants standing in the water were cleared, and plants on the cut banks were lowered with the ground.
- **Crossings.** Where a road meets a creek, the road dips into a shallow ford with gentle approaches. At Salinae and at the Severn ford, gravel bars lie across the river about 25 cm under the water, from marker post to marker post.
- **Darker creek water.** Shallow water over the light bed looked like a dry path from above. It is now darker and more tinted, and reads as water from the air and from the bank.

![Salinae from above. Blue is the water, orange is where the ground was cut, and the arrows show the flow, all heading west.](assets/img/gallery/devlog33_salinae_flow_carve_map_1025.jpg)

![After: the Salinae ford, shallow water across the road over a gravel bar](assets/img/gallery/devlog33_salwarpe_ford_1025.jpg)

![The Severn ford: a gravel bar under the water from post to post](assets/img/gallery/devlog33_severn_ford_gravel_1025.jpg)

The ruined Roman bridge piers still stand in the Severn beside the ford.

![The ruined Roman bridge piers in the Severn](assets/img/gallery/devlog33_roman_piers_1025.jpg)

## Results

Hidden water dropped to 0% in ten regions. Shrowesbery shows 5%, all inside the original test stretch, which stays as approved. Between 81% and 99% of the mapped stream length now carries visible water. The rest are short stretches where the mapped stream crosses ground too high to cut through. Those are dry for now.

![River length with water hidden below ground, before and after the carve, per region](assets/img/gallery/devlog33_hidden_water_chart_1025.png)

| Region | Hidden before | Hidden after |
|---|---|---|
| Shrowesbery | 28% | 5% (test stretch) |
| Viroconium | 20% | 0% |
| Wrekin | 16% | 0% |
| Wenlock Edge | 25% | 0% |
| Long Forest | 31% | 0% |
| Long Mynd | 35% | 0% |
| Stiperstones | 32% | 0% |
| High Country | 32% | 0% |
| Meres | 49% | 0% |
| Clee Hills | 41% | 0% |
| Salinae | 28% | 0% |

Creek rocks are now drawn in batches per rock shape instead of thousands of single objects, which makes them lighter to draw.

![The Severn at Viroconium](assets/img/gallery/devlog33_severn_wide_1025.jpg)

![High Country: moorland streams cut into the hillside](assets/img/gallery/devlog33_moorland_streams_1025.jpg)

## Outfits for the women

All twelve outfits for Rhiannon, Elen, Hild and Nest were rebuilt, three each.

A motion review showed the capes puffing out behind the characters like a balloon. Several "capes" were really sleeved over-dresses. With clothes on, the women looked broad shouldered and heavy, while the body underneath is fit.

The capes ballooned because the cloth simulation collided against a body shape too large for these characters. A collision body sized to their real proportions fixed it. Nest's court outfit was rebuilt first as a pilot and approved before the rest were touched.

![Nest's court outfit before and after: the old over-dress against the new fitted gown and open cape pinned at the chest](assets/img/gallery/devlog33_cape_before_after_1025.jpg)

- **Real capes.** Every over-garment is now an open cape, pinned with brooches at the front of the chest and hanging behind the arms with no sleeves. Eight capes, each with its own brooch set.
- **Fitted gowns.** Gowns follow the waist and hips and flare below, in fine linen and soft wool. On the pilot, outfit width at the shoulders dropped from 31 cm to 22.5 cm.
- **Nothing poking through.** Under-layers keep only the parts that can be seen, such as cuffs and a hem band. The pilot under-gown went from 12,058 triangles to 236. Skin under clothing is hidden per outfit, so knees and shins no longer show through skirts while running.
- **Movement.** Skirts on the long, knee and riding gowns and all eight capes move with cloth simulation. Aprons and short gowns stay fitted to the body.

![All twelve rebuilt outfits in the engine, shot before the new footwear went on](assets/img/gallery/devlog33_outfits_lineup_1025.jpg)

## Period footwear

The old shoes looked like brown paint on the feet. Three period styles replace them:

- **Turnshoes.** Soft low shoes with a seam down the top of the foot and a leather thong tied around the ankle.
- **Ankle boots.** Closed above the ankle bone with two toggles at the front.
- **Tall boots.** To just below the knee, laced up the front, with a turned cuff.

All three have a separate sole, a darker leather band at the opening, a rounded toe box and full heel coverage. Each has four levels of detail. At the top level a pair is about 4,800, 5,400 and 6,600 triangles.

Turnshoes go with the court, feast, courtship, healer, Saxon and British gowns. Ankle boots go with the winter outfit, and under leg wraps with the forge and refugee outfits. Tall boots go with the expedition and riding outfits. The rites outfit stays barefoot.

![The three footwear styles from the front, side, three-quarter and back](assets/img/gallery/devlog33_period_footwear_1025.jpg)

## Changes to the plan

- Every river system now drains one way to a single exit, and the ground is carved to carry it.
- Roads cross creeks at shallow fords. Large river crossings use gravel bar fords.
- All over-garments for the women are open capes. Sleeved over-dresses are dropped.

## Next

- Decide on the short dry stretches: carve deeper, or let the stream sink and reappear.
- Two places where a road meets a big river with no crossing yet.
- Swimming depth and current, splashes and bank dressing.
- Grass growing up through shallow water on the bed.
- A lighter cloth mesh for the long skirts, and footwear colour variations per character.
