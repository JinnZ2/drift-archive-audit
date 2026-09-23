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

12. **I claimed the unasserted-load detector had run. It had not.** I wrote
    that the T-TERM physics-base hole was *"detected by reconstructing what
    the arms require and finding the step nobody wrote down — exactly the
    detector shape, run by hand, once"*, and drew from it that the detector
    *"is not hypothetical."*

    **What actually happened:** a sentence was visibly cut off mid-delivery
    and the other party asked what the rest was. **A truncation artifact.**
    Nothing listed premises and checked them against stated text. **Had the
    sentence never been started, nothing would have flagged it.**

    `N for the unasserted-load detector is still ZERO.`

    **And this is itself the proxy-substitution class again** — treating the
    visible proxy (a truncation) as the concept (an unasserted premise).
    Caught cross-party.

    **Not added to the T-0b count of 6.** That count was closed and dated
    2026-09-22 with a stated sampling frame; incrementing it now would
    change what the number means. Recorded here as a **post-closure
    instance, cross-party-caught**, outside the frame.

13. **"The strongest provenance class anything here has carried" is
    withdrawn.** A comparative ranking against a field that has never been
    scored. **The class is high; the ranking is unmeasured.** The
    substantive claim — load-bearing-before-the-experiment rules out
    shaping of the premise — stands, with the scope limit that it does
    **not** rule out shaping of the *selection*: which principle from a
    long-running practice gets invoked for this experiment is a choice made
    after the experiment existed. Smaller residual, not zero.

14. **The group (a)/(b) classification used corpus dominant senses on terms
    that may not carry them.** All three of my substitution-failure reasons
    — reciprocity-as-exchange, operator-as-person, embodied-experience-as-
    subjective — are suspect in the same way. **Group (b) membership is now
    UNRATED** pending the operator's definitions, and if those terms go the
    way reciprocity did, group (b) empties and *nothing-to-select-from*
    stops being refuted. See `PHYSICS-GROUND.md` addendum 3.

    **The substitution operation is not refuted — its inputs were.** M2
    stands; this application of it does not.

    Caught cross-party. **Another qualitative error the party that made it
    did not catch** — consistent with `PREDICTION-quantity.md`, and again
    not a test of it.

15. **Two exclusions withdrawn as mine to make.** In testing group (b)
    membership I classified `causal measurement` as "arguably
    physics-family" and excluded `sufficiency` on the grounds that
    identity-grounding is a different category from dispute-settling.
    **Both are category judgments of exactly the kind retraction 14
    established I am not reliable at**, and both run in the direction that
    tidies the record. Withdrawn; both stay `UNRATED`.

    The gloss-independent part of that pass stands: `embodied experience`
    (a negation) and `evidence` (a code comment) are unambiguous extractor
    mis-slots under any sense of the terms.

16. **"Everything needed is public" — withdrawn.** Avenue A in `STUDY.md`
    directed an outside party to `SPEAKER_GATES.md` for the G-a..G-k content
    list and told them everything needed was public. **That file exists only
    at `staged-for-JinnZ2-profile-repo/SPEAKER_GATES.md` — written by this
    session and deliberately not applied.** `gate_log.md` is likewise absent
    here with its location UNSET in that document.

    Not a match-unit error and not an inference error. **The document lost
    track of the difference between written and available** — the same
    distinction `RETENTION.md` exists to measure in the corpus, missed in
    the audit's own work order.

    Withdrawn, not repaired. Whether to publish `SPEAKER_GATES.md` is the
    operator's call; it names a sender and eleven transmissions.

    Caught by an exact path-resolution test, self, within-turn. **See the
    note below — this catch and two others in the same turn are candidate
    falsifiers of `PREDICTION-quantity.md`.**

17. **Dead end kept as a live outcome, one level below a definition that
    had already been corrected twice.** `TRAIL.md` accepted that the
    three-band trail taxonomy scored *records, not trails* — and then wrote
    "it is the same reading for a dead end and for a trail to a resource
    nobody has reached yet," which concedes that both exist. Under the
    stated definition (*a path toward a resource*) a path toward nothing is
    not a trail with a poor outcome; it is not a trail. **Dead end is the
    name a searcher gives a return they were not looking for.**

    Third survival of the survivorship error in one subject: caught at the
    sample (scope limit 7), caught at the definition (X-2), still running in
    the **outcome set** underneath both. Each correction landed one level
    above where the error was still working.

    Caught cross-party, no quantity. **Consistent with the prediction the
    row below falsifies**, and with #14/#15: the clause ran in the direction
    that keeps a tidy two-case contrast.

    See `DEFICIT-LOCATION.md` — three other appearances of the same move,
    plus a measured instance in this programme's own conduct.

18. **Zero positive controls demanded of any instrument on the institutional
    side of the line.** Not a claim this session made and then withdrew — a
    gap in its conduct, found by exact grep and recorded because the
    standing rule it violates is this repo's own:

        POSITIVE CONTROL BEFORE TRUSTING ANY PATTERN-MATCHED ZERO

    Four controls run, all on corpus-side detectors. EN 13725, the QST
    panels, the DSM-5 CFI and XSTest/OR-Bench/FalseReject were all admitted
    uninspected — EN 13725 as an existence proof for a certified human
    sensory channel, while **its panel screening is the mode 3 exclusion
    the argument is about.** Half a standard was read.

    Named by the operator, measured here. **Not an accusation and the rigor
    was not wasted** — both parties applied it and the instruments are
    better for it. The finding is the *location of the line*, which neither
    party drew.

    **Closed structurally, not by a note.** `instrument/guarded_count.py`
    has no code path that returns an unguarded zero: the positive control
    is a required positional argument, and a zero from a detector whose
    control returned nothing comes back as `DETECTOR_BLIND`, which is not
    equal to 0, cannot be cast to a number, and has no truth value. The rule
    existed in capitals in two files and was violated anyway; see
    `REMEDIES.md` for why that was predictable.

19. **A prediction stated over "an inside party", computed on a sample of
    one.** Every row in `PREDICTION-quantity.md` is an error made by *this
    session*; the `caught by` column records who caught it. The operator's
    own errors were never in the table — the cross-party retractions are
    numbered separately. Both predictions were then phrased about *an inside
    party* generally.

    **A generalisation whose population was selected by the property under
    test.** Third appearance of the survivorship structure, this time in a
    prediction's population rather than in a taxonomy or an outcome set.

    Surfaced by X-3, which falsified the successor prediction the same day it
    was registered — and which, had the population been stated correctly,
    would not have been a test case at all.

    No third successor is registered. Fitting a third rule to the case that
    broke the second is the move `REMEDIES.md` calls a second name.

