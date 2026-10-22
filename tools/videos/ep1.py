from h import fig, prompt, table, stats, script, section, step

I = "../assets/img/videos/ep1/"

body = ""

body += section("overview", "Overview", f"""
<p class="lead">One reference image goes in. A game-ready head comes out: fitted to the shared body, rebuilt with animation topology, textured at 4K, rigged with 52 facial shapes, and wearing a hairstyle that can be swapped onto any other head.</p>
<p>Episode 1 follows Cynan, captain of the garrison, through the two repeatable skills that build every KnightZ character head: <code>/newhead</code> (8 steps) and <code>/newhair</code> (6 steps). Claude runs the steps in Blender and in a cloud Python workspace. Each step saves a versioned file and a review render, and nothing moves forward until the owner approves it.</p>
<p>This page expands on the video with the numbers, settings, tools and fixes behind each step, so you can follow the same process on your own characters.</p>
{stats([("208,701", "vertices in the raw AI bust"), ("13,014", "quads in the final head"), ("52", "ARKit facial shape keys"), ("10,991", "quads of swappable hair")])}
""")

body += section("chapters", "Chapters", """
<p>Click a chapter to jump the player to that point.</p>
{CHAPTERS}
""")

body += section("software", "Software and tools used", table(
    ["Tool", "Version / type", "What it did in this episode"],
    [
        ["Claude", "Claude desktop app, Opus model", "Ran every pipeline step, wrote and ran the scripts, rendered review sheets, kept the build records"],
        ["Blender", "5.2", "Master scene, QuadriFlow remesh, shape keys, rig, final asset files"],
        ["Blender MCP", "Local MCP server", "Lets Claude drive the open Blender session: run Python, read objects, save files"],
        ["Cloud Python workspace", "Python 3 with numpy, scipy, trimesh, fast_simplification, Pillow", "Heavy geometry work: solidify, ICP fit, seam band, masks, visual hull, hair growth"],
        ["bpy (headless Blender)", "pip wheel 5.2.2", "Cycles and Workbench renders in the cloud for review sheets and the episode frames"],
        ["Trellis.2", "Image-to-3D generator", "Turned the portrait into a textured 3D bust. Pixal3d, stable-fast-3d and Hunyuan3D were also tested on earlier heads"],
        ["AI image generator", "Text-to-image", "Three-quarter portrait, bald four-view head sheet, four-view hair sheet"],
        ["MakeHuman hm08 head", "CC0 template mesh", "Animation-ready edge loops wrapped over the AI shape"],
        ["Apple ARKit naming", "52 blendshape standard", "Shape key names, so phone face capture and Unreal Live Link can drive the face"],
        ["Filmora", "Video editor", "Edited the episode from the 44 rendered frames and narration"],
    ]) + """
<p>Everything runs on one desktop: RTX 5090 (32 GB), Intel Core Ultra 9 285K, 64 GB DDR5. Episode 2 covers the full hardware and software list.</p>
""")

body += section("skills", "Two skills: /newhead and /newhair", f"""
<p>A <strong>skill</strong> is a saved set of instructions Claude loads on demand. Instead of pasting a page of steps into every session, you type one line. Both skills follow the same pattern:</p>
<ol>
<li><strong>Load context first.</strong> Read the playbook, the "Don't" list of rejected attempts, and the script docs from the project, then rebuild the scripts in the cloud workspace.</li>
<li><strong>Ask once, only for what is missing.</strong> Character name, which base body, special notes such as scars or baldness.</li>
<li><strong>Back up before writing.</strong> The master Blender file is copied to a <code>MayNeedLater</code> folder before anything changes.</li>
<li><strong>Version every output.</strong> Each step writes a new file name (<code>_v1</code>, <code>_v2</code>), so any step can be reverted.</li>
<li><strong>Gate on approval.</strong> Renders go to the owner at fixed points. A rejected attempt is reverted and added to the "Don't" list so it never repeats.</li>
<li><strong>Record.</strong> New methods, numbers and failed attempts go back into the project docs, so the next character starts with everything learned so far.</li>
</ol>
{prompt("How a new head starts", '/newhead Cynan\n[attach: 3/4 portrait + bald four-view head sheet]\nNotes: scar across the nose bridge, chipped front tooth, keep the AI face shape. No stubble.', "<b>Why it works:</b> the skill already holds the 8 steps, the rules and the file paths. The prompt only needs what is unique to this character.")}
{prompt("How the hair starts", '/newhair Cynan\n[attach: four-view hair reference]\nStyle: medium shag, dark brown with grey streaks. Hair only, no stubble.')}
""")

