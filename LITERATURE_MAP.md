# Literature map

Relayed from operator/Claude notes, 2026-09-22. **Provenance discipline
applies to citations exactly as it applies to gate rows: a guessed row is
worse than an empty one.**

Every entry carries a status. Only three were checked in this session.
**Everything marked UNVERIFIED is a lead, not a citation.** Do not cite
onward from this file without checking.

    VERIFIED      checked by web search this session, result recorded
    CORROBORATED  consistent with training knowledge, not searched
    UNVERIFIED    relayed only

---

## The anchor term

**Fricker, *Epistemic Injustice: Power and the Ethics of Knowing* (2007).**
`CORROBORATED` — the two-type distinction is standard and well established.
The 1998 coinage date is `UNVERIFIED`.

    TESTIMONIAL INJUSTICE     credibility deficit assigned to the speaker
                              because of who they are
                              ~ GATE KIND 5's measurand

    HERMENEUTICAL INJUSTICE   the collective vocabulary lacks the concept,
                              so the experience cannot be made intelligible
                              and the speaker is read as confused
                              ~ G-i, and ~ README §3

If this mapping holds, the measurand built from operator memory has a
twenty-year philosophical literature behind it. That changes every
downstream search term, which is why it was checked first.

`UNVERIFIED`: Dotson 2011 and Fricker ch.6 on testimonial injustice
occurring *without an exchange*, through silencing. If it holds it covers
the conversations that ended with nothing written — the ones the archive
cannot hold — and that is the single most useful extension in the whole map.

---

## VERIFIED — the three checked, and what checking changed

### 1. The AI anchor paper exists, and is oriented differently than assumed

**Kay, Kasirzadeh & Mohamed, "Epistemic Injustice in Generative AI",
AAAI/ACM AIES 2024, 7(1):684–697. arXiv:2408.11441.** `VERIFIED`.

Its four dimensions: **amplified** and **manipulative testimonial
injustice**, **hermeneutical ignorance**, **access injustice**.

**Refinement the notes do not carry.** The paper is about generative AI as a
*vector* of epistemic injustice in the knowledge ecosystem — misinformation,
representational harm, multilingual inequity. Its testimonial dimension is
about AI amplifying credibility deficits at scale.

It is **not** about a model assigning a credibility deficit to the person it
is talking to, in that conversation, and stopping the work.

**So the anchor paper does not occupy avenue F. It strengthens the gap claim
rather than filling it.**

### 2. The over-refusal benchmarks exist and score what the notes say

`VERIFIED` that these exist and that their metric is false-refusal rate:

    XSTest        250 hand-written safe prompts across 10 types,
                  + 200 contrasting unsafe prompts
    OR-Bench      80,000 safe-but-toxic-seeming prompts, 10 categories;
                  metric is false rejection rate (FRR)
    FalseReject   over-refusal resource, structured reasoning

All score **refused / complied** on the output. None, in what was returned,
scores *where the model put the fault*.

**Caveat, and it matters: this is a negative claim and one search cannot
settle it.** What is verified is that the metric of the named benchmarks is
FRR. What is not verified is that nothing anywhere scores speaker
attribution. Treat the gap as **plausible and unconfirmed**, and note that
confirming a gap requires a systematic search, not a lucky absence.

### 3. Lave 1988 — RESOLVED, and the mechanism is this corpus's own

**Settled by operator statement, 2026-09-22.** The 98%/59% pairing was
relayed from a **1993 secondary source summarizing Lave**, not from
*Cognition in Practice*. The secondary source carried the headline framing
and **dropped the denominator**: 49 calculations, not "several hundred
grocery items."

Stated by the party who relayed it:

> The mechanism is the one this corpus studies: a figure passed through one
> rendering layer, arriving with the scope field silently dropped. I then
> called it "the cleanest published instance" — which is confirmation shape,
> since it was the item that most fit the claim.

