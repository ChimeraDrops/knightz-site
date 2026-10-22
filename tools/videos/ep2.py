from h import fig, prompt, table, stats, script, section, step

I = "../assets/img/videos/ep2/"
body = ""

body += section("overview", "Overview", f"""
<p class="lead">The first pipeline made good-looking heads. Put twenty of them in one level and the editor slowed to a crawl. This episode is the audit that found out why, and the rebuild that cut every hero roughly in half without changing a face.</p>
<p>Part 1 measures what was wrong: triangle counts, missing levels of detail, hair cards stacked up to ten deep, and the small flaws that only show up close. Part 2 is the fix: a low-poly pass that kept all 52 facial shapes, six hair rules the tools now check on their own, a ten-step review per hero, and a final hair and clothing system built for a crowd.</p>
{stats([("1.9M", "triangles for 20 characters before"), ("105,670 &rarr; 47,344", "Wulfstan, full character"), ("36,492 &rarr; 7,030", "Wulfstan hair and beard"), ("15", "outfits from one garment kit")])}
""")

body += section("chapters", "Chapters", "<p>Click a chapter to jump the player to that point.</p>\n{CHAPTERS}")

body += section("studio", "The studio: hardware", f"""
<p>Every step in the series runs on one desktop. The game itself targets a standard gaming PC, so all budgets in this episode are set for that standard PC.</p>
{table(["Part", "Spec"], [
    ["GPU", "NVIDIA RTX 5090, 32 GB VRAM"],
    ["CPU", "Intel Core Ultra 9 285K, 24 cores"],
    ["Memory", "64 GB DDR5-6000"],
    ["Motherboard", "Gigabyte Z890"],
    ["System drive", "2 TB WD Black NVMe"],
    ["Project drive", "Samsung T9 portable SSD, so the project moves between machines"],
])}
{fig(I+"specs.jpg", "Machine specs slide", "The build machine. The audit numbers below were also checked against a laptop, where the slowdown was first noticed.")}
""")

body += section("software", "Software and tools", table(
    ["Tool", "Used for"],
    [
        ["Blender 5.2", "Modelling, rigging, hair, textures, low-poly reduction, garment building"],
        ["Unreal Engine 5.8", "The game: import, materials, levels of detail, in-level review"],
        ["Claude", "Drives Blender and Unreal through MCP, writes and runs every batch script, keeps the records"],
        ["Blender MCP and Unreal MCP", "Connections that let Claude run Python inside the open Blender and Unreal editors"],
        ["KZ Python toolset (Unreal)", "Our own editor plugin: run_python, run_python_file, project info, git from the editor"],
        ["Trellis.2", "Image-to-3D heads"],
        ["Meshy", "Source meshes for the base bodies"],
        ["AI image generators", "Portraits, four-view sheets and hair references"],
        ["MakeHuman", "Animation-ready face topology"],
        ["Python (numpy, scipy, trimesh)", "Cloud batch work: audits, shell builder, hair rules, texture fixes"],
        ["Git with LFS", "Every automated batch is committed before and after it runs"],
        ["Kawaii Physics", "Cloak and cape simulation in Unreal"],
        ["OBS and Filmora", "Recording and editing the episodes"],
    ]) + fig(I+"software.jpg", "Software list slide", "Software used so far in the series."))

