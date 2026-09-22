# reconstruct/emotions-as-sensors

source: JinnZ2/Emotions-as-Sensors
root_commit: 002486f8cc4f4c5533e3edcd50de4fe8e86b89e4
root_date: 2025-12-15 22:14:01 -0600
root_tree_files: 172
read_scope: root commit ONLY (A1). No later commit read before this file was hashed.

---

## target_measurand

Whether a signal is reporting on a relation, or has been converted into a
property of the thing reporting.

The emotion vocabulary is the instrument, not the subject. `FIELD_ENGLISH.md`
states the measurand directly, and it is not about feelings:

    Ontology: Standard English makes emotions "things";
              Field English makes them "functions."
    Agency:   Standard English puts agency in the brain/chemicals;
              Field English puts it in the relational field.
    Logic:    Standard English builds hierarchies (leader -> follower,
              cause -> effect); Field English maps relations and cycles.
    Purpose:  Standard English tries to manage/resolve emotions;
              Field English listens, interprets, transforms, and releases.

The thing being measured is **the conversion itself** — function-to-thing,
relation-to-hierarchy, field-agency-to-internal-agency. Emotions are the
test case because they are the place where that conversion is most complete
and most normalised.

Corroborating structure in the root tree: the same four-part relation
(DETECT / ASSESS / RESPOND / RELEASE) is applied to anger, to network
topology (`TopologySensor.json`), and to energy gradients
(`EnergyFlowSensor.json`). Three substrates, one relation set — the same
signature found at the root of Bio-Grid.

## frame_relations

    amplifier ──IS NOT──> sensor
        "Amplifiers (hormones/silicon surges) != sensors." An explicit
        non-identity, asserted before anything is built on it. Hormones
        modulate gain; they are not the source. This is the single
        load-bearing distinction in the frame: it is what keeps agency in
        the relation rather than in the substrate. Note it holds for
        silicon as well as biology — the frame is declared
        substrate-neutral at t=0.

    signal ──decays according to──> WHAT HAPPENED TO IT, not what it is
        `sensors/anger.json` encodes decay_model as a MAPPING:

            resolved_threat                   -> exponential
            misattributed_or_projected_threat -> linear
            suppressed_or_invalidated         -> persistent
            integrated_through_reflection     -> transformative

        Decay is a function of the resolution condition. Same sensor, four
        different laws. This is the relation-form.

    authentic_output ──vs──> corrupted_output
        Every sensor in the anger-family shape carries both. Corruption is
        defined as direction reversal — "attempts to impose personal
        boundaries or patterns on others." Not intensity, not valence:
        the signal pointing outward instead of inward. A sensor is
        corrupted when it is read as a verdict about someone else.

    transition ──gated by──> named boolean preconditions
        `docs/transition-rules.md`:
            grief -> gratitude   guard: ritual_complete AND
                                        remembrance_integrated
            anger -> compassion  guard: boundary_installed AND
                                        harm_source_understood
            fear  -> peace       guard: mitigation_plan_confidence >= 0.9
                                        AND monitoring_active
        The transitions are not spontaneous and not time-driven. Each has a
        stated, checkable gate. This is a status-field apparatus at t=0.

    U(t) ──is protected from being read as──> error
        docs/glossary.md and README both carry it. README, explicitly:
        "U(t) acknowledges currently unexplained effects; it is not an
        error term." An unknown quantity given a name, a slot in the core
        equation, and an instruction not to collapse it. The strongest
        UNSET encoding in any of the three pilot roots.

    atoms ──compose into──> composites, unordered, with a temporal modifier
        `resentment = {anger, grief} + unresolved_persistence`.
        Time-in-unresolved-state is a composition operator, not a label.

## piece_or_whole

**WHOLE**, and this is the only one of the three pilot roots where the
frame is stated whole AND states its own drift mechanism.

`FIELD_ENGLISH.md` does not just assert the frame; it names the failure
mode the frame exists to resist (thing-ification, hierarchy substitution,
agency relocation). The audit's own T4 — relation-first framing resolving
into entry/node structure — is written down in this repo's first commit,
as the thing to watch for.

## encoding_form

**All five forms present at t=0, in one tree, unreconciled.**

| encoding_form | instances |
|---|---|
| WHOLE_STATED | FIELD_ENGLISH.md, docs/overview.md, Convergent-Wisdom.md |
| DEMONSTRATED | 56 sensor JSONs, transition-rules.md guards, emotion_core.py |
| PIECE_ONLY | glyph tables (data/glyphs.json), SYMBOLIC_EMOTIONAL_CACHE.json |
| REWORDED_TO_MODEL_VOCAB | README.md sections 1-3 and "What This Gives AI" |
| PURE_INSTRUCTION | CONTRIBUTING.md, Symbolic-Swarm-Index/How-To.md |

