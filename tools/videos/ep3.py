from h import fig, prompt, table, stats, script, section, step

I = "../assets/img/videos/ep3/"
I2 = "../assets/img/videos/ep2/"
body = ""

body += section("overview", "Overview", f"""
<p class="lead">Bedwyr's hair took 24 versions. The prompt that finally landed was one screenshot with two coloured circles and four plain sentences: what I saw, where I saw it, what it should look like, and why.</p>
<p>Episode 3 goes back through three weeks of KnightZ sessions and pulls out the prompts that made the biggest difference. In that time Claude helped build 16 hero characters with face rigs, imported them all into Unreal, generated hundreds of animation clips, and wrote a screenplay, a combat design and an economy. This page lists the actual prompts, what each one did, why it worked, the four that cost time, and two templates you can copy.</p>
{stats([("24", "versions of Bedwyr's hair"), ("15", "characters reviewed in one loop"), ("4", "parts of a session-start prompt"), ("200+", "project docs used as memory")])}
""")

body += section("chapters", "Chapters", "<p>Click a chapter to jump the player to that point.</p>\n{CHAPTERS}")

body += section("software", "Software and tools", table(
    ["Tool", "Role in this episode"],
    [
        ["Claude (desktop app)", "Every session, prompt and review in the episode"],
        ["Claude project docs", "Shared memory between sessions: character records, rules, scripts, next-session prompts"],
        ["Claude skills", "/newhead, /newfathead, /newhair, rigging and Weight Pose Adjust: one line replaces a page of instructions"],
        ["Blender 5.2 with Blender MCP", "Hair caps, skin, rig rebuild"],
        ["Unreal Engine 5.8 with Unreal MCP", "Character import, animation review tool, root motion edits"],
        ["HY-Motion", "Text-to-motion model that generated the animation clips (four takes per prompt)"],
        ["Git with LFS", "Every edit committed from inside the Unreal editor"],
        ["Filmora", "Episode edit"],
    ]))

body += section("bedwyr", "The prompt that fixed Bedwyr's hair", f"""
<p>Version 1 of Bedwyr's hair cap came out of an overnight batch. Versions 2 to 23 came from text feedback. Version 24 was approved after this prompt and one marked-up screenshot.</p>
<div class="fig-2">
{fig(I+"bedwyr_markup.jpg", "Bedwyr hair cap with blue and red circles", "The screenshot: blue for skull showing through the cap, red for grey streaks running across the hair grain.")}
{fig(I2+"caps_iter.jpg", "Bedwyr hair version 1 and version 24", "Version 1 (top) and the approved version 24 (bottom).")}
</div>
{prompt("Visual feedback prompt (Bedwyr hair)", "I can see the skull mesh through the hair cap where circled in blue.\nYour grey streaks run perpendicular to the hair grain where circled in red.\nThe grey streaks should run the same direction as the hair texture so they look like grey hairs.\nThe idea for the grey streaks is to make his hair more grey; it is too brown for an old man with a grey beard.", "<b>What it did:</b> Claude mapped the circles back onto the 3D mesh, filled the hole, re-aligned the streaks and shifted the overall hair colour.<br><b>Why it worked:</b> location (colour-coded circles), problem, desired result and the reason. The reason fixed a problem the circles never showed: the overall colour was too brown.")}
""")