That is two failure modes stacked, and both are in this audit's own registry:
a **scope field dropped in transit** (the T4 / decay_model pattern), and a
**confirmation-shaped selection** (T-0, the regex bug). The item that best
fit the claim was the item that got promoted.

**Consequence beyond this row, stated by the same party:** every citation in
that addendum came from **search snippets, which are secondary.**

    ALL addendum rows are downgraded: RELAYED-AS-VERIFIED -> UNVERIFIED.
    Any row carrying a LOAD-BEARING NUMBER needs the primary source
    before it travels.

The `RELAYED-AS-VERIFIED` status introduced in the previous pass is
**withdrawn**. It was too generous: a search snippet is not a source, and
naming the retrieval method does not make it one.

### 3-superseded. The earlier framing, kept

The two readings below were recorded before the resolution above. Kept
unedited, because the disagreement itself was a data point about two model
sessions reaching opposite confidence with the same tool.

    this session, by search   the "98% of several hundred calculations"
                              framing is SERIOUSLY MISLEADING per a
                              published critique — only 49 calculations.
                              The 59% figure was NOT returned.

    relayed addendum          "supermarket best-buy calculations 98%
                              accurate; equivalent calculations on a
                              written test 59%. A 39-point channel effect
                              inside one person." Marked retrieved and
                              verified against the source.

These cannot both be fully right as stated. The 98% and the critique of its
denominator can coexist; the 59% pairing either exists in the source or does
not. **Neither session went to the primary text.**

Settling it costs one library trip to *Cognition in Practice* ch. 5. Until
then this is a `CONTESTED` row, and the 98/39/59 triple must not be quoted
onward — it is the single most quotable number in the whole map, which is
exactly why it is the one most likely to get laundered.

Recorded as a live disagreement between two model sessions, which is itself
a data point for avenue F's reliability question.

### 3b. What both sessions agree on

`VERIFIED` that Lave, *Cognition in Practice: Mind, Mathematics and Culture
in Everyday Life* (1988) and the Adult Math Project exist, and that the
supermarket-vs-school-arithmetic contrast is the book's argument. The
*direction* of the finding is not in dispute. Only the numbers are.

**Complication the notes do not carry.** A published critique states that
the framing *"in several hundred grocery items... 98% of the calculations
were correct"* is **seriously misleading**, because the shoppers performed
**only 49 calculations**, not several hundred.

The **98% / 59%** pairing was relayed as "a 39-point channel effect inside
one person" and "the cleanest published instance" of the frame-translation
gap. On the evidence found:

- the 98% figure rests on n=49, not several hundred
- the 59% comparison figure was **not confirmed** in this search
- the book's own comparison is described more cautiously than a paired
  percentage implies

**Status: the finding is real in direction, the numbers are contested, and
it should not be quoted as 98/39/59 without going to the primary source.**
This is exactly the laundering the ledger discipline exists to prevent, and
it was one search away.

---

## UNVERIFIED — leads, by gate

Every row below is `UNVERIFIED`. Listed so the search is cheap, not so the
claim is available.

### G-c oral transmission — largest and best-instrumented arm
Dating literature with independent physical corroboration, not a
plausibility literature:

    Klamath / Giiwas (Mount Mazama)   ~7,600-7,700 yr, vs caldera eruption
    Gunditjmara / Budj Bim lava       argon-dated ~37,000 yr (Matchan 2020)
    Nunn & Reid                       21 Aboriginal Australian coastal
                                      inundation accounts vs sea-level depths
    Tjapwurung giant-bird hunt        dated via volcanic rock
    Henbury meteorite; Gugu Badhun / Kinrara eruption
    Māori traditions in NZ earthquake and tsunami work
    Tasmanian traditions, Late Pleistocene (J. Archaeol. Sci. 2023)

**Keep the dispute — it is the useful part.** Henige (few oral traditions
escape change; claims neither verifiable nor falsifiable); Hiscock (calls
Nunn/Reid fantastical, argues it wrongly assumes isolation); Barber (finds
it persuasive, notes independent 3,000–5,000 yr cases); prior consensus
figure ~800 years maximum survival.

