---
title: Dev Log #26: An ash sky, horses and life on the road
date: 2026-10-18
---

The hub got a new sky. Twelve winters after the sun went grey, the light over the manor now comes through black volcanic ash. Alongside it, a long design session settled how big the world should feel on foot, brought horses into the game and planned several new things to do between fights.

## The ash sky

The old sky and clouds in the hub were removed and replaced with one custom sky system in C++. It drives the sun, the moon, the cloud layer, the lightning and the haze together, in the editor and in game.

- **Two cloud layers.** A heavy layer of black ash sits between about 1.5 and 5 km up, with coverage that drifts slowly over time. A thin, pale veil sits much higher, at about 8.5 to 10 km, and it never clears. That veil is what keeps the sun a dull red disc all day.
- **A gap toward the sun.** The heavy ash thins along the line from the player to the sun, so the sun usually glows through. The gap grows when the sun is low, because the light then passes through more cloud.
- **Heavy cells.** Every 6 to 14 minutes a dense cell drifts across the sun for about two and a half minutes. The ground darkens to 30 percent of normal light and then recovers. It never goes black. A cell can also be held in place for scripted moments.
- **Lightning.** Strikes come rarely, every 20 to 30 minutes, in bursts of one to three strokes. They land 3 to 12 km away, light the inside of the ash and give a short blue-white flash on the ground. Thunder is timed to the distance of the strike.
- **Night.** A second light acts as the moon. It is dim and red.
- **Day length.** A full day and night takes 48 minutes of play for now.

![Sunlight under the ash sky over 90 minutes of play](assets/img/gallery/devlog26_ash_sky_light_1018.png)

Haze and fog were retuned to match: low blue scatter, red-brown dust and red light in the height fog. Exposure is held in a narrow range so the eye does not adjust the gloom away. In test shots at the manor the ground measured 17 under a clear sun and 7 under a heavy cell, on the same scale.

Two crashes came up during the build. Both were fixed by making sure the cloud material is flagged for cloud use and by creating the cloud layer only after its shaders are ready.

## How big the world feels

The world is built from real elevation and river data, and a real valley takes a long time to cross on foot. New rules set the balance.

- Fast travel between regions stays.
- Inside a region the ground is true size by default and never squeezed more than two times. Crossing a region at a jog should take 10 to 15 minutes.
- Only empty land can be compressed: moor, bog, deep wood and long runs of field. The manor, buildings, towns, ruins and fords always stay true size. Buildings are never scaled, only moved.
- Hills keep their real height. Slopes are capped so the ground stays walkable.
- The manor simulation keeps real acres, real yields and real hauling distances. The fields you see are a sample of real-size strips, and the horizon carries the rest.
- Something worth stopping for every one to two minutes of walking.

![Time to cross a region on foot at different compression factors](assets/img/gallery/devlog26_crossing_time_1018.png)

At a game jog of 5 metres per second, the current 3 to 4 km region windows already land inside the target at true size. Larger areas get the minimum compression needed. The hub is the pilot. Each region will be audited before anything moves.

To keep that ground busy, the plan is a small, high quality kit of plants, rocks and clutter per landscape type, scattered by procedural rules from the existing land masks. Grass and small clutter fade out at 50 to 80 metres and shrubs at 150 metres, and distant trees hand over to simplified versions. Density follows the graphics settings, so low settings thin the grass on the same world.

## Horses

Riding is now in the game. This reverses the earlier plan of no horses. The bar is set high: a horse must move with real weight and visible muscle in the flanks and legs, or it does not ship. The approach is a bought, high quality horse with a motion-captured animation set, then a machine-learned muscle deformer trained on a simulation for the flex, foot placement on uneven ground and physics on the mane and tail. Sweat and mud build up as you ride. A stocky breed suits the period. Whether there is fighting from horseback is still open.

## Things to do between fights

Three new activities were designed. All of them feed the manor directly. Nothing goes into a pack to be carried home.

**Tree felling.** Any tree in the world can be cut, including the coppice by the manor. The forest stays cheap instanced foliage. Only the tree you are chopping turns into a physics object. Each hit deepens a notch on your side. When it gives, the trunk hinges on the stump, tips slowly, speeds up and breaks free, then lands with dust, leaves and a camera shake. A falling tree hurts anything it hits, you included. Chop off the crown, split the trunk into logs and send each log to the stores. Stumps are saved, and in time a stump can grow back.

**Spear fishing at the weir.** Stand on the manor weir and spear fish as they pass through the gap. A faint ripple marks your aim, and you must lead the fish for the current and the bend of light in water. Trout and roach are easy. An eel has to be held steady for a moment or it wriggles free. Salmon are fast and rare, mostly in the autumn run. A miss scares the fish off for a few seconds. Muddy spring flood water hides them, and dawn and dusk bring more.

**Hunting.** Deer, boar, hare and birds roam the world as part of normal play. After a kill, one interaction sends the meat, hide, sinew and bone to the stores, where the craftsmen turn them into goods. Rare trophies such as a great stag's antlers or a boar's tusks go into your own pack. Boar fight back.

## Encounters on the road

Walking between places should never be empty. Road events are short, from 30 seconds to 3 minutes, and each one leaves a mark: a new worker, a rumour, a resource or a grudge. Examples include refugees asking for food, an ambush at a ford, a peddler with salt and gossip, a body in a ditch, a Roman ruin with stone to salvage, your own foragers in trouble, wolves at dusk and sudden storms that force you into shelter. The odds shift with season, time of day, region and road. Some travellers turn up again across the seasons and remember what you did last time.

## Paired combat without a motion capture stage

Kills and finishing moves need two bodies that meet. The plan for making them without a mocap studio:

1. Film two people acting each move with foam weapons on a phone, and convert the video into motion. Fill gaps with paired stock animation.
2. Fix contact and impact in a physics-based animation tool and in Blender, where scripts line up the two characters, make the blade meet its target and bake the result.
3. Scripts make variants from each good pair: mirrored, faster and slower, swapped reactions, taller and shorter targets, and different weapon lengths.
4. In Unreal, each move becomes a two-role scene. Both fighters slide into place before contact, and the strike frame triggers the reaction and any lost limb.

Three pilot moves come first: a straight kill, an arm cut and a grab and stab.

## Site

The site now has a Discord invite in the menu and footer, and new dev log entries post to the Discord server on their own.

## Changes to the plan

- Horse riding is in. Mounted combat is undecided.
- New map scale rules: true size inside a region by default, at most two times compression of empty land, real numbers in the simulation.
- Tree felling, spear fishing, hunting and road events added to the design.
- Paired kill animations will come from phone video capture and stock packs, cleaned up by script.

## Next

The base animation set for the four women: idles, walks, jogs, guard walks and turns for each weapon set, plus weapon sockets and the grip layer on the female body. A thunder sound for the sky, and an audit of every region for the new scale rules.
