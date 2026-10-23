from h import fig, prompt, table, stats, script, section, step

I = "../assets/img/videos/ep4/"
G = "../assets/img/gallery/"
RM = "../assets/img/roadmap/"
body = ""

body += section("overview", "Overview", f"""
<p class="lead">Eleven maps of real ground, 99 plant sets built by hand, more than 60 million plants placed by script, one switch for the seasons and a sky full of volcanic ash. This is how the world of KnightZ was built in two weeks with Claude, Blender and Unreal Engine 5.</p>
<p>Episode 4 covers the environment pipeline from the ground up: real elevation data turned into game terrain, rules for how big a map should feel on foot, plans that place every tree and building, rivers that flow, trees and plants modelled in Blender instead of bought, a season system that drives every leaf, and a custom sky. Each step lists the tools, the numbers and the mistakes that cost time.</p>
{stats([("11", "region maps from real elevation"), ("99", "hand-built plant sets"), ("60 M+", "plants placed across the maps"), ("4", "seasons from one switch")])}
<div class="note"><b>Video status.</b> The video for this episode is being recorded now. This page is the full written breakdown and goes live first. The <a href="../roadmap.html">RoadMap</a> has the checklists behind every section below.</div>
""")

body += section("plan", "Episode plan", table(["#", "Segment", "What it shows"], [
    ["1", "Cold open", "One woodland view turning through spring, summer, autumn and winter"],
    ["2", "Real ground", "Elevation data and rivers turned into 2017 x 2017 heightmaps"],
    ["3", "How big is a map?", "Crossing time, true-size story sites and squeezed empty land"],
    ["4", "Plans before props", "Placement plans, gray box and biomes"],
    ["5", "Water", "One continuous river surface and the ford"],
    ["6", "Trees from Blender", "Why the bought packs went, and how a tree is built"],
    ["7", "Shrubs, climbers and 54 ground plants", "Four seasons on one texture sheet"],
    ["8", "Five million plants", "The environment test map and the density rules"],
    ["9", "One plant list per region", "Core, minor and exclusive sets"],
    ["10", "The season switch", "Grass height and autumn colour groups"],
    ["11", "The ash sky", "Two cloud layers, sun cover, lightning and a red moon"],
    ["12", "Streaming and performance", "World Partition grids and draw distances"],
    ["13", "Lessons and what's next", "Six mistakes and the next episode"],
]))

body += section("software", "Software and tools", table(
    ["Tool", "Role in this episode"],
    [
        ["Claude (desktop app)", "Planning, every script, review of every capture, project docs as memory between sessions"],
        ["Claude skills", "/newtree builds a tree species from a reference folder; plant and shrub procedures saved as docs"],
        ["Blender 5.2 with Blender MCP", "Trees, shrubs, climbers, 54 ground plants, water mesh, impostor and wind bakes"],
        ["Unreal Engine 5.8 with Unreal MCP", "Landscapes, World Partition, foliage placement, materials, sky system in C++"],
        ["Python", "Heightmaps, placement plans, biome maps, density maps and the season switch"],
        ["Copernicus GLO-30", "30 m surface elevation data for the real terrain"],
        ["OpenStreetMap", "Rivers, brooks and lakes (ODbL)"],
        ["Pivot Painter 2", "Per-branch wind on the trees"],
        ["Git with LFS", "Every map and asset committed from the editor"],
    ]))

