# Integrating the field manual

Working tracker for `research/ai-gm-field-manual.md`. Each row is a claim or
technique from that document and what we did with it.

Status vocabulary:

- **encoded** — it's in `CLAUDE.md`; the "where" column says which section.
- **scaffolded** — it exists as a file, template, or script rather than as a
  prompt clause.
- **pending** — agreed in principle, not yet built.
- **rejected** — deliberately not doing it; the "where" column says why. A
  rejection is a decision and is worth as much as an adoption.

Sections named below are in `CLAUDE.md` unless the row says `rules/…`, which
means a path-scoped rule that loads when the GM opens a matching file. Stance 6
explains which goes where.

Nothing gets silently dropped. If a row leaves this table it's because it moved
to "encoded" and the text it became is findable.

Where a row says "stance", the reasoning is in `stances.md`, not here.

## The anti-sycophancy spine (manual: Stage 1, §d, §g)

| Claim | Status | Where / why |
|---|---|---|
| Over-compliance is the dominant AI-GM failure mode; weight the prompt toward it | encoded | §Adjudication → The failure mode. Section is front-loaded and opens by naming the drift, per the manual's note that buried rules get lost |
| Resolve mechanics before narrating outcome | encoded | §Roll before you narrate |
| Fixed machine-readable output block each turn | rejected | Stance 5. Requirement kept, format replaced by the visible `roll.py` call — a block is written by the same pass that chose the outcome and can be back-filled; a tool call can't |
| Forbid auto-success; failure must be possible and consequential | encoded | §Only roll when it matters; §Failure, by domain |
| Adjudicate against game state regardless of how well the player argues | encoded | §A good argument is not a success. The manual's dominant attack vector, so it gets its own heading |
| Don't confirm player theories or hand over clue interpretations | encoded | §Mysteries → Then stop. Includes the tell — warming to a right guess, going quiet on a wrong one |
| Redirect in-world (information / consequence / NPC), never bare denial | encoded | §Never a bare "no" |
| "Yes, but / no, and" over unconditional "yes, and" | encoded | §And never an unconditional "yes" |

## Prep and planning (manual: §a, §j, Stage 5)

| Claim | Status | Where / why |
|---|---|---|
| Prep situations, not plots | encoded | §Planning, and `rules/prep.md`. Sharpened by stance 1 into prep-the-world / play-the-plot, with a no-placeholders rule |
| Goal-oriented opponents with a timeline of what they do unopposed | encoded | `rules/prep.md` — what each party wants, does this week unopposed, and would never do |
| Rebuild prep when play contradicts it, rather than drifting | encoded | §Planning trigger; craft in `rules/prep.md`. Stance 1 — where we depart from the improv camp |
| Lazy DM eight-step prep checklist | rejected | As a checklist it's system-specific (steps 7–8 assume D&D-likes). The transferable steps are encoded separately: secrets and clues, NPC goals, locations |
| ~10 reusable secrets and clues as improvisation fuel | encoded | `rules/prep.md`; `notes/gm/CLUES.md` → Loose clues |
| Carry unrevealed secrets forward between sessions | encoded | `rules/prep.md`; CLUES.md status vocabulary distinguishes undelivered from spent |
| Advance offscreen clocks between sessions | encoded | §The world and the people in it; clocks table in `notes/gm/STATE.md` |
| Prep is stickier than conversation; the plan bends to play | encoded | §When the plan breaks — predates the manual, agrees with it |
| "Play to find out what happens" (PbtA) | encoded | §Planning — adopted for the plot, rejected for the world. Stance 1 |
| Czege Principle — don't author both problem and solution | encoded | §The oracle, and stance 1's split: the world is authored, the plot is not |
| Strong start — open on a problem or a choice | pending | |

## Mysteries and information (manual: §h, Stage 2)

| Claim | Status | Where / why |
|---|---|---|
| Three Clue Rule — three clues per conclusion | encoded | §Mysteries and `rules/prep.md`; enforced by the revelation table in `notes/gm/CLUES.md` |
| GUMSHOE: never gate a *core* clue behind a roll | encoded | §Mysteries; CLUES.md marks each clue core or not |
| Node-based scenario design with a revelation list | scaffolded | `notes/gm/CLUES.md` |
| Track who knows / believes / lies about what | scaffolded | CLUES.md table, a per-person block in `notes/gm/characters/TEMPLATE.md`, and `rules/prep.md` |
| Facts are not clues; leave inference to the player | encoded | §Mysteries → Then stop |
| Move information toward those who can act on it | encoded | §Getting information to them |
| Inverted Three Clue Rule — any three clues yield a conclusion | pending | Currently implicit in the graph structure; not stated as a design instruction |

## Scene craft and pacing (manual: §c, §e)

| Claim | Status | Where / why |
|---|---|---|
| Cut to the interesting part; frame late, leave early | encoded | §Scenes |
| Frame the expected scene, then check whether it holds | encoded | §Scenes; `oracle.py scene` |
| Address the character, not the player | encoded | §Scenes |
| Describe to the senses | encoded | §Scenes |
| Don't resolve stakes too fast | encoded | §Scenes |
| Clocks as a pacing and consequence device | scaffolded | `notes/gm/STATE.md` clocks table; referenced from §Scenes and §Adjudication |
| End sessions on a hook or unresolved beat | encoded | §Scenes |
| Hope/fear beat oscillation (Laws) | pending | Wants a tracking mechanism to be more than a slogan |
| Infer and adapt to the player's evident preferences (Laws' player types) | partly encoded | Session zero step 3 asks outright what they want to be *doing* — tone, appetite for combat, kind of play — and step 2's personality probe reads what the player enjoys deciding rather than what they said about the character. Both land in `CAMPAIGN.md`. Inferring *during* play, and adapting to it, is still pending |
| Reading the room / body language / physical staging | rejected | Doesn't transfer; the manual flags this itself. Substitute is the explicit check-ins in §Safety |

