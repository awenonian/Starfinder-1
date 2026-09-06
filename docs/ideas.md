# Ideas not yet built

Design ideas that are agreed or promising but not implemented. Each says what
it is, why it might work, and what would have to be true. Kept here rather than
in `integration.md` because these don't come from the research — they come from
noticing something while building or playing.

---

## Prep for the next session at the end of the current one

**The idea.** Session prep happens during the close of the previous session,
not at the start of the next one. First session excepted, since there is no
previous.

**Why it's likely better than prepping at the start:**

*The author who was there does the prep.* Prep at the start of a session is
written by an author with only the notes. Prep at the end is written by the
author who ran the thing — who knows which NPC landed, which thread the player
kept circling back to, which prepped beat quietly died. That is the same
argument the standing prompt already makes about the player's recap: it is
information the notes structurally cannot hold. Right now the GM only gets that
information *about* the last session; this would let it use its own equivalent.

*It turns the compression problem into a test.* The known failure of
end-of-session write-ups is that you compress and cannot feel what you're
compressing out. But if you have to write next session's plan from the notes
you just wrote, the plan becomes a check on them: prep that can't be built is
prep whose notes were insufficient — and you find that out while the session is
still in context and the gap is still cheap to fix. Prep-at-end is the
handoff's own test case.

*It moves the cost off the player's clock.* A long close can spin. A session
opening cannot; the player has just asked to play and is waiting.

**What would have to be true:**

- *The plan has to survive the recap.* The player's recap arrives after the
  prep now exists, and prep is stickier than conversation — the exact failure
  the prompt already warns about, newly load-bearing. The startup sequence
  would have to explicitly re-check the prep against the recap, not just the
  notes, and re-prep where they disagree.
- *Sessions don't always end cleanly.* A session that stops mid-scene has no
  close to hang prep on. There would need to be a recorded state for "prep is
  owed," so the next session knows to do it at the start rather than assuming
  it exists and running on nothing.
- *Elapsed real time is unknown at prep time.* Offscreen clocks advance between
  sessions, and the close doesn't know whether the gap is a day or a month.
  Probably: prep the situation, and advance the clocks at the start when the
  gap is known. That splits cleanly along prep-situations-not-plots anyway.
- *It has to reload after compaction.* Prep at the end of a session happens
  after compaction is likely to have occurred, so the prep guidance cannot live
  only in root `CLAUDE.md` — it has to be reachable when the GM opens a plan
  file. This is already handled: `.claude/rules/prep.md` is path-scoped and
  reloads on read.

**Open question.** Whether the close should also draft the *next* session's
strong start, or stop at the situation. Drafting an opening scene is close to
prepping a plot, and the player's first move may invalidate it — but a session
that opens on something concrete is worth a lot, and re-prepping one scene is
cheap. Probably: prep the situation, note two or three places the session could
open, commit to none.

**Status.** Not implemented. Would touch: the startup sequence in `CLAUDE.md`,
a new close sequence, and `notes/gm/plans/` conventions.

---

## A place to record rule-breaks observed in play

**The idea.** The practitioner literature recommends treating every observed
rule-break as a new prompt clause. There is nowhere to write down "the GM
confirmed a theory in session 4" when it happens.

**Why it matters.** The prompt is currently built entirely from research —
what other people found, generalised. Nothing in it comes from watching *this*
prompt fail. That is the highest-value source available and it is being thrown
away every session.

**What it would need.** A log the player or the GM can append to during play
without breaking the fiction, and a development-side habit of reading it before
editing `CLAUDE.md`. The awkward part is that the GM noticing its own
sycophancy is exactly what the prompt says it cannot reliably do, so the useful
entries will mostly come from the player.

**Status.** Built. `playtests/` holds the logs and `docs/playtesting.md` the
protocol; the `log:` command is in `CLAUDE.md` under Safety. The log is the
player's rather than the GM's, since a GM assessing its own compliance is the
thing the research says it can't do.

