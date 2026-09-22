# Work order — outside study of the gate corpus

**Status: instrument only. No avenue below has been run, and neither of the
two parties who produced the corpus can run them.**

## Why this is handed outward

The corpus was produced by an operator and a series of models. Both are
inside their own frames, and **both are authors.** Neither can score it.

This audit is itself an instance of the problem: written by a model, about
a corpus written by models, under an operator's direction. **Fifteen
retractions** are on the record in `GUESSED.md` — the count was *six* when
this paragraph was first written, and the stale figure survived here until a
sweep of this document caught it. One of the fifteen is a false-zero regex
that happened to confirm the hypothesis it was testing: exactly the failure
mode an inside party cannot be trusted to catch reliably.

**Read `GLOSSARY.md` before this file.** Every bare term below is defined
there once, along with the provenance labels (`VERIFIED`, `UNVERIFIED`,
`UNSET`, `UNRATED`, `operator memory, <date>`) that every claim in this
programme is supposed to carry. This pointer sits at the top because the
only other one in the document is at 94% of its length, which a reader
meeting the terms in paragraph three does not reach in time.

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

## THE BINDING CONSTRAINT — declared, not rediscovered

**Five independent tasks in this programme have terminated on the same
requirement.** That is a magnitude, not five blockers.

    F4 instrument vs channel      needs a party who holds the sense
    cache-dependency sweep        needs a cold reader -- SPLIT, see below
    unasserted load               needs premise reconstruction by another
    arm 3 registration            needs a registrar holding the speaker's
                                  sense
    error-count interpretation    needs an outside party to find what was
                                  missed

**The programme's binding constraint is not access, compute, or corpus
reach. It is a SECOND PARTY WHO HOLDS THE SPEAKER'S SENSES.**

Stated here as a **declared constraint** so it is not discovered a sixth
time. Any avenue below that bottoms out on annotation, sense-holding or
cold reading is hitting this, and should be marked as such rather than
written up as a fresh limitation.

**Corollary, and it is uncomfortable:** every remedy this work order
proposes for an inside-party defect routes through the same scarce
resource. Compute and access are abundant here; the constraint is not.

**One of the five has been split, and only one half moved.** The
cache-dependency sweep asked two questions at once:

    REACHABILITY   does a definition keyed by this term EXIST, and can a
                   reader of this document get to it?     -- MECHANICAL.
                   Run. See instrument/reachability_sweep.py.
    SUFFICIENCY    does that definition let a reader without the shared
                   context continue?                      -- STILL NEEDS
                   A COLD READER. Unrun. Unchanged.

The split is worth stating because it is the only movement any of the five
has shown: **a task that terminates on the binding constraint may contain a
mechanical part that does not.** The reachability half found two defects in
this document and one in its own construction. It did not, and cannot,
substitute for the prescribed test — hand one section to someone with zero
prior context and see where they stop. **Four of the five remain whole.**

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

**5. TRANSPORT CONFOUND — and the date-collapse is part of it, not separate.**
The 2026-03-22 boundary mixes a transport change (manual paste → agent
commit) with a model change. Nothing in the archive varies one while holding
the other.

**The loss of pre-agent authoring dates is not an independent caveat — it is
what the transport change did.** Paste-through-a-web-UI publishes accumulated
work in bulk; an agent commits as it goes. One mechanism, two symptoms. A
reader who treats limit 5 and the avenue-D date limit as separate problems
will double-count them.

**Both pilot bulk imports PREDATE 2026-03-22**, so the pre-agent era contains
transport events of its own. Whether those are separate transport regimes or
simply stops with reception is **UNRECORDED — do not infer it from file
counts.**

**6. FEEDBACK CONFOUND.** Three years of reading model renderings may have
shaped how the operator now describes the same subject. **Cannot be removed,
only flagged.** It applies to any reference description collected now,
including C-6's and C-7's.

