#!/usr/bin/env python3
"""Enum sweep — a bounded list that converts FIND into a reading task.

WHY. Four of this audit's derivations were instruments the corpus already
held, and none was found by search (FINDABILITY.md). A search needs a term,
and the term is exactly what the searching side does not have. The FIND job
therefore required a party fluent in both vocabularies -- declared the
scarcest constraint on the list.

An enum does not need a term to find. It is a CLOSED SET someone wrote down
because the distinctions in it mattered enough to enumerate. Collecting all
of them is mechanical, and a corpus has far fewer enums than terms.

    FIND, before   needs a party fluent in both vocabularies
    FIND, after    needs a party who will read a bounded list
                   -> reader-side. Substitutable.

WHAT IT DOES NOT DO. It does not tell anyone what an enum means, which one
matters, or what is missing from their own vocabulary. It hands over a list.
The reading is the part that is not automated and is not automatable here.

BOUNDEDNESS IS THE CLAIM UNDER TEST, not an assumption. The sweep reports the
total. A list too long to read is a failed instrument even if every entry is
correct, so the number is printed first.

POSITIVE CONTROL, per standing rule. The sweep must recover the one enum
already known to have been missed: Keystone-Codex's evidence-type enum, whose
non-assertion members (`field_measurement`, `oral_tradition_encoded`,
`replication_record`, `engineering_record`) are what should have produced the
ENACTED provenance grade hours before it was derived as new.

**If the control does not fire, the run ABORTS and no list is printed.** A
sweep that cannot recover a known instance says nothing by returning few.

NO PASS STATE. The output is a list and a count.

CC0. Stdlib only.
"""

import json
import os
import re
import sys

# The control: an enum containing these members must be recovered.
CONTROL_MEMBERS = {'field_measurement', 'oral_tradition_encoded',
                   'replication_record', 'engineering_record'}

SKIP_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv',
             '.pytest_cache', 'dist', 'build'}

# Python: a module-level constant bound to a literal collection of strings.
#
# DELIBERATELY NOT ONE REGEX. The first version of this used a nested
# quantifier -- ((?:\s*"[^"]+"\s*,?\s*)+) -- which backtracks catastrophically
# on a long non-matching line and hung the run past 120 seconds. It is left
# recorded rather than silently replaced: it is the MATCH-UNIT family again,
# this time failing on cost rather than on correctness, in the instrument
# built to make FIND cheap.
PY_OPEN = re.compile(r'^([A-Z][A-Z0-9_]{2,})\s*=\s*([\(\[\{])', re.MULTILINE)
PY_LITERAL_OPEN = re.compile(r'Literal\[')
STR_ITEM = re.compile(r'["\']([^"\']{1,200})["\']')
CLOSERS = {'(': ')', '[': ']', '{': '}'}
MAX_BODY = 4000          # characters scanned forward for a closing bracket
MAX_FILE = 2_000_000     # bytes; larger files are skipped and counted


def walk_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            yield os.path.join(dirpath, fn)