body += section("real-ground", "Real ground from elevation data", f"""
<p>The game is set in western Britain in AD 548, so the land is real. Each region map starts from a window cut out of satellite elevation data around the real place.</p>
{step(1, "Get the elevation")}
<p>Copernicus GLO-30 is a free 30 m surface model of the world. It is a surface model, so it includes trees and buildings. A grey-scale opening with a 90 m kernel strips them off and leaves the ground.</p>
{step(2, "Add the water")}
<p>Rivers, brooks and lakes come from OpenStreetMap. Modern water is removed: canals, reservoirs, fish pools and park lakes. River banks are regraded with runoff gullies so the water sits in a believable channel.</p>
{step(3, "Write the heightmap")}
<p>Each map becomes a 2017 x 2017 pixel, 16-bit heightmap with masks for forest, field, meadow, moor, marsh, road, river, ruin and rock, plus a metadata file with the exact scale for Unreal. Building pads are flattened into the ground where the manor and other sites stand.</p>
<div class="fig-2">
{fig(I+"real_map.jpg", "Hillshade of the real terrain at the manor with the Severn", "The manor window: hillshade from the elevation data with the Severn loop in blue.")}
{fig(I+"river_map.jpg", "River channel cut into the terrain", "The river channel cut into the ground with the brook joining from the south.")}
</div>
{fig(I+"bank_compare.jpg", "River banks before and after regrading", "River banks before (left) and after the regrade with runoff gullies (right).")}
{table(["Map", "Ground range in game", "Real reference"], [
    ["M03 The Wrekin", "103 to 396 m", "Summit 407 m"],
    ["M04 Wenlock Edge", "96 to 276 m", "Edge top about 280 m"],
    ["M06 The Long Mynd", "221 to 512 m", "Pole Bank 516 m"],
    ["M07 The Stiperstones", "247 to 523 m", "Manstone Rock 536 m"],
    ["M10 The Clee Hills", "183 to 532 m", "Abdon Burf 540 m"],
    ["M11 Salinae", "26 to 59 m", "River about 30 m, hill about 55 m"],
])}
<div class="note"><b>Lesson.</b> Summits read 4 to 14 m low. The same 90 m opening that strips trees also trims narrow hilltops. A summit restore pass is on the list.</div>
""")

body += section("scale", "How big should a map feel?", f"""
<p>A real valley takes a long time to cross on foot. The rules below were settled in one design session and applied to every map.</p>
<ul>
<li><b>Measure in time.</b> Crossing a map at a 5 m/s jog should take 10 to 15 minutes.</li>
<li><b>True size by default.</b> Only empty land (moor, bog, deep wood, long field runs) can be squeezed, and never more than 2x.</li>
<li><b>Places stay true size.</b> The manor, buildings, towns, ruins and fords sit in keep zones that are copied 1:1. Buildings are moved, never scaled.</li>
<li><b>Height is never compressed.</b> Squeezed land gets steeper, so slopes over 33 degrees outside keep zones are smoothed (30 passes).</li>
<li><b>Density target.</b> Something worth stopping for every 1 to 2 minutes of walking.</li>
<li><b>The simulation keeps real acres.</b> The fields you see are a sample of real-size strips; the manor's books use the true total.</li>
</ul>
{fig(I+"chart_crossing.jpg", "Crossing time for each region map", "Crossing time for every map. Five maps are squeezed by 1.15x to 1.25x, the rest are true size. Salinae is a small town map by design.")}
<p>The warp is separable and monotone, so rivers stay continuous. Every later tool converts real coordinates to game coordinates through the same warp table stored with the map.</p>
{prompt("Owner decisions before the overnight build (condensed)", "Scope: rebuild M02 to M10, build M11 Salinae new.\nElevation: same source and method as M01 (bank regrade with runoff gullies, building pads).\nScale: compress per the map scale procedure. Keep zones 1:1, height never scaled, slopes capped.\nFoliage: M01 density, our own plants only, per the plant allocation by map.\nClearings: building footprint + 8 m with no trees, shrubs or tall plants;\nshort grass allowed from 2 m outside the walls.", "<b>What it did:</b> Claude rebuilt ten maps overnight with no step errors.<br><b>Why it worked:</b> every rule pointed at a saved project doc, so nothing had to be explained twice, and the clearing rule was a number, not a description.")}
""")

body += section("plans", "Plans before props", f"""
<p>Nothing is placed by hand. A Python planner per map reads authored zones (the manor, fields, coppice, ford, ruins) and writes rule rasters at 1 m. Trees, props and buildings are then scattered with Poisson spacing so nothing overlaps and nothing lines up.</p>
<ul>
<li>The hub gray box: <b>49,259</b> placeholder props in 74 sets, so scale and walking time could be tested before any art existed.</li>
<li>The coppice wood near the manor is managed the period way: six panels cut on rotation under oak standards.</li>
<li>Every building pad is cleared for its footprint plus 8 m.</li>
</ul>
{fig(I+"graybox_manor.jpg", "Gray-box manor with placeholder buildings", "The manor in gray box: placeholder blocks and props on the real ground before final art.")}
<h3>Biomes</h3>
<p>Each map is split into biomes from the plan masks and the terrain: slope, height above the nearest water, altitude over 250 m, building footprints and scene zones. Edges are softened with noise so one biome bleeds into the next.</p>
{fig(I+"biomes_m02_m11.jpg", "Biome maps for ten regions", "Biome maps for M02 to M11. Dark green woodland, light green pasture, purple moor, blue-green wet ground, yellow fields.")}
{table(["Map", "Main biomes"], [
    ["M05 The Long Forest", "Woodland 80%, wet woodland along the brooks 16%"],
    ["M06 The Long Mynd", "Heather and bilberry moor 58%, batch woods 20%, bog and flush 8%, rock and scree 4%"],
    ["M09 The Meres", "Mere-country woods and carr 56%, pasture 25%, water 6%, bog 3%"],
    ["M11 Salinae", "Pasture 54%, strip fields 17%, town 11%, wet grassland 7%"],
])}
""")