body += section("head", "/newhead: building the head, step by step", f"""
{step("01", "Reference", "head-1")}
<p>Two AI-generated images set the character. The <strong>three-quarter portrait</strong> carries the personality and the details to keep: a scar across the nose bridge, pale brown eyes and a chipped upper incisor. The <strong>bald four-view sheet</strong> (front, left, back, right) gives skin tone and proportions from every angle. It is bald on purpose, because hair is built separately.</p>
<div class="fig-2">
{fig(I+"portrait.jpg", "Cynan three-quarter portrait reference", "Three-quarter portrait: scar, eye colour and the chipped tooth come from here.")}
{fig(I+"four_view_bald.jpg", "Cynan bald four-view head reference sheet", "Bald four-view sheet: front, left, back and right for tone and proportion.")}
</div>
<div class="note"><b>What to ask your image tool for:</b> a neutral expression, even studio lighting, the same head in four orthographic-style views at the same scale, shoulders included, and no hair for the head sheet. Consistent views matter more than style.</div>

{step("02", "AI mesh (image-to-3D)", "head-2")}
<p>The portrait runs through image-to-3D. When several generators are available, all candidates are rendered from the front, quarter and side and ranked against the reference. For Cynan, Trellis.2 gave the best likeness: a textured bust of <strong>208,701 vertices</strong> in under a minute.</p>
<p>It looks right but cannot be used as is. The surface is a dense soup of triangles with no edge flow, so it will not deform cleanly, cannot be UV-unwrapped well, and is far over a game budget. AI meshes are also thin double shells about 1 mm thick, which breaks most remesh tools. From here on the AI output is treated as a <strong>shape to match</strong>, never as final geometry.</p>

{step("03", "Seam fit to the shared neck", "head-3")}
<p>All male heroes share one base body, <strong>HM1</strong>. Dropped on that body, the raw bust is the wrong size, angle and position, and its shoulders clash with the body.</p>
<p>The fit runs as a chain of scripts:</p>
<ol>
<li><strong>Solidify.</strong> Voxelize the shell at 0.5 mm, fill each slice below the neck, flood fill from outside, then marching cubes. This turns the thin shell into a closed solid (about 0.0042 m&sup3; for Cynan).</li>
<li><strong>Decimate and remesh.</strong> Reduce to 400k, then 120k triangles, then QuadriFlow into clean quads (about 20,800 for Cynan).</li>
<li><strong>Align.</strong> ICP (iterative closest point) matches the AI skull to the HM1 head above the neck. For Cynan, free rotation tilted the chin up 17 degrees, so the pitch was fixed at -8 degrees and only scale and position were solved.</li>
<li><strong>Widen the neck</strong> so its radius matches HM1, then cut 12 mm above the seam.</li>
<li><strong>Bridge band.</strong> A ring of quads (546 for Cynan) connects the head to the <strong>64-vertex neck ring</strong>, followed by a relax pass that removes folds. Result: 0 flipped faces, seam gap 0.0 mm.</li>
</ol>
{fig(I+"fit_compare.jpg", "Cynan fitted head compared with the HM1 base head", "Fit v2: the base HM1 head (top) and Cynan fitted to the same body (bottom), four views.")}
<p><strong>The 64-vertex ring is the key design choice.</strong> Every head welds to exactly the same ring with zero gap, so any head fits any body built on HM1, and helmets and armour carry across characters.</p>
<div class="note warn"><b>Fix from this build:</b> fit v1 was rejected because the brow, nose, ears and chin sat too far forward and the neck looked angled. The head was scaled to 94 % and shifted so the ear centre lines up with the HM1 ear. Rule added: a face 13 to 19 mm forward of the base ear makes the neck lean forward.</div>

{step("04", "Emote topology, eyes and mouth", "head-4")}
<p>Even clean quads animate poorly without the right edge loops. A <strong>MakeHuman hm08 head template</strong> (CC0) is wrapped over the fitted shape using facial landmarks (eye corners, lids, mouth corners, nose, chin) and a thin-plate-spline warp. The template brings loops that follow the facial muscles. The face area is then subdivided for detail, ending at <strong>13,014 quads</strong>.</p>
<p>The inside of the mouth and eyes is built too: eyeballs with lids rolled over them (6.1 mm lid opening for Cynan), upper and lower teeth, gums, tongue and a mouth bag. Cynan's chipped incisor is cut into the upper teeth with a slanted plane 2.6 mm deep.</p>
{fig(I+"emote_wire.jpg", "Cynan emote topology wireframe sheet", "Emote topology review sheet: clay views, eye loops, mouth loops, cutaway with teeth and tongue, and the teeth close-up.")}

{step("05", "Reference sheet", "head-5")}
<p>Our clay head is rendered in the same four views as the reference. Features are then placed <strong>relative to our own eyes, ears and mouth</strong>. AI references never match our proportions exactly, so the image is never projected straight onto the model.</p>

{step("06", "Skin", "head-6")}
<p>The head is unwrapped first. The face UV island is scaled up 1.6 times so the area people look at gets the most texture detail. The base colour map is 4096 px.</p>
<p>Only <strong>tone, brow shape and eye colour</strong> come from the reference. All fine detail is generated procedurally in 3D and baked into base colour, roughness (ORM) and normal maps: pores, forehead furrows, frown lines, crow's feet, nasolabial creases and the nose scar with a raised centre. Brows are 1,400 painted strokes, dark brown with about 20 % grey. Procedural detail stays sharp at any distance and never carries lighting baked into a photo.</p>
{fig(I+"skin_compare.jpg", "Cynan skin render compared with the reference", "Every skin pass is checked against reference crops. If the render does not match, it is not approved.")}
<div class="note warn"><b>Fix from this build:</b> the first skin pass had an orange iris, solid-looking brows, forehead stripes that were too regular, a faint scar and a collar band at the neck. The band came from copying streaky body texels and from pore detail running into the seam. Fixes: wider tone sampling, pore detail faded out within 4 to 34 mm of the seam, and head plus body rendered as one welded object.</div>

{step("07", "Neck seam", "head-7")}
<p>Where the head meets the shared body there can be a crease or a colour band. Three passes hide it:</p>
<ul>
<li><strong>Shape:</strong> the profile kink at the seam was 18 degrees on average (40 max). Taubin smoothing over 8 rings of vertices, 60 passes, brought it to 2.4 degrees. All 52 shape keys were rebased on the new shape.</li>
<li><strong>Normals:</strong> head seam normals copied from the body (they differed by up to 11 degrees), so lighting is continuous.</li>
<li><strong>Colour:</strong> a 16 mm band above the seam blended into the body tone. Maximum colour difference across the seam: 3.1 out of 255.</li>
</ul>

{step("08", "Face rig", "head-8")}
<p>A jaw bone, two eye bones and the <strong>52 ARKit shape keys</strong>, named exactly to Apple's standard, so the face can be driven by phone face capture or keyed by hand in Unreal. Teeth, lower gums and tongue follow the jaw; the lids partly follow the eye bones. The keys stack into full expressions.</p>
{fig(I+"arkit52.jpg", "All 52 ARKit shape keys on Cynan", "The 52 ARKit shape keys, one tile each.")}
{fig(I+"expressions.jpg", "Cynan combined facial expressions", "Combined expressions built from the keys.")}
<div class="note warn"><b>Bug caught here:</b> in Blender 5.2, a new shape key added from script starts at value 1.0. Every key was on at once, so the saved face showed all 52 summed. All values were reset to 0, and the same fix was applied to earlier heads. The loader scripts now set new keys to 0.</div>
""")

