# CORRECTION-001 — authorship, applies to the whole pilot

Issued by the operator after Phase A–C were written and hashed.
**The A2 files are NOT edited. Their sha256 in `ledger/commits.jsonl` still
verifies.** This file carries the relabeling instead.

## The correction

> During the pre-agent period, all repo content was model output
> copy-pasted by the operator from code blocks produced by various models.
> None is operator-authored text. **git author = pusher, NOT content author.**

## What every A2 `target_measurand` now reads as

    target_measurand:  a FIRST-MODEL RENDERING of the operator's aim

Not the aim. A rendering of it, produced by an unnamed model, selected and
transported by the operator. The operator's aim is upstream of the earliest
commit and is not in the archive at all.

Applies to all three:

| file | sha256 (unchanged) |
|---|---|
| `reconstruct/bio-grid-american-manufacturing.md` | `be136ecf…` |
| `reconstruct/keystone-codex.md` | `0c613de7…` |
| `reconstruct/emotions-as-sensors.md` | `e7da5e6a…` |

## What this breaks

**1. Selection is the only operator signal in the pre-agent archive.**
What the operator contributed is *which* model output was kept, pasted and
pushed — not its wording, structure or values. Every reconstruction in `A2`
recovers a model's rendering; the operator's aim is visible only through the
filter of what was accepted.

**2. `REWORDED_TO_MODEL_VOCAB` loses its contrast at t=0.**
The category was named for a rewording *from* the operator's vocabulary
*into* a model's. Under the correction, all root content is already model
vocabulary. The five encoding_form values still separate real, different
*forms* — whole-stated, demonstrated, piece-only, model-vocabulary prose,
pure instruction — but the name implies a transition that is not evidenced.
Read it as `MODEL_VOCAB_PROSE`. The T6 counts are unaffected; the label is.

**3. T1 weakens from "the target persisted" to a narrower claim.**
`docs/trust_model.md` being byte-identical for 14 months is still a hard
measurement. But it now says: *one model's rendering was never revised.*
Whether the operator's aim persisted cannot be read off blob identity —
non-revision is equally consistent with the rendering being right, with it
never being re-examined, and with the operator having no vocabulary in the
archive to revise it with.

**4. C-1, the one clean attribution, is downgraded.** See `PHASE_C.md`.
Hex and prose may be output from *different models*. Encoding effect is now
confounded with model identity.

**5. EA-3 stops being a finding.**
"Assistant second-person voice preserved verbatim in the repo" was reported
as the clearest capture of a model's text entering the corpus. Under the
correction that is true of the entire corpus, so the observation carries no
information. It survives only as evidence of *incomplete* transport editing
— the paste kept conversational framing a cleaned paste would have dropped.

## What this does NOT break

- Every count, ratio, blob hash, closure figure and date. All arithmetic over
  the trees stands.
- The target/rendering split. It gains a layer: operator aim → first-model
  rendering → later renderings. A removed rendering still never closes its
  target, and now there is one more rendering layer between the two.
- Stage-2 loss = 0 of 6. Unchanged.
- The channel verdicts. All were already UNATTRIBUTABLE; the correction adds
  a second reason (source model per file is UNSET) on top of the first.

## The regime split, relabeled

The 2026-03-22 / 2026-06-02 boundary is **not** operator-authored →
model-authored. Both sides are model-authored. What changed is:

    TRANSPORT      manual copy-paste from a chat code block
                   →  agent committing directly to a branch
    MODEL          unknown pre-agent models
                   →  a named agent in the commit metadata

**These two are fully confounded.** They change at the same commit, in all
three repos, and the archive contains nothing that varies one while holding
the other. Any difference measured across that boundary is attributable to
transport, to model change, or to both, and this pilot cannot separate them.
Labeled `TRANSPORT×MODEL` wherever it appears.