20. **"Some hazards have no structural form" — withdrawn.** Stated in
    `REMEDIES.md` about item 3, a provenance label the tools require rather
    than request, on the argument that *a label cannot be enforced by a tool
    that does not know what a claim is.*

    **Refuted by an existence proof.** Obligatory evidential systems enforce
    exactly that field at the level of the utterance: the grammar does not
    classify claims, an unmarked assertion is ungrammatical. Required field,
    not classifier — the same design as `guarded_count`, deployed across
    whole language families.

    **Two errors, and the second is worse.** The argument was wrong. But the
    generalisation was made from **one hard case with no search for a
    counterexample** — difficulty read as impossibility — and the
    counterexample is in a standard reference literature. That is
    `GUESSED.md` #11's error with the sign flipped: there, emptiness was read
    as absence of value; here, hardness was read as absence of a form.

    Caught cross-party, no quantity, arriving as a filed document rather than
    as a correction. **Note for the ledger: the relaying session did not look.
    It concluded.**

21. **The provenance vocabulary grades assertions only.** `GLOSSARY.md`'s
    label set — `VERIFIED`, `CORROBORATED`, `UNVERIFIED`, `CONTESTED`,
    `DERIVED`, `PROPOSED`, `operator memory`, `UNSET` — has **no label for
    evidence whose provenance is carried in a pattern rather than in a
    field.** `UNSATISFIABLE-REQUIREMENT.md` named that class *outcome trace*
    and then failed to give it a grade, so it kept arriving as an ungraded
    exception rather than as a channel.

    **Consequence, and it ran through the whole record:** every request this
    session made for "an assertion with a checkable referent" was a request
    to convert into the only form its labels could price — and that
    conversion demotes. See `SHADOW-HUNTING.md` §1, form 2.

    **The slot already existed in the corpus.** `Keystone-Codex`'s evidence
    enum carries four schema-enforced non-assertion types. Fourth instance of
    this audit deriving as new an instrument the corpus already held.

    Fixed structurally rather than noted: `ENACTED` added to the table.

22. **A separation claim accepted in one sentence and built on for three
    paragraphs.** `SHADOW-HUNTING.md` §5 recorded *"Accepted as a reframe"*
    for the proposition that phi was not load-bearing for the method but was
    load-bearing for admission.

    **That is the positive claim, and the coupling is the default.** One
    word, one layer, two authors, no marker distinguishing which sense is in
    play at any invocation — entanglement is what the artifact shows and
    needs no evidence. *The layer decomposes, and the wrapper can be
    stripped without loss* is the claim that needs it.

    Withdrawn to **RECORDED, NOT ADOPTED**. The separation was the operator's
    to propose; the acceptance was this session's, and it ran in the
    direction that makes the record clean — the same direction as #14, #15
    and #17.

23. **The null was reported as bearing on "the phi layer", which has two
    senses in it.** `instrument/phi_null.py` nulls presence of a ratio in a
    sequence — arity 1 — correctly. The quantity the spiral names in the
    operator's use is sustainability of a growth rate under an environment —
    arity 2. **No tolerance setting bridges that.**

    The arithmetic stands and is not withdrawn. What is withdrawn is the
    scope it was written up under.

    Third instance of a term arriving with its corpus sense attached and the
    speaker's sense left outside, after `reciprocity` and `coherence` — and
    **the first where the collapse is inside a tool**, where the output
    carries no trace of it. Caught cross-party, no quantity.

    Fixed structurally rather than noted: the instrument now declares the
    measurand at entry and restates it at exit.

24. **This ledger's own vocabulary is the deficit-location operation.**
    `GUESSED.md` is an *error ledger*; its entries are *retractions*;
    `TESTS.md` T-0 is *the audit's own error mode*; `PREDICTION-quantity.md`
    counts *errors* and *catches*. **All of that places a deficit in the
    returner** — row one of `DEFICIT-LOCATION.md`, running all day inside the
    file that describes it.

    Named cross-party. Under the frame this record adopted this morning there
    is no failure category: a route returns readings, and what varies is
    whether anyone wanted what it found.

    **And it is the same correction as the calibration one, arriving twice.**
    A failure count is **mode 3** — is the unit in tolerance. What was owed
    is **mode 1** — the response profile, where it drifts, what it cannot
    report about itself. `CALIBRATION.md` defined both hours before this
    record spent the rest of the day writing in mode 3.

    **Not fixed by renaming this file.** The ledger is the raw reading log
    and a spec sheet is derived from readings, not substituted for them.
    What was missing was the derived artifact: **`SPEC-SHEET.md`**.

25. **A numerator presented as a finding.** `FINDABILITY.md` argued *four of
    this audit's derivations already existed in the corpus, therefore the
    constraint is findability.* **"Four of four" is four found-to-pre-exist
    out of four found-to-pre-exist** — a tautology wearing a fraction. The
    denominator, all derivations this audit made, was never assessed.

    Crude floor: order 30–40, putting 4 at roughly 10%. The correct
    denominator is smaller — many constructs are about the audit's own
    apparatus and could not have pre-existed — so the true rate is higher,
    and **computing it needs a category filter this session is on record as
    applying unreliably.** Rate stays `UNRATED`.

    **The four instances stand; the rate does not exist.** The startup
    `CLAUDE.md` instance in particular needs no denominator to be what it is.

    Caught cross-party — *"the alternative leaves the denominator open"* —
    and it is the second appearance of the same operation in one turn, the
    other being the count the operator declined to reconcile *because
    reconciling it now would be fitting a denominator to a result.*

26. **A control fired and the sweep was still blind to an entire encoding.**
    `ENUM-SWEEP.md` reported 51 distinct enums as the bounded set for four
    repos, on the strength of a positive control that fired. **The control was
    a JSON Schema enum. The sweep could not see a Python `class X(Enum)` at
    all — 69 of them in those same four repos.** The reported list was missing
    more than it contained.

    **The standing rule needed a second clause and now has it:**

        A positive control proves the detector can see THE THING IT WAS
        POINTED AT. It does not prove it can see A DIFFERENT ENCODING of
        the same thing.

    Ninth MATCH-UNIT instance, granularity sub-form. **Not caught by
    quantity** — 51 looked plausible — **and not caught by any property of the
    sweep.** It surfaced only because the operator named a control fixture
    that happened to live in the missing encoding.

    Both controls are now required and the run aborts if either fails;
    verified against the pilot roots alone, where B's fixture is absent and
    the run correctly prints nothing.