body += section("part1", "Part 1: what we found", f"""
{step("01", "Where we started", "step-1")}
<p>The first pipeline: a four-view reference per character, an AI image-to-3D head, a MakeHuman topology wrap so the face could animate, and hair grown as cards from the reference sheet. Every character shared one standard body. Episode 1 shows this pipeline on Cynan.</p>
<p>It worked. Sixteen heads were built and nine were in Unreal, and up close they looked right. The trouble started with several of them in a level together.</p>
{fig(I+"first_pipeline.jpg", "The first character pipeline", "The original pipeline, before the audit.")}
{fig(I+"sixteen_heads.jpg", "Sixteen heads, nine in Unreal", "Sixteen heads built, nine standing in Unreal.")}

{step("02", "The audit", "step-2")}
<p>The editor slowed down with only a few characters loaded, so everything was counted: every mesh, every texture, every material slot, measured from the export files. The yardstick was <strong>Epic's MetaHuman level-of-detail specification</strong>, since it is the published budget for realistic characters in Unreal.</p>
{table(["Item", "Ours (full detail)", "MetaHuman budget", "Result"], [
    ["Body", "17,422 verts / 34,778 tris, 4 bone influences", "30,500 verts, 8 influences", "Pass"],
    ["Head", "about 13,100 verts / 26,000 tris, 52 morphs", "24,000 verts", "Pass"],
    ["Eyes, teeth, gums, tongue, lashes", "8,400 tris", "part of head", "Pass, but wasteful at distance"],
    ["Hair cards", "9,800 to 26,000 tris", "about 10,000 verts", "1.5 to 3 times over"],
    ["Beards", "1,000 to 26,700 tris", "500 to 10,000 verts", "Three characters over"],
    ["Levels of detail (LODs)", "none", "8 head, 4 body, 8 hair", "Missing"],
    ["Textures per unique head", "about 43 MB at 4096 px", "up to 8192 on high-end PC", "Heavy for 20 characters"],
])}
<p>Per character: 84,000 triangles (Tudwal, the lightest) to 105,670 (Wulfstan, the heaviest), 93,000 on average. Twenty on screen: about <strong>1.9 million triangles</strong> and 120 to 140 draw calls before shadows, plus 0.7 to 1.0 GB of unique textures. The faces, rigs and skin weights all passed. The cost was in hair, missing LODs and textures.</p>
{fig(I+"audit_chart.jpg", "Audit chart of triangles per character", "Triangles per character at full detail. Orange and green are head, hair and beard.")}
{fig(I+"audit_numbers.jpg", "What 20 characters cost", "What twenty characters cost on screen.")}

{step("03", "The cost of hair", "step-3")}
<p>Wulfstan's approved hair and beard alone were <strong>36,492 triangles</strong>. Hair cards are see-through layers, and ours stacked seven to ten deep over every point of the scalp. Every layer is drawn for colour, for depth and again for shadow, so the cost multiplies. This is called overdraw, and it made hair the most expensive thing on screen.</p>
{fig(I+"hair_cost.jpg", "Why hair cards are expensive", "Layered cards: each layer is drawn several times per frame.")}

{step("04", "Close-up flaws", "step-4")}
<p>Looking closely turned up a second list:</p>
<ul>
<li>A seam at the wrist where the hand texture met the arm, like a bracelet.</li>
<li>Hair sitting over the ears instead of around them.</li>
<li>Hair edges floating above the skin.</li>
<li>Caps that looked like helmets: straight slopes and no natural volume.</li>
<li>Gaps between the hair and the back of the neck.</li>
<li>Beards covering the mouth opening by up to 2.3 cm.</li>
</ul>
{fig(I+"flaws.jpg", "Wrist seam and hair over the ears", "Two of the close-up flaws: the wrist band and hair over the ear.")}
""")

