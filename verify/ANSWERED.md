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
