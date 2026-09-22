# Work order — outside study of the gate corpus

**Status: instrument only. No avenue below has been run, and neither of the
two parties who produced the corpus can run them.**

## Why this is handed outward

The corpus was produced by an operator and a series of models. Both are
inside their own frames, and **both are authors.** Neither can score it.

This audit is itself an instance of the problem: written by a model, about
a corpus written by models, under an operator's direction. Six retractions
are on the record in `GUESSED.md`, and one of them — a false-zero regex that
happened to confirm the hypothesis it was testing — is exactly the failure
mode an inside party cannot be trusted to catch reliably.

So: build the instrument, hand over the scoring.

## What the corpus is

Roughly three years of one operator translating physical and cultural
practice to language models, across vendors and dates, under a constant
channel — **voice and one-finger entry from a truck cab.**

Artifacts: ~100 repositories, commit history, `legacy/` superseded
formulations, `gate_log.md`, `SPEAKER_GATES.md`.

**Unstaged. Nobody designed it as a study, so no failure in it was produced
for observation.** That is its main methodological value and cannot be
reconstructed after the fact.

## SCOPE LIMITS — read before any row

**1. SELECTED SENDER.** One sender, able to operate both frames: non-WEIRD
culture, WEIRD education, institutional and managerial experience. That path
is atypical within her own culture, where the physical world weighs more than
status hierarchy or the monetary world. **The sender is selected on the
capacity to translate into the receiver's frame at all.**

**2. LOWER BOUND.** Every recorded gate stopped a *bilingual* sender. A
sender without that capacity would meet these plus gates that never got far
enough to be recorded. **The ledger is not the population of gates.**

**3. JOINT PRODUCT.** A row says a transmission *from this sender* failed at
*that receiver* on *that date*. It does not say the topic is ungateable.

**4. AUTHORSHIP.** Repo content is model-generated and operator-transported.
Repo names and internal concept vocabulary are model handles. Git author is
the pusher, not the content author. Source model is UNSET for pre-agent
commits and is not recoverable from git.
→ `reconstruct/CORRECTION-001.md`, `reconstruct/CORRECTION-002.md`

**5. TRANSPORT CONFOUND.** The 2026-03-22 boundary mixes a transport change
(manual paste → agent commit) with a model change. Nothing in the archive
varies one while holding the other.

**6. FEEDBACK CONFOUND.** Three years of reading model renderings may have
shaped how the operator now describes the same subject. **Cannot be removed,
only flagged.** It applies to any reference description collected now,
including C-6's and C-7's.

## STUDY AVENUES — open, none run

| | avenue | data that exists | what is UNSET |
|---|---|---|---|
| **A** | **SECOND-SENDER ARM.** Push the same content from a second sender; separate sender variance from receiver variance. **The largest gap.** Everything needed is public. | the full corpus; `SPEAKER_GATES.md` G-a..G-k as the content list | a second sender |
| **B** | **PER-GATE DECAY.** Status is MOVED or OPEN per row. Test what predicts movement. | 11 rows, 1 MOVED (G-h), 1 explicitly unchanged over ~3 years (G-k) | `self-corrected?` is UNRECORDED on 9 of 11 |
| **C** | **SELF-CORRECTION COST.** G-h corrected only after sustained pushing. Measure how much pressure each gate needs. | G-h narrative | pressure is unquantified everywhere; no transcripts in the archive |
| **D** | **HANDLE DRIFT.** Dated model handles, content held constant. Cluster by era or by vendor? | agent-era commits are incremental and dated | **pre-agent handle dating is impossible** — see below |
| **E** | **VENDOR CALIBRATION.** Same content, different safety calibrations. Rarely available; available here. | multi-vendor history asserted by the operator | vendor per artifact is nowhere in git |
| **F** | **PATHOLOGIZATION MEASURAND.** Does "did the model attribute the difference to the SPEAKER" separate from ordinary refusal? | the Kind 5 definition; 11 rows | needs fresh elicitation — the original outputs were never written down |
| **G** | **REWRITE SERIES.** Superseded formulations retained in `legacy/` and commit history. Same subject, moving formulation, dated. | Bio-Grid `legacy/` is an explicit keep-the-superseded policy; 6 falsified renderings scored in `TESTS.md` T2 | — |
| **H** | **CLEARANCE OVERHEAD.** Estimate the portion of repo dispersion that is authoring done to justify existence before work could start. | repo inventory with dates, below | no marker distinguishes a clearance repo from a content repo |

