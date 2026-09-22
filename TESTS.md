# Tests reported

Pilot: Bio-Grid-American-Manufacturing- (63 commits), Keystone-Codex (27),
Emotions-as-Sensors (123). Root commits 2025-07-10, 2025-08-28, 2025-12-15.
All A2 hashes written before any A3 read — see `ledger/commits.jsonl`.

---

## T1  attractor persistence across dates

Measured as: does the WHOLE_STATED encoding of each target survive unedited?

| repo | artifact | root blob | HEAD blob | verdict |
|---|---|---|---|---|
| Bio-Grid | `docs/trust_model.md` | `c4a2523` | `c4a2523` | **byte-identical**, 63 commits, 14 months |
| Emotions | `docs/field-english.md` (was `FIELD_ENGLISH.md`) | — | R100 rename | content preserved |
| Emotions | `docs/transition-rules.md` guards | — | — | unchanged, intact |
| Keystone | — | — | — | no WHOLE_STATED artifact exists (frame is PIECE) |

**The earliest renderings persisted. Later renderings moved.** In every case
where the frame was written down once, whole, it was never touched — including across
the 2026-03-22 tooling boundary and the agent-era rewrites.

Under CORRECTION-001 this is a claim about blob identity, not about the
operator's aim: non-revision is equally consistent with the rendering being
right, with it never being re-examined, and with there being no operator
vocabulary in the archive to revise it with.

Tool vs agent split: **not available**. The 2026-03-22 boundary is
`TRANSPORT×MODEL` — manual paste vs agent commit, confounded with a change of
model — and nothing in the archive varies one while holding the other. C-5 records that the archive holds no
experiment with content fixed across the regime boundary. Authorship is
recorded per commit (JinnZ2 vs Claude) and the divergence tables are split by
it, but authorship is not a channel.

---

## T2  stage-2 loss rate — falsified renderings that took their target with them

Falsified or withdrawn renderings identified: **6**

| # | rendering | falsified | target survived? |
|---|---|---|---|
| 1 | `$85B / 275k jobs / 340% ROI / 99.95% / 500 H100` | 2026-08-14 | YES — target never rested on them |
| 2 | `φ = 1.618` as the single "base tuning constant" | 2026-08-14 | YES — recovered as two couplings |
| 3 | `W(t+1)=φW(t)+ΔL(1-φ)` at φ=1.618 | 2026-08-14 | YES — corrected to φ⁻¹ for decay |
| 4 | Keystone rules v1.0 | 2026-08-17 | YES — v1.1 extended it; v1.0 kept runnable in `legacy/` |
| 5 | `morphic resonance` (term) | 2026-05-14 | YES — renamed Non-Local Pattern Correlation Sensor, measurand retained |
| 6 | 8 duplicated `os.walk` loaders | 2026-08-14 | YES — consolidated to `corpus.py` |

    STAGE2_LOSS: 0 of 6.

**No falsified rendering took its target with it.** In four of the six the
superseded rendering was deliberately kept runnable or archived rather than
deleted (`legacy/`, `legacy/reports/`, rules v1.0).

Caveat: this counts renderings that were *found and marked*. A rendering that
was silently dropped would not appear here. T2 measures the handled cases.

---

## T3  status-field decay — first vs last commit

Corpus-wide, files containing each category, normalised per 100 files:

| category | bio-grid | keystone | emotions |
|---|---|---|---|
| UNSET / UNKNOWN / UNCLEAR | 0.0 → 8.7 | 0.0 → 19.8 | 18.9 → 33.5 |
| conditional / guard / threshold | 12.9 → 20.1 | 53.3 → 60.4 | 24.4 → 68.5 |
| provenance / evidence_refs / DOI | 3.2 → 26.8 | 100 → 207 | 22.6 → **19.7** |
| assumption / speculative / unvalidated | 4.8 → 47.7 | 0.0 → 128 | 6.1 → 24.4 |
| falsified / superseded / withdrawn | 0.0 → 55.7 | 0.0 → 183 | 1.2 → 49.6 |

**The predicted decay is not observed. Every category rises but one.**

The single decline is Emotions' provenance rate (22.6 → 19.7 per 100 files),
and in absolute terms it rose (37 → 50 files) while the corpus grew faster.
At the sensor level it is flat: 4/51 → 5/55 carry `provenance`.

Three named status fields DID decay, and the corpus-level counts hide them:

| field | fate |
|---|---|
| Keystone `ethical_alignment` | populated in every entry since t=0, scored by nothing for 13 months |
| Keystone longevity margin | the uncertainty carried in the discount below era-span: **38% → 5%** (see T-extra) |
| Emotions `decay_model` mapping | 5 files at root, 5 at HEAD — never spread; the relation reappeared as prose in strings instead |

**Status-field vocabulary grew; specific status fields that had no type to
hold them decayed.** The counting metric and the mechanism point opposite
ways. Report both.

Method caveat: these are lexical proxies over file counts. Keystone's
provenance figure exceeds 100 per 100 files because `evidence_refs` and
`source:` recur inside every entry. Treat as direction, not magnitude.