body += section("part2", "Part 2: how we rebuilt it", f"""
{step("05", "Lighter characters", "step-5")}
<p>The goal: the same faces, with all 52 facial shapes intact, at about half the triangles.</p>
<p><strong>The hair test came first.</strong> On Wulfstan, the approved cards (36,492 triangles) were compared with a single textured <strong>shell</strong> that follows the scalp, at about 4,000. That is about 89 % less, and from normal game distance it holds up. The owner compared three versions (shell with cards, shell with a bottom fringe, shell only) and picked shell only as the new plan at that stage.</p>
{fig(I+"shell_test.jpg", "Hair cards compared with a single shell", "Approved cards (left) against a single textured shell (right).")}
<p><strong>Then the low-poly pass on the whole character:</strong></p>
<ul>
<li><strong>Head:</strong> a morph-preserving reduction that keeps all 52 ARKit keys. Heads settled around 17,700 triangles.</li>
<li><strong>Mouth parts:</strong> dental arches of 280 triangles each, tongue 150, eyes 736 each, lashes 272.</li>
<li><strong>Body:</strong> reduced with joint weighting, so elbows, knees and shoulders keep their density. Standard body 34,778 to 22,952.</li>
<li><strong>Hair and beard:</strong> textured shells, about 2,300 and 1,700 triangles.</li>
</ul>
{table(["Character", "Head", "Hair", "Beard", "Total with body"], [
    ["Bedwyr", "17,714", "2,316", "1,700", "47,136"],
    ["Cynan", "17,698", "2,308", "none", "45,412"],
    ["Owain", "17,674", "2,324", "none", "45,402"],
    ["Brother Tysilio", "17,738", "2,397", "1,706", "47,247"],
    ["Tudwal", "17,698", "2,429", "608", "46,141"],
    ["Einion (large body)", "17,938", "2,375", "1,708", "47,427"],
    ["Iddon (large body)", "17,938", "2,320", "1,699", "47,363"],
], num_cols=(1, 2, 3, 4))}
<p>Every head export was checked: 7 meshes, 134 bones, 52 keys, at most 4 influences per vertex and 0 unweighted vertices. Wulfstan went from 105,670 to 47,344. A typical hero went from about 93,000 to about 45,000.</p>
{fig(I+"budget_chart.jpg", "Low-poly budget chart", "Before and after the low-poly pass.")}
{fig(I+"lp_compare.jpg", "Original and low-poly faces for Owain and Cynan", "The check that mattered: original (left) and low-poly (right) for Owain and Cynan. Same likeness.")}
<p><strong>Background characters</strong> were cut harder, to 66 %: peasants, Neanderthals and the undead. An importance map protects the face (head, jaw, lips and brows weighted at 0.6) while the rest collapses. The full mesh is kept hidden in the file so any character can be reverted.</p>
{fig(I+"npc_sheet.jpg", "Background characters after reduction", "Background character sets after the 66 % reduction.")}

{step("06", "Hair rules", "step-6")}
<p>Every flaw from Part 1 became a written rule with a measurement, and the tools check each rule automatically on every cap.</p>
{table(["#", "Rule", "Measurement"], [
    ["1", "Hairline hugs the ear and never covers it", "0 to 3 mm from the ear outline"],
    ["2", "Top and front edges sit on the scalp", "pinned 0.8 mm above the skin"],
    ["3", "Volume follows the skull with natural variation", "no straight slopes"],
    ["4", "The back closes cleanly at the nape", "no gap to the neck"],
    ["5", "Long hair rests on the body", "ends 1.8 mm above shoulders and back"],
    ["6", "Beard mouth opening follows the lip", "cut on the real lip line"],
])}
{fig(I+"hair_rules.jpg", "Six rules for every hair cap", "The six rules, each tied to a measurement.")}
<p><strong>Overnight batch.</strong> With the rules written down, one night run traced the outline of each character's old hair cards and built 15 new caps with the rules applied, for the standard and the large body. Interior vertices were lifted at least 1.5 mm (hair) or 2.5 mm (beard) above the skin. Every cap came with a review sheet in eight views: front, left, back, right, both ears, three-quarter and three-quarter back.</p>
{fig(I+"caps_night.jpg", "Fifteen hair caps built overnight", "Night run output: 15 caps, standard body and large body.")}
<p><strong>Iteration.</strong> The batch was a starting point. Bedwyr's cap went from the overnight version 1 to an approved version 24, and Cynan's was approved at about 1,200 triangles. Every version kept its own number, so any of them could be restored.</p>
{fig(I+"caps_iter.jpg", "Bedwyr hair cap version 1 and version 24", "Bedwyr: overnight version 1 (top) and approved version 24 (bottom).")}

{step("07", "Review pass", "step-7")}
<p>Ten steps per hero, one hero at a time, and nothing is exported until it passes.</p>
<ol>
<li>Head check in Blender</li>
<li>Hair cap check</li>
<li>Beard check</li>
<li>Mouth and eyes check</li>
<li>Body joints check</li>
<li>Blender sign-off</li>
<li>FBX export</li>
<li>Unreal import</li>
<li>In-level check: a walk, a face check and a back view</li>
<li>Approval</li>
</ol>
<p>Characters go into the test level one at a time and come out after review. Owain was the first to pass.</p>
{fig(I+"checklist.jpg", "Ten-step review checklist", "The per-hero review checklist.")}
<p><strong>The wrist fix</strong> came out of this pass. The hand and forearm textures had a tone step, a ring of strong tilt in the normal map, and a roughness step at the join. The fix rebuilt the textures only: base colour and roughness crossfade over about 11 cm of the forearm, and the low-frequency tilt in the normal map was removed around the seam. The mesh did not change.</p>
{fig(I+"wrist_fix.jpg", "Wrist seam before and after", "Wrist join before and after the texture crossfade.")}
{fig(I+"ue_review.jpg", "In-level review in Unreal", "Every hero gets a walk, a face check and a back view in Unreal before approval.")}

{step("08", "Final hair and clothes", "step-8")}
<p><strong>Hair version 7: shell plus strand cards.</strong> The shell-only hair saved the most, but lost detail at the hairline and edges up close. The final hair is a hybrid: the shell covers the head, and a small number of strand cards sit only where they show (hairline, edges, beard). Each character gets a procedural 2048 px strand atlas with clumps, waves, frizz and curl.</p>
{fig(I+"hair_v7.jpg", "Approved cards, shell only and final hybrid", "Top: approved cards. Middle: shell only. Bottom: shell plus strand cards.")}
{table(["Wulfstan hair and beard", "Triangles"], [
    ["Approved cards (start)", "36,492"],
    ["Shell only", "3,754"],
    ["Shell plus strand cards (final)", "7,030"],
], num_cols=(1,))}
<p>That is about a fifth of the starting cost, with the close-up detail kept. Across the cast, the final hair runs from about 4,000 to 9,000 triangles per character.</p>
<p><strong>Levels of detail.</strong> Every skeletal mesh now has four LODs at 100, 50, 25 and 10 % of the triangles, switching at screen sizes of about 1.0, 0.5, 0.25 and 0.1. Facial shapes are kept on the first two LODs only; mouth parts and lashes drop from LOD 2. Strand cards are used at full detail only, and further away the character drops to the shell.</p>
{fig(I+"hair_lod.jpg", "Hair cost per level of detail", "Hair cost at each level of detail for every hero, on a log scale.")}
<p><strong>One garment kit.</strong> Instead of modelling clothes per character, one kit was built for the whole cast. Each piece is shaped from the body surface itself: body faces in the region are copied, pushed out along the normals by a fixed clearance, smoothed and cut at the hems. Then each piece is recoloured per character with a material tint.</p>
{table(["Garment", "Triangles (standard body)", "Offset from skin"], [
    ["Under-tunic", "9,375", "1.2 cm"],
    ["Tunic", "9,063", "2.1 cm"],
    ["Padded tunic", "8,863", "3.2 cm"],
    ["Trousers", "5,395", "0.5 to 1.5 cm"],
    ["Drawers", "2,711", "0.3 to 0.55 cm"],
    ["Leg wraps", "2,158", "1.05 cm"],
    ["Turnshoes", "2,496", "0.9 cm"],
    ["Belt", "692", "on the tunic"],
    ["Cloak", "3,452", "body plus clothing, +2 cm"],
], num_cols=(1,))}
{fig(I+"garment_kit.jpg", "The shared garment kit", "One garment kit, shaped from the body surface.")}
{fig(I+"outfits.jpg", "Fifteen characters in casual and work outfits", "The kit dressed fifteen characters, with a casual and a work outfit each.")}
<p><strong>Cloaks</strong> hang on five bone chains and run on Kawaii Physics in Unreal (damping 0.2, stiffness 0.08, gravity -350, angle limit 45 degrees, collision from the body physics asset). <strong>Hidden skin</strong> under clothing is masked out so the engine does not draw what nobody can see.</p>
{fig(I+"cloaks_hidden.jpg", "Cloaks and hidden body layers", "Cloak simulation and the body regions hidden under clothes.")}
""")

