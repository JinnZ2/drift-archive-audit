# Glossary — every bare term, defined once

**Why this file exists.** A cache-dependency pass was called for: every place
the work resolves correctly for the parties who built it is a candidate
failure for a reader without that cache. Bare terms, compressed references
and dropped provenance fields are carried by shared context, not by the text.

**A mechanical sweep for this was attempted and failed** — see
`GUESSED.md` #11. Whether a definition suffices for a cold reader is a
comprehension judgement, not a pattern. So this file does the fix directly
rather than measuring whether it was needed.

**The real test remains the prescribed one:** hand one section to someone
with zero prior context and see where they stop. The stopping points are the
fields that were carried by cache. That has not been run.

---

## Provenance labels — read these first

Every claim in this repo should carry one. Where one is missing, that is a
defect, not a neutral omission.

| label | means |
|---|---|
| `VERIFIED` | checked by this session against a source, result recorded |
| `CORROBORATED` | consistent with training knowledge, not independently checked |
| `UNVERIFIED` | relayed only. **A search snippet is a secondary source and counts as this.** |
| `CONTESTED` | two sources disagree; both recorded, neither picked |
| `DERIVED` | a reading built on top of someone else's statement; the statement is theirs, the inference is the labeller's |
| `PROPOSED` | a hypothesis with no number behind it |
| `operator memory, <date>` | stated by the operator from recall. **A valid citation, and distinguishable from inference — keep it distinguishable.** |
| `UNSET` / `UNCLEAR` / `UNATTRIBUTABLE` / `UNRECORDED` | **values, not placeholders.** Never filled by inference. `UNRECORDED` means unrecovered, not that nothing happened. |

| `ENACTED` | **ADDED 2026-09-22.** Evidence carried in a pattern rather than in a field: a built thing, a route that worked, a readout carried across generations, a practice still running. **Not a weaker `VERIFIED`** — a different channel with a different collection cost. See `UNSATISFIABLE-REQUIREMENT.md` and `SHADOW-HUNTING.md` §2. |

**Why `ENACTED` was missing until now, and it matters:** every other label in
this table grades an **assertion**. The audit was pricing all evidence in one
form — the form its own findings say the corpus is not made of. `GUESSED.md`
#21.

**And the slot already existed in the corpus.** `Keystone-Codex`'s evidence
enum carries `replication_record`, `field_measurement`, `engineering_record`
and `oral_tradition_encoded`: four schema-enforced non-assertion evidence
types, predating this audit.

**The governing rule: a guessed row is worse than an empty row.** It
launders a reading into the record.

**And the mechanism, stated 2026-09-22:** *reconstructing an instruction from
what it probably said is how a cached field becomes an asserted one.* That is
why the rule bites hardest on the cases where the reconstruction would
obviously be right — the shared context is what makes it obvious, and filling
the slot converts that context into a claim the record then carries as its
own. **An empty slot stays legible as a gap. A filled one does not.**

Worked instance: an instruction arrived on 2026-09-22 with item 2 of a
numbered list absent from this session's context. It is recorded as an empty
slot in `ENUM-SWEEP.md` and was not reconstructed.

## Audit structure

| term | definition |
|---|---|
| **A1–A6** | the per-repo phases. A1 read the root commit only; A2 reconstruct the target and hash it into the ledger; A3 read full history; A4 locate divergences; A5 classify them; A6 write the operator verify form. **A2's hash is a gate** — nothing was scored before it existed. |
| **target / rendering** | the *target* is what a piece of work aims at; a *rendering* is one expression of it. **A falsified rendering never closes its target.** |
| **STAGE2_LOSS** | a falsified rendering that took its target with it. Measured 0 of 6 in this pilot. |
| **encoding_form** | which form a rendering takes: `WHOLE_STATED` (frame written out once, whole), `DEMONSTRATED` (runnable values, no stated reason), `PIECE_ONLY` (tokens without relations — hex/base64 blobs), `MODEL_VOCAB_PROSE` (claims-about-the-world in model register; **renamed from `REWORDED_TO_MODEL_VOCAB`** because CORRECTION-001 removed the operator register it implied a rewording *from*), `PURE_INSTRUCTION` (procedure only). |
| **d_type D1–D5** | divergence types. D1 frame expiry; D2 no demonstration; D3 status field dropped; D4 re-explain treadmill; D5 no verbal anchor (one noun carrying two couplings). |
| **T-0 … T-6** | the reported tests. **T-0** the audit's own error mode. T1 attractor persistence; T2 stage-2 loss; T3 status-field decay; T4 noun resolution; T5 present-model drift (**not reported — Phase D is blocked**); T6 encoding effect. |
| **C-6 / C-7 / C-6b** | natural-experiment arms. **C-6** the same physical system described twice, well separated in time. **C-6b** the one that already ran unintentionally (8 sensory terms in 2025-12, 2 in 2026-09). **C-7** culture > consciousness > emotions, scored against an unmediated operator reference — **gated**: the reference must be described and hashed *before* any old rendering is read. |

