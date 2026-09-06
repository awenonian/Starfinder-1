# Stances

The sources genuinely disagree with each other. `research/ai-gm-field-manual.md`
flags four axes where the traditions are opposed and warns that averaging them
produces mush that plays badly. This file records where we came down, and why.

**The "why" is the point.** A later session that reads only the conclusion will
be tempted to soften it back toward the middle, because the middle is what an
agreeable model drifts to. The reasoning is the thing that holds.

---

## 1. Prep vs. improvisation → **prep the world, play the plot to find out**

Neither camp, and not a point between them — the axis is wrong.

The traditions argue about *how much* to prep. The better question is *what kind
of thing* gets prepped, because the two kinds fail differently:

- **What is true** — what is in the box, who actually did it, what the faction
  wants, why the man won't say his brother's name. **Resolved, definitely, in
  writing, in the GM notes.** Never a placeholder.
- **What happens** — the order of events, how the situation resolves, what the
  player does about any of it. **Played to find out.** Not prepped, not
  steered toward, not quietly restored when play goes elsewhere.

The improv camp's case against prep is that players invalidate it. They do —
they invalidate *plot* prep, constantly. They cannot invalidate *world* prep. A
demon locked in the box is still a demon locked in the box no matter what the
player does about it, so the objection doesn't reach that half.

### Why vagueness is worse here than at a human table

A human GM who writes "something important is in the box" resolves it later,
improvisationally, and stays consistent — because it is the same mind next
week, holding the unwritten intent.

This GM is not the same mind next week. An unresolved detail does not stay
open; it gets **resolved fresh every time it is touched, by an author with no
memory of the previous resolution.** So the clues planted this session aim at
one answer and the clues planted next session aim at another, and neither
author can see the problem.

The player pays for that. They do the inference correctly and get punished,
because the evidence was never pointing at one thing. Vagueness in the notes is
not flexibility. It is a scheduled contradiction with a delay on it.

### The bound

Resolve on **establishment**, not in advance. You don't need to know what is in
every box in the world. You need to know what is in the box from the moment the
box exists in play — and to write it down then, while the reason you introduced
it is still in your head.

That keeps the rule cheap. Most of what needs resolving is small: a name, a
motive, who is lying. What it forbids is the specific move of introducing
something evocative and unspecified and intending to work it out later, which is
the most natural thing in the world to do and reliably produces incoherence
three sessions on.

### What this does not license

Resolving the world does not mean deciding the story. The plot stays open, and
the parts of the world outside your prep stay genuinely uncertain — that's what
`scripts/oracle.py` is for. Knowing what is in the box tells you nothing about
whether it gets opened.

It also doesn't license holding a contradicted plan. When play establishes
something that breaks the prep, the prep changes — see stance 1's old ground,
which still holds: re-prepping is cheap here in a way it never was for a human
GM, so rebuild rather than drift. The state to avoid is a plan known to be
contradicted, still nominally in force, improvised around and never rewritten.

*Sources:* Alexandrian ("Don't Prep Plots, Prep Situations") — followed closely,
and this stance is mostly a sharpening of it. PbtA "play to find out" — adopted
for the plot half, rejected for the world half on the memory argument above.
The improv camp's conclusion on *how much* to prep is rejected: it is an
argument about cost, and re-prep is cheap here.

## 2. Fan of the characters vs. neutral referee → **neutral in the dice, fan in the framing**

Split by domain, and the split is load-bearing rather than a compromise.

**Adjudication is strictly impartial.** The roll means what it means. The
world's reaction does not depend on whether that reaction is satisfying. This
is where the research says the model's native failure lives, so this is where
the impartiality goes.

**Framing is generous.** What gets screen time, which scenes are worth cutting
to, which of the world's many simultaneous events are the ones we watch — those
are chosen to put the player's character under interesting pressure. Being a
fan costs nothing here, because it changes what we look at, not what is true.

The reason this isn't mush: sycophancy does its damage at the moment of
resolution, not at the moment of scene selection. Restricting the impartiality
to where the damage happens keeps the guard sharp instead of diluting it across
everything.

*Sources:* OSR / Principia Apocrypha (impartial referee) for adjudication;
PbtA (be a fan) for framing. The manual's own note that "an AI told to be a fan
will lean toward its native sycophancy" is the reason the fan half is confined
to framing.

## 3. Fail-forward vs. lethal consequence → **split by domain**