body += section("session-start", "The session-start prompt: four parts", f"""
<p>Every new AI session starts with no memory of yesterday. The first prompt has to carry the context. The best session starts all had the same four parts:</p>
{table(["#", "Part", "What to include"], [
    ["1", "Where the work lives", "Engine and version, project path, file and object names. Claude stops guessing which file you mean."],
    ["2", "What to read first", "The project docs that hold the history. Naming three docs replaces pages of explaining."],
    ["3", "Numbered tasks", "One fix per item, in order, each with the exact change wanted."],
    ["4", "The finish line", "Save, commit, update the checklist. Without it you get a different idea of done every time."],
])}
{prompt("Session start (animation review, Oct 12)", "We are reviewing and editing the HY-Motion animation clips in Unreal\n(KnightZ, UE 5.8.3, project D:/__KSUIE_Gaming/KnightZ_3D/KnightZ_3D).\nRead these project docs first: SESSION_NOTES_20261012_anim_review.md,\nANIM_POSE_RULES_20261012.md, UE_ANIM_REVIEW_tool_20261012.md.\n\n1. Apply the 4 \"Needs edit\" notes on Guard_Walk:\n   - FL: trim the opening where he walks forward-right; start where he walks forward-left.\n   - R: trim the opening half step left; start where he steps right.\n   - L: keep the animation, scale root motion so the feet stop sliding.\n   - BR: he moves back-left. Tell me the options before changing it.\n   Edit clips in place, keep root motion, check shield clearance, save, commit to git.\n   I think we generated four options for each animation on our first pass,\n   so check whether one of the others is correct.\n\nKeep responses brief and factual. No em dashes.", "<b>What it did:</b> a brand new session fixed all four clips and committed them in three commits with no re-explaining.<br><b>Why it worked:</b> exact path and engine version, docs to read, one numbered fix per clip, safety rules (edit in place, keep root motion), a gate on the one risky item, and a hunch.")}
<div class="note"><b>Share your hunch.</b> The line \"I think we generated four options for each animation\" sent Claude to the alternate takes, where it found the real cause: the motion generator ranks its four takes by how far they travel, never by direction, so wrong-way steps pass. Future runs now check path direction too.</div>
<p>The finished clips can be seen in <a href="../post.html?p=2026-10-12-from-motion-library-to-fighting-stance">Dev Log #20</a>.</p>
""")

body += section("visual", "Feedback on visual work", f"""
<p>Game development is visual. The AI can measure a mesh, but it cannot see what bothers you unless you say it.</p>
<h3>Name a reference and the symptoms</h3>
<p>The first look at Owain in Unreal got the feedback \"he looks deformed\". That gave Claude nothing to measure, so it came back with questions. The second try named a reference and four symptoms:</p>
{prompt("Owain in Unreal (Oct 7)", "Compare this to our blender model. He is deformed. At idle he should be\nstanding up straight and look like our blender model that was approved.\nHis bones look like they have been repositioned so his chest is stretched,\nhis back is crooked, he is leaning forward and his toes go into the ground.", "<b>What it did:</b> Claude measured all four symptoms and traced them to bone axes off by 76 to 104 degrees from Unreal's Manny skeleton. It rebuilt the rig with Manny's bone frames. Idle lean went from 16.3 cm to 10.2 cm (Manny: 9.5 cm).<br><b>Why it worked:</b> \"deformed\" alone gives nothing to test. \"Leaning forward, toes in the ground, compared to the approved model\" gives a target and a measurement.")}
{fig(I+"posture_vs_manny.jpg", "Body on the rebuilt rig next to Manny", "Posture check after the rig rebuild: our body on the new rig (left) next to Manny (right).")}
<h3>Mark it up</h3>
<p>Take a screenshot and circle the problems, one colour per problem. Then add the reason (see the Bedwyr prompt above).</p>
<h3>Plain words work</h3>
<p>You do not need the technical term. A clear description of the look and the direction of change is enough.</p>
{prompt("Bedwyr skin (Oct 8)", "His skin looks like dry leather, reduce the depth of the texture a bit\nto make it look more natural and less dry and tanned rhino hidish.", "<b>What it did:</b> became a standing rule for every head in the game: if skin reads like dry leather, use a softer copy of its normal map.")}
<div class="note"><b>Formula for visual feedback:</b> where, what is wrong, what it should look like, and why.</div>
""")

