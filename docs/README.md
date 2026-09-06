# docs/

**This directory is about building the GM. It is not part of the game.**

A session that is running a game should read `CLAUDE.md` and `notes/`, and stop
there. Nothing in `docs/` is campaign canon, and nothing in it is an
instruction to the GM — advice here has authority only once it has been
distilled into `CLAUDE.md` or the `notes/` scaffolding.

That distinction matters more than it looks. `docs/research/` holds outside
material written *about* AI GMs, in the second person, full of imperatives. A
GM that read it mid-session would take it for orders.

| | |
|---|---|
| `research/` | Source material, verbatim as received. Never edited to fit; if it's wrong, it stays wrong and gets contradicted in `integration.md`. |
| `integration.md` | The working tracker: what from `research/` has been encoded, rejected, or is still pending, and where it landed. |
| `stances.md` | Decisions on the axes where the sources genuinely disagree, with reasons. |
| `ideas.md` | Agreed or promising, not built. Ideas from noticing things rather than from the research. |
| `playtesting.md` | How to run a playtest and what to do with the result. The logs themselves live in `playtests/`, outside `docs/`, so a GM writing one mid-game doesn't load these development instructions. |

## How the two jobs stay apart

The GM prompt is `CLAUDE.md` at the root, loaded into every session, alongside
`.claude/rules/notes.md` and `.claude/rules/prep.md`, which are part of the game
and load when the GM opens the files they describe. The instructions for
*building* the GM are `.claude/rules/developing.md`, which
carries `paths:` frontmatter and so loads only when something opens `CLAUDE.md`,
`README.md`, `docs/`, `scripts/`, or `.claude/`. A session that is playing
touches none of those — play reads and writes `notes/` — so the development
instructions never appear during a game.

The separation is deliberately one-directional. Root `CLAUDE.md` is the only
instruction file re-injected after `/compact`, so the GM prompt has to live
there and will load during development sessions too. That's why it opens by
naming both jobs and pointing away from itself.

One gap worth knowing: `notes/` is excluded from the rule's paths on purpose,
because the GM reads `notes/README.md` at the start of every session and
matching there would fire the development instructions during play. A session
that *only* edits the notes templates won't load them. In practice such a
session also touches `docs/` or `CLAUDE.md`; if it doesn't, say so out loud.
