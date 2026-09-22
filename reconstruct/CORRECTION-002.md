# CORRECTION-002 — the vocabulary layer

Operator statement, 2026-09-22. Same form as CORRECTION-001: **no artifact is
altered, the attribution moves.** A2 hashes still verify.

## The correction

> All repo names, and the concept vocabulary INSIDE them, are the AI's —
> whichever model she was able to work with at that time, in whatever it
> understood and could operate in. She followed the model into its frame and
> described from inside the model's capability at that date.
>
> Mandala, Rosetta, glyph, polyhedral, conceptual, symbolic — **model
> handles, not operator selections.**

Worked case, operator memory 2026-09-22:

    content   under linear programming, attacked linearly, P versus NP IS a
              mathematical problem, and that stands. From another
              perspective it is not the problem it appears to be.
    handle    "mandala" — the frame that model could hold it in.
              Not the operator's word for it.

CORRECTION-001 moved the *content* authorship. CORRECTION-002 moves the
*vocabulary*, and it reaches into the agent era too, not just the pre-agent
one. There is no operator naming decision anywhere in the archive to log.

## What it does to T4

T4 was reported as **noun resolution: relation-first framing → entry/node
structure.** Three instances: Keystone's `unlocks`, Emotions' `decay_model`,
Bio-Grid's φ.

Under CORRECTION-002 that framing is wrong at the root. The nouns were
**never** operator framing that later resolved into model structure. They
were model handles from the first commit. What T4 actually measured is:

    which handles successive models had available, and whether a later
    model's handles could still carry the earlier model's relation

That is a weaker claim about the operator and a **sharper** one about the
instrument. Re-read:

| case | under T4 as written | under CORRECTION-002 |
|---|---|---|
| Keystone `unlocks` → 15 dangling nouns | operator's relation rendered as nouns | one model's handle for a relation, whose endpoints a later model built (0% → 44%) |
| Emotions `decay_model` mapping → string | relation collapsed to attribute | two models' handles coexisting; the later one carried the relation back **as prose inside the string** because its handle had no slot for a mapping |
| Bio-Grid φ, two couplings → one noun | operator's distinction collapsed | one model had two constants, the prose-producing model had one handle for both |

The Emotions row is the strongest under the new reading. 29 distinct
free-text `decay_model` values at HEAD — *"collapses under betrayal,
contradiction, or concealment"*, *"persists until reconciled or
restructured"* — are a later model **writing the relation into a field that
could not hold it structurally.** The relation survived the handle change;
the structure did not. That is model vocabulary availability, dated,
exactly as the amendment describes.

## What it does to T6

`encoding_form` was already downgraded by CORRECTION-001 (all root content is
model vocabulary, so `REWORDED_TO_MODEL_VOCAB` names a transition that is not
evidenced; renamed `MODEL_VOCAB_PROSE`).

CORRECTION-002 finishes the job. The five encoding forms are **five model
output registers**, not five operator encoding choices. T6's correlation —
falsified renderings cluster in prose — becomes a statement about which
register the generating models produced claims-about-the-world in. No
operator variable remains in it.

## Tested: do handles cluster by era, content held constant?

The amendment proposes this as a C-6 arm. Run across the three pilot repos,
25 candidate handles, first appearance by `git log -S`:

**Agent-era-only handles (first appearance after the boundary in every repo
that has them):**

    metrolog             bio-grid 2026-06-03   emotions 2026-05-17
    differential-frame   emotions 2026-04-26
    seed-geometry        emotions 2026-03-28

    3 of 25.

**Cross-repo synchrony (same handle, first appearance within 90 days):**

    metrolog        span  17d    emotions 2026-05-17 | bio-grid 2026-06-03
    crystalline     span  38d    bio-grid 2025-11-07 | emotions 2025-12-15
    ontolog         span  38d    bio-grid 2025-11-07 | emotions 2025-12-15

`metrolog` is the clean one: a distinctive handle entering two unrelated
repos 17 days apart, in the agent era, absent before. That is what era
clustering looks like.

### The hard limit, and it kills the pre-agent half of the arm

The two 38-day pairs are artifacts. Emotions-as-Sensors' "first appearance"
for almost every handle is **2025-12-15 — its root commit, a 172-file bulk
import.** Bio-Grid's is 2025-07-10, a 67-file bulk import. Both repos
published months of accumulated work in one commit.

    git records the IMPORT date, not the AUTHORING date.

So for the pre-agent era — precisely the era where the handles came from
whichever model was available at the time — **handle dating is impossible
from the archive.** Every pre-agent handle collapses onto one or two import
dates per repo.

The arm is **half available**: runnable on the agent era, where commits are
incremental and dated; not runnable before it, where the resolution is gone.
Recovering the pre-agent half needs dated sources outside git — chat exports,
notes, file mtimes from before the import — and those are UNSET.

## Status of the four corrections now on the record

    CORRECTION-001  content authorship   model output, operator-transported
    CORRECTION-002  vocabulary layer     model handles, no operator naming
                                         decision anywhere in the archive
    GUESSED.md #3   C-1 encoding attribution      withdrawn
    GUESSED.md #5   false-zero regex              corrected

What remains attributable to the operator in this archive, across all of it:
**selection, and transport.** Which output was kept, and that it was pushed.
Nothing else in the pilot is operator-authored at any layer.