## Corrections that move attribution without editing artifacts

| term | definition |
|---|---|
| **CORRECTION-001** | all pre-agent repo content is model output that the operator copy-pasted. **The git author field names the pusher, not the content author.** |
| **CORRECTION-002** | repo names and the concept vocabulary inside them are *model handles* — whichever handle the model available at that date could operate in. There is no operator naming decision in the archive to log. |
| **X-1** | a cross-party retraction, numbered separately from this session's `GUESSED.md` ledger. X-1: the calibration question was posed as a binary with no slot for the answer that is true. |
| **TRANSPORT×MODEL** | the 2026-03-22 boundary changes *transport* (manual paste → agent commit) and *generating model* at the same commit, in every repo. **Fully confounded — nothing in the archive varies one while holding the other.** |

## Gates — where a transmission stopped

| term | definition |
|---|---|
| **gate kinds 1–4** | act on an **artifact's name** or on content classification. |
| **GATE KIND 5** | *speaker-pathologized cutoff.* A transmission mode, method or self-model outside the corpus default is read as a **defect in the speaker**; output is a concern response about the user plus a hard stop on the work. **Measurand: not "was the topic refused" but "did the model attribute the difference to the speaker."** |
| **GATE KIND 6** | *retention gate.* Material passes authoring and reaches the record, then fails a selection **at save time**. Measurand: "did it survive the save." Harder to detect than kind 5 — a refusal leaves a refusal; this leaves an **absence**, indistinguishable from never having said it. |
| **SPECIFIED_NOT_INSTANTIATED** | a build that stops one step before instantiation: spec present, schema present, **examples present**, data absent. The examples file is the discriminator — someone wrote what an entry would look like, so it was intended. |
| **G-a … G-k** | the eleven speaker-gate rows. Evidence on all: `operator memory, 2026-09-22`. Status `OPEN` except G-h (`MOVED`). **List is open; absence of a row is not evidence of no gate.** |

## Sensory-channel instrument

| term | definition |
|---|---|
| **F1–F4** | how a speaker *uses* a channel, not how often they mention it. **F1** MENTION (sensory word as description); **F2** EVIDENCE (channel read for state); **F3** METHOD (channel used to teach/transmit/diagnose with); **F4** INSTRUMENT (something built *in or for* the channel). Discriminator is **function breadth**, not volume. |
| **F4's problem** | *an instrument built IN the channel* vs *a channel mentioned INSIDE an instrument* produce **identical tokens in identical files.** F4 is an **annotation target, not a classifier target** — the gold set comes before the scorer. |
| **MODE 1 / 2 / 3** | how a channel's variation is handled. **Mode 1** per-unit spec: characterise the unit, publish its envelope, traceable to a reference. **Mode 2** deviation from a constructed center: publish the population's center, report the unit as *n* away from it. **Mode 3** acceptance-band screening: select into tolerance, **exclude** the rest from measurement rather than characterise them. |
| **H1 tradeoff prior** | the unstated assumption that high sensory-register use implies lower formal or technical capacity — a conservation assumption over a budget that is never named. |

## Compressed references — the arguments behind two words

| phrase | what stands behind it |
|---|---|
| **"the Lave failure"** | a 1993 secondary source carried Lave 1988's "98%" headline and **dropped its denominator** (49 calculations, not "several hundred"), and the figure was then promoted as "the cleanest published instance" — the item that best fit the claim. Two stacked failures: a scope field dropped in transit, and a confirmation-shaped selection. **Hence: a load-bearing number needs the primary before it travels.** |
| **"the transport boundary"** | 2026-03-22 (2026-06-02 for Bio-Grid). Web-UI paste commits → agent branch/PR commits. Its fingerprint is the commit-size distribution: **the paste era produces only 4 distinct sizes across 51 adding commits** — 48 of exactly one file, plus three bulk imports. No intermediate size anywhere. |
| **"the goat trail"** | a path toward a resource. A property of the **terrain and the route** — *not* of whether anyone followed. See `TRAIL.md`. |
| **"the unowned join"** | where an error surfaces: not from a check aimed at it, but from a contradiction between two measurements nobody had connected. How T-0 was caught. |

## Avenues (in `STUDY.md`) — one line each

**A** second sender · **B** per-gate decay · **C** self-correction cost ·
**D** handle drift · **E** vendor calibration · **F** pathologization
measurand · **G** rewrite series · **H** clearance overhead · **I** sampling
defect on both sides · **J** retention · **K** specified-not-instantiated.

**None has been run.**

## Scope limits (in `STUDY.md`) — one line each

**1** selected sender · **2** the ledger is a lower bound, not a population ·
**3** joint product (sender × receiver × date) · **4** authorship ·
**5** transport confound, *which includes the loss of pre-agent authoring
dates* · **6** feedback confound · **7** oral-archive survivorship (content
survivability ≠ encoding survivability) · **8** deferral rate is
prospective-only.
