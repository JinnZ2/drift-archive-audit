# VERIFY-FORM-CONTENTS — the relayed derivation, corrected against the file

    RELAY       "WHAT THE FORM MOST LIKELY ASKS — DERIVED from the pipeline
                 order, not from the form"
    STATUS      derivation superseded by reading. DERIVED -> OBSERVED.
    METHOD      cat verify/*.txt          (one command, artifact on disk)
    DATE        2026-09-23

The relay derived the forms' content from the A1–A5 order because it was
reasoning about a file it did not have open. This session has the file. It
was opened. What follows is what is in it.

## 1. THE DERIVATION WAS RIGHT ON THE AXES AND SILENT ON THE REST

Relayed prediction, verbatim:

    likely questions per repo:
      - is the reconstructed target what you were aiming at?
      - at each divergence: did the aim move, or did the build drift away
        from an aim that stayed put?

Both are in the forms. They are the TARGET section and the
DIVERGENCE/UNRESOLVED section. Neither is a whole form.

    form                          items   TARGET  RELATIONS  ENCODING  DIV/UNRES  OPEN
    bio-grid-american-manuf.        20      4        5          5         3        3
    emotions-as-sensors             21      4        6          3         4        4
    keystone-codex                  17      3        5          3         3        3
    ------------------------------------------------------------------------------
    TOTAL                           58     11       16         11         7+3      10

    PREDICTED BY THE PIPELINE ORDER   21 of 58   (TARGET + DIV/UNRES)
    NOT PREDICTED                     37 of 58   (RELATIONS + ENCODING + OPEN)

**The order carries the sections it produced and nothing else.** A1–A5
generate a target and a divergence list, so a derivation from the order
recovers exactly those two. RELATIONS and ENCODING are A3/A5 residue —
findings, not stages. OPEN is not derivable from any order: it is the
measurements that came out UNCLEAR and stayed that way.

## 2. WHAT IS ACTUALLY ON EACH LINE

Every line is `<statement> | operator:` — a blank to be marked YES / PARTLY
/ NO. The header states the rule the whole audit hangs on:

    # Under CORRECTION-001 every item below is a FIRST-MODEL RENDERING.
    # You are marking whether it matches your aim, not whether you wrote it.
    # Nothing in this audit is scored against an unmarked line.

So the scoring gate is **58 blanks**, not 6 questions, and not 3 forms.

## 3. THE TEN OPEN ITEMS ARE A DIFFERENT KIND OF QUESTION

The other 48 lines ask the operator to **mark a rendering**. These 10 ask a
**question of fact** that the archive cannot answer:

    bio-grid   self-healing interval: base64 says 2 min, both hex blobs say
               20 min — which is the target?
    bio-grid   data/biogrid_specs.json and data/compressed_hex_codes.txt are
               named in the root README and are not in the root tree — did
               they exist?
    bio-grid   the work predates the first commit (2025-07-10) by how long?

    emotions   two decay vocabularies at HEAD (4-value elder-sensor enum vs
               5-value CLAUDE.md/atlas enum), neither validating the 29
               free-text values — which is the target?
    emotions   three licences in the root tree (MIT-with-attribution /
               attribution-required / CC0-without-attribution) — which is real?
    emotions   CONVERGENT_WISDOM.md is referenced and does not exist;
               Convergent-Wisdom.md does — rename or dangling?
    emotions   a log file in the root tree is dated 95 days BEFORE the root
               commit — how far back does the work go?

    keystone   ethical_alignment populated and unscored for 13 months —
               intended, or dropped?
    keystone   haudenosaunee_council.json carrying id great_law_of_peace —
               deliberate (institution vs instrument), or a half-landed rename?
    keystone   44% closure: is closing the remaining 50 dangling edges the
               goal, or are some meant to stay open?

**These are the fiat points.** Each has at least two readings the archive
supports equally. Filling one is settling a question by fiat, which the
work order forbids outright.

One DIVERGENCE line in `keystone-codex` is already written as a question
with an explicit third value, and it is the form's own precedent for the
rule:

    did the operator request uncertainty in these values?  YES / NO / DON'T KNOW

`DON'T KNOW` is a result there, exactly as `UNSET`/`UNCLEAR`/`UNATTRIBUTABLE`
are results elsewhere.

## 4. THE RELAY'S CLOSING POINT — CONFIRMED, NOT DERIVED

    "the repo text is model-built from what you translated in.
     the AIM exists only on your side — the archive holds renderings.
     anyone else filling it = settling by fiat"

Confirmed against the file. The forms encode precisely that: the header
states the items are first-model renderings, the marking asks whether the
rendering matches an aim held elsewhere, and the scoring refuses to run on
an unmarked line. The archive is not withholding the answers. It does not
have them.

## 5. WHOSE MISS

    the derivation                the relaying session could not open the file
    the path                      named 6 times in this repo (README, PHASE_D,
                                  DECLINED, ENUM-SWEEP, SHADOW-HUNTING)
    the contents                  never rendered outside verify/*.txt — not once
    whether the relay had read    UNSET. Not determinable from here, and not
      access to this repo         filled by inference.

So the failure that is certainly this record's: **the forms were cited by
path six times and quoted zero times.** A party reasoning about what the
form asks had the name of the file and none of its content, from this side.

That is `FINDABILITY.md`'s shape, not `GUESSED.md` #32/#37's. #32 and #37
were *function inferred from a name with the artifact one command away on
my own disk*. Here the artifact was one command away on **this** side and
the derivation happened on the **other** side. Same distance, opposite end
of the channel — and it is the end that could not close it.

**The structural remedy, not the naming one:** this file renders the
contents. The citation is no longer a path.