body += section("water", "Water that flows", f"""
<p>The Severn, the mill leat and the brook share <b>one continuous water mesh</b> built in Blender: 9 tiles, 119,000 triangles, with the flow direction baked into the mesh. The material moves the surface downstream, lightens it in the shallows and fades it at the banks.</p>
<ul><li>The Severn is about 3 m deep.</li><li>The ford is 50 cm deep, so it can be waded.</li></ul>
<div class="fig-2">
{fig(I+"water_ford.jpg", "The ford on the Severn", "The ford: shallow enough to cross on foot.")}
{fig(I+"sky_river.jpg", "River and alders under the ash sky", "The river with alders on the bank, under the ash sky.")}
</div>
""")

body += section("trees", "Trees built in Blender", f"""
<p>The first plan was to buy foliage. An audit of the bought packs changed that: most did not match the period or the region, some had no textures, and the clean-up removed <b>2,911 packages and 13 GB</b>. New rule: only fully textured packs are kept, and every plant in the game is built for KnightZ.</p>
{step(1, "Grow a skeleton")}
<p>A Python script grows each tree in four levels: trunk, limbs, branches and branchlets, with twigs and leaf cards riding on the last level. Rules per species set the shape: a tall leader for ash, a cone for alder, a dense tangle for hawthorn.</p>
{step(2, "Bark and leaf cards")}
<p>Bark is tiled with species detail. Leaves are cards cut from a leaf sheet with opacity, roughness and translucency packed into one mask.</p>
{step(3, "Wind")}
<p>Pivot Painter 2 stores a pivot and a direction for every branch, so wind moves the trunk, limbs, branches and twigs separately.</p>
{step(4, "Far trees")}
<p>Impostors: the tree is rendered from 144 directions (12 x 12) into a 2048 atlas. Past a set distance the mesh is swapped for one flat card that shows the right view.</p>
{step(5, "Seasons and budget")}
<p>Each species has mature, young and old forms and spring, summer, autumn and winter states. Young oaks keep their brown leaves through winter, as real ones do. Full detail is capped at 5,000 triangles.</p>
{fig(I+"oak_sheet.jpg", "Oak variants in summer and winter", "The oak set: young, mature, veteran, pollard and dead forms in summer (top) and winter (bottom).")}
<div class="fig-2">
{fig(I+"ashalder_summer.jpg", "Ash and alder variants in summer", "Ash and alder, summer.")}
{fig(I+"ashalder_winter.jpg", "Ash and alder variants in winter", "Ash and alder, winter.")}
</div>
<div class="fig-2">
{fig(I+"oak_wind.jpg", "Oaks in Unreal with wind", "Oaks in Unreal with per-branch wind.")}
{fig(I+"impostor_row.jpg", "A row of trees fading from mesh to impostor", "Distance test: meshes near the camera, impostor cards far away.")}
</div>
{prompt("Building a new species", "/newtree \"Rowan reference folder\"", "<b>What it does:</b> the skill reads the reference photos in the folder and builds mature, young and old forms in three seasons with levels of detail and the 5,000-triangle cap, then updates the procedure and writes the Unreal import notes.<br><b>Why it matters:</b> after the oak, every species was a one-line prompt. 21 species and 66 meshes exist now.")}
<p>The full species list with every step is on the <a href="../roadmap/trees.html">Trees checklist</a>.</p>
""")