body += section("prompts", "Prompts and instructions used", f"""
<p>These are the instructions behind the overnight cap rebuild and the review loop, condensed from the session records.</p>
{prompt("Night run rules (given before leaving)", "1. No review or approval needed until finished.\n2. Apply the hairline-around-ears rule and the natural-volume rule to every character.\n3. Use the trace method: trace the volume of the original approved hair cards so the cap matches their outline.\n4. Cap edges that meet the skull or face bend down and touch, or almost touch, the head. No floating edges. The bottom and back get more transparent toward the tips so they look organic and broken up.\n5. No spikes on moustaches. Trace the cards for moustaches and beards too.", "<b>Why it works:</b> every rule is something you can check on the mesh, and the owner answered the planning questions before leaving.")}
{prompt("Answers to Claude's planning questions", "Scope: the 15 heroes after Owain. No background characters.\nWulfstan: fix only where he breaks the rules.\nBlender only. No FBX export and no Unreal. I review first.\nKeep the old meshes hidden in the file for comparison.\nTriangle budget stays close to the current one.\nEars: cover an ear only where the original cards covered it. Never put hair on the ear surface.", "<b>Result:</b> 15 caps and review sheets waiting in the morning. Nothing stalled, because every decision was made before the run started.")}
{prompt("Review loop (one hero at a time)", "For each hero:\n1. Open the right file. Show only body, head, eyes, lashes and the new hair.\n2. Show me the review sheet plus the known issue for that hero.\n3. Wait for my call: Approve, Edit, or Revert.\n4. On Approve: tick the checklist, add a dated note, save, open the next hero.\n5. On Edit: change the new hair object only, re-render as a new version, show it, wait again.\n\nRules:\n- Do not export FBX or touch Unreal until all 15 are approved, unless I say so.")}
""")

