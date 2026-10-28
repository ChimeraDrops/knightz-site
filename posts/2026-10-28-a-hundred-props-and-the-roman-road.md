---
title: Dev Log #35: A hundred props and the Roman road
date: 2026-10-28
---

The hub had a lot of grey boxes standing in for things that did not exist yet. This push replaced most of them. About 100 new props went in across six batches, plus a full chapel set, the dead, 15 new surface materials and 9 decals. The old Roman road was also built as a kit and laid across its region, with tombstones and monuments along the verge.

![Farm and yard props](assets/img/gallery/devlog35_farm_yard_props_1027.jpg)

## The prop push

Every prop was built from code in Blender. Each one has simple collision and a low detail version for distance, and was imported to Unreal and swapped in for its stand-in box in the hub. Props that had no stand-in were placed by hand around the yard, the fields, the gate and the ford.

The setting is Shropshire around 548 AD, and the props follow the period. Timber is split or hewn. There are no sawn boards, wire nails or glass.

- **Yard and field.** A camp fire ring, faggot and cordwood stacks, hurdles, wattle fences and field gates. Sheaves, stooks and hay ricks. An ard plough and an ox yoke. A tool rack, a water yoke and butt, troughs and strip field stakes.
- **Carts.** Two-wheel carts in whole, tipped and broken states, a four-wheel wagon, a stone sledge and a handcart. Cart loads of stone, timber, faggots, sacks, barrels, hay, dung and salt.
- **River and ruins.** Plank bridges, coracles and a wattle fish weir. Roman column drums and piles of reused masonry. Sharpened stakes, a brazier, a dead hedge and a ford marker post.

![Carts, wagons and their loads](assets/img/gallery/devlog35_carts_and_wagons_1027.jpg)

![River pieces, Roman ruins and hand tools](assets/img/gallery/devlog35_river_ruins_and_tools_1027.jpg)

Coppice regrowth reuses the young hazel and coppice plants already in the game. No new models were needed.

## The chapel set

The chapel got its own set: altars bare and clothed, a Roman stone coffin, a bier and a shrouded body. A funeral pyre comes in three stages: built, burning and ash. There are grave mounds with wooden markers, a bronze cross, candlesticks, a book chest and satchel, a writing desk with its kit, and a chapel bell. The chronicle is there too, closed, open and as loose pages.

![The chapel set](assets/img/gallery/devlog35_chapel_set_1027.jpg)

## The dead

The bodies are made from the existing villager characters, male and female. Each one was posed into a death pose and frozen into a static prop. Blood is painted at the wound and runs toward the ground. Mud sits on the side that touches the ground. The decayed versions use the undead skins with dried blood and mildew. There are six so far: four fresh and two decayed.

A farm animal model became the dead ox at the ford. It is bloated and wet below the waterline.

![Fallen villagers, the ox at the ford and bones](assets/img/gallery/devlog35_the_dead_1027.jpg)

## Bones from images

Bones are hard to model by hand. So they were generated as full 3D models from reference images, on our own GPU. The raw models came out at up to 20 million triangles. The game versions keep the same shape with about 30 times fewer triangles, and the fine detail is carried in the textures. They were judged side by side and approved.

![Bones at full detail (left) and the game versions (right)](assets/img/gallery/devlog35_bones_high_vs_low_1027.jpg)

## Materials and decals

Fifteen new tiling materials and nine decals were generated on our own GPU from text prompts, then turned into game textures with colour, surface bumps and roughness.

The materials: fresh oak, reed thatch, loose straw, mud, flagstone paving, reused Roman masonry, limestone, quartzite, dolerite, volcanic ground, Roman pink render, bronze, lead, bone and vellum.

The decals are single stains cut out of a plain background, so they can be stamped onto any wall or floor: soot, damp, grime, mud splash, scorch, moss and lichen, a daub patch, limewash and blood.

![Fifteen new surface materials](assets/img/gallery/devlog35_new_materials_1027.jpg)

![Nine new decals](assets/img/gallery/devlog35_decals_1027.jpg)

## In the engine

The props now sit in the hub. The ard and yoke are out in a field, stakes and braziers guard the gate, and the ford has the ox and the fallen. The plank bridge was checked in the test level first.

![Props placed in the hub](assets/img/gallery/devlog35_in_engine_1027.jpg)

## The Roman road

Watling Street runs through the region around the old Roman city. It was built as a kit of road pieces, each 5 m long, made to bend along a spline in Unreal.

- **Three road surfaces.** Paved, with intact flags and full kerbs. Broken, with about 40 percent of the flags gone, gravel and mud showing, and puddles. Grass grown, with turf over the raised bed, cart ruts and a few flags and kerbs poking through.
- **Ends and ditches.** End pieces ramp the raised bed down to the ground. A ditch piece adds a side ditch on both sides with a wet bottom, and fades out where the road stops.
- **Seamless joins.** Every piece shares the same end shape, and the surface noise repeats every 5 m, so pieces join with no steps. Textures run on across the joins.

A planner merged the old road tracks into one line about 4 km long, rounded the corners, and kept the road close to the real ground. The road stops short of every brook and picks up again on the far side, where the crossings are ruined fords for now. That gives 4 runs and 770 road pieces. The surface changes along its length, and paved never meets grass grown without a broken stretch between them. Through the city there are no ditches and more paving.

The ground under the road was lowered and blended back to the land around it. Plants and props were moved with the ground, and about 25,000 plants that stood on the road were cleared.

Along the verge east of the city are the roadside graves the Romans left behind. Six tombstone designs were built, some with busts, a standing figure or a rider, plus worn, broken and leaning versions and toppled ones lying face up. There are two tomb monuments, one whole and one robbed of its facing stone, and a milestone. More than 100 grey stand-ins along the road were replaced, and every upright stone was turned to face the road.

## Changes to the plan

- **Complex organic props** such as bones are generated in 3D from reference images. The full model is kept as the source and baked down to a light game mesh. The third-person camera distance sets how much detail each one needs.
- **Bodies are static posed props** built from the character bodies, with no ragdoll physics.

## Next

- Twig cards for the dead hedge, and new soot and damp decals.
- A jaw bone. The reference image produced a second skull.
- Spots for bones and bodies in the other regions. So far they are only in the hub.
- The same road for two more regions, and a crossing piece for the brooks.
- Lettering decals for the tombstones, monuments and milestone.
- A season input for the road verge grass.