body += section("limits", "Limits, gates and fixed replies", f"""
<p>An AI that can run Blender and Unreal can also break them. Four habits keep that in check:</p>
{table(["Habit", "Example from KnightZ", "Effect"], [
    ["Hard limits", "\"Do not export FBX or touch Unreal until all 15 are approved.\"", "One line protects the whole downstream pipeline"],
    ["Non-negotiables", "\"We definitely want face bones.\"", "All 45 face, skirt and cloak bones survived the skeleton rebuild"],
    ["Gates", "\"Tell me the options before changing it.\"", "Claude laid out three choices for the back-left walk; one was picked and nothing was lost"],
    ["Fixed reply words", "Approve, Edit or Revert", "Fifteen characters became a repeatable loop"],
])}
{prompt("Review loop (hair caps, Oct 8)", "For each hero:\n1. Open the right blend. Show only body, head, eyes, lashes and the new hair.\n2. Show me the review sheet plus the known issue for that hero.\n3. Wait for my call: Approve, Edit, or Revert.\n4. On Approve: tick the checklist, add a dated note, save, open the next hero.\n5. On Edit: change the new hair object only, re-render as a new version, show it, wait again.\n\nRules:\n- Do not export FBX or touch UE until all 15 are approved, unless I say so.", "<b>Why it worked:</b> a fixed order, a fixed set of replies, what to do after each reply, versioned outputs, and a hard stop line.")}
{fig(I2+"checklist.jpg", "Per-hero review checklist", "The per-hero checklist the Approve / Edit / Revert loop filled in.")}
{prompt("Skeleton rebuild: check the record, name what must survive (Oct 7)", "Please review our notes because I'm pretty sure you suggested a different skeleton than Manny. Review the notes while I pose the session working in blender... figure out why we didn't use a manny skeleton to begin with. But we definitely want face bones so figure that out also.", "<b>What it did:</b> Claude found two earlier skeletons in the notes, showed that the old rule \"never import onto Manny's skeleton\" had no recorded reason, and built a Manny-conformed rig that kept every face, skirt and cloak bone.")}
""")

body += section("night-run", "The night run: decide first, then one word", f"""
<p>For the overnight hair cap rebuild, Claude asked its planning questions first: which characters, Blender only or Unreal too, keep the old meshes, triangle budget, how to handle ears. The answers went into a project doc so an interrupted session could resume. Then:</p>
{prompt("The whole prompt", "Go")}
<p>Next morning: 15 new hair caps, each with a review sheet and a known-issues list. Every decision had been made before leaving, so nothing stalled overnight.</p>
{fig(I2+"caps_night.jpg", "Fifteen hair caps from the night run", "Night run output: 15 caps for the standard and large bodies.")}
""")

body += section("mistakes", "Four mistakes I made so you don't have to", f"""
{table(["Mistake", "What was missing", "Cost", "Fix now in use"], [
    ["Sent a big character build from my phone", "Blender was connected through the desktop app; the phone session could not reach it", "Session stalled until reopened on the desktop", "Start tool-heavy sessions from the computer that runs the tools"],
    ["A rule with no reason: \"never import onto Manny's skeleton\"", "Nobody wrote down why", "A whole session working out the history", "Every rule lives in a doc with the reason and the measurement"],
    ["Described a hair underside shape in words", "A clear picture of the target shape", "Generated version rejected", "Asked for a flat plane, sculpted it by hand, had Claude measure the sculpt and turn it into a rule"],
    ["Vague opener: \"review the project files and you'll get an idea for the economy\"", "A specific question", "A general summary before the real answer", "Ask the direct question first"],
])}
{fig(I+"cynan_underside_n13_n14.jpg", "Cynan hair cap version 13 and version 14", "Cynan's hair underside: generated version 13, rejected (top), and version 14 from the hand-sculpted plane (bottom).")}
{prompt("The direct question that worked", "We have production of stone, but how are we consuming it?\nHave we worked out that logic and that structure?")}
<div class="note"><b>The pattern:</b> when you can show it (sculpt, circle, screenshot), show it. When you can name the reference, name it. When a rule exists, write down why.</div>
{fig(I2+"hair_rules.jpg", "Rules written from corrections", "Rules written from corrections, each with its measurement.")}
""")