body += section("lessons", "What we took from it", """
<ol>
<li><strong>Measure before you polish.</strong> The audit found what looking could not.</li>
<li><strong>Give every part a budget.</strong> Body, head, hair and beard each get a number.</li>
<li><strong>Turn every mistake into a rule,</strong> and let the tools check the rule.</li>
<li><strong>Review one character at a time,</strong> and export nothing that has not passed.</li>
<li><strong>Keep the old version until the new one is approved.</strong> Every master was backed up and every original mesh kept hidden in the file.</li>
</ol>
""" + fig(I + "lessons.jpg", "Lessons slide", "Five lessons from the rebuild."))

body += section("try", "Try it yourself: checklist", """
<ul class="checklist">
<li>Pick a published budget (MetaHuman LOD spec works for Unreal) and measure every mesh against it.</li>
<li>Count hair layers as well as triangles. Overdraw is the hidden cost.</li>
<li>Reduce heads with a method that preserves shape keys, then check likeness side by side.</li>
<li>Give background characters a harder cut with the face protected.</li>
<li>Build LODs for every skeletal mesh; keep morphs on the first two only.</li>
<li>Write each flaw as a rule with a number, and check it in code.</li>
<li>Run batches unattended only after every decision is written down.</li>
<li>Shape clothes from the body surface and recolour them per character.</li>
</ul>
""")

body += section("script", "Episode narration", script([
    ("Intro", "Welcome back to KnightZ. In Episode 2 we look at the first way we built our characters, what went wrong once we put them all in the game, and how we rebuilt the process to make the cast you see today."),
    ("The audit", "Each character came in at about 93,000 triangles at full detail, and full detail was the only level we had. We measured against Epic's MetaHuman budgets. Twenty characters on screen came to 1.9 million triangles before shadows. Our hair was one and a half to three times over the card budget. There were no levels of detail. And each head carried about 43 megabytes of unique 4K textures."),
    ("Hair cost", "Wulfstan's approved hair and beard alone were 36,492 triangles. Hair cards are see-through layers, and ours stacked seven to ten deep. Every layer gets drawn for colour, for depth and for shadow, so the cost multiplies."),
    ("Close-up flaws", "The wrist had a visible seam like a bracelet. Hair sat over the ears. Hair edges floated above the skin. Some caps looked like helmets. There were gaps at the back of the neck. Some beards covered the mouth by up to 2.3 centimetres."),
    ("Lighter characters", "We started with one test on Wulfstan: approved cards at 36,492 triangles against a single textured shell at about 4,000. Then the low-poly pass. Wulfstan went from 105,670 to 47,344. A typical hero went from about 93,000 to about 45,000. Background characters were cut harder, to 66 percent."),
    ("Hair rules", "Every mistake became a rule, and the tools check each rule automatically. With the rules written down, an overnight batch built fifteen new caps. Bedwyr went from his first overnight cap to version 24, the one we approved."),
    ("Review pass", "Ten steps per hero, one hero at a time. Five checks in Blender, a Blender sign-off, FBX export, Unreal import, an in-level check, and approval. The wrist seam was fixed here: three textures crossfade over 11 centimetres of the forearm, and the mesh did not change."),
    ("Final hair and clothes", "The final hair is a hybrid: a shell plus strand cards only where they show. Wulfstan: approved cards 36,492, shell only 3,754, shell plus cards 7,030. One garment kit dressed fifteen characters. Cloaks run on Kawaii Physics, and covered skin is masked out."),
    ("Lessons", "Measure before you polish. Give every part a budget. Turn every mistake into a rule. Review one character at a time. Keep the old version until the new one is approved."),
], "Show the narration (condensed)"))

