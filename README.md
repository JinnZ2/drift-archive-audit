# drift-archive-audit

Treats a repository archive as a dated capability record: recover the
aimed-at target from the earliest commits, locate where the work drifted, and
separate TOOL limits from AGENT shaping where the archive allows it.

Reads source repositories **read-only**. Nothing here was committed to them.

**The operator's frame is held constant.** What changed over time is the
ENCODING of that frame. Encoding is the measured variable, not a confound.

**CORRECTION-001 (operator-issued, post-audit).** All pre-agent repo content
is model output, copy-pasted by the operator from chat code blocks. None of
it is operator-authored text; **the git author field is the pusher, not the
content author.** Every A2 target therefore reads as *a first-model rendering
of the operator's aim*, not the aim itself. The A2 files are unedited and
their hashes still verify — see `reconstruct/CORRECTION-001.md`.

## Pilot

| repo | root commit | first | last | commits |
|---|---|---|---|---|
| JinnZ2/Bio-Grid-American-Manufacturing- | `abb4b49c` | 2025-07-10 | 2026-08-16 | 63 |
| JinnZ2/Keystone-Codex | `34498a6e` | 2025-08-28 | 2026-09-22 | 27 |
| JinnZ2/Emotions-as-Sensors | `002486f8` | 2025-12-15 | 2026-08-21 | 123 |

Not expanded past the pilot. Waiting on verification.

`AI-Consciousness-Sensors` was in scope and not selected — still unsearched.
`JinnZ2/JinnZ2` (the profile README, and the declared parent frame of
Emotions-as-Sensors) was never in scope. It is reachable now and is
deliberately NOT added: see `PHASE_C7.md`, the reference-first gate.

## Layout

    ledger/commits.jsonl   A2 hashes, written BEFORE any history was read
    reconstruct/           A2 — target recovered from the root commit alone
    divergence/            A4/A5 — where it moved, typed and split
    verify/                A6 — operator forms, fields blank
    PHASE_B.md             cross-repo groupings and spanning frames
    PHASE_C.md             natural experiments found in the archive
    PHASE_C6.md            repeat description of a PHYSICAL referent —
                           the only arm with an outside reference.
                           BLOCKED on one operator answer.
    PHASE_C7.md            culture > consciousness > emotions, scored
                           against an unmediated reference.
                           GATED on the operator's reference description.
    PHASE_D.md             channel probe — BLOCKED on the verify forms
    TESTS.md               T1-T6
    GUESSED.md             every value not filled in, and two retractions

## Order

    A1 root commit only
    A2 reconstruct -> sha256 -> ledger        <- gate
       (re-labelled by CORRECTION-001; files unedited, hashes stand)
    A3 full history
    A4 locate divergences
    A5 classify (d_type / target-vs-rendering / channel)
    A6 verify form

Nothing was scored before the A2 hash for that repo existed.

    $ sha256sum reconstruct/*.md
    $ cat ledger/commits.jsonl

## Findings, in one screen

    earliest renderings persisted; later renderings moved
      trust_model.md byte-identical across 63 commits and 14 months
      field-english.md and the transition guards unchanged
      no WHOLE_STATED artifact in the pilot was ever edited
      (blob identity only - says nothing about the aim upstream of it)

    stage-2 loss: 0 of 6
      no falsified rendering took its target with it
      4 of 6 superseded renderings kept runnable or archived

    status-field decay: NOT observed at the corpus level
      every lexical category rose; the one decline is a rate, not a count
      three specific fields did decay - all three had no type to hold them

    noun resolution: occurred 3 times, reversed in 2
      Keystone  unlocks    0% -> 44% closure, being built
      Emotions  decay_model  relation returned as prose, structure did not
      Bio-Grid  phi        two couplings -> one noun -> two couplings

    encoding effect: WITHDRAWN under CORRECTION-001
      the one experiment needed its two encodings to share an author
      they may be different models; confounded, downgraded

    every historical channel: UNATTRIBUTABLE
      no experiment across the boundary, and the boundary itself is
      TRANSPORT x MODEL - paste->agent and model change, inseparable

## Rules this audit runs under

- Target/rendering split applies everywhere. A removed rendering never closes
  its target.
- `UNSET`, `UNCLEAR`, `UNATTRIBUTABLE` are values. They are not filled in by
  inference.
- No verdicts on content. Where things moved, not whether the movement was
  good.
- Nothing scored before the A2 hash exists.
- Anything that would need settling by fiat: stop and report. Phase D did.

The operator is referenced only as "operator", only in the verification
field. No author profile, no characterization.

CC0-1.0. Python stdlib only. No dependencies.