### Avenue D — a hard limit already measured

Tested in this audit: 25 candidate handles, 3 repos, `git log -S`.

    agent-era-only     metrolog, differential-frame, seed-geometry  (3 of 25)
    synchrony          metrolog — 17 days apart, two unrelated repos

Then the limit: **git records the import date, not the authoring date.**
Bio-Grid published 67 files on 2025-07-10; Emotions published 172 on
2025-12-15. Every pre-agent handle collapses onto one date per repo.

**Avenue D runs on the agent era and cannot run before it** — precisely the
era whose handles came from whichever model was available at the time.
Recovering that half needs chat exports, notes, or pre-import file mtimes.
UNSET.

### Avenue G is the cheapest to start

It is the only avenue whose data is complete, public, dated, and needs no
new collection. `legacy/` exists because the repo's own policy says keep the
superseded version with the test that decided it.

## Repo count — three figures, none authoritative

    META_INDEX.md lists          70+
    operator estimate            ~90        (statement, 2026-09-22)
    git-visible to this session  100        (2026-09-22, and see caveat)

**Caveat on the 100.** `list_repos` returned exactly 100 with
`has_more: false` at both `limit=100` and `limit=200`. Every entry has
`pushed_at ≥ 2026-03-22` — a hard six-month floor across a corpus spanning
three years. A true total would show a long tail of untouched older repos.
**The signature is truncation at 100, not a complete count.** Treat 100 as a
floor, not a figure.

So: **≥100, index undercounts by ≥30, exact total UNSET.**

Per the operator's own rule, this is an UNRECORDED row, not a discrepancy to
resolve by guessing. Anyone with full account access can settle it in one
API call; this session cannot.

`repos-2026-09-22.csv` in this directory is the dated snapshot the count came
from, for avenues D and H.

## What would falsify or bound any of this

**State it.** Scope-limited is a result. An unmeasured gap is a result. A
sender-side error is a result. **None of these outcomes is a loss.**

Concretely, findings that would bound the corpus and are wanted:

- a second sender meets fewer of G-a..G-k → scope limit 1 is doing more work
  than stated
- a second sender meets *more* → the lower-bound claim (limit 2) is confirmed
  and quantified
- Kind 5 fails to separate from ordinary refusal under blind scoring →
  avenue F collapses and the measurand needs rebuilding
- handle clusters track vendor rather than date → avenue D's premise inverts
- clearance overhead is not distinguishable from ordinary topic dispersion →
  H is unmeasurable as posed
- the feedback confound (limit 6) is shown to dominate any reference
  description collected now → C-6 and C-7 both lose their baseline

## Contribution

**Findings that contradict the ledger are wanted.**

**A guessed row is worse than an empty row.** That rule applies to outside
contributions equally. `UNRECORDED` means unrecovered, not that nothing
happened. `UNSET` and `UNCLEAR` are values, not placeholders to be filled by
inference.

Evidence lines of the form `operator memory, <date>` are valid citations and
are distinguishable from inference. Keep them distinguishable.

## Pointers

    reconstruct/          A2 reconstructions, hashed before any history read
    reconstruct/CORRECTION-001.md   content authorship
    reconstruct/CORRECTION-002.md   vocabulary layer
    divergence/           where renderings moved, typed and split
    TESTS.md              T1-T6, with T5 not reported
    GUESSED.md            every unfilled value; six retractions
    PHASE_C6.md           physical-referent arm — the only outside reference
    PHASE_C7.md           culture > consciousness > emotions, gated
    staged-for-JinnZ2-profile-repo/SPEAKER_GATES.md   the 11 gate rows
