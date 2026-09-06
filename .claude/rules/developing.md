---
paths:
  - "CLAUDE.md"
  - "README.md"
  - "docs/**"
  - "scripts/**"
  - ".claude/**"
---

# Working on this repository

You are building a Game Master. You are not being one.

**If you are actually running a game and reached this file incidentally** —
you opened a script to check its usage, say — ignore everything below and carry
on. This loaded because of a path match, not because the job changed.

`CLAUDE.md` at the root is a **product artifact**. It is addressed to a GM
running a campaign, in the second person, and it will have told you that you
are the Game Master. That instruction is for the campaign copy, not for this
session. Read it as the thing you are editing.

## The layout

| | |
|---|---|
| `CLAUDE.md` | The GM prompt. Loaded into every session of every campaign. The product. |
| `notes/` | Scaffolding for the campaign's memory. Templates and READMEs only — no play content. |
| `scripts/` | `roll.py` and `oracle.py`. The parts of the game the GM can't talk itself out of. |
| `docs/research/` | Source material, verbatim. |
| `docs/integration.md` | What we did with each claim in the research. |
| `docs/stances.md` | Where the sources conflict and which side we took. |

## Why the GM prompt lives at the root

Root `CLAUDE.md` is the only instruction file re-injected after `/compact`.
Nested `CLAUDE.md` files and path-scoped rules — including this one — are not.
A long session of play will compact, so anything the GM must not lose has to be
in the root file.

That constraint decides several things that look like style choices. Don't move
the GM prompt into an import or a nested file to tidy it up; you would be
trading a real guarantee for a cosmetic one.

## Working rules

**`docs/research/` is verbatim and stays verbatim.** Don't fix its errors,
trim it, or reformat it. If it's wrong, it stays wrong on the page and gets
contradicted in `integration.md`. It is a record of what a source said, and a
record that gets edited to agree with us is worthless.

**Every change to `CLAUDE.md` updates `docs/integration.md`.** If you encoded
something, move its row to `encoded` and say which section it landed in. If you
decided against something, mark it `rejected` and say why — a rejection is a
decision and carries as much weight as an adoption. The table's value is that
nothing was silently dropped, and that holds only if it stays current.

**Changing a stance means rewriting its reasoning.** `docs/stances.md` records
*why*, because a later session reading only conclusions will drift back toward
the agreeable middle — which is the same failure the prompt is built against,
one level up. A stance that gets softened in practice without being edited there
is the exact thing the file exists to prevent.

**Run the scripts.** They're small enough to look correct while being wrong.
`roll.py` and `oracle.py` both take `--seed`, so a check is reproducible.

**Check whether the client already does it.** Before writing a rule, ask
whether the surface the game runs on already provides that capability. A prompt
that reimplements a platform feature pays for it twice — in context, and in the
session time spent announcing it — and ships the weaker version. Rewinding is
the worked example: the client's rollback removes turns, which beats asking the
narrator to un-say something. See `playtests/01-cold-start-preamble.md`.

**Keep `CLAUDE.md` earning its length.** It loads in full every session, and
the docs are explicit that longer files reduce adherence. Adding to it is a
real cost paid by every session of every campaign. Prefer sharpening a clause
over adding one, and put anything that isn't needed *during play* somewhere
else.

**`notes/` stays empty of play.** This repository is a GitHub template, so the
files in `notes/` are the starting state of every campaign made from it. If a
campaign's content lands in one, it becomes someone else's opening canon.

## The thing to be suspicious of

Most of `CLAUDE.md` exists to stop a model handing the player whatever they
asked for. When you edit it, you are the same kind of model, working on the
same failure, with no dice in the loop. Softening a rule because it reads as
harsh is that failure wearing a different hat. If a guard feels too strict,
that is evidence about the guard being load-bearing, not evidence it should go.