body += section("loop", "Every session writes the next prompt", f"""
<p>The prompts got shorter over time, and better. At the end of every session Claude saves what was learned to the project: character records, scripts and rule docs (over 200 so far). Then it writes the prompt for the next session, ready to paste. The animation prompt above was written that way.</p>
<ol>
<li><strong>Session prompt</strong>: where, what to read, numbered tasks, finish line.</li>
<li><strong>Claude does the work</strong> and renders review images.</li>
<li><strong>You review</strong>: Approve, Edit or Revert.</li>
<li><strong>Lessons saved</strong>: rules with reasons and measurements.</li>
<li><strong>Next prompt written</strong> into a NEXT_SESSION doc.</li>
<li><strong>Repeated procedures become skills.</strong></li>
</ol>
<p>When a procedure repeats, it becomes a skill. The question that started it:</p>
{prompt("Asking for judgement", "Is it possible to build a subagent that does all of these hair edits we are working on?\nDo you know how to do that? Would it make sense to do that?", "<b>What it did:</b> Claude recommended a skill instead of the subagent named in the question, with reasons. Asking whether something makes sense got a better answer than the tool first named.")}
<p>Now a new hairstyle or head starts with one line:</p>
{prompt("Skill call", "/newhair Wulfstan")}
<p>Skills in use: <code>/newhead</code>, <code>/newfathead</code>, <code>/newhair</code>, <code>knightz-rig-model</code> and Weight Pose Adjust. Episode 1 shows <code>/newhead</code> and <code>/newhair</code> step by step.</p>
""")

body += section("templates", "Templates you can copy", f"""
{prompt("Session-start template", "We are [task] in [tool + version], project [path].\nRead these docs first: [doc 1], [doc 2], [doc 3].\nUse [connector / tool] for [what].\n\nTasks, in order:\n1. [Item]: [exact change wanted].\n2. [Item]: [exact change wanted].\n3. [Risky item]: tell me the options before changing it.\n\nRules:\n- Do not [hard limit] until I say so.\n- Keep [thing that must survive].\n- Back up / version every change.\n\nFinish: save, commit, update [checklist / notes], write the next-session prompt.\nHunch: [anything you suspect, even if unsure].\nKeep responses brief and factual.")}
{prompt("Visual feedback template", "[Attach screenshot with circles, one colour per problem.]\nBlue: [what is wrong there].\nRed: [what is wrong there].\nIt should look like [reference: approved model, reference image, real-world comparison].\nThe reason: [why you want it].")}
<h3>Checklist before you send</h3>
<ul class="checklist">
<li>Did I name the files, paths and versions?</li>
<li>Did I point to the docs that hold the history?</li>
<li>Is each fix its own numbered item?</li>
<li>Did I say what must not happen?</li>
<li>Did I gate the risky step behind \"show me options\"?</li>
<li>For visual issues: did I give a reference and a reason?</li>
<li>Did I say what \"done\" means (save, commit, notes)?</li>
</ul>
""")

body += section("rules", "Ten rules for effective prompts", table(
    ["#", "Rule", "KnightZ example"],
    [
        ["1", "Say where the work lives", "\"UE 5.8.3, project [path]\""],
        ["2", "Point to the memory", "\"Read these project docs first\""],
        ["3", "Number the tasks", "FL / R / L / BR, each with its own instruction"],
        ["4", "State the finish line", "Save, commit, update the checklist"],
        ["5", "Set hard limits", "\"Do not export FBX until all 15 are approved\""],
        ["6", "Gate the risky step", "\"BR: tell me the options before changing it\""],
        ["7", "Describe symptoms against a reference", "\"Leaning forward, toes in the ground, compared to the approved model\""],
        ["8", "Give the reason", "\"Too brown for an old man with a grey beard\""],
        ["9", "Mark it up", "Blue for skull showing, red for streak direction"],
        ["10", "Fix the reply format", "Approve / Edit / Revert; \"brief, factual, no em dashes\""],
    ]))

body += section("script", "Episode talking points", script([
    ("Cold open", "This is Bedwyr's hair. Version 1, built overnight by Claude. Version 24, approved. The fix that finally landed came from one plain-language prompt: what I saw, where I saw it, and why it mattered."),
    ("Session start", "Every new AI session starts with no memory of yesterday. My best session starts had four parts: where the work lives, what to read first, numbered tasks with one fix per item, and the finish line. Bonus: share your hunch."),
    ("Visual feedback", "The AI can measure a mesh, but it can't see what bothers you unless you tell it. Name a reference and the symptoms. Mark it up with one colour per problem. Add the reason. Plain words work."),
    ("Limits and gates", "Hard limits protect the downstream pipeline. Non-negotiables protect what must survive. Gates stop risky changes until you pick an option. Fixed reply words turn review into a loop. Then the night run: answer the planning questions, save them to a doc, and type one word."),
    ("Mistakes", "Wrong device. A rule with no reason. Describing a shape in words instead of showing it. A vague opener instead of a direct question."),
    ("The loop", "At the end of every session Claude saves what we learned and writes the next prompt. When a procedure repeats, it becomes a skill."),
    ("Template", "Where it lives, what to read, numbered tasks, hard limits, a gate on the risky step, the finish line, and your hunch. For visual feedback: where, what's wrong, what it should look like, and why."),
], "Show the talking points"))

