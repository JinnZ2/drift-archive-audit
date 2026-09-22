# Where the discipline came from — the 4-way question, measured

## The question, as posed

`CROSSCHECK-ai-human-audit-protocol.md` recorded that repo's use of
sha256-identified supersession, `"original": "retained, unmodified"`, and
three-valued honesty fields as **independent arrival** of this audit's own
rules — "two separate efforts, no shared code, same rules" — and offered a
2-way choice: forced by the problem, or common upstream source.

**Two candidates were missing, and one of them is decisive:**

    1  forced by the problem
    2  common upstream source
    3  SAME CHANNEL AUTHORSHIP  <- not in my list
       Per CORRECTION-001/002 repo content and concept vocabulary are
       model-given. So "no shared code" does NOT establish "no shared
       source." Two model sessions, one operator translating, overlapping
       training corpora. "Independently arrived at" collapses to
       "arrived at twice through the same pipe."
    4  operator practice as the source — the discipline comes from her
       described doing, not from either model

**Candidate 4 is testable.** It predicts the discipline appears in the
fabrication / forest / CNC material, where no audit framing was in play.

## The test, run

Cloned `DIY-CNC`, `tool-off-metrology`, `Prosthetic-arm-CNC` read-only.

### First pass — and it was wrong

I grepped for the **implementation** markers (`sha256`, `retained
unmodified`, `append-only`) and got 0/3. I was about to record "the
discipline does not appear in fabrication material."

**It does. I was searching for its surface form.** The same failure mode as
the T-0 regex: operationalizing a concept by its tokens.

    DIY-CNC/legacy/README.md
      "Nothing in this folder is current. It's kept because the PROCESS of
       being wrong and correcting it is worth more to a future builder than
       the corrected answer alone."
      Claim -> Test -> Falsify -> Revise -> RECORD WHAT'S STILL UNKNOWN
       -> Rerun
      "The failure mode isn't being wrong. It's being wrong and never
       checking, or checking and QUIETLY EDITING SO NOBODY CAN SEE THE
       CORRECTION HAPPENED."

    tool-off-metrology/README.md — a lineage tag system
      [obs]  direct field / operator observation
      [inf]  inference, untested
      [lit]  literature, with confidence
      [open] unresolved
      [gap]  no instrument exists
      "Every asserted edge carries one. UNTAGGED CLAIMS ARE THE DEFECT."
      "Tags do not get promoted. [inf] becomes [lit] when there is a
       citation, and not before."
      CLAUDE.md: "Do not launder uncertainty in prose."

That is this programme's discipline, stated in fabrication repos, with
`[gap] no instrument exists` sitting there as vocabulary this audit reached
for independently.

### Second pass — the dates settle it

    DIY-CNC/README.md          added 2025-07-10  JinnZ2   (operator era)
    DIY-CNC/SCOPE.md           added 2025-09-02  Jinn2Z   (operator era)
    DIY-CNC/CLAUDE.md          added 2026-03-22  Claude
    DIY-CNC/legacy/README.md   added 2026-08-14  Claude   <-- the discipline

**The discipline in the fabrication repo is agent-era and model-authored.**
It is not in the operator-era commits. `tool-off-metrology`'s first commit
is 2026-08-14 — the repo's entire existence is that window.

### And it is one cross-repo pass, visible in the archive

commits in 2026-08-13..17:

    Emotions-as-Sensors          11
    tool-off-metrology           17
    DIY-CNC                      10
    Bio-Grid-American-Manufacturing-   8
    Keystone-Codex                3
    ai-human-audit-protocol       0

**49 commits across five repos in five days**, all Claude-authored, and it
is where `legacy/` and the retire-don't-delete rule were installed
account-wide. Bio-Grid `680c51d`, Keystone `b05bc21` and DIY-CNC `17d3658`
are the same act in three places on the same day.

`ai-human-audit-protocol` is **not** in that window. Its sha256-correction
discipline entered **2026-09-09**, author string `claude` (lowercase), four
weeks later, in a separate pass.

## Answer

    candidate 4  operator practice        NOT SUPPORTED. The fabrication
                                          discipline is agent-era; the
                                          operator-era commits in the same
                                          repo do not carry it.
    candidate 3  same channel authorship  SUPPORTED, and it is the
                                          parsimonious reading. Both
                                          disciplines are model-authored.
    candidate 1  forced by the problem    not excluded, no longer needed
    candidate 2  common upstream source   not excluded; 3 is a specific
                                          form of it

**Two passes, not two efforts.** 2026-08-14 (five repos, `legacy/`) and
2026-09-09 (audit-protocol, sha256 corrections). Four weeks apart, same
channel.

## RETRACTION 9 — mine

I recorded the audit-protocol repo's discipline as **independent arrival**
and framed it as a join: *"two separate efforts, no shared code, same
rules."*

**"No shared code" never established "no shared source."** CORRECTION-001
and -002 were already on the record and said exactly that, and I applied
them to the operator's vocabulary while exempting the discipline I had
adopted myself.

The corrected statement: this audit's discipline and the audit-protocol
repo's discipline are **two agent-era passes through one channel**, not two
efforts converging. Whether the rules are *also* forced by the problem is
untested and no longer carries the weight I gave it.

**This bears directly on whether this audit's discipline is a finding or a
house style — and the answer moved toward house style.**

## What would still distinguish 3 from 1

Candidate 4's other prediction remains open: the discipline appearing in
material with **no model involvement at all**. Every repo reachable from
this session has a `CLAUDE.md`. Whether any operator-era artifact anywhere
carries it is `UNSET` — and per CORRECTION-001, even operator-era repo
content is model-generated, so the archive may contain no such artifact by
construction.

That check has to go outside the repositories entirely: notes, shop
records, anything transported by a channel that was never a chat.

Distinguishing 3 from 1 needs source model per pre-agent commit. **UNSET,
unrecoverable from git — blocked by the same gap as avenue D.**