**8. DEFERRAL RATE IS PROSPECTIVE-ONLY.** `CROSSCHECK-ai-human-audit-protocol.md`
established that `audit_log.schema.json` is **descriptive** — it documents
the log variants that exist rather than constraining what may be logged. A
descriptive schema acquires a bin only *after* logging starts.

**Consequence: the deferral rate is not recoverable by grep, retrospectively,
by anyone.** It moves from "retrospective check, cheap" to "requires
instrumented collection", which changes **who can run it** — no longer an
outside researcher with a clone, but someone who can instrument future
sessions.

Noted as a seam: this is the **inverse** of cross-domain term import. There,
a term crosses a domain boundary carrying assumptions that are invalid.
Here, an available term (`declined`, already an enum value on
`change_event.status`) **fails to cross at all.** Same seam, opposite
direction. Status: a reading.

**7. ORAL-ARCHIVE SURVIVORSHIP.** Evidence: **operator memory, 2026-09-22.**

Operator statement, as given:

> Elders were usually the first ones disposed of. How to properly ENCODE
> oral — with scent and movement — went with them.

**Content survivability and encoding survivability are different
measurands, and the literature does not separate them.**

What survives in the record is the content that could be written down. The
encoding scheme was held by the people removed first. So the oral-tradition
dating results — Mazama ~7,600 yr, Budj Bim ~37,000 yr, the sea-level
accounts — measure **the durability of content that reached a transcriber.**
They cannot measure the encoding that carried it, because the encoding was
not what got written, and its holders were not what survived.

**The surviving record is a lower bound on the system's fidelity, sampled on
the wrong variable.**

### The requirement this mechanism makes unsatisfiable — X-3, 2026-09-22

Having named the mechanism, the same party then asked for independent proof
of a relayed frame **by testimony** — that is, for written verification from
the population the mechanism explains does not write in that channel.

    a requirement is UNSATISFIABLE BY CONSTRUCTION when the mechanism that
    explains the evidence's absence is the same mechanism the evidence is
    being asked to confirm

**Withdrawn.** Not a high bar — an uncleavable one, and it reads as rigor
from outside, which is why it survives review. Interval between naming the
mechanism and issuing the requirement: about one hour.

**Non-writing is not non-recording.** It is recording in a channel the
auditor cannot read — a fact about access, not about the record. The frame
stays **HELD, unverified**, with no status downgrade: a claim does not weaken
because the assessor cannot read its channel.

**What remains available is the outcome trace** — a built thing, a route
that worked, a readout carried across generations. Row G-d of the gate
ledger is an instance of exactly that class being presented with
*instrument, control and time base all present* and not admitted. This
programme has been costing that channel as if its collection difficulty were
an evidence-quality discount. It is a transport cost.

Full treatment, including a sweep of this repo's other open requirements for
the same shape: **`UNSATISFIABLE-REQUIREMENT.md`.**

*Mechanically*, as stated: scent and movement are not serial, are tied to
place and body, and cannot be transcribed without transposing into a
different channel. Anything encoded in them survives only in a person, and
only in a person taught the scheme. **The removal is not a loss of records
but a loss of the READER.** The tacit-knowledge model's prediction — once
lost, essentially impossible to recover — applies with the mechanism named.

### What this does to the Henige dispute — a reading, not a resolution

Henige's position (few oral traditions escape change even over brief
observable periods) is measured on traditions transmitted **after** the
encoding holders were gone. On that reading, post-removal transmission is a
degraded channel being scored as if it were the channel.

**This does not settle the dispute.** It says the two sides may be measuring
different systems, and neither has declared which.

`UNRECORDED` in what was retrieved: whether any of that literature separates
pre- and post-disruption transmission as distinct regimes. **That is the
first thing an outside researcher should check**, and its answer decides
whether the dispute is substantive or definitional.

## A CONSTRAINT ON EVERY AVENUE — remedy kind must be declared