body += section("hair", "/newhair: building the hairstyle, step by step", f"""
<p>Hair is its own skill and its own object, so any style can be moved to any head. It is built as <strong>hair cards</strong>: thin strips with a strand texture and transparency.</p>

{step("01", "Hair reference", "hair-1")}
<p>A four-view hair sheet from the image tool: a medium shag, dark brown with grey streaks. Same four views as the head sheet.</p>
{fig(I+"hair_reference.jpg", "Cynan four-view hair reference", "Four-view hair reference: front, left, back and right.")}

{step("02", "Masks and camera fit", "hair-2")}
<p>Each view is split into background, skin and hair using colour and local texture variance. Hair is fine and noisy; skin is smooth and more saturated. That difference finds the hairline. Only hair regions that reach the top 30 % of the panel are kept, which drops shoulders and stubble.</p>
<p>A <strong>camera fit</strong> then scales and shifts our clay render until its outline matches each reference silhouette. For Cynan all four views agreed on a shared scale of 0.83, with a silhouette error of 0.5 to 2 %. From that point every reference pixel maps to a point on our head.</p>

{step("03", "Visual hull", "hair-3")}
<p>With four matched silhouettes, the volume all four views agree on is carved out. Subtract the head and what remains is where hair lives and how thick it is at each point on the scalp. A minimum thickness of 8 mm stops thin spots at the back from going bald.</p>

{step("04", "Strand atlas", "hair-4")}
<p>Most of the look comes from one 2048 px texture: <strong>8 columns</strong> of fine, clumped strands, 90 to 120 strands per column, painted procedurally with colours sampled from the reference hair, including the grey streaks. Roots are darkened over the first 45 % of each strand.</p>
{fig(I+"strand_atlas.jpg", "Procedural strand atlas detail", "Detail of the strand atlas: clumped, wavy strands with alpha.")}

{step("05", "Hair cards", "hair-5")}
<p>Roots are scattered over the scalp with Poisson spacing (9.5 mm), in four layers at different heights. Each strand grows along a <strong>flow field</strong>: swept back, pulled down by gravity, a fringe across the forehead (45 % of the front roots) with a ragged stop line, and stop rules around the ears. Strands end at heights set per angle around the head. Cynan's hair is <strong>10,991 quads</strong> (21,982 triangles), inside the budget for short hair at the time.</p>
<div class="note"><b>Ear rule from the reference:</b> hair touches the ear over the top and back (2 to 3 mm), sits 4 mm behind the lobe, and never covers the ear below or in front of the lobe.</div>

{step("06", "Final check against the reference", "hair-6")}
<p>The atlas goes on the cards and the hair is rendered through the same four cameras, side by side with the reference. That comparison is the approval gate.</p>
{fig(I+"hair_compare.jpg", "Final hair compared with the reference in four views", "Reference (top) and our hair (bottom), plus top and three-quarter views.")}
<div class="note warn"><b>Fixes during the hair build:</b> a bald stripe over the top (surface sampling returned only 33.5k of 60k points; switched sampler), a bald back crown (hull too thin; dilated hull for the exit test), a visible part gap (hard split replaced by a smooth outward term), and a fringe that looked like a bowl cut (only 45 % of front roots forward, ragged stop).</div>
""")