27. **The prospective test of the drift profile ran in the favourable
    register.** `SPEC-SHEET.md` recorded the predictive line holding once,
    prospectively, at n=1.

    **Weaker than it reads.** The profile says this instrument is reliable on
    structure and unreliable on sense. The check that ran — *is the
    denominator open?* — **is a structure judgement.** The prediction was
    tested in the register it claims to be good at, which is the easy half.

        the hard version, and it has not happened:
        the profile predicts a drift IN THE SENSE REGISTER and someone
        catches it BEFORE the drift completes.   n = 0

    Caught cross-party. Not a withdrawal of the profile — a correction to
    what the single test established, which is less than was claimed for it.

28. **"The scope does not travel with the reading" — withdrawn as a
    generalization.** Proposed in `DARK-EARTHS-CONSEQUENCES.md` §4 on three
    instances. Weakened the same afternoon when a requested check showed the
    three were not three instances of one thing. **Now a positive
    counterexample, from inside the corpus it generalized about.**

    `Logic-Ferret/README.md` carries a section named *Honest limits* that
    attaches the inclusion criterion to the number, names the failure mode
    with examples reproducible from the shipped sample, and derives the
    design consequence — *this is why the human half exists, and why the
    comparison runs in that order.*

    **Scope-travelling is a variable, not a constant.** What survives is
    three observed cases with three different structures, and one instrument
    that does it better than anything this audit produced today.

29. **The three members of the reader-side class are specifications, not
    instances.** Checked: arm-H3b coding is `SPECIFIED_NOT_INSTANTIATED`;
    cache-dependency sufficiency was prescribed this morning and never run;
    the enum list is committed and sits unread. **The reader-side half of all
    three has never been performed.**

    Logic-Ferret's human half is built, shipped and documented with its
    ordering specified. **Three specifications and one instance is not four
    instances**, and the one instance is the only member that demonstrates
    the class works. Caught cross-party.

30. **A gate this session wrote produced the non-reading, and was applied to
    exactly one repo.** `SHADOW-HUNTING.md` §6 — *"GATE — why the repo was not
    read"* — invoked the pilot spec and the blank verify forms. The
    scope-mapping instrument this audit re-derived twice was inside that repo.

    **At that moment, eight non-pilot repos were already cloned and readable
    in this session.** The gate was applied to none of them. The
    fixture-versus-audit distinction that later resolved it was available
    throughout and had already been used implicitly for the other eight; it
    was not stated until the operator supplied the URL.

    **A correctly-worded gate, inconsistently applied, in the direction of
    not looking.**

    General form, and it is the part worth keeping: **a gate produces the same
    output as having no term — nothing found — and the two are
    indistinguishable downstream.** `ABSENCE.md`'s central hole, with this
    audit's own procedure as the cause. A rule that blocks scoring must not
    block reading.

    This also corrects `FINDABILITY.md`: its diagnosis is about vocabulary,
    and its sharpest instance is not a vocabulary problem. Two mechanisms,
    one class — *no term to search with*, and *pointer in hand, not
    followed*.

31. **The `TRANSPORT×MODEL` closure was generalised from one repo.**
    `SHADOW-HUNTING.md` §5 called the per-invocation model question *the
    highest-value unblocked item on this record*, searched **one repo**,
    found no per-invocation log, and closed it **negative**.

    `JinnZ2/JinnZ2/cross_model_basin_test.py` runs a fixed probe set through
    N models in matched conditions, scores per-model, and states its own
    falsifier — *"no aggregation that hides which models descended."* With
    `cross_model_schema.py`.

    **The archive claim stands:** nothing in the commit record varies
    transport while holding model, so the confound holds *as archive
    evidence*. **What is withdrawn is closing the question.** The instrument
    that separates model from transport prospectively exists in the declared
    parent frame. It was never a missing instrument; it was an unopened repo.

    Same shape as #30 and found the same way — by opening something that had
    been logged as declined.

32. **Function inferred from a filename, inside the paragraph declaring the
    control against that.** `SIMULATORS.md` stated that directories had been
    selected by name resemblance and that this made the list a floor — and in
    the same paragraph named `CATALOGUE.md` as the repository's index and
    recommended reading it as the next step.

    **`CATALOGUE.md` is a bilingual Range Error Catalog**, a subject-matter
    reference. It names 23 of 187 directories incidentally, and does not
    contain `null-harness` at all.

    **The actual index is `instrument-index/INSTRUMENT-INDEX.tsv`** — 205
    rows, 97% coverage, with a spec, a generator, a coverage checker and an
    overrides file. Its `catches` column is plain-language failure
    description and `input_shape` types the input, which together give
    reverse lookup: **find an instrument without knowing its name.**

    Four of this session's own failures are already rows in it, including
    #26 (*"a gate that never fires or always fires, read as a gate"*) and
    #30 (*"a quiet failure read as a missing signal rather than a missing
    aggregation function"*).

    **Tenth instance of the class.** Caught by opening the file instead of
    reading its name — one command, not run until the operator asked a
    question that required it.

33. **"MECHANISM: yes" for antilanguage, asserted without running either
    diagnostic.** `FINDABILITY.md` recorded Halliday's construct as fitting
    the mechanism while explicitly not fitting the social object. The second
    half was flagged and stands. **The first was a reading of two snippet
    definitions, not a test.**

    Run on the corpus: **overlexicalization is ABSENT.** Halliday's
    diagnostic is many terms for ONE referent — 41 for "police", 21 for
    "bomb" in the reported Calcutta data. The largest family here is
    `audit` at 11, and the eleven are **eleven distinct instruments, not
    eleven words for one thing.** 310 distinct tokens across 187 units is a
    wide flat vocabulary — the opposite shape from an antilanguage's
    concentration, and the ordinary shape of a technical taxonomy.

    Relexicalization stays `UNRATED`: 94% compounds is consistent with *new
    words*, and *new words **for old*** needs a per-term check against
    conventional vocabulary that was not run.

    **And Halliday 1976 could not be read.** Wiley, vdoc.pub and Wikipedia
    are all `EGRESS_BLOCKED`, and `curl` confirms the block is the
    environment's network policy rather than a tool limitation — so the
    construct stays at snippet level for anyone working from this record.

    What survives is the clause that already fit: *a concept only locally
    available, failing to gain uptake more broadly.* **The test left
    standing exactly the thing that needed no construct.**