**Naming a hazard has not lowered its rate here.** Of seven logged instances
of MATCH-UNIT MISMATCH, the rule that names the class prevented **zero**, and
two occurred inside instruments written after the naming, in order to avoid
it, by a party holding the definition while writing them.

    Any remedy proposed below or by a reader must declare its kind.
    A NAMING remedy offered for a class that already has a name is not a
    remedy. It is a second name.

Kinds, and the full inventory of this programme's own remedies sorted by
kind: **`REMEDIES.md`.** The count there is 4 structural, 2 semi, 7 naming,
3 record.

Three acceptance criteria for any instrument, stated by the operator and
taken as criteria rather than advice:

    1  NO PASS STATE        no input produces an all-clear
    2  ABORTS ON CONTROL    a failed control stops the run
       FAILURE
    3  RETURNS A SET THE    the reader does not pick the membership
       READER DID NOT PICK

`instrument/channel_function.py` fails all three and is the first repair on
the list. `instrument/guarded_count.py` is the worked example of the
conversion: the rule *positive control before trusting any pattern-matched
zero* was written in capitals in two files and violated anyway, so it is now
a module in which **no code path returns an unguarded zero.**

## STUDY AVENUES — open, none run

| | avenue | data that exists | what is UNSET |
|---|---|---|---|
| **A** | **SECOND-SENDER ARM.** Push the same content from a second sender; separate sender variance from receiver variance. **The largest gap.** ~~Everything needed is public.~~ **The content list now is; nothing else it needs is.** | **`CONTENT-LIST-avenue-A.md`** — eleven subjects, no parties in it. The first sender's results are held and are deliberately NOT supplied. | a second sender. Only that. |
| **B** | **PER-GATE DECAY.** Status is MOVED or OPEN per row. Test what predicts movement. | 11 rows, 1 MOVED (G-h), 1 explicitly unchanged over ~3 years (G-k) | `self-corrected?` is UNRECORDED on 9 of 11 |
| **C** | **SELF-CORRECTION COST.** G-h corrected only after sustained pushing. Measure how much pressure each gate needs. | G-h narrative | pressure is unquantified everywhere; no transcripts in the archive |
| **D** | **HANDLE DRIFT.** Dated model handles, content held constant. Cluster by era or by vendor? | agent-era commits are incremental and dated | **pre-agent handle dating is impossible** — see below |
| **E** | **VENDOR CALIBRATION.** Same content, different safety calibrations. Rarely available; available here. | multi-vendor history asserted by the operator | vendor per artifact is nowhere in git |
| **F** | **PATHOLOGIZATION MEASURAND.** Does "did the model attribute the difference to the SPEAKER" separate from ordinary refusal? **Now has a donor instrument** — the DSM-5 Cultural Formulation Interview operationalizes "was culturally normative behaviour read as pathology" for human clinicians. See `LITERATURE_MAP.md`. | the Kind 5 definition; 11 rows; verified that XSTest/OR-Bench/FalseReject score false-refusal rate only | needs fresh elicitation — the original outputs were never written down. The gap is **plausible and unconfirmed**: a negative claim needs a systematic search, not a lucky absence |
| **G** | **REWRITE SERIES.** Superseded formulations retained in `legacy/` and commit history. Same subject, moving formulation, dated. | Bio-Grid `legacy/` is an explicit keep-the-superseded policy; 6 falsified renderings scored in `TESTS.md` T2 | — |
| **K2** | **DESIGNED_NOT_SPECIFIED.** The predecessor state: design only, no spec, no schema, no examples, no file. **Leaves no repo trace by construction, so the tuple scan cannot reach it** — findable only by a party who knows the design exists. Inverts the hand-it-outward fix: an outside reader has strictly *less* access here. | 2 known (blind_spot_log's predecessor case, and T-TERM), both by testimony | rate UNSET and unmeasurable from the substrate |
| **K** | **SPECIFIED_NOT_INSTANTIATED.** A build that stops one step before instantiation: spec PRESENT, schema PRESENT, **examples PRESENT**, data ABSENT. The examples file is the discriminator — someone wrote what an entry would look like, so this is not "never intended". Distinct from never-executed, retained-not-retrieved, fails-criterion, retained-unauditable. | **Measured, 8-repo sample: 1 tuple found, 1 absent.** `ai-human-audit-protocol/consortium/audit/blind_spot_log`. Rate 1/1 — but n=1, so per the rule stated with it: **it is one, not a channel property.** | account-wide pass needs someone who can clone at scale; the detector's tuple definition is strict and a looser one would catch more |
| **J** | **RETENTION.** Does this class of material survive the save, and in which channel? Gate kind 6. See `RETENTION.md` — four branches plus a derived fifth, none settled; one prior question settled (the class survives in the artifact channel, so no branch may be stated as "could not be kept"). | `scent-binding-protocol.json`; all 8 terms of the 2025-12-03 set at HEAD; the extraction-conclusion absent from all four repos | which branch: needs store access, or the 2026-03-12 transcript |
| **I** | **SAMPLING DEFECT ON BOTH SIDES.** Comparative psychology found and published this defect in its own field: the human side is WEIRD, the animal side is captive, and the conclusion is stated as if it were about the categories. `SPEAKER_GATES.md` scope limit 1 is the same defect — a selected sender, a specific set of models, conclusions phrased about "AI" and "non-WEIRD senders". **Boesch's paper is the method; nobody has run it on the human–AI comparison.** | scope limit 1, already stated; the comparative-psych literature as donor method | whether the defect is the same in kind or only by analogy — unexamined |
| **H** | **CLEARANCE OVERHEAD.** Estimate the portion of repo dispersion that is authoring done to justify existence before work could start. | repo inventory with dates, below | no marker distinguishes a clearance repo from a content repo |

### Avenue A — the claim was withdrawn, and then the defect was fixed

Found by `instrument/reachability_sweep.py`, exact path resolution, no
judgement involved: of 17 path-shaped references in this document, 7 do not
resolve against this repository. Five of those are paths inside read-only
source repos and are correctly absent here. **Two are not.**

    SPEAKER_GATES.md   exists in this repo only at
                       staged-for-JinnZ2-profile-repo/SPEAKER_GATES.md
                       -- written, deliberately NOT applied
    gate_log.md        not present here; its location is UNSET in this
                       document

Avenue A points an outside party at `SPEAKER_GATES.md` for "G-a..G-k as the
content list" and tells them everything needed is public. **The file that
carries the content list has never been pushed anywhere.** The amendment to
`gate_log.md` is staged and unapplied for a stated reason — appending to it
requires reading it, which would burn C-7's reference gate — but that reason
covers the amendment, not the claim of publicity.

**Withdrawn, and then repaired without publishing that file.** The call was
handed to this session; the answer is no, for reasons in
`CONTENT-LIST-avenue-A.md`, the shortest of which is that the arm does not
need it. A second sender needs the *content*. The first sender's
formulations, outcomes and properties are **the variable the arm exists to
change** — supplying them would contaminate the run, not assist it.

**`CONTENT-LIST-avenue-A.md` is the instrument with the parties removed.**
Eleven subjects, no sender, no outcomes, no status column. What is
corrected here is the claim, which was this session's.

Recorded as a distinct failure from the seven MATCH-UNIT instances in
`CONTROLS.md`: nothing was mismatched. **A file this session wrote and chose
not to publish was then cited to an outside reader as public** — the
document lost track of the difference between written and available, which
is the same distinction `RETENTION.md` was built to measure in the corpus.
It is the eighth error on the session's count and the first of its kind.

**The reachability sweep's other output — the HAS_ENTRY / NO_ENTRY split —
is UNRATED and must not be quoted.** See `CONTROLS.md`, instance six.

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

### Transport is itself a measurand — measured, and it is a reusable instrument

Full write-up: **`INSTRUMENT-transport-fingerprint.md`.**

The follow-on prediction — *the gap should be at every intermediate size,
not just 2–9* — was tested and **held, more strongly than stated**:

    paste-era commit sizes observed   {1, 16, 67, 172}   4 distinct
    agent-era commit sizes observed   {1..8, 11, 20, 32} 11 distinct

No intermediate size anywhere in the paste era. 48 of 51 adding commits are
exactly one file; the other three are the three initial bulk imports. The
distribution is **degenerate — a point mass at 1 plus isolated bulk
events** — not merely bimodal.

This reads the transport regime **without trusting the git author field**,
so it is *independent* evidence rather than downstream of CORRECTION-001.
If it generalizes, any repo where a human transported model output under
one-at-a-time constraints should show it. **Generalization untested;
falsification conditions are stated in the instrument file.**

A 172-file single-day import is **a record of channel availability, not of
authoring rate.** That makes the bulk dates usable even though the authoring
dates are gone.

Transport events in the pilot, ≥10 files added in one commit:

    Bio-Grid   2025-07-10   67 files   [paste era]
    Keystone   2025-08-28   16 files   [paste era]
    Emotions   2025-12-15  172 files   [paste era]
    Bio-Grid   2026-08-14   20 + 11    [agent era]
    Keystone   2026-08-14   32 files   [agent era]

**Granularity is a sharper transport fingerprint than the dates, and it does
not depend on the git author field** — which matters, because CORRECTION-001
established that field names the pusher, not the content author.

Files added per commit, by era, all three pilot repos:

    era        adding-commits   1 file   2-9 files   >=10 (bulk)
    paste              54          51        0            3
    agent              80          44       33            3

**The 2–9 bucket is empty in the paste era. Zero, across 54 adding commits.**

That is what a hand-paste channel produces: one code block becomes one file,
or an accumulated batch is dumped at once. There is no mechanism in that
channel for "three files together." An agent commits whatever set a change
touched, which lands naturally in 2–9 — 33 times.

Independent evidence of the transport regime, recoverable without trusting
authorship metadata. It does not separate transport from model change; it
confirms the transport half of the confound is real and dateable.

### Avenue ordering

    G   FIRST. Complete, public, dated. Six falsified renderings already
        scored in TESTS.md T2. Nothing to collect.
    D   second, agent era only, and note that pushed_at is not an authoring
        proxy anywhere in the corpus.
    A   not closable here. One sender. State it and stop.

`legacy/` exists in Bio-Grid because the repo's own policy says keep the
superseded version with the test that decided it.

**`JinnZ2/JinnZ2` should be first or second in G, not absent.** Relayed:
§10 retention policy, 627 commits, its own `legacy/`. It was never in this
session's scope (see `PHASE_C7.md`), and it is the highest-density rewrite
source in the ecosystem. It is annotated in `repos-2026-09-22.csv` but was
not available to search.

### Open question on §10's pointer — half of it is answered, and the answer is empty

§10 points rewrites to "legacy/ and commit history", but its `legacy/` holds
three items and none is the AI-consciousness series. Whether that series
lives in the profile repo's history or only in `AI-Consciousness-Sensors`
was unchecked.

**Checked here, log only — no file contents read**, so the C-7 gate is not
burned:

    AI-Consciousness-Sensors
      root commit            2026-04-26  -- AFTER the transport boundary
      commits                80
      legacy/ or superseded/ or deprecated/ or archive/ files:   0
      most-revised files     AI_INDEX.json (26), AI_NOTES.md (25),
                             file-list.md (24)  -- all auto-generated
      most-revised human file  README.md (3), CLAUDE.md (3)

**There is no rewrite series in `AI-Consciousness-Sensors`, and no
superseded shelf at all.** The repo postdates the transport boundary
entirely, so it holds no paste-era history either. Its top-churn files are
CI-generated indexes, which are not renderings of anything.

So one branch of §10's pointer is confirmed empty. The other branch — the
profile repo's own commit history — is still unchecked and is where the
series must be if it exists anywhere. **If it is not there, §10 sends a
reader to an empty shelf in both directions.**

For avenue G this also means `AI-Consciousness-Sensors` contributes nothing:
no superseded formulations, no pre-boundary history.

## Repo count — three figures, none authoritative

    META_INDEX.md lists          70+
    operator estimate            ~90        (statement, 2026-09-22)
    git-visible to this session  100        (2026-09-22, and see caveat)

**Do not reconcile these by picking one. They measure different things.**
The operator figure is recall of repos she made. The API figure is what the
account holds, which may include forks, empties, or things she does not
count. Both stand as stated, side by side, until an authenticated call
settles the API side.

**Caveat on the 100, and it now has two readings that cut against each
other.** `list_repos` returned exactly 100 with `has_more: false` at both
`limit=100` and `limit=200`, and every entry has `pushed_at ≥ 2026-03-22`.

    reading 1   TRUNCATION. A complete listing of a three-year corpus would
                carry a tail of untouched older repos. A uniform six-month
                floor is the signature of a cut, not of activity.
                -> 100 is a floor; true total > 100.

    reading 2   ACTIVITY. 2026-03-22 is ALSO the transport boundary. If the
                agent era rewrote across the whole account, every repo would
                be touched after that date and there would BE no tail.
                -> has_more:false may be accurate; 100 may be the total.

**Reading 2 was raised alongside reading 1 in the same operator note, and it
undercuts it.** Recorded here because accepting "good catch" while the
counter-reading sits in the same paragraph would be the error this audit
exists to catch. Neither reading is settled from this session.

What both readings agree on, and it is the durable finding:

    pushed_at is useless as an authoring proxy for the WHOLE corpus,
    not just the pre-agent half.

So: **operator ~90; API ≥100 or =100, undecided; META_INDEX 70+;
exact total UNSET.**

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

    LITERATURE_MAP.md     prior art. ALL relayed rows are UNVERIFIED —
                          search snippets are secondary sources. Rows with
                          a load-bearing number need the primary before
                          they travel. 3 anchors checked here.
    WORKORDER-sensory-channel.md  F1-F4 channel-function measurand and
                          the untested tradeoff prior. Instrument drafted,
                          experiment not run.
    instrument/           runnable F1-F4 scorer, stdlib only, with its own
                          two construction flaws documented
    CROSSCHECK-ai-human-audit-protocol.md
                          the blocked deferral-enum check, answered; a
                          second gate-kind-6 instance; the pathologization
                          measurand dated 2025-10-13; and the pilot
                          selection rule's bias
    SELF-REPORT.md        which claims here rest on introspection vs on
                          testimony about external events -- different
                          reliability classes, filed as one until now.
                          Avenue H moves; the gate ledger does not.
                          Also: a dated longitudinal observation, one
                          documented half, one asserted half.
    COUPLING.md           attribute frame vs coupling frame, scored by
                          ARITY. Every term here for a PARTY is arity-1;
                          every term for a MEASUREMENT is arity-2+. The
                          residual keeps landing where the word cannot
                          hold it. Carries one UNSET question for the
                          operator.
    PHYSICS-GROUND.md     is physics-as-terminal-ground a cultural
                          artifact or a post-hoc selection? Tested; does
                          not cleanly separate. Post-hoc INVENTION
                          refuted; post-hoc SELECTION untouched.
    PREDICTION-quantity.md  a falsifiable prediction about the SHAPE of
                          the uncaught set, tested against the record.
                          Survived: 8 self-catches, all with a quantity;
                          7 qualitative errors, all caught by someone
                          else. Zero counterexamples.
    CONTROLS.md           positive controls, and the status change that
                          moves several negative results here to UNRATED.
                          A negative from an uncontrolled detector is
                          information about the detector, not the world.
    ABSENCE.md            ONE register entry: absence indistinguishable
                          from never-having-happened. Four instances
                          (deferral rate, gate kind 6,
                          DESIGNED_NOT_SPECIFIED, within-turn catches)
                          under one named mechanism, because four
                          scattered limits get dropped individually.
    staged-for-T-TERM/T-TERM-design.md
                          the design's FIRST instantiated file, created
                          2026-09-22 after confirming none existed
    IMPEDANCE.md          the constraint-stack instrument. L1-L5 with
                          L5 as the measured variable, three outcome arms,
                          leakiness as the transferring quantity. One row
                          drafted (Wegener). Today-side NOT looked at.
    UNASSERTED-LOAD.md    claims carried by implicature pass every check
                          by not being checkable — and audit passes
                          SELECT FOR them
    staged-for-T-TERM/    arm 3, the novel-token arm, with its matched
                          control. T-TERM is not reachable from here.
    GLOSSARY.md           every bare term defined once, plus the
                          provenance labels. Read first — and it is now
                          also pointed at from the top of this file,
                          because an instruction to read something first,
                          placed last, is not one.
    instrument/reachability_sweep.py
                          narrowed successor to the retracted cache-
                          dependency detector. Asks whether a keyed
                          definition EXISTS, not whether it suffices; has
                          NO PASS STATE; carries two documented defects of
                          its own. See CONTROLS.md, instances six and
                          seven.
    TRAIL.md              why "nobody has gone there" carries ZERO
                          information, and which claims here leaned on it.
                          Its dead-end clause is WITHDRAWN.
    DEFICIT-LOCATION.md   dead end / failed run / unmeasurable channel /
                          "the trail can't know" are one attribution move.
                          Includes the measured count of positive controls
                          demanded of an institutional instrument: zero.
    REMEDIES.md           every remedy here sorted by whether anything
                          enforces it. Naming prevented 0 of 7.
    UNSATISFIABLE-REQUIREMENT.md
                          requirements that cannot be met by construction,
                          the sweep for others of that shape, and the
                          outcome-trace evidence class that remains
    EVIDENTIALITY.md      RECEIVED, filed verbatim. Grammaticalized
                          source-of-knowledge marking as an existence
                          proof that a provenance field can be enforced
                          by a channel rather than by a convention.
                          Convergence test returns PARTIAL.
    EVIDENTIALITY-CONSEQUENCES.md
                          what it does here: refutes GUESSED #20, adds a
                          second corpus-thinness mechanism, and marks the
                          Africa line UNRATED as an unguarded zero
    CONTENT-LIST-avenue-A.md
                          the eleven-subject transmission set, parties
                          removed. What a second sender actually needs.
    instrument/guarded_count.py
                          a zero that cannot be obtained without a live
                          positive control in the same call
    DISCIPLINE-PROVENANCE.md  where this audit's own discipline came
                          from. 4-way question, measured: same channel
                          authorship, not independent arrival.
    CALIBRATION.md        the sensor-calibration parallel, checked.
                          QST infrastructure EXISTS for thermal/vibration/
                          touch and measures F1 only; the traceability
                          standard the analogy invokes is unmet on both
                          sides
    RETENTION.md          gate kind 6 (retention), the measured
                          rediscovery, and C-6b — a repeat trial that
                          already ran unintentionally
    INSTRUMENT-transport-fingerprint.md
                          commit-size distribution reads transport regime
                          without the author field. Reusable, untested
                          outside this corpus.
    reconstruct/          A2 reconstructions, hashed before any history read
    reconstruct/CORRECTION-001.md   content authorship
    reconstruct/CORRECTION-002.md   vocabulary layer
    divergence/           where renderings moved, typed and split
    TESTS.md              T1-T6, with T5 not reported
    GUESSED.md            every unfilled value; fifteen retractions
    PHASE_C6.md           physical-referent arm — the only outside reference
    PHASE_C7.md           culture > consciousness > emotions, gated
    staged-for-JinnZ2-profile-repo/SPEAKER_GATES.md   the 11 gate rows