body += section("gates", "Approval gates and versioned files", table(
    ["Gate", "What the owner sees", "Possible answers"],
    [
        ["After the seam fit", "Front, side and back renders on the body", "Approve, or list what is off (for Cynan: too far forward, scale down)"],
        ["After emote topology", "Wireframe sheet: face, eye loops, mouth loops, cutaway", "Approve or edit"],
        ["After skin", "Cycles close-ups beside reference crops", "Approve or list fixes"],
        ["After hair", "Four views plus ear close-ups beside the reference", "Approve, edit, or revert to the last version"],
        ["After the face rig", "Expression contact sheet", "Approve"],
    ]) + """
<p>Every step writes a new file name (for example <code>Cynan_fit_v1</code>, then <code>Cynan_fit_v2</code>), and the master scene is backed up before each write. A rejected step is reverted from its file, and the attempt is written to the "Don't" list in the playbook.</p>
""")

body += section("prompts", "Prompts and feedback used", f"""
<p>The skills carry most of the instructions, so the prompts in this build were short. These are the inputs that moved Cynan forward, condensed from the session records.</p>
{prompt("Fit feedback that produced fit v2", "The brow, nose, ears, chin and Adam's apple sit too far forward. Scale the head down. The neck angle looks wrong.", "<b>Result:</b> head scaled to 94 % and aligned by the ear position. Approved as fit v2, and a new rule was saved about ear position.")}
{prompt("Touch-up request", "Smooth the neck seam.", "<b>Result:</b> kink 18 to 2.4 degrees, seam normals matched, colour band blended. It also exposed the shape-key-at-1.0 bug.")}
{prompt("Rig request", "Rig head and hair.", "<b>Result:</b> face rig checked, hair weighted to the head bone. A 20 degree head turn moves the hair with the scalp (69 mm at the top).")}
{prompt("Body binding", "Full body pass.", "<b>Result:</b> head bound to the HM1 body rig with 4 influences, seam vertices copying body weights exactly. Pose test: seam gap 0 mm.")}
""")

body += section("lessons", "What we learned", """
<ul>
<li><strong>AI gives the shape; you build the structure.</strong> Image-to-3D gives a likeness in a minute. Topology, UVs, rig and seams still have to be built.</li>
<li><strong>One shared seam makes everything modular.</strong> The 64-vertex ring is why heads, hair, helmets and bodies can be mixed.</li>
<li><strong>Measure against your own model.</strong> Place features relative to your head, never by projecting the reference image.</li>
<li><strong>Procedural detail beats sampled detail.</strong> Take tone and colour from the reference; generate pores, lines and scars in 3D.</li>
<li><strong>Every fix becomes a rule.</strong> The ear-position rule, the seam fade distances and the shape-key reset all came from Cynan and now apply to every head.</li>
</ul>
""")

