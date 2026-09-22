#!/usr/bin/env python3
"""Reachability sweep — narrowed successor to the retracted cache-dependency detector.

WHAT THE RETRACTED ONE DID WRONG (GUESSED.md #10): it asked "is this term
DEFINED?" — a comprehension judgement — and answered it with a surface
heuristic (a definitional cue near a table pipe or heading). Every file here
is tables and headings, so it returned an all-clear on 23 of 23 terms. An
all-clear is the worst possible output shape: it stops further checking.

WHAT THIS ONE ASKS INSTEAD. A strictly narrower, mechanical question:

    REACHABILITY: does a definition keyed by this exact term EXIST anywhere
                  a reader of this document can get to?

Not "does the definition suffice." Sufficiency is still the prescribed test
in GLOSSARY.md — hand a section to a cold reader and see where they stop —
and it is still unrun, and still needs a second party.

DESIGN CONSTRAINT, stated so it can be checked: THIS INSTRUMENT HAS NO PASS
STATE. Its output is a list of terms and their reachability status. It
cannot return "all clear", because the thing it measures is not the thing
that would justify one.

Four controls run on every invocation and the run aborts if any fails.

TWO CONSTRUCTION DEFECTS, FOUND ON THE FIRST RUN AND LEFT DOCUMENTED RATHER
THAN TUNED AWAY. Both are the class this corpus already named: MATCH-UNIT
MISMATCH, granularity sub-form (`CONTROLS.md`).

  DEFECT 1 -- the HAS_ENTRY / NO_ENTRY split is UNRATED and must not be read
  as a reachability rate. The extractor's unit is a whole backtick span or a
  whole ALL-CAPS run; the glossary's unit is a bare term. So
  `reconstruct/CORRECTION-001.md` never matches the key `CORRECTION-001`,
  and `TRANSPORT CONFOUND` never matches `TRANSPORT*MODEL`. First run on
  STUDY.md: HAS_ENTRY = 1 of 108, while 10 glossary keys were verified
  present in the text as substrings and extracted as candidates by neither
  channel. CAUGHT BY QUANTITY -- 1 of 108 is not a believable reachability
  rate for a document written by the party that wrote the glossary.

  DEFECT 2 -- the key splitter, see glossary_keys(). Caught before it fired.

WHAT SURVIVES BOTH DEFECTS, because neither touches it:

  * the POINTER check -- an exact string search for the glossary's filename,
    reported as a line position, not a verdict;
  * the FILE_ABSENT list -- exact path resolution. It does NOT distinguish
    "broken reference" from "lives in a read-only source repo", so it is
    reported as a list and never as a count.

Do not repair DEFECT 1 by loosening the matcher. Substring fallback is the
move that produced the T-TERM error; a fuzzy matcher here would raise
HAS_ENTRY toward a number that looks right and means nothing.
"""

import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

# --- glossary keys: exact lookup, no heuristic --------------------------------

GLOSSARY_ROW = re.compile(r'^\|\s*\*\*(.+?)\*\*\s*\|')


def glossary_keys(text):
    """Return the set of terms GLOSSARY.md defines, one per bolded table key.

    A key like 'A1-A6' or 'target / rendering' covers several surface forms,
    so each key is also split on the separators the glossary uses.
    """
    keys = set()
    for line in text.splitlines():
        m = GLOSSARY_ROW.match(line)
        if not m:
            continue
        raw = m.group(1).strip()
        keys.add(raw)
        for part in re.split(r'\s*(?:/|,|…|\.\.\.)\s*', raw):
            part = part.strip().strip('`')
            # DEFECT 2, caught before it fired. Splitting a compound key such
            # as 'CALIBRATION MODE 1/2/3' on its separators yields the bare
            # fragments '2' and '3', which would then classify any token '2'
            # as HAS_ENTRY. The splitter's unit (a separator) was not the
            # key's unit (a term) -- the same GRANULARITY mismatch as
            # DEFECT 1 below, one level up. Fragments that are not terms are
            # dropped, and the control in controls() keeps them out.
            if len(part) > 1 and not part.isdigit():
                keys.add(part)
    return keys


# --- candidate terms in the swept document ------------------------------------

BACKTICKED = re.compile(r'`([^`\n]+)`')
ALLCAPS = re.compile(r'\b([A-Z][A-Z0-9_]{3,}(?:[ -][A-Z][A-Z0-9_]{2,})*)\b')

# Words that are ALL-CAPS for emphasis, not terms. Listed explicitly rather
# than filtered by a rule, so the exclusion is auditable.
EMPHASIS = {
    'NOT', 'AND', 'THE', 'FOR', 'BUT', 'ALL', 'ANY', 'ONE', 'TWO', 'ZERO',
    'THIS', 'THAT', 'THEY', 'THEM', 'WITH', 'FROM', 'HAVE', 'ONLY', 'MORE',
    'LESS', 'EVERY', 'NEVER', 'ALWAYS', 'WHICH', 'WHOSE', 'WHERE', 'THERE',
    'AFTER', 'BEFORE', 'CANNOT', 'SHOULD', 'BECAUSE', 'SELECT', 'MOVED',
    'OPEN', 'READ', 'AI', 'WEIRD',
}


