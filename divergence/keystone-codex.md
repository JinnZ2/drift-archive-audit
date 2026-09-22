# divergence/keystone-codex

A3 read: 27 commits, 2025-08-28 → 2026-09-22.
Git author field: Claude 19, JinnZ2 7, `Jinn2Z` 1 (typo, `0aed497`). **Author = pusher, not content author (CORRECTION-001).** Pre-agent content is model output transported by paste; source model UNSET.
Regime boundary: commit 6 (`be471a3`, 2026-03-22, "Add CLAUDE.md") after a
199-day gap. `TRANSPORT×MODEL` — paste→agent and model change together.

| # | commit | date | file(s) | what replaced what | d_type | split | channel |
|---|---|---|---|---|---|---|---|
| KC-1 | `34498a6` | 2025-08-28 | data/*, build_graph.py | `unlocks` declared as the only outward relation; 15/15 edges dangling, 0% closure. `build_graph.py` emits 15 arrows into undeclared space | OTHER (unbuilt at origin) | TARGET stated, endpoints absent | UNATTRIBUTABLE |
| KC-2 | `34498a6` | 2025-08-28 | data/governance/haudenosaunee_council.json | filename says `haudenosaunee_council`, `"id"` says `great_law_of_peace` | OTHER | — | UNATTRIBUTABLE |
| KC-3 | `6ff1e05` `d31804a` | 2026-03-22 | src/*.py | `os.walk` loaders 4 → 6 → **8** (6 in src/ + 2 in tests/ at `d31804a`) | D4 re-explain treadmill | RENDERING duplicated | UNATTRIBUTABLE |
| KC-4 | `b05bc21` | 2026-08-14 | src/corpus.py | all 8 loaders → 1 (`corpus.py`). Registry files at `data/` top level separated from entries in `data/<domain>/` | — (repair) | RENDERING consolidated | UNATTRIBUTABLE |
| KC-5 | `6ff1e05`…`d2f96a0` | 2026-03-22 | data/** | 5 entries → 42; unlock edges 15 → 90; **closure 0% → 44%** (40 of 90 resolve). Commit subjects name it explicitly: "Resolve highest-impact dangling links: 3 entries, 11 edges resolved" | — | **TARGET advanced.** The relation named at t=0 was built toward, not dropped | UNATTRIBUTABLE |
| KC-6 | `b2a5393` | 2026-08-17 | rules/keystone_rules.json | v1.0 (4 criteria, all about the TECHNOLOGY, pass 0.65) → v1.1 (+`evidence_strength`, `evidence_independence`, `claim_coverage`, pass 0.70). `evidence.quality`, collected but unscored at t=0, became a measurand | — | TARGET extended to the record, as the root data already anticipated | UNATTRIBUTABLE |
| KC-7 | across corpus | 2025-08 → 2026-09 | data/** | longevity_years / era-span ratio: **mean 0.62 → 0.95**, max 0.88 → 1.00, count over 1.0: **0 → 0** across 42 entries. `hxaro` sits at exactly 1.00 (125 / 125) | **D3 status field dropped** | **RENDERING changed.** The stated rule (never claim more than the span) holds with zero violations. The unstated one (discount below the span by an epistemic margin) did not: the margin fell 38% → 5%. Under CORRECTION-001 the margin is the FIRST MODEL's uncertainty rendering, not the operator's; no later model reproduced it because the schema never named it. Whether the operator wanted uncertainty here at all is UNSET — on the verify form | UNATTRIBUTABLE |
| KC-8 | `b05bc21` | 2026-08-14 | unknowns/, ledger/, hypotheses/, src/falsify.py | UNSET/UNKNOWN/dormant vocabulary 0 files → 6 files; falsification vocabulary 0 → 22 files. "Dormant != resolved" introduced as an explicit third value | — (addition) | new status apparatus, absent at t=0 | UNATTRIBUTABLE |
| KC-9 | (never) | — | README.md | "Initiated by JinnZ2 × ChatGPT" present at root, present at HEAD, unchanged | — | provenance tag SURVIVED | — |
| KC-10 | — | HEAD | src/, rules/ | `ethical_alignment`: populated in every entry since t=0, still scored by **nothing**. Present only in `fieldlink_export.py` (re-export) and `scaffold.py` (writes 0.0) | D3 status field never promoted | instrumented, never a measurand — 13 months | UNATTRIBUTABLE |