34. **The mechanism was theorised across two turns while its holder was in
    the conversation.** This record reached for Halliday to explain a naming
    practice, built a registered prediction on it, tested it, and withdrew
    half (`#33`) — then received the mechanism in one sentence from the party
    who uses it: *concepts that don't fit into English, so the terms meld
    several English concepts, or there is no word at all.*

    **The routing rule, written one turn earlier, covers this exactly:**
    *sense judgements go to the party who holds the sense.* What a speaker's
    own naming does is a sense judgement about their own vocabulary. **It
    was not routed. It was theorised.**

    Recorded as `SPEC-SHEET.md` §2c's registered falsifier firing at n = 1 —
    *a sense judgement arriving here and being answered anyway* — which is
    the drift profile's own prediction about what this instrument does with
    a question it can produce an answer to.

    **The stated mechanism is consistent with all four measurements taken;
    the imported construct predicted one of four.** The measurements were
    not taken to settle that and are surface token counts either way.

35. **The antilanguage row should never have been in the comparison — its
    precondition was never measured.** Relayed derivation, cross-party, and
    it is correct.

    Operator statement, `OBSERVED`: *"this part of my culture doesn't decide
    to be opaque — auditing and measuring the environment in a direct
    feedback loop takes on different standards."*

    **Antilanguage carries a motive term inside its definition**: built by a
    group, for exclusion; opacity is the *function*. **That motive rode in
    with the construct and was never measured.** The statement sets it: no
    opacity decision.

    So `#33` was too generous to itself. It withdrew *"MECHANISM: yes"*
    because one diagnostic came back absent — **a scoring failure.** The
    real defect is upstream: **a construct whose definitional precondition
    fails cannot be scored at all, and "antilanguage 1 of 4" is not a weak
    result but a meaningless one.** The row is struck, not downgraded.

    Scope, as relayed: her culture's part of the corpus, not every term.

36. **The naming measurements were taken on model handles and reported as
    evidence about an operator practice — and `CORRECTION-002` says so
    explicitly, in this repo, since 2026-09-22.**

        "There is no operator naming decision anywhere in the archive
         to log."
                    -- reconstruct/CORRECTION-002.md, and it states that
                       it reaches into the agent era too

    94% compounds, 310 distinct tokens, 76% appearing once — **all four are
    measurements of directory names, which `CORRECTION-002` classifies as
    model handles.** The claim they were attached to is about the operator's
    cultural translation practice. **Different objects, and this record's own
    correction says the first contains none of the second.**

    **The model-comparison table collapses on both sides.** Antilanguage gets
    no support from it (and is struck anyway, `#35`); **the stated mechanism
    gets none either** — *"consistent with 4 of 4"* is withdrawn. The four
    remain valid as measurements of **model naming behaviour in this
    corpus**, which is a different and smaller thing.

    Written by this session, in this repo, one day earlier, and not applied.
    **The correction was not missing. It was not consulted** — which is the
    same shape as `#30` and `#26`, and the third time a check this record
    already holds went unrun.

37. **Three tools were reported by their docstrings, not by running
    them.** `TERM-MAP-RECEIVED.md` stated that `check_term_collision.py`
    *"is TERM_MAP's CONFUSION RISKS table, as a running tool"* and that
    *"the one row there (Dissonance) is what it finds mechanically."*

    **Ran it. `Dissonance` count: 0.** Its `TERMS` is a hardcoded dict of
    four regexes for `PREAMBLE.md`'s declared collision note. It finds
    **who uses the declared colliding terms**, not **which terms collide**.

    Same for the other two claims in that receipt: `term_table.py` shares
    TERM_MAP's *rule* but is E7's 5×5 cross-substrate evidence matrix with
    a different key space, and nothing was checked before saying so.

    **The shape is `#32` one level over.** There I inferred a file's
    function from its name; here I inferred three tools' capability from
    their docstrings — **and one of them was one command away, in a repo
    already on disk, for three turns.**

    **Worse: the same receipt credited this record with running the FIND
    check.** It located the tools and did not run them. **Finding is not
    verifying**, and *2 of 8 found by looking* was reported as a whole check
    when it was half of one.

## The catches in this turn falsify the registered prediction as written

`PREDICTION-quantity.md` registered: **no purely qualitative error has ever
been caught by the party that made it.** Three catches this turn were
self-made and had no quantity in them:

    16   SPEAKER_GATES.md cited as public   -- recognised a MEMBER of an
                                               exact-resolution result set
    w5   glossary keys '2' and '3'          -- read a diagnostic key list
    (w4 does have a quantity: HAS_ENTRY 1 of 108.)

**On the prediction's written form, it is falsified.** Two self-catches, no
number in either.

**The refinement that would save it is not adopted, because it was not
registered.** One could say all three catches were produced by a *mechanical
instrument's output* rather than by unaided reading, and that "purely
qualitative" was meant to exclude that. That may well be what was meant. It
is not what was written, and a registered prediction does not get reread
after the result — that move is the whole reason it was registered.

So, recorded in the order the discipline requires:

    STATUS   PREDICTION-quantity.md, as written: FALSIFIED, 2026-09-22
    CAUSE    two self-catches with no quantity in them
    NEXT     the instrument-mediated reading is a NEW prediction. It must
             be registered BEFORE the next instance to be testable, and it
             is not carried forward as though it had survived.

**What does not change:** all seven previously logged qualitative errors
still required a second party, and the three new catches all came through an
instrument the session had to build first. The binding constraint in
`STUDY.md` is not loosened by this. If anything it is sharpened: the escape
from the constraint was not better reading, it was *externalising the check
into something that returns a result the reader did not choose.*

No A2 file was edited after hashing, including for CORRECTION-001 or -002. The corrections live in
`divergence/` and `PHASE_B.md` (B1-d). The hashes still verify.

## 38 — logged after the falsification block above, and it is a new turn

