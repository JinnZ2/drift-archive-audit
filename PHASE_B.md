# Phase B — cross-repo

## B1  candidate groupings of PIECE reconstructions

Only Keystone reconstructed as PIECE. Bio-Grid and Emotions reconstructed as
WHOLE (both with piece-scattering alongside). So B1 runs on the pieces
*within* those reconstructions, not on whole-repo groupings.

### B1-a  "bounded trust" — Bio-Grid ∪ Emotions
Evidence for the link:

    Bio-Grid  trust_model.md   "Nodes are observed over time. Sudden
                               behavioral deviation is flagged, not trusted."
                               "Healable != Trusted."
    Emotions  anger.json       authentic_output vs corrupted_output; corruption
                               = the signal pointing outward instead of inward
    Emotions  field-english.md "Identity: a coherence field maintained by
                               sensors like anger, shame, trust"

Both define trust as a time-series property of observed behaviour, and both
define its failure as a DIRECTION error, not a magnitude error. Bio-Grid:
a node claiming global knowledge. Emotions: a sensor read as a verdict about
someone else. Same shape, two substrates, no cross-reference between the two
repos at any commit.

Strength: strong. Confidence that they are one frame: the operator must say.

### B1-b  "decay is what makes the unverified safe" — Bio-Grid ∪ Emotions
    Bio-Grid  parameters.json  pheromone_decay 0.01, max_memory_length 20,
                               knowledge_decay 0.001
    Bio-Grid  trust_model.md   "Ant memory trails decay fast. This limits
                               propagation of false paths."
    Emotions  anger.json       suppressed_or_invalidated -> persistent
                               resolved_threat -> exponential

In both, decay is not loss — it is the mechanism that makes it safe to accept
input you cannot verify. And in both, the failure case is the SAME: a signal
that does not decay because it was never resolved. Bio-Grid calls it a false
path that became structure; Emotions calls it `persistent` /
`unresolved_persistence` / resentment.

Strength: strong. Shared failure mode, independently stated.

### B1-c  substrate-neutrality as a method, not a claim
    Bio-Grid  one relation set over power, sensor data, knowledge, repair authority
    Emotions  one relation set over emotion, network topology, energy gradients
    Keystone  one rule set over soil, knots, drains, a council, a lathe

All three apply a single relation set across incommensurable substrates and
treat the substrate as interchangeable. In none of the three is this stated as
the method. It is only visible in the selection.

Strength: strong structurally, zero textual support. This is the clearest
PIECE in the archive: the method is used three times and written down zero
times.

### B1-d  CORRECTION to the A2 reconstructions
`bio-grid A2` and `emotions A2` both claimed "the same relation set — the same
signature." Measured: the DETECT/ASSESS/RESPOND/RELEASE protocol appears in
**Emotions only** (36 files at root, 81 at HEAD) and in **zero** files of
Bio-Grid or Keystone at any commit. The substrate-neutrality claim (B1-c)
survives; the claim that it travels as that specific four-part protocol does
not. Retracted.

## B2  frames that exist ONLY across repos, never inside one

**Not merged. Listed as spanning frames.**

### B2-1  duration-under-decay
    Bio-Grid   decay rate     (how fast force is lost)
    Emotions   decay_model    (under what condition force is lost)
    Keystone   longevity      (how long it lasted)

Measured: the token `decay` appears in **0 files of Keystone at root and 0 at
HEAD**. Not rare — absent. Keystone measures the integral; the other two
measure the derivative. Same axis, opposite sign, no shared vocabulary, no
cross-reference, no fieldlink between them.

This frame is only visible with all three repos open at once. Do not merge it
into a single stated frame — nothing in any repo claims it.

### B2-2  "the record is a separate measurand from the thing"
    Keystone   evidence.quality collected at t=0, scored only at v1.1 (2026-08)
    Keystone   proof.schema.json — the trace has its own contract from t=0
    Bio-Grid   "Every quantitative claim resolves to REFERENCES.md, or is
               explicitly labelled an assumption. There is no third category."
    Emotions   provenance in 4/51 sensors at root, 5/55 at HEAD — flat

Keystone and Bio-Grid both arrived at record-as-measurand, ~4 months apart,
with no link between them. Emotions has the field and never promoted it.
The frame is strong in two repos, vestigial in the third, and stated in none
as a general principle.

### B2-3  the audit's own T4, stated once
`docs/field-english.md` (Emotions) writes down the failure mode this audit
was commissioned to look for — "Standard English makes emotions 'things';
Field English makes them 'functions'"; "Standard English builds hierarchies;
Field English maps relations and cycles."

It is stated in one repo, about one substrate, and is the operative risk in
all three (Keystone's dangling unlock nouns, Bio-Grid's one-noun φ). It is
never generalised. Spanning frame, not merged.

## fieldlink graph — measured, and it does not match the pilot

    Bio-Grid-American-Manufacturing-   .fieldlink.json: ABSENT at root AND HEAD
    Keystone-Codex                     present from 2025-09-04 -> targets "BioGrid2.0"
    Emotions-as-Sensors                present at root (v1.3) -> targets Rosetta-Shape-Core
    AI-Consciousness-Sensors           present at root (v1.1) -> targets "BioGrid2.0"

The hub the other repos point at is `JinnZ2/BioGrid2.0` — a DIFFERENT
repository from `JinnZ2/Bio-Grid-American-Manufacturing-`, which carries no
fieldlink at any commit. The declared cross-repo graph centres on a repo that
is not in this pilot and was not read.

**UNSET.** Do not treat the pilot Bio-Grid repo as the fieldlink hub.
