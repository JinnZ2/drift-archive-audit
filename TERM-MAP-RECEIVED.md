# TERM_MAP

Coined terms in this repo, mapped to existing English terms where one exists.
Carries the "is there already a word for this" question forward so it is not
dropped between conversation and code.

## Rule

Coined term in a commit → add a row. If no search was done, set
`existing_term = UNCHECKED`. The row exists either way.

`status`: MATCH / PARTIAL / NONE / UNCHECKED — overlap as assessed by the
model that searched.
`operator_fit`: set only by the operator. UNSET until then. A MATCH status
does not fill it.

## Seed — 2026-09-22, from README, BNRAM_STRICT.md, PVL.md only

Other folders not yet searched. Terms in these docs may be model coinages;
rows record the term, not its author.

| repo_term | existing_term | source | covers | misses | status | operator_fit |
|---|---|---|---|---|---|---|
| narrative smoothing | narrative smoothing | Spence 1982, *Narrative Truth and Historical Truth* | coherence made by dropping data that doesn't fit | — | MATCH | UNSET |
| Empirically Observed vs Thermodynamically Validated | phenomenological model vs mechanistic model | physics / engineering | output fit without mechanism vs mechanism mapped | no entropy-budget requirement | MATCH | UNSET |
| Verified Outcomes, Opaque Source | proven in use (+ in-service monitoring) | IEC 61508 functional safety | qualification by operating history, not design analysis | written for components, not practices | MATCH | UNSET |
| Persistence-Over-Time over Volume-of-Documentation | Lindy effect | Mandelbrot; Taleb | survival time as evidence of further survival | no energy denominator (Ph / Total Energy) | MATCH | UNSET |
| Physical State Query / Inverse Audit | ground truthing | remote sensing | check model/sensor output against on-site state | not framed as first step before literature | MATCH | UNSET |
| grounding AI | symbol grounding problem | Harnad 1990 | symbols anchored to non-symbolic referents | Harnad's anchor is perception, not physics layers | MATCH | UNSET |
| Model/Reality Dissonance | sim-to-real gap; model misspecification | robotics; statistics | model output diverges from world | — | MATCH | UNSET |
| Correction of Scalar Bias | law of requisite variety | Ashby 1956 | regulator needs variety ≥ regulated system | Ashby is about control, not insight claims | MATCH | UNSET |
| Deflection #2 (tone / moral intent) | tone policing | common use | redirect from content to delivery | — | MATCH | UNSET |
| Literal Baseline Lexicon | controlled vocabulary; semantic drift | information science | fixed term list; drift named | locks terms to physical units, not a list | PARTIAL | UNSET |
| hidden entropy debt | latent conditions; deferred maintenance | Reason (Swiss cheese); maintenance eng. | failure accumulating unseen | no thermodynamic accounting | PARTIAL | UNSET |
| opacity quadrant | black / grey / white box | systems engineering | transparency axis | no observed-vs-unobserved axis | PARTIAL | UNSET |
| Entropy-Constraint Engine | exergy analysis; EROI; emergy | thermodynamics; ecological economics (H.T. Odum) | energy accounting of a proposal | not a gate on assertions | PARTIAL | UNSET |
| the ground itself is the manual | landscape archaeology (weak) | archaeology | ground read as record | ground as running reference, not archive | NONE | UNSET |
| Deflection #3 (immunity via complexity) | — | — | — | no term located | NONE | UNSET |

## Confusion risks

| repo_term | risk | reads as | alternative that carries the referent |
|---|---|---|---|
| Dissonance | high | cognitive dissonance (psychology) | sim-to-real gap |

---

# RECEIPT — added by the receiving session, not by the author

Filed verbatim, unedited. **Nothing above this line was written or altered
here.** `operator_fit` is untouched in every row and stays `UNSET`; this
session judges no fit, per the routing rule and `GUESSED.md` #34.

## THE FIND CHECK WAS RUN BEFORE FILING — first time

`FINDABILITY.md` prescribes: *before the next instrument is built in this
programme, search the corpus for an existing one.* **Run, unprompted, and it
returned three hits.** Seventh findability instance, and the first found by
looking rather than by being told.

    tools/check_term_collision.py
      "who uses the colliding terms, and who declares which sense"
      Finds phrases naming two distinct objects and reports which
      modules carry the disambiguating note.
      -> This is TERM_MAP's CONFUSION RISKS table, as a running tool.
         The one row there (Dissonance) is what it finds mechanically.

    cooperative-substrate/term_table.py
      "a schema with the one worked cell the pack supplies and EVERY
       OTHER CELL UNRECORDED. Nothing is filled from memory. A
       non-UNRECORDED cell needs a BASIS naming the pack items it
       rests on."
      -> This is TERM_MAP's RULE, already built, and STRICTER: it
         requires a basis for any filled cell, where TERM_MAP carries
         the basis informally in `source`.

    term-drift-citation
      "A citation carries a measurement forward under a word. The
       citation is only valid if the word's referent held between the
       measurement and the use. Nothing in a citation records whether
       it did."
      -> The TEMPORAL half. TERM_MAP maps coinage to existing term at
         one moment; this asks whether the referent held over time.

## WHAT IS ACTUALLY NEW — verified, not assumed

    grep for `existing_term` and `operator_fit` across the repo: NO HITS.
    INSTRUMENT-INDEX.tsv columns: id name repo path input_shape catches
      load_bytes load_tok_est run_cost run_basis status gate built_against
      -- neither column present.

**`operator_fit` is the new part, and it is the load-bearing one.** A
holder-only column with `UNSET` as its default is the same construction as
`ENACTED` and `DETECTOR_BLIND`: **a missing judgement is a value, not a
blank**, and a `MATCH` status explicitly does not fill it. That is the
routing rule as a schema rather than as a sentence.

## TWO STRUCTURAL NOTES — proposed, not imposed

**Structure is this session's register; the contents of any row are not.**

1. **No column records who coined the term.** The seed handles it in prose —
   *"rows record the term, not its author."* Under `CORRECTION-002` that
   value is `UNSET` across the whole archive, which is a fact worth carrying
   in a field rather than a note. A prose caveat is a naming remedy;
   `REMEDIES.md` measures those at **0 preventions out of 8**.

2. **Two `source` cells are not citations.** `common use` and `—` sit beside
   `Spence 1982`, `Harnad 1990`, `Ashby 1956`, `IEC 61508`. Nothing marks
   the difference, so a reader cannot tell a sourced row from an unsourced
   one without reading every cell. The status enum covers *overlap*; it does
   not cover *whether the match has a source*.

**Whether to fold `operator_fit` onto the existing machinery, or keep
TERM_MAP separate, is not this session's call** — it is the operator's
index, in the operator's repo, and the audit is read-only there.