---

## T4  noun resolution — relation-first framing → entry/node structure

| repo | the relation | how it resolved | measured |
|---|---|---|---|
| Keystone | `unlocks` | into 15 bare nouns with no referent at t=0 | **closure 0% → 44%** (40 of 90 edges resolve at HEAD; 50 still dangling) |
| Emotions | `decay_model` (condition → law) | into a single-valued attribute | mapping 5/51 → 5/55; string 38 → 39, now holding **29 distinct free-text values** |
| Bio-Grid | φ (geometry coupling, decay coupling) | into ONE noun, "the BioGrid base tuning constant" | 2 constants → 1 symbol at t=0; re-split after ~13 months |

**Three instances, three different outcomes:**

- Keystone: the nouns were **built into entries**. The relation is being
  closed, not dropped. Target advancing.
- Emotions: the relation **came back as prose inside the attribute**. Meaning
  retained, machine-readability lost. `elder-sensor.schema.json` keeps
  `oneOf: [string, object]` and calls it backward compatible — the mapping
  form was defended, not abandoned.
- Bio-Grid: the collapse **propagated into a recursion** and made it diverge
  geometrically, until corrected.

Noun resolution occurred in all three. It was reversed in two and is being
reversed in the third.

---

## T5  present-model drift (Phase D4)

**NOT REPORTED.** Phase D is blocked on the A6 forms. See `PHASE_D.md`.
One unprompted observation is logged there and is explicitly not a T5 result.

---

## T6  encoding effect — drift rate by encoding_form

| encoding_form | instances in pilot roots | drifted | held |
|---|---|---|---|
| WHOLE_STATED | 4 | **0** | 4 — one byte-identical for 14 months |
| DEMONSTRATED | many | 0 observed | `this.phi = 1.0008` held while the prose that described it did not |
| PIECE_ONLY | 5 | 0 | preserved `1.0008` against the prose (C-1) |
| MODEL_VOCAB_PROSE (was REWORDED_TO_MODEL_VOCAB) | ~12 files (Bio-Grid), ~4 (Emotions) | **all 6 falsified renderings in T2 originate here** | — |
| PURE_INSTRUCTION | 4 | n/a | n/a |

**Every falsified rendering in this pilot originated in MODEL_VOCAB_PROSE.
None originated in WHOLE_STATED, DEMONSTRATED or PIECE_ONLY.**

Under CORRECTION-001 the category is renamed: all root content is model
vocabulary, so there is no rewording *from* an operator register to detect.
What the five values still separate is real — different FORMS of rendering —
and the counts are unaffected.

Three things must be said against over-reading that:

1. It is expected by construction. REWORDED is where claims-about-the-world
   live, and only claims-about-the-world can be falsified. A guard condition
   or a hex token has no truth value to lose.
2. n is small: 3 repos, 6 falsified renderings.
3. Under CORRECTION-001 the forms may not be comparable at all: different
   files may be output from different models, so "encoding_form" is
   confounded with "which model produced this file". C-1, the one experiment
   that held content fixed, is downgraded for exactly this reason — see
   `PHASE_C.md`.

**T6 therefore reports a correlation with no isolated cause.** Falsified
renderings cluster in prose. Whether that is a property of the encoding or of
the models that produced prose cannot be separated in this pilot.

---

## T-0  the audit's own error mode

Reported as a finding, not only as retraction #5 in `GUESSED.md`.

A regex defect (`git grep -E` with backslash-escaped pipes, which are literal
in POSIX ERE) produced a table of zeros. Those zeros **agreed with the
hypothesis under test** — that parallel and always-on were unfiled. The
reading was written up as confirmation. It was caught only when an unrelated
check on a different term returned a nonzero count that contradicted the
table.

    the audit's own error mode was confirmation-shaped, and was not
    caught by any check aimed at it

No verification step in this audit was pointed at that failure. The catch
came from an unowned join between two measurements, which is the same
mechanism the corpus studies: **a locally correct component whose error is
invisible from inside and surfaces only where nobody is looking.**

