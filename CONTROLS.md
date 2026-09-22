# Positive controls — and a status change across every negative result here

## The generalizable form

    A negative from an UNCONTROLLED detector carries no information about
    the world. Only about the detector. And you cannot tell which without
    the control.

**Why controls work *here specifically*, which is stronger than "run
controls":**

The only thing that has ever reliably caught the proxy-substitution class in
this programme is **a magnitude violating expectation** — 96 `short-term`
hits, an all-clear on 23 terms, 0-vs-3 on `vibrotactile`. Three instances,
one mechanism. And it has a hard precondition:

    it requires a QUANTITY to exist. A qualitative failure produces no
    arithmetic, and nothing looks wrong.

**A positive control is the first designed version of that detector. It
manufactures the quantity on purpose instead of waiting for one to show
up.**

That is the whole argument. Not "controls are good practice" — *this
programme's only working detector is accidental, and a control is the same
detector run deliberately.*

## STATUS CHANGE — a set moves to UNRATED

**None of these become wrong. They become UNRATED**, which is a different
thing and is not a retraction of any member.

| negative result | status |
|---|---|
| avenue F gap (no benchmark scores speaker attribution) | **UNRATED** — no control run |
| the haptic EN-13725 empty cell | **UNRATED** — one negative search, no control |
| the 0/3 fabrication-discipline grep | **already retracted** on other grounds; was also uncontrolled |
| `DESIGNED_NOT_SPECIFIED` zero-hit scan | **RATED** — see below |
| TT-4 standards thread | **PARTLY RATED** — see below |
| the sensory-taxonomy gap (no corpus has a sensory bin) | **UNRATED** — two corpora, one search, no control |

**Cheap to fix going forward. Cheap-ish retroactively: rerun each with a
term known to be present.** That is the entire remedy.

## TT-4 — RE-REPORTED with controls

### Control 1 — technical word class
`vibrotactile`, known present locally → **3 hits account-wide**
(`tool-off-metrology` ×2, `Simulators` ×1). **Detector sees technical words
in markdown.**

### Control 2 — standards-number class
`ISO 12944`, ground-truthed locally to
`Bio-Grid/Electromagnetic-energy-harvesting/Framework-design.md` →
`"12944"` account-wide returns **that exact file**, plus coincidental CSV
numerics. **Detector sees bare 5-digit standards numbers in markdown.**

This is the control the previous report lacked. `vibrotactile` proved the
query *form* worked; it did not prove the search would find **standards
material** if present — different vocabulary, different files. Control 2
closes that.

### Results, with per-term status

| term | account-wide | reading |
|---|---|---|
| `"13725"` | 3 hits — all `boundary_waters` CSVs | string found, **context absent**. RATED. |
| `"13091"` | 2 hits — CSVs | same. RATED. |
| `"11132"` | 4 hits — CSVs, `metrics.json` | same. RATED. |
| `"18436"` | 4 hits — CSVs, `seed_output_pairs.json`, `metrics.json` | same. RATED. |
| `"7029"` | 17 hits — CSVs, equation files, sims | same. RATED. |
| `olfactometry` | 0 | RATED by control 1 (word class). **Absent.** |
| `audiogram` / `audiometric` / `psychophysics` | **query was an OR chain** | **DISCARDED, not reported.** OR chains silently fail here — that is how instance 5 was found. **NOT YET RUN.** |

**A subtlety worth keeping:** for the numeric terms, the searches *returned
hits*. Coincidental ones, but hits — which **proves the string was
findable.** Those negatives were never uncontrolled; they were
**positive-for-string, negative-for-context.** Only `olfactometry` was a true
zero needing an external control.

### TT-4 verdict

**The standards thread is absent account-wide** — rated, for every term
actually run. Three verified-to-search-level findings (EN 13725 as existence
proof, the three-mode taxonomy, ISO 13091's receptor-class decomposition)
exist only in the transcript and in `CALIBRATION.md`.

**Three audiometry terms remain NOT RUN**, because the only query that
touched them used a form known to manufacture zeros.

## The adjacent item — and it is a seam, not a hit

`tool-off-metrology/unnamed-instruments.md` and `experiments.md`:
vibrotactile magnetic-north belts, worn, "for a receptor."

    magnetic-north belts   SENSORY AUGMENTATION -- giving a person a
                           channel they lacked
    the standards thread   the human channel AS METROLOGY for an external
                           system -- EN 13725's panel measuring an odour
                           concentration

**Different measurand. The empty cell stands.**

But: **the account contains human-channel instrumentation work that was
never joined to the human-channel-as-metrology material.** That is the
disciplinary seam appearing *inside one person's repositories* — a smaller
and far more checkable version of the thing `IMPEDANCE.md` claims happens
between fields.

    between fields   Wegener's resolution came from paleomagnetism and
                     marine geophysics, outside the discipline holding
                     the verdict
    inside one       two bodies of human-channel work, same author, same
    account          account, never cross-referenced

The second is checkable in an afternoon. The first took four decades.

## Standing procedure, proposed

    every negative result in this record carries a CONTROL TERM and its
    result, or it is marked UNRATED.

**Narrowed 2026-09-22 — the sharper version of the same rule:**

    POSITIVE CONTROL BEFORE TRUSTING ANY PATTERN-MATCHED ZERO.

Not merely "before any negative." **Specifically before any zero produced by
a pattern layer**, because REGEX-DIALECT MISMATCH is a failure mode of the
engine that is *independent of whether the query was correct*. Four
instances this session: `\|` literal in POSIX ERE; `T-TERM` substring-
matching `short-term`; GitHub `OR` chains silently failing; `(?:...)`
unsupported in `git grep -E`. **In every one the reasoning was sound and the
engine disagreed.** See `PHYSICS-GROUND.md` addendum 2 for why this is a
distinct class from surface-token operationalization.

No negative is reportable without naming the term that proved the detector
could see something. **This programme has run exactly three positive
controls: one by accident (`vibrotactile`), two on purpose (`terra_preta`,
`ISO 12944`), all within one day of noticing the problem.**
