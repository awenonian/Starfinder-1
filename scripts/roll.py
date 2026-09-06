#!/usr/bin/env python3
"""Dice roller for the GM.

Usage:
    python3 scripts/roll.py '1d20+7'
    python3 scripts/roll.py '4d6kh3' -n 6      # six ability scores
    python3 scripts/roll.py '2d6+1' '1d8' '1d100'

Notation:
    NdX             roll N dice of X sides (N defaults to 1)
    d%              same as d100
    NdXkh#  NdXkl#  keep the highest / lowest #
    NdXdh#  NdXdl#  drop the highest / lowest #
    + - integers and further dice terms chain freely: 1d8+1d6+3-1

Kept dice are shown plain, dropped dice in parentheses.
"""

import argparse
import random
import re
import sys

TERM = re.compile(
    r"""^
    (?P<count>\d*)
    d
    (?P<sides>\d+|%)
    (?:(?P<mode>kh|kl|dh|dl)(?P<amount>\d+))?
    $""",
    re.IGNORECASE | re.VERBOSE,
)


class DiceError(ValueError):
    pass


def roll_term(term, rng):
    """Roll one dice term. Returns (total, rendering)."""
    m = TERM.match(term)
    if not m:
        raise DiceError(f"can't read dice term {term!r}")

    count = int(m.group("count") or 1)
    sides = 100 if m.group("sides") == "%" else int(m.group("sides"))
    if count < 1:
        raise DiceError(f"need at least one die in {term!r}")
    if sides < 2:
        raise DiceError(f"a d{sides} is not a die")
    if count > 1000:
        raise DiceError(f"{count} dice is more dice than anyone needs")

    rolls = [rng.randint(1, sides) for _ in range(count)]

    mode = (m.group("mode") or "").lower()
    if mode:
        amount = int(m.group("amount"))
        if amount > count:
            raise DiceError(f"can't {mode}{amount} from only {count} dice in {term!r}")
        order = sorted(range(count), key=lambda i: rolls[i], reverse=mode in ("kh", "dl"))
        # kh/kl name what to keep; dh/dl name what to drop.
        cut = amount if mode in ("kh", "kl") else count - amount
        kept = set(order[:cut])
    else:
        kept = set(range(count))

    total = sum(rolls[i] for i in kept)
    shown = " ".join(str(r) if i in kept else f"({r})" for i, r in enumerate(rolls))
    return total, f"{term}: [{shown}]"


def roll(expression, rng):
    """Evaluate a whole expression. Returns (total, [renderings])."""
    expr = expression.replace(" ", "")
    if not expr:
        raise DiceError("empty expression")
    if not re.match(r"^[-+]?[0-9dkhl%+-]+$", expr, re.IGNORECASE):
        raise DiceError(f"can't read expression {expression!r}")

    total = 0
    parts = []
    for sign, term in re.findall(r"([+-]?)([^+-]+)", expr):
        factor = -1 if sign == "-" else 1
        if term.isdigit():
            total += factor * int(term)
            parts.append(f"{sign or '+'}{term}")
        else:
            subtotal, shown = roll_term(term, rng)
            total += factor * subtotal
            parts.append(shown if factor == 1 else f"-{shown}")
    return total, parts


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Roll dice.", formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="examples:\n  roll.py 1d20+7\n  roll.py 4d6kh3 -n 6\n  roll.py 2d6+1 1d8",
    )
    parser.add_argument("expression", nargs="+", help="dice expression, e.g. 4d6kh3")
    parser.add_argument("-n", "--times", type=int, default=1, help="repeat each expression")
    parser.add_argument("--seed", help="seed, for reproducible rolls")
    args = parser.parse_args(argv)

    if args.times < 1:
        parser.error("--times must be at least 1")

    rng = random.Random(args.seed) if args.seed is not None else random.SystemRandom()

    for expression in args.expression:
        for _ in range(args.times):
            try:
                total, parts = roll(expression, rng)
            except DiceError as err:
                print(f"{expression}: {err}", file=sys.stderr)
                return 2
            print(f"{total:>6}   {'  '.join(parts)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
