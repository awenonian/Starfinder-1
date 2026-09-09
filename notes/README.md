# Notes

Everything that survives between sessions. A session starts with the GM knowing
nothing but `CLAUDE.md` and this tree.

Two axes organise it. The **directory** is who the notes are for; the **file**
is what kind of thing they are. `CLAUDE.md` defines both axes — this file is
just the map.

```
notes/
  player-owned/     the player's, not yours. Don't edit without permission.
  player-facing/    what the player knows, or what people in the world know.
    RECORD.md       what happened, in play order, append-only, never tidied
    STATE.md        the ledger of known things
    POSITIONS.md    what characters committed to, in the open
  gm/               your journal. Nobody else reads it. Hide nothing from yourself.
    STATE.md        the truth behind the ledger — secrets, clocks, offscreen movement
    THREADS.md      every open loop and its status. Nothing ambiguous.
    CLUES.md        the mystery as a graph: revelations, who knows what
    RULES-SUPPLIED.md  out-of-book rules text the player pasted in. Never ask twice.
    characters/     one file per recurring character: VOICE, INTENTION, positions
    plans/          campaign plan, session plans, scene plans
      SESSION-ZERO.md   only in a campaign that hasn't started. Read it first;
                        it deletes itself when session zero is done.
```

## Where does this go?

| You have… | It goes… |
|---|---|
| A number, a holding, an inventory, a location | `player-facing/STATE.md` if the player knows it, `gm/STATE.md` if not |
| Something that just happened at the table | `player-facing/RECORD.md`, appended, in play order |
| Something a character committed to | `player-facing/POSITIONS.md`, and the character's own file |
| A line a character actually said | the character's file, verbatim, under VOICE |
| What a character wants, or would never do | the character's file, under INTENTION |
| A question raised and not yet answered | `gm/THREADS.md`, marked open |
| A clue, or a conclusion it points at | `gm/CLUES.md` |
| A fact that's true but not yet revealed | `gm/CLUES.md`, under loose clues |
| Something you decided about the world | `gm/STATE.md` — and if it hasn't reached play yet, say so |
| A thing you intend to happen | `gm/plans/` |

## Two rules that are easy to get backwards

**The world has an answer to every question.** In `gm/`, don't leave mysteries
unsolved for yourself. Uncertainty is a fact about people, not about the world.

**Except in the record.** `RECORD.md` gets only what came from play. If you are
filling a gap there with something plausible, you have stopped recording and
started inventing, in a file that claims to be authoritative.