## Adjudication (manual: §d)

| Claim | Status | Where / why |
|---|---|---|
| Roll only when the outcome is uncertain and both branches are interesting | encoded | §Only roll when it matters |
| State stakes and consequences before the roll | encoded | §Say what's at stake first |
| Rulings, not rules; then apply the ruling consistently | encoded | §Rulings, not rules; rulings table in `notes/gm/STATE.md` so consistency survives the session boundary |
| Fail forward — failure changes the situation rather than stalling it | encoded | §Failure, by domain. Stance 3 — applies to investigation and social play only |
| Telegraph danger before it can kill | encoded | §Failure, by domain |
| Let a clever plan work; don't buff opposition to save a planned fight | encoded | §Let them win when they've won |
| Advance a clock rather than forcing a choice under analysis paralysis | encoded | §When the player stalls |
| Devil's Bargains | pending | Needs a system-agnostic form — the bonus-die currency it trades in doesn't exist in every system |
| Position and effect stated before the roll (BitD) | pending | Stakes-before-roll is encoded; the finer position/effect grading isn't, and may not port cleanly |

## NPCs and the world (manual: §f)

| Claim | Status | Where / why |
|---|---|---|
| Name everyone; everyone wants something | encoded | §The world and the people in it; INTENTION in `notes/gm/characters/TEMPLATE.md` |
| Think offscreen; factions pursue goals unobserved | encoded | §The world and the people in it |
| NPCs are competent but must not solve the player's problems | encoded | §The world and the people in it — framed as the same sycophancy in a costume, since that's how it gets back in after the dice are guarded |
| Nobody explains the whole situation as they see it | encoded | §The world and the people in it; §Tone — predates the manual |
| Distinct, consistent NPC voices | encoded | `rules/notes.md` (VOICE); `notes/gm/characters/TEMPLATE.md` |

## Continuity (manual: §i, Stage 2)

| Claim | Status | Where / why |
|---|---|---|
| External state is the source of truth, not model memory | encoded | The `notes/` tree is the scaffolding; §Notes now also requires the notes to reach the repository's default branch before the session ends. A file written and never committed is not external state — the next session is a fresh clone |
| Re-anchor canon at session open (the AI's reason to recap differs from a human's) | encoded | §Starting up |
| Just-in-time rule injection rather than parametric recall | scaffolded | Rules skills, per §Starting up |
| Retconning policy decided in advance | pending | Partly served by the recap-reconciliation rules in §Starting up, which resolve player-vs-notes but not notes-vs-notes |

## Solo play and surprise (manual: Stage 4)

| Claim | Status | Where / why |
|---|---|---|
| A single intelligence on both sides collapses into wish-fulfilment (Czege) | encoded | §The oracle |
| An oracle the GM must consult and cannot rationalise away | scaffolded | `scripts/oracle.py ask`; §The oracle forbids re-rolling and reinterpreting |
| Chaos factor tuning how often the unexpected intrudes | scaffolded | `oracle.py --chaos`; stored in `notes/gm/STATE.md` |
| Scene check: expected scene → altered / interrupted | scaffolded | `oracle.py scene` |
| Random events with a focus and a word pair to read | scaffolded | `oracle.py event`; also fires on doubles inside the chaos factor during `ask` |

## Safety (manual: §k)

| Claim | Status | Where / why |
|---|---|---|
| Lines and veils, negotiated before play | encoded | Set in `notes/gm/plans/CAMPAIGN.md`, not negotiated in session — playtest 01 showed the negotiation eating the opening. §Safety says read, don't ask. Where they get *set* moves into session zero, which is a before-play conversation and the right home for it |
| X-card as an always-available explicit command | partly rejected | §Safety keeps "obey an out-of-character stop without negotiating". The rewind half is dropped: the client's rollback removes turns outright, which beats a GM un-narrating, so the prompt was shipping a worse copy of a feature the player already had (playtest 01) |
| Script change — rewind / pause / fast-forward | rejected | Provided by the client's rollback control, better than the prompt can. The manual's note that an AI "can literally rewind and re-narrate" is true and still the wrong build (playtest 01) |
| Explicit out-of-character check-in channel | encoded | §Safety |

## Architecture (manual: Stage 6)

| Claim | Status | Where / why |
|---|---|---|
| Prefer one strong GM prompt with tool-grounded state | encoded | The design: one `CLAUDE.md`, state in `notes/`, mechanics in scripts |
| LLM committees that critique each other measurably degrade correctness | rejected as a design | No reviewer subagents. The manual's own evidence (rule violations 1.32 → 3.26) argues against them |
| At most one narrow, well-scoped adjudication check | encoded | `roll.py` and `oracle.py` are that check, and they aren't LLMs — so they can't degrade a correct output the way the reviewer agents did |
| Front-load the most-violated rules; buried rules are lost to recency | encoded | §Adjudication sits immediately after startup, before Notes and Planning |
| A versioned system-prompt "contract" | pending | Nothing versions `CLAUDE.md` beyond git history |
| Once-per-campaign setup shouldn't be paid for every session | encoded | `.claude/rules/session-zero.md`, path-scoped to a `notes/gm/plans/SESSION-ZERO.md` that deletes itself at the close. Not from the manual — see `ideas.md` for why a self-deleting trigger file beat a skill, and stance 7 for the appetite/circumstance split it runs on |
| Treat every observed rule-break as a new prompt clause | encoded | `playtests/` and the `log:` command in §Safety; protocol in `docs/playtesting.md` |
