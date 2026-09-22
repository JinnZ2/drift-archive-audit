#!/usr/bin/env python3
"""Null distribution for phi-adjacent ratio detection.

WHAT THIS TESTS AND WHAT IT DOES NOT.

  TESTS      how often a phi-ratio search finds a hit in data with NO
             structure in it, as a function of the two free parameters
             every such search has: the tolerance, and how many members
             the "phi-adjacent" target set is allowed.
  DOES NOT   test any particular detector. No instrument from any repo was
             read. Nothing here says anything about the 16-storm result or
             the 82% figure; those belong to a detector this file has not
             seen.

WHY IT EXISTS. A claim was made that phi-adjacent ratios are dense enough
that a detector without a null will find them in almost any sequence. That
is a quantitative claim and it can be checked with the standard library in
one file, so it was, rather than being agreed with.

It is the same defect family as this session's false-zero regex, running in
the opposite direction: there a query form manufactured an ABSENCE, here a
target set manufactures a PRESENCE. Both are match-unit failures and neither
is detectable from inside the result.

NO PASS STATE. The output is a table of null rates. There is no input that
makes this file say a finding is real, and none that makes it say a finding
is spurious -- it reports what the floor is, and the floor is what a real
finding has to clear.

Stdlib only. CC0.
"""

import random
import math

PHI = (1 + 5 ** 0.5) / 2

# Target sets, nested. Each level is what a search is willing to call
# "phi-adjacent". The levels are named because the choice is a free
# parameter that is almost never declared.
FAMILIES = [
    ('L1  phi only',        [PHI]),
    ('L2  + reciprocal',    [PHI, 1 / PHI]),
    ('L3  + squares',       [PHI, 1 / PHI, PHI ** 2, 1 / PHI ** 2]),
    ('L4  + root, cube',    [PHI, 1 / PHI, PHI ** 2, 1 / PHI ** 2,
                             PHI ** 0.5, 1 / PHI ** 0.5,
                             PHI ** 3, 1 / PHI ** 3]),
]

TOLERANCES = [0.01, 0.02, 0.05, 0.10]


def hits(ratio, targets, tol):
    """True if ratio is within relative tolerance tol of any target."""
    return any(abs(ratio - t) <= tol * t for t in targets)


def sequence_ratios(values):
    """Adjacent ratios, orientation-free (larger over smaller)."""
    out = []
    for a, b in zip(values, values[1:]):
        if a <= 0 or b <= 0:
            continue
        out.append(max(a, b) / min(a, b))
    return out


def make_sequence(n, kind, rng):
    """Structureless positive values. Two shapes, because the answer should
    not depend on which one a reader finds plausible."""
    if kind == 'uniform':
        return [rng.uniform(1.0, 100.0) for _ in range(n)]
    return [math.exp(rng.gauss(0.0, 1.0)) for _ in range(n)]


def run(n_values, trials=20000, seed=20260922):
    """Per-ratio and per-sequence null rates across the parameter grid."""
    rng = random.Random(seed)
    seqs = {k: [make_sequence(n_values, k, rng) for _ in range(trials)]
            for k in ('uniform', 'lognormal')}

    print('  sequence length n = %d   (%d adjacent ratios per sequence)'
          % (n_values, n_values - 1))
    print('  trials per cell   = %d' % trials)
    print()
    header = '  %-22s %-11s' % ('target set', 'shape')
    header += ''.join('   tol %-5s' % ('%d%%' % int(t * 100)) for t in TOLERANCES)
    print(header)
    print('  ' + '-' * (len(header) - 2))

    for label, targets in FAMILIES:
        for kind in ('uniform', 'lognormal'):
            row = '  %-22s %-11s' % (label, kind)
            for tol in TOLERANCES:
                any_hit = 0
                for values in seqs[kind]:
                    rs = sequence_ratios(values)
                    if any(hits(r, targets, tol) for r in rs):
                        any_hit += 1
                row += '   %8.1f%%' % (100.0 * any_hit / len(seqs[kind]))
            print(row)
        print()


def main():
    print(__doc__.split('Stdlib only')[0].strip().splitlines()[0])
    print()
    print('PHI = %.10f' % PHI)
    print()
    print('=== AT LEAST ONE PHI-ADJACENT ADJACENT-RATIO PER SEQUENCE ===')
    print('    in data with no structure in it')
    print()
    for n in (4, 8, 16):
        run(n)

    print('READING THE TABLE')
    print()
    print('  Every cell is a FALSE POSITIVE RATE. It is what a detector')
    print('  reports on noise, with those two parameters chosen.')
    print()
    print('  The two parameters are the whole story. Neither is usually')
    print('  declared, and a search that widens the target set after')
    print('  looking at the data has no null at all -- the family was')
    print('  chosen to contain what was found.')
    print()
    print('  NO PASS STATE. This file does not certify or refute any')
    print('  result. It reports the floor a real finding has to clear.')


if __name__ == '__main__':
    main()