body += section("try", "Try it yourself: checklist", """
<ul class="checklist">
<li>Pick one shared base body and lock its neck ring vertex count before building heads.</li>
<li>Generate a portrait and a bald four-view sheet with consistent views and lighting.</li>
<li>Run two or more image-to-3D tools and rank them against the portrait.</li>
<li>Solidify the AI shell before remeshing; thin shells break remesh tools.</li>
<li>Fit with scale and position first; fix the pitch if free rotation tilts the head.</li>
<li>Wrap a template head (MakeHuman CC0) for animation loops.</li>
<li>Bake procedural detail into colour, roughness and normal maps at 4K.</li>
<li>Name shape keys to the ARKit standard if you want phone capture.</li>
<li>Version every file and keep a written list of attempts that failed.</li>
</ul>
""")

body += section("glossary", "Glossary", table(
    ["Term", "Meaning"],
    [
        ["Image-to-3D", "An AI model that turns a picture into a textured 3D mesh"],
        ["Topology", "How the polygons of a mesh are laid out; good topology follows muscles so faces deform cleanly"],
        ["ICP", "Iterative closest point: an algorithm that aligns one shape to another by repeated matching"],
        ["QuadriFlow", "A remesher built into Blender that converts triangles into evenly sized quads"],
        ["UV island", "A flattened piece of the mesh that a texture is painted onto"],
        ["ORM map", "One texture holding ambient occlusion, roughness and metalness in its three channels"],
        ["Shape key / morph", "A stored version of the mesh, blended in to make an expression"],
        ["ARKit 52", "Apple's standard set of 52 facial shapes used by phone face capture"],
        ["Visual hull", "The 3D volume consistent with several 2D silhouettes"],
        ["Hair card", "A flat strip with a strand texture and transparency, the standard way to draw game hair"],
    ]))

body += section("script", "Episode narration", script([
    ("Intro", "Welcome to KSUIE_Gaming. We are building KnightZ, a 3D action adventure game, and this channel follows the AI pipeline we use to make it. In this first episode we take one character, Cynan, captain of the garrison, from a single reference image to a game-ready head with skin, hair and a face rig."),
    ("Overview", "The work is split into two repeatable skills. Newhead builds the head. The first four steps take us from a reference image to an AI mesh, fit it to our base body, and rebuild it with topology that can animate. The next four steps finish the head: a reference sheet to line up features, the skin textures, the neck seam blend, and the face rig. Newhair builds a swappable hairstyle on top: the hair sheet, masks and camera fit, the visual hull, the strand atlas, then the hair cards and a check against the reference. Every step ends with a saved, versioned file and a review render, and nothing moves forward until I approve it."),
    ("Reference", "Everything starts with a reference. For Cynan I generated a three-quarter portrait and a bald four-view sheet: front, both sides and back. The portrait carries the details we want to keep: the scar across the nose bridge, pale brown eyes and a chipped front tooth."),
    ("AI mesh", "The portrait goes through image-to-3D. I run several generators and rank them against the reference; for Cynan, Trellis.2 gave the best likeness. In under a minute we have a textured bust with 208,701 vertices. Up close it is a dense soup of triangles with no edge flow."),
    ("Seam fit", "Our characters share one base body, HM1. We solidify the AI shell, remesh it into clean quads, and fit it to the base head with a scale and position solve. The key is a ring of 64 vertices around the neck. Every head welds to exactly the same ring with a gap of zero."),
    ("Emote topology", "We wrap a MakeHuman head template over the shape. It brings proper edge loops, then the face area is subdivided for detail. This head lands at 13,014 quads. Inside, we build eyeballs with lids, teeth, gums, a tongue and a mouth bag. Cynan's chipped incisor is modeled into the upper teeth."),
    ("Reference sheet and skin", "We render our own clay head in the same four views as the reference and place features relative to our own eyes, ears and mouth. The face island is scaled up 1.6 times and the base colour map is 4K. Tone, brow shape and eye colour come from the reference. Pores, wrinkles, crow's feet and the nose scar are generated procedurally in 3D and baked into colour, roughness and normal maps."),
    ("Neck seam and face rig", "We smooth the shape across the seam, match the normals, and blend the head colour into the body tone so the join disappears. Then a jaw bone, two eye bones and the 52 ARKit facial shape keys, named to Apple's standard."),
    ("Hair", "Each view is split into background, skin and hair. A camera fit matches our head outline to the reference silhouette. With four matched silhouettes we carve the visual hull. The strand atlas holds eight columns of clumped strands. Roots are scattered over the scalp and each strand follows a flow field. Cynan's hair is 10,991 quads."),
    ("Outro", "This is Cynan: AI mesh, fitted to our body, animation topology, procedural skin, a 52-key face rig and swappable hair. Because every head shares the same neck seam, this body can wear any of them."),
], "Show the narration (condensed)"))