def json_enums(path, obj, trail, out):
    """Every "enum": [...] in a JSON document, with the key path that holds it."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'enum' and isinstance(v, list) and all(
                    isinstance(x, (str, int, float)) for x in v):
                out.append((path, '.'.join(trail) or '(root)',
                            tuple(str(x) for x in v)))
            else:
                json_enums(path, v, trail + [str(k)], out)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            json_enums(path, v, trail + ['[%d]' % i], out)


def _body_after(text, start, closer):
    """Slice from start to the matching closer, bounded. Linear, no backtracking."""
    end = text.find(closer, start, start + MAX_BODY)
    return text[start:end] if end != -1 else None


def python_enums(path, text, out):
    for m in PY_OPEN.finditer(text):
        body = _body_after(text, m.end(), CLOSERS[m.group(2)])
        if body is None or '\n\n' in body:
            continue
        items = tuple(STR_ITEM.findall(body))
        if len(items) >= 2 and len(items) == body.count(',') + 1 - body.count(',,'):
            out.append((path, m.group(1), items))
        elif len(items) >= 2 and ':' not in body:
            out.append((path, m.group(1), items))
    for m in PY_LITERAL_OPEN.finditer(text):
        body = _body_after(text, m.end(), ']')
        if body is None:
            continue
        items = tuple(STR_ITEM.findall(body))
        if len(items) >= 2:
            out.append((path, 'Literal[...]', items))


def sweep(roots):
    found = []
    for root in roots:
        if not os.path.isdir(root):
            continue
        for path in walk_files(root):
            low = path.lower()
            try:
                if low.endswith('.json'):
                    with open(path, encoding='utf-8') as fh:
                        json_enums(path, json.load(fh), [], found)
                elif low.endswith('.py'):
                    if os.path.getsize(path) > MAX_FILE:
                        continue
                    with open(path, encoding='utf-8', errors='replace') as fh:
                        python_enums(path, fh.read(), found)
            except (ValueError, OSError):
                continue
    return found


# DECLARED MEMBER CRITERION, statable in advance and independent of what is
# found: an enum is a closed set of SHORT IDENTIFIER-LIKE values. A prose
# sentence is not an enum member under any reading. This is a filter on FORM,
# not on content, and both counts are reported so it stays auditable.
MEMBER_MAX = 60


def is_enum_like(members):
    if len(members) < 2:
        return False
    for m in members:
        if len(m) > MEMBER_MAX or '\n' in m or '. ' in m:
            return False
    return True


def control_fires(found):
    for _, _, members in found:
        if CONTROL_MEMBERS.issubset(set(members)):
            return True
    return False


def main(argv):
    roots = argv[1:] or [
        '/home/user/Keystone-Codex',
        '/home/user/AI-Consciousness-Sensors',
        '/home/user/Emotions-as-Sensors',
        '/home/user/Bio-Grid-American-Manufacturing-',
    ]
    found = sweep(roots)

    if not control_fires(found):
        print('CONTROL FAILED. The evidence-type enum was not recovered.')
        print('Required members: %s' % sorted(CONTROL_MEMBERS))
        print('ABORTED — no list printed. A sweep that cannot recover a')
        print('known instance says nothing by returning few.')
        return 2
    print('POSITIVE CONTROL: FIRED. The known-missed enum was recovered.')
    print()

    # Deduplicate by member set: the same enum restated in two files is one
    # distinction, not two.
    def dedupe(rows):
        d = {}
        for path, key, members in rows:
            d.setdefault(frozenset(members), []).append((path, key, members))
        return d

    all_sets = dedupe(found)
    kept = [r for r in found if is_enum_like(r[2])]
    kept_sets = dedupe(kept)

    print('BOUNDEDNESS — the claim under test, reported before the list')
    print('  roots swept                 %d' % len([r for r in roots
                                                    if os.path.isdir(r)]))
    print('  enum occurrences found      %d' % len(found))
    print('  distinct member sets        %d' % len(all_sets))
    print('  removed by the declared member criterion  %d'
          % (len(all_sets) - len(kept_sets)))
    print('  DISTINCT SETS TO READ       %d   <- the number that decides'
          % len(kept_sets))
    print('                                     whether this is bounded')
    print()
    print('  The removed rows are prose constants and regex tables caught by')
    print('  the Python channel -- module-level string collections that are')
    print('  not closed sets. The criterion is on FORM (member length, no')
    print('  sentence punctuation), was statable before the run, and both')
    print('  counts are printed so the filtering is auditable.')
    print()
    by_members = kept_sets

    rows = sorted(by_members.items(), key=lambda kv: (-len(kv[1]), len(kv[0])))
    for members, occurrences in rows:
        path, key, ordered = occurrences[0]
        rel = path.replace('/home/user/', '')
        print('  [%d file%s] %s :: %s'
              % (len(occurrences), '' if len(occurrences) == 1 else 's',
                 rel, key))
        print('      %s' % ', '.join(ordered))
    print()
    print('NO PASS STATE. This is a list. It does not say which of these')
    print('matters, what any of them means, or what is missing from the')
    print("reader's own vocabulary. That reading is the part that is not")
    print('automated here, and it needs A party, not THE party.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
