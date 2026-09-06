#!/usr/bin/env python3
"""An oracle, for questions the GM should not be allowed to answer itself.

A single intelligence running both sides of a game collapses toward
wish-fulfilment: it proposes the problem and then chooses the solution, and the
surprise goes out of it. This script is the external source of uncertainty that
prevents that. Its answers are not suggestions.

    oracle.py ask "does the harbourmaster know?" --odds unlikely
    oracle.py scene "she agrees to meet"
    oracle.py event
    oracle.py chaos

The chaos factor (1-9) tunes how often the world intrudes. It lives in
notes/gm/STATE.md, not in this script — pass it with --chaos. Raise it when the
player is losing control of the situation, lower it when they are gaining it.

`ask` also fires a random event on a doubles roll within the chaos factor, the
same way a scene check can be interrupted. When that happens the event is not
optional colour; something has just happened, and it is the GM's job to work
out what.
"""

import argparse
import random
import sys

# Chance of "yes" at chaos 5, before the chaos shift.
ODDS = {
    "certain": 95,
    "near-certain": 90,
    "very-likely": 80,
    "likely": 70,
    "even": 50,
    "unlikely": 30,
    "very-unlikely": 20,
    "near-impossible": 10,
    "impossible": 5,
}

# Each step of chaos away from 5 moves the odds this far toward yes.
CHAOS_STEP = 5

EVENT_FOCUS = [
    (18, "a thread advances"),
    (28, "a thread stalls or reverses"),
    (38, "an NPC acts on what they want"),
    (48, "an NPC appears, unexpectedly"),
    (56, "an NPC suffers something"),
    (64, "an NPC helps, for their own reasons"),
    (72, "the player character's situation worsens"),
    (78, "the player character's situation improves"),
    (86, "something in the world changes"),
    (93, "something hidden becomes visible"),
    (100, "something arrives from outside the current situation"),
]

ACTIONS = [
    "abandon", "accuse", "arrive", "bargain", "betray", "block", "break",
    "carry", "conceal", "confront", "demand", "delay", "deprive", "divide",
    "expose", "extort", "follow", "gather", "guard", "harm", "hurry",
    "imitate", "inform", "inspect", "intrude", "judge", "lie", "mourn",
    "offer", "oppose", "postpone", "praise", "propose", "protect", "refuse",
    "release", "repair", "replace", "return", "reveal", "sell", "separate",
    "summon", "surrender", "suspect", "take", "threaten", "trade", "wait",
    "withhold",
]

SUBJECTS = [
    "a debt", "a message", "a name", "a promise", "a rumour", "a secret",
    "a weapon", "a witness", "an heirloom", "an old grievance", "authority",
    "blood", "coin", "documents", "evidence", "family", "fire", "food",
    "goods", "history", "hospitality", "illness", "information", "kinship",
    "labour", "law", "loyalty", "machinery", "medicine", "memory", "money",
    "news", "passage", "property", "reputation", "ritual", "safety",
    "shelter", "sickness", "silence", "status", "supplies", "the dead",
    "the past", "territory", "the truth", "trade", "travel", "trust", "water",
]


def clamp(value, low, high):
    return max(low, min(high, value))


def check_chaos(value):
    if not 1 <= value <= 9:
        raise ValueError(f"chaos factor is 1-9, got {value}")
    return value


def random_event(rng):
    """Roll up a random event: what it touches, and a verb/noun pair to read."""
    focus_roll = rng.randint(1, 100)
    focus = next(text for threshold, text in EVENT_FOCUS if focus_roll <= threshold)
    action = rng.choice(ACTIONS)
    subject = rng.choice(SUBJECTS)
    return focus, action, subject


def print_event(focus, action, subject):
    print(f"  RANDOM EVENT: {focus}")
    print(f"  read as: {action} / {subject}")
    print("  This happened. Work out what it means before you narrate on.")


def cmd_ask(args, rng):
    chaos = check_chaos(args.chaos)
    threshold = clamp(ODDS[args.odds] + (chaos - 5) * CHAOS_STEP, 2, 98)
    roll = rng.randint(1, 100)

    if roll <= threshold:
        answer = "YES"
        if roll <= max(1, threshold // 5):
            answer = "YES, AND — more so than asked"
    else:
        answer = "NO"
        if roll >= threshold + (100 - threshold) * 4 // 5:
            answer = "NO, AND — worse than asked"

    if args.question:
        print(f"Q: {args.question}")
    print(f"{answer}   (rolled {roll} vs {threshold}, {args.odds} at chaos {chaos})")

    # Doubles within the chaos factor drag something else in with the answer.
    tens, ones = divmod(roll, 10)
    if tens == ones and 1 <= tens <= chaos:
        print()
        print_event(*random_event(rng))
    return 0


def cmd_scene(args, rng):
    chaos = check_chaos(args.chaos)
    roll = rng.randint(1, 10)

    if args.expected:
        print(f"Expected: {args.expected}")

    if roll > chaos:
        print(f"SCENE AS EXPECTED   (rolled {roll} vs chaos {chaos})")
        return 0

    if roll % 2 == 1:
        print(f"SCENE ALTERED   (rolled {roll} vs chaos {chaos})")
        print("  One assumption behind the expected scene is wrong. Pick the")
        print("  one whose failure is most interesting and play that instead.")
    else:
        print(f"SCENE INTERRUPTED   (rolled {roll} vs chaos {chaos})")
        print("  The expected scene does not happen. This does:")
        print()
        print_event(*random_event(rng))
    return 0


def cmd_event(args, rng):
    print_event(*random_event(rng))
    return 0


def cmd_chaos(args, rng):
    print("Chaos factor — how much the world intrudes. Store it in notes/gm/STATE.md.")
    print()
    print("  1-3  the player is in control; the world mostly waits")
    print("  4-6  contested; things happen while they decide")
    print("  7-9  the player is being carried by events")
    print()
    print("After a scene: raise it by one if the player ended less in control")
    print("than they started, lower it by one if more. Don't move it further")
    print("than that, and don't move it because a scene felt slow.")
    return 0


def main(argv=None):
    # --chaos and --seed hang off each subcommand rather than the top level, so
    # they read the way the examples write them: `oracle.py ask ... --chaos 7`.
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--chaos", type=int, default=5, help="chaos factor, 1-9 (default 5)")
    common.add_argument("--seed", help="seed, for reproducible results")

    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)

    ask = sub.add_parser("ask", parents=[common],
                         help="yes/no question about something you don't control")
    ask.add_argument("question", nargs="?", help="the question, for the transcript")
    ask.add_argument("--odds", default="even", choices=sorted(ODDS), help="how likely, before chaos")
    ask.set_defaults(func=cmd_ask)

    scene = sub.add_parser("scene", parents=[common],
                           help="check whether a framed scene happens as expected")
    scene.add_argument("expected", nargs="?", help="what you expect the scene to be")
    scene.set_defaults(func=cmd_scene)

    event = sub.add_parser("event", parents=[common], help="roll a random event outright")
    event.set_defaults(func=cmd_event)

    chaos = sub.add_parser("chaos", parents=[common], help="how to set the chaos factor")
    chaos.set_defaults(func=cmd_chaos)

    args = parser.parse_args(argv)
    rng = random.Random(args.seed) if args.seed is not None else random.SystemRandom()

    try:
        return args.func(args, rng)
    except ValueError as err:
        print(f"oracle: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