body += section("shrubs", "Shrubs, understory and climbers", f"""
<p>Below the canopy sit 11 shrubs (hazel coppice, hawthorn and blackthorn thickets, holly, elder, osier willow, dog rose, dogwood, spindle, guelder rose and juniper), 4 understory plants (bracken, bramble, heather and bilberry) and 2 climber kits.</p>
<p>The ivy kit has mats, caps, edges, hangs and stems for ruined Roman walls. The honeysuckle kit has twines, loops, sprays and hangs. Both are also baked onto host trees, split by species so each region gets its own: birch on the Wrekin, wych elm on Wenlock Edge, lime in the Long Forest, alder in the Meres and ash on the Clee Hills.</p>
<div class="fig-2">
{fig(RM+"shrubs/ivy.jpg", "Ivy kit pieces", "The ivy kit.")}
{fig(RM+"shrubs/dogwood.jpg", "Dogwood in autumn", "Dogwood in autumn, one of the Wenlock Edge plants.")}
</div>
""")

body += section("plants", "54 ground plants, four seasons on one sheet", f"""
<p>The ground layer has 54 plants: woodland flowers, ferns, mosses, fungi and litter; grasses and meadow herbs; reeds, sedges and bog plants; and the crops of the manor (spelt, six-row barley, oats, rye, peas, field beans, flax, leeks, onions, garlic, brassicas and orchard fruit). Each is under 1,000 triangles.</p>
<h3>One texture sheet, four seasons</h3>
<p>Every plant's texture sheet is split into four quarters: spring top-left, summer top-right, autumn bottom-left, winter bottom-right. The material shifts the texture coordinates by half a sheet to pick the season, so a season change costs nothing at run time and needs no second mesh.</p>
{fig(I+"bluebell_seasons.jpg", "Bluebell in spring, summer, autumn and winter", "Bluebell from one mesh and one sheet: spring, summer, autumn and winter.")}
{fig(I+"card_sheet_barley.jpg", "Six-row barley card sheet", "A crop card sheet: six-row barley.")}
<div class="fig-2">
{fig(RM+"plants/c04.jpg", "Ramsons close-up", "Ramsons, spring.")}
{fig(RM+"plants/f07.jpg", "Flax close-up", "Flax, one of the manor crops.")}
</div>
<p>All 54 with their regions are on the <a href="../roadmap/ground-plants.html">Ground Plants checklist</a>.</p>
""")

body += section("five-million", "Five million plants on a test map", f"""
<p>The hub was copied to an environment test map, 3 km by 3 km, so ground cover could be tuned without touching the real map. The ash sky was swapped for plain white light there so plant colours could be judged on their own.</p>
<ul>
<li><b>10 biomes</b> from the existing masks: grazed pasture, woodland interior, wood edge, hay meadow, wet grassland, river bank, fallow, two crop fields and the manor gardens.</li>
<li><b>44 plant layers</b>, each with its own meshes, spacing, scale and random seed.</li>
<li><b>Density</b> = biome weight x clump noise (8 to 45 m) x broad noise (160 m). That gives drifts, thin grazed patches and carpets of one flower.</li>
<li><b>5,244,259 plants</b>, grouped into one batch per mesh per 256 m cell.</li>
</ul>
{table(["Plant size", "Draw distance"], [["Litter and moss", "30 to 60 m"], ["Short herbs", "60 to 110 m"], ["Tall herbs and tussocks", "140 to 200 m"], ["Reeds", "320 m"], ["Crops", "650 m"]])}
<div class="fig-2">
{fig(G+"devlog27_woodland_floor_1019.jpg", "Woodland floor with bluebells and ferns", "Woodland floor.")}
{fig(G+"devlog27_hay_meadow_1019.jpg", "Hay meadow", "Hay meadow.")}
</div>
<div class="fig-2">
{fig(G+"devlog27_grain_field_1019.jpg", "Strip field of grain", "Crop strips.")}
{fig(I+"meadow.jpg", "Pasture with clover and buttercups", "Pasture after the ground-grass fix.")}
</div>
<div class="note"><b>Black leaves.</b> Leaves turned black under some light angles. The cause was the normals on the leaf cards. The fix went into the shared plant materials, so every plant in the project was fixed at once.</div>
<p>After the owner approved the test map, the same planting was rebuilt on the real hub: <b>5,559,591</b> plant instances, <b>33,681</b> trees and shrubs and <b>249,300</b> crop tiles.</p>
""")