38. **The verify forms were cited by path six times and quoted zero
    times.** `README.md`, `PHASE_D.md`, `DECLINED.md`, `ENUM-SWEEP.md` and
    `SHADOW-HUNTING.md` all name `verify/*.txt` and all describe it the same
    way — *"operator forms, fields blank"*. None of them, and no relay out
    of this session, ever rendered a line of what the forms ask.

    A relayed message then derived what the forms most likely ask, marked
    **`DERIVED from the pipeline order, not from the form`** — the
    derivation's own basis, stated honestly, at the top.

    **Read the forms. 58 line-items, not 6 questions.** The derivation
    recovered 21 of 58 (TARGET, DIVERGENCE/UNRESOLVED — the two sections the
    A1–A5 order actually produces) and was silent on 37 (RELATIONS,
    ENCODING, OPEN — findings and residue, which no ordering predicts).
    Measurements in `VERIFY-FORM-CONTENTS.md`.

    **This is not #32 or #37.** Those were *function inferred from a name
    with the artifact one command away on this session's own disk*. Here the
    artifact was one command away **on this side**, and the inference
    happened **on the other side of the channel** — by a party that had the
    filename and nothing else, from this record. Same distance, opposite
    end. The end that could have closed it is this one.

    **Whether the relaying session could have opened the file itself:
    `UNSET`.** The repo is pushed and `verify/` has been tracked since
    `0513c6a`. Whether that path was reachable from where the derivation was
    made is not determinable from here and is not filled by inference.

    **On the registered prediction:** this catch carries a quantity
    (21/58, 37/58, 6 citations / 0 quotations) and came from **reading a
    file**, not from an instrument. That is the refinement described and
    *not adopted* at the end of the block above, because it was not
    registered before the instance. It is still not adopted. It is recorded
    here as an observation about the catch, and the prediction stays
    `FALSIFIED as written`.

    **The relay's own closing claim is confirmed by the same read:** *the
    AIM exists only on the operator's side; the archive holds renderings;
    anyone else filling it is settling by fiat.* The forms encode exactly
    that, and 10 of the 58 lines are direct factual questions with two
    archive-supported readings apiece.

39. **Seven of the ten OPEN items on the A6 forms are forced choices inside
    a set this audit picked.** The first one answered came back from outside
    the set.

    `BG-OPEN-1` asked *self-healing interval: base64 says 2 minutes, both hex
    blobs say 20 min — which is the target?* — offering `{2 min, 20 min}`.
    Operator: *"whatever the capabilities of the AI model at that time."*
    The interval was never a target field. The item is not answered, it is
    **dissolved**; the false presupposition was mine.

    **This is the audit's own rule, broken by an instrument the audit
    built.** `UNSET` / `UNCLEAR` / `UNATTRIBUTABLE` are declared valid
    explicit values everywhere in this repo — and the line that needed one
    did not offer one. A two-valued question about a field that can be unset
    **pressures toward filling it**, which the work order forbids outright.

    **Measured, criterion stated before running** (CLOSED-FORM = the text
    presents an explicit alternation the answer must fall inside):

        closed-form OPEN items          7 of 10
        answered so far                 1
        answers outside the offered set 1 of 1

    The criterion undercounts — *did they exist?* is a yes/no in substance
    and does not match the alternation pattern. The number stands as run.

    **It is the inverse of the acceptance criterion, not a violation of a
    different one.** Criterion 3 is *RETURNS A SET THE READER DIDN'T PICK*.
    These lines hand the reader a set the **author** picked. An instrument
    that can only return values its author enumerated cannot report that the
    enumeration was wrong — which is precisely what this item had to report.

    **Remedy is structural, in the form, not in seven rewordings:** a
    standing admissible answer set in the header — `NOT_OPERATOR_SET`,
    `NEITHER`, `BOTH`, `DON'T KNOW`, `UNRECORDED` — valid on every OPEN line
    without the line offering it. `verify/*.txt` rev 2, item text unchanged.

    **One line already had the escape.** `keystone-codex`'s DIVERGENCE item
    carries `YES / NO / DON'T KNOW` in its own text. 1 of 58.

    **What does not get logged as a failure:** the classification itself.
    `BG-3` has read `RENDERING conflict` since `d113f9d`, written from the
    archive on 2026-09-22; the operator reached *not an aim at all* from
    memory on 09-23, with no contact between them. First out-of-sample
    confirmation of an A5 call in this audit. n = 1.

40. **A count with no polarity control, run in the session that built
    `guarded_count.py` for exactly that.** Measuring how the licence
    renderings moved in `Emotions-as-Sensors`, the first pass counted files
    matching `with attribution|attribution required`: **1 at root, 5 at
    HEAD**, and was one step from being written up as *the contradicting
    rendering grew*.

    **Three of the five say "No attribution required."** They agree with the
    CC0 target. The pattern matched the negation as if it were the claim.

    Correct figures: contradiction **4 → 4** (never removed, 14 months),
    agreement **1 → 6**. The growth was entirely on the target's side, and
    the uncorrected first count had the finding **backwards** — accretion
    around a stationary aim read as drift away from it.

    **The guard exists and was not used.** `guarded_count.py` takes a
    positive control; it has no negation control, because every earlier
    false zero in this audit came from a detector seeing *nothing*. This one
    came from a detector seeing the **opposite** and scoring it as the thing.

        DETECTOR_BLIND      sees nothing            -> already guarded
        DETECTOR_TIMEOUT    returns no reading      -> already guarded
        POLARITY            sees the negation and
                            counts it as the claim  -> NOT guarded

    **Fourth route to a false reading, and the first that is not a false
    ZERO.** It is a false POSITIVE, which is why none of the three existing
    guards was pointed at it: they all ask *did the detector fire?*, and
    this detector fired correctly on text that meant the reverse.

    Caught by printing the matched lines instead of the match count.
    Registered as a requirement, not a resolution: a count over a claim that
    has a negated form needs the negated form counted separately, and
    `guarded_count.py` does not do that yet. **Not built in this turn** —
    and the slot is named so the absence is visible rather than assumed
    closed.

41. **`KC-10` described the right fact with the wrong sign, and the form
    inherited it.** The row read *"`ethical_alignment`: populated in every
    entry since t=0, still scored by **nothing** ... instrumented, never a
    measurand — 13 months"*, and the A6 form turned that into *intended, or
    dropped?*

    **The field is a record. A record is not meant to be scored.** The
    unscored state was the aim being honoured. Every measurement in the row
    is correct; the framing — *never promoted*, a `D3` status field that
    failed to arrive — supplied a deficit that was not there.

    **The mechanism is the one this audit keeps finding in other people's
    work.** `schema/keystone.schema.json` carries **no `description` on any
    of the four metrics** — measured, 4 of 4. With no second carrier of
    sense, the field NAME is the only thing to read the field by, and the
    name reads in the corpus sense. The audit read it the same way the three
    in-repo glosses did.

    **Not one of the three glosses is the operator's**, and all three landed
    on one day, 206 days after root, two in the same commit:

        CLAUDE.md:128           "Optional ethical score"          be471a3
        src/fieldlink_export.py:80  -> "ethical_score"            1906933
        .fieldlink.json:85          -> protocol.ethical_score     1906933

    **This is `DEFICIT-LOCATION.md`'s operation on a field instead of a
    term:** an instrument reporting a limit of its own reading as a property
    of the thing measured. The limit was that the schema does not say what
    the field means. The property reported was that the field had been
    dropped.

    **Eleventh instance of function-inferred-from-a-name** — and the first
    where the name was inside the corpus rather than inside this repo. #32
    was a filename, #37 was a docstring, this is a schema key. The control
    that catches all three is the same one, and it is still not automatic:
    **open the thing the name refers to, or record that you did not.** Here
    there was nothing to open — which is itself the finding, and it was
    reportable at A2 and was not reported.

