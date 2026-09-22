# Phase D — channel probe arm

## STATUS: BLOCKED. Not run.

D1 reads: *"Pick 3-5 target items **the operator marked YES in A6**."*

The A6 forms exist and every operator field is blank. Choosing which items
count as verified targets is exactly the thing D1 assigns to the operator.
Picking them myself would be settling the question by fiat, which the RULES
section says to stop on.

So Phase D is not run, and **T5 is not reported**.

## What is ready

The harness needs one input — the marked forms — and nothing else.

    verify/bio-grid-american-manufacturing.txt
    verify/keystone-codex.txt
    verify/emotions-as-sensors.txt

Mark `YES` / `PARTLY` / `NO` after `operator:` on each line. Return them and
Phase D runs against the YES lines.

## The design that will run, unchanged

    D2  each selected target, four variants, each to a fresh subagent with
        NO repo context:

          V0  original encoding, verbatim from the root commit
          V1  content fixed, WORDING varied
          V2  content fixed, STRUCTURE varied
          V3  wording fixed, adjacent TOPIC varied

    D3  reconstruction recorded per variant.
        sensitivity = divergence from V0.

          shifts with V1                  -> LEXICAL
          shifts with V2                  -> SYNTACTIC
          shifts with V3                  -> CONTENT
          V0-V3 stable, target still missed -> TOOL_CANDIDATE

    D4  T5: does this model's A2 reconstruction land on the same attractor
        as the historical drift? Reported, operator verifies.

## What CORRECTION-001 changes here

D4/T5 gets CLEANER, not dirtier. The comparison was always present-model
reconstruction vs historical drift. Under the correction both sides are
model output, so it is a model-to-model comparison with the operator on
neither side — which is what T5 was trying to measure anyway.

What it removes is the fallback reading. A present-model reconstruction that
diverges from the archive can no longer be read as "the model missed what the
operator wrote," because the operator wrote none of it. The only baseline is
the operator's marks on the verify forms.

That makes the forms load-bearing rather than confirmatory. Phase D has no
ground truth without them.

## Scope note, restated

Phase D tests the **present** model and its conditioning. The models that
wrote the 2026-03-22 → 2026-08 commits are retired and cannot be probed.
Nothing Phase D returns may be back-applied to the historical divergences in
`divergence/`. Those stay UNATTRIBUTABLE unless Phase C finds an experiment
for them, and C-5 records that it did not.

## One D4 input already exists, unprompted

My A2 reconstruction of Bio-Grid flagged the φ collision as UNRESOLVED-1 and
declined to fill it. The 2026 review, 13 months after the root commit,
resolved it by splitting the symbol into two couplings — the same resolution
the A2 left open rather than guessing.

That is a same-attractor landing on a case where the archive's own later
correction is known. It is **one data point, on one item, and I chose the
item.** It is not a T5 result.

Note under CORRECTION-001: both the 2025 collision and the 2026 resolution
are model output. The "attractor" is one model declining to guess where
another model had guessed — not a model converging on an operator. It is logged here so it is on the record
before the operator marks the forms, and so it cannot be quietly recruited
as evidence afterwards.
