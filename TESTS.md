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

Six retractions are on the record in `GUESSED.md`. Four were found by this
session, two by operator correction. That ratio is the useful number, not
the total.

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