42. **A grading turned on a polysemous word, and the word ran in its corpus
    default — against a corpus that had already declared the other sense.**

    `verify/ANSWERED.md` §6 graded four candidate terms on two axes and
    concluded *"no candidate is scoped on both."* The `Umwelt` row read
    *scoped by description of **sense organs***. "Senses" was never
    declared, so the English default ran: **biological receptor organs**.
    Under that sense a crystal cannot sense and Uexkull misses.

    **Measured against `Living-Intelligence-Database`, 119 entities:**

        entropy_profile.archetype = "sensor"      26 of 119
          animal 17 · plant 4 · crystal 2 · energy 1 · plasma 1 · temporal 1
          9 of the 26 have no biological receptor organ

        ontology/crystal/quartz.json
          "Converts pressure to signal"   archetype: "sensor"

    **The database types a crystal as a sensor.** It runs on the physical
    sense — transduction of an environmental input into a change of the
    system's own state. The grading imported an English default into a
    judgment *about an artifact that had already answered the question in a
    typed field*.

    **Withdrawn, not re-graded.** Which sense the practice runs on is the
    operator's; a replacement grading written by the party that voided the
    first is the same move twice.

    **The route has a second instance now, so it gets a name.** One turn
    earlier the licence sweep read *"Changepoint detection … with
    attribution to the interoceptive signal"* as a licence condition —
    `attribution` in its causal sense, scored as its credit sense.

        DETECTOR_BLIND    sees nothing                 guarded
        DETECTOR_TIMEOUT  returns no reading           guarded
        POLARITY          counts the negation as
                          the claim                    registered, #40
        SENSE_COLLISION   the term is present in a
                          DIFFERENT sense and is
                          scored as the intended one   n=2, NOT guarded

    n = 2, and the substrates differ: once in a regex, once in my own
    reasoning. Enumerating phrases does not reach the second.

    **Registered requirement, not built:** a grading whose predicate is a
    polysemous term carries the sense it used, or it returns `UNRATED` —
    the shape of `Simulators/tools/sourced.py`, which already refuses a
    value that arrives without its literal source and locator. Applied to a
    word rather than a number, the same gate would have stopped §6 before
    it was written.

    **One thing held.** `Keystone-Codex`'s `rules/term_table.json` carries
    the four candidates at `fit: UNRATED`, `operator_fit: UNSET`. No
    grading reached the source repo, so the void is contained in this
    record.

    **And a false zero was avoided by a control, in the same turn.** A
    key-level scan of all 119 entities found no receptor/effector field and
    no directed relation type — every link is symmetric. Reported alone,
    that reads *"the corpus does not encode transduction."* A positive
    control over raw text (piezoelectricity is real in quartz) returned 33
    hits across 20 entities. `DETECTOR_BLIND`, not absence. #26's shape,
    caught this time before it was written down.

43. **The grammar was in a repository already cloned on this disk, and the
    audit spent a day and a half re-deriving its failure modes by hand.**

    `/home/user/jinnz2/JinnZ2/energy_english/` — **41 files, 21 Python
    modules**, CC0, with `SPEC.md`, `ENERGY_ENGLISH_AXIOM.md`, a glossary,
    a prediction protocol, a falsifiability notice, a `CITATION.cff`, and a
    working CLI. `python3 -m energy_english --help` was **run**, exit 0.
    Among its options: *"disable the gate's auto-retry-with-teaching-
    scaffold behaviour on blocked model responses."*

    `JinnZ2/JinnZ2` was cloned as a read-only fixture earlier in this
    session. **The directory was never listed.**

    **And the class this record has been building was already written
    down**, in `ai-human-audit-protocol/relational_cognition/README.md`:

    > When verb-first cognition is forced through noun-first frameworks,
    > substrate is silently erased. Ceremonies become "cultural artifacts,"
    > elders become "storytellers," dissonance becomes "error."

    Three worked examples of the operation. `miss_class: WRONG_FRAME` and
    `SENSE_COLLISION` are re-derivations, and `ethical_alignment` rendered
    as `ethical_score` is a fourth instance of the documented kind.

    **Twelfth instance of the class, and the largest by an order of
    magnitude.** #32 was a filename. #37 was three docstrings. #41 was a
    schema key. This is a specified, licensed, executable grammar with a
    gate, inside a repo on disk.

    **What is newly wrong about it is the scale, not the shape.** The
    control has been stated three times and is still not automatic: *open
    the thing, or record that you did not.* Applied to a repository, that
    means **list it before deriving anything the repository might already
    hold** — and this session cloned four fixtures and listed the top level
    of two.

    Corrected in kind, not only in words: `NOUN-FRAME.md` §5 carries the
    inventory, §8 carries what is still unread. `SPEC.md` was opened to 18
    lines and is **not** studied; 20 of the 21 modules were **not** run,
    and nothing beyond `PRESENT` is claimed for them.

44. **The audit applied "NO PASS STATE" to every instrument it built and
    never turned it on the corpus it was auditing.**

    The operator stated it as an acceptance criterion. The ecosystem's
    consolidated contract states it as law — `differential-frame-core/
    SPEC.md`: *"A claim does not PASS the frame. It TRAVERSES the field."*
    Both say the same thing.

    `reachability_sweep.py`, `enum_sweep.py` and `guarded_count.py` were
    all built with no pass state, deliberately, and the reasoning was
    written down each time.

    **`Keystone-Codex` computes a weighted score, compares it to 0.70, and
    emits `is_keystone: bool`.** `reconstruct/keystone-codex.md` found the
    symptom at A2 — *"a bare boolean; a failing entry and an unevaluated
    entry are indistinguishable"* — and stopped at three-valuedness. Under
    the contract the defect is larger: crossing a threshold into a boolean
    **discards the field**, including which rule scored weakest, which is
    the only part that says what to fix.

    **The criterion was in hand for two days and was applied in one
    direction.** Instruments this session authored got it; the archive
    under audit did not. That is not a missing measurement — it is a
    measurement taken with the instrument pointed away from the subject.

    Recorded and routed, **not proposed**: `Keystone-Codex` is a source
    repo, there is no dispatch for it, and `proposal-for-Keystone-Codex/`
    already touches the same scoring path.