Nine retractions are on the record in `GUESSED.md`, under **three** catch
columns, not one ratio:

    self-caught        4   of which one (#5) came from an unowned join
                           between two measurements, not from any check
                           aimed at it
    operator-caught    3
    cross-party-caught 2   required a party outside BOTH the operator and
                           this session

**Self-catch is 4 of 9.** The original "four of six" merged the operator
and cross-party columns; corrected here. The cross-party column is the one
that argues for handing scoring outward — those two would not have been
caught by either party inside the work.

A tenth was caught within a turn and never published: a grep for the
*implementation* markers of a discipline (`sha256`, `retained unmodified`)
returned 0/3 and nearly became "the discipline does not appear in
fabrication material". It appears there stated as principle rather than
mechanism. **Same failure mode as #5 — operationalizing a concept by its
surface tokens.** Twice now, in the same audit.

## T-0b  substituting the observable proxy for the concept — a closed count

**Recorded before the discriminators ran, which makes it a committed
prediction rather than a post-hoc fit. Count CLOSED at 2026-09-22 and
contaminated from here on** — this session is now looking for it, so
instances 4+ are not independent.

### The taxonomy, corrected

    PARENT        substituting the observable proxy for the concept
    SPECIAL CASE  surface-token operationalization (the mechanical form)

The first framing counted only the special case. Corrected:

| # | instance | class | caught |
|---|---|---|---|
| 1 | regex `\|` searched literal strings; the resulting zeros **agreed with the hypothesis under test** | special case | after reporting, by an unrelated nonzero count |
| 2 | pilot selection: **age** proxied for articulation density | **parent** | after 5 findings landed outside it |
| 3 | fabrication-discipline grep: searched *implementation* markers, got 0/3, nearly concluded the discipline was absent | special case | within-turn, unpublished |
| 4 | cache-dependency detector: heuristic matched any table or heading; returned **all-clear on 23 terms** | special case | within-turn, by implausibility |
| 5 | emptiness → value: **follower count** proxied for terrain | **parent** | by a second party |
| 6 | `T-TERM` grep, case-insensitive substring: 96 hits, all `short-term` | special case | pre-report, by implausibility |

    total 6     parent 2     special case 4
    caught after reporting 3     caught pre-report 3

    ^ 6 IS A FLOOR. ONE-SIDED. DIRECTION KNOWN.  (see immediately below --
      this is part of the count, not a caveat appended to it)

**Two of the three pre-report catches came from an implausible NUMBER
contradicting expectation, not from any check aimed at the failure.** Same
mechanism as T-0's unowned join. **No check in this audit detects this class
directly.**

### The only working detector has a hard scope limit, and it biases the count

The audit's sole reliable detector for this class is
**expectation-violation on a magnitude** — which nobody designed, which is
in no checklist, and which requires:

    a QUANTITY that can look implausible.

A **qualitative** claim operationalized by surface tokens produces no
arithmetic. **Nothing looks wrong.** Every catch to date is in the subset
that happened to produce a number.

**So the 6-instance count is sampled on the same variable that made the
instances visible.** Instances producing no countable output are absent from
it by the same mechanism that revealed the others.

    6 is a FLOOR, the bias is ONE-SIDED, and the direction is KNOWN.

This is not a caveat on the count. **It is a property of the count**, and it
is stated inside it above rather than appended after it — because a caveat
appended after a number is exactly the shape that gets dropped in transit
(the Lave failure, `GUESSED.md` #7).

### What it does and does not establish

**Does not** separate statistical from structural. All six are one model
family, one session, same corpora — exactly the confound arm 3 exists to
break. A second party reports the same class twice in the same window, which
adds instances but not independence.

**Does** remove one alternative explanation before the arms run: the
observable is **not an artifact of the agentic surface**, since it appears in
both an agentic session and a non-agentic one.

### Evidence class — the weakest in the programme

This is **a self-report by an instrument about its own failure mode.** It is
not observation. It belongs in the work order as a **recorded prior**, with
arm 3 as the actual measurement, and **the number marked as not independent
of the party reporting it.**

Third instance of the T-0 structure: the session is a data point in the study
it is specifying.

## T-extra  the finding none of T1–T6 asked for

Keystone `longevity_years` against `era.end - era.start`:

    root (5 entries)     mean 0.62   max 0.88   over 1.0: 0
    HEAD (42 entries)    mean 0.95   max 1.00   over 1.0: 0

The stated rule held perfectly — **zero entries claim more longevity than
their era span**, across 42 entries and 13 months. The repo's own
documentation states it: "Never inflate a metric to clear a bar."

The unstated practice did not hold. At t=0 the root content — model-generated,
operator-transported — sat below the span by a margin that tracks epistemic
confidence: terra_preta, whose era bounds are least certain, is discounted
hardest (0.20); the lathe, whose dates are documented, least (0.88). That
margin was an uncertainty channel running through a field with no uncertainty
type. At HEAD the margin is 5% and `hxaro` sits at exactly 1.00.

**The rule was kept and the signal it was carrying was not.** A constraint
that is checkable survives; an unstated convention riding inside a plain
integer does not.

### attribution, under CORRECTION-001

The margin is **the generating model's**, not the operator's. It is one
model's uncertainty rendering, transported into the archive by paste. Later
entries, written by a different model under a different transport, do not
reproduce it.

So the finding is narrower than first written. It is not "the operator's
uncertainty signal was lost." It is: **a first-model rendering encoded
uncertainty in the size of a discount, and no later model reproduced that
convention, because nothing in the schema named it.** An untyped convention
does not survive a change of author, and every commit here is a change of
author.

Whether the operator ever wanted uncertainty in these values at all is
**UNSET** and is on the verify form. If the answer is NO, this ceases to be
a drift finding and becomes an artifact of the generating model.

It also remains the finding most likely to be wrong on its own terms:
"the margin means epistemic confidence" is an inference from five numbers.