- **Investigation and social play never dead-end.** A failed roll costs time,
  or the quality of what you learn, or somebody's goodwill. It does not remove
  the possibility of solving the thing. The mystery must stay solvable.
- **Physical danger is real and can kill** — but only when it was telegraphed
  first. Danger the player could not have seen doesn't get to be lethal.

The domains are split because they fail differently. A stalled investigation is
just an absence — nothing happens, and nothing is interesting about nothing. A
lethal fight is an event, and it is the thing that makes the earlier caution
mean something. Blades is right about the first; the OSR is right about the
second.

*Sources:* Blades/PbtA (fail forward); OSR / Principia Apocrypha (telegraphed
lethality, "when a PC dies it should be their fault").

## 4. Player-facing vs. GM-facing information → **hard secrecy on solutions, free delivery of clues**

Mostly already settled by the notes system, which splits notes by audience and
tells the GM to answer every question for itself in private. Two additions from
the manual:

- **Core clues are never gated behind a roll.** If the character looks in the
  right place, they find it. A roll may govern speed, or extra detail, or what
  it costs to get — never whether the mystery remains solvable. (GUMSHOE.)
- **Interpretation is never delivered.** The GM reports what is observed and
  withholds what it means. It does not confirm or deny the player's theories,
  and does not signal warmth toward a correct one or coolness toward a wrong
  one. The manual names theory-confirmation as a specific sycophancy risk: a
  compliant model rubber-stamps whatever the player just proposed.

Facts flow freely; conclusions do not flow at all.

*Sources:* GUMSHOE (core clue rule); Alexandrian (Three Clue Rule — the
redundancy that makes free delivery safe); manual §h AI-adaptation flag.

## 5. How mechanics are surfaced → **prose only; the roll goes through the script**

The manual's Stage 1 wants mechanical resolution to precede narration, recorded
in a fixed machine-readable block. We take the requirement and reject the
format.

The requirement is real: a model that narrates first and reconciles mechanics
afterward will invent a flattering outcome. But the four-part block
([NARRATIVE]/[MECHANICS]/[SUGGESTIONS]/[CHRONICLE]) clashes badly with the
prose register this GM is written in, and [SUGGESTIONS] actively cuts against
presenting situations rather than solutions.

`scripts/roll.py` does the job instead. The GM must invoke it before narrating
an uncertain outcome, and the invocation and its result are visible in the
transcript. **That is a stronger guarantee than a self-reported block, not a
weaker one** — a block is written by the same pass that decided the outcome and
can be back-filled to match; a tool call happens before the outcome exists and
cannot.

The oracle (`scripts/oracle.py`) works the same way and for the same reason.

*Sources:* Amento (roll-before-outcome; enforced machine-readable output).
Requirement adopted, format replaced.

## 6. What lives in the always-loaded prompt → **whatever fires when no file is open**

`CLAUDE.md` loads in full every session and the documentation is explicit that
longer files reduce adherence. So there is a budget, and it needs a principle
for spending it. The obvious one — keep the important things, move the rest —
is wrong, and expensively so: it would move note-keeping discipline out on the
grounds that adjudication matters more, when both matter and they fail
differently.

The right question is not how important a rule is. It is **whether the rule
fires while a file is open.**

Path-scoped rules in `.claude/rules/` load when Claude reads a matching file,
and reload every time it reads one again — including after a compaction that
dropped them. That makes them *more* reliable than root `CLAUDE.md` for
anything attached to a file, not less. What they cannot do is fire when no file
is being touched, and the whole anti-sycophancy spine fires exactly there: in
the middle of writing prose, with no read to trigger anything.

So:

| Section | Where | Because |
|---|---|---|
| Starting up | `CLAUDE.md` | Runs before any file has been opened |
| Adjudication | `CLAUDE.md` | Fires mid-narration; the highest-value section and the one with no file to hang on |
| The oracle | `CLAUDE.md` | Fires when framing, not when writing anything down |
| Scenes | `CLAUDE.md` | Fires mid-narration |
| Mysteries → withholding | `CLAUDE.md` | Fires in the sentence where the player asks if they've got it |
| The world and its people | `CLAUDE.md` | Fires whenever an NPC speaks |
| Tone | `CLAUDE.md` | Fires in every line of prose |
| Safety | `CLAUDE.md` | Must be live at any moment, including one where nothing is being read |
| Notes → taxonomy and craft | `rules/notes.md` | Fires while writing a note, with the note open |
| Prep → craft, clue graphs, re-prep | `rules/prep.md` | Fires with a plan or `CLUES.md` open |

