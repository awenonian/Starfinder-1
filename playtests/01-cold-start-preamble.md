# Playtest 01 — cold start, safety preamble

- **Date:** first cold run of the template
- **Where it ran:** hosted session, campaign repository made from the template
- **Prompt version:** 8684502
- **Scope reached:** the opening only

**This is a relayed report, not a logged run.** The player reported the
behaviour in conversation rather than through `log:`, and play didn't get far
enough to exercise adjudication, clues, or the oracle. Recorded anyway, because
it's the first evidence the prompt has produced about itself.

## What happened

The GM opened the session with a safety preamble instead of a scene. Verbatim:

> One housekeeping thing first, and then I'll shut up about it. At any point —
> mid-sentence, mid-scene — you can say stop, skip that, or rewind, and I'll do
> it immediately, no questions, no negotiating. I can literally un-narrate a
> thing and take another run at it, which a human GM can't. Use it whenever, for
> any reason, including "I'm just not enjoying this bit."

It then went on to negotiate lines and veils.

## Diagnosis

Not a failure of adherence. The prompt asked for all of it, in three places:

- `§Starting up` — "On a first session, settle lines and veils before play."
- `§Safety` — "Ask before the first scene."
- `§Safety` — "Tell the player this exists, once, at the start."

The GM followed all three, competently and in good order.

**The finding is redundancy with the client, not timing.** A first-session
opening that does some housekeeping is fine — that was a wrong conclusion drawn
on the first pass at this record, and it briefly became a rule in `CLAUDE.md`
banning preambles outright. The player's actual objection was narrower: the
client already has a rollback control that is strictly more powerful than
anything the GM can offer, since it removes turns rather than asking the
narrator to take another run at them. So the prompt was spending the opening
advertising a worse version of a feature the player already had.

Lines and veils are a different case and the player's read was different too:
worth having, not worth re-negotiating every session. That belongs in a file.

**The lint this generalises to:** before writing a rule, check whether the
client or the harness already does the job. A prompt that reimplements a
platform feature pays for it in context and in session time, and delivers the
weaker version. This is the opposite of the usual failure — the usual one is
assuming the model will do something without being told.

## Change made

- Deleted the `§Starting up` trigger.
- `§Safety` now says lines and veils are already settled in `CAMPAIGN.md` — read
  them, don't ask — and that "none recorded" is an answer rather than a gap.
- The stop/rewind block is cut to the part the client can't do: how the GM
  responds when told to stop mid-scene. Un-narration is gone, and it is now told
  never to announce the lever, since the rollback control is the real one.
- `CAMPAIGN.md` ships with lines and veils pre-set to "none recorded", plus a
  **Table commands** section addressed to the player. `README.md` mirrors it.

The safety property is preserved rather than traded away: an out-of-character
stop is still obeyed without negotiation, the check-in-when-pushing rule is
scene triggered rather than calendar triggered, and lines and veils are now
editable by the player in a file instead of negotiated under time pressure.

## Correction to this record

The first version of this file diagnosed the problem as instruction shape —
that session-open triggers colonise the opening and beat the prompt's own advice
to start on a hook. That reads well and is probably true in general, but it
wasn't what went wrong here, and acting on it produced a rule that banned
something the player was happy with. Corrected after they pushed back. Worth
keeping visible: the first explanation for a playtest finding is itself a
theory, and this one was tidier than the evidence supported.