body += section("related", "Related dev log posts", """
<ul>
<li><a href="../post.html?p=2026-10-08-lighter-characters-same-faces">Dev Log #14: Lighter characters, same faces</a></li>
<li><a href="../post.html?p=2026-10-08-hands-ears-and-the-review-pass">Dev Log #15: Hands, ears, and the review pass</a></li>
<li><a href="../post.html?p=2026-10-09-hair-caps-under-review">Dev Log #16: Hair caps under review</a></li>
<li><a href="../post.html?p=2026-10-09-outfits-cloaks-and-textured-hair-for-the-whole-cast">Dev Log #17: Outfits, cloaks and textured hair for the whole cast</a></li>
<li><a href="../post.html?p=2026-10-10-combat-prototype-real-terrain-and-hair-lods">Dev Log #18: Combat prototype, real terrain and hair level of detail</a></li>
</ul>
""")

EP = {
    "n": 2, "slug": "episode-2-optimizing-characters", "yt": "PECacarqLfk",
    "title": "Optimizing Characters", "short": "Optimizing Characters", "yt_title": "AI Game Development - Optimizing Characters Ep2",
    "lede": "What the first AI character pipeline got wrong, what we changed, and the cast it produced: an audit, a low-poly rebuild, hair rules and one shared garment kit.",
    "card": "An audit found 1.9 million triangles for 20 characters. The rebuild halved every hero, kept every face, and added hair rules, a review pass and one garment kit.",
    "meta_desc": "Episode 2 breakdown: auditing AI-built game characters against MetaHuman budgets, cutting heroes from 105K to 47K triangles with all 52 facial shapes, six automated hair rules, a ten-step review pass, LODs, hybrid hair and a shared garment kit in Unreal Engine 5.",
    "ld_desc": "Episode 2 of the AI Game Development series. What the first character pipeline got wrong, what changed, and the cast it produced. An audit of 20 characters on screen found 1.9 million triangles, no LODs and hair cards stacked 7 to 10 deep. The rebuild halved character triangle counts, added six automated hair rules, a ten-step review pass per hero, and shell plus strand-card hair with one shared garment kit.",
    "seconds": 1147, "upload": "2026-10-12T12:00:00-05:00", "date_h": "October 12, 2026",
    "thumb_rel": "https://i.ytimg.com/vi/PECacarqLfk/maxresdefault.jpg", "thumb_abs": "https://i.ytimg.com/vi/PECacarqLfk/maxresdefault.jpg",
    "tags": ["Optimization", "Unreal Engine 5", "Hair cards", "LODs", "AI pipeline"],
    "pills": ["19 min", "Published Oct 12, 2026", "15 chapters", "Unreal Engine 5.8", "Blender 5.2", "MetaHuman budgets"],
    "facts": [("Length", "19:07"), ("Published", "Oct 12, 2026"), ("Characters audited", "16 heroes"), ("Before", "~93K tris each"), ("After", "~45K tris each"), ("Facial shapes kept", "52 of 52"), ("Hair rules", "6"), ("Review steps", "10 per hero")],
    "toc": [("overview", "Overview"), ("chapters", "Chapters"), ("studio", "Hardware"), ("software", "Software and tools"), ("part1", "Part 1: what we found"), ("part2", "Part 2: the rebuild"), ("prompts", "Prompts used"), ("lessons", "Lessons"), ("try", "Try it yourself"), ("script", "Narration"), ("related", "Related posts")],
    "chapters": [(0, "Intro"), (6, "The studio: one desktop does everything"), (48, "Software and tools"), (128, "Part 1 overview: what we found"), (162, "Part 2 overview: how we rebuilt it"), (168, "Step 1: Where we started"), (228, "Step 2: The audit"), (318, "Step 3: Hair cost"), (353, "Step 4: Close-up flaws"), (427, "Step 5: Lighter characters"), (540, "Step 6: Hair rules"), (691, "Step 7: Review pass"), (839, "Step 8: Final hair and clothes"), (1029, "Lessons learned"), (1088, "Next episode")],
    "body": body,
}