body += section("regions-plants", "One plant list per region", f"""
<p>All 99 plant sets were assigned to the 11 maps by real habitat. Core sets are the dominant or signature plants of a map; minor sets appear at low weight. Every map has at least one set of its own, so each place looks different on the ground.</p>
{table(["Map", "Plants found only here"], [
    ["M01 Pengwern (the manor)", "Orchard apple and pear, spelt, barley, peas, field beans, flax"],
    ["M02 Viroconium", "Feral plum from Roman gardens, elder scrub, ivy on ruined walls"],
    ["M04 Wenlock Edge", "Wych elm, dogwood, spindle"],
    ["M05 The Long Forest", "Small-leaved lime, wild cherry, honeysuckle, holly understory"],
    ["M06 The Long Mynd", "Juniper"],
    ["M07 The Stiperstones", "Reindeer lichen"],
    ["M08 The High Country", "Rowan"],
    ["M09 The Meres", "Alder and willow carr"],
    ["M11 Salinae", "Ash pollards, guelder rose"],
])}
{fig(G+"devlog30_flora_by_region_1022.png", "Plant sets by region", "Plant sets assigned to each region.")}
{fig(I+"chart_plants.jpg", "Trees and ground plants per map", "Plants placed per map after the overnight build. The Long Forest has the most trees; the moors carry the most ground plants.")}
<div class="fig-2">
{fig(I+"m03_wrekin.jpg", "The Wrekin in autumn", "The Wrekin: hanging woods below the open crest.")}
{fig(I+"m06_polebank.jpg", "Heather and bilberry on the Long Mynd", "Pole Bank on the Long Mynd: heather and bilberry.")}
</div>
""")

body += section("seasons", "The season switch", f"""
<p>One call sets the season for the whole project: <code>set_season('autumn')</code>. It drives the plant material parameters, the older tree materials and the day of the year for the sun.</p>
{table(["Season", "Sheet quarter", "Grass height", "Leaves", "Sun day"], [
    ["Spring", "Top left", "Half", "Fresh green", "120"],
    ["Summer", "Top right", "Full", "Full growth", "196"],
    ["Autumn", "Bottom left", "Full", "Colour by species", "303"],
    ["Winter", "Bottom right", "Full, dead", "Broadleaf trees bare", "15"],
])}
{table(["Autumn group", "Species"], [
    ["Red", "Hawthorn, blackthorn, bramble, dog rose, wild cherry, rowan, dogwood, spindle, guelder rose, crab apple, bilberry"],
    ["Orange", "Field maple, apple, pear, plum, both oaks"],
    ["Rust", "Bracken"],
    ["Gold", "Ash, birch, hazel, willow, lime, wych elm, elder, alder"],
    ["Stays green", "Holly, yew, juniper, heather, moss, clover"],
])}
{fig(I+"seasons_grid.jpg", "The same woodland in four seasons", "One woodland view in spring, summer, autumn and winter.")}
<div class="note"><b>Floating trees.</b> Trees were placed with collision on, so later trees landed on the crowns of earlier ones. All 233,344 trees, shrubs and crops were dropped again with collision off: 7,971 moved, and a check of 6,158 found none floating. Placement now always runs with collision off.</div>
""")

