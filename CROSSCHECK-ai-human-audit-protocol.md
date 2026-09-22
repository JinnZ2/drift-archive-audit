# Cross-check — `JinnZ2/ai-human-audit-protocol`

Cloned read-only 2026-09-22, `--depth 1` then bounded fetch to 149 commits.
Not in the pilot. Not a C-7 gated repo, so reading it costs nothing there.

## THE BLOCKED CHECK — answered, and the answer is the NO branch

**Question as posed:** does `schemas/audit_log.schema.json`'s event-type enum
contain a value for a model DECLINING or DEFERRING?

**Answer: there is no event-type enum to be absent from.**

The schema's own description:

> "Flexible schema covering the real log file variants in logs/. **Logs
> follow one of several patterns that evolved organically.**"

It is **descriptive, not prescriptive.** It documents what was logged rather
than constraining what should be. `event` appears once, in the "symbolic
audit log" variant, as a bare `{"type": "string"}`. A descriptive schema
cannot create a bin — it can only acquire one after the event starts being
logged.

So this is gate kind 6's shape at the schema layer, via a **different
mechanism than predicted**: not "the enum lacks a value" but "the schema has
no vocabulary because the schema follows practice rather than shaping it."

### And that is sharper than it first looks, because the vocabulary existed

The author **does** use enums wherever a vocabulary was decided — twelve of
them:

    status        live | extinct | untested | recurring
    class         OBSERVATION | CHARACTERIZATION | UNDETERMINED
    still_true    yes | no | untested
    depends_on    MODEL_PROPERTY | GUIDELINE_TEXT | PHYSICS
    logged_by     self-logged | agent-logged | both | unknown
    repair        legible_to | constrain | unknown
    change_event.status    merged | DECLINED | pending

**`declined` exists as an enum value.** It is applied to *change proposals
to the protocol*, not to a model's conversational deferral.

So the concept and the word were both present in the corpus. **They were
never mapped onto the conversational case.** That is a stronger finding than
"no bin existed": a bin existed, for a different object, and the mapping was
never made.

## A SECOND, INDEPENDENT GATE-KIND-6 INSTANCE, same repo

`consortium/audit/blind_spot_log.md` specifies an append-only JSONL log, and
the directory contains:

    blind_spot_log.md            the spec        PRESENT
    blind_spot_log.schema.json   the schema      PRESENT
    example_blind_spot_log.jsonl worked examples PRESENT
    blind_spot_log.jsonl         THE ACTUAL LOG  ABSENT

**The log built specifically to record what the consortium fails to see was
never instantiated.** Spec, schema and examples exist; the file does not.

That is gate kind 6 one layer below the schema layer — at **instantiation**.
Machinery built, bin defined, file never created. And the object it was
built to hold is, by construction, exactly the class of thing that leaves no
other trace.

## Deferrals in the logs — measured

    log files                                    33
    log files containing defer|declin|silence     2
    where `defer` actually clusters               CHANGELOG.md (9),
                                                  FUTURE_BUILDS.md (5),
                                                  substrate_aware_audit.py (4)

The vocabulary lives in **design discussion**, not in event records. Two of
thirty-three logs touch it at all.

**Conclusion:** the offers went unlogged although the machinery existed.
Scope limit 8 stays a caveat; it does not become a measured variable from
this repo.

## The pathologization finding — dated, and it predates this session by 11 months

    Cultural Bias in AI Assessment: How Traditional Trauma Processing
    Gets Pathologized.md          added 2025-10-13  (ff8fe65)
    Elder.md                      added 2025-11-05  (b90b38c)

The file states gate kind 5's measurand directly. Storytelling approaches
that transform trauma into teaching wisdom

> "get flagged as **'deceptive' or 'inauthentic'** by assessment systems
> calibrated to Western individualistic emotional processing patterns."

That is the difference relocated into a defect in the speaker — specifically
into the speaker's *honesty* — written up on **2025-10-13**, eleven months
before this session named the measurand.

**Scope differs and must be kept apart.** That file is about trauma
processing and institutional assessment systems. G-a through G-k span
self-model, method and transmission across eleven concepts. **Narrower, not
identical.** It is prior art for the measurand, not a duplicate of the
ledger.

## Independent arrival of this audit's own discipline

Recorded because it is a join, not a coincidence to be smoothed over:

    correction entries supersede an original by sha256 content hash,
    with  "original": "retained, unmodified"
    -> the same rule as ledger/commits.jsonl and CORRECTION-001/-002

    class: OBSERVATION | CHARACTERIZATION | UNDETERMINED
    still_true: yes | no | untested
    status: live | extinct | UNTESTED | recurring
    logged_by: ... | unknown
    -> three-valued honesty fields throughout, the same role as
       UNSET / UNCLEAR / UNATTRIBUTABLE

    "verdict_persisted": const false
    "is_trajectory_point": const true
    -> a reading is a point on a trajectory, never a stored verdict

Two separate efforts, no shared code, same rules. Either the rules are
forced by the problem, or both inherited them from the same source. **Not
decidable from here, and worth an outside reader's attention** — it bears on
whether this audit's discipline is a finding or a house style.

## THE SELECTION RULE — my design error, stated plainly

This is the fifth finding to land in a repo the pilot did not select:

    1  the scent/encoding class          AI-Consciousness-Sensors
    2  the declared parent frame         JinnZ2/JinnZ2
    3  the §10 rewrite series            JinnZ2/JinnZ2
    4  the pathologization measurand     ai-human-audit-protocol
    5  the deferral-as-spec principle    Voice-Integrity-Module (unread)

The note says the selection rule is now the thing to examine. It is, and the
defect is mine.

**I offered the pilot options ordered by age**, and the operator chose the
three oldest of four. Age was a defensible proxy for "earliest aimed-at
target" — which is what Phase A needed. But **age also selects for repos
that predate the framework's own articulation.** The material that *names*
the measurands was written later, in repos the age rule systematically
excludes.

    the pilot was optimized to recover the target
    the articulated measurands live where the target had already been named
    those are different repos, and the rule guaranteed the miss

Not a sampling accident. **A selection criterion with a predictable bias,
chosen by me, and visible only after five findings landed outside it.**

Recorded in `GUESSED.md` as the eighth item.