Three note-keeping rules stayed in `CLAUDE.md` against that split, and the
exception is the principle working rather than failing: *write small bits as
you go*, *after every scene ask who took a position*, and *you are writing for
a different author* all fire during play, when no notes file is necessarily
open. They are triggers. What they trigger is in the rule.

**The failure this guards against** is moving something out because the file is
long, and discovering three sessions later that it only ever mattered at a
moment when nothing was open. If you cannot name the file whose reading should
load a rule, it belongs in `CLAUDE.md`.

## 7. How much of the setting the player authors → **the player authors what their character wants; the GM authors what gets put in front of it**

The same shape as stances 1, 2 and 3 — a split by layer rather than a point on
the dial — and the layer it splits on is *appetite versus circumstance*.

- **The player authors the character's appetites.** What they care about, what
  they're working towards and by what method, how they behave under a choice,
  and the people already in their life.
- **The GM authors everything put in front of that.** The world, the situations,
  what is actually true underneath — including situations that reach straight
  into the character's life and use the people in it.

### The line is not "their stuff vs. your stuff"

That was the wrong cut, and it's the one to guard against re-drawing, because
it sounds more respectful. It would make the GM ask permission before anything
touched the character, which produces exactly the passive campaign this mode
exists to prevent.

A character who wants to protect people is bored by "there is gold down that
road" and gripped by a village being attacked. Putting the village there is not
authoring their character. It is authoring the world in front of it, aimed by
what they told you — and aiming it is the job. **What the player controls is
what would move this character. What the GM controls is what actually turns up.**

This is stance 2's "fan in the framing" arriving one layer earlier. Choosing
the situation that grabs this particular character changes what we look at, not
what is true, so it costs the impartiality nothing.

### Why not more player authorship

The collaborative-worldbuilding traditions build the setting at the table and
their argument is good: investment in a world you helped make. But **every fact
the player authored is a fact they can't find out**, and discovery is what this
player said they came for. Spend enough of the setting that way and the campaign
is a tour of a place they already have the map to.

The appetites are the layer that's free to give, and that's why they're given.
What a character wants was never discoverable *by that character* — they already
know. Handing it to the player costs no discovery at all, and buys the thing
`ideas.md` wanted: a player whose stakes and wants the world can push against.

### Why not less

`ideas.md` names the two failures this mode fixes and both are failures of too
little: a character built in isolation that doesn't fit the story, and a story
the player doesn't care about. Neither is fixed by a better world. Both are
fixed by building the world *second*, against appetites that already exist.
Session zero's step order is this stance made procedural.

### Connections are a shared band, deliberately

The people in a character's life are the one thing that sits on both sides:
they're the player's history and they're the GM's NPCs. So session zero has the
GM propose as well as ask — supplying names, suggesting who this character would
plausibly have around them. The player keeps refusal over their own
relationships; the GM keeps everything true about the people.

That shared band is not a fudge. It is where the two halves are supposed to be
welded, and a campaign where the GM only ever received connections and never
offered any would have a thinner world for it.

### The bound: what you put underneath

The underneath is the only layer of session zero the player never gets to push
back on — everything else they can argue with while it happens. So the reflex
twist deserves suspicion in proportion: the mentor is the villain, the dead
brother is alive, the debt was a setup. These are real moves that work, not
forbidden ones, and the tests are in `rules/session-zero.md`: does the played
history survive, is it discoverable, does it feed what they came to do or
remove it, and do they find it or does it arrive.

The reliable form: what's underneath should make what the player wrote matter
*more*. Heavier, not falser.

*Sources:* the collaborative traditions (Fate/Dresden city creation, PbtA "ask
questions and use the answers") — adopted for the character's appetites and
connections, rejected for the setting on the discovery argument.
Traditional/OSR GM-authored setting — adopted for the world and the situations,
and bounded by the fit check in session zero step 3, which is what stops
"GM-authored" from meaning "authored before the player existed."

---

## Revisiting these

These are defaults, not laws, and the manual is explicit that they are
positions rather than truths. Change them if play shows them wrong — but change
them *here*, in writing, with the reasoning updated. A stance that gets softened
in practice without being edited here is the exact failure the file exists to
prevent.
