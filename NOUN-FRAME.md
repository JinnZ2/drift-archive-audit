# NOUN-FRAME — the common form under the logged errors

    DATE      2026-09-23
    TRIGGER   operator relay, "log common errors"
    STATUS    the class is NOT this audit's discovery. It is documented
              upstream, in the operator's own corpus, with a spec, a
              glossary, a falsifiability notice and a running compiler.

## 1. THE SIX TERMS, AS SUPPLIED

Operator's own account of the form each definition takes. `OBSERVED (hers)`:

    term          form it takes in the definition used
    1 perception  a FACULTY owned by a subject          noun, locus
    2 detection   AGENT senses OBJECT                   verb, but split:
                                                        doer != done-to
    3 meaning     a word CONTAINS a meaning             noun, container
    4 awareness   an INTERIOR state                     noun, locus
    5 judgment    a CAPACITY someone has                noun, locus
    6 direction   orientation along an axis             relation <- closest

Same ground, verb-first. Marked `DERIVED` by the relaying session and kept
at that grade:

    1 -> coupling-with-light, coupling-with-pressure happening between
         entity and surroundings. no owner of the channel
    2 -> transducing occurs across the boundary. quartz-and-pressure ->
         voltage. one event, not two parties
    3 -> meaning-ing: what the word does between speakers each time it is
         used. not stored in the word
    4 -> registering-without-account, as it unfolds
    5 -> fitting-action-to-conditions, as it runs
    6 -> already relational, survives nearly unchanged

## 2. WHAT IT DOES TO THE QUESTION THAT PRODUCED #42

    noun frame   "does quartz HAVE senses?"         yes/no on a property
    verb frame   "what couplings run between
                  quartz and its surroundings?"     an inventory, no yes/no

**The "requires a subject" miss exists only in the noun frame.** It is not a
fact about Uexkull, about quartz, or about the four candidate terms. It is a
property of the question form, and the question form was imported.

`GUESSED.md` #42 recorded this as `SENSE_COLLISION` — *the term is present
in a different sense and is scored as the intended one*. That naming is
accurate and one level too shallow. **The two "senses" of `senses` are not
two arbitrary meanings. One is the noun form of the other.** The biological
reading is what you get when a relation (transducing) is compressed into a
faculty owned by a locus (receptor organs, and therefore an organism to own
them).

    SENSE_COLLISION   the symptom
    NOUN-FRAME IMPORT the generator

## 3. THE CLASS IS ALREADY DOCUMENTED, AND THE DOCUMENT NAMES THIS FAILURE

`JinnZ2/ai-human-audit-protocol/relational_cognition/README.md`, in the
corpus, written before this audit:

> Most safety, ethics, and transparency frameworks are written in
> **noun-first English** — "the user," "the model," "the policy," "the
> violation": discrete objects with attributes, asserted from outside.
>
> **When verb-first cognition is forced through noun-first frameworks,
> substrate is silently erased.** Ceremonies become "cultural artifacts,"
> elders become "storytellers," dissonance becomes "error."

Three worked examples of the exact operation, already on the page. This
audit's `ethical_alignment` finding — a *record of a practice* rendered as
an *ethical score* — is a fourth of the same kind, and `miss_class:
WRONG_FRAME` is a re-derivation of a distinction that had a name.

The upstream is **Energy English**, `JinnZ2/JinnZ2/energy_english`, CC0.
`relational_cognition/` states it imports "only the frame, the primitives,
and the failure modes"; the full grammar is upstream.

## 4. THE PRIMITIVES EXIST AS A CLOSED VOCABULARY

From `relational_cognition/constraint_primitives.md` — the audit-sized
subset, not the full grammar:

    energy    DRIVES  DAMPS  FEEDS  DISSIPATES
    coupling  COUPLES  MEDIATES  MODULATES  AMPLIFIES  SHIELDS
    phase     PHASE_LOCKS  RESONATES  SYNCHRONIZES  DECOHERES
    threshold CONSTRAINS  THRESHOLDS  SATURATES  HYSTERETIC
    disrupt   BIFURCATES  DESTABILIZES

