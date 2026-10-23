---
title: Dev Log #30: Every region gets its own plants, and the seasons turn
date: 2026-10-23
---

Today was about plants. Every hand-built plant set now has a home in one or more of the 11 regions, and one switch turns all of them through the four seasons. The environment test map was rebuilt to prove both.

## A plant list for every region

The game now has 99 plant sets built for KnightZ, from trees and shrubs to grasses, wetland plants, mosses, fungi, litter and crops. Each set is assigned to the regions where it would really grow. Core sets are the dominant or signature plants of a region. Minor sets appear at low weight.

Shared sets follow real habitat. Lowland meadow grasses and pasture plants run through the valleys. Heather, bilberry and bracken cover the high moors. Reeds, sedges and carr woodland fill the wetlands.

Every region also has at least one plant set of its own, so each place looks different on the ground:

- The manor hub keeps the orchards and the field crops: apple, pear, spelt, barley, peas, beans and flax.
- Viroconium has feral plum from old Roman gardens, elder scrub and an ivy kit for ruined walls.
- Wenlock Edge has wych elm, dogwood and spindle on the limestone.
- The Long Forest has small-leaved lime, wild cherry, honeysuckle and a holly understory.
- The Long Mynd has juniper, the Stiperstones reindeer lichen on the rocks, and the High Country rowan.
- The Meres and Mosses have alder and willow carr.
- Salinae has ash pollards and guelder rose.

Ivy and honeysuckle climbing trees are split by host species, so each region gets its own: birch on the Wrekin, wych elm on Wenlock Edge, lime in the Long Forest, alder in the Meres and ash on the Clee Hills.

Third-party plants are no longer used in any region. Bought rocks, logs, stumps and debris are still allowed.

![Plant sets assigned to each of the 11 regions](assets/img/gallery/devlog30_flora_by_region_1022.png)

## Four seasons from one switch

One setting now moves every plant in the project to a season.

- Spring: grass at half height, short and fresh green.
- Summer: full growth.
- Autumn: leaves turn by species. Hawthorn, blackthorn, bramble, cherry, rowan and other shrubs go red. Field maple, oak and the fruit trees go orange. Bracken goes rust. Ash, birch, hazel, willow, lime, elder and alder go gold. Holly, yew, juniper, heather and moss stay green.
- Winter: broadleaf trees go bare and the grass dies back.

The season also sets the day of the year for the sky and light, so the sun matches the plants.

![Grass height by season and leaf colour groups](assets/img/gallery/devlog30_season_switch_1022.png)

## Environment test map rebuilt

The test copy of the hub was replanted with only our own plants, using the list for the manor region. Ground grass across the landscape now draws only from our sets as well.

A fault left some trees floating or sitting inside the crowns of other trees. Trees were placed with collision on, so later trees landed on top of earlier ones. All 233,344 trees, shrubs and crops were dropped to the ground again with collision off, which moved 7,971 of them. A sample check afterwards found none of 6,158 trees floating. New placement runs now work this way from the start.

Leaf litter was also scaled up on the forest floor and now stays visible further from the camera.

## Next

- The larger built oak, ash and alder canopies stay mostly green in autumn. They need their own autumn colours.
- A four-season comparison render of the same woodland view.
- Plant the region lists into the other maps.
