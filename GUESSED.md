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

## Authoring date per pre-agent file — UNSET, and not recoverable

Both pre-agent repos published accumulated work in a single bulk commit
(Bio-Grid 67 files on 2025-07-10; Emotions 172 files on 2025-12-15). **Git
records the import date, not the authoring date.**

This was known from A2 ("the work predates its own first commit by an unknown
interval"). CORRECTION-002 makes it costly: the handle-clustering arm the
operator proposes needs dated handles, and every pre-agent handle in this
pilot collapses onto one date per repo. The arm runs on the agent era only.

Recovering the pre-agent half requires dated sources outside git — chat
exports, notes, pre-import file mtimes. UNSET.

## Source model per commit — UNSET, and not recoverable

Under CORRECTION-001, all pre-agent repo content is model output that the
operator copy-pasted from chat code blocks. Which model produced any given
file, block or value is **UNSET**.

It is not recoverable from git. The author field records the pusher. The
committer field records the web UI. Nothing in any tree names a generating
model, a date of generation, or a session. Two files in the same commit may
be output from two different models and the archive cannot distinguish them.

Consequences, all of them live:

| affected | consequence |
|---|---|
| C-1 (φ) | hex and prose may be different models — the encoding attribution is confounded and **withdrawn** |
| T6 | `encoding_form` is confounded with `which model wrote this file`; reports a correlation with no isolated cause |
| the 2026-03-22 boundary | `TRANSPORT×MODEL`, inseparable |
| T-extra | the longevity margin belongs to the generating model; whether the operator wanted uncertainty there is on the verify form |
| every A2 | recovers a first-model rendering, never the aim |

The only pre-agent operator signal in the archive is **selection**: which
output was kept, pasted and pushed. Not its wording, structure or values.

## Channels

**Every historical divergence: UNATTRIBUTABLE** — now for two independent
reasons: no experiment across the regime boundary (C-5), and source model
per file UNSET (above).

The archive holds no case where the same content appears in two encodings
across the 2026-03-22 regime boundary (C-5). Without that, LEXICAL /
SYNTACTIC / CONTENT cannot be separated for any retired model. Authorship is
recorded per commit and the divergence tables are split by it; authorship is
not a channel and is not used as one.

**No attribution survives.** C-1 was the single candidate — φ, content fixed,
encoding varied inside one commit — and it is withdrawn: it required the two
encodings to share an author, which CORRECTION-001 removes.

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

Four claims were made and then withdrawn. Listed here so the corrections are
not buried. The first two were measured false by this audit; the last two
fell to CORRECTION-001:

1. **"9–19 live files still carry withdrawn figures"** (Bio-Grid). Inspection
   showed all but 2 sit inside explicit supersession blocks. Real count: 2,
   both untouched since the root commit.
2. **"Bio-Grid and Emotions share the same relation set — the same
   signature"** (in both A2 files). The DETECT/ASSESS/RESPOND/RELEASE
   protocol is Emotions-only: 36 files at root, 81 at HEAD, and **zero** in
   Bio-Grid or Keystone at any commit. Substrate-neutrality (B1-c) survives;
   the shared-protocol claim does not.

3. **"Compression preserved a relation that prose lost"** (C-1, T6). Needed
   the hex and the prose to share an author. Source model per file is UNSET.
   Withdrawn; what survives is a weaker claim about paste-assembled trees
   carrying undetected internal conflicts.
4. **"Assistant second-person voice preserved verbatim"** as evidence of a
   model's text entering the corpus (EA-3). True of the entire corpus under
   CORRECTION-001, so it carries no information. Survives only as evidence
   of incomplete transport editing.

5. **A broken regex produced a table of false zeros** (C-7, parallel/
   always-on). `git grep -E "a\|b\|c"` was used with backslash-escaped
   pipes; in POSIX extended regex `\|` is a LITERAL pipe, not alternation,
   so every multi-term row searched for the literal string and returned 0.
   The first reading — "parallel and always-on are encoded nowhere" — was
   wrong and would have confirmed the hypothesis it was testing. Corrected
   in `PHASE_C7.md`; the corrected result inverts it.

   Worth keeping visible: a measurement error that happens to agree with the
   claim under test is the failure mode this whole audit is about. It got
   caught only because an unrelated check (`affective`) returned a nonzero
   count that contradicted the table.

6. **I merged two distinct gates into one on a shared property**
   ("bounded unit, single state" — `PHASE_C7.md` Kind 5 / Kind 5b). The
   operator states they were distinct strong gates and the list is longer
   than two: G-a through G-k, eleven rows, list open. The merge was an
   inference over a report, not a reading of the archive. **Withdrawn.**
   My Kind 5/5b split is superseded by the stated definition — Gate Kind 5
   is *speaker-pathologized cutoff*, and its measurand is not what blocked
   but **whether the model located the defect in the speaker.** That is a
   different axis from the one I split on.

7. **A relayed figure was promoted because it best fit the claim.**
   Lave 1988's "98% / 59%, a 39-point channel effect" was relayed from a
   1993 secondary source that carried the headline and dropped the
   denominator — 49 calculations, not several hundred — and was then called
   "the cleanest published instance". Withdrawn by the relaying party,
   2026-09-22.

   Two failure modes stacked, both already in this registry: a **scope field
   dropped in transit** (the T4 pattern) and a **confirmation-shaped
   selection** (T-0). The item that best fit the claim is the item that got
   promoted.

   Consequence: the `RELAYED-AS-VERIFIED` status introduced in the previous
   pass is **withdrawn as too generous**. Search snippets are secondary
   sources; naming the retrieval method does not make one primary. All
   relayed citations are `UNVERIFIED`, and any carrying a load-bearing
   number needs the primary before it travels.

8. **The pilot selection rule had a predictable bias, and I chose it.**
   I offered the pilot options ordered by repo age; the operator selected
   the three oldest of four available. Age is a defensible proxy for
   "earliest aimed-at target", which is what Phase A needed — **and it also
   selects for repos that predate the framework's own articulation.** Five
   findings have now landed in unselected repos (see
   `CROSSCHECK-ai-human-audit-protocol.md`). The rule guaranteed the miss.
   Not a retraction of a claim; a retraction of a **method choice**, which
   is the harder kind to notice.

9. **"Independent arrival" was a shared channel.** I recorded
   `ai-human-audit-protocol`'s sha256-supersession and three-valued fields
   as independent arrival of this audit's rules — *"two separate efforts,
   no shared code, same rules"* — and offered a 2-way explanation.
   **"No shared code" never established "no shared source."**
   CORRECTION-001 and -002 were already on the record saying exactly that;
   I applied them to the operator's vocabulary and exempted the discipline
   I had adopted myself. Measured: two agent-era passes through one
   channel, 2026-08-14 and 2026-09-09. See `DISCIPLINE-PROVENANCE.md`.
   **Moves this audit's discipline toward house style and away from
   finding.**

### The general form of retraction 8 — statable as a rule before the next pilot

    age proxied for        "earliest aimed-at target"
    the five misses needed "highest articulation density"

These are not merely different. **They are ANTI-CORRELATED by
construction**, because articulation of a method is a later event than the
work the method was first aimed at.

    RULE: in any corpus that documents its own method over time,
          selection by age selects AGAINST articulation.

Not specific to this pilot. Isomorphic to archive-siting bias — the proxy
sits where one property is maximised, not where the signal is. **Known
sign, therefore correctable rather than fatal.** Status: DERIVED (a
reading of the retraction; the retraction itself is this session's).

### Catch attribution — three columns, not one ratio

T-0 originally reported "four of six retractions found by this session".
That merged two different measurements. Corrected:

    #  what                                    caught by
    1  live-figures overcount                  self
    2  shared-relation-set claim               self
    3  C-1 encoding attribution                operator correction
    4  EA-3 second-person voice                operator correction
    5  false-zero regex                        self (unowned join)
    6  gate merge on a shared property         operator correction
    7  Lave 98/59                              cross-party (relaying
                                               session's own retraction)
    8  pilot selection rule                    self, after 5 instances
    9  "independent arrival"                   CROSS-PARTY — a second
                                               party supplied candidate 3
    -  fabrication-discipline grep             self, within-turn, unpublished

    self-caught        4   (1, 2, 5, 8)
    operator-caught    3   (3, 4, 6)
    cross-party-caught 2   (7, 9)

**The self-catch rate is 4 of 9, not 4 of 6.** Two of the nine required a
party outside both the operator and this session. Do not merge those
columns — they measure different things, and the cross-party column is the
one that argues for handing scoring outward.

10. **The cache-dependency detector returned a false all-clear.** Asked to
    sweep for bare terms carried by shared context, I built a detector whose
    "is this defined?" heuristic matched a definitional cue within a ~460
    character window plus a table pipe or a heading anywhere nearby. Every
    file in this repo is tables and headings. **It returned OK on all 23
    terms, including ones used in a single file.**

    **Third instance of operationalizing a concept by its surface form** —
    after the regex (#5) and the fabrication-discipline grep (near-miss).
    This one is the worst direction: it produced an *all-clear*, which
    stops further checking.

    Whether a definition suffices for a cold reader is a **comprehension
    judgement, not a pattern** — the same conclusion F4 forced. `GLOSSARY.md`
    does the fix directly instead of measuring whether it was needed. **The
    prescribed test — hand a section to someone with zero context and see
    where they stop — has not been run and is the only valid one.**

11. **The emptiness-implies-value slide.** See `TRAIL.md`. This repo argues
    for avenue F, the haptic cell and the sensory-taxonomy gap **largely
    from their emptiness**, and emptiness is a follower count. Corrected:
    unoccupied is correctly scoped as a claim about the paved network;
    *worth going* is argued nowhere and must be argued separately.

No A2 file was edited after hashing, including for CORRECTION-001 or -002. The corrections live in
`divergence/` and `PHASE_B.md` (B1-d). The hashes still verify.