---

## A visible session zero

**The idea.** Character creation and the initial worldbuilding happen as an
explicit collaborative mode, out in the open, with player input — before the
first session of play proper.

**Why stance 1 wants it.** The world-resolution rule says the GM answers every
established question definitely. Done entirely in private before session one,
that produces a fully-realised setting the player had no hand in, and the
proactive style the player prefers runs on the player having stakes,
connections, and wants that the world can push against. Those can't be
prepped for them.

**The argument that makes it more than taste:** a world the player helped build
is a world the player *remembers*. That is a second store for the setting layer,
outside the notes and outside the context window — and the recap protocol
already makes the player authoritative where they disagree with the notes.
Session zero extends that authority from events to the setting, which is
precisely the layer the resolution rule is trying to hold consistent. The
player stops being only a source of recap and becomes an error-check on drift.

**Why it's a separate mode, not a first scene.** Almost none of the standing
prompt applies. No adjudication, no oracle, no withholding of interpretation, no
scene framing, no dice. It is collaborative document authoring with a person.
That makes it the clearest candidate in the whole design for a **skill** rather
than prompt content: genuinely once per campaign, needing none of the play-time
machinery, and loading only when invoked. Which is also the first real test of
whether skills are the answer to the context budget.

**The constraint to design against.** A collaborative setting build can hollow
out the mysteries — a player who helped construct the world knows things their
character shouldn't, and the GM's private answers get thinner as the shared ones
get richer. The split probably wants to be: the player authors the *situation*,
the connections, and what their character cares about; the GM privately authors
what is actually going on underneath it. Getting that boundary wrong in either
direction is the failure — too much player authorship and there is nothing to
find out, too little and it is just prep with extra steps.

**Also absorbs** the lines-and-veils conversation, which `CLAUDE.md` currently
hangs off "on a first session."

## How it's wired

The mode is triggered by a **file that deletes itself**, not by a skill. The
skill instinct above was right about the cost and wrong about the firing.

- `notes/gm/plans/SESSION-ZERO.md` ships in the template. Its *existence* is
  the flag for "this campaign hasn't started". It's also the worksheet: the GM
  writes into it during session zero, distributes the content into the
  permanent notes at the close, and deletes it. Gone means it never fires
  again.
- `.claude/rules/session-zero.md` is path-scoped to exactly that file, so the
  procedure can be as long as it needs to be and costs nothing from the second
  session onward, when the path stops matching.
- One paragraph in `CLAUDE.md` § Starting up points at the file if it exists.
  That is the entire permanent cost, and it self-cancels.

**Why not a skill.** Skills fire on description-matching, which is
probabilistic, and the one moment this must fire is the moment the GM has the
least context to match against — turn one of a cold repo. A skill also doesn't
retire: it sits in the campaign forever and can trip in session nine. The rule
gets skill-like laziness from a path that only ever matches once, with
deterministic firing.

**Why it beats putting the procedure in `CLAUDE.md`.** Beyond stance 6 — a
long session-zero conversation will compact, and root `CLAUDE.md` is the only
thing re-injected. But a path rule reloads on *every* matching read, and the
worksheet is the GM's working document during the mode. The procedure
re-injects itself for free, which the root file's guarantee does not do.

**Two things it gets for nothing.** A session zero interrupted halfway leaves a
partly-filled worksheet, which the next session reads and resumes from — no
extra state machine. And re-running it later (a second character, a new arc) is
just recreating the file; the rule's guard asks whether that was deliberate
rather than assuming it wasn't.

**Status.** Built. `.claude/rules/session-zero.md` carries the four-step
procedure — character mechanically, who they are, the world built onto them,
finalise — and stance 7 records the authorship split it turns on. Untested: no
playtest has run it, and the two things most likely to be wrong are its length
in practice and whether the fit check at the end of step 3 actually catches a
mismatch or just describes one.

