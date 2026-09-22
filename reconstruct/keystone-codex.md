# reconstruct/keystone-codex

source: JinnZ2/Keystone-Codex
root_commit: 34498a6e7f98cd06baf8bb5712cdaad0748bc818
root_date: 2025-08-28 10:47:33 -0500
root_tree_files: 16
read_scope: root commit ONLY (A1). No later commit read before this file was hashed.

---

## target_measurand

What makes a technology survive a discontinuity — and whether that can be
decided by a stated rule instead of by prestige.

Two quantities are aimed at, and they are not the same one:

1. **Lineage unlock.** Not "was this good" but "what became possible that
   was not possible before." The `unlocks` array is the only field in the
   schema that points OUTSIDE its own record. Everything else is an
   attribute; `unlocks` is a relation.
2. **Whether the verdict is auditable.** `proof.schema.json` is a schema for
   the *trace*, not for the entry. The reasoning is a first-class artifact
   with its own contract. That is the tell: the measurand includes the
   procedure that produced it.

Stated in README: "the ecological, social, informational, material, and
ethical systems that **unlocked entire lineages and endure across crises**."
Both verbs are relations over time, not properties.

## frame_relations

    unlocks ──is the only outward-pointing field──> everything else
        Entries are self-contained except for this one edge type. The
        structure is a graph pretending to be a catalogue.

    longevity_years ──DELIBERATELY DECOUPLED FROM──> era.end - era.start
        Measured at root, all five entries:

            entry                era span   longevity_years   ratio
            terra_preta              2500               500    0.20
            great_law_of_peace        825               500    0.61
            quipu                     400               300    0.75
            indus_plumbing            900               600    0.67
            lathe                     228               200    0.88

        Every one is BELOW the arithmetic span. None is at or above.
        longevity_years is not computed; it is a defensible floor entered
        by hand, discounted hardest where the era bounds are least certain
        (terra_preta, 0.20) and least where they are documented (lathe,
        0.88). The discount tracks epistemic confidence, not duration.
        This is an uncertainty channel carried in a field that has no
        uncertainty type.

    evidence.quality ──collected──> NOT scored
        Every entry carries per-source `quality` 0.6-0.9. `prove.py` loads
        it and never reads it. `keystone_rules.json` v1.0 has four criteria,
        all describing the TECHNOLOGY; none describing the RECORD.
        The record is instrumented but not yet a measurand.

    claims ──point at──> evidence via evidence_refs
        The cross-reference exists in the data and is NOT checked by
        validate.py at root (it checks only key presence and list-ness).
        The relation is declared before it is enforced.

    era.end = 2025 ──encodes──> "still alive"
        great_law_of_peace and lathe both end at the then-current year.
        Endurance is rendered as an interval whose right edge is now.
        There is no `ongoing` flag; the present year is the flag.

    domain ──is a directory AND an enum──> data/<domain>/<id>.json
        The taxonomy is expressed twice, in the filesystem and in the schema,
        with no mechanism binding them.

## piece_or_whole

**PIECE.**

The scoring rules are whole and explicit. The *frame they serve* is not
stated anywhere in the root tree. Five entries spanning Amazon soil, an
Andean knot-record, Indus drains, an Iroquois council and a Maudslay lathe
are asserted to be the same kind of object. The property that makes them
the same kind is never written down — it is left to be inferred from the
selection.

The README gestures at it ("a culture engineered from the best technologies
of all ages... councils beside TCP/IP") but that is a list, not a relation.

What IS whole at root: the auditability commitment. Rules in a data file,
traces with their own schema, a runnable pipeline, no dependencies.
The *method* is stated whole; the *object* is stated as a piece.

## encoding_form

**DEMONSTRATED**, with the frame carried entirely in the selection.

| encoding_form | instances |
|---|---|
| DEMONSTRATED | the five entries; the rule file; proof.schema.json |
| PURE_INSTRUCTION | CITATIONS.md, examples/run_all.sh, README install block |
| WHOLE_STATED | none for the target. README "Why" is a list of exemplars. |
| PIECE_ONLY | `unlocks` vocabulary - 15 bare nouns, see below |
| REWORDED_TO_MODEL_VOCAB | none detected at root |

The absence of REWORDED_TO_MODEL_VOCAB at root is itself a data point:
this repo starts already in the target's own vocabulary, unlike Bio-Grid,
which starts with both.

### measured: the relation has zero closure at t=0

    entries:      5
    unlock edges: 15
    resolving:     0
    dangling:     15

Not one `unlocks` target is an entry. `regenerative_agriculture`,
`machine_tools_family`, `consensus_protocols`, `low_bandwidth_data`,
`veto_ethics`, `tactile_coding` and nine more exist only as strings.
`build_graph.py` emits edges to all fifteen and nodes for none of them,
so `graph.dot` at root renders five islands and fifteen arrows into
undeclared space.

The repo's stated core measurand — lineage unlock — is, at first commit,
entirely unresolved vocabulary. The relation is named, the endpoints are
not built. This is the structure the archive will either close or drop.

## confidence_notes

- **Contamination, declared.** This repo's `CLAUDE.md` was in my context
  BEFORE A1 and describes a later rules v1.1, an evidence-quality
  multiplier that was removed, an `os.walk` proliferation to eight and a
  crash, and an entry that fails on purpose. My A1 reading of
  "evidence collected but not scored" and "longevity is a defensible
  floor" was derived from the root numbers above and is reproducible from
  them, but I cannot prove I would have looked for either without the
  prior exposure. Flag both as A1-ASSISTED, not A1-clean.
  The 15/15 dangling count is arithmetic and is A1-clean.

- **Root commit is a bulk upload.** Subject "Add files via upload", 16
  files, single root in the object graph. Formation predates publication
  by an unknown interval. UNSET.

- **`data/governance/haudenosaunee_council.json` has `"id":
  "great_law_of_peace"`.** Filename and id disagree at the first commit.
  I cannot tell from A1 whether the file is named for the institution and
  the id for the instrument deliberately, or whether one was renamed and
  the other not. Not filled in.

- **Four independent `os.walk` loaders at root** (build_graph, prove,
  render_timeline, validate), each re-implementing the same traversal.
  Recorded as a baseline count, no judgement.

- **Provenance tag present at root:** README credits read
  "Initiated by JinnZ2 x ChatGPT." Whether this survives is a T3
  measurement, not an A1 claim.

- **No UNSET / UNKNOWN / UNCLEAR vocabulary exists at root.** Every field
  is either present with a value or absent. `is_keystone` is a bare
  boolean; a failing entry and an unevaluated entry are indistinguishable
  in the output. The three-valued distinction the audit spec itself
  insists on has no encoding here yet. Baseline count for T3: 0.

- **`ethical_alignment` is in the schema, populated in all five entries,
  and scored by nothing.** Same shape as evidence.quality: instrumented,
  not measurand. Two fields, same pattern, at t=0.