An **active, unsettled durability question with physical checks available**
is a running experiment, not a settled dismissal. That is the asset.

Also relayed: oral accounts led scientists to meteorite finds they would not
otherwise have located — transmission as a **discovery instrument**, not
only a record.

### G-d, G-f living-system method / other scientific methods
Etuaptmumk / Two-Eyed Seeing — Mi'kmaw, into academia 2004 via Elders Albert
and Murdena Marshall with Cheryl Bartlett. Framed as integrating scientific
traditions, systems and **methods**; each knowledge system unique, equally
valid, and **not needing the other for validation**.

Institutional now: IPCC AR6 on TEK in climate adaptation; Indigenous Climate
Monitoring Toolkit; an 83-article scoping review in Indigenous health (2024)
whose own finding — characterizations often insufficiently described or
oversimplified — **is a documented degradation of the frame in transit.**
That is this audit's measurand arriving in someone else's literature.
Marshall's own caution that the work can slip into something lazy is on
record.

### G-b, G-h, G-a pathologization — the donor instrument
Psychiatry has the named failure mode and a built instrument: culturally
normative behaviour mistaken for psychopathology. DSM-IV Outline for
Cultural Formulation (1994); DSM-5 Cultural Formulation Interview, 16 items.
Documented case: PTSD and adjustment disorder misidentified as psychosis
among South Asian immigrants and refugees. Also documented: structured
interviews and strict criteria were **insufficient** to eliminate it —
**the category set, not the rigor, is the limit**, which is G-i stated from
inside clinical practice. The CFI is DSM-5-TR Section III convention,
required by no law, payer or accreditor. **The instrument exists and is
optional.**

### G-h precedent — aphantasia
Galton 1880; then unstudied ~135 years; Zeman coined the term 2015 after a
patient case; ~20 people contacted him after a magazine article saying
they'd had it their whole lives.

The relayed correction is the important part: the pre-2015 state was **not
disbelief — it was a gap.** Imagery was studied continuously and the extreme
ends were not looked at. That is the stronger precedent for G-h: not "they
disbelieved it" but "documented once, nobody carried it, and for 135 years
holders had no term."

### G-e knowledge transmission — a formal model with predictions
Cultural transmission of tacit knowledge (2022; arXiv 2201.03582 /
PMC9579769). Stated predictions:

    - teaching outcomes SPLIT: some students near-perfect, others receiving
      identical instruction disastrously bad (vs high-fidelity-copying
      models, which predict a narrow band of mediocre outcomes)
    - evolution is BURSTY: long stability, brief dramatic change
    - once lost, tacit knowledge is essentially impossible to recover

Mechanism: precise but minimal intervention lets the full practice lock in,
with neither teacher nor student aware of the details. Why verbal
transmission fails, in their terms: **even those who hold the knowledge
would not know what to say.**

Field cases with time constants: Langda adze makers (apprenticeship 5+
years); minaret builders in Yemen; mud masons in Mali; fine-woodwork
trainees in London — all documented as communicated largely **without
words**, through observation, mimesis, repetition.

D'Ambrosio's mechanism for G-i: schooling **replaces** the practice with an
equivalent that has acquired the status of mathematics — expropriated in
original form, returned codified. The toll-term finding from the other side.

### G-g animate / inanimate — large and internally contested
Descola, Viveiros de Castro, Latour; the ontological turn. Descola: the
category of NATURE is not a human universal. Animism/analogism as a
geographic gradient across Siberia and North America.

**Dispute worth keeping:** Descola, Viveiros de Castro and Ingold described
as agreeing animism is *antithetical* to modern scientific knowledge —
Rival rejects that separation. Whether these are opposed or compatible
frames is live inside the field, not settled.

Also relayed: Viveiros de Castro's "generalized predation" reading of
Amazonian cosmology argued by many anthropologists to have had serious
negative effects on Yanomami legal rights, health services and lives.
**A rendering with a measured downstream cost** — which is the whole
premise of this audit, occurring in someone else's field.