body += section("sky", "The volcanic ash sky", f"""
<p>Twelve winters after the sun went grey, the light comes through ash. The brief for the sky was short:</p>
{prompt("Sky brief (condensed)", "Black volcanic ash clouds. Lightning every 20 to 30 minutes, not constant.\nThin high cloud always over the sun so it glows red.\nNow and then a heavy black cloud covers the sun: darker, but never black, always a red glow.\nA dim red moon at night.", "<b>What it did:</b> Claude wrote one sky system in C++ that drives the sun, moon, clouds, lightning and haze together.<br><b>Why it worked:</b> every line is something you can see and check in a screenshot.")}
{table(["Part", "Setting"], [
    ["Heavy ash layer", "1.5 to 5.3 km, drifting coverage"],
    ["High veil", "8.5 to 10 km, always present, keeps the sun red"],
    ["Gap toward the sun", "Heavy ash thins along the sightline, wider at low sun"],
    ["Sun cover", "A heavy cell every 6 to 14 minutes for about 150 s; light floor 30 percent"],
    ["Lightning", "Every 20 to 30 minutes, 1 to 3 strokes, 3 to 12 km away"],
    ["Thunder", "Delayed by distance at 343 m/s"],
    ["Day", "48 minutes, red moon at night"],
])}
<div class="fig-2">
{fig(I+"sky_clear.jpg", "The manor under the ash sky with the sun showing", "Sun clear: ground brightness 17.")}
{fig(I+"sky_covered.jpg", "The manor with a heavy cell over the sun", "Sun covered: ground brightness 7, never black.")}
</div>
<div class="fig-2">
{fig(I+"sky_lightning.jpg", "Lightning inside the ash", "Lightning lights the inside of the ash.")}
{fig(I+"sky_moon.jpg", "Night under the red moon", "Night under the red moon.")}
</div>
<div class="note"><b>Two crashes.</b> The editor crashed in the cloud shadow pass because the cloud material was not flagged for volumetric cloud use. Setting that flag fixed it. A second crash at startup came from a cloud layer saved with an unfinished shader, so the layer is now created at run time, only after its shaders are ready.</div>
{fig(G+"devlog23_hall_firelight_1015.jpg", "The hall lit by firelight", "Inside, firelight: the hall has 12 lights sharing one flicker pattern.")}
""")

body += section("streaming", "Streaming and performance", f"""
<p>Every map is a World Partition level. Content is split into grids that load at different distances, so the player only holds what is near.</p>
{table(["Grid", "Cell size", "Loading range"], [
    ["Terrain", "512 m", "6 km"], ["Trees", "256 m", "700 m"], ["Buildings", "256 m", "600 m"], ["Detail", "128 m", "300 m"], ["Ground cover", "256 m", "200 m"],
])}
<ul>
<li>Distant trees switch to a hierarchical level of detail with impostor cards.</li>
<li>Grass and small clutter fade at 50 to 80 m; shrubs at 150 to 300 m.</li>
<li>First standalone measurement at the hub's north gate: about <b>6.7 ms per frame</b> (about 150 fps) with about 570,000 plant and prop instances in range, before the five-million-plant pass.</li>
<li>The ten new maps hold about 8.8 GB of streamed actor files between them.</li>
</ul>
""")

body += section("lessons", "Lessons", table(["#", "Mistake", "Fix"], [
    ["1", "Bought foliage that did not fit the period", "Build every plant for the game; keep only fully textured packs"],
    ["2", "Trees placed with collision on landed on other trees", "Place with collision off, switch it on after"],
    ["3", "A re-run left the first ground-cover pass behind", "World Partition only deletes loaded actors: load the folder first"],
    ["4", "Grass kept spawning old meshes", "Recompile and save the terrain material, then flush the grass cache"],
    ["5", "Console commands during a level load crashed the editor", "Never run them from Python while a map is loading"],
    ["6", "Summits 4 to 14 m low", "The tree-stripping filter trims narrow tops; restore pass planned"],
]))

body += section("next", "What's next", """
<ul>
<li>Autumn colours for the older oak, ash and alder canopies.</li>
<li>Summit restore on the ten new maps and a far-view build for each.</li>
<li>Replace the placeholder blocks with finished buildings and scene sets (see the <a href="../roadmap/buildings.html">Buildings checklist</a>).</li>
<li>Playtest each map for crossing time and points of interest.</li>
</ul>
""")

body += section("script", "Episode talking points", script([
    ("Cold open", "Same woodland, four seasons, one switch. Every plant here was built for this game in Blender. Here's how the world came together."),
    ("Real ground", "Satellite elevation, trees stripped off, real rivers cut in. Eleven maps of real Shropshire, each a 2017 pixel heightmap."),
    ("Scale", "Real land is slow to cross. Rule: 10 to 15 minutes at a jog, story places true size, only empty land squeezed, height never squeezed."),
    ("Plans", "Nothing placed by hand. Zones, 1 m rules and Poisson spacing; gray box first, 49,259 placeholders on the hub."),
    ("Water", "One continuous river mesh with the flow baked in. Severn 3 m deep, ford 50 cm."),
    ("Trees", "Bought packs out: 13 GB deleted. Skeleton, cards, Pivot Painter wind, impostors, seasons, 5,000 triangles. Then /newtree for the other 20 species."),
    ("Ground plants", "54 plants, four seasons on one sheet, under 1,000 triangles each."),
    ("Five million", "Test map, 10 biomes, 44 layers, density from noise. Five million plants, then onto the real hub."),
    ("Regions", "99 sets, each map with plants of its own. 60 million plus across all maps."),
    ("Seasons", "One call. Grass height, colour groups, the sun's day. The floating trees bug."),
    ("Sky", "The brief in four lines. Two cloud layers, sun cover, lightning, red moon. Two crashes and their fixes."),
    ("Performance", "World Partition grids, draw distances, 6.7 ms at the gate."),
    ("Wrap", "Six lessons, the RoadMap page, next episode."),
], "Show the talking points"))

