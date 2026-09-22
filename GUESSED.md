# Guessed values — listed, not filled in

Every value the audit could have settled by inference and did not.
`UNSET`, `UNCLEAR` and `UNATTRIBUTABLE` are the answers, not placeholders.

## From the spec

| field | status | why |
|---|---|---|
| repo name `drift-archive-audit` | **CONFIRMED by operator** | was marked PROPOSED |
| PILOT repos | **CONFIRMED by operator** | spec said "OPERATOR TO NAME" |
| A6 operator marks | **UNSET** | every line blank; Phase D and T5 blocked on it |

## Per repo

### Bio-Grid
| item | status |
|---|---|
| how long the work predates 2025-07-10 | UNSET — single root, bulk import of 67 files |
| φ 1.0008 vs 1.618 at t=0: two constants or a transcription error | **resolved by the archive itself** 2026-08-14 → two couplings. Confirm on the form |
| self-healing: 2 minutes or 20 minutes | UNSET — unresolved at root AND at HEAD |
| `data/biogrid_specs.json`, `data/compressed_hex_codes.txt` | UNCLEAR — named in root README, absent from root tree |
| whether rendering A was ever believed | **NOT ASKED.** No verdicts on content |

### Keystone
| item | status |
|---|---|
| `haudenosaunee_council.json` id `great_law_of_peace` | UNCLEAR — deliberate or half-landed rename |
| `ethical_alignment` unscored for 13 months | UNCLEAR — intended or dropped |
| the longevity discount margin = epistemic confidence | **INFERENCE from 5 numbers.** On the verify form |
| whether the remaining 50 dangling edges should close | UNSET |

### Emotions
| item | status |
|---|---|
| which decay vocabulary is the target (4-value vs 5-value vs 29 free-text) | UNSET |
| which of three licences is real | UNSET |
| `CONVERGENT_WISDOM.md` vs `Convergent-Wisdom.md` | UNCLEAR |
| how far the work predates 2025-12-15 | UNSET — ≥ 95 days, from a log file dated 2025-09-11 inside the root tree |
| whether the frame preceded Bio-Grid or was retrofitted | UNSET — Emotions' root postdates Bio-Grid's by 158 days and calls it "a prototype application of this framework" |

## Channels

**Every historical divergence: UNATTRIBUTABLE.**

The archive holds no case where the same content appears in two encodings
across the 2026-03-22 regime boundary (C-5). Without that, LEXICAL /
SYNTACTIC / CONTENT cannot be separated for any retired model. Authorship is
recorded per commit and the divergence tables are split by it; authorship is
not a channel and is not used as one.

One attribution is made, and it is an ENCODING effect, not a model channel:
C-1, φ, content fixed and encoding varied inside a single commit.

## Contamination, declared

Each repo's `CLAUDE.md` — a document written during the agent era, describing
the archive's later state — **was in my context before A1 was read.** It
could not be excluded.

Marked inline in each reconstruction:

| reconstruction | A1-clean | A1-ASSISTED / CONTAMINATED |
|---|---|---|
| bio-grid | frame_relations, piece_or_whole | the "two renderings at t=0" reading |
| keystone | the 15/15 dangling arithmetic | "evidence collected but not scored"; "longevity is a defensible floor" |
| emotions | all counts (20 shapes, 38/5/8, 56 files) | attention to `decay_model`'s two forms |

The arithmetic is reproducible from the root trees without CLAUDE.md. The
choice of *what to count* may not be. A re-run by a reader with no CLAUDE.md
in context would test this, and is the cheapest way to check whether the
audit itself drifted toward the archive's own later account of itself.

## Retracted during the audit

Two claims were made and then measured false. Both are corrected in place
and listed here so the corrections are not buried:

1. **"9–19 live files still carry withdrawn figures"** (Bio-Grid). Inspection
   showed all but 2 sit inside explicit supersession blocks. Real count: 2,
   both untouched since the root commit.
2. **"Bio-Grid and Emotions share the same relation set — the same
   signature"** (in both A2 files). The DETECT/ASSESS/RESPOND/RELEASE
   protocol is Emotions-only: 36 files at root, 81 at HEAD, and **zero** in
   Bio-Grid or Keystone at any commit. Substrate-neutrality (B1-c) survives;
   the shared-protocol claim does not.

Neither A2 file was edited after hashing. The corrections live in
`divergence/` and `PHASE_B.md` (B1-d). The hashes still verify.