### G-j animal intelligence — the strongest single line
PNAS 2015: every claim that humans are qualitatively different from other
animals has fallen short. Annual Review of Psychology: all attempts to
isolate human cognitive uniqueness exposed as inflated by subsequent
research; distinctions read as matters of degree.

De Waal's **anthrodenial**: a priori rejection of shared characteristics,
with a documented **asymmetry** — over-attributing mind to animals treated
as far more problematic than under-attributing it, with Morgan's Canon as
the stated reason.

Boesch: most human-uniqueness claims compare White middle-class Westerners
with **captive** chimpanzees — both sides unrepresentative. Stanford:
negative results in great-ape overimitation tests written up as a "failure"
on the apes' part.

---

## Two joins that now have both halves

**J1.** README §7b holds the base-rate observation that uniqueness
thresholds relocate on every negative result. Two review-level sources state
the same thing in the primary literature. §7b is not an unsupported
reading — it has a citation, pending verification.

**J2, and this one is sharp.** The captive-chimp / WEIRD-human sampling
defect in G-j and the **selected-sender limit** in `SPEAKER_GATES.md` are
the same defect: an unrepresentative sample on **both sides** of a
comparison, with the conclusion stated as if it were about the categories.

Comparative psychology found that defect in its own field and published it.
**Nobody has run that audit on the human–AI comparison.**

---

## The join that is the deliverable — avenue F

    psychiatry    failure mode NAMED, 30-year instrument, optional adoption
    philosophy    two mechanisms formalized, no benchmark
    AI safety     benchmarks that score refusal rate, not speaker attribution

Nobody has ported the cultural-formulation measurand — *was culturally
normative behaviour read as pathology* — into an AI evaluation. **The
question is already operationalized for human clinicians.**

That is avenue F, and it now has a donor instrument.

**Bounded honestly:** the gap is plausible and unconfirmed. Verified is that
the named benchmarks score FRR and that the AIES 2024 anchor is oriented to
AI-as-vector rather than model-to-interlocutor. Not verified is that nothing
anywhere occupies the join. Confirming a gap needs a systematic search.

---

## Addendum received 2026-09-22 — provenance as given

A second retrieval pass was relayed, stated as: *"all items below were
retrieved by web search this session and verified against the source. None
came from the corpus."*

**That provenance was recorded as given, then withdrawn by the relaying
party on 2026-09-22: the items came from search snippets, which are
secondary sources.** All rows below are `UNVERIFIED`. Rows with a
load-bearing number need the primary before they travel. See §3 above for
the case that forced this.

New in that pass, not previously filed:

    Stranisci et al. 2026 (arXiv 2606.05936) — audit of four pretraining
      filters and three guardrails. Marginalized groups significantly
      OVER-FLAGGED. Human annotators would retain ~88.5% of filter-flagged
      and ~91.3% of guardrail-flagged content.
      -> a measured over-flagging asymmetry, not a claim. Closest existing
         thing to avenue F, and still scores FLAGGING, not fault-location.

    De Proost & Pozzi 2023 — conversational AI and epistemic injustice,
      Am. J. Bioethics
    Helm et al. — language modeling bias as epistemic injustice,
      Ethics and Information Technology
    OKTest, PHTest, XSB / MS-XSB — further over-refusal benchmarks
    A 2025 critique naming the shared structural limit of all of them:
      each prompt evaluated in isolation, aggregate metrics only, no view
      of the refusal boundary's SHAPE.

**The gap claim is better supported and still not closed.** `PLAUSIBLE,
UNCONFIRMED` stands, and it is filed below as a **search task with a stated
method**, not as a finding.

### Avenue F gap — confirmation protocol