body += section("related", "Related dev log posts", """
<ul>
<li><a href="../post.html?p=2026-10-05-opening-cinematic-and-the-armoury">Dev Log #10: The opening cinematic, two more heads, and the full armoury</a></li>
<li><a href="../post.html?p=2026-10-06-cynan-complete-einion-goch">Dev Log #11: Cynan complete, Einion Goch's head, and shared rules for every head</a></li>
<li><a href="../post.html?p=sir-bedwyr">Dev Log #8: Sir Bedwyr</a></li>
</ul>
""")

EP = {
    "n": 1, "slug": "episode-1-character-pipeline", "yt": "KGuS8q2UXDE",
    "title": "Character Pipeline", "short": "Character Pipeline", "yt_title": "AI Game Development - Character Pipeline Ep1",
    "lede": "From one reference image to a rigged, textured head with swappable hair: the full /newhead and /newhair pipeline on Cynan.",
    "card": "One reference image becomes a rigged, textured head with hair: an 8-step head pipeline and a 6-step hair pipeline on Cynan.",
    "meta_desc": "Episode 1 breakdown: how one reference image becomes a game-ready KnightZ head with AI image-to-3D, a shared 64-vertex neck seam, MakeHuman topology, 4K procedural skin, 52 ARKit shape keys and swappable hair cards.",
    "ld_desc": "Episode 1 of the AI Game Development series. One reference image becomes a rigged, textured head with hair for Cynan, a KnightZ character. An eight-step head pipeline covers the AI mesh, seam fit to a shared 64-vertex neck, emote topology, 4K skin and a face rig with 52 ARKit keys. A six-step hair pipeline builds hair cards from a four-view reference using masks, a visual hull and a strand atlas.",
    "seconds": 711, "upload": "2026-10-05T12:00:00-05:00", "date_h": "October 5, 2026",
    "thumb_rel": "https://i.ytimg.com/vi/KGuS8q2UXDE/maxresdefault.jpg", "thumb_abs": "https://i.ytimg.com/vi/KGuS8q2UXDE/maxresdefault.jpg",
    "tags": ["AI pipeline", "Character heads", "Hair cards", "Face rig", "Blender"],
    "pills": ["12 min", "Published Oct 5, 2026", "17 chapters", "Blender 5.2", "Trellis.2", "Claude + Blender MCP"],
    "facts": [("Length", "11:51"), ("Published", "Oct 5, 2026"), ("Character", "Cynan"), ("Head steps", "8"), ("Hair steps", "6"), ("Final head", "13,014 quads"), ("Hair", "10,991 quads"), ("Face keys", "52 ARKit")],
    "toc": [("overview", "Overview"), ("chapters", "Chapters"), ("software", "Software and tools"), ("skills", "The two skills"), ("head", "/newhead steps 1 to 8"), ("hair", "/newhair steps 1 to 6"), ("gates", "Approval gates"), ("prompts", "Prompts used"), ("lessons", "What we learned"), ("try", "Try it yourself"), ("glossary", "Glossary"), ("script", "Narration"), ("related", "Related posts")],
    "chapters": [(0, "Intro: Cynan, from one image to a game-ready head"), (84, "Pipeline overview: /newhead and /newhair"), (164, "Head step 1: Reference"), (187, "Head step 2: AI mesh"), (252, "Head step 3: Seam fit to the shared neck"), (340, "Head step 4: Emote topology and teeth"), (404, "Head step 5: Reference sheet"), (424, "Head step 6: Skin"), (462, "Head step 7: Neck seam"), (477, "Head step 8: Face rig"), (495, "Hair step 1: Four-view hair reference"), (510, "Hair step 2: Masks and camera"), (535, "Hair step 3: Visual hull"), (549, "Hair step 4: Strand atlas"), (562, "Hair step 5: Hair cards"), (586, "Hair step 6: Final check against reference"), (599, "Final result")],
    "body": body,
}