def candidates(text):
    """Terms a cold reader might have to look up. Over-collects on purpose."""
    found = set()
    for m in BACKTICKED.finditer(text):
        t = m.group(1).strip()
        if t and not t.startswith(('http', '/', '$')) and len(t) < 60:
            found.add(t)
    for m in ALLCAPS.finditer(text):
        t = m.group(1).strip()
        if t in EMPHASIS:
            continue
        found.add(t)
    return found


# --- classification -----------------------------------------------------------

def classify(term, keys):
    """HAS_ENTRY iff an exact glossary key matches. No fuzzy fallback."""
    if term in keys:
        return 'HAS_ENTRY'
    bare = term.strip('`*').rstrip('.,;:')
    if bare in keys:
        return 'HAS_ENTRY'
    # A filename is reachable if the file exists — a different reachability
    # test, and an exact one.
    if '/' in term or term.endswith(('.md', '.py', '.json', '.jsonl', '.csv',
                                     '.sh', '.txt', '.yml')):
        p = ROOT / bare.rstrip('/')
        return 'FILE_PRESENT' if p.exists() else 'FILE_ABSENT'
    return 'NO_ENTRY'


# --- controls -----------------------------------------------------------------

def controls(keys):
    """Both must hold or the run aborts. A detector that cannot fail is #10."""
    ok = True
    # positive control: a token that is definitionally absent must come back
    # NO_ENTRY. If this passes silently, the classifier is not discriminating.
    seeded = 'ZZZ_SEEDED_CONTROL_TERM'
    if classify(seeded, keys) != 'NO_ENTRY':
        print('CONTROL FAIL: seeded absent term did not classify NO_ENTRY')
        ok = False
    # negative control: a term the glossary demonstrably defines must come
    # back HAS_ENTRY.
    for known in ('STAGE2_LOSS', 'encoding_form'):
        if classify(known, keys) != 'HAS_ENTRY':
            print('CONTROL FAIL: known glossary key %r did not classify '
                  'HAS_ENTRY' % known)
            ok = False
    # extraction control: the seeded token must survive candidate extraction.
    if seeded not in candidates('a sentence containing %s inline.' % seeded):
        print('CONTROL FAIL: seeded term not extracted as a candidate')
        ok = False
    # key-unit control: no key may be a fragment that is not a term. A bare
    # numeral or single character as a key is a false-positive generator --
    # it would mark arbitrary tokens HAS_ENTRY. This is DEFECT 2's guard;
    # it must stay even though the splitter no longer produces them.
    junk = sorted(k for k in keys if len(k) < 2 or k.isdigit())
    if junk:
        print('CONTROL FAIL: non-term glossary keys would generate false '
              'HAS_ENTRY: %r' % junk)
        ok = False
    return ok


# --- report -------------------------------------------------------------------

def main(argv):
    target = pathlib.Path(argv[1]) if len(argv) > 1 else ROOT / 'STUDY.md'
    gtext = (ROOT / 'GLOSSARY.md').read_text(encoding='utf-8')
    ttext = target.read_text(encoding='utf-8')
    keys = glossary_keys(gtext)

    if not controls(keys):
        print('ABORTED — controls did not hold. No result is reported.')
        return 2

    print('reachability sweep')
    print('  swept:    %s' % target.relative_to(ROOT))
    print('  against:  GLOSSARY.md (%d keys)' % len(keys))
    print('  measurand: does a definition keyed by this term EXIST and is it')
    print('             reachable. NOT whether it suffices.')
    print()

    # Pointer check: a glossary is only reachable if the document names it,
    # and where it names it is a position, not a verdict.
    pos = ttext.find('GLOSSARY.md')
    lines = ttext.count('\n') + 1
    if pos < 0:
        print('  POINTER: STUDY.md never names GLOSSARY.md.')
        print('           Every HAS_ENTRY below is unreachable in practice.')
    else:
        ln = ttext[:pos].count('\n') + 1
        print('  POINTER: first mention of GLOSSARY.md at line %d of %d '
              '(%.0f%% in).' % (ln, lines, 100.0 * ln / lines))
        print('           Position is reported, not judged.')
    print()

    buckets = {}
    for term in sorted(candidates(ttext), key=str.lower):
        buckets.setdefault(classify(term, keys), []).append(term)

    for status in ('FILE_ABSENT', 'FILE_PRESENT'):
        print('  %-13s %d   (exact path resolution)'
              % (status, len(buckets.get(status, []))))
    for status in ('HAS_ENTRY', 'NO_ENTRY'):
        print('  %-13s %d   UNRATED -- see DEFECT 1. Not a reachability rate.'
              % (status, len(buckets.get(status, []))))
    print()
    for status in ('FILE_ABSENT', 'NO_ENTRY'):
        items = buckets.get(status, [])
        if not items:
            continue
        label = {'FILE_ABSENT': 'FILE_ABSENT  (does not resolve in THIS repo; '
                 'does not distinguish a broken reference from a path in a '
                 'read-only source repo -- listed, never counted)',
                 'NO_ENTRY': 'NO_ENTRY  UNRATED, listed for a reader, not '
                 'summed'}[status]
        print('  --- %s ---' % label)
        for t in items:
            print('    %s' % t)
        print()

    print('  NO PASS STATE. This run reports a list. It does not certify')
    print('  the document, and an empty NO_ENTRY bucket would mean only')
    print('  that every extracted token had a keyed entry.')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