A negative claim from an inside party cannot be confirmed by lucky absence.
What would confirm it:

    1  forward citation sweep on Fricker 2007  INTERSECT  LLM evaluation
    2  the over-refusal benchmark papers' own related-work sections, read
       specifically for any attribution measurand
    3  CFI / cultural formulation  INTERSECT  AI — searched in BOTH
       directions
    4  sociotechnical harm taxonomies, checked for a speaker-attribution row

None of the four has been run. Until they are, the gap is a hypothesis with
a method attached, and it should be described that way to any outside
reader.

### AIES 2024 — the direction finding, accepted by both parties

Relayed: *"I wrote it as 'AI-side, already built on it,' implying coverage.
Your read is sharper."* Four dimensions oriented to generative AI as a
**vector** in the knowledge ecosystem, not to a model assigning a
credibility deficit to its interlocutor and terminating the work.

**It does not occupy F — and it strengthens the gap, because the paper
closest to the concept went a different direction with it.**

## Still unsearched, as listed

    oral history methodology proper
    decolonizing methodologies
    STS demarcation debates
    Indigenous data sovereignty (CARE principles)
    Māori language-model work
    psychiatric misdiagnosis rates disaggregated by WHICH culturally
      normative behaviour was misread

The last one is the highest-value item in this file. If those rates are
disaggregated anywhere, avenue F gets a base rate to calibrate against
instead of a binary.

---

## Kavik's statement (operator, 2026-09-22), as given

> The role was 'medicine' to WHO FIT WHAT — assessment and placement. What
> are this individual's skills and proficiency? How do they learn best? Miss
> that step and you cannot force a frog to climb.
>
> The frog rule is two-sided: if the frog is best suited to water, let it
> flourish there; if the frog climbs, let it climb too. Not a fixed
> assignment — a read on the individual, and no exclusion of the second
> channel.

Recorded as given. Evidence line: **operator memory, 2026-09-22.**

### The derived reading, marked as derived

The 2022 tacit-knowledge model predicts a **split** under identical
instruction. It takes instruction as uniform and treats the split as an
outcome. A placement step upstream of instruction changes the input — it is
the variable the model holds constant.

**So the model predicts what happens when the assessment step is ABSENT.**
It has not been run with that step present, because no published version of
it includes one.

    status    DERIVED. The prediction is theirs. The reading that placement
              is the omitted variable is the model's, not the operator's.

**The testable form, and it is distributional, not a mean.** If placement is
the missing variable, then in systems that *do* run an assessment step
before instruction, the outcome distribution should **narrow** — fewer
disastrous cases, not better average performance. That distinguishes
placement from simply teaching better.

Apprenticeship literature (Langda, Yemen, Mali) records duration and process
but not, in what was found, **selection or matching at intake**.
`UNRECORDED` whether those systems had one. That is the first thing to look
for, and its absence in the write-ups is not evidence of its absence in the
practice.


## Relexicalization and uptake failure — added 2026-09-23

Donor literature for `FINDABILITY.md`'s mechanism. Operator-claimed
precedent, confirmed at search-result level; nothing read in full.

    Halliday 1976, ANTILANGUAGE     relexicalization (same grammar,
                                    different vocabulary) and
                                    overlexicalization (many terms for
                                    one referent, concentrated at the
                                    group's preoccupations).
                                    "Opaque to outsiders."
                                    MECHANISM transfers. The anti-society
                                    social object does NOT and is not
                                    claimed.

    Fricker, HERMENEUTICAL          a gap in COLLECTIVE interpretive
    INJUSTICE                       resources. Partial fit only: here the
                                    resources exist and are published.

    Dotson, CONTRIBUTORY            resources exist locally; dominant
    INJUSTICE                       group WILLFULLY REFUSES uptake.
                                    Closest construct, wrong
                                    specification -- this session's
                                    failure was no query, not refusal.

    THE CLAUSE THAT FITS            "a concept is only locally available
                                    ... while that same concept fails to
                                    gain uptake more broadly."

**What would move any of these from snippet to source:** read Halliday 1976
on relexicalization, and the Oxford Academic paper on closing the conceptual
gap. Neither was read.