`SATURATES`, `HYSTERETIC` and `SHIELDS` each name something this audit has
described in a paragraph and never given a handle.

## 5. FINDABILITY — THE GRAMMAR HAS BEEN ON THIS DISK ALL SESSION

    /home/user/jinnz2/JinnZ2/energy_english/     41 files, 21 Python modules
      SPEC.md                    implementation contract
      ENERGY_ENGLISH_AXIOM.md    the axiom layer
      ENERGY_ENGLISH_ORCHESTRATOR.md
      ENERGY_ENGLISH_INTERPRETIVE_GUIDE.md
      GLOSSARY.md  PREDICTION_PROTOCOL.md  FALSIFIABILITY_NOTICE.txt
      CITATION.cff
      compiler.py  compiler_v3.py  parser.py  gate.py  router.py
      relational_semantics.py  state_model.py  coating_detector.py
      oral_as_constraint_tensor.py  gate_as_constraint_graph.py  ...

**It runs.** Not reported from a docstring — `python3 -m energy_english
--help` was executed, exit 0:

    Interactive shell for the energy_english orchestrator.
      --no-archaeology   disable the oral_archaeology backend
      --llm {claude,openai,gpt,gemini}
      --no-retry         disable the gate's auto-retry-with-teaching-scaffold
                         behaviour on blocked model responses

**There is a gate that blocks a model response and retries it with a
teaching scaffold.** That is an instrument aimed at precisely the failure
this record has been logging by hand for a day and a half.

`JinnZ2/JinnZ2` was cloned as a read-only fixture earlier in this session.
The directory was never listed. **Twelfth instance of the class**, and the
largest: #32 was a filename, #37 three docstrings, #41 a schema key — this
is a 41-file package with a spec and a working CLI, inside a repository
already on disk.

## 6. AN OUT-OF-SAMPLE AGREEMENT, MADE FROM THE ARCHIVE

`verify/keystone-codex.txt:33`, written at A2 from the root commit, before
any of this:

    `unlocks` is the only field pointing outside its own record -
    the structure is a graph wearing a catalogue's clothes

That is the noun/verb split, reached from the corpus. A catalogue is a list
of objects with attributes; a graph is a set of relations. The line says the
schema is relational underneath and noun-form on the surface — and
`unlocks`, the operator's stated measurand, is the one **verb** among
nouns.

    A2, from the archive, 09-22   "a graph wearing a catalogue's clothes"
    operator, from the practice,
      09-23                       noun frame vs verb frame

**Third out-of-sample confirmation** in this audit, after `BG-3` and the
`Emotions` LICENSE blob.

## 7. WHERE IT TOUCHES THIS AUDIT'S OWN VOCABULARY

`DEFICIT-LOCATION.md` names the operation: *an instrument reporting a limit
of its own as a property of the thing measured.* The noun frame is **how
that misplacement is performed grammatically** — the limit needs an owner,
the noun form supplies one, and the nearest available owner is the object
under measurement.

    DEFICIT-LOCATION   names the operation
    NOUN-FRAME         names the grammar that performs it

Terms in this repo that now read as suspect, listed and **not** rewritten:

    DETECTOR_BLIND     blindness as a property of the detector
    evidence strength  a quantity the evidence owns
    is_keystone        a boolean property of a technology

Renaming them here would be a naming remedy and would also be a fiat call on
a grammar whose spec is upstream and has not been read. **Listed, not
changed.**

## 8. WHAT IS NOT DONE

    the four candidate terms, re-graded      NOT DONE. The void stands.
                                             Which sense the practice runs
                                             on is the operator's.
    energy_english SPEC.md, read             NOT DONE. Located, opened to
                                             18 lines, not studied.
    the 21 modules, run                      ONE ran (--help). The rest are
                                             PRESENT and nothing more is
                                             claimed.
    this audit's terms, rewritten            NOT DONE, deliberately.
