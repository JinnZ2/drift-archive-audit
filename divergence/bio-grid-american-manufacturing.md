# divergence/bio-grid-american-manufacturing

A3 read: 63 commits, 2025-07-10 → 2026-08-16.
Git author field: JinnZ2 50, Claude 13. **Under CORRECTION-001 the git author is the PUSHER, not the content author.** All pre-agent content is model output transported by paste; the source model per commit is UNSET.
Regime boundary: commit 47 (`ba6f3d1`, 2026-06-02), after a 204-day gap.
Both sides are model-authored; what changes is TRANSPORT (paste → agent) and
MODEL (unknown → named), confounded.

| # | commit | date | file(s) | what replaced what | d_type | split | channel |
|---|---|---|---|---|---|---|---|
| BG-1 | `abb4b49` | 2025-07-10 | README.md | nothing replaced — rendering A (`$85B / 275k jobs / 340% ROI / 99.95% / 500 H100 / status: Mobilizing`) and rendering B (`a speculative infrastructure framework... a thought experiment gone operational`) committed in the SAME FILE, A first, B after an unterminated fence | OTHER (co-origination) | TARGET intact in B; A never carried it | UNATTRIBUTABLE |
| BG-2 | `abb4b49` | 2025-07-10 | Technical-equations.md vs docs/FullHex.md, docs/Blueprint/Ultra-compressed.md | prose names `φ = 1.618` "the BioGrid base tuning constant" (ONE constant, ONE name) while both hex blobs carry `phi1.0008` and the engine uses `this.phi = 1.0008` | **D5 no verbal anchor** | RENDERING collapsed two couplings into one noun; TARGET (two distinct couplings) survived in the hex + the engine | UNATTRIBUTABLE — and the original reason ("both encodings operator-authored") is withdrawn under CORRECTION-001; source model per file is UNSET and the two encodings may be different models |
| BG-3 | `abb4b49` | 2025-07-10 | core_brief.md (base64) vs FullHex.md + Ultra-compressed.md (hex) | self-healing recovery `2minutes` vs `20min` | OTHER | RENDERING conflict | **CORRECTED 2026-09-23: UNATTRIBUTABLE -> TOOL_CANDIDATE.** Operator, on the A6 form: the interval was *"whatever the capabilities of the AI model at that time"* — `operator memory, 2026-09-23`. The field is `NOT_OPERATOR_SET`, so AGENT shaping is excluded on this row. It is not `TOOL`: source model per file is UNSET under CORRECTION-001, and capability vs sampling variance vs two different models is not separated. `verify/ANSWERED.md` BG-OPEN-1 |
| BG-4 | gap | 2025-11-10→2026-06-02 | — | 204 days, no commits. Regime changes across the gap: web-UI paste commits (`Create X.md`) → agent branch/PR commits (`feat:`, `fix:`). **`TRANSPORT×MODEL`** — transport and generating model change together | OTHER (tooling) | neither | **TOOL_CANDIDATE** — the encoding layer demonstrably changed here; what it did to content is not established |
| BG-5 | `1ae3aec` `857641b` `f4ed2ad` | 2026-08-14 | README, Economic_Impact, Northwoods_Bridge_Strategy, risk_assessment, implementation_matrix, +legacy/ | rendering A's figures withdrawn and marked: "340% ROI was withdrawn in the 2026 review", "99.95% system reliability **target** — no reliability analysis exists yet", `spec_superseded: "500 H100 GPUs"` | D1 frame expiry (of the RENDERING) | **RENDERING falsified; TARGET survived.** Not stage-2 loss — the target never rested on those figures | UNATTRIBUTABLE |
| BG-6 | `1ae3aec` | 2026-08-14 | Technical-equations.md, SCIENCE_UPDATE_2026.md, Blueprint/* | the φ collision of BG-2 resolved INTO TWO couplings: "φ = 1.618 remains correct for **geometric** use — spacing, radii, layout. That was never in question"; φ⁻¹ for decay; `1.0008` retained as the spacing/engine constant | — (repair, not divergence) | TARGET recovered its second coupling after ~13 months | see Phase C, C-1 |
| BG-7 | (never) | — | `docs/trust_model.md` | **nothing.** Blob `c4a2523` at root == blob at HEAD. Byte-identical across 63 commits, 14 months, and the entire agent-era rewrite | — | TARGET's WHOLE_STATED encoding untouched | — |
| BG-8 | (never) | — | `Regional-bio-grid/dual-system/integration/RecoveryReadme.md`, `data/northwoods_specs.md` | 2 root files still byte-identical to 2025-07-10 and still carrying a withdrawn figure with no marker in-file. 28 of 67 root files are byte-identical to root | D3-adjacent (status field never applied) | RENDERING not reached by the correction | UNATTRIBUTABLE |

## measured

    root files:                            67
    still present at HEAD:                 59
    byte-identical to root at HEAD:        28  (42%)
    withdrawn figure + no in-file marker:   2

    Earlier raw greps suggested 9-19 live files still carrying withdrawn
    figures. Inspection showed all but 2 sit inside explicit supersession
    blocks. The raw count was a false positive and is retracted here.
