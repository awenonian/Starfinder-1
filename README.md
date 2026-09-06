# GM infrastructure

Boilerplate for running a tabletop RPG with Claude Code as the Game Master.

Take a copy, say what you're playing, and play. The campaign's memory lives in
the repo, so a session can start cold — a fresh Claude with no recollection of
last week reads the notes and picks up where you left off.

## Using it

1. **Press "Use this template" → Create a new repository.** One repository per
   campaign; the notes are the campaign. (This repo is a GitHub template, so
   this works from any device, including a phone browser, and works whether or
   not you own this copy. Forking also works if you don't.)
2. **Start a Claude Code session in it** and declare the system and the
   starting point:

   > *"Let's play Starfinder, starting from character creation."*
   >
   > *"ACKS, with this character: …"*

3. **Session zero happens first.** A fresh copy carries a
   `notes/gm/plans/SESSION-ZERO.md`, and the GM opens by reading it: character,
   connections, what you actually want to be playing, and lines and veils, all
   settled out in the open before any of it is prepped. It deletes itself when
   you're done, and the campaign starts.

4. **Play.** From the second session on, open with a short recap of where you
   think you left off — off the cuff is fine, lossy is expected. That recap is
   information the notes structurally can't hold, and the GM is told to trust
   it over its own notes where the two disagree.

That's the whole ritual — there is nothing to configure. A fresh copy is
playable as created, including from a phone: the dice and oracle are
pre-approved, the notes the GM needs are already scaffolded, and the setup step
is something you play rather than something you fill in.

Everything else is in `CLAUDE.md`, which Claude Code loads automatically.

## Saying something out of character

**"stop" or "skip that"** — obeyed immediately, with no questions and no
negotiating. To undo something that already happened, use your client's
rollback; the GM won't try to duplicate it, and won't advertise either one at
you.

Lines and veils live in `notes/gm/plans/CAMPAIGN.md` and are set by editing that
file, not negotiated at the top of a session.

**`log:` followed by anything**, out of character, at any point:

> `log: you confirmed my theory about the sister`

That gets written down verbatim and play carries on — no discussion, no
defending the thing you flagged. That's a note for whoever edits the GM's instructions
later, and it's the only way the prompt gets improved from evidence rather than
from theory. `playtests/` explains the rest; delete it from a copy that's only
playing.

## What's here

| | |
|---|---|
| `CLAUDE.md` | The standing instructions. How to open a session, how to keep notes, how to plan, how to talk. This is the piece that does the work. |
| `notes/` | The campaign's memory, empty and ready. `notes/README.md` maps it. |
| `scripts/roll.py` | Dice. |
| `scripts/oracle.py` | The oracle — yes/no questions, scene checks, random events. The part of the game the GM doesn't control. |
| `docs/` | How the GM was built: research, the integration tracker, and the stances taken where the sources disagree. Not part of the game. |
| `.claude/settings.json` | Pre-approves rolling dice, writing to `notes/`, and the git commands that get a session's notes onto the default branch — so play isn't interrupted by permission prompts. Delete it if you'd rather approve each one. |

`CLAUDE.md` is deliberately system-agnostic — it's about running a game, not
about any particular game. The rules of whatever you're playing come from a
rules skill, if one is installed for that system; the GM is told to look rules
up rather than trust what it thinks it remembers.

## Dice and the oracle

```
python3 scripts/roll.py '1d20+7'
python3 scripts/roll.py '4d6kh3' -n 6      # six ability scores
python3 scripts/roll.py '2d6+1' '1d8' 'd%'
```

`kh`/`kl` keep the highest/lowest N, `dh`/`dl` drop them. Dropped dice show in
parentheses. `--seed` makes a roll reproducible.

```
python3 scripts/oracle.py ask "does she already know?" --odds unlikely
python3 scripts/oracle.py scene "he agrees to meet" --chaos 7
python3 scripts/oracle.py event
```

The oracle exists because one mind running every side of a game will quietly
stop being surprised by it — it proposes the problem and also picks the
solution, and every branch gets judged by the same taste that built it. These
are the questions the GM is not allowed to answer itself, and the answers are
results rather than suggestions.

Both scripts are deliberately external. A number that arrives before the
outcome exists can't be chosen to suit it, and the call is visible in the
transcript.

## The shape of the notes

Two axes. Directories are **who the notes are for** — the player's own sheet,
what the table knows, and the GM's private journal. Files are **what kind of
thing they are** — a ledger of state, an append-only record of play, positions
characters have committed to, verbatim voice samples, and intentions.

The distinction that earns its keep is between the ledger and the record. The
GM is told to invent freely in its journal — the world should have an answer to
every question — but to write only what actually happened into the record. The
failure mode is a plausible invention landing in the file that claims to be
authoritative.

See `notes/README.md`.

## Why the prompt is shaped the way it is

The research on AI game masters converges on one failure: the model gives the
player what they want. Not by deciding to — it's built to continue text
agreeably, and a proposed action arrives looking exactly like a writing prompt
to build on. So actions succeed, plans work, theories get confirmed, and the
game empties out, because nothing that succeeds means anything once nothing can
fail.

Most of `CLAUDE.md` is built against that. Mechanics resolve through a script
before anything is narrated; stakes are named before the dice; a well-argued
action still rolls; clues are delivered freely but never interpreted. The
sources genuinely disagree with each other on several axes, and `docs/stances.md`
records which side this repo took and why — the reasoning matters more than the
conclusion, because the conclusion is what a compliant model will drift back
from.
