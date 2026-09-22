# drift-archive-audit

Treats a repository archive as a dated capability record: recover the
aimed-at target from the earliest commits, locate where the work drifted, and
separate TOOL limits from AGENT shaping where the archive allows it.

Reads source repositories **read-only**. Nothing here was committed to them.

**The operator's frame is held constant.** What changed over time is the
ENCODING of that frame. Encoding is the measured variable, not a confound.

## Pilot

| repo | root commit | first | last | commits |
|---|---|---|---|---|
| JinnZ2/Bio-Grid-American-Manufacturing- | `abb4b49c` | 2025-07-10 | 2026-08-16 | 63 |
| JinnZ2/Keystone-Codex | `34498a6e` | 2025-08-28 | 2026-09-22 | 27 |
| JinnZ2/Emotions-as-Sensors | `002486f8` | 2025-12-15 | 2026-08-21 | 123 |

Not expanded past the pilot. Waiting on verification.

## Layout

    ledger/commits.jsonl   A2 hashes, written BEFORE any history was read
    reconstruct/           A2 — target recovered from the root commit alone
    divergence/            A4/A5 — where it moved, typed and split
    verify/                A6 — operator forms, fields blank
    PHASE_B.md             cross-repo groupings and spanning frames
    PHASE_C.md             natural experiments found in the archive
    PHASE_D.md             channel probe — BLOCKED on the verify forms
    TESTS.md               T1-T6
    GUESSED.md             every value not filled in, and two retractions

## Order

    A1 root commit only
    A2 reconstruct -> sha256 -> ledger        <- gate
    A3 full history
    A4 locate divergences
    A5 classify (d_type / target-vs-rendering / channel)
    A6 verify form

Nothing was scored before the A2 hash for that repo existed.

    $ sha256sum reconstruct/*.md
    $ cat ledger/commits.jsonl

## Findings, in one screen

    targets persisted; renderings moved
      trust_model.md byte-identical across 63 commits and 14 months
      field-english.md and the transition guards unchanged
      no WHOLE_STATED artifact in the pilot was ever edited

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

    encoding effect: compression preserved what prose lost
      one clean experiment, content fixed, four encodings, one commit

    every historical channel: UNATTRIBUTABLE
      the archive holds no experiment across the tooling boundary

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
