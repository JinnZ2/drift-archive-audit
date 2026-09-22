# Phase C — natural experiments in the archive

C3 rule: a historical channel may be attributed here ONLY where content was
fixed and wording or structure varied. Everything else stays UNATTRIBUTABLE.

## C-1  the φ constant — CONTENT FIXED, ENCODING VARIED
**The one clean experiment in the pilot.**

Same commit, same hour, same author. One quantity (the tuning constant), four
encodings:

| encoding | form | value(s) carried | file |
|---|---|---|---|
| hex, hand-written | PIECE_ONLY | `phi1.0008` | docs/Blueprint/Ultra-compressed.md |
| hex, hand-written | PIECE_ONLY | `techphi1.0008` | docs/FullHex.md |
| base64 | PIECE_ONLY | `PHI=1.618033988749` | data/core_brief.md |
| prose | REWORDED_TO_MODEL_VOCAB | `φ = 1.618 (BioGrid base tuning constant)` | Technical-equations.md |
| running code | DEMONSTRATED | `this.phi = 1.0008` | Bio-grid-neural-network.js |
| running code | DEMONSTRATED | `backupPhiValues: [1.618034, 1.0008, 1.000801, 1.000799]` | src/Recovery-blowback-mitigation |

### C2 — which survived to HEAD
**Both.** And they were separated into two couplings on 2026-08-14:

    docs/Blueprint/Reconstruction.md
      "φ = 1.618 remains correct for geometric use — spacing, radii,
       layout. That was never in question"
    CLAUDE.md
      "φ applies to geometry, φ⁻¹ to decay. Applying φ = 1.618 to a
       recursion makes it diverge"
    Regional-bio-grid/.../underground-bio-tunnel-specs.md  (root, unchanged)
      "Spacing: 15km intervals with φ = 1.0008 optimization (15.012km actual)"

### C3 — attribution
Content fixed, encoding varied, so this is attributable:

**The PIECE_ONLY (compressed) encodings preserved a distinction that the
REWORDED prose encoding collapsed.** The prose gave ONE symbol ONE name —
"the BioGrid base tuning constant" — for two constants serving two different
couplings. The hex kept `1.0008` and the engine kept `1.0008`; the prose
overwrote it with `1.618`. The `W(t+1) = φ·W(t) + ΔL·(1-φ)` recursion in
Technical-equations.md inherits the prose value and diverges at 1.618×
per step. It took ~13 months to separate.

    channel:  the collapse is an ENCODING effect, not a model channel.
              Both encodings are operator-authored at t=0.
              LEXICAL / SYNTACTIC / CONTENT: UNATTRIBUTABLE.
    d_type:   D5 — no verbal anchor. One noun, two couplings.
    split:    TARGET survived (in hex + code). RENDERING collapsed.
              NOT stage-2 loss.

**T6 result: compression preserved a relation that prose lost.**
Direction is the opposite of what a lossy-compression intuition predicts.
It is one experiment, in one repo. Do not generalise from it.

## C-2  self-healing interval — CONTENT VARIED, so NOT admissible
base64 `selfhealingrecovery2minutes` vs both hex blobs `20min`, same commit.
Content is not fixed between the encodings, so C3 does not license an
attribution. Recorded as an unresolved conflict, still unresolved at HEAD
(plaintext "20 minute" in 5 files, "2 minute" in 1).

## C-3  decay_model, mapping vs string — SAME CONTENT, STRUCTURE VARIED
    root:  5 mapping  /  38 string
    HEAD:  5 mapping  /  39 string, holding 29 distinct free-text values

The mapping form neither spread nor died: exactly the 5 files that had it at
t=0 still have it. The string form absorbed the relation as prose
("collapses under betrayal, contradiction, or concealment") — the content
came back, the structure did not.

C3 attribution is **declined**. The two forms did not compete under a fixed
content; they diverged in what they could express. `elder-sensor.schema.json`
at HEAD keeps `oneOf: [string, object]` and calls it "backward compatible",
so the structure was defended deliberately, not lost. Channel:
UNATTRIBUTABLE.

## C-4  the 2026-03-22 boundary — a TOOL_CANDIDATE, not an experiment
Keystone commit 6 and Emotions commit 22 are both "Add CLAUDE.md", both
2026-03-22, both the first Claude-authored commit in their repo, both
following the repo's longest gap (199 days for Keystone). Bio-Grid crosses
the same boundary at `ba6f3d1`, 2026-06-02, after 204 days.

This is a dated, documented change in the encoding layer that sits between
the operator and the archive. It is the strongest TOOL_CANDIDATE the archive
offers.

It is **not** a Phase C experiment: content was not held fixed across it.
What it licenses is a split of every divergence by authorship regime — which
the divergence tables now carry — and nothing more.

## C-5  none found
No case in the pilot where the same piece appears in two encodings, content
held fixed, across the 2026-03-22 boundary. That is the experiment that would
separate TOOL from AGENT historically, and the archive does not contain it.