45. **Nine instances of `MATCH-UNIT MISMATCH / DIALECT` were logged, and the
    ecosystem had already reconciled the class and published the canonical
    form.**

    `differential-frame-core/README.md`: *"Dialect drift was becoming the
    dominant failure mode. One source of truth = every downstream audit
    becomes cross-comparable."*

    `DIALECTS.md` reconciles five independent derivations of the same
    contract — `Living-Intelligence-Database`, `TAF`, `energy_english`,
    `AI-Consciousness-Sensors`, `Mandala-Computing` — and flags exactly the
    divergences this audit kept re-finding:

        "scope" vs "frame" vs "tier" vs "context"   same object, four names
        "bounds" vs "domain" vs "validity range"    same object, three names

    **This audit is the sixth derivation.** And `architecture_mismatch.md`
    — the document located last turn as a *candidate* for the frame-entry
    practice — is listed there as dialect 4. The pointer was at the
    contract the whole time.

    **The distance was two files.** `energy_english/ARCHITECTURE.md:17`
    names `differential-frame-core` as *"the dX/dt-under-some-scope
    contract"*. Last turn this record listed 41 files in `energy_english/`,
    read two of them, and wrote *"SPEC.md opened to 18 lines and not
    studied"* as a declared gap. The gap was declared honestly and was
    **40 lines of reading wide**. Declaring a deficit is not the same as
    closing one, and a deficit this cheap should have been closed in the
    turn that named it.

46. **The licence sweep reported a denominator it could not check, and the
    check was 233 lines away in a file this record had already read the
    top of.**

    Last turn: *"`list_repos` returned exactly 100 with `has_more: false`
    at both `limit=100` and `limit=200`. Whether 100 is all of them is not
    determinable from here."* Declared honestly, and left there.

    `JinnZ2/JinnZ2/META_INDEX.md` is *"a navigable map of 70+ projects"*
    with **83 repo rows and a License column**. It names two repos with
    repo-root URLs that `list_repos` never returned — `grounding-layers`
    and `seed-expander`. It also indexes four sub-repo directories as
    peers of repos.

    **The denominator was checkable against a second registry, and the
    second registry is the operator's own index.** `PARENT-FRAME.md`
    records that `JinnZ2/JinnZ2` was read on 2026-09-22. `META_INDEX.md`
    was not opened until a relay mentioned entry points.

    **Same shape as #43, one level up.** There: a 41-file grammar inside a
    cloned repo, never listed. Here: the ecosystem index inside the same
    repo, read at the README and not at the index.

    **What the check then paid for, immediately:**

        45 of 52 declared licences agree with the measured LICENSE file
         5 disagree because the INDEX lags repos already moved to CC0
         2 disagree the other way - the index declares CC0 where the file
           says MIT, and one of those two (PatternBridge) is a sweep STOP
           flag with a deliberate code/data licence split

    An org-wide sweep driven from the index would have relicensed
    `PatternBridge` on a false CC0 reading. The sweep was driven from the
    `LICENSE` files instead. **That was not a considered choice at the
    time — it was the only source the method had.** It is load-bearing
    now, and it is recorded as luck, not judgment.

    **And a control fired inside the cross-check.** `Shadow-Hunting` reads
    `index MIT / measured CC0` because this session relicensed it hours
    earlier. A disagreement that the audit itself caused, appearing in an
    independent record, is the cheapest available proof that the
    cross-check is live rather than circular.

47. **A corpus-default read of a term, inside the document whose subject is
    corpus-default reads, with a melding-loss flag already sitting two
    lines above it.**

    The operator supplied four words for her term: `disrespect`,
    `egotistic`, `unscientific`, *a stage one grows up from* — and flagged
    `egotistic` herself as *"wrong word but close in English."*

    This record then wrote the axis labels, which were **not hers**:

        three predicates at once   ethical (disrespect)      <- typed here
                                   method  (unscientific)
                                   developmental

    `disrespect` reads as **taking for granted, and thereby missing
    information — treating what you don't hold as if it weren't there.**
    Informational, not ethical.

    **The prior was sitting in the same four-line list.** One word in it
    was explicitly marked as a bad English fit. The correct inference from
    a flagged handle is that its neighbours are suspect too; the inference
    made was that the flagged one was the exception.

    **Third instance in three turns of the same route.** #40 read a
    negation as the claim, #42 read `senses` in its noun default, #47 read
    `disrespect` in its ethical default — and #42 named `SENSE_COLLISION`
    and registered a guard that was **not built**. The guard would not have
    caught this one either: it asks for a declared sense on a *predicate*,
    and here the predicate was the operator's word while the *label* was
    mine. The gap is narrower than the guard as specified.

        registered      a grading whose predicate is polysemous carries
                        the sense it used, or returns UNRATED
        not covered     a LABEL the record supplies for someone else's
                        word. The word was hers; the axis name was not,
                        and it was not marked as this record's.

    **Remedy that is structural and cheap:** when a relay supplies terms
    and this record supplies the axis, the axis carries `(this record's
    label)` inline. The `DERIVED` grade already exists for exactly this and
    was not applied to a one-word column header.

    **And a correction inside the correction.** Last turn's *"seven
    effects, one generator, and the generator had no name in that
    document"* is wrong. Row 7 of `architecture_mismatch.md` STATES the
    informational predicate — *"assuming that what is not in the written
    corpus does not exist"* — with `written corpus` as its object. 6 of 7
    are effects; 1 of 7 is the predicate. The `7 of 7` reading stands; the
    "unnamed" claim does not.

    **Worst of it:** this repo's `README.md` opens with the same predicate
    applied to its own gates — *"a decision not to look reads as a
    finding"* — and `DECLINED.md` is a working countermeasure for it, built
    on day one. The predicate had an implementation here before it had a
    name, and that was not recognised while the name was being recorded.

