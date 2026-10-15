---
title: Dev Log #23: Firelight, earthworks and the first trees
date: 2026-10-15
---

The buildings from the last entry were empty shells. Now they have furniture, tools, fires and doors that open. The manor has a bank, a ditch and a walkway on its palisade. Outside the walls, the first three tree species are built and planted, the rivers have real water, and the whole hub streams by distance.

## Furniture and craft props

Two new prop kits fill the buildings. The household kit has 43 meshes: long and round hearths, a cauldron, benches, trestle tables, a high table, box beds and sleeping platforms, chests, shields on posts, spear racks, a tafl board, and five kinds of light from candle to lantern.

![Household props: hearths, beds, benches, chests, racks and lights](assets/img/gallery/devlog23_household_props_1015.jpg)

The craft kit adds 37 more: a forge with bellows, anvil and quench trough, a warp-weighted loom, a rotary quern, a beehive clay oven, brewing vats, barrels, salt sets, fish and eel traps, a pole lathe, pottery, baskets and rope. Grain sacks, grain bins and woodpiles followed later in the day.

A dressing script places the props from a short list per building. Fourteen buildings are dressed: the hall alone has 57 items. A check then tests every doorway for a clear path on both sides. Eight buildings had a bench, sack or tool in the way, and all were moved.

## Fire and light

Every hearth, forge, oven and lamp now gives off warm light. Values were tuned by hand: the first pass at three times the final strength turned the bakehouse solid orange. The hall has 12 lights. Most buildings have one to three.

Fires use small particle systems for flames, embers and smoke, and every light flickers through a shared light function. A pot crane was added over the hall hearth so the cauldron chain hangs from a beam.

![The hall with the long hearth, benches, shields on the posts and the high table](assets/img/gallery/devlog23_hall_firelight_1015.jpg)

## Doors that open

Every door in the manor is now an automatic door. It swings away from whoever walks up to it and closes behind them once they leave. The leaves ignore the player's collision, so a fast run never snags on a swinging door. The hall double door, the granaries, the longhouses, the workshops and the byre gates all use it.

## Bank, ditch and walkway

The manor defences are now a full earthwork: a ditch outside, a bank inside and the palisade on the crest. A plank bridge crosses the ditch at the north gate. A walkway runs along the inside of the palisade with a ladder every tenth section.

The gate tower was rebuilt as a gatehouse with its posts outside the passage and no braces across it. Its deck sits at walkway height, so defenders walk straight onto it from the rampart.

## Trees built in Blender

No tree pack covered the native species the hub needs, so they are built in Blender with one generator. Oak came first, then ash and alder from the same code with different rules for branching, leaves and bark. Each tree has bending wind animation, trunk collision and a flat stand-in for long distance.

![Height of every tree variant](assets/img/gallery/devlog23_tree_variants_1015.png)

Each species has its own winter look. Ash and alder drop their leaves and keep some keys, cones and catkins. Young oaks keep their brown leaves through winter, as real ones do. The season changes with the in-game day: autumn colour from day 260 and bare branches from day 310 to day 105.

![First oak in an Unreal test level](assets/img/gallery/devlog23_oak_test_1015.jpg)

## Dressing the hub

The hub now has about 4,400 oaks, 1,400 ash, 600 alder and 22,600 hazel coppice stools, all from the placement plan with no random scatter. Hawthorn, blackthorn and willow use stand-ins for now. Ground cover changes by zone: pasture, meadow, field, woodland floor, wood edge, bank and verge.

The river banks were regraded so they slope into the water. Reeds now grow in 210 dense beds on the inside of bends and at stream mouths, about 45,000 plants in total. One wetland plant pack shipped without textures and was removed. New rule: only fully textured plant packs go in.

## Water

The rivers, the mill leat and the brook now share one continuous water surface with a flow direction baked in. The surface moves downstream, turns lighter in the shallows and fades out at the banks. The main river is about 3 m deep. The ford is 50 cm deep, so it can be waded.

## Streaming by distance

The hub map is now split into cells that load by distance. Buildings with all their props load within 300 m and swap to a simple stand-in beyond that. Trees load within 700 m and ground cover within 200 m. The map used to take up to 20 minutes to save and now saves in under a second.

First measurement with the game running standalone at the north gate: about 6.7 ms per frame, roughly 150 frames per second, with about 570,000 plant and prop instances in range.

## Voices

A local text-to-speech tool now runs on the desktop GPU. A first voice was picked for each of 17 speaking roles from a public speech dataset with English, Scottish and Irish accents. Each line takes 1 to 5 seconds to generate. The women's cast is next.

## Changes to the plan

- The hub moved onto the map built from real elevation data. The older hand-made version of the hub is retired.
- Riding is dropped.
- Native trees are built in-house. Stand-in trees from other species are not used in the woods.

## Next

The remaining farm and field props (ploughs, carts, hay ricks, hurdles and tools), chapel furnishings, and the yard buildings: pigsty, hen coop, corn-drying kiln, hay shelter and privy. Holly, birch and hawthorn are the next trees.