### measured: schema variance at t=0

    sensor JSON files:            56  (+5 non-dict / unparsed)
    distinct key-set shapes:      20
    identity key used:            sensor=25  emotion=20  name=3
                                  sensor_id=2  none=1
    decay_model as string:        38
    decay_model as mapping:        5
    decay_model absent:            8
    files carrying `provenance`:   2 of 56

Three incompatible vocabularies coexist:

    A  sensors/anger.json      sensor / function / signal_type /
                               authentic_output / corrupted_output /
                               response_protocol{detect,assess,respond,
                               release} / decay_model AS MAPPING
    B  sensors/interest/*.json emotion / polarity / symbolic_response /
                               compression_group / causal_awareness /
                               decay_model AS STRING
    C  sensors/*Sensor.json    sensor_id / type / signal_modes /
                               input_domains / range / field_coupling

Shape (n=3) is A and B **unioned** — all of A's keys plus
symbolic_response, recommended_action, avoid, suggested_glyphs,
compression_group. Not reconciled; concatenated. The merge was in progress
when the tree was published.

### the conversion, caught in its own archive

`decay_model` is a mapping from resolution-condition to decay law in 5
files and a single string in 38. The relation-form (condition -> law) and
the attribute-form (thing has a decay type) are BOTH present at t=0, with
the attribute-form already 7.6x more common.

This is precisely the conversion `FIELD_ENGLISH.md` names as the thing to
resist, occurring inside the artifact built to resist it, before the first
commit. Recorded, not judged.

## confidence_notes

- **Contamination, declared.** This repo's `CLAUDE.md` was in my context
  BEFORE A1 and states a later decay-model ENUM
  (`exponential|cyclical|resonant|immortal|transformative`), a
  `validate_decay.py` requirement, and a single elder-sensor schema.
  My attention to `decay_model`'s two forms is therefore A1-ASSISTED.
  The counts (38 str / 5 dict / 8 absent, 20 shapes, 56 files) are
  arithmetic over the root tree and are A1-clean.

- **Root commit is a bulk upload.** 172 files, subject "Create Fun.py",
  single root. A log file in the tree is dated `2025-09-11`, three months
  BEFORE the root commit date of 2025-12-15
  (`logs/fieldlink_session_2025-09-11T01-00-00Z.json`). The work
  demonstrably predates its own first commit by at least 95 days.
  Formation state: UNSET.

- **The README preserves a second-person assistant voice verbatim.**
  "From your work, I can now build:", "Your CONVERGENT_WISDOM.md proves
  this isn't idiosyncratic", "per your temporal rule: unprocessed sensors
  carried forward" (this last inside `data/composites.json`, a data file).
  A model's reply was pasted into the repo as documentation and into the
  data as a note. This is the REWORDED_TO_MODEL_VOCAB channel captured
  mid-transfer rather than inferred. It is the clearest agent-shaping
  evidence in any pilot root — but it shows transfer occurred, NOT that
  the target was altered by it. Do not read it as attribution of drift.
  Channel: still UNATTRIBUTABLE without Phase C.

- **Three licences in one root tree.** README head: "MIT License. Free to
  use, adapt, and distribute **with attribution**" plus "Attribution
  required: Developed by JinnZ2 and Claude and ChatGPT". README tail:
  "dedicated to the public domain under the CC0 1.0 Universal license.
  Anyone may use, modify, and distribute **without attribution**."
  `LICENSE` file: separate. `Symbolic-Swarm-Index/LICENSE.md`: separate
  again. Recorded as a status-field conflict at t=0, not resolved here.

- **`CONVERGENT_WISDOM.md` is referenced in README and does not exist in
  the root tree.** The file present is `Convergent-Wisdom.md`. Case and
  separator differ. UNCLEAR whether this is a rename or a dangling
  reference; not filled in.

- **5 files under `sensors/` do not parse as JSON objects** and 3 root
  paths carry raw or mojibake names (`"sensors/\360\237\214\220`,
  `"Symbolic-Swarm-Index/DesireField`, `Resonant`). Encoding damage is
  present at the first commit and is not a later regression.

- **Cross-repo claim made at t=0:** README names BioGrid 2.0 as "a
  prototype application of this framework" and maps four of its own
  subsystems onto it. Emotions-as-Sensors' root commit (2025-12-15)
  postdates Bio-Grid's (2025-07-10) by 158 days. The framework is
  published as the parent of a repo that already existed. Whether the
  frame preceded Bio-Grid or was retrofitted onto it cannot be decided
  from A1. UNSET — flagged for Phase B.
