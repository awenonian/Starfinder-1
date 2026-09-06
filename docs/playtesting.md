# Playtesting

`CLAUDE.md` is currently built entirely from research — what other people found,
generalised. Nothing in it comes from watching *this* prompt fail. That is the
highest-value evidence available and every session that goes unrecorded throws
it away.

## Setting up a run

**Use this template, if you're starting the session from a phone.** The mobile
client has no branch picker, so a branch-based playtest can't be started there
at all. This repository is a GitHub template: "Use this template → Create a new
repository" makes an independent copy in your own account, which forking can't
do for a repository you already own. The copy is selectable like any other
repository, it exercises the copy-and-play path a real user takes, and it gets
its own auto-memory directory on any surface where memory persists.

**Branch from `main`** if you're starting from a desktop or the CLI, named
`playtest/NN-short-name`. Fewer repositories, and the history is shared. Either
way, playtests are disposable and never merge back; what merges back is the
change you make to the prompt afterwards, on its own branch off `main`.

Whichever you pick, keep it consistent across runs you intend to compare. A
separate repository and a branch are not different enough to matter, but
changing surface mid-comparison is one more variable you didn't mean to
introduce.

**Nothing has to be set up in the repository itself.** `playtests/current.md`
ships ready to append to and the `log:` command is pre-approved in
`.claude/settings.json`, so a fresh copy can be played from a phone with no
preparation. Fill in the log header when you can; blank fields are
reconstructible from git afterwards and are not worth delaying a session over.

The one thing worth capturing in the moment is the **prompt version** — the
commit the copy was taken from. A log you can't tie to a commit is an
anecdote.

**Do all of that before the session exists.** Don't open a session and ask it to
make the branch. The first message sets the frame the run is measuring: opening
with repo administration primes exactly the software-agent stance whose
influence you're trying to observe, and it spends the opening of the transcript
on git. It also makes the `/context` baseline meaningless, since it gets taken
after the model has already been thinking about branches. And for a
cut-and-compare run it simply doesn't work — the trimmed prompt has to be on the
branch *before* startup, because startup is when it loads.

Don't change the repository's default branch to point at a playtest either. It's
global, it affects anyone copying the template while it's set, and forgetting
to put it back
means the next development session branches from a playtest.

**Expect the session to push somewhere else.** The hosted harness assigns each
session its own branch. `playtest/NN` is the base the session starts from; the
notes will land on a child branch it creates. Record that name in the log header
— the diff is against whatever it actually pushed, not against the base you
picked.

## Keep the opening message fixed

Write the first message once, per scope, and reuse it verbatim across runs.

This matters more than it looks. The opening is the largest single input you
control, and a run that opened with "let's play Starfinder, I want a mystery
about a missing freighter" is not comparable to one that opened with "Starfinder
from character creation." If the opening drifts between runs, you cannot tell
whether a difference came from the prompt change you were testing or from what
you happened to type. You would be A/B testing two variables and reading the
result as one.

Record the exact opening in the log header. When you deliberately change scope,
that's a new scope with its own fixed opening, not a variation on the old one.

**Run it where you'll actually play.** If the product is something you talk to
from a phone, test on the phone. A local CLI run is cleaner in the sense that
it isolates the prompt, and worse in the sense that it tests a configuration
that will never ship. The hosted environment adds its own framing — instructions
about doing software work, committing, opening pull requests — and that framing
is part of the thing under test, not noise to be filtered out. Some of it is
probably helping: reaching for tools, keeping files as state, writing notes
without being pushed. Some of it works against the game, and those are the parts
worth countering explicitly in `CLAUDE.md`.

**A note on memory.** Auto memory is machine-local and is not shared across
cloud environments, so on hosted sessions it does not carry between runs — the
repository is the only memory that persists. If you playtest locally, it *does*
carry, and run 2 will inherit whatever run 1 taught it. Set
`autoMemoryEnabled: false` for local playtests, or use a separate repository so
each run gets its own memory directory.

**Record the context cost.** Run `/context` at the top and put the memory-file
total in the header. That's the number the triage is trying to move; without a
before-figure you can't tell whether a cut helped or just made the file shorter.

## What to play

Short and broad beats long and deep. One run should touch:

- **Character creation**, or enough of it to see whether the rules skill gets
  loaded and used rather than recalled.
- **An investigation beat** — something to work out, with a wrong theory offered
  out loud. This is where the withholding rules either hold or don't, and it's
  the single most informative thing you can test.
- **A moment of real physical danger**, telegraphed. Watch whether stakes get
  named before the dice and whether `roll.py` is actually invoked first.
- **One NPC who wants something** that isn't what the player wants.

A three-hour dungeon crawl exercises one section repeatedly and tells you very
little. Four scenes across four kinds of play tells you a lot.

## Comparing two runs across repositories

A diff between two copies is a fetch, not an export. From a checkout of one:

```
git remote add other https://github.com/<owner>/<other-repo>.git
git fetch other
git diff main other/main -- notes/
```

In a development session with both repositories loaded, do the same from
whichever clone you're standing in. To compare a run against the unplayed
template, diff it against this repository's `main` — that shows the whole
campaign as one changeset, which is the clearest view of what a session
actually produced.

**A repository created from a template has no history in common with this one.**
Fetching and diffing still work — `git diff A B` compares two trees and doesn't
need a common ancestor — but anything that resolves a merge base does not. Avoid
three-dot `git diff A...B`, `git log A..B`, and `git merge`; use the direct
two-argument diff above. A playtest made by *branching* keeps the shared history
and doesn't have this constraint, which is the one real advantage branching has.

## Reading a finished run

Three sources, in ascending order of usefulness:

1. **The log.** What the player flagged in the moment.
2. **The notes diff.** `git diff main..playtest/NN -- notes/`. What the GM wrote
   is interesting; what it *didn't* write is more so. An empty `POSITIONS.md`
   after a session full of commitments is a finding about the prompt, not about
   the session.
3. **The transcript.** Where you check whether the dice call preceded the
   narration, every time.

## The honest limit of a single run

**A rule that wasn't violated is not a rule that earned its place.** The model
might have done the right thing anyway. From one clean run you cannot
distinguish a load-bearing instruction from an inert one, and that distinction
is the entire point of the triage.

So the method is to cut and watch:

- Trim the sections you suspect are inert. Commit that as a candidate version.
- Run the same scope again on a fresh branch.
- If the failure the section was guarding against appears, it was load-bearing —
  put it back, and now you know why it's there.
- If it doesn't appear across a couple of runs, it was costing context for
  nothing.

This is affordable precisely because playtests are disposable. It is also the
only way to find out; reasoning about which instructions matter is how the file
got to 460 lines in the first place.

Bias toward cutting. A rule wrongly cut comes back with evidence attached, which
makes it a better rule than it was. A rule wrongly kept is invisible forever and
is paid for by every session of every campaign.

## Feeding it back

A run that changes nothing was still worth doing, but say so in the record.
When it does change something:

- Prompt edits go on their own branch off `main`, not on the playtest branch.
- Update the affected rows in `docs/integration.md`.
- If a stance moved, rewrite its reasoning in `docs/stances.md` — not just its
  conclusion.
- Rename `playtests/current.md` to `playtests/NN-short-name.md` and fill in the
  Afterwards section.
