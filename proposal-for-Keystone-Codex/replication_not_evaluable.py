#!/usr/bin/env python3
"""Proposed replacement for Keystone-Codex's replication criterion.

READ-ONLY. This script does not write to Keystone-Codex. It reads the corpus
and shows what the proposed change would do.

THE DEFECT. rules/keystone_rules.json v1.1:

    replication   ">= 2 regions INDEPENDENTLY"       weight 0.14

`src/prove.py::_c_replication` implements this as `v >= thr` on an integer.
The word carrying the entire load is INDEPENDENTLY -- and establishing it for
one entry took two filed documents and still came back split into practice
level and recognition level.

**A schema that accepts a bare integer for that quantity is the surface-token
class at the schema level**: the criterion is operationalized by the variable
that is easy to store.

THE FIX, and it is one type change plus one return value.

    replication_regions: integer
        ->
    replication_regions: integer
    replication_basis:   string, REQUIRED when replication_regions >= 2

    _c_replication returns PASS / FAIL / NOT_EVALUABLE
    NOT_EVALUABLE when the basis is absent.

NOT_EVALUABLE is not FAIL. An entry with no basis has not been shown to miss
the bar; it has not been measured against it. Same distinction as
`instrument/guarded_count.py`'s DETECTOR_BLIND, and the same reason: a
missing measurement must not be usable as a value.

WHY A DOCUMENTATION FIX WOULD NOT WORK. v1.1's own revision note diagnoses
v1.0 as scoring "four numbers typed by hand" -- and v1.1 fixed it by adding
three evidence criteria ALONGSIDE the four, not by backing them. The naming
was correct and the rate did not move. See REMEDIES.md.

PRECEDENT INSIDE THE SAME RULE SET. The longevity criterion already does
this: ">= 300 years durable or revivable; WHERE THE FIGURE IS NOT DERIVABLE
FROM THE ERA, THE ENTRY MUST DECLARE A longevity_basis". Seven entries carry
one. The mechanism exists; it was applied to one metric of four.

CC0. Stdlib only.
"""

import json
import glob
import os
import sys

NOT_EVALUABLE = 'NOT_EVALUABLE'


def c_replication_current(entry, threshold=2):
    """What prove.py does today."""
    v = entry['metrics'].get('replication_regions', 0)
    return ('PASS' if v >= threshold else 'FAIL'), 'replication_regions=%s' % v


def c_replication_proposed(entry, threshold=2):
    """PASS / FAIL / NOT_EVALUABLE. A count without a basis is not a reading."""
    v = entry['metrics'].get('replication_regions', 0)
    basis = entry.get('replication_basis')
    if v < threshold:
        # Below the bar is a real result and needs no basis to be one:
        # the entry is not claiming the regions.
        return 'FAIL', 'replication_regions=%s' % v
    if not basis or not str(basis).strip():
        return NOT_EVALUABLE, ('replication_regions=%s asserted, no '
                               'replication_basis' % v)
    return 'PASS', 'replication_regions=%s; basis present' % v


def main(root):
    files = sorted(glob.glob(os.path.join(root, 'data', '*', '*.json')))
    if not files:
        print('no entries found under %s/data/*/*.json' % root)
        return 2

    counts = {'PASS': 0, 'FAIL': 0, NOT_EVALUABLE: 0}
    changed = []
    for f in files:
        with open(f) as fh:
            e = json.load(fh)
        if 'metrics' not in e:
            continue
        now, _ = c_replication_current(e)
        new, why = c_replication_proposed(e)
        counts[new] += 1
        if now != new:
            changed.append((e['id'], now, new, why))

    total = sum(counts.values())
    print('Keystone-Codex, read-only.  entries with metrics: %d' % total)
    print()
    print('  under the PROPOSED criterion')
    for k in ('PASS', 'FAIL', NOT_EVALUABLE):
        print('    %-15s %3d   (%.0f%%)' % (k, counts[k], 100.0 * counts[k] / total))
    print()
    print('  entries whose verdict CHANGES: %d' % len(changed))
    print('    every one moves PASS -> NOT_EVALUABLE. None moves to FAIL.')
    print('    Nothing here says an entry misses the bar. It says the bar')
    print('    was never applied.')
    print()
    for eid, now, new, why in changed[:6]:
        print('    %-28s %s -> %s' % (eid, now, new))
    if len(changed) > 6:
        print('    ... and %d more' % (len(changed) - 6))
    print()
    print('  THE SCORING CONSEQUENCE IS THE POINT, NOT A SIDE EFFECT.')
    print('  A NOT_EVALUABLE criterion must not silently score 0 (that')
    print('  penalises an entry for a missing field) and must not score')
    print('  its weight (that is the current behaviour). The aggregate')
    print('  itself becomes NOT_EVALUABLE until the basis exists --')
    print('  which is the no-PASS-state move applied to a rule set.')
    print()
    print('  That %d of %d entries land there is not an argument against'
          % (counts[NOT_EVALUABLE], total))
    print('  the change. It is the measurement of how much of the corpus')
    print('  currently scores on an unbacked integer, and it is what')
    print("  v1.1's own revision note predicts.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1
                          else '/home/user/Keystone-Codex'))
