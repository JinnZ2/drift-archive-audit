# verify/ANSWERED — operator answers, one row per item, provenance kept split

Answers arrive relayed. Three things travel together and are **never merged**
into one row: what the operator said, what a relaying session inferred from
it, and what this record then changed. Each gets its own line and its own
grade.

    the operator fields in verify/*.txt stay BLANK.
    an answer is recorded HERE, with its grade. the form stays the index.

---

## BG-OPEN-1 — bio-grid, self-healing interval

**The item, as the form asked it:**

    self-healing interval: base64 says 2 minutes, both hex blobs say 20 min
    - which is the target? | operator:

**Operator, verbatim:**

    "whatever the capabilities of the AI model at that time"

    grade: operator memory, 2026-09-23. OBSERVED (hers).

**Relaying session's reading, kept separate:**

    interval is RENDERING, not TARGET                        DERIVED
    2 min vs 20 min = two model renderings disagreeing,
    no aim moved between them                                DERIVED
    routing: TOOL-side (capability), not AGENT shaping       DERIVED
    target field for the interval: NOT_OPERATOR_SET          DERIVED

**What this record changes:**

    BG-3 channel      UNATTRIBUTABLE -> TOOL_CANDIDATE
    C-2 status        stays unresolved IN THE CORPUS; the QUESTION dissolves
    new value         NOT_OPERATOR_SET, entered in GLOSSARY.md

---

## 1. THE QUESTION HAD A FALSE PRESUPPOSITION, AND IT WAS MINE

`which is the target?` offers the set `{2 min, 20 min}`. The answer is
outside it. The interval was **never a target field** — so the item is not
answered, it is **dissolved**, and the defect is in the form.

This is the audit's own rule, violated by an instrument the audit built:

    UNSET, UNCLEAR and UNATTRIBUTABLE are valid, explicit values.

The form offered no such value on this line. A two-valued question about a
field that can be unset **pressures toward filling it**, which is the one
thing the work order forbids outright.

## 2. IT IS NOT ONE LINE — MEASURED

Criterion, stated before running: an OPEN item is CLOSED-FORM if its text
presents an explicit alternation the answer must fall inside — `which is` /
`which one`, or `A, or B?`.

    closed-form OPEN items:   7 of 10
    open-form:                3 of 10   (two "how long / how far back",
                                         one "did they exist?")

    answered so far:          1
    answers falling outside
    the offered set:          1 of 1

The criterion **undercounts**: `did they exist?` is a yes/no in substance and
does not match the alternation pattern. The number stands as run; it is not
re-derived after the result.

## 3. THIS IS THE INVERSE OF THE ACCEPTANCE CRITERION

The operator's third criterion for an instrument:

    RETURNS A SET THE READER DIDN'T PICK.

These forms do the opposite on 7 lines: they hand the operator a set **the
audit picked**, and ask them to choose inside it. An instrument that can only
return values its author enumerated cannot report that the author's
enumeration was wrong — which is exactly what BG-OPEN-1 needed to report.

## 4. THE REMEDY IS IN THE FORM, NOT IN THE WORDING

Rewording seven questions is a naming remedy. The structural one is a
standing answer set in the header, admissible on every OPEN line without the
line having to offer it:

    NOT_OPERATOR_SET   the field was never an aim — no value was chosen
    NEITHER            both listed options are wrong
    BOTH               both held, at different times or in different places
    DON'T KNOW         asked and not recoverable from memory
    UNRECORDED         happened, not retained

`DON'T KNOW` already had a precedent inside the forms: `keystone-codex`'s
DIVERGENCE line carries `YES / NO / DON'T KNOW` explicitly. One line of the
three forms had the escape; the other 57 did not.

    verify/*.txt header: rev 2, 2026-09-23. Item text UNCHANGED.
    One item (BG-OPEN-1) was answered under rev 1. Its answer arrived from
    outside the offered set anyway, which is how the defect surfaced.

## 5. WHAT THE ANSWER SETTLES, AND WHAT IT DOES NOT

    SETTLED    the interval was not operator-specified.
               one of the two candidate sources for 2-vs-20 is removed.

    NOT SETTLED
               which model produced which value       UNSET
                 (CORRECTION-001: source model per file is UNSET)
               whether the gap is capability, sampling variance, or two
                 different models                     UNSET
               whether the corpus should now carry one value
                 -> that is a repo decision, not an audit finding, and
                    this audit commits nothing to source repos

So `TOOL_CANDIDATE`, not `TOOL`. The operator's statement establishes the
**absence of AGENT shaping** on this field. It does not establish a tool
mechanism, and the two are not the same measurement.

## 6. AN INDEPENDENT AGREEMENT, WORTH RECORDING BECAUSE IT WAS OUT OF SAMPLE

`BG-3`'s split column has read **`RENDERING conflict`** since commit
`d113f9d`, 2026-09-22 — written from the corpus, before any answer existed.
The operator's answer, 2026-09-23, reaches the same classification from the
other side.

    A5 call:        RENDERING, not TARGET     (from the archive, 09-22)
    operator:       not an aim at all         (from memory, 09-23)

Two sources, no contact between them, same result. That is the first
out-of-sample confirmation of an A5 classification in this audit. **n = 1**,
and it is one line, not a rate.

---

## EA-OPEN-2 — emotions-as-sensors, three licences in the root tree

**The item, as the form asked it:**

    three licences in the root tree (MIT-with-attribution /
    attribution-required / CC0-without-attribution) - which one is real?
    | operator:

**Operator:**

    aim at root = CC0

    grade: operator memory, 2026-09-23. OBSERVED (hers).

**Relaying session's reading, kept separate:**

    CC0 is TARGET; the other two are renderings that didn't match it   DERIVED
    target held from root through today's "all CC0" — the aim never
    moved, the renderings drifted around it                            DERIVED

**Answer-set note:** this one landed **inside** the offered set. `BG-OPEN-1`
did not. Running count: **2 answered, 1 outside the set.** The form defect in
`GUESSED.md` #39 stands; it is not universal, and the rate is n = 2.

## 1. INDEPENDENTLY CORROBORATED — the canonical slot never moved

    Emotions-as-Sensors  LICENSE  blob at root  66b468e1f97e98096a7ce7103206990a39cd0c86
                         LICENSE  blob at HEAD  66b468e1f97e98096a7ce7103206990a39cd0c86
                         first line, both:      CC0 1.0 Universal Public Domain Dedication

**Byte-identical across 123 commits.** `VERIFIED` by this session against the
archive, and it was not asked for — it is the second `BG-7` shape in the
pilot: the slot that carries the target is the one nothing touched.

The operator's answer and the archive agree, and were produced without
contact. **Second out-of-sample confirmation** (after `BG-3`). n = 2.

## 2. THE DRIFT IS NOT AWAY FROM THE AIM — IT IS ACCRETION AROUND A STATIONARY ONE

    site class                          root    HEAD    delta
    canonical LICENSE = CC0              yes     yes    byte-identical
    files carrying "CC0"                   9      48    +39
    "no attribution required" /
      "without attribution" statements     1       6     +5
    bare-MIT project claims                4       4      0
    "attribution required" /
      "with attribution" claims            4       4      0

    bare-MIT sites, root AND HEAD, same text, 14 months apart:
        README.md:152   "released under the MIT License ... with attribution"
        README.md:300   "Released under the MIT License."
        sensors/README.md:100  "MIT License. Open-source, symbolic..."
        src/ucm_monitor.py:14  "License: MIT (belongs to the commons)"
                               (at root: ucm_monitor.py:14 — file moved, text did not)

    attribution-required sites, all four in README.md, root AND HEAD:
        :138 / :294  "Attribution required: Developed by JinnZ2 and
                      Claude and ChatGPT"   (":281/:136" at root)
        :152 / :301  "Free to use, adapt, and distribute with attribution."

**The aim spread 5x. The contradicting renderings were never removed — not
one, in 14 months.** The correction propagated by *addition*: 39 new files
saying CC0, alongside four original sites still saying MIT, untouched.

That is `BG-8`'s shape in a second repo — *"root files still byte-identical
and still carrying a withdrawn figure with no marker in-file."* **D3-adjacent:
a status field that was never applied to the original site.** Two repos, two
domains, same mechanism. Recorded as a Phase B candidate, **not** a confirmed
spanning frame: n = 2 and both were found by looking for them.

## 3. THE CORPUS'S OWN REVIEW FOUND 2 OF 3 AND AIMED THE FIX AT A FILE WITH NOTHING IN IT

`REVIEW.md` §1.2 is titled *"License contradiction — MIT vs CC0"*. It is
already in the tree. Measured against the four sites:

    REVIEW.md:40  names README.md and src/ucm_monitor.py       2 of 3 files
    sensors/README.md:100                                      NOT NAMED
    REVIEW.md:66  "Audit src/emotions_playground.py header
                   for similar MIT strings"                    that file has
                                                               NO MIT string

So the conflict was found, written up, given a remedy — and the remedy has
not been applied to any of the four sites, while one named target is empty
and one real target is missing. **A correction can be present in the tree and
still not reach the site.** Findability, inside the corpus, not this audit's.

## 4. MY OWN COUNT WAS WRONG FIRST, AND THE CONTROL CAUGHT IT

First pass counted files matching `with attribution|attribution required`:
**1 at root, 5 at HEAD**, and was about to be reported as *"the contradicting
rendering grew."*

Three of those five say **"No attribution required"** — they AGREE with CC0.
The regex counted agreement as contradiction. Correct figures are in §2:
contradiction 4 → 4, agreement 1 → 6. The growth was on the target's side.

    a count with no polarity control, run in the session that built
    guarded_count.py for exactly this.

Caught by reading the matched lines instead of the match count — which is the
one habit the timeout finding turned into procedure. Logged: `GUESSED.md` #40.

## 5. WHAT IS NOT SETTLED, AND IS NOT SETTLED HERE

    Symbolic-Swarm-Index's own licence     ROUTED, NOT DECIDED

`Symbolic-Swarm-Index/LICENSE.md` is a deliberate **MIT + CC0 "Gift
Protocol"** with its own FAQ arguing the pairing on the merits; `CLAUDE.md`
describes the directory as a self-contained subsystem with its own schemas,
demos and docs. Eight of the twelve HEAD files mentioning MIT are describing
*that* licence accurately.

Two readings, both supported by the archive:

    (a) "all CC0" covers the whole tree -> SSI's dual licence is a
        rendering that does not match
    (b) SSI is a separately-licensed subsystem, deliberately -> its
        licence is its own target, and the tree has two aims, not one

**Nothing here picks one.** This audit commits nothing to source repos, and
choosing between (a) and (b) is settling a question by fiat. It is the one
place the answer to `EA-OPEN-2` does not reach.

    SSI scope: UNSET. Routed to the operator.