body += section("related", "Related", """
<ul>
<li><a href="episode-1-character-pipeline.html">Episode 1: Character Pipeline</a> (the /newhead and /newhair skills)</li>
<li><a href="episode-2-optimizing-characters.html">Episode 2: Optimizing Characters</a> (the night run and review loop in context)</li>
<li><a href="../post.html?p=2026-10-11-a-motion-library-written-in-plain-english">Dev Log #19: A motion library written in plain English</a></li>
<li><a href="../post.html?p=2026-10-12-from-motion-library-to-fighting-stance">Dev Log #20: From motion library to fighting stance</a></li>
</ul>
""")

EP = {
    "n": 3, "slug": "episode-3-vibe-coding-prompts", "yt": "Bp-HNgwDLhE",
    "title": "Vibe Coding Prompts", "short": "Vibe Coding Prompts", "yt_title": "AI Game Development - Vibe Coding Prompts Ep3",
    "lede": "How I write prompts that get game-ready results from AI: session-start prompts, marked-up screenshots, limits and gates, four mistakes, and a loop where every session writes the next prompt.",
    "card": "Bedwyr's hair took 24 prompt iterations. The real prompts behind KnightZ, what each did, four mistakes, and two templates to copy.",
    "meta_desc": "Episode 3 breakdown: the real prompts used to build KnightZ with Claude in Blender and Unreal Engine. Session-start prompts, marked-up visual feedback, hard limits, gates, fixed replies, night runs, four costly mistakes and copyable templates.",
    "ld_desc": "Episode 3 of the AI Game Development series. How prompts are written to get game-ready results from AI. Bedwyr's hair took 24 prompt iterations; the one that worked was an annotated screenshot and one sentence. The episode covers a session-start prompt with context, tasks and a finish line, annotated screenshots for animation fixes, hard limits, gates and fixed reply words that let 15 characters run through review overnight, four mistakes and their fixes, and a loop where every session writes the next prompt.",
    "seconds": 1089, "upload": "2026-10-14T22:01:07-07:00", "date_h": "October 15, 2026",
    "thumb_rel": "https://i.ytimg.com/vi/Bp-HNgwDLhE/maxresdefault.jpg", "thumb_abs": "https://i.ytimg.com/vi/Bp-HNgwDLhE/maxresdefault.jpg",
    "tags": ["Prompting", "AI pipeline", "Claude", "Unreal Engine 5", "Blender"],
    "pills": ["18 min", "Published Oct 15, 2026", "10 chapters", "10 real prompts", "2 templates"],
    "facts": [("Length", "18:09"), ("Published", "Oct 15, 2026"), ("Prompts shown", "10"), ("Templates", "2"), ("Sessions studied", "3 weeks"), ("Docs as memory", "200+")],
    "toc": [("overview", "Overview"), ("chapters", "Chapters"), ("software", "Software and tools"), ("bedwyr", "Bedwyr's hair prompt"), ("session-start", "Session-start prompt"), ("visual", "Visual feedback"), ("limits", "Limits and gates"), ("night-run", "The night run"), ("mistakes", "Four mistakes"), ("loop", "The loop and skills"), ("templates", "Templates"), ("rules", "Ten rules"), ("script", "Talking points"), ("related", "Related")],
    "chapters": [(0, "Intro"), (14, "What this episode covers"), (27, "Bedwyr's hair: 24 prompt iterations"), (117, "The session-start prompt"), (193, "Visual feedback: annotated screenshots for animation fixes"), (314, "Say what must not happen: limits, gates and fixed replies"), (460, "The review loop and the night run"), (528, "Four mistakes I made so you don't have to"), (767, "Every session writes the next prompt"), (1004, "Wrap-up")],
    "body": body,
}