body += section("related", "Related", """
<ul>
<li><a href="../roadmap.html">RoadMap</a>: <a href="../roadmap/regions.html">Region maps</a>, <a href="../roadmap/trees.html">Trees</a>, <a href="../roadmap/shrubs-and-climbers.html">Shrubs and climbers</a>, <a href="../roadmap/ground-plants.html">Ground plants</a>, <a href="../roadmap/world-effects.html">Sky and seasons</a></li>
<li><a href="../post.html?p=2026-10-15-firelight-earthworks-and-the-first-trees">Dev Log #23: Firelight, earthworks and the first trees</a></li>
<li><a href="../post.html?p=2026-10-18-an-ash-sky-horses-and-life-on-the-road">Dev Log #26: An ash sky, horses and life on the road</a></li>
<li><a href="../post.html?p=2026-10-20-five-million-plants-crop-strips-and-kitchen-gardens">Dev Log #27: Five million plants</a></li>
<li><a href="../post.html?p=2026-10-23-every-region-gets-its-own-plants-and-the-seasons-turn">Dev Log #30: Every region gets its own plants</a></li>
</ul>
""")

EP = {
    "n": 4, "slug": "episode-4-world-plants-and-sky", "yt": None,
    "title": "World, Plants and Sky", "short": "World, Plants and Sky", "yt_title": "AI Game Development - World, Plants and Sky Ep4",
    "lede": "How the world of KnightZ was built: real elevation data, rules for map scale, 99 hand-built plant sets with four seasons, more than 60 million plants placed by script, and a volcanic ash sky.",
    "card": "Real terrain, trees and plants built in Blender, one season switch for every leaf, and a custom ash sky. The full breakdown is live; the video follows.",
    "meta_desc": "Episode 4 breakdown: building the KnightZ world with AI. Real elevation data to Unreal landscapes, map scale rules, placement plans, flowing rivers, trees and 54 ground plants built in Blender with four seasons, 60 million plants, a season switch and a C++ volcanic ash sky.",
    "ld_desc": "Episode 4 of the AI Game Development series covers the environment pipeline of KnightZ.",
    "seconds": 0, "upload": "2026-10-23T12:00:00-05:00", "date_h": "Video coming soon",
    "thumb_rel": "assets/img/videos/ep4_title.jpg", "thumb_abs": "https://chimeradrops.github.io/knightz-site/assets/img/videos/ep4_title.jpg",
    "soon": "Recording early next week. The full breakdown is below.",
    "tags": ["Environment", "Foliage", "Terrain", "Unreal Engine 5", "Blender"],
    "pills": ["Video coming soon", "Breakdown published Oct 23, 2026", "13 segments", "11 maps", "99 plant sets"],
    "facts": [("Status", "Video in production"), ("Maps", "11 from real elevation"), ("Plant sets", "99"), ("Ground plants", "54, four seasons each"), ("Tree species", "21"), ("Plants placed", "60 M+")],
    "toc": [("overview", "Overview"), ("plan", "Episode plan"), ("software", "Software and tools"), ("real-ground", "Real ground"), ("scale", "Map scale"), ("plans", "Plans and biomes"), ("water", "Water"), ("trees", "Trees"), ("shrubs", "Shrubs and climbers"), ("plants", "54 ground plants"), ("five-million", "Five million plants"), ("regions-plants", "Plants per region"), ("seasons", "Season switch"), ("sky", "Ash sky"), ("streaming", "Streaming"), ("lessons", "Lessons"), ("next", "What's next"), ("script", "Talking points"), ("related", "Related")],
    "chapters": [],
    "body": body,
}