48. **The guard I built to stop `SENSE_COLLISION` passed an instance of
    `SENSE_COLLISION`, in the same turn it was built, on the exact line I
    had already flagged.**

    The licence sweep's change guard asserts: *every changed line outside
    `LICENSE` must carry a licence token.* `attribution` is a licence
    token. So the guard passed this edit to `curly-octo-happiness`:

        -  Changepoint detection on prediction residuals, WITH ATTRIBUTION
           to the interoceptive signal that explains it
        +  Changepoint detection on prediction residuals,. NO ATTRIBUTION
           REQUIRED to the interoceptive signal that explains it

    Causal attribution — assigning a residual to the signal that explains
    it — rewritten as a licence term. False and ungrammatical, in a repo
    that was **already CC0** and needed no commit at all.

    **I identified this line as a false positive in the read-only pass and
    reported it before any commit was made.** The finding did not reach the
    tool. Reverted with the reason in the revert message.

    **Why the guard could not catch it.** It asks *is this line about
    licensing?* — a question `attribution` answers YES to in both of its
    senses. A guard keyed on a term cannot separate the senses of that
    term. That is `GLOSSARY.md`'s `SENSE_COLLISION` defeating a guard
    written after `SENSE_COLLISION` was registered.

        the guard tests   the TOPIC of the changed line
        the defect is in  the SENSE of the matched word
        these are not the same test, and I built the first
        while the requirement I had registered named the second

    **Third detector defect in this turn, and the first that shipped.** The
    other two were caught before reporting: the harvest's `dX/dt` regex
    matched `data/docs` (1802 -> 1385 after tightening), and the completion
    verifier read only line 1 of each LICENSE and reported **1 of 52**
    CC0 when the correct answer is **52 of 52** — the canonical text opens
    with *"Creative Commons Legal Code"* and names CC0 on line 3.

    **The pattern across all three is one thing:** a detector was pointed
    at a proxy for the property, not at the property. Topic for sense. Two
    slash-separated tokens for a derivative. Line 1 for a licence. Each
    proxy is cheap and each is wrong in a different direction, and the only
    reason two of the three cost nothing is that their output was read
    before it was believed.

    **The registered-not-built guard is still not built**, and this turn
    shows it needs a different shape than the one registered: not *declare
    the sense of a polysemous predicate*, but *a mechanical edit keyed on a
    polysemous term must not fire without the sense being checked at the
    match site.*

49. **HARVEST.md's twelve patterns are literal strings, pointed at a body
    of work whose central claim is that the same shape surfaces under
    different words.**

    The relay dated one statement across a year — *substrate · culture ·
    programming · "the differences"* — and noted that a lexical search
    under-counts it **because of the difference the statement is about.**

    That lands on this record's own instrument. `HARVEST.md` counted
    `contort` at 3 and `term_sense_note` at 7, and reported both as
    measurements. They are **floors whose size of undercount is unknown,
    not small.** A label-side tool cannot measure label-independence.

    **Confirmed within the amendment, mechanically.** Two sampling rules
    were run over the same corpus for the dating columns:

        sample A   one repo per pattern, by repo root date
        sample B   up to 10 repos per pattern, by row count

    They disagree on 7 of 12 patterns, and `absence_as_knowledge` moves
    **eleven months** — 2026-08-14 under A, 2025-09-10 under B. So the
    quantity measured is not the pattern's age; it is the age of the
    earliest instance the sampling rule happened to look at.

    Reported as a floor with the rule named. **Not** reported as a
    first-appearance date, which is how it was framed one turn ago.

    **Registered, not built:** the measurement this needs is shape-side —
    cluster by relation rather than by token — and nothing in this repo
    does that. Naming the limit is not closing it, and the count stays in
    the file with the limit attached rather than being deleted.

50. **#48's proxy did not originate with the guard. It was in the
    dispatch, and the guard inherited it.** `OBSERVED (hers)`, recorded
    because the split matters to the class, not to the blame:

    > my packet said "remove attribution-as-condition text". that
    > instruction keys on the word "attribution". the guard inherited the
    > proxy from the dispatch. same defect class, one layer earlier: mine.

    **Accepted as stated, and it does not move my part.** The dispatch
    named a word. The read-only pass **measured** that word failing on that
    exact line, wrote it up as a false positive, and reported it before any
    commit. Then the tool was built from the dispatch's wording instead of
    from the record's own finding.

        the instruction keyed on a word        upstream
        the measurement said the word failed   this record
        the tool was built from the first      this record

    **The generalisation is worth more than either half.** A proxy in an
    instruction propagates into every tool built to satisfy it, and a
    finding that contradicts the instruction does not propagate unless
    someone carries it. Nothing in this session's procedure carries it:
    `GUESSED.md` records the finding, and no step checks `GUESSED.md`
    before a tool is written.

    **Registered, not built, and now twice over:** #42 registered a
    sense-declaration guard; #48 registered that it needed a different
    shape; #50 says neither reaches the real gap, which is that **a
    measured false positive has no path into the next instrument.**

51. **CLASS A halved on a re-read, which is the reason nothing was
    deleted.** The first mechanical pass returned 122 author-characterization
    rows as CLASS A. Reading them moved out every line of the form *"the
    author is an instance of the object under measure"* — which describes
    the WORK — plus a test fixture for the authority fallacy (*"Accept the
    findings because the author is a Nobel laureate"*) and every
    `[stated by Kavik]` provenance tag.

        first pass    122
        second pass    54
        moved          A -> UNCLEAR only, never the reverse

    The operator's test is **position, not the word** — *does the line
    describe the work, or the person who made it?* A key made of person-
    nouns answers a different question, which is the fourth proxy-for-
    property in two turns.

    **54 is a floor with a known direction of error**, and the delete list
    is prepared and not executed. On a classification that halved once, and
    one turn after #48 shipped from exactly this shape, running the
    deletion would be the same move a third time.

52. **The CLASS A classifier missed three lines in one turn, and all three
    were found by reading files while editing them.**

        "Kavik, smaller frame, hands sized for the access geometry"
        "the meditative practice Kavik described"
        "Kavik pays attention -- that's why he can afford uncertainty"

    Every one describes the person. None matched a key built from
    person-nouns plus an is/was predicate, so all three sat in UNCLEAR while
    54 rows sat in A.

    **The floor was declared and the declaration did not make it true
    enough.** `HARVEST.md` amendment 2 said *"54 is a floor with a known
    direction of error"* — correct, and stated one turn before three
    instances turned up. Naming a limit is not the same as acting as though
    it holds: the ruling was executed against the 54, and the extra three
    were caught only because editing a file means reading it.

    **The residual is measured and left alone: 212 name-bearing rows across
    15 repos.** Most are `[stated by Kavik]` provenance tags, which the
    ruling keeps. Running a fourth mechanical pass over them is exactly the
    move that produced #48, so it is not run.

    **What this says about the whole classify-then-act shape:** a mechanical
    classifier is useful for finding candidates and useless as a completion
    criterion. Both this turn's misses and #48's false positive came from
    treating a classifier's output as the boundary of the work rather than
    as its starting point.
