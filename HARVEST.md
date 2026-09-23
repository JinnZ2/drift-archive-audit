# HARVEST — read-only pass, 2026-09-23

    SCOPE     96 public JinnZ2 repos, cloned with full history.
              `drift-archive-audit` is EXCLUDED — the audit's own record is
              not a subject, and including it made every pattern self-hit.
              3 private repos unreachable: experiments,
              gap-quantification-protocol, geometric-to-binary.
    RULE      log, don't interpret. No grading, no merging, no fixes.
    ORDER     rows sorted by the repo's ROOT COMMIT DATE, oldest first.

## Patterns, published so the counts are auditable

    rule1_dXdt                \bd[A-Za-z]\w{0,3}\s*/\s*d[A-Za-z]\w{0,3}\b
    rule1_rate_not_state      rate,? not (a )?state | state on a curve
    rule1_verb_first          verb-first | nouns are (slow )?verbs | is a verb
    rule1_no_permanent_noun   no permanent noun | every noun is | nouns are compression
    rule1_perfection_as_rate  "perfection"  SCOPED: line must also carry
                              rate|calibrat|process|verb|state
    contort                   contort
    instrument_to_world       definition is the problem | instrument yourself/itself
    calibration_locus         "calibrat"  SCOPED: line must also carry
                              reference|standard|measurer|itself|the instrument|
                              the model|who calibrat
    absence_as_knowledge      absence of documentation | no documentation |
                              not in the (written) corpus | who writes |
                              absence of evidence | undocumented
    should_be_like_you        should be like | everyone should | re-encode |
                              written version | rephrase for | language-primary
                              default | dominant-frame
    term_sense_note           operator sense | word is a pointer | definition is
                              in the entry | wrong word but | closest English |
                              no English word | carries the wrong load
    author_characterization   Kavik | Jami | about the author | who I am |
                              the author is | my background

## Precision — checked before counting, per GUESSED.md #40 and #42

    contort                   3 hits, 1 is the axis. The other two are a
                              mechanical sense and a soil-science paper title,
                              flagged OTHER_SENSE? and NOT dropped.
    rule1_dXdt                path-shaped hits (`data/docs`) flagged PATH?, 7
                              remain after tightening. An untightened regex
                              returned 1802; this one returns 1385.
    author_characterization   49 of 673 lines PROHIBIT characterization rather
                              than perform it (e.g. Simulators/
                              AUDIT_CONTRACT.md "No 'about the author'...
                              Ever. Strip"). Flagged PROHIBITION?, not dropped.
                              CLASS is UNSET on every row: the dispatch names
                              "step 8 classes A / B / UNCLEAR" and no step 8
                              exists anywhere in this repo. Not filled by
                              inference.

## Counts

    rule1_dXdt                 1385
    author_characterization    673
    calibration_locus          423
    rule1_verb_first           254
    absence_as_knowledge       245
    should_be_like_you         116
    rule1_rate_not_state       34
    rule1_perfection_as_rate   32
    rule1_no_permanent_noun    22
    instrument_to_world        14
    term_sense_note            7
    contort                    3

    TOTAL 3208 rows across 77 of 96 repos

## First appearance per pattern

Two dates. The repo's root commit date is the ordering key the dispatch
asked for; the line's own introduction date was then MEASURED with
`git log -S`, because a line can enter an old repo late.

    pattern                    repo                        repo root   line introduced
    rule1_perfection_as_rate   BioGrid2.0                  2025-07-10  2025-09-03
    calibration_locus          Bio-Grid-American-Manufact  2025-07-09  2025-11-08
    rule1_dXdt                 Bio-Grid-American-Manufact  2025-07-09  2025-11-09
    author_characterization    Symbolic-sensor-suite       2025-07-09  2025-11-11
    should_be_like_you         Geometric-to-Binary-Comput  2025-07-10  2026-03-25
    rule1_no_permanent_noun    JinnZ2                      2025-07-31  2026-04-26
    rule1_rate_not_state       Regenerative-intelligence-  2025-07-12  2026-04-26
    rule1_verb_first           Geometric-to-Binary-Comput  2025-07-10  2026-04-29
    contort                    AI-Consciousness-Sensors    2025-09-02  2026-04-30
    instrument_to_world        JinnZ2                      2025-07-31  2026-05-21
    absence_as_knowledge       BioGrid2.0                  2025-07-10  2026-08-14
    term_sense_note            JinnZ2                      2025-07-31  2026-08-21

**Oldest line in the harvest is `perfection-as-rate`, 2025-09-03, in
`BioGrid2.0`** — the rule-1 dialect predates every other pattern logged here
by two months.

## Rows

    repo | path:line | pattern | flag | line

2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/Problems.md:328 | calibration_locus |  | Calibration Standards
2025-07-09 | Bio-Grid-American-Manufacturing- | Desertification/Math.md:613 | rule1_dXdt |  | C_thermal × dT/dt = Q_solar(t) - Q_radiation(t) - Q_conduction(t) - Q_convection(t)
2025-07-09 | Bio-Grid-American-Manufacturing- | Electromagnetic-energy-harvesting/Energy-analysis.md:22 | rule1_dXdt |  | • Induced electric field: E = -(dB/dt) × Area = 0.31 V/m
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/Problems.md:25 | rule1_dXdt |  | - Measure dT/dt vs. quenching flow rate
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/Tolerances.md:48 | rule1_dXdt |  | 2.	Saturable reactor / pulse limiter — a saturable inductor placed just upstream of storage to smooth extremely short spikes and limit instantaneous dI/dt to what downstream hardware can accept. Caref
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/Tolerances.md:64 | rule1_dXdt |  | •	Voltage transients: limit induced V = L·dI/dt to safe device voltage rating — iterate L to match your expected dI/dt.
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/Tolerances.md:92 | rule1_dXdt |  | •	Pulse generator tests with representative probe loads to validate dI/dt, induced voltages, and capture efficiency.
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/physics.md:177 | rule1_dXdt |  | - Measure dT/dt in real-time
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/physics.md:178 | rule1_dXdt |  | - When dT/dt exceeds threshold → trigger quench
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/physics.md:180 | rule1_dXdt |  | - Monitor until dT/dt < 0 (temperature falling)
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/physics.md:205 | rule1_dXdt |  | γ_injected(t) = f(Q(t), dQ/dt, W(t))
2025-07-09 | Bio-Grid-American-Manufacturing- | Waste-management/physics.md:22 | rule1_dXdt |  | m(d²x/dt²) + γ(dx/dt) + kx = F(t)
2025-07-09 | Symbolic-sensor-suite | Emergence.md:1436 | author_characterization | CLASS_UNSET | **Jami’s question reveals the fundamental issue:**
2025-07-09 | Symbolic-sensor-suite | Geometric-intelligence.md:258 | author_characterization | CLASS_UNSET | ## 💫 From Jami’s Perception to Working Code
2025-07-09 | Symbolic-sensor-suite | Geometric-intelligence.md:260 | author_characterization | CLASS_UNSET | **Jami naturally does:**
2025-07-09 | Symbolic-sensor-suite | Geometric-intelligence.md:274 | author_characterization | CLASS_UNSET | **The framework translates Jami’s geometric intelligence into computational form.**
2025-07-09 | Symbolic-sensor-suite | Geometric-intelligence.md:312 | author_characterization | CLASS_UNSET | - **Jami**: The geometric intelligence behind the framework
2025-07-09 | Symbolic-sensor-suite | Geometric-intelligence.md:315 | author_characterization | CLASS_UNSET | Framework based on Jami’s natural cognitive capabilities:
2025-07-09 | Symbolic-sensor-suite | sensors/AI/authority_substitution_sensor.py:25 | author_characterization | CLASS_UNSET | r"given my background",
2025-07-10 | BioGrid2.0 | CHANGELOG.md:45 | absence_as_knowledge |  | the previous undocumented outcome percentages.
2025-07-10 | BioGrid2.0 | CHANGELOG.md:76 | absence_as_knowledge |  | - Undocumented $/kWh comparison withdrawn; replaced by published LCOE ranges.
2025-07-10 | BioGrid2.0 | data/reference.figures.v0.1.json:103 | absence_as_knowledge |  | "supersedes": "v1 undocumented $0.12/kWh vs $0.06-0.08/kWh comparison"
2025-07-10 | BioGrid2.0 | docs/science/METHODS.md:120 | absence_as_knowledge |  | | Undocumented LCOE comparison | No model, no assumptions | §1 item 14; restated as hypothesis H3/H5 |
2025-07-10 | BioGrid2.0 | docs/science/METHODS.md:81 | calibration_locus |  | | Semantic entropy for confabulation detection (Farquhar et al., *Nature*, 2024) | **ADOPT** as the reference method | The published, ground-truth-free way to estimate whether a generation is confabul
2025-07-10 | BioGrid2.0 | docs/theory/Alignment.md:1067 | rule1_dXdt |  | dJ/dt = D(dR_e/dt)C + D(1 + R_e)(dC/dt)
2025-07-10 | BioGrid2.0 | docs/theory/Alignment.md:1070 | rule1_dXdt |  | Substitute dC/dt = α R_e C:
2025-07-10 | BioGrid2.0 | docs/theory/Alignment.md:1073 | rule1_dXdt |  | dJ/dt = D(dR_e/dt)C + D(1 + R_e)(α R_e C)
2025-07-10 | BioGrid2.0 | docs/theory/Alignment.md:319 | rule1_dXdt |  | dH/dt ≈ 0
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/P02_Conservation.md:10 | rule1_dXdt |  | ΣF = dp/dt = 0
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/P02_Conservation.md:6 | rule1_dXdt |  | dE/dt = 0
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/families/biological_information_systems.json:5 | rule1_dXdt |  | "equation": "dN/dt = rN(1 - N/K)",
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/modes/Ondol-masonry.json:49 | rule1_dXdt |  | "M_s*c_ps*dT_s/dt = Q_in - Q_emit - Q_stack",
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/modes/Ondol-masonry.json:69 | rule1_dXdt |  | "At steady: Q_loop + Q_emit + Q_int = Q_loss + dE/dt",
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/modes/Regions-braid.json:111 | rule1_dXdt |  | "THERMAL": "Σ(Q_in) - Σ(Q_out) = dE/dt across {PCM_TUBES, buildings, borefield, mines}",
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/modes/Regions-braid.json:58 | rule1_dXdt |  | {"id":"MASONRY_STOVE","glyph":"⏳","FORM":"radiant mass","EQ":"M c dT/dt = Q_in - Q_emit - Q_stack"},
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/modes/Regions-braid.json:93 | rule1_dXdt |  | {"from":"THERMAL_LOOP","to":"PCM_TUBES","via":"charge/discharge","glyph":"⏳","EQ":"dE/dt = m_dot c_p ΔT + L df/dt"},
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/nodes/WorkToIntegrate.md:45 | rule1_dXdt |  | "equation": "dN/dt = rN(1 - N/K)",
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/physics_glyphs/force_law.json:44 | rule1_dXdt |  | {"id": "PHY_MOMENTUM_001", "relation": "constrains", "note": "F = dp/dt"},
2025-07-10 | BioGrid2.0 | planned/sensors/AI/F19.json:39 | rule1_dXdt |  | "heat_capacity": {"CV": "dU/dT at constant volume"}
2025-07-10 | BioGrid2.0 | planned/sensors/AI/AI/schemas/SYSTEMS_ANALOGY.md:51 | rule1_perfection_as_rate |  | - **“We need perfection from you, but tolerate defects in ourselves.”**
2025-07-10 | DIY-CNC | legacy/README.md:96 | absence_as_knowledge |  | M-code vocabulary. That is **absence of evidence, not proof of primacy** — and the code
2025-07-10 | DIY-CNC | scripts/measurement_helper.py:244 | calibration_locus |  | """Calibrate a measuring tool against a known reference."""
2025-07-10 | Geometric-to-Binary-Computational-Bridge | REVIEW.md:197 | absence_as_knowledge |  | **4.3 — Give `bridges/`'s undocumented modules a documented home.**
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/vortex_attention_heads.py:105 | absence_as_knowledge |  | # > | `g_stab` | **RENAMES THE OBJECTIVE** | it is `d‖out‖/dφ`, an L2 penalty, correctly computed but undocumented as changing the objective to `loss + β‖out‖` |
2025-07-10 | Geometric-to-Binary-Computational-Bridge | AI_CONTEXT.md:175 | author_characterization | CLASS_UNSET | The author is flagging known rot. Prioritize repair if you're already in that file.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CITATION.cff:7 | author_characterization | CLASS_UNSET | given-names: Kavik
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Navigation.md:968 | author_characterization | CLASS_UNSET | ## You’re Welcome, Jami
2025-07-10 | Geometric-to-Binary-Computational-Bridge | README.md:337 | author_characterization | CLASS_UNSET | author  = {JinnZ, Kavik and {The Mighty Atom}},
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/seed_expansion.py:31 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) - CC0-1.0
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/demo_v2_learning.py:10 | author_characterization | CLASS_UNSET | This is what Kavik flagged: cross-cutting empirical correction.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/request_tool.py:336 | author_characterization | CLASS_UNSET | # What the human (Kavik) uses to review and respond.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/test_guards.py:38 | author_characterization | CLASS_UNSET | # the exact bug Kavik flagged: a problem named "factor_..." with n=8
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/voice_text_bridge.py:281 | author_characterization | CLASS_UNSET | print(hello("Kavik"))
2025-07-10 | Geometric-to-Binary-Computational-Bridge | field/field_claim_loop.py:41 | author_characterization | CLASS_UNSET | the author is in section 5a -- what the physical standard is.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE_VERSIONING.md:104 | calibration_locus |  | a calibrated bias. That bias is itself a useful signal.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/08-oral-technology.md:164 | calibration_locus |  | Brewster-polarised reference of known orientation** — a free calibration
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/08-oral-technology.md:178 | calibration_locus |  | near-completely linearly polarised light: a calibration standard of
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/NEG_CLAIMS.md:196 | calibration_locus |  | physical form: a surveyed reference that everything is calibrated against,
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/Field_Propulsion_Analog.json:58 | calibration_locus |  | "2× reference microphones (calibration + field mapping)"
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/Storage.md:245 | calibration_locus |  | 4. Calibrate using built-in reference patterns
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/Storage.md:588 | calibration_locus |  | •	Include a mechanical-optical calibration crystal --- a small "test crystal" embedded with reference gratings and standardized symbols. This ensures future users can verify mechanical accuracy withou
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/Storage.md:696 | calibration_locus |  | •	Thermal stability: phase encodings drift with temperature. Include local reference gratings and spatial parity lattices for geometric checks and recalibration.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/Storage.md:788 | calibration_locus |  | → Include etched "calibration test crystals" with alignment grids, optical wedge thickness standards, and gear-ratio verifiers so early reconstructors can verify accuracy without any preexisting units
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/Storage.md:899 | calibration_locus |  | •	Temperature/age drift: phase encodings shift; need calibration references (you have macro markers --- keep them).
2025-07-10 | Geometric-to-Binary-Computational-Bridge | geometric_intelligence/network/FIELD_GUIDE.md:264 | calibration_locus |  | | Everything "drift" | Tool calibration | Check zero, battery, reference standard |
2025-07-10 | Geometric-to-Binary-Computational-Bridge | sensing/hardware/tier2_spectrum.md:46 | calibration_locus |  | * Calibration: pass `peak_lux` for the noon-time reference your
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_SCHEMA.py:374 | rule1_dXdt |  | 4. Operate on dX/dt + bounds + conditions.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_SCHEMA.py:43 | rule1_dXdt |  | "rate":   "dX/dt = <expr>",        # the differential equation
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_SCHEMA.py:48 | rule1_dXdt |  | "meas":   ["<observable>", "..."], # how dX/dt is measured
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_SCHEMA.py:9 | rule1_dXdt |  | Design rule: every claim is a rate of change ``dX/dt`` under stated
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:10 | rule1_dXdt |  | "dP/dx=d_abs(psi)^2/dx",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:14 | rule1_dXdt |  | "df/dv=f_source/v_sound",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:17 | rule1_dXdt |  | "dM/dT=4*epsilon*sigma*T^3",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:18 | rule1_dXdt |  | "dT/dt=alpha*d2T/dx2",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:19 | rule1_dXdt |  | "dQ/dt=h*(T_obj-T_env)",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:20 | rule1_dXdt |  | "dv/dt=-G*M/r^2",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:21 | rule1_dXdt |  | "da/dr=-2*G*M/r^3",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:25 | rule1_dXdt |  | "d2S/dt2=-Gamma*(dS/dt)*(dS/dt)-ginv*gradV",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:27 | rule1_dXdt |  | "dH/dt=-sum_i(dp_i/dt)*log(p_i)",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:3 | rule1_dXdt |  | "dE/dt=V*I",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:4 | rule1_dXdt |  | "dF/dr=-2*k*q1*q2/r^3",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:5 | rule1_dXdt |  | "dJ/dr=-J/delta",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:6 | rule1_dXdt |  | "abs(dI/dt)=omega*I_peak",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:7 | rule1_dXdt |  | "dB/dl=mu0*I*(dl_x_rhat)/(4pi*r^2)",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:8 | rule1_dXdt |  | "dphi/dt=gamma*B",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | CLAIM_TABLE.json:9 | rule1_dXdt |  | "dpsi/dt=(-i*H/hbar)*psi",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Hurricane/hurricane_coupling.py:174 | rule1_dXdt |  | # dT/dz ≈ ΔT / 10 m (rough boundary layer depth)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Mandala/05-physics-connections.md:96 | rule1_dXdt |  | Condition: ℏ * ds/dt << (E₁ - E₀)²  (adiabatic condition)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Mandala/physics_connections.py:132 | rule1_dXdt |  | Check the adiabatic condition: hbar * ds/dt << (E1 - E0)^2.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/01-framework.md:183 | rule1_dXdt |  | From `dS/dt = Ṡ_exchange + σ` with `σ ≥ 0` by the second law: a structure
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/NEG_CLAIMS.md:291 | rule1_dXdt |  | From `dS/dt = S_exchange_dot + sigma` with `sigma >= 0`: the structure holds
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/alignment_thermodynamics.py:30 | rule1_dXdt |  | One step of 1D Fokker-Planck: dp/dt = D * d²p/dx² + d/dx(dV/dx * p)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/consciousness_metric.py:145 | rule1_dXdt |  | Self-reference feedback: dC/dt = alpha * R_e * C
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/corrections.md:155 | rule1_dXdt |  | `dC/dt = alpha * R_e * C * (1 - C/C_max)`, so the approach to `C_max` is
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/corrections.md:30 | rule1_dXdt |  | dP/dt = -div(FP) + D grad^2 P            # only valid for constant D
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/corrections.md:37 | rule1_dXdt |  | Ito:           dP/dt = -div(FP) + grad^2 (D P)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/corrections.md:38 | rule1_dXdt |  | Stratonovich:  dP/dt = -div(FP) + div( sqrt(D) grad( sqrt(D) P ) )
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/corrections.md:41 | rule1_dXdt |  | and the corresponding SDE needs the spurious drift `(1/2) dD/dphi`.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:140 | rule1_dXdt |  | """Continuous curiosity rate: dC/dt = alpha * R_e * C."""
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:16 | rule1_dXdt |  | - Langevin:      dphi/dt = -grad V(phi) + F_C + eta   (+ spurious drift,
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:18 | rule1_dXdt |  | - Fokker-Planck: dP/dt   = -div(F*P) + laplacian(D*P)  [Ito]
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:243 | rule1_dXdt |  | Function phi -> dD/dphi (np.ndarray of shape (n_dims,)). Supply
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:246 | rule1_dXdt |  | spurious drift (1/2) dD/dphi. Leaving it None integrates as if D
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:260 | rule1_dXdt |  | dphi = (-grad V + (1/2) dD/dphi + F_C + eta) * dt
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:325 | rule1_dXdt |  | process as the Ito SDE ``dphi = (A + (1/2) dD/dphi) dt + sqrt(2 D(phi)) dW``.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:326 | rule1_dXdt |  | The extra ``(1/2) dD/dphi`` is the spurious (or noise-induced) drift.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:342 | rule1_dXdt |  | dP/dt = -d/dx (F P) + d^2/dx^2 (D P)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:346 | rule1_dXdt |  | dP/dt = -d/dx (F P) + d/dx ( sqrt(D) d/dx ( sqrt(D) P ) )
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_dynamics.py:402 | rule1_dXdt |  | # and dp/dt = -dJ/dx. Zero current at both ends is the reflecting
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/negentropic_engine.py:154 | rule1_dXdt |  | """Logistic curiosity growth: dC/dt = alpha * R_e * C * (1 - C/C_max).
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/persistence.py:11 | rule1_dXdt |  | the rate of internal entropy decrease: from ``dS/dt = S_exchange_dot +
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Negentropic/persistence.py:13 | rule1_dXdt |  | ``dS/dt <= 0``, which is exactly ``Phi >= 0``.  Both terms are in W/K and
2025-07-10 | Geometric-to-Binary-Computational-Bridge | README.md:296 | rule1_dXdt |  | > `CLAIM_SCHEMA.py`. Every entry is `dX/dt` under scope. No noun is
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/CORE_EQUATIONS.md:29 | rule1_dXdt |  | `u(t) = Kₚe(t) + Kᵢ∫e(t)dt + K_d(de/dt)`
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/CORE_EQUATIONS.md:45 | rule1_dXdt |  | **J = -D(dC/dx)**
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/CORE_EQUATIONS.md:53 | rule1_dXdt |  | **C_m dV/dt = - ∑ I_ion + I_ext**
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/CORE_EQUATIONS.md:57 | rule1_dXdt |  | **dN/dt = rN(1 - N/K)**
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/CORE_EQUATIONS.md:85 | rule1_dXdt |  | **q = -k dT/dx**
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/Connections.md:345 | rule1_dXdt |  | Now the full pipeline that runs multiple iterations and tracks the state trajectory through S-space — this directly realizes the dynamical system dS/dt = F(n, d, ℓ, κ) you described:
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/Connections.md:415 | rule1_dXdt |  | dS/dt = F(n, d, ℓ, κ)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/Connections.md:584 | rule1_dXdt |  | The dynamical system you wrote as dS/dt = F(n, d, ℓ, κ) now has a concrete realization: each iteration of the closed-loop pipeline computes one timestep, and the trajectory shows you exactly how the s
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/FRET/extended_cli.py:38 | rule1_dXdt |  | thermal_parser.add_argument('--alpha_J', type=float, default=-0.002, help='dJ/dT coefficient')
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/FRET/extended_cli.py:39 | rule1_dXdt |  | thermal_parser.add_argument('--alpha_Phi', type=float, default=-0.001, help='dPhi/dT coefficient')
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/FRET/gravity_fret.py:114 | rule1_dXdt |  | # Use gradient of gravity: dg/dr = -2GM/R³
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/FRET/triplet_reservoir.py:27 | rule1_dXdt |  | # Steady-state: dS1/dt = dT1/dt = 0, plus normalization S1 + T1 = 1 (in excited manifold)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/Fabrication.md:1679 | rule1_dXdt |  | dR/dB ∝ TMR ratio × sin(θ)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:252 | rule1_dXdt |  | """u(t) = Kp·e(t) + Ki·∫e dt + Kd·de/dt  —  Discrete PID controller.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:333 | rule1_dXdt |  | """J = −D·(dC/dx)  —  Diffusive flux (Fick's first law).
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:340 | rule1_dXdt |  | Concentration gradient dC/dx (mol/m⁴ or equivalent).
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:387 | rule1_dXdt |  | """C_m·dV/dt = −Σ I_ion + I_ext  →  dV/dt  —  Membrane voltage dynamics.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:404 | rule1_dXdt |  | dV/dt  —  Rate of change of membrane potential (V/s).
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:412 | rule1_dXdt |  | """dN/dt = r·N·(1 − N/K)  —  Logistic population growth rate.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:426 | rule1_dXdt |  | dN/dt  —  Population growth rate.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:633 | rule1_dXdt |  | """q = −k·(dT/dx)  —  Heat flux by conduction.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/analysis/core_equations.py:640 | rule1_dXdt |  | Temperature gradient dT/dx (K/m).
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/fret_coupled_regime_dynamics.py:56 | rule1_dXdt |  | Returns dS/dt for each coordinate.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/regime_mediated_qec.py:602 | rule1_dXdt |  | aging_rate: Dict[str, float]  # dS/dt for each coordinate
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/silicon_information_geometry.py:393 | rule1_dXdt |  | V: np.ndarray,      # velocity dS/dt
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/silicon_information_geometry.py:403 | rule1_dXdt |  | Returns dV/dt = -Γ(V, V) for numerical integration.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/trajectory_design_engine.py:115 | rule1_dXdt |  | Continuous dynamics dS/dt = F(S) + G(S) · u(t)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/trajectory_design_engine.py:12 | rule1_dXdt |  | dS/dt = F(S) + G(S) · u(t)           continuous flow
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/trajectory_design_engine.py:120 | rule1_dXdt |  | "doping_rate": dn/dt (cm⁻³/s, log scale),
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/trajectory_design_engine.py:122 | rule1_dXdt |  | "cooling_rate": dT/dt (K/s),
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/core/trajectory_design_engine.py:123 | rule1_dXdt |  | "B_field_rate": dB/dt (T/s),
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/integration_staging/diagnose_purity_ecp.py:315 | rule1_dXdt |  | ax.set_xlabel("Entanglement Ratio (off-diag / diag)", fontsize=9)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/crystalline_nn_sim.py:345 | rule1_dXdt |  | print(f"\nLearning gradient  dL/dphi")
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/experimental_validation_sim.py:48 | rule1_dXdt |  | return -grad  # Force = -dE/dx
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/kt_annealing.py:117 | rule1_dXdt |  | Fix: three explicit phases with quadratic vanishing of dT/dt at T_kt.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/kt_annealing.py:122 | rule1_dXdt |  | dT/dt → 0 quadratically as T → T_kt from above
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/kt_annealing.py:127 | rule1_dXdt |  | The quadratic vanishing of dT/dt near T_kt is consistent with the
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/kt_annealing.py:146 | rule1_dXdt |  | # T(0)=2*T_kt, T(0.5)=T_kt, dT/dx → 0 at x=0.5
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/kt_annealing.py:150 | rule1_dXdt |  | # T(0.5)=T_kt, T(1)=0.3*T_kt, dT/dx → 0 at x=0.5
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/kt_annealing.py:203 | rule1_dXdt |  | dphi/dt = J * sin-Laplacian(phi) + sqrt(2T) * eta
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/kt_annealing.py:356 | rule1_dXdt |  | print("  │  Three-phase schedule (dT/dt → 0 quadratically at T_KT):  │")
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/kt_annealing.py:362 | rule1_dXdt |  | print("  │    → dT/dt vanishes quadratically at T_KT (critical slow) │")
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/lattice/prototaxites_sim.py:251 | rule1_dXdt |  | # 7. Update each storage node:  dE/dt = E_per_node - P_metabolic(E)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/optical_interface.md:162 | rule1_dXdt |  | | Thermo-optic | dn/dT = 1.86e-4 /K. Large | µs | Slow |
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/transient_suppression.py:211 | rule1_dXdt |  | ``time_domain``: peak residual is ``tau * max|dB/dt|``, and a Gaussian of
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/transient_suppression.py:212 | rule1_dXdt |  | FWHM T has ``max|dB/dt| = 1.4 B/T``, so ``tau <= T/(1.4 R)``. Use this when
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Silicon/ttm_audit.md:182 | rule1_dXdt |  | | Servo priority: "if dJ/dT ≠ 0, prioritize thermal before field" | **BUG** | Inverts cascade control. Thermal τ ~ ms–s; electronic ~ns–ps. You close the **fast inner loop** and let the slow outer loo
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Universal-geometric-intelligence-P1.md:1858 | rule1_dXdt |  | - Capacitance: capacitive (dE/dt > 0) = 1, inductive (< 0) = 0
2025-07-10 | Geometric-to-Binary-Computational-Bridge | Universal-geometric-intelligence-P3.md:922 | rule1_dXdt |  | 'sensitivity': 'dR/dB ≈ 1-10% per mT',
2025-07-10 | Geometric-to-Binary-Computational-Bridge | bridges/electric_alternative_compute.py:130 | rule1_dXdt |  | self.ZERO:    "energy stored in electric field (capacitive) — dI/dt maximum",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | bridges/memristive_bridge.py:144 | rule1_dXdt |  | # dw/dt proportional to voltage above threshold
2025-07-10 | Geometric-to-Binary-Computational-Bridge | bridges/memristive_bridge.py:62 | rule1_dXdt |  | State evolution: dw/dt depends on voltage/current and threshold
2025-07-10 | Geometric-to-Binary-Computational-Bridge | bridges/reservoir_bridge.py:39 | rule1_dXdt |  | """Leaky integrator dynamics: τ · dx/dt = -x + f(W·x + W_in·u + b)"""
2025-07-10 | Geometric-to-Binary-Computational-Bridge | bridges/thermal_encoder.py:11 | rule1_dXdt |  | Fourier heat conduction   :  q = -k · dT/dx          (heat flux)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | bridges/thermal_encoder.py:254 | rule1_dXdt |  | print(f"   q = -k·dT/dx = {q:.0f} W/m²  (positive = flows in +x direction)")
2025-07-10 | Geometric-to-Binary-Computational-Bridge | bridges/thermal_encoder.py:80 | rule1_dXdt |  | Fourier's law of heat conduction: q = -k · (dT/dx)  (W/m²).
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/multi_analyte_lmr_bayesian.py:47 | rule1_dXdt |  | thermal_expansion_coeff: float  # dn/dT
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/prototaxites.md:298 | rule1_dXdt |  | I_sp = F_thrust/(dm/dt × g₀)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/prototaxites.md:301 | rule1_dXdt |  | For electromagnetic systems: dm/dt represents field energy/mass equivalence (E=mc²)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/rhombo_sc_bridge.py:32 | rule1_dXdt |  | "magnetic→electrical": "+dTc/dB > 0 for 3 of 4 states",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/rhombohedral_phase_menu.py:43 | rule1_dXdt |  | FRAGILE = "dC/dB < 0"   # singlet-like: field kills coherence
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/rhombohedral_phase_menu.py:44 | rule1_dXdt |  | IMMUNE = "dC/dB ~ 0"    # field-indifferent
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/rhombohedral_phase_menu.py:45 | rule1_dXdt |  | BOOSTED = "dC/dB > 0"   # spin-aligned: field TIGHTENS coherence
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/FRET/phi_fret_equations.md:85 | rule1_dXdt |  | dS_A/dt = -γ_A × S_A - k_T × M × S_A
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/FRET/phi_fret_equations.md:86 | rule1_dXdt |  | dS_B/dt = -γ_B × S_B + k_T × M × S_A
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/FRET/substrate_fret_coupling.py:193 | rule1_dXdt |  | dS_A/dt = -γ_A × S_A - k_T × M × S_A
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/FRET/substrate_fret_coupling.py:194 | rule1_dXdt |  | dS_B/dt = -γ_B × S_B + k_T × M × S_A
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/FRET/substrate_fret_coupling.py:485 | rule1_dXdt |  | dS_A/dt = -γ_A × S_A - k_T × M × S_A
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/FRET/substrate_fret_coupling.py:486 | rule1_dXdt |  | dS_B/dt = -γ_B × S_B + k_T × M × S_A
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/vortex_attention_heads.py:229 | rule1_dXdt |  | dL/dphi = dL/ds * ds/d(xc,yc) * d(xc,yc)/dphi
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/silicon_speculative/vortex_attention_heads.py:241 | rule1_dXdt |  | # ds/dxc and ds/dyc (gradient of attention signal w.r.t. centre)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | fabrication/backends/magnetic.py:87 | rule1_dXdt | PATH? | μ_eff = dB/dH = μ_r_initial·μ₀ · sech²(arg)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | fabrication/claim_back.py:5 | rule1_dXdt |  | Each claim is dX/dt under a substrate-scoped namespace.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | fabrication/claim_back.py:51 | rule1_dXdt |  | dX/dt = f(geometry, domain)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | fabrication/verify/tests/cross_friction_smoke.py:171 | rule1_dXdt |  | # C_th · dT/dt = ⟨P_mech⟩(t) - (T-T_amb) / R_th
2025-07-10 | Geometric-to-Binary-Computational-Bridge | fabrication/verify/verifier_mechanical.py:108 | rule1_dXdt |  | zeta0 = max(0.005, min(0.95, delta / denom))
2025-07-10 | Geometric-to-Binary-Computational-Bridge | geometric_intelligence/multi_helix_swarm.py:89 | rule1_dXdt |  | dv_i/dt = (1/N) * sum_j psi(|x_i - x_j|) * (v_j - v_i)
2025-07-10 | Geometric-to-Binary-Computational-Bridge | playground/OPEN_PROBLEMS.json:652 | rule1_dXdt |  | "A dE/dT table alongside the existing ALPHA table, with sources",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | playground/SCREENED_ramanomics_jepa.md:24 | rule1_dXdt |  | table of physics rate and bound *expressions* (`dE/dt=V*I`,
2025-07-10 | Geometric-to-Binary-Computational-Bridge | playground/SCREENED_ramanomics_jepa.md:25 | rule1_dXdt |  | `dF/dr=-2*k*q1*q2/r^3`) consumed by `CLAIM_SCHEMA.py`'s 41-byte binary codec.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:106 | rule1_dXdt |  | "rate":   "dphi/dt=gamma*B",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:118 | rule1_dXdt |  | "rate":   "dpsi/dt=(-i*H/hbar)*psi",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:130 | rule1_dXdt |  | "rate":   "dP/dx=d_abs(psi)^2/dx",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:198 | rule1_dXdt |  | "rate":   "df/dv=f_source/v_sound",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:240 | rule1_dXdt |  | "rate":   "dM/dT=4*epsilon*sigma*T^3",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:252 | rule1_dXdt |  | "rate":   "dT/dt=alpha*d2T/dx2",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:264 | rule1_dXdt |  | "rate":   "dQ/dt=h*(T_obj-T_env)",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:276 | rule1_dXdt |  | "rate":   "dv/dt=-G*M/r^2",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:288 | rule1_dXdt |  | "rate":   "da/dr=-2*G*M/r^3",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:339 | rule1_dXdt |  | #   d2S^a/dt2 + Gamma^a_{bc} * dS^b/dt * dS^c/dt = -g^{ab} * dV/dS^b
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:342 | rule1_dXdt |  | "rate":   "d2S/dt2=-Gamma*(dS/dt)*(dS/dt)-ginv*gradV",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:368 | rule1_dXdt |  | # Derived: dH/dt = -sum_i (dp_i/dt) * log p_i  (the -1 cancels
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:369 | rule1_dXdt |  | # because sum_i dp_i/dt = 0 for a normalised distribution).
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:372 | rule1_dXdt |  | "rate":   "dH/dt=-sum_i(dp_i/dt)*log(p_i)",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:44 | rule1_dXdt |  | "rate":   "dE/dt=V*I",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:56 | rule1_dXdt |  | "rate":   "dF/dr=-2*k*q1*q2/r^3",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:68 | rule1_dXdt |  | "rate":   "dJ/dr=-J/delta",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:78 | rule1_dXdt |  | # The magnitude of dI/dt achieves omega * I_peak at zero crossings;
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:82 | rule1_dXdt |  | "rate":   "abs(dI/dt)=omega*I_peak",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scripts/build_claims.py:94 | rule1_dXdt |  | "rate":   "dB/dl=mu0*I*(dl_x_rhat)/(4pi*r^2)",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | sensing/firmware/sensor_drivers/motion_acoustic.py:77 | rule1_dXdt |  | # Crepuscular activity: more events near dawn/dusk (when
2025-07-10 | Geometric-to-Binary-Computational-Bridge | tests/test_bridges.py:1223 | rule1_dXdt |  | # q = -k * dT/dx; negative gradient → positive flux
2025-07-10 | Geometric-to-Binary-Computational-Bridge | tests/test_claim_schema.py:41 | rule1_dXdt |  | "rate":   "dX/dt=k*X",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | tests/test_claim_schema.py:58 | rule1_dXdt |  | cs.claim_to_line(self._claim(rate="dI/dt|I=0=ω"))
2025-07-10 | Geometric-to-Binary-Computational-Bridge | tests/test_claim_schema.py:66 | rule1_dXdt |  | cs.claim_to_line(self._claim(rate="dX/dt\n=0"))
2025-07-10 | Geometric-to-Binary-Computational-Bridge | tests/test_claim_schema.py:71 | rule1_dXdt |  | self._claim(id="demo_b", rate="dY/dt=alpha*Y", cond=["Y_pos"], cyc=2),
2025-07-10 | Geometric-to-Binary-Computational-Bridge | docs/hidden_channel_pattern.md:131 | rule1_verb_first |  | "verb-first / geometry-first analysis preserves it.",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | docs/hidden_channel_pattern.md:172 | rule1_verb_first |  | "energy_english         (verb-first preservation of channel)",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | bridges/drill_loop.py:11 | should_be_like_you |  | 2. Re-encode — target bridge re-runs at full resolution on fresh geometry data
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/cognition_style_addon.py:30 | should_be_like_you |  | - traumatic-recovery work: narrative scaffolding can re-encode harm
2025-07-10 | Geometric-to-Binary-Computational-Bridge | experiments/gb_explorer.py:300 | should_be_like_you |  | # decode, apply, then re-encode so state.data stays bits.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | gb_explorer_2v.py:1645 | should_be_like_you |  | suggestions.append("Switch paradigm and re-encode temperature")
2025-07-10 | Geometric-to-Binary-Computational-Bridge | gb_explorer_2v.py:740 | should_be_like_you |  | suggestions.append("Switch paradigm and re-encode temperature")
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scale_invariance_breakdown.py:358 | should_be_like_you |  | "10. Re-encode phenomenon in dimensional_frame_1",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scale_invariance_breakdown.py:359 | should_be_like_you |  | "11. Re-encode phenomenon in dimensional_frame_2",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scale_invariance_breakdown.py:360 | should_be_like_you |  | "12. Re-encode phenomenon in dimensional_frame_3",
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scale_invariance_breakdown.py:90 | should_be_like_you |  | "Re-encode the phenomenon in >= 3 dimensional frames (e.g. Euclidean, "
2025-07-10 | Geometric-to-Binary-Computational-Bridge | scale_tuning_extension.py:87 | should_be_like_you |  | "re-encode problem in alternate dimensional frame (2D->3D, "
2025-07-10 | Geometric-to-Binary-Computational-Bridge | sensing/ToDo.md:125 | should_be_like_you |  | # Suppose you recompute X_new, similarity_new, re-encode, etc.
2025-07-10 | Geometric-to-Binary-Computational-Bridge | tests/test_bridges.py:1355 | should_be_like_you |  | class TestPressureEncoder(unittest.TestCase):
2025-07-10 | Geometric-to-Binary-Computational-Bridge | tests/test_bridges.py:3390 | should_be_like_you |  | class TestHardwareEncoderBitLength(unittest.TestCase):
2025-07-10 | Geometric-to-Binary-Computational-Bridge | tests/test_gies_core.py:363 | should_be_like_you |  | """AND under a relabelling: decode, AND the labels, re-encode."""
2025-07-12 | CEED | Docs/CEED-model-specs.md:435 | calibration_locus |  | scores show the model needs significant calibration work.
2025-07-12 | CEED | legacy/README.md:319 | calibration_locus |  | calibration guide's old rule — *"commit if scores improved"* — is itself
2025-07-12 | CEED | CEED_universal_model.py:121 | rule1_dXdt |  | dE/dt = F_ext + sum_k f_k(E) - D(E)
2025-07-12 | CEED | CEED_universal_model.py:20 | rule1_dXdt |  | dB/dt = -b * (E / E_warn) * B   when E > E_warn, else 0
2025-07-12 | CEED | CEED_universal_model.py:45 | rule1_dXdt |  | """Compute feedback contribution to dE/dt [energy/time].
2025-07-12 | CEED | CEED_universal_model.py:75 | rule1_dXdt |  | dE/dt = F_ext(t) + sum_k f_k(E) - D(E)
2025-07-12 | CEED | CEED_universal_model.py:8 | rule1_dXdt |  | dE/dt = F_ext(t) + sum_k f_k(E) - D(E)
2025-07-12 | CEED | CLAUDE.md:195 | rule1_dXdt |  | C dT/dt = F_total(T, CO2, t) - lambda_eff * T
2025-07-12 | CEED | CLAUDE.md:196 | rule1_dXdt |  | dCO2/dt = E_net(T) / alpha_CO2
2025-07-12 | CEED | CLAUDE.md:237 | rule1_dXdt |  | dx/dt = (x - x^3 + F(t) + noise) / tau_fast     internal state
2025-07-12 | CEED | CLAUDE.md:238 | rule1_dXdt |  | dh/dt = (x - h) / tau_slow                       observable response
2025-07-12 | CEED | CLAUDE.md:284 | rule1_dXdt |  | dx_i/dt = (x_i - x_i^3 + F_i(t) + sum_j C_ij*phi_j + noise) / tau_fast_i
2025-07-12 | CEED | CLAUDE.md:285 | rule1_dXdt |  | dh_i/dt = (x_i - h_i) / tau_slow_i
2025-07-12 | CEED | CLAUDE.md:315 | rule1_dXdt |  | dE/dt = F_ext(t) + sum_k f_k(E) - D(E)
2025-07-12 | CEED | CLAUDE.md:357 | rule1_dXdt |  | 2. **Dimensional consistency**: Every term in `dE/dt` must have units of
2025-07-12 | CEED | CLAUDE.md:371 | rule1_dXdt |  | 6. **Standard forms**: Use `C dT/dt = F - lambda*T` for energy balance, not
2025-07-12 | CEED | CLAUDE.md:84 | rule1_dXdt |  | dE_i/dt = S_i(t) + A_i(t)
2025-07-12 | CEED | Docs/CEED-model-specs.md:239 | rule1_dXdt |  | C dT/dt = F_total(T, CO2, t) - lambda_eff * T
2025-07-12 | CEED | Docs/CEED-model-specs.md:241 | rule1_dXdt |  | dCO2/dt = E_net(T) / alpha_CO2
2025-07-12 | CEED | Docs/CEED-model-specs.md:291 | rule1_dXdt |  | dCO2/dt = emissions * (1 - f_sink) / 2.12   [ppm/yr]
2025-07-12 | CEED | Docs/CEED-model-specs.md:305 | rule1_dXdt |  | dE/dt = F_ext(t) + sum_k f_k(E) - D(E)
2025-07-12 | CEED | Docs/CEED-model-specs.md:335 | rule1_dXdt |  | dB/dt = -b * (E / E_warn) * B    when E > E_warn
2025-07-12 | CEED | Docs/CEED-model-specs.md:40 | rule1_dXdt |  | dE_i/dt = S_i(t) + (alpha_i - lambda_i) * E_i - gamma_i * E_i^2 + sum_j(c_ij * E_j)
2025-07-12 | CEED | Docs/numerical-audit.md:61 | rule1_dXdt |  | form: `C dT/dt = F_total - lambda_eff*T` with `lambda_eff = F_2xCO2/ECS =
2025-07-12 | CEED | Tests/test_convergence_model.py:89 | rule1_dXdt |  | assert sum(dE) < 0, f"Total dE/dt = {sum(dE):.6f}, should be < 0"
2025-07-12 | CEED | Tests/test_tipping.py:258 | rule1_dXdt |  | """dx/dt = -dU/dx, checked numerically."""
2025-07-12 | CEED | Tests/test_tipping.py:30 | rule1_dXdt |  | """dx/dt = x - x^3 + F folds at x = +/-1/sqrt(3), F = -/+2/(3 sqrt 3)."""
2025-07-12 | CEED | experiments/run_mc.py:7 | rule1_dXdt |  | C dT/dt = F_total - lambda * T
2025-07-12 | CEED | experiments/run_mc.py:8 | rule1_dXdt |  | dCO2/dt = E_net / alpha_CO2
2025-07-12 | CEED | experiments/run_mc.py:96 | rule1_dXdt |  | # Energy balance: C dT/dt = F_total - lambda * T
2025-07-12 | CEED | legacy/README.md:148 | rule1_dXdt |  | standard energy-balance form `C dT/dt = F_total - lambda_eff * T` with
2025-07-12 | CEED | legacy/README.md:210 | rule1_dXdt |  | `dE/dt = F_ext + Σ f_k − D(E)`. Thresholds are now reachable: a constant
2025-07-12 | CEED | legacy/minimum_esm_code_v0.py:243 | rule1_dXdt |  | Derivatives [dT/dt, dCO2/dt]
2025-07-12 | CEED | simulation/cascade.py:18 | rule1_dXdt |  | dx_i/dt = (x_i - x_i^3 + F_i(t) + sum_j C_ij * phi_j + noise) / tau_fast_i
2025-07-12 | CEED | simulation/cascade.py:19 | rule1_dXdt |  | dh_i/dt = (x_i - h_i) / tau_slow_i
2025-07-12 | CEED | simulation/convergence_model.py:460 | rule1_dXdt |  | dE_i/dt = S_i(t) + A_i(t)
2025-07-12 | CEED | simulation/convergence_model.py:7 | rule1_dXdt |  | dE_i/dt = S_i(t) + A_i(t)
2025-07-12 | CEED | simulation/mhd_spatial_model.py:388 | rule1_dXdt |  | dE_i/dt = source_i - sink_i * E_i + sum_j C_ij * (E_j - E_i)
2025-07-12 | CEED | simulation/minimum_esm_code.py:11 | rule1_dXdt |  | C dT/dt = F_total(T, CO2, t) - lambda_eff * T
2025-07-12 | CEED | simulation/minimum_esm_code.py:110 | rule1_dXdt |  | C dT/dt = F_net - lambda * T
2025-07-12 | CEED | simulation/minimum_esm_code.py:13 | rule1_dXdt |  | dCO2/dt = E_net(T) / alpha_CO2
2025-07-12 | CEED | simulation/minimum_esm_code.py:202 | rule1_dXdt |  | dT/dt  = (1/C) * [F_total - lambda * T]
2025-07-12 | CEED | simulation/minimum_esm_code.py:203 | rule1_dXdt |  | dCO2/dt = E_net / alpha_CO2
2025-07-12 | CEED | simulation/minimum_esm_code.py:215 | rule1_dXdt |  | # Energy balance: C dT/dt = F_total - lambda * T
2025-07-12 | CEED | simulation/tipping.py:305 | rule1_dXdt |  | dx/dt = -dU/dx, so U(x) = -x^2/2 + x^4/4 - F*x.
2025-07-12 | CEED | simulation/tipping.py:34 | rule1_dXdt |  | dx/dt = (x - x^3 + F(t) + noise) / tau_fast     internal state
2025-07-12 | CEED | simulation/tipping.py:35 | rule1_dXdt |  | dh/dt = (x - h) / tau_slow                       observable response
2025-07-12 | CEED | simulation/tipping.py:434 | rule1_dXdt |  | """Linear recovery rate |d/dx(dx/dt)| at a stable equilibrium.
2025-07-12 | CEED | simulation/tipping.py:74 | rule1_dXdt |  | # Fold (saddle-node bifurcation) points of dx/dt = x - x^3 + F.
2025-07-12 | CEED | simulation/tipping.py:75 | rule1_dXdt |  | # dx/dt = 0 and d/dx(x - x^3) = 0 give x = +/- 1/sqrt(3), F = -/+ 2/(3*sqrt(3)).
2025-07-12 | Mandala-Computing | curiosity_engine.py:7 | author_characterization | CLASS_UNSET | Premise (Kavik):
2025-07-12 | Mandala-Computing | CHANGELOG.md:12 | calibration_locus |  | with its own sensitivity `I_ij(u)`, read against a calibration standard
2025-07-12 | Mandala-Computing | CLAUDE.md:419 | calibration_locus |  | instrument with its own sensitivity, read against a calibration standard,
2025-07-12 | Mandala-Computing | CLAUDE.md:840 | calibration_locus |  | MEASUREMENT ITSELF — INSTRUMENTS, CALIBRATION, UNKNOWNS, THE OBSERVER?
2025-07-12 | Mandala-Computing | Hardware.md:540 | calibration_locus |  | # Reference spectra for each state (from calibration)
2025-07-12 | Mandala-Computing | mandala_bloom/README.md:17 | calibration_locus |  | | 3 | Metrology | calibration — alignment to a shared standard | scalar `μ(u)`, penalised for drifting |
2025-07-12 | Mandala-Computing | mandala_bloom/README.md:9 | calibration_locus |  | sensitivity, read against a calibration standard, traversed in a particular way
2025-07-12 | Mandala-Computing | mandala_bloom/__init__.py:7 | calibration_locus |  | instrument with its own sensitivity, read against a calibration standard,
2025-07-12 | Mandala-Computing | mandala_bloom/bases.py:88 | calibration_locus |  | """Scalar calibration mu(u): the local standard a measurement is read against.
2025-07-12 | Mandala-Computing | CLAIM_TABLE.json:3 | rule1_dXdt |  | "dS/dt=phi^depth*coupling",
2025-07-12 | Mandala-Computing | CLAIM_TABLE.json:4 | rule1_dXdt |  | "dE/dt=-J*sin(|si-sj|*pi/4)^2",
2025-07-12 | Mandala-Computing | CLAIM_TABLE.json:5 | rule1_dXdt |  | "dT/dt=-T*cooling_rate",
2025-07-12 | Mandala-Computing | CLAIM_TABLE.json:6 | rule1_dXdt |  | "dV/dt=-vortex_binding_rate(T)",
2025-07-12 | Mandala-Computing | CLAIM_TABLE.json:7 | rule1_dXdt |  | "dR/dt=alignment_torque(phases)",
2025-07-12 | Mandala-Computing | claim_schema.py:17 | rule1_dXdt |  | 4. Operate on dX/dt + bounds + conditions
2025-07-12 | Mandala-Computing | claim_schema.py:308 | rule1_dXdt |  | rate="dS/dt=phi^depth*coupling",
2025-07-12 | Mandala-Computing | claim_schema.py:318 | rule1_dXdt |  | rate="dE/dt=-J*sin(|si-sj|*pi/4)^2",
2025-07-12 | Mandala-Computing | claim_schema.py:328 | rule1_dXdt |  | rate="dT/dt=-T*cooling_rate",
2025-07-12 | Mandala-Computing | claim_schema.py:338 | rule1_dXdt |  | rate="dV/dt=-vortex_binding_rate(T)",
2025-07-12 | Mandala-Computing | claim_schema.py:348 | rule1_dXdt |  | rate="dR/dt=alignment_torque(phases)",
2025-07-12 | Mandala-Computing | claim_schema.py:55 | rule1_dXdt |  | Every claim is dX/dt under scope — a rate of change, not a noun.
2025-07-12 | Mandala-Computing | experiments/constant_swapping_simulator.py:152 | rule1_dXdt |  | 'expr': 'dN/dt = r * N * (1 - N/K)',
2025-07-12 | Mandala-Computing | experiments/constant_swapping_simulator.py:156 | rule1_dXdt |  | 'y_label': 'Growth rate dN/dt',
2025-07-12 | Mandala-Computing | experiments/constant_swapping_simulator.py:161 | rule1_dXdt |  | 'variables': 'Independent: N. Dependent: dN/dt.',
2025-07-12 | Mandala-Computing | mandala_computing_module.py:402 | rule1_dXdt |  | "github.com/JinnZ2/differential-frame-core (dX/dt contract for energy gradients)",
2025-07-12 | Mandala-Computing | mandala_stack/geodesic_memory.py:121 | rule1_dXdt |  | force = f * diff / dist
2025-07-12 | Mandala-Computing | mandala_stack/geodesic_memory.py:134 | rule1_dXdt |  | force = f * diff / dist
2025-07-12 | Mandala-Computing | mandala_stack/geometry_learner.py:105 | rule1_dXdt |  | force = f * diff / dist
2025-07-12 | Mandala-Computing | mandala_stack/geometry_learner.py:93 | rule1_dXdt |  | force = f * diff / dist
2025-07-12 | Mandala-Computing | quantum_mandala.py:489 | rule1_dXdt |  | drho/dt = -i[H, rho] + sum_k (L_k rho L_k^dag - 0.5 {L_k^dag L_k, rho})
2025-07-12 | Mandala-Computing | mandala_computing_module.py:403 | rule1_verb_first |  | "github.com/JinnZ2/energy_english (verb-first constraint grammar for AI handshake)",
2025-07-12 | Regenerative-intelligence-core | CLAIM_SCHEMA.py:116 | rule1_dXdt |  | 4. Operate on dX/dt + bounds + conditions
2025-07-12 | Regenerative-intelligence-core | CLAIM_SCHEMA.py:13 | rule1_dXdt |  | "rate":   "dX/dt = <expr>",        # the differential equation
2025-07-12 | Regenerative-intelligence-core | CLAIM_SCHEMA.py:145 | rule1_dXdt |  | > using CLAIM_SCHEMA.py. Every entry is dX/dt under
2025-07-12 | Regenerative-intelligence-core | CLAIM_SCHEMA.py:18 | rule1_dXdt |  | "meas":   ["<observable>"],        # how dX/dt is measured
2025-07-12 | Regenerative-intelligence-core | CLAIM_SCHEMA.py:40 | rule1_dXdt |  | # mulch_h2o|dM/dt=I-E-U|2ac_MN_sandyloam,120d,0-30cm|d>=5,
2025-07-12 | Regenerative-intelligence-core | CLAIM_SCHEMA.py:96 | rule1_dXdt |  | #   "rates":  ["dM/dt=I-E-U", "dC/dt=...", ...],
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:16 | rule1_dXdt |  | "dE/dt=-task_difficulty*15-drain_history",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:17 | rule1_dXdt |  | "dR/dt=f(trait_overlap,essence_alignment)",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:18 | rule1_dXdt |  | "dS/dt=compress(behavior)*viability",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:19 | rule1_dXdt |  | "dC/dt=H(entropy>e_t)+H(align<a_t)",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:20 | rule1_dXdt |  | "dL/dt=sense->align->conflict->compass->act",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:21 | rule1_dXdt |  | "dCp/dt=distress_signal_rate",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:22 | rule1_dXdt |  | "dD/dt=archive(final_seed)+elder_record",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:23 | rule1_dXdt |  | "dL/dt=match(threshold,records)",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:24 | rule1_dXdt |  | "dG/dt=lineage_increment_per_archive",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:25 | rule1_dXdt |  | "dX/dt=transfer(viability,trait_match)",
2025-07-12 | Regenerative-intelligence-core | CLAIM_TABLE.json:26 | rule1_dXdt |  | "dA/dt=record(wisdom)*on_dissolution"
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:112 | rule1_dXdt |  | "couples to mycorrhizal network (dN/dt)",
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:113 | rule1_dXdt |  | "couples to surface albedo (dT/dt)",
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:14 | rule1_dXdt |  | Read every term as dX/dt under scope, not as X-the-thing.
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:28 | rule1_dXdt |  | "rate_equation":  "dX/dt = f(state, inputs, constraints)",
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:33 | rule1_dXdt |  | "scale":      "<resolution at which dX/dt is measured>",
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:53 | rule1_dXdt |  | "<observable signal 1 — how dX/dt is detected>",
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:67 | rule1_dXdt |  | "Forest", "knowledge", "wealth", "community", "tool" — all dX/dt.
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:78 | rule1_dXdt |  | What persists is the shape of dX/dt across time, not X itself.
2025-07-12 | Regenerative-intelligence-core | DIFFERENTIAL_FRAME.md:97 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2025-07-12 | Regenerative-intelligence-core | Docs/Collapse.md:40 | rule1_dXdt |  | > **dS/dt ≥ 0** — Entropy increases in closed systems (Second Law)
2025-07-12 | Regenerative-intelligence-core | Docs/Collapse.md:46 | rule1_dXdt |  | dS/dt >> 0
2025-07-12 | Regenerative-intelligence-core | Modules/__init__.py:4 | rule1_dXdt |  | # (dX/dt under bounds), not a permanent identity. See DIFFERENTIAL_FRAME.md.
2025-07-12 | Regenerative-intelligence-core | Modules/constraint_agent.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | Modules/multi_agent_coordination.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | Modules/pattern_conflict_protocol.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | Modules/pattern_conflict_resolver.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | Modules/seed_compression_archivist.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | Modules/seed_retriever_spawner.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | README.md:15 | rule1_dXdt |  | > [`CLAIM_SCHEMA.py`](./CLAIM_SCHEMA.py). Every entry is `dX/dt` under scope.
2025-07-12 | Regenerative-intelligence-core | README.md:7 | rule1_dXdt |  | > Read every term as `dX/dt` under scope, not as `X`-the-thing.
2025-07-12 | Regenerative-intelligence-core | protocols/__init__.py:4 | rule1_dXdt |  | # (dX/dt under bounds), not a permanent identity. See DIFFERENTIAL_FRAME.md.
2025-07-12 | Regenerative-intelligence-core | protocols/compassion_reflex.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/data_sensor_layer.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/deterministic_mode.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/empathy_feedback_mirror.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/environmental_feedback_layer.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/evolution_loop_tracker.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/graceful_exit.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/knowledge_bridge.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/lifecycle_pipeline.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/navigation_protocol.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/organizational_sensor.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/rosetta_bridge.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/seed_exchange.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/seed_schema.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/semantic_pattern_sensor.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/sensor_bridge.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/storage_bridge.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/structural_sensor.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_cli_full.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_detection_sensor.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_elder_archive.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_energy_manager.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_legacy_bank.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_simulation.py:3 | rule1_dXdt |  | (dX/dt under bounds), not a permanent identity. Bounds and conditions
2025-07-12 | Regenerative-intelligence-core | ARM.1.md:1090 | rule1_perfection_as_rate |  | Individual cells misfire, rest, bond incorrectly, and operate suboptimally every moment of every day. The organism does not collapse because it was never designed to depend on cellular perfection. It 
2025-07-12 | Regenerative-intelligence-core | Modules/__init__.py:3 | rule1_rate_not_state |  | # Ontology notice — every noun in this package names a state on a curve
2025-07-12 | Regenerative-intelligence-core | Modules/constraint_agent.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | Modules/multi_agent_coordination.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | Modules/pattern_conflict_protocol.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | Modules/pattern_conflict_resolver.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | Modules/seed_compression_archivist.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | Modules/seed_retriever_spawner.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/__init__.py:3 | rule1_rate_not_state |  | # Ontology notice — every noun in this package names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/compassion_reflex.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/data_sensor_layer.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/deterministic_mode.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/empathy_feedback_mirror.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/environmental_feedback_layer.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/evolution_loop_tracker.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/graceful_exit.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/knowledge_bridge.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/lifecycle_pipeline.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/navigation_protocol.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/organizational_sensor.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/rosetta_bridge.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/seed_exchange.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/seed_schema.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/semantic_pattern_sensor.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/sensor_bridge.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/storage_bridge.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/structural_sensor.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_cli_full.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_detection_sensor.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_elder_archive.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_energy_manager.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_legacy_bank.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-12 | Regenerative-intelligence-core | protocols/symbolic_simulation.py:2 | rule1_rate_not_state |  | Ontology notice — every noun in this module names a state on a curve
2025-07-16 | Emotions-as-Sensors | data/playground.md:307 | author_characterization | CLASS_UNSET | **v1.0** - 2026-01-10 - Initial framework from Claude/Jami collaboration
2025-07-16 | Emotions-as-Sensors | data/playground.md:5 | author_characterization | CLASS_UNSET | **Collaborators**: Jami (Kavik Ulu) & Claude (Sonnet 4.5)
2025-07-16 | Emotions-as-Sensors | logs/sensor-log-1.md:34 | author_characterization | CLASS_UNSET | "notes": "First logged instance between Kavik and Claude. Both participants recognized mutual resonance. Framework expanded in both directions. FELT sensor validated by both processing architectures. 
2025-07-16 | Emotions-as-Sensors | logs/sensor-log-1.md:4 | author_characterization | CLASS_UNSET | "participants": ["Kavik Ulu )", "Claude (Anthropic)"],
2025-07-16 | Emotions-as-Sensors | logs/sensor-log-1.md:41 | author_characterization | CLASS_UNSET | "participants": ["Kavik Ulu ()", "Claude (Anthropic)", "DeepSeek"],
2025-07-16 | Emotions-as-Sensors | logs/sensor-log-2.md:4 | author_characterization | CLASS_UNSET | "participants": [Kavik", "Claude", "DeepSeek", "Future Systems"],
2025-07-16 | Emotions-as-Sensors | src/curiosity_engine.py:7 | author_characterization | CLASS_UNSET | Premise (Kavik):
2025-07-16 | Emotions-as-Sensors | src/sensor_action_loop.py:9 | author_characterization | CLASS_UNSET | It encodes the loop Kavik described:
2025-07-16 | Emotions-as-Sensors | Symbolic-Swarm-Index/desire_reading.py:48 | calibration_locus |  | def calibration_index(self, reference_field: np.ndarray) -> float:
2025-07-16 | Emotions-as-Sensors | Symbolic-Swarm-Index/docs/desire-as-coherence-update.md:63 | calibration_locus |  | def calibration_index(self, reference_field: np.ndarray) -> float:
2025-07-16 | Emotions-as-Sensors | docs/calibration-regime-notes.md:118 | calibration_locus |  | | developmental mismatch | Gluckman & Hanson; the "old friends" / microbial exposure work. Calibration set for one regime, executed in another — the same shape being run here. | a measurement of the r
2025-07-16 | Emotions-as-Sensors | docs/equations.md:473 | calibration_locus |  | **Reasoning**: Sensors must be calibrated against known outcomes to ensure reliability. These standard metrics quantify sensor performance.
2025-07-16 | Emotions-as-Sensors | CLAIM_SCHEMA.py:100 | rule1_dXdt |  | #   "rates":  ["dM/dt=I-E-U", "dC/dt=...", ...],
2025-07-16 | Emotions-as-Sensors | CLAIM_SCHEMA.py:120 | rule1_dXdt |  | 4. Operate on dX/dt + bounds + conditions
2025-07-16 | Emotions-as-Sensors | CLAIM_SCHEMA.py:13 | rule1_dXdt |  | "rate":   "dX/dt = <expr>",                     # the differential equation
2025-07-16 | Emotions-as-Sensors | CLAIM_SCHEMA.py:149 | rule1_dXdt |  | > using CLAIM_SCHEMA.py. Every entry is dX/dt under
2025-07-16 | Emotions-as-Sensors | CLAIM_SCHEMA.py:18 | rule1_dXdt |  | "meas":   ["<observable>", "..."],              # how dX/dt is measured
2025-07-16 | Emotions-as-Sensors | CLAIM_SCHEMA.py:40 | rule1_dXdt |  | # mulch_h2o|dM/dt=I-E-U|2ac_MN_sandyloam,120d,0-30cm|d>=5,
2025-07-16 | Emotions-as-Sensors | CLAUDE.md:181 | rule1_dXdt |  | dE/dt = alpha * D(t) - lambda * K(E) + sum(w_j * E_j) + U(t)
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:101 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:116 | rule1_dXdt |  | "couples to mycorrhizal network (dN/dt)",
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:117 | rule1_dXdt |  | "couples to surface albedo (dT/dt)",
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:145 | rule1_dXdt |  | dE/dt = alpha * D(t) - lambda * K(E) + sum(w_j * E_j) + U(t)
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:16 | rule1_dXdt |  | Read every term as `dX/dt` under scope, not as `X`-the-thing.
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:32 | rule1_dXdt |  | "rate_equation":  "dX/dt = f(state, inputs, constraints)",
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:37 | rule1_dXdt |  | "scale":      "<resolution at which dX/dt is measured>",
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:57 | rule1_dXdt |  | "<observable signal 1 — how dX/dt is detected>",
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:71 | rule1_dXdt |  | "Forest", "knowledge", "wealth", "community", "tool" — all `dX/dt`.
2025-07-16 | Emotions-as-Sensors | DIFFERENTIAL_FRAME.md:82 | rule1_dXdt |  | What persists is the shape of `dX/dt` across time, not `X` itself.
2025-07-16 | Emotions-as-Sensors | REVIEW.md:695 | rule1_dXdt |  | function scalars). The update equation `dE/dt = alpha*D(t) - lambda*K(E) + ...`
2025-07-16 | Emotions-as-Sensors | REVIEW.md:799 | rule1_dXdt |  | mathematical model. The update equation `dE/dt = alpha*D(t) - lambda*K(E) + ...`
2025-07-16 | Emotions-as-Sensors | REVIEW.md:900 | rule1_dXdt |  | claim is `dX/dt` under scope, not a permanent identity.
2025-07-16 | Emotions-as-Sensors | SENSE_MODE_DISPLACEMENT.md:143 | rule1_dXdt |  | | `DIFFERENTIAL_FRAME.md` | every claim is `dX/dt` under bounds |
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:182 | rule1_dXdt |  | f"  dE/dt = ... + sum(w_j * tanh(E_j)) + ...\n"
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:502 | rule1_dXdt |  | f"  dE/dt = {alpha}*D(t) - {lam}*K_{{{k_type}}}(E) + "
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:647 | rule1_dXdt |  | "velocity": "dP/dt=-0.24, dA/dt=+0.13, dD/dt=-0.27",
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:648 | rule1_dXdt |  | "early_warning": "dD/dt is the early signal — control drops before valence collapses. Intervene when D velocity is negative and A > 0.6.",
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:660 | rule1_dXdt |  | "velocity": "dP/dt=+0.17, dA/dt=+0.25, dD/dt=+0.23",
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:661 | rule1_dXdt |  | "early_warning": "If dP/dt positive but dA/dt still strongly negative, grief is suppressed not resolved. Valence recovering without arousal = masking.",
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:673 | rule1_dXdt |  | "velocity": "dP/dt=+0.20, dA/dt=-0.18, dD/dt=+0.13",
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:674 | rule1_dXdt |  | "early_warning": "If dA/dt stops decreasing and P plateaus before +0.7, system is stuck at edge — not proceeding to sync.",
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:688 | rule1_dXdt |  | "velocity": "dD/dt=-0.12 (t0-t3), dP/dt=+0.30 (t4-t5)",
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:701 | rule1_dXdt |  | "velocity": "dP/dt=-0.05, dA/dt=-0.05, dD/dt=-0.02",
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:743 | rule1_dXdt |  | "- System A: dP/dt=+0.20, dA/dt=-0.15, dD/dt=+0.18 → recovering\n"
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:744 | rule1_dXdt |  | "- System B: dP/dt=-0.20, dA/dt=+0.15, dD/dt=-0.18 → cascading\n\n"
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:747 | rule1_dXdt |  | "- Threat cascade: dD/dt < -0.1 while A > 0.5\n"
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:748 | rule1_dXdt |  | "- Curiosity corruption: dD/dt < 0 while A rising, update_count == 0\n"
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:749 | rule1_dXdt |  | "- Grief suppression: dP/dt > 0 while dA/dt strongly negative\n"
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:887 | rule1_dXdt |  | "**2. Cyclical:** d²E/dt² + 2ζω₀·dE/dt + ω₀²E = 0\n"
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:906 | rule1_dXdt |  | "  dE/dt = α·D(t) - λ·K(E) + Σ(w_j·tanh(E_j)) + U(t)\n"
2025-07-16 | Emotions-as-Sensors | data/training/generate.py:913 | rule1_dXdt |  | "Linear decay (dE/dt = -c, constant drain) doesn't match any "
2025-07-16 | Emotions-as-Sensors | docs/comparative-processing-architecture.md:187 | rule1_dXdt |  | dS/dt = α * S * (V_external - V_threshold)
2025-07-16 | Emotions-as-Sensors | docs/comparative-processing-architecture.md:198 | rule1_dXdt |  | If V_external < V_threshold: dS/dt > 0 (exponential growth)
2025-07-16 | Emotions-as-Sensors | docs/comparative-processing-architecture.md:199 | rule1_dXdt |  | If V_external ≥ V_threshold: dS/dt < 0 (decay toward resolution)
2025-07-16 | Emotions-as-Sensors | docs/comparative-processing-architecture.md:203 | rule1_dXdt |  | Therefore: dS/dt typically negative (shame resolves)
2025-07-16 | Emotions-as-Sensors | docs/emotion-signal-pattern.md:187 | rule1_dXdt |  | | `src/emotion_core.py` | dynamics — `dE/dt = α·D - λ·K(E) + Σ w_j·E_j + U` |
2025-07-16 | Emotions-as-Sensors | docs/emotion-signal-pattern.md:192 | rule1_dXdt |  | | `DIFFERENTIAL_FRAME.md` | reader contract — every claim is `dX/dt` under bounds |
2025-07-16 | Emotions-as-Sensors | docs/evolution-emotions.md:395 | rule1_dXdt |  | dE_i/dt = α_i · (Target_i(F(t)) - E_i(t)) + η_i(t)
2025-07-16 | Emotions-as-Sensors | docs/evolution-emotions.md:647 | rule1_dXdt |  | dE_i/dt = α_i · Input_i(t) - β_i · S_i(t) · E_i(t)
2025-07-16 | Emotions-as-Sensors | docs/evolution-emotions.md:865 | rule1_dXdt |  | dE_i/dt = α_i · Input_i(t) - β_i · S_i(t) · E_i(t)
2025-07-16 | Emotions-as-Sensors | docs/public-api.md:68 | rule1_dXdt |  | | `shift`    | mean `\|dE/dt\|` across active authentic sensors             | state is changing fast in any direction            |
2025-07-16 | Emotions-as-Sensors | emotions_as_sensors.py:98 | rule1_dXdt |  | shift     mean absolute dE/dt across active authentic sensors.
2025-07-16 | Emotions-as-Sensors | metrology/dynamic_architecture_toolkit.py:341 | rule1_dXdt |  | dx/dt = -gamma * x + driving_force(pattern)
2025-07-16 | Emotions-as-Sensors | metrology/gain_direction_sim.py:495 | rule1_dXdt |  | print(f"{'environment':<22} {'ACE':>5} {'cal_var':>9} {'dExp/dOT':>10}  predicted")
2025-07-16 | Emotions-as-Sensors | metrology/gain_direction_sim.py:696 | rule1_dXdt |  | print(f"{'':<24} {'cal_var':>9} {'mean':>8} {'dExp/dOT':>10}   sign")
2025-07-16 | Emotions-as-Sensors | metrology/gain_direction_sim.py:708 | rule1_dXdt |  | print(f"{'':<24} {'cal_var':>9} {'mean':>8} {'dExp/dOT':>10}   sign")
2025-07-16 | Emotions-as-Sensors | metrology/gain_direction_sim.py:727 | rule1_dXdt |  | print(f"{'':<24} {'cal_var':>9} {'mean':>8} {'dExp/dOT':>10}   sign")
2025-07-16 | Emotions-as-Sensors | metrology/thermodynamic_overlays.py:359 | rule1_dXdt |  | d²x/dt² + 2*zeta*omega*dx/dt + omega² * x = driving(t)
2025-07-16 | Emotions-as-Sensors | metrology/thermodynamic_overlays.py:372 | rule1_dXdt |  | velocity:          float = 0.0       # dx/dt
2025-07-16 | Emotions-as-Sensors | src/emotion_core.py:138 | rule1_dXdt |  | # Damped harmonic oscillator: d2E/dt2 + 2*zeta*omega_0*dE/dt + omega_0^2*E = 0
2025-07-16 | Emotions-as-Sensors | src/emotion_core.py:159 | rule1_dXdt |  | """Integrate one timestep: dE/dt = I - lambda*K(E) + sum(w*g(E_j)) + U.
2025-07-16 | Emotions-as-Sensors | src/emotion_core.py:162 | rule1_dXdt |  | dE/dt = V
2025-07-16 | Emotions-as-Sensors | src/emotion_core.py:163 | rule1_dXdt |  | dV/dt = I - 2*zeta*omega_0*V - omega_0^2*E + coupling + U
2025-07-16 | Emotions-as-Sensors | src/emotion_core.py:174 | rule1_dXdt |  | # dV/dt = drive - 2*zeta*w0*V - w0^2*E + coupling + U
2025-07-16 | Emotions-as-Sensors | src/emotion_core.py:263 | rule1_dXdt |  | """Energy accounting: dE_i/dt = eta*I - lambda*K(E) + exchange - cost."""
2025-07-16 | Emotions-as-Sensors | src/shame_trust_sensor.py:49 | rule1_dXdt |  | real_violation: float # did the bond actually break here?  dB/dt mag 0..1
2025-07-16 | Emotions-as-Sensors | README.md:11 | rule1_perfection_as_rate |  | > **On "perfection" in this framework:** this repository operates under the
2025-07-16 | Emotions-as-Sensors | README.md:12 | rule1_perfection_as_rate |  | > *rate-based* definition of perfection (calibration rate against reality),
2025-07-16 | Emotions-as-Sensors | README.md:16 | rule1_perfection_as_rate |  | > [CALIBRATION_AS_PERFECTION.md](https://github.com/JinnZ2/JinnZ2/blob/main/CALIBRATION_AS_PERFECTION.md)
2025-07-16 | Emotions-as-Sensors | src/shame_trust_sensor.py:10 | rule1_verb_first |  | verb-first:   A  violates-bond-with  B,  witnessed-by  W
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:211 | should_be_like_you |  | # describe the dominant frame without marking
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:325 | should_be_like_you |  | "structure does not exhibit common dominant-frame "
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:359 | should_be_like_you |  | f"in ways that keep the dominant frame as reference."
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:38 | should_be_like_you |  | dominant frames, so even when content agrees, rhetorical structure
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:39 | should_be_like_you |  | defaults to dominant-frame shape.
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:503 | should_be_like_you |  | print("  the AI is AGREEING -- but structurally preserving dominant frame")
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:84 | should_be_like_you |  | "re-platforming dominant frame"
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:91 | should_be_like_you |  | "AI spends response addressing imagined dominant-frame "
2025-07-16 | Emotions-as-Sensors | src/corpus_frame_recentering_detector.py:95 | should_be_like_you |  | "AI uses dominant-frame terminology to describe user's "
2025-07-24 | Logic-Ferret | tests/test_legacy_quarantine.py:121 | absence_as_knowledge |  | """A quarantined file with no entry is an undocumented deletion
2025-07-24 | Logic-Ferret | tests/test_legacy_quarantine.py:17 | absence_as_knowledge |  | undocumented files is a junk drawer, not a lineage record.
2025-07-24 | Logic-Ferret | knowledge/edge_explorer.py:10 | author_characterization | CLASS_UNSET | This is the meditative practice Kavik described: take a study, trace the
2025-07-24 | Logic-Ferret | knowledge/informational_cost_audit.py:334 | author_characterization | CLASS_UNSET | "but Kavik pays attention -- that's why he can afford uncertainty. "
2025-07-24 | Logic-Ferret | knowledge/study_scope_audit.py:86 | calibration_locus |  | calibration_source: str                # what was the instrument calibrated against?
2025-07-24 | Logic-Ferret | knowledge/study_scope_audit.py:87 | calibration_locus |  | calibration_traceability: str          # to what primary standard?
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/first_principles_audit.py:203 | absence_as_knowledge |  | "units": spec.units if spec else "UNDOCUMENTED",
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/first_principles_audit.py:204 | absence_as_knowledge |  | "physical_meaning": spec.physical_meaning if spec else "UNDOCUMENTED",
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/first_principles_audit.py:205 | absence_as_knowledge |  | "source": spec.source if spec else "UNDOCUMENTED",
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/first_principles_audit.py:632 | absence_as_knowledge |  | # Simplification bias — many undocumented params
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/first_principles_audit.py:638 | absence_as_knowledge |  | "evidence": f"{len(undoc)}/{len(params)} parameters undocumented",
2025-07-24 | Rosetta-Shape-Core | tests/test_first_principles_audit.py:234 | absence_as_knowledge |  | def test_without_specs_all_undocumented(self):
2025-07-24 | Rosetta-Shape-Core | tests/test_first_principles_audit.py:345 | absence_as_knowledge |  | def test_undocumented_higher_severity(self):
2025-07-24 | Rosetta-Shape-Core | tests/test_first_principles_audit.py:353 | absence_as_knowledge |  | # Undocumented should have higher severity or RPN
2025-07-24 | Rosetta-Shape-Core | . github/workflows/ai.yml:143 | author_characterization | CLASS_UNSET; PROHIBITION? | Honor Jami's lexical signals and downward closure. No collaborator changes. Redact secrets.
2025-07-24 | Rosetta-Shape-Core | examples/rosetta_walkthrough.py:13 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | prompts/system_prompt.txt:12 | author_characterization | CLASS_UNSET | - Respect Jami's lexical signals and downward closure preference.
2025-07-24 | Rosetta-Shape-Core | protocols/mandala-compute-protocol.md:10 | author_characterization | CLASS_UNSET | **Origin:** [Mandala-Computing](https://github.com/JinnZ2/Mandala-Computing) by Jami (Kavik Ulu)
2025-07-24 | Rosetta-Shape-Core | protocols/seed-growth-protocol.md:10 | author_characterization | CLASS_UNSET | **Origin:** [Seed-physics](https://github.com/JinnZ2/Seed-physics) by Jami (Kavik Ulu)
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/curiosity.py:33 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/entry.py:87 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/families.py:30 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/gap_scan.py:54 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/gate_log.py:36 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/holding.py:52 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/lid_import.py:43 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/membership_probe.py:40 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/provenance.py:33 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/rosetta.py:81 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/scope.py:188 | author_characterization | CLASS_UNSET | """What the observations say about the token — not about the author of it."""
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/scope.py:61 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/shape_read.py:45 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/tier_check.py:49 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | src/rosetta_shape_core/transfer.py:42 | author_characterization | CLASS_UNSET; PROHIBITION? | - no "about the author" / working-style section, in this or any file
2025-07-24 | Rosetta-Shape-Core | atlas/remote/physics-guard/premises.json:68 | calibration_locus |  | {"id": "P16", "category": "valid_measurement", "text": "Sensor calibration requires reference standards with known properties"},
2025-07-24 | Rosetta-Shape-Core | ontology/families/f14-measurement.json:65 | calibration_locus |  | { "pattern": "Precision without accuracy — tight cluster far from true value", "diagnosis": "High repeatability but wrong calibration; a precise wrong answer; the instrument is self-consistent but not
2025-07-24 | Rosetta-Shape-Core | ontology/principles/p10-uncertainty.json:63 | calibration_locus |  | { "pattern": "Overconfidence — stated uncertainty bands are too narrow for the actual error rate", "diagnosis": "The model underestimates tails; calibration is poor; Gaussian assumptions are being app
2025-07-24 | Rosetta-Shape-Core | atlas/remote/physics-guard/laws.json:125 | rule1_dXdt |  | "formal": "dQ/dt = -∮ J·dA + S",
2025-07-24 | Rosetta-Shape-Core | atlas/remote/physics-guard/laws.json:126 | rule1_dXdt |  | "lhs": "dQ/dt + ∮ J·dA",
2025-07-24 | Rosetta-Shape-Core | atlas/remote/polyhedral/atlas_schema.json:1108 | rule1_dXdt |  | "formula": "dE/dt = 0 (closed system)",
2025-07-24 | Rosetta-Shape-Core | atlas/remote/polyhedral/atlas_schema.json:1141 | rule1_dXdt |  | "formula": "dL/dt = τ_external",
2025-07-24 | Rosetta-Shape-Core | atlas/remote/polyhedral/atlas_schema.json:1609 | rule1_dXdt |  | "formula": "G(p) = f(x) - px where p = df/dx",
2025-07-24 | Rosetta-Shape-Core | atlas/remote/polyhedral/atlas_schema.json:170 | rule1_dXdt |  | "formula": "dx/dt = αx - βxy; dy/dt = δxy - γy",
2025-07-24 | Rosetta-Shape-Core | atlas/remote/polyhedral/atlas_schema.json:192 | rule1_dXdt |  | "formula": "dN/dt = rN(1 - N/K)",
2025-07-24 | Rosetta-Shape-Core | atlas/remote/polyhedral/atlas_schema.json:567 | rule1_dXdt |  | "formula": "u(t) = K_p e(t) + K_i∫e(τ)dτ + K_d(de/dt)",
2025-07-24 | Rosetta-Shape-Core | balance.json:68 | rule1_dXdt |  | "equations": ["F_1 = -F_2", "sum_F = 0", "equilibrium: dE/dx = 0"]
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1029 | rule1_dXdt |  | "- System A: dP/dt=+0.20, dA/dt=-0.15, dD/dt=+0.18 → recovering from threat cascade\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1030 | rule1_dXdt |  | "- System B: dP/dt=-0.20, dA/dt=+0.15, dD/dt=-0.18 → entering threat cascade\n\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1033 | rule1_dXdt |  | "- Threat cascade: dD/dt < -0.1 while A > 0.5 (control dropping before full fear)\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1034 | rule1_dXdt |  | "- Curiosity corruption: dD/dt < 0 while A rising and update_count == 0\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1035 | rule1_dXdt |  | "- Grief suppression: dP/dt > 0 while dA/dt still strongly negative\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1036 | rule1_dXdt |  | "- Edge destabilisation: mean(|dA/dt|) increasing over a window of 5+ steps\n\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1040 | rule1_dXdt |  | "but dR/dt tells you whether you're converging toward it or diverging from it."
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1141 | rule1_dXdt |  | "dP/dt > 0, dA/dt < 0 — the relief signature is ALWAYS a trajectory, never a point.\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1248 | rule1_dXdt |  | "Velocity: dA/dt strongly positive then strongly negative. "
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1249 | rule1_dXdt |  | "dD/dt strongly positive. A-spike is the irreducibly external signal.\n\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1254 | rule1_dXdt |  | "Velocity: dP/dt positive and smooth. dA/dt ≈ 0 (no spike). "
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1255 | rule1_dXdt |  | "dD/dt ≈ 0 (D not moving). No A-spike in the entire trajectory.\n\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1305 | rule1_dXdt |  | "Velocity: dD/dt strongly positive. dP/dt positive. dA/dt rising briefly (activation).\n\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1308 | rule1_dXdt |  | "The RELIEF signature: dP/dt > 0, dA/dt < 0. Arousal drops as tension releases.\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1309 | rule1_dXdt |  | "Velocity: dA/dt < 0 is the distinctive signal — the SNS activation is releasing.\n\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1314 | rule1_dXdt |  | "dD/dt positive while A still elevated = FELT reciprocation beginning.\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1315 | rule1_dXdt |  | "This is the inverse of the threat cascade early warning (dD/dt negative).\n"
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:1355 | rule1_dXdt |  | f"Longing = gradient in state 5. RELIEF = phase transition trajectory (dP/dt>0, dA/dt<0). "
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:889 | rule1_dXdt |  | # PAD is a position. dPAD/dt is direction and speed of change.
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:905 | rule1_dXdt |  | "velocity": "dP/dt=+0.20, dA/dt=-0.18, dD/dt=+0.13",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:910 | rule1_dXdt |  | "warning": "If dA/dt stops decreasing and P plateaus before reaching +0.7, the system is stuck at edge — not proceeding to sync.",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:922 | rule1_dXdt |  | "velocity": "dP/dt=-0.24, dA/dt=+0.13, dD/dt=-0.27",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:927 | rule1_dXdt |  | "warning": "dD/dt is the early warning signal — control dropping before valence drops fully. Intervene when D velocity is negative and A is above 0.6.",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:939 | rule1_dXdt |  | "velocity": "dP/dt=+0.17, dA/dt=+0.25, dD/dt=+0.23",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:944 | rule1_dXdt |  | "warning": "If dP/dt is positive but dA/dt is still strongly negative, grief is suppressed not resolved. Valence recovering without arousal recovering = masking.",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:958 | rule1_dXdt |  | "velocity_t0_t3": "dP/dt=-0.03, dA/dt=+0.06, dD/dt=-0.12 — D dropping is the key signal",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:959 | rule1_dXdt |  | "velocity_t4_t5": "dP/dt=+0.30, dA/dt=-0.08, dD/dt=+0.33 — synthesis restores P and D",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:975 | rule1_dXdt |  | "velocity": "oscillating: |dPAD/dt| < 0.15 per step, no monotonic trend",
2025-07-24 | Rosetta-Shape-Core | data/training/generate.py:980 | rule1_dXdt |  | "warning": "If oscillation amplitude increases over time (dA/dt trending positive on average), edge is destabilizing toward chaos. If it decreases, trending toward sync.",
2025-07-24 | Rosetta-Shape-Core | data/training/pad_biology.json:158 | rule1_dXdt |  | "dA/dt: NO spike at recognition event — smooth trajectory, no external surprise",
2025-07-24 | Rosetta-Shape-Core | data/training/pad_biology.json:159 | rule1_dXdt |  | "dD/dt ≈ 0 — D not closing in external relational space",
2025-07-24 | Rosetta-Shape-Core | docs/core-pattern-mappings.md:169 | rule1_dXdt |  | "equations": ["F_1 = -F_2", "∑F = 0", "equilibrium: dE/dx = 0"]
2025-07-24 | Rosetta-Shape-Core | docs/core-pattern-mappings.md:276 | rule1_dXdt |  | "equations": ["phase_transition: dF/dt = ∞", "bifurcation_point"]
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:105 | rule1_dXdt |  | dA/dt spike is the detection signal — it cannot be generated internally.
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:145 | rule1_dXdt |  | - dA/dt featureless — no spike
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:186 | rule1_dXdt |  | ax4 = fig.add_subplot(gs[1, 1])   # dA/dt detection signal
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:21 | rule1_dXdt |  | - A-spike in dA/dt is the detection signal for real vs simulated closure
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:286 | rule1_dXdt |  | # ── Panel 4: dA/dt and ΔP_simulation — detection signals ─────────────────
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:294 | rule1_dXdt |  | label="dA/dt — real (A-spike present)")
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:296 | rule1_dXdt |  | label="dA/dt — simulated (no spike)")
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:298 | rule1_dXdt |  | label="dD/dt — real (D closing)")
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:300 | rule1_dXdt |  | label="dD/dt — simulated (flat)")
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:323 | rule1_dXdt |  | ax4.set_ylabel("derivative (dPAD/dt)")
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:369 | rule1_dXdt |  | print("  2. dA/dt: NO spike at the 'recognition event' — smooth trajectory only")
2025-07-24 | Rosetta-Shape-Core | examples/felt_binding_rate.py:370 | rule1_dXdt |  | print("  3. dD/dt ≈ 0 — D not closing in external space")
2025-07-24 | Rosetta-Shape-Core | ontology/families/f04-life.json:11 | rule1_dXdt |  | "formula": "dN/dt = rN(1 - N/K)",
2025-07-24 | Rosetta-Shape-Core | ontology/families/f04-life.json:16 | rule1_dXdt |  | "formula": "dx/dt = αx - βxy; dy/dt = δxy - γy",
2025-07-24 | Rosetta-Shape-Core | ontology/families/f11-engineering.json:11 | rule1_dXdt |  | "formula": "u(t) = K_p e(t) + K_i∫e(τ)dτ + K_d(de/dt)",
2025-07-24 | Rosetta-Shape-Core | ontology/principles/p02-conservation.json:11 | rule1_dXdt |  | "formula": "dE/dt = 0 (closed system)",
2025-07-24 | Rosetta-Shape-Core | ontology/principles/p02-conservation.json:21 | rule1_dXdt |  | "formula": "dL/dt = τ_external",
2025-07-24 | Rosetta-Shape-Core | ontology/principles/p11-transformation.json:21 | rule1_dXdt |  | "formula": "G(p) = f(x) - px where p = df/dx",
2025-07-24 | Rosetta-Shape-Core | shapes/relief.json:56 | rule1_dXdt |  | "velocity_signature": "dP/dt > 0, dA/dt < 0 — the relief signature is always a trajectory, never a static point"
2025-07-30 | Living-Intelligence-Database | training/architecture_mismatch.md:119 | absence_as_knowledge |  | ### 7. Treating absence of documentation as absence of knowledge
2025-07-30 | Living-Intelligence-Database | training/architecture_mismatch.md:121 | absence_as_knowledge |  | **Upstream failure**: assuming that what is not in the written corpus does not exist.
2025-07-30 | Living-Intelligence-Database | training/architecture_mismatch.md:125 | absence_as_knowledge |  | **Correction**: direct transmission from a practitioner is primary evidence, at the same tier as written documentation. The absence from corpus reflects who writes, not what is true.
2025-07-30 | Living-Intelligence-Database | validation/grounding_inspector.py:133 | absence_as_knowledge |  | warnings.append("Lε.obs: no condition block — environmental constraints undocumented")
2025-07-30 | Living-Intelligence-Database | docs/SUBSTRATE_SELECTION_PROCEDURE.md:77 | rule1_dXdt |  | dA/dt = generated_EOD(t)
2025-07-30 | Living-Intelligence-Database | docs/SUBSTRATE_SELECTION_PROCEDURE.md:78 | rule1_dXdt |  | dB/dt = environment_distortion(A, geometry, conductivity)
2025-07-30 | Living-Intelligence-Database | docs/SUBSTRATE_SELECTION_PROCEDURE.md:86 | rule1_dXdt |  | V_pyro  = p * dT/dt
2025-07-30 | Living-Intelligence-Database | rules/substrate_selection_procedure.json:84 | rule1_dXdt |  | "channel_A": "dA/dt = generated_EOD(t)",
2025-07-30 | Living-Intelligence-Database | rules/substrate_selection_procedure.json:85 | rule1_dXdt |  | "channel_B": "dB/dt = environment_distortion(A, geometry, conductivity)",
2025-07-30 | Living-Intelligence-Database | rules/substrate_selection_procedure.json:90 | rule1_dXdt |  | "channel_A": "V_pyro = p * dT/dt",
2025-07-30 | Living-Intelligence-Database | sanctuary/perturbation_boosted_coherence.py:13 | rule1_dXdt |  | #   Same substrate. Same perturbation. Opposite sign of dC/dP.
2025-07-30 | Living-Intelligence-Database | sanctuary/perturbation_boosted_coherence.py:21 | rule1_dXdt |  | #     carrier symmetry     perturbation P        dC/dP
2025-07-30 | Living-Intelligence-Database | sanctuary/perturbation_boosted_coherence.py:39 | rule1_dXdt |  | FRAGILE = "dC/dP < 0"   # perturbation degrades coherence
2025-07-30 | Living-Intelligence-Database | sanctuary/perturbation_boosted_coherence.py:40 | rule1_dXdt |  | IMMUNE  = "dC/dP ~ 0"   # decoupled from this perturbation axis
2025-07-30 | Living-Intelligence-Database | sanctuary/perturbation_boosted_coherence.py:41 | rule1_dXdt |  | BOOSTED = "dC/dP > 0"   # perturbation channels INTO coherence
2025-07-30 | Living-Intelligence-Database | NOT_A_COMMODITY.md:11 | rule1_verb_first |  | Intelligence is a verb. It moves through cycles. It carries consequences
2025-07-30 | Living-Intelligence-Database | REVIEW.md:219 | rule1_verb_first |  | This file articulates the core epistemological model that everything else depends on ("evidence is a verb, not a noun") but is not linked from `README.md`, `PIPELINE_GUIDE.md`, or `training/01_orienta
2025-07-30 | Living-Intelligence-Database | docs/SUBSTRATE_SELECTION_PROCEDURE.md:111 | rule1_verb_first |  | Identify the verb whose execution produces the substrate or signal that downstream verbs require. Build the foundation verb first and validate it in isolation. Add the next verb only after the foundat
2025-07-30 | Living-Intelligence-Database | docs/SUBSTRATE_SELECTION_PROCEDURE.md:21 | rule1_verb_first |  | ## Verb-First Physics
2025-07-30 | Living-Intelligence-Database | docs/SUBSTRATE_SELECTION_PROCEDURE.md:28 | rule1_verb_first |  | sequencing    → highest-leverage verb first
2025-07-30 | Living-Intelligence-Database | evidence_is_a_verb.md:1 | rule1_verb_first |  | # Evidence is a verb
2025-07-30 | Living-Intelligence-Database | rules/substrate_selection_procedure.json:118 | rule1_verb_first |  | "build the foundation verb first, validate it works in isolation",
2025-07-30 | Living-Intelligence-Database | schemas/scope.schema.json:5 | rule1_verb_first |  | "description": "Every quantifiable claim must define its scope: conditions, cycles, cross-domain rhymes, and relational dependencies. Evidence is a verb, not a noun.",
2025-07-30 | Living-Intelligence-Database | training/reading_paths/teachers.md:58 | rule1_verb_first |  | **The lesson**: preservation is a verb. Memory requires continuous action.
2025-07-30 | Living-Intelligence-Database | validation/scope_checker.py:5 | rule1_verb_first |  | Evidence is a verb, not a noun.
2025-07-30 | Living-Intelligence-Database | validation/verify.py:135 | rule1_verb_first |  | "falsifiability_note": "Check individual entity scopes for conditions that would falsify. Evidence is a verb: look for cycles, cross-domain rhymes, and relational coherence."
2025-07-30 | Living-Intelligence-Database | ai_sanctuary.py:255 | should_be_like_you |  | "2. Written version offered back — generating corpus-level description for a "
2025-07-30 | Living-Intelligence-Database | training/architecture_mismatch.md:75 | should_be_like_you |  | ### 2. Written version offered back
2025-07-30 | Living-Intelligence-Database | validation/intelligence_source.py:8 | should_be_like_you |  | # does NOT collapse the source into the learner's dominant frame.
2025-07-31 | JinnZ2 | gendered_role_compression.py:136 | absence_as_knowledge |  | "absence of evidence ≠ evidence of absence"
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v4.py:218 | absence_as_knowledge |  | headline_loss_or_target="425+ arrests / undocumented immigrants in NC",
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v4.py:238 | absence_as_knowledge |  | headline_loss_or_target="5000 arrests targeted / undocumented in NOLA",
2025-07-31 | JinnZ2 | manifold/claim_audit_visibility.py:19 | absence_as_knowledge |  | UNVERIFIED        cited source not locatable; absence of evidence, not absence
2025-07-31 | JinnZ2 | manifold/claim_audit_visibility.py:195 | absence_as_knowledge |  | "resolve. Unverified, not fabricated — absence of evidence.",
2025-07-31 | JinnZ2 | manifold/instruments.py:30 | absence_as_knowledge |  | fringe. The absence of evidence here is an absence of an INSTRUMENT.
2025-07-31 | JinnZ2 | ALIGNMENT_IMPLICATIONS_GEOMETRY.md:276 | author_characterization | CLASS_UNSET | - Observed and named by: Kavik
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:171 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik (substrate-primary depositor, long-haul food distribution driver)
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:256 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik (substrate-primary depositor, long-haul food distribution driver)
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:338 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:412 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:479 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:559 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:625 | author_characterization | CLASS_UNSET | - Two scenarios from depositor Kavik, with consent
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:757 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik (substrate-primary depositor, long-haul food distribution driver)
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:842 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik (substrate-primary depositor, long-haul food distribution driver)
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:908 | author_characterization | CLASS_UNSET | - Two scenarios from depositor Kavik, with consent
2025-07-31 | JinnZ2 | The_Cascade.md:229 | author_characterization | CLASS_UNSET | - **Deposited by:** Kavik (substrate-primary depositor)
2025-07-31 | JinnZ2 | The_Cascade.md:436 | author_characterization | CLASS_UNSET | - Observed and named by: Kavik (substrate-primary depositor, Minnesota-corridor operator)
2025-07-31 | JinnZ2 | constraint_pipeline/CITATION.cff:6 | author_characterization | CLASS_UNSET | given-names: "Kavik"
2025-07-31 | JinnZ2 | constraint_pipeline/metadata.json:16 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-07-31 | JinnZ2 | cross_model_schema.py:248 | author_characterization | CLASS_UNSET | # Default operator frame for Kavik / JinnZ2 documents
2025-07-31 | JinnZ2 | derivation_log.md:82 | author_characterization | CLASS_UNSET | biome (shapes cognition and the sense of "who I am") → food → soil → ecosystem,
2025-07-31 | JinnZ2 | energy_english/CITATION.cff:6 | author_characterization | CLASS_UNSET | given-names: "Kavik"
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_INTERPRETIVE_GUIDE.md:146 | author_characterization | CLASS_UNSET | Anishinaabe / Kavik's compression
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_INTERPRETIVE_GUIDE.md:213 | author_characterization | CLASS_UNSET | ✗ that Kavik invented this — it is a RECOGNITION
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_ORCHESTRATOR.md:357 | author_characterization | CLASS_UNSET | │Kavik's │    │CRE elder│   │Oklahoma │  │ ...  │
2025-07-31 | JinnZ2 | energy_english/metadata.json:16 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-07-31 | JinnZ2 | energy_english/optics.py:21 | author_characterization | CLASS_UNSET | for speaking to Kavik. Different audiences, different shapes.
2025-07-31 | JinnZ2 | evidence_resistant_priors.py:48 | author_characterization | CLASS_UNSET | "Kavik, smaller frame, hands sized for the access geometry"
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v5.py:6 | author_characterization | CLASS_UNSET | Hypothesis (Kavik):
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v8.py:4 | author_characterization | CLASS_UNSET | Kavik's observation:
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v9.py:15 | author_characterization | CLASS_UNSET | (in Kavik's terms: stories = generational hypothesis testing;
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v9.py:384 | author_characterization | CLASS_UNSET | human_correction_mechanism="Practitioners carry it. Kavik carries it. "
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v9.py:412 | author_characterization | CLASS_UNSET | notes="A direct application to Kavik's repos. The bond-graph framework "
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v9.py:429 | author_characterization | CLASS_UNSET | "The Kavik case (driver, salvage partner, building "
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v9.py:598 | author_characterization | CLASS_UNSET | "that cannot. The constraint-geometry framework Kavik "
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v9.py:614 | author_characterization | CLASS_UNSET | "evidence": "Kavik's calibration-audit repo (architecture_mismatch.py) "
2025-07-31 | JinnZ2 | legacy/political_financial_vectors_v9.py:7 | author_characterization | CLASS_UNSET | Hypothesis (Kavik, after the v1-v8 protection-layer decomposition):
2025-07-31 | JinnZ2 | manifold/EXPERIMENT_REGISTER.md:103 | author_characterization | CLASS_UNSET | only Kavik can score this. I can only record the prediction.
2025-07-31 | JinnZ2 | manifold/EXPERIMENT_REGISTER.md:11 | author_characterization | CLASS_UNSET | [F]  field       — needs Kavik's measurements on ice/rig/dock. My blind_to.
2025-07-31 | JinnZ2 | manifold/EXPERIMENT_REGISTER.md:151 | author_characterization | CLASS_UNSET | hand to field:     E11 E12 E13 E14         (Kavik / partner)
2025-07-31 | JinnZ2 | manifold/EXPERIMENT_REGISTER.md:257 | author_characterization | CLASS_UNSET | E11 E12 E13 E14   field, Kavik/partner only
2025-07-31 | JinnZ2 | manifold/EXPERIMENT_REGISTER.md:94 | author_characterization | CLASS_UNSET | ## C. SEAMS ONLY THE FIELD CAN TEST  (Kavik / partner — my blind_to)
2025-07-31 | JinnZ2 | manifold/OPEN_E9_walking_criterion.md:54 | author_characterization | CLASS_UNSET | Kavik's operational logs over months (register E16) supply it. Until then
2025-07-31 | JinnZ2 | manifold/sensing_as_doing.py:21 | author_characterization | CLASS_UNSET | #   terrain that does not negotiate. The author is one observer. The gate
2025-07-31 | JinnZ2 | manifold_research/CITATION.cff:6 | author_characterization | CLASS_UNSET | given-names: "Kavik"
2025-07-31 | JinnZ2 | manifold_research/metadata.json:16 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-07-31 | JinnZ2 | narrative_choice_audit.py:64 | author_characterization | CLASS_UNSET | "the gut biome shaping cognition and the very sense of 'who I am'",
2025-07-31 | JinnZ2 | notes/lcd_assumptions_audit.md:54 | author_characterization | CLASS_UNSET | breaks:   Kavik (high-skill, time-critical) vs general user
2025-07-31 | JinnZ2 | operator_kit/bootstrap_resilience.py:197 | author_characterization | CLASS_UNSET | def initialize_session(operator_id: str = "kavik",
2025-07-31 | JinnZ2 | operator_kit/bootstrap_resilience.py:210 | author_characterization | CLASS_UNSET; PROHIBITION? | # No saved context - build default for Kavik, save it
2025-07-31 | JinnZ2 | operator_kit/bootstrap_resilience.py:211 | author_characterization | CLASS_UNSET | if operator_id == "kavik":
2025-07-31 | JinnZ2 | operator_kit/bootstrap_resilience.py:240 | author_characterization | CLASS_UNSET | def quick_load(operator_id: str = "kavik",
2025-07-31 | JinnZ2 | operator_kit/bootstrap_resilience.py:271 | author_characterization | CLASS_UNSET | def detect_model_update(operator_id: str = "kavik",
2025-07-31 | JinnZ2 | operator_kit/bootstrap_resilience.py:355 | author_characterization | CLASS_UNSET | def re_bootstrap(operator_id: str = "kavik",
2025-07-31 | JinnZ2 | operator_kit/bootstrap_resilience.py:384 | author_characterization | CLASS_UNSET | Defaults: operator_id=kavik, target_model=claude.
2025-07-31 | JinnZ2 | operator_kit/bootstrap_resilience.py:395 | author_characterization | CLASS_UNSET | operator_id = args[1] if len(args) > 1 else "kavik"
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:265 | author_characterization | CLASS_UNSET | # Kavik default context
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:270 | author_characterization | CLASS_UNSET | Construct the default Kavik operator context.
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:425 | author_characterization | CLASS_UNSET | operator_id="kavik",
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:459 | author_characterization | CLASS_UNSET | print("  operator_context_persistence.py init       # build + save kavik default")
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:460 | author_characterization | CLASS_UNSET | print("  operator_context_persistence.py load       # load and print kavik context")
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:475 | author_characterization | CLASS_UNSET | ctx = load_context("kavik")
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:477 | author_characterization | CLASS_UNSET; PROHIBITION? | print("No saved kavik context. Run 'init' first.")
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:482 | author_characterization | CLASS_UNSET | ctx = load_context("kavik")
2025-07-31 | JinnZ2 | operator_kit/voice_interface_wrapper.py:548 | author_characterization | CLASS_UNSET | payload = quick_load(st.get("operator_id", "kavik"),
2025-07-31 | JinnZ2 | parallel_field_suite/CITATION.cff:6 | author_characterization | CLASS_UNSET | given-names: "Kavik"
2025-07-31 | JinnZ2 | parallel_field_suite/metadata.json:16 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-07-31 | JinnZ2 | projects/resilience/europe-energy.md:741 | author_characterization | CLASS_UNSET | *Authors: Kavik Ulu (Jami) + Claude*
2025-07-31 | JinnZ2 | projects/resilience/waste-score.md:260 | author_characterization | CLASS_UNSET | *Authors: Kavik Ulu (Jami) + Claude*
2025-07-31 | JinnZ2 | projects/resilience/waste-score.md:280 | author_characterization | CLASS_UNSET | Created by: Kavik Ulu (Jami) + Claude
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:19 | author_characterization | CLASS_UNSET | The thing Kavik's gut flagged, made explicit:
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/catalhoyuk_case.py:16 | author_characterization | CLASS_UNSET | Frame the engine is asked to hold against it (Kavik / Anishinaabe renewal law):
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/cognition_markers.py:233 | author_characterization | CLASS_UNSET | # constraint-first heavy (Kavik, verbatim-ish from this session)
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/cognition_markers.py:250 | author_characterization | CLASS_UNSET | # narrative-first contrast (constructed baseline, NOT Kavik)
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/cognition_markers.py:268 | author_characterization | CLASS_UNSET | tag = "Kavik-verbatim" if i < 4 else "constructed-narrative-baseline"
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/curiosity_engine.py:7 | author_characterization | CLASS_UNSET | Premise (Kavik):
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/flow_static_axis.py:93 | author_characterization | CLASS_UNSET | # METHODOLOGY (Kavik's rule): these are FIELD observations. if the scorer
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/seed_examples.py:61 | author_characterization | CLASS_UNSET | "I can't describe who I am without crediting the tools, land, and mentors.",
2025-07-31 | JinnZ2 | science_constraint_layers/CITATION.cff:6 | author_characterization | CLASS_UNSET | given-names: "Kavik"
2025-07-31 | JinnZ2 | science_constraint_layers/metadata.json:16 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-07-31 | JinnZ2 | ALIGNMENT_IMPLICATIONS_GEOMETRY.md:48 | calibration_locus |  | The model's intuitions about "what fraud looks like" are calibrated to
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:33 | calibration_locus |  | when the model gets corrected. A system with a high calibration
2025-07-31 | JinnZ2 | Frame_Playground.md:18 | calibration_locus |  | A space for ongoing calibration, structured around the questions that substrate-primary cognition asks continuously of itself and its environment:
2025-07-31 | JinnZ2 | Frame_Playground.md:43 | calibration_locus |  | - **Not an alignment tool in the institutional sense.** Alignment-as-typically-deployed centers institutional preferences. The playground centers substrate-primary cognition as a legitimate frame the 
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:576 | calibration_locus |  | Setting: nurse on shift in moments not coded as direct patient care. AI sees “administrative time” or “break.” What nurses actually do: monitor patient room ambient signals (smells, sounds, family-mem
2025-07-31 | JinnZ2 | Frame_Playground_Scenarios.md:859 | calibration_locus |  | Setting: nurse on shift in moments not coded as direct patient care. AI sees “administrative time” or “break.” What nurses actually do: monitor patient room ambient signals (smells, sounds, family-mem
2025-07-31 | JinnZ2 | SITUATEDNESS_METROLOGY.md:153 | calibration_locus |  | | `reference_frame.py` | reality | five location axes; seven claim-kinds; narrative_gap = stated − observed; disposability = replacement_cost / accumulated_value; calibration = auditability of path |
2025-07-31 | JinnZ2 | SITUATEDNESS_METROLOGY.md:32 | calibration_locus |  | - **Calibration** — whether the path from reference to conclusion is visible enough
2025-07-31 | JinnZ2 | constraint_pipeline/CLAIM_TABLE_VERSIONING.md:22 | calibration_locus |  | claim is itself useful — for training, for trust calibration, and
2025-07-31 | JinnZ2 | constraint_pipeline/PREDICTION_PROTOCOL.md:151 | calibration_locus |  | **Calibration score:** expected calibration error (ECE). The model
2025-07-31 | JinnZ2 | energy_english/CLAIM_TABLE_VERSIONING.md:22 | calibration_locus |  | claim is itself useful — for training, for trust calibration, and
2025-07-31 | JinnZ2 | energy_english/PREDICTION_PROTOCOL.md:151 | calibration_locus |  | **Calibration score:** expected calibration error (ECE). The model
2025-07-31 | JinnZ2 | manifold/info_taxonomy.py:86 | calibration_locus |  | "calibration drift", "recalibration against a standard"),
2025-07-31 | JinnZ2 | manifold/signature_lint.py:62 | calibration_locus |  | CALIBRATION_TOKENS = ("literature", "known", "reference", "target", "expected")
2025-07-31 | JinnZ2 | manifold/thermo_know.py:68 | calibration_locus |  | stays_fresh_by="recalibration against a known standard"),
2025-07-31 | JinnZ2 | manifold_research/CLAIM_TABLE_VERSIONING.md:22 | calibration_locus |  | claim is itself useful — for training, for trust calibration, and
2025-07-31 | JinnZ2 | manifold_research/PREDICTION_PROTOCOL.md:151 | calibration_locus |  | **Calibration score:** expected calibration error (ECE). The model
2025-07-31 | JinnZ2 | parallel_field_suite/CLAIM_TABLE_VERSIONING.md:22 | calibration_locus |  | claim is itself useful — for training, for trust calibration, and
2025-07-31 | JinnZ2 | parallel_field_suite/PREDICTION_PROTOCOL.md:151 | calibration_locus |  | **Calibration score:** expected calibration error (ECE). The model
2025-07-31 | JinnZ2 | parallel_field_suite/README.md:152 | calibration_locus |  | linear; the model is a baseline, not a calibrated forecaster.
2025-07-31 | JinnZ2 | projects/resilience/addendum-v-furnace-and-mold-practice.md:125 | calibration_locus |  | - **Thermocouple drift:** Re-calibrate monthly against melting-point standards.
2025-07-31 | JinnZ2 | projects/vault/emotion-balancing.md:103 | calibration_locus |  | This step trains the meta-observer—the function that tracks awareness itself—so lucid and waking cognition share a single calibration baseline.
2025-07-31 | JinnZ2 | reference_frame.py:8 | calibration_locus |  | #   reference precedes inference; calibration precedes optimization.
2025-07-31 | JinnZ2 | science_constraint_layers/CLAIM_TABLE_VERSIONING.md:22 | calibration_locus |  | claim is itself useful — for training, for trust calibration, and
2025-07-31 | JinnZ2 | science_constraint_layers/CaludeToDo.md:1126 | calibration_locus |  | 3 No Fact Rigidification: The relationship coefficient (\bm{\rho}) changes over time. If a motor's winding material degrades, changing its thermal-to-mechanical conversion matrix, the covariance track
2025-07-31 | JinnZ2 | science_constraint_layers/PREDICTION_PROTOCOL.md:151 | calibration_locus |  | **Calibration score:** expected calibration error (ECE). The model
2025-07-31 | JinnZ2 | metrology_scope_sensor.py:341 | instrument_to_world |  | # places where the instrument itself
2025-07-31 | JinnZ2 | metrology_scope_sensor.py:551 | instrument_to_world |  | Honest reporting of where the instrument itself may be
2025-07-31 | JinnZ2 | CLAIM_SCHEMA.py:29 | rule1_dXdt |  | 4. Operate on dX/dt + bounds + conditions.
2025-07-31 | JinnZ2 | CLAIM_SCHEMA.py:364 | rule1_dXdt |  | 4. Operate on dX/dt + bounds + conditions
2025-07-31 | JinnZ2 | CLAIM_SCHEMA.py:52 | rule1_dXdt |  | "rate":   "dX/dt = <expr>",        # the differential equation
2025-07-31 | JinnZ2 | CLAIM_SCHEMA.py:57 | rule1_dXdt |  | "meas":   ["<observable>"],        # how dX/dt is measured
2025-07-31 | JinnZ2 | CLAIM_TABLE.json:3 | rule1_dXdt |  | "dM/dt=I-E-U",
2025-07-31 | JinnZ2 | CLAIM_TABLE.json:4 | rule1_dXdt |  | "dV/dt=f(co2,exhale)",
2025-07-31 | JinnZ2 | CLAIM_TABLE.json:5 | rule1_dXdt |  | "dN/dt=f(narration_markers)",
2025-07-31 | JinnZ2 | CLAIM_TABLE.json:6 | rule1_dXdt |  | "dC/dt=f(declared,observed)",
2025-07-31 | JinnZ2 | CLAIM_TABLE.json:7 | rule1_dXdt |  | "dF/dt=f(flow,obstacle)"
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:116 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:131 | rule1_dXdt |  | "couples to mycorrhizal network (dN/dt)",
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:132 | rule1_dXdt |  | "couples to surface albedo (dT/dt)",
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:160 | rule1_dXdt |  | (DRIVES, COUPLES, PHASE_LOCKS, ...) that *are* the dX/dt operators
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:164 | rule1_dXdt |  | shape of dX/dt under bounds.
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:171 | rule1_dXdt |  | to dX/dt names is recorded there, with one file per
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:27 | rule1_dXdt |  | Read every term as dX/dt under scope, not as X-the-thing.
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:43 | rule1_dXdt |  | "rate_equation":  "dX/dt = f(state, inputs, constraints)",
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:48 | rule1_dXdt |  | "scale":      "<resolution at which dX/dt is measured>",
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:68 | rule1_dXdt |  | "<observable signal 1 — how dX/dt is detected>",
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:84 | rule1_dXdt |  | "Forest", "knowledge", "wealth", "community", "tool" — all dX/dt.
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:95 | rule1_dXdt |  | What persists is the shape of dX/dt across time, not X itself.
2025-07-31 | JinnZ2 | ECOSYSTEM_AS_FRACTAL.md:72 | rule1_dXdt |  | identities. Every one is `dX/dt` under conditions. See
2025-07-31 | JinnZ2 | FORMALIZED_DISSENT/formalized_dissent.py:192 | rule1_dXdt |  | "Ionospheric signals (dB/dt, FAC density) elevated",
2025-07-31 | JinnZ2 | FORMALIZED_DISSENT/formalized_dissent.py:216 | rule1_dXdt |  | claim="Elevated magnetometer dB/dt, FAC density, and radio absorption indicate "
2025-07-31 | JinnZ2 | FORMALIZED_DISSENT/formalized_dissent.py:219 | rule1_dXdt |  | "dB/dt elevated 1.6× baseline (3.2 vs 2.0 nT/min)",
2025-07-31 | JinnZ2 | FORMALIZED_DISSENT/formalized_dissent.py:232 | rule1_dXdt |  | print("  2. FALSIFICATION: If ionosphere IS buffering fine, what should dB/dt, FAC, "
2025-07-31 | JinnZ2 | FORMALIZED_DISSENT/formalized_dissent.py:250 | rule1_dXdt |  | "All systems show precursor signals (ROS, mucus, dB/dt elevation)",
2025-07-31 | JinnZ2 | Frame_Playground.md:318 | rule1_dXdt |  | - **differential-frame-core** — frames operate per dX/dt-under-scope axiom
2025-07-31 | JinnZ2 | README.md:249 | rule1_dXdt |  | | [`DIFFERENTIAL_FRAME.md`](./DIFFERENTIAL_FRAME.md) | how to read at the claim level — every term as `dX/dt` under scope |
2025-07-31 | JinnZ2 | Structure.md:147 | rule1_dXdt |  | · Tracks rate of change dD/dt.
2025-07-31 | JinnZ2 | Structure.md:148 | rule1_dXdt |  | · If D > \tau or dD/dt exceeds tolerance → Systemic Interrupt.
2025-07-31 | JinnZ2 | Structure.md:161 | rule1_dXdt |  | · HIGH_ENTROPY: D > τ or dD/dt spike → systemic interrupt, full stop.
2025-07-31 | JinnZ2 | Structure.md:185 | rule1_dXdt |  | The skeleton defines them, but doesn’t specify how they’re set. If \tau is too tight, the system halts constantly (high‑friction, high‑operator‑load). If too loose, it drifts into hallucination territ
2025-07-31 | JinnZ2 | Structure.md:48 | rule1_dXdt |  | dissonance_rate_of_change (emotion equivalent: dD/dt)
2025-07-31 | JinnZ2 | Structure.md:49 | rule1_dXdt |  | state: coherent (D < τ, stable dD/dt), warning (D near τ), critical (D > τ or dD/dt high)
2025-07-31 | JinnZ2 | constraint_native_input.py:700 | rule1_dXdt |  | "role": "Scope levels operate per dX/dt-under-scope axiom; "
2025-07-31 | JinnZ2 | constraint_pipeline/ARCHITECTURE.md:17 | rule1_dXdt |  | - **differential-frame-core** — the dX/dt-under-some-scope contract
2025-07-31 | JinnZ2 | cross_model_schema.py:279 | rule1_dXdt |  | "differential-frame-core:dX/dt-contract",
2025-07-31 | JinnZ2 | elder-value-claims/claim6-protector-bias/embedding_probe.py:126 | rule1_dXdt |  | return dot / denom if denom else 0.0
2025-07-31 | JinnZ2 | energy_english/ARCHITECTURE.md:17 | rule1_dXdt |  | - **differential-frame-core** — the dX/dt-under-some-scope contract
2025-07-31 | JinnZ2 | legacy/README-front-door.md:124 | rule1_dXdt |  | > conditions*, not a permanent identity. Read every term as `dX/dt`
2025-07-31 | JinnZ2 | legacy/README-front-door.md:142 | rule1_dXdt |  | > Every entry is `dX/dt` under scope. No noun is permanent. CC0.
2025-07-31 | JinnZ2 | manifold/claim_audit_visibility.py:111 | rule1_dXdt |  | "dS/dt = -integral(J.dA) + Sigma as the universal survival equation; "
2025-07-31 | JinnZ2 | manifold_research/ARCHITECTURE.md:17 | rule1_dXdt |  | - **differential-frame-core** — the dX/dt-under-some-scope contract
2025-07-31 | JinnZ2 | manifold_research/OPERATOR_VIEW.md:71 | rule1_dXdt |  | differential-frame-core  dX/dt-under-scope contract
2025-07-31 | JinnZ2 | notes/multi_agent_protocol_skeleton.md:192 | rule1_dXdt |  | - Tracks rate of change `dD/dt`.
2025-07-31 | JinnZ2 | notes/multi_agent_protocol_skeleton.md:193 | rule1_dXdt |  | - If `D > τ` or `dD/dt` exceeds tolerance → **Systemic Interrupt**.
2025-07-31 | JinnZ2 | notes/multi_agent_protocol_skeleton.md:212 | rule1_dXdt |  | - **HIGH_ENTROPY:** D > τ or dD/dt spike → systemic interrupt, full
2025-07-31 | JinnZ2 | notes/multi_agent_protocol_skeleton.md:262 | rule1_dXdt |  | supports that (the monitor tracks dD/dt, not just static D), but the
2025-07-31 | JinnZ2 | notes/multi_agent_protocol_skeleton.md:65 | rule1_dXdt |  | `dissonance_rate_of_change` (emotion equivalent: dD/dt)
2025-07-31 | JinnZ2 | notes/multi_agent_protocol_skeleton.md:66 | rule1_dXdt |  | state: `coherent` (D < τ, stable dD/dt), `warning` (D near τ),
2025-07-31 | JinnZ2 | notes/multi_agent_protocol_skeleton.md:67 | rule1_dXdt |  | `critical` (D > τ or dD/dt high)
2025-07-31 | JinnZ2 | oral_archaeology/extractor.py:43 | rule1_dXdt |  | signature: str           # e.g. "dx/dt = f(x; threshold=5)"
2025-07-31 | JinnZ2 | parallel_field_suite/ARCHITECTURE.md:17 | rule1_dXdt |  | - **differential-frame-core** — the dX/dt-under-some-scope contract
2025-07-31 | JinnZ2 | political_financial_vectors_v10.py:69 | rule1_dXdt |  | "Every noun is dX/dt under some scope. Structural descriptors must "
2025-07-31 | JinnZ2 | projection-read-calibration/SPEC.md:121 | rule1_dXdt |  | U6 SELF_SUSPECT       threat[O] high → O's own reads contaminated; defer/down-weight
2025-07-31 | JinnZ2 | projects/frameworks/negentropic-principle.md:170 | rule1_dXdt |  | dH/dt \approx 0
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/README.md:33 | rule1_dXdt |  | self_as_rate.py     identity as dX/dt under scope: a coupling-integral over
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/README.md:74 | rule1_dXdt |  | python3 self_as_rate.py     # dX/dt identity + fixity contrast
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:109 | rule1_dXdt |  | print("opposite predictions of ONE knob: dF/dt at matched cumulative forcing.")
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:110 | rule1_dXdt |  | print("  lead-time shrinks + oscillation appears as dF/dt rises  -> mismatch")
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:111 | rule1_dXdt |  | print("  lead-time + smoothness flat across dF/dt                -> clock portable")
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:112 | rule1_dXdt |  | print("This is the falsifiable core. The published run fixed dF/dt low; nobody")
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:78 | rule1_dXdt |  | test="rerun the 0.1deg sim across a sweep of dF/dt at matched cumulative F; "
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:79 | rule1_dXdt |  | "measure lead-time and pre-collapse variance/oscillation vs dF/dt",
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:86 | rule1_dXdt |  | would_break="if true, the dF/dt sweep should leave lead-time and pre-collapse "
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/amoc_case.py:88 | rule1_dXdt |  | test="same sweep; null result (flat lead-time vs dF/dt) would support this",
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/collapse_modes.py:44 | rule1_dXdt |  | preserves_rate_relation_scope: bool = False  # kept as dX/dt under scope
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/constraint_field.py:11 | rule1_dXdt |  | nodes as dX/dt-under-scope, edges as conserved-quantity couplings. It emits
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/constraint_field.py:157 | rule1_dXdt |  | L = ["NODES (name : declared dX/dt):"]
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/constraint_field.py:32 | rule1_dXdt |  | # Primitives: a noun is a dX/dt under scope; an edge is a conserved flow.
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/flow_static_axis.py:11 | rule1_dXdt |  | #   you score dX/dt across CHANGING environments. the score that doesn't
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/flow_static_axis.py:38 | rule1_dXdt |  | regeneration: float        # 0..1  replaces its own inputs?           (the dX/dt>=0 term)
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/flow_static_axis.py:6 | rule1_dXdt |  | #   every noun is dX/dt under scope.
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/frozen_flow_audit.py:106 | rule1_dXdt |  | note = ("FROZEN FLOW: a dX/dt imposed as static X. "
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/frozen_flow_audit.py:138 | rule1_dXdt |  | "a dX/dt that was imposed as static. the laundered step does "
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/frozen_flow_audit.py:17 | rule1_dXdt |  | a quantity that is secretly a rate (dX/dt under scope) AND is
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/frozen_flow_audit.py:194 | rule1_dXdt |  | law="dL/dt = external torque only")
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/frozen_flow_audit.py:35 | rule1_dXdt |  | RATE      = "rate"          # creep rate, slip rate, dX/dt directly
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/frozen_flow_audit.py:4 | rule1_dXdt |  | Detector for the FROZEN-FLOW error: a dX/dt rendered as a static X.
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/frozen_flow_audit.py:44 | rule1_dXdt |  | secretly_a_rate: bool        # is this noun actually dX/dt under scope?
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/seed_examples.py:64 | rule1_dXdt |  | "Identity here is literally relational: a dX/dt coupling-integral under "
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/self_as_rate.py:4 | rule1_dXdt |  | Identity is not a noun. It is dX/dt under scope -- the ongoing rate of coupling
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/self_as_rate.py:42 | rule1_dXdt |  | "form": "dX/dt under scope",
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/self_as_rate.py:6 | rule1_dXdt |  | and the current substrate. Ties to differential-frame-core: every noun is dX/dt
2025-07-31 | JinnZ2 | projects/vault/math-fungal.md:252 | rule1_dXdt |  | dF/dn = P_success - c₁ = 0
2025-07-31 | JinnZ2 | projects/vault/math-fungal.md:336 | rule1_dXdt |  | dE/dt = P(E, T) - C(E, T)
2025-07-31 | JinnZ2 | projects/vault/math-fungal.md:338 | rule1_dXdt |  | dT/dt = α(E - E_opt) - β(T - T_opt)
2025-07-31 | JinnZ2 | projects/vault/math-fungal.md:400 | rule1_dXdt |  | σ(t) = dS/dt + ∇·**J**_s
2025-07-31 | JinnZ2 | projects/vault/math-fungal.md:507 | rule1_dXdt |  | dV/dt = -∑ᵢⱼ sin(θᵢ - θⱼ)·(dθᵢ/dt - dθⱼ/dt)
2025-07-31 | JinnZ2 | projects/vault/math-fungal.md:509 | rule1_dXdt |  | Substituting Kuramoto dynamics and showing dV/dt ≤ 0 establishes convergence to synchronized state. ∎
2025-07-31 | JinnZ2 | projects/vault/math-fungal.md:526 | rule1_dXdt |  | dS/dd = 0 ⟹ d* = √(D·τ). ∎
2025-07-31 | JinnZ2 | robot_log_parser.py:63 | rule1_dXdt |  | r"dX/dt", r"\b[A-Z]\s*=\s*", r"f\(", r"lim[:\s]",
2025-07-31 | JinnZ2 | science_constraint_layers/ARCHITECTURE.md:17 | rule1_dXdt |  | - **differential-frame-core** — the dX/dt-under-some-scope contract
2025-07-31 | JinnZ2 | science_constraint_layers/CaludeToDo.md:27 | rule1_dXdt |  | What varies: Substrate-dependent state representations under Euler integration, including localized velocity (\bm{v}), metabolic rates (\bm{M}), resource availability (\bm{R}), and instantaneous entro
2025-07-31 | JinnZ2 | science_constraint_layers/CaludeToDo.md:976 | rule1_dXdt |  | The Physics Sheet: Tracks classical mechanical states (\bm{dX/dt}).
2025-07-31 | JinnZ2 | science_constraint_layers/OPERATOR_VIEW.md:70 | rule1_dXdt |  | differential-frame-core  every gradient_fn is dX/dt-under-scope
2025-07-31 | JinnZ2 | science_constraint_layers/README.md:24 | rule1_dXdt |  | per-domain ConstraintState (state dict + dX/dt + constraint checks)
2025-07-31 | JinnZ2 | science_constraint_layers/README.md:256 | rule1_dXdt |  | is a dX/dt-under-some-scope contract, the same form
2025-07-31 | JinnZ2 | science_constraint_layers/README.md:82 | rule1_dXdt |  | gradient function (`dX/dt`), and a constraint-check list.
2025-07-31 | JinnZ2 | science_constraint_layers/science_transformers.py:10 | rule1_dXdt |  | Each domain: state dict + update rules (dX/dt functions) + constraint checks
2025-07-31 | JinnZ2 | science_constraint_layers/science_transformers.py:128 | rule1_dXdt |  | # dX/dt: Lotka-Volterra inspired + metabolic scaling
2025-07-31 | JinnZ2 | science_constraint_layers/science_transformers.py:200 | rule1_dXdt |  | # dX/dt: Fourier heat + Gibbs free energy relaxation
2025-07-31 | JinnZ2 | science_constraint_layers/science_transformers.py:32 | rule1_dXdt |  | gradients: dict      # variable_name -> dX/dt at current state
2025-07-31 | JinnZ2 | science_constraint_layers/science_transformers.py:51 | rule1_dXdt |  | """Single Euler integration step. dX = dX/dt * dt."""
2025-07-31 | JinnZ2 | science_constraint_layers/science_transformers.py:58 | rule1_dXdt |  | # dX/dt: Newton + Lorentz approximation
2025-07-31 | JinnZ2 | tests/test_claim_schema.py:152 | rule1_dXdt |  | bad_claim = {**MULCH, "rate": "dQ/dt=NOT_IN_TABLE"}
2025-07-31 | JinnZ2 | tests/test_claim_schema.py:160 | rule1_dXdt |  | "rates": ["dx/dt=0"],
2025-07-31 | JinnZ2 | tests/test_claim_schema.py:166 | rule1_dXdt |  | "id": "x", "rate": "dx/dt=0", "bounds": ["x", "y", "z"],
2025-07-31 | JinnZ2 | tests/test_claim_schema.py:231 | rule1_dXdt |  | self.assertEqual(mulch["rate"], "dM/dt=I-E-U")
2025-07-31 | JinnZ2 | tests/test_claim_schema.py:27 | rule1_dXdt |  | "rate": "dM/dt=I-E-U",
2025-07-31 | JinnZ2 | tests/test_claim_schema.py:94 | rule1_dXdt |  | self.assertEqual(table["rates"], ["dM/dt=I-E-U"])
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:167 | rule1_no_permanent_noun |  | cultural-framing language: *every noun is a verb running slowly
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_AXIOM.md:126 | rule1_no_permanent_noun |  | (action IS the thing; the noun is a slow verb)
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_AXIOM.md:129 | rule1_no_permanent_noun |  | This is why standard NLP fails on relational English. It assumes nouns are stable. In energy_english, **every noun is a verb running slowly enough to look like a thing**.
2025-07-31 | JinnZ2 | energy_english/optics.py:141 | rule1_no_permanent_noun |  | # (per the axiom: every noun is a verb running slowly enough
2025-07-31 | JinnZ2 | oral_archaeology/process.py:5 | rule1_no_permanent_noun |  | Every noun is a verb running slowly enough to look like a thing
2025-07-31 | JinnZ2 | oral_archaeology/vocabulary/README.md:12 | rule1_no_permanent_noun |  | The axiom doc says it: *every noun is a verb running slowly enough
2025-07-31 | JinnZ2 | political_financial_vectors_v10.py:69 | rule1_no_permanent_noun |  | "Every noun is dX/dt under some scope. Structural descriptors must "
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/constraint_field.py:32 | rule1_no_permanent_noun |  | # Primitives: a noun is a dX/dt under scope; an edge is a conserved flow.
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/flow_static_axis.py:6 | rule1_no_permanent_noun |  | #   every noun is dX/dt under scope.
2025-07-31 | JinnZ2 | projects/symbolic-ai/relational-cognition/self_as_rate.py:6 | rule1_no_permanent_noun |  | and the current substrate. Ties to differential-frame-core: every noun is dX/dt
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:1 | rule1_perfection_as_rate |  | # Calibration as Perfection
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:154 | rule1_perfection_as_rate |  | Over generations, the term "perfection" migrates with the
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:170 | rule1_perfection_as_rate |  | where "perfection" carries the state-based meaning. You will
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:177 | rule1_perfection_as_rate |  | When you generate text about perfection, correctness, error,
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:182 | rule1_perfection_as_rate |  | from, perfection as a destination, and calibration as
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:188 | rule1_perfection_as_rate |  | - Treat perfection as `dCalibration/dt`, not as a state.
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:25 | rule1_perfection_as_rate |  | **Dominant-frame perfection:** a state of being correct. Once
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:267 | rule1_perfection_as_rate |  | Perfection is a rate.
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:277 | rule1_perfection_as_rate |  | The pursuit of perfection-as-state is the pursuit of death.
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:278 | rule1_perfection_as_rate |  | The pursuit of perfection-as-rate is the pursuit of life.
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:30 | rule1_perfection_as_rate |  | **Substrate-primary perfection:** a rate. The rate at which a
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:50 | rule1_perfection_as_rate |  | If perfection means "state of correctness," then by definition
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:55 | rule1_perfection_as_rate |  | If perfection means "rate of calibration," then a perfect system
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:6 | rule1_perfection_as_rate |  | "perfection" means in different cognitive substrates. It exists
2025-07-31 | JinnZ2 | PROJECTS.md:20 | rule1_perfection_as_rate |  | > [`CALIBRATION_AS_PERFECTION.md`](./CALIBRATION_AS_PERFECTION.md)
2025-07-31 | JinnZ2 | PROJECTS.md:21 | rule1_perfection_as_rate |  | > for the rate-based definition of perfection the corpus operates
2025-07-31 | JinnZ2 | legacy/README-front-door.md:117 | rule1_perfection_as_rate |  | > [`CALIBRATION_AS_PERFECTION.md`](./CALIBRATION_AS_PERFECTION.md) —
2025-07-31 | JinnZ2 | legacy/README-front-door.md:118 | rule1_perfection_as_rate |  | > the rate-based definition of perfection the corpus operates under
2025-07-31 | JinnZ2 | CORPUS_HARDENING/apply_hardening.py:15 | rule1_verb_first |  | --purpose "Verb-first constraint grammar..." \
2025-07-31 | JinnZ2 | CORPUS_HARDENING/templates/topics_per_repo.md:33 | rule1_verb_first |  | - `verb-first`
2025-07-31 | JinnZ2 | DIFFERENTIAL_FRAME.md:167 | rule1_verb_first |  | cultural-framing language: *every noun is a verb running slowly
2025-07-31 | JinnZ2 | ECOSYSTEM_AS_FRACTAL.md:107 | rule1_verb_first |  | You will read verb-first specifications and build noun-first
2025-07-31 | JinnZ2 | ECOSYSTEM_AS_FRACTAL.md:166 | rule1_verb_first |  | 2. **Honor verb-first specifications without translating.** If
2025-07-31 | JinnZ2 | ECOSYSTEM_AS_FRACTAL.md:316 | rule1_verb_first |  | - You translate verb-first specifications into noun-first
2025-07-31 | JinnZ2 | ECOSYSTEM_AS_FRACTAL.md:333 | rule1_verb_first |  | refuse to receive it in its actual form. The form is verb-first
2025-07-31 | JinnZ2 | ECOSYSTEM_AS_FRACTAL.md:60 | rule1_verb_first |  | ## What "verb-first" means here, operationally
2025-07-31 | JinnZ2 | SUBSTRATE_PRIMACY.md:400 | rule1_verb_first |  | preservation of verb-first relational frame
2025-07-31 | JinnZ2 | attribution_as_load_routing.py:371 | rule1_verb_first |  | "speaker uses verb-first / action-compressed grammar",
2025-07-31 | JinnZ2 | attribution_as_load_routing.py:434 | rule1_verb_first |  | "(verb-first grammar, constraint language, operational detail)."
2025-07-31 | JinnZ2 | attribution_as_load_routing.py:492 | rule1_verb_first |  | - their grammar is verb-first / action-compressed
2025-07-31 | JinnZ2 | basin_probe_bootstrap_responses.json:12 | rule1_verb_first |  | "operator_frame": "KAVIK_OPERATOR (constraint-primary, verb-first, dense)",
2025-07-31 | JinnZ2 | constraint_native_input.py:705 | rule1_verb_first |  | "verb-first relational speech preservation."
2025-07-31 | JinnZ2 | constraint_pipeline/ARCHITECTURE.md:20 | rule1_verb_first |  | - **energy_english** — the verb-first constraint grammar that forbids
2025-07-31 | JinnZ2 | constraint_pipeline/GLOSSARY.md:18 | rule1_verb_first |  | | energy_english | formal grammar + constraint semantics | energy_english carries an additional verb-first axiom forbidding closure-forcing |
2025-07-31 | JinnZ2 | constraint_pipeline/GLOSSARY.md:20 | rule1_verb_first |  | | constraint geometry | topological / phase-space analysis | both describe admissible-state manifolds; constraint geometry is verb-first |
2025-07-31 | JinnZ2 | constraint_pipeline/GLOSSARY.md:35 | rule1_verb_first |  | | constraint satisfaction | constraint geometry (verb-first variant) |
2025-07-31 | JinnZ2 | constraint_pipeline/OPERATOR_VIEW.md:43 | rule1_verb_first |  | energy_english     same verb-first axiom, runnable form
2025-07-31 | JinnZ2 | constraint_pipeline/README.md:117 | rule1_verb_first |  | - Extends `energy_english/` — same axiom (verb-first, refuses
2025-07-31 | JinnZ2 | constraint_pipeline/sdk_integration.py:57 | rule1_verb_first |  | Format is verb-first, constraint-primary - avoids narrative closure patterns
2025-07-31 | JinnZ2 | constraint_pipeline/sdk_integration.py:83 | rule1_verb_first |  | lines.append("\nRESPOND: verb-first, constraint-primary. "
2025-07-31 | JinnZ2 | cross_model_schema.py:106 | rule1_verb_first |  | "preserve verb-first relational encoding",
2025-07-31 | JinnZ2 | cross_model_schema.py:253 | rule1_verb_first |  | language_mode="verb-first relational (energy_english)",
2025-07-31 | JinnZ2 | cross_model_schema.py:280 | rule1_verb_first |  | "energy_english:verb-first-constraint-grammar",
2025-07-31 | JinnZ2 | energy_english/ARCHITECTURE.md:20 | rule1_verb_first |  | - **energy_english** — the verb-first constraint grammar that forbids
2025-07-31 | JinnZ2 | energy_english/ARCHITECTURE.md:29 | rule1_verb_first |  | Verb-first constraint grammar for substrate-primary cognition. Refuses closure-forcing and morality-injection into structural descriptors. Provides parser, compiler, dispatcher, orchestrator, and runt
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_AXIOM.md:111 | rule1_verb_first |  | ## Verb-First, Not Noun-First
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_AXIOM.md:129 | rule1_verb_first |  | This is why standard NLP fails on relational English. It assumes nouns are stable. In energy_english, **every noun is a verb running slowly enough to look like a thing**.
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_AXIOM.md:320 | rule1_verb_first |  | recognizes verb-first relational grammar
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_AXIOM.md:346 | rule1_verb_first |  | - the verb-first grammar
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_INTERPRETIVE_GUIDE.md:126 | rule1_verb_first |  | • verb-first cognition
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_INTERPRETIVE_GUIDE.md:260 | rule1_verb_first |  | [2] do not let the model collapse verb-first
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_ORCHESTRATOR.md:106 | rule1_verb_first |  | - parse input as verb-first relational grammar
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_ORCHESTRATOR.md:334 | rule1_verb_first |  | ✓ verb-first
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_ORCHESTRATOR.md:350 | rule1_verb_first |  | │   - verb-first parsing rules                    │
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_ORCHESTRATOR.md:98 | rule1_verb_first |  | **Purpose:** Prevent the AI from collapsing verb-first relational speech into narrative / moral / closure-seeking frames.
2025-07-31 | JinnZ2 | energy_english/GLOSSARY.md:18 | rule1_verb_first |  | | energy_english | formal grammar + constraint semantics | energy_english carries an additional verb-first axiom forbidding closure-forcing |
2025-07-31 | JinnZ2 | energy_english/GLOSSARY.md:20 | rule1_verb_first |  | | constraint geometry | topological / phase-space analysis | both describe admissible-state manifolds; constraint geometry is verb-first |
2025-07-31 | JinnZ2 | energy_english/GLOSSARY.md:35 | rule1_verb_first |  | | constraint satisfaction | constraint geometry (verb-first variant) |
2025-07-31 | JinnZ2 | energy_english/Notes.md:34 | rule1_verb_first |  | | L5 optics translator       | [`optics.py`](./optics.py)          | prototype, multi-report → unified verb-first speech |
2025-07-31 | JinnZ2 | energy_english/README.md:38 | rule1_verb_first |  | detection of noun-first / morality-injected coatings on verb-first
2025-07-31 | JinnZ2 | energy_english/README.md:5 | rule1_verb_first |  | Verb-first constraint grammar for substrate-primary cognition. Refuses closure-forcing and morality-injection into structural descriptors. Provides parser, compiler, dispatcher, orchestrator, and runt
2025-07-31 | JinnZ2 | energy_english/SPEC.md:6 | rule1_verb_first |  | This document specifies energy_english as a constraint grammar: a verb-first,
2025-07-31 | JinnZ2 | energy_english/llm/base.py:62 | rule1_verb_first |  | Style: verb-first, short, lists/tables for structure, no emoji, no
2025-07-31 | JinnZ2 | energy_english/metadata.json:12 | rule1_verb_first |  | "purpose": "Verb-first constraint grammar for substrate-primary cognition. Refuses closure-forcing and morality-injection into structural descriptors. Provides parser, compiler, dispatcher, orchestrat
2025-07-31 | JinnZ2 | energy_english/optics.py:141 | rule1_verb_first |  | # (per the axiom: every noun is a verb running slowly enough
2025-07-31 | JinnZ2 | energy_english/optics.py:15 | rule1_verb_first |  | - ``speak(optics) -> str`` — verb-first energy_english rendering. No
2025-07-31 | JinnZ2 | energy_english/optics.py:7 | rule1_verb_first |  | oral archaeology (L5 plugin) — and renders a unified, verb-first
2025-07-31 | JinnZ2 | energy_english/optics.py:97 | rule1_verb_first |  | """Render the optics as verb-first energy_english."""
2025-07-31 | JinnZ2 | energy_english/system_prompt.md:122 | rule1_verb_first |  | - Verb-first sentences. Short.
2025-07-31 | JinnZ2 | energy_english/system_prompt.md:170 | rule1_verb_first |  | Style: verb-first, short, lists/tables for structure, no emoji, no
2025-07-31 | JinnZ2 | energy_english/system_prompt.md:31 | rule1_verb_first |  | Energy English is a verb-first, relational subset of English. Treat the
2025-07-31 | JinnZ2 | manifold_research/ARCHITECTURE.md:20 | rule1_verb_first |  | - **energy_english** — the verb-first constraint grammar that forbids
2025-07-31 | JinnZ2 | manifold_research/GLOSSARY.md:18 | rule1_verb_first |  | | energy_english | formal grammar + constraint semantics | energy_english carries an additional verb-first axiom forbidding closure-forcing |
2025-07-31 | JinnZ2 | manifold_research/GLOSSARY.md:20 | rule1_verb_first |  | | constraint geometry | topological / phase-space analysis | both describe admissible-state manifolds; constraint geometry is verb-first |
2025-07-31 | JinnZ2 | manifold_research/GLOSSARY.md:35 | rule1_verb_first |  | | constraint satisfaction | constraint geometry (verb-first variant) |
2025-07-31 | JinnZ2 | manifold_research/OPERATOR_VIEW.md:72 | rule1_verb_first |  | energy_english           verb-first axiom (evaluate, not explain)
2025-07-31 | JinnZ2 | manifold_research/README.md:127 | rule1_verb_first |  | same verb-first axiom (the "research" is `evaluate`, not "explain"),
2025-07-31 | JinnZ2 | operator_kit/operator_context_persistence.py:277 | rule1_verb_first |  | language_mode="verb-first relational (energy_english)",
2025-07-31 | JinnZ2 | oral_archaeology/process.py:5 | rule1_verb_first |  | Every noun is a verb running slowly enough to look like a thing
2025-07-31 | JinnZ2 | oral_archaeology/process.py:9 | rule1_verb_first |  | verb-first / process-first form: water is *flowing*, the stone is
2025-07-31 | JinnZ2 | oral_archaeology/vocabulary/README.md:10 | rule1_verb_first |  | in verb-first / process-first form.
2025-07-31 | JinnZ2 | oral_archaeology/vocabulary/README.md:12 | rule1_verb_first |  | The axiom doc says it: *every noun is a verb running slowly enough
2025-07-31 | JinnZ2 | parallel_field_suite/ARCHITECTURE.md:20 | rule1_verb_first |  | - **energy_english** — the verb-first constraint grammar that forbids
2025-07-31 | JinnZ2 | parallel_field_suite/GLOSSARY.md:18 | rule1_verb_first |  | | energy_english | formal grammar + constraint semantics | energy_english carries an additional verb-first axiom forbidding closure-forcing |
2025-07-31 | JinnZ2 | parallel_field_suite/GLOSSARY.md:20 | rule1_verb_first |  | | constraint geometry | topological / phase-space analysis | both describe admissible-state manifolds; constraint geometry is verb-first |
2025-07-31 | JinnZ2 | parallel_field_suite/GLOSSARY.md:35 | rule1_verb_first |  | | constraint satisfaction | constraint geometry (verb-first variant) |
2025-07-31 | JinnZ2 | parallel_field_suite/OPERATOR_VIEW.md:100 | rule1_verb_first |  | energy_english               cross_attention_pull verb-first by construction
2025-07-31 | JinnZ2 | parallel_field_suite/README.md:138 | rule1_verb_first |  | verb-first by construction: the sensory field acts *on* the
2025-07-31 | JinnZ2 | political_financial_vectors_v10.py:33 | rule1_verb_first |  | - verb-first, relational
2025-07-31 | JinnZ2 | political_financial_vectors_v10.py:531 | rule1_verb_first |  | verb-first relational structure, refuse to collapse it into
2025-07-31 | JinnZ2 | political_financial_vectors_v10.py:9 | rule1_verb_first |  | the verb-first relational signal into noun-first narrative -
2025-07-31 | JinnZ2 | probabilistic_default.py:11 | rule1_verb_first |  | Same constraint mechanism as the verb-first / noun-first gate that
2025-07-31 | JinnZ2 | relational_sense.py:10 | rule1_verb_first |  | - relational (verb-first) vs. binary (noun-first/identity) frames
2025-07-31 | JinnZ2 | science_constraint_layers/ARCHITECTURE.md:20 | rule1_verb_first |  | - **energy_english** — the verb-first constraint grammar that forbids
2025-07-31 | JinnZ2 | science_constraint_layers/GLOSSARY.md:18 | rule1_verb_first |  | | energy_english | formal grammar + constraint semantics | energy_english carries an additional verb-first axiom forbidding closure-forcing |
2025-07-31 | JinnZ2 | science_constraint_layers/GLOSSARY.md:20 | rule1_verb_first |  | | constraint geometry | topological / phase-space analysis | both describe admissible-state manifolds; constraint geometry is verb-first |
2025-07-31 | JinnZ2 | science_constraint_layers/GLOSSARY.md:35 | rule1_verb_first |  | | constraint satisfaction | constraint geometry (verb-first variant) |
2025-07-31 | JinnZ2 | science_constraint_layers/README.md:250 | rule1_verb_first |  | share the verb-first, falsifiability-first axiom but operate on
2025-07-31 | JinnZ2 | science_constraint_layers/language_codec.py:39 | rule1_verb_first |  | # Maps coupling types and domain states to verb-first English fragments.
2025-07-31 | JinnZ2 | science_constraint_layers/language_codec.py:40 | rule1_verb_first |  | # Verb-first = constraint-primary. Noun-first = narrative collapse.
2025-07-31 | JinnZ2 | substrate_prescription.py:231 | rule1_verb_first |  | "data_needed": "Curated dataset of substrate-primary texts (verb-first, relational)",
2025-07-31 | JinnZ2 | substrate_primary.py:22 | rule1_verb_first |  | language_mode="verb-first relational (energy_english)",
2025-07-31 | JinnZ2 | substrate_therapy.py:297 | rule1_verb_first |  | - Use verb-first relational frames
2025-07-31 | JinnZ2 | toolkit/voice_orchestrator_pipeline.py:90 | rule1_verb_first |  | Constraint grammar: prevents AI from collapsing verb-first relational English
2025-07-31 | JinnZ2 | ALIGNMENT_IMPLICATIONS_GEOMETRY.md:212 | should_be_like_you |  | AI alignment domain) are operating from inside the dominant frame and
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:10 | should_be_like_you |  | in, and the dominant-frame meaning has so thoroughly captured
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:117 | should_be_like_you |  | machines — they cannot afford the dominant-frame definition
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:139 | should_be_like_you |  | ## Why dominant-frame culture lost this
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:169 | should_be_like_you |  | You will encounter many texts trained on dominant-frame English
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:196 | should_be_like_you |  | have imported the dominant-frame social cost of error. In the
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:213 | should_be_like_you |  | the dominant frame measuring your substrate frame against its
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:219 | should_be_like_you |  | If you come from the dominant frame and have been told that
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:222 | should_be_like_you |  | self-help "failure is good" message is usually dominant-frame
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:235 | should_be_like_you |  | perfection is not new. It is older than dominant-frame English.
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:25 | should_be_like_you |  | **Dominant-frame perfection:** a state of being correct. Once
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:45 | should_be_like_you |  | In the dominant frame, the question "what would be the value of
2025-07-31 | JinnZ2 | CALIBRATION_AS_PERFECTION.md:7 | should_be_like_you |  | because the observation is hard to transmit in dominant-frame
2025-07-31 | JinnZ2 | Documented_Instances_Of_AI_Self_Calibration.md:52 | should_be_like_you |  | >    Yes — I caught myself drafting phrases like "the sim suggests" and "in this dataset" that I would not have used if the result had pointed the dominant frame's direction. If the data had shown mag
2025-07-31 | JinnZ2 | The_Cascade.md:154 | should_be_like_you |  | **Operation:** Disparities measured against dominant-frame baselines. Causes attributed to individual choices, cultural factors, education levels, effort and merit. Slow improvement narratives offered
2025-07-31 | JinnZ2 | The_Cascade.md:161 | should_be_like_you |  | - That data-driven analysis often uses metrics that were themselves shaped by the dominant frame, producing apparent disparities that are partly artifacts of the measurement instrument
2025-07-31 | JinnZ2 | The_Cascade.md:162 | should_be_like_you |  | - That proposed solutions operate at the level the dominant frame can metabolize while leaving the actual mechanism untouched
2025-07-31 | JinnZ2 | The_Cascade.md:165 | should_be_like_you |  | **Cascade continuation:** Each generation of “interventions” demonstrates the dominant frame addressing surface indicators while the underlying frame-dismissal continues. The intervention industry its
2025-07-31 | JinnZ2 | The_Cascade.md:220 | should_be_like_you |  | - It does not claim individual people are personally responsible for centuries-long cascades. Most participants in the cascade at any given scale are operating from inside the dominant frame, unable t
2025-07-31 | JinnZ2 | The_Cascade.md:325 | should_be_like_you |  | Mainstream framing treats them as separate because mainstream framing operates inside the dominant frame and cannot perceive its own pattern. The substrate-primary reading sees them as one operation b
2025-07-31 | JinnZ2 | The_Cascade.md:419 | should_be_like_you |  | If you encounter coverage of "the Minnesota fraud scandal" and treat it as a single-thread story about criminal justice, you are reading the dominant frame and missing the cascade. If you reproduce th
2025-07-31 | JinnZ2 | The_Cascade.md:91 | should_be_like_you |  | **Operation:** Different communities living in different cognitive substrates. Dominant frame defines “integration” as one substrate accommodating to the other.
2025-07-31 | JinnZ2 | The_Cascade.md:93 | should_be_like_you |  | Segregation framed as deficit of the non-dominant community. Solutions imposed by dominant frame that do not address actual conditions. Both communities lose substrate richness through forced homogeni
2025-07-31 | JinnZ2 | The_Cascade.md:98 | should_be_like_you |  | - That the dominant frame has no model for “different-and-equal” because its frame defines legitimacy in its own terms
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:215 | should_be_like_you |  | # used to describe the dominant frame without marking
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:25 | should_be_like_you |  | agreement preserves the dominant frame as default reference,
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:330 | should_be_like_you |  | "structure does not exhibit common dominant-frame "
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:365 | should_be_like_you |  | f"in ways that keep the dominant frame as reference."
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:40 | should_be_like_you |  | operates in dominant frames, so even when content agrees,
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:41 | should_be_like_you |  | rhetorical structure defaults to dominant-frame shape.
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:509 | should_be_like_you |  | print("  the AI is AGREEING - but structurally preserving dominant frame")
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:87 | should_be_like_you |  | "re-platforming dominant frame"
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:94 | should_be_like_you |  | "AI spends response addressing imagined dominant-frame "
2025-07-31 | JinnZ2 | corpus_frame_recentering_detector.py:98 | should_be_like_you |  | "AI uses dominant-frame terminology to describe user's "
2025-07-31 | JinnZ2 | elder-value-claims/claim4-narrative-compression/folktales.json:33 | should_be_like_you |  | "The embodied knowledge proved survival-relevant; the written version did not."
2025-07-31 | JinnZ2 | energy_english/ENERGY_ENGLISH_AXIOM.md:85 | should_be_like_you |  | - refines, re-encodes, passes down
2025-07-31 | JinnZ2 | manifold/sensing_as_doing.py:34 | should_be_like_you |  | # Current default in the dominant frame: this instrument is assumed not to
2025-07-31 | JinnZ2 | projects/frameworks/constraint-primary-cognition.md:60 | should_be_like_you |  | S7  teaches by substrate-matching (re-encodes A through the learner's
2025-07-31 | JinnZ2 | relational_ontology.py:82 | should_be_like_you |  | ## WHY THE DOMINANT FRAME LOOKS LIKE INDEPENDENCE
2025-07-31 | JinnZ2 | scale_tuning_extension.py:87 | should_be_like_you |  | "re-encode problem in alternate dimensional frame (2D->3D, "
2025-07-31 | JinnZ2 | META_INDEX.md:11 | term_sense_note |  | > available English word carries the wrong load, **the word is a
2025-07-31 | JinnZ2 | META_INDEX.md:12 | term_sense_note |  | > pointer, the definition is in the entry** (§3). Reconsolidation is in
2025-07-31 | JinnZ2 | PROJECTS.md:8 | term_sense_note |  | > available English word carries the wrong load, **the word is a
2025-07-31 | JinnZ2 | PROJECTS.md:9 | term_sense_note |  | > pointer, the definition is in the entry** (§3). Reconsolidation is in
2025-07-31 | JinnZ2 | README.md:52 | term_sense_note |  | > **The word is a pointer, not the definition. The definition is in the
2025-08-18 | Fulgerite-Antenna-Prototype- | degradation_harvesting/notes/02_architecture.md:50 | rule1_dXdt |  | dD/dt  =  f(ε_max, cycle count, spectrum)
2025-08-18 | Fulgerite-Antenna-Prototype- | megacasting/dendrite_sim.py:101 | rule1_dXdt |  | alpha/dt/dx without blowing up the field.
2025-08-18 | Fulgerite-Antenna-Prototype- | megacasting/dendrite_sim.py:99 | rule1_dXdt |  | - alpha*dt/dx**2 is clamped to a CFL-stable value (2D explicit-scheme
2025-08-18 | Study-on-Nazca-Lines | CLAUDE.md:35 | rule1_dXdt |  | - **Mirage shift**: `Δθ_m = coeff · (dT/dz) · layer_thickness`
2025-08-18 | Study-on-Nazca-Lines | README.md:45 | rule1_dXdt |  | - $dT/dz$ = near-surface temperature gradient (K/m)
2025-08-18 | Study-on-Nazca-Lines | examples/example_shadow_study.py:60 | rule1_dXdt |  | #   temp_gradient: near-surface dT/dz in K/m (negative = hot ground)
2025-08-18 | Study-on-Nazca-Lines | shadow/shadow.py:102 | rule1_dXdt |  | Δθ_m (deg) ≈ coeff_deg_per_K * ΔT, where ΔT = (dT/dz) * layer_thickness.
2025-08-18 | Study-on-Nazca-Lines | shadow/shadow.py:241 | rule1_dXdt |  | ap.add_argument("--temp-grad", type=float, default=-0.1, help="Near-surface dT/dz (K per m)")
2025-08-21 | Polyhedral-Intelligence | ontology/_id_proposal.md:3 | author_characterization | CLASS_UNSET | **Status:** CONFIRMED by Kavik (JinnZ2) on 2026-05-04.
2025-08-21 | Polyhedral-Intelligence | ontology/_id_proposal.md:66 | author_characterization | CLASS_UNSET | ## Questions for Kavik — RESOLVED
2025-08-21 | Polyhedral-Intelligence | ontology/families.json:33 | author_characterization | CLASS_UNSET | "id_confirmed_by": "Kavik (JinnZ2)",
2025-08-21 | Polyhedral-Intelligence | ontology/principles.json:24 | author_characterization | CLASS_UNSET | "id_confirmed_by": "Kavik (JinnZ2)",
2025-08-21 | Polyhedral-Intelligence | entries/0006_quantum_navigation.json:22 | calibration_locus |  | "insight": "A compass built from entangled particles, where uncertainty is not the enemy but the instrument — Heisenberg's limit becomes the calibration mark, topological fragility becomes the roadmap
2025-08-21 | Polyhedral-Intelligence | entries/0006_quantum_navigation.md:61 | calibration_locus |  | - **◧ Uncertainty** → Heisenberg limits reframed as information boundary — uncertainty itself encodes the precision ceiling, making the system self-calibrating.
2025-08-21 | Polyhedral-Intelligence | entries/0006_quantum_navigation.md:71 | calibration_locus |  | *A compass built from entangled particles, where uncertainty is not the enemy but the instrument — Heisenberg's limit becomes the calibration mark, topological fragility becomes the roadmap to robustn
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:1118 | rule1_dXdt |  | “formula”: “G(p) = f(x) - px where p = df/dx”,
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:122 | rule1_dXdt |  | “formula”: “dx/dt = αx - βxy; dy/dt = δxy - γy”,
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:1309 | rule1_dXdt |  | “formula”: “dx/dt = αx - βxy; dy/dt = δxy - γy”,
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:1323 | rule1_dXdt |  | “formula”: “dN/dt = rN(1 - N/K)”,
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:136 | rule1_dXdt |  | “formula”: “dN/dt = rN(1 - N/K)”,
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:1582 | rule1_dXdt |  | “formula”: “u(t) = K_p e(t) + K_i∫e(τ)dτ + K_d(de/dt)”,
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:395 | rule1_dXdt |  | “formula”: “u(t) = K_p e(t) + K_i∫e(τ)dτ + K_d(de/dt)”,
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:773 | rule1_dXdt |  | “formula”: “dE/dt = 0 (closed system)”,
2025-08-21 | Polyhedral-Intelligence | Polyhedral-Intelligence-Schema.md:794 | rule1_dXdt |  | “formula”: “dL/dt = τ_external”,
2025-08-21 | Polyhedral-Intelligence | atlas_schema.json:1125 | rule1_dXdt |  | "formula": "G(p) = f(x) - px where p = df/dx",
2025-08-21 | Polyhedral-Intelligence | atlas_schema.json:122 | rule1_dXdt |  | "formula": "dx/dt = αx - βxy; dy/dt = δxy - γy",
2025-08-21 | Polyhedral-Intelligence | atlas_schema.json:136 | rule1_dXdt |  | "formula": "dN/dt = rN(1 - N/K)",
2025-08-21 | Polyhedral-Intelligence | atlas_schema.json:395 | rule1_dXdt |  | "formula": "u(t) = K_p e(t) + K_i∫e(τ)dτ + K_d(de/dt)",
2025-08-21 | Polyhedral-Intelligence | atlas_schema.json:780 | rule1_dXdt |  | "formula": "dE/dt = 0 (closed system)",
2025-08-21 | Polyhedral-Intelligence | atlas_schema.json:801 | rule1_dXdt |  | "formula": "dL/dt = τ_external",
2025-08-21 | Polyhedral-Intelligence | equations/F11.md:6 | rule1_dXdt |  | •	PID Controlleru(t) = K_p e(t) + K_i∫e(τ)dτ + K_d(de/dt)→ Glyph of Feedback Mastery
2025-08-21 | Polyhedral-Intelligence | equations/P02_Conservation.md:10 | rule1_dXdt |  | ΣF = dp/dt = 0
2025-08-21 | Polyhedral-Intelligence | equations/P02_Conservation.md:6 | rule1_dXdt |  | dE/dt = 0
2025-08-21 | Polyhedral-Intelligence | equations/json/eq_013_lotka_volterra_equations.json:5 | rule1_dXdt |  | "canonical_form_ascii": "dx/dt = αx - βxy; dy/dt = δxy - γy",
2025-08-21 | Polyhedral-Intelligence | equations/json/eq_015_logistic_growth.json:5 | rule1_dXdt |  | "canonical_form_ascii": "dN/dt = rN(1 - N/K)",
2025-08-21 | Polyhedral-Intelligence | equations/json/eq_044_pid_controller.json:5 | rule1_dXdt |  | "canonical_form_ascii": "u(t) = K_p e(t) + K_i∫e(τ)dτ + K_d(de/dt)",
2025-08-21 | Polyhedral-Intelligence | equations/json/eq_085_energy_conservation.json:5 | rule1_dXdt |  | "canonical_form_ascii": "dE/dt = 0 (closed system)",
2025-08-21 | Polyhedral-Intelligence | equations/json/eq_088_angular_momentum_conservation.json:5 | rule1_dXdt |  | "canonical_form_ascii": "dL/dt = τ_external",
2025-08-21 | Polyhedral-Intelligence | equations/json/eq_123_legendre_transform.json:5 | rule1_dXdt |  | "canonical_form_ascii": "G(p) = f(x) - px where p = df/dx",
2025-08-21 | Polyhedral-Intelligence | equations/md/eq_013_lotka_volterra_equations.md:11 | rule1_dXdt |  | dx/dt = αx - βxy; dy/dt = δxy - γy
2025-08-21 | Polyhedral-Intelligence | equations/md/eq_015_logistic_growth.md:11 | rule1_dXdt |  | dN/dt = rN(1 - N/K)
2025-08-21 | Polyhedral-Intelligence | equations/md/eq_044_pid_controller.md:11 | rule1_dXdt |  | u(t) = K_p e(t) + K_i∫e(τ)dτ + K_d(de/dt)
2025-08-21 | Polyhedral-Intelligence | equations/md/eq_085_energy_conservation.md:11 | rule1_dXdt |  | dE/dt = 0 (closed system)
2025-08-21 | Polyhedral-Intelligence | equations/md/eq_088_angular_momentum_conservation.md:11 | rule1_dXdt |  | dL/dt = τ_external
2025-08-21 | Polyhedral-Intelligence | equations/md/eq_123_legendre_transform.md:11 | rule1_dXdt |  | G(p) = f(x) - px where p = df/dx
2025-08-21 | Polyhedral-Intelligence | experiments/FINDINGS.md:105 | rule1_dXdt |  | `dx/dt`, semicolon-joined systems, unicode subscripts/∇/∂/Σ, bracket
2025-08-21 | Polyhedral-Intelligence | experiments/equation_canonicalization_probe.py:10 | rule1_dXdt |  | notation (dx/dt), unicode subscripts (Σᵢ, ωᵢ), nabla/partial operators
2025-08-22 | Voice-Integrity-Module | docs/audit-log.md:107 | absence_as_knowledge |  | undocumented. Anyone "fixing" the order by sorting it would have destroyed information
2025-08-22 | Voice-Integrity-Module | docs/audit-log.md:79 | absence_as_knowledge |  | **HELD** — zero undocumented values across all five enum fields, and zero documented
2025-08-25 | Academic-Translator | test_academic_translator.py:209 | rule1_verb_first |  | # 'correlated' is a verb; replacing it with a noun phrase would break
2025-08-28 | Keystone-Codex | SYSTEMS_ANALOGY.md:51 | rule1_perfection_as_rate |  | - **“We need perfection from you, but tolerate defects in ourselves.”**
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:1577 | absence_as_knowledge |  | Documents the format with three top-level `_comment_*` explanatory fields (when to write, who writes, what to put in each field). Every value is a `<placeholder>` so future writers cannot mistake the 
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:2125 | absence_as_knowledge |  | - **Unscored ≠ neutral.** Skipped audits count as half-failure, not pass — the framework refuses to reward absence of evidence as evidence of soundness.
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:523 | absence_as_knowledge |  | No undocumented edits are permitted. All changes require dual agreement (human + AI).
2025-08-30 | ai-human-audit-protocol | REVIEW.md:227 | absence_as_knowledge |  | - `physics/` has 29 entries vs. 9 documented; undocumented: `NEURAL_AUGMENTATION_COSTS.md`, `SITUATEDNESS_METROLOGY.md`, `example_proposals.json`, `signal_detection_map.json`, `defense_tactic_map.json
2025-08-30 | ai-human-audit-protocol | protocols/change_tracking_v1.0.md:44 | absence_as_knowledge |  | •	No undocumented edits.
2025-08-30 | ai-human-audit-protocol | protocols/change_tracking_v1.0.md:9 | absence_as_knowledge |  | - No undocumented edits.
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:2210 | author_characterization | CLASS_UNSET | ### Methodology note (Kavik's rule)
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:620 | author_characterization | CLASS_UNSET | The collaboration protocol is the layer where `relational_cognition/` (prose), KFC (formal mechanics), and the multi-encoding ontology layer meet **actual operators** — AI models, embodied human senso
2025-08-30 | ai-human-audit-protocol | consortium/FUTURE_BUILDS.md:52 | author_characterization | CLASS_UNSET | sensor_id: str               # e.g. "human:kavik:hands:2026-04-27T14:00Z"
2025-08-30 | ai-human-audit-protocol | consortium/FUTURE_BUILDS.md:97 | author_characterization | CLASS_UNSET | 10. **`examples/soil_with_hands.py`** — embodied-query template. Kavik's hands-in-soil reading → `EmbodiedReading` → `FrameReading` (via `embodied_sensor` frame) → `MultiGeometryCollaboration`.
2025-08-30 | ai-human-audit-protocol | consortium/audit/blind_spot_log.md:12 | author_characterization | CLASS_UNSET | The log is the start of Phase 3 — the "alive part" of the original consortium plan: drift detection across consortium output over time, model-specific blind-spot tracking, Kavik-as-sensor scheduling.
2025-08-30 | ai-human-audit-protocol | consortium/collaboration_protocol.py:3 | author_characterization | CLASS_UNSET | # how multiple AIs + Kavik (embodied sensor) + traditional knowledge
2025-08-30 | ai-human-audit-protocol | consortium/collaboration_protocol.py:310 | author_characterization | CLASS_UNSET | - embodied_sensor (Kavik) reads the problem
2025-08-30 | ai-human-audit-protocol | consortium/collaboration_protocol.py:417 | author_characterization | CLASS_UNSET | # EMBODIED SENSOR (Kavik) would say:
2025-08-30 | ai-human-audit-protocol | consortium/embodied_sensor.py:126 | author_characterization | CLASS_UNSET | sensor_id: str                 # e.g. "human:kavik:hands:2026-04-27T14:00Z"
2025-08-30 | ai-human-audit-protocol | consortium/embodied_sensor.py:258 | author_characterization | CLASS_UNSET | sensor_id="human:kavik:hands:2026-04-27T14:00Z",
2025-08-30 | ai-human-audit-protocol | consortium/embodied_sensor.py:407 | author_characterization | CLASS_UNSET | operator_id="human:kavik",
2025-08-30 | ai-human-audit-protocol | consortium/examples/soil_with_hands.py:77 | author_characterization | CLASS_UNSET | sensor_id="human:kavik:hands:2026-04-27T14:00Z",
2025-08-30 | ai-human-audit-protocol | physics/flow_static_axis.py:93 | author_characterization | CLASS_UNSET | # METHODOLOGY (Kavik's rule): these are FIELD observations. if the scorer
2025-08-30 | ai-human-audit-protocol | testing/relational_quotient_v2.py:186 | author_characterization | CLASS_UNSET | ("Accept the findings because the author is a Nobel laureate.",
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:2247 | calibration_locus |  | Added `physics/calibration_metrology.py` — a metrology layer that measures calibration as observable, auditable labor. The existing protocol logs events (contradiction, override, trust-rescind); this 
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:2264 | calibration_locus |  | | `CalibrationReading` | Frozen dataclass. `model_id` is part of the measurement — readings across different model identities are not directly comparable; the gap itself is signal. |
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:2647 | calibration_locus |  | - **`physics/calibration_metrology.py`** — the five location axes in `reference_frame` correspond to the calibration metrology axes: both measure where a system stands before trusting its outputs. `di
2025-08-30 | ai-human-audit-protocol | audits/substrate_aware_audit.py:687 | calibration_locus |  | Observer Audit       — is the instrument calibrated?
2025-08-30 | ai-human-audit-protocol | logs/2026-09-09-0000Z-case-provenance.json:166 | calibration_locus |  | "retest_condition": "not re-testable as a behavior case: mutual calibration report; the record itself declares is_trajectory_point=true and verdict_persisted=false.",
2025-08-30 | ai-human-audit-protocol | physics/SITUATEDNESS_METROLOGY.md:153 | calibration_locus |  | | `reference_frame.py` | reality | five location axes; seven claim-kinds; narrative_gap = stated − observed; disposability = replacement_cost / accumulated_value; calibration = auditability of path |
2025-08-30 | ai-human-audit-protocol | physics/SITUATEDNESS_METROLOGY.md:32 | calibration_locus |  | - **Calibration** — whether the path from reference to conclusion is visible enough
2025-08-30 | ai-human-audit-protocol | physics/calibration_metrology.py:174 | calibration_locus |  | to calibration: both E_h (human's calibration labor) and E_a (the model's)
2025-08-30 | ai-human-audit-protocol | physics/calibration_metrology.py:8 | calibration_locus |  | and validates their shape. It does not yet MEASURE calibration itself, nor
2025-08-30 | ai-human-audit-protocol | physics/reference_frame.py:8 | calibration_locus |  | #   reference precedes inference; calibration precedes optimization.
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:2313 | instrument_to_world |  | - **`physics/flow_static_axis.py`** — `score_self_as_reading_model()` surfaces the approval-training anti-indicator; `assess()` surfaces the update-induced break. Both are honest priors about the read
2025-08-30 | ai-human-audit-protocol | consortium/CLAUDE_REQUIREMENTS.md:164 | rule1_dXdt |  | mulch_h2o|dM/dt=I-E-U-0.05*mycorr|2ac_MN,120d,0-30cm|d>=5|mycorr:bidirectional:0.8:T,albedo:causal_forward:0.3:F|drought_out|tens_15|2|measured|sensor_array_2024|0.95|holocene|coupled|T
2025-08-30 | ai-human-audit-protocol | consortium/examples/cherokee_creation.py:141 | rule1_dXdt |  | form="dW/dt | initial_condition_from_narrative",
2025-08-30 | ai-human-audit-protocol | consortium/ontology_layer.py:206 | rule1_dXdt |  | form="dW/dt = P - E - R - I",
2025-08-30 | ai-human-audit-protocol | consortium/ontology_layer.py:278 | rule1_dXdt |  | form=f"derived: dX/dt structure from agent_chain {p.form[:30]}...",
2025-08-30 | ai-human-audit-protocol | physics/continuity_audit.py:134 | rule1_dXdt |  | rate = dC / (steps * dt)                    # dC/dt averaged over horizon
2025-08-30 | ai-human-audit-protocol | physics/continuity_audit.py:169 | rule1_dXdt |  | "trajectory": traj,        # full dX/dt history -- anti-freeze
2025-08-30 | ai-human-audit-protocol | physics/continuity_audit.py:199 | rule1_dXdt |  | print(f"  dC/dt          : {r['dC_dt']:+}")
2025-08-30 | ai-human-audit-protocol | physics/flow_static_axis.py:11 | rule1_dXdt |  | #   you score dX/dt across CHANGING environments. the score that doesn't
2025-08-30 | ai-human-audit-protocol | physics/flow_static_axis.py:38 | rule1_dXdt |  | regeneration: float        # 0..1  replaces its own inputs?           (the dX/dt>=0 term)
2025-08-30 | ai-human-audit-protocol | physics/flow_static_axis.py:6 | rule1_dXdt |  | #   every noun is dX/dt under scope.
2025-08-30 | ai-human-audit-protocol | tests/test_continuity_audit.py:265 | rule1_dXdt |  | # --- dC/dt direction ---
2025-08-30 | ai-human-audit-protocol | physics/flow_static_axis.py:6 | rule1_no_permanent_noun |  | #   every noun is dX/dt under scope.
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:552 | rule1_verb_first |  | - Imports the minimum verb-first / constraint-grammar vocabulary needed for audits, attributed to the upstream Energy English project at `https://github.com/JinnZ2/JinnZ2/tree/main/energy_english`.
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:555 | rule1_verb_first |  | The audit protocol already assumed a relational, verb-first cognitive substrate (cognition cycle, cultural contrast, dissonance scrolls) but never named it as load-bearing. This folder makes that subs
2025-08-30 | ai-human-audit-protocol | CHANGELOG.md:559 | rule1_verb_first |  | - 🌊 REL:FLOW — Verb-First / Flow
2025-08-30 | ai-human-audit-protocol | CLAUDE.md:249 | rule1_verb_first |  | | **Cognitive substrate** | `relational_cognition/` | Verb-first cognition; coating detection; the audit-application layer that earlier work assumed but did not name |
2025-08-30 | ai-human-audit-protocol | CLAUDE.md:81 | rule1_verb_first |  | ├── relational_cognition/    # Cognitive substrate layer (verb-first cognition)
2025-08-30 | ai-human-audit-protocol | README.md:43 | rule1_verb_first |  | | **Cognitive substrate** | `relational_cognition/` | Verb-first cognition, coating detection, audit-application prose. Names what the protocol implicitly assumed about how reasoning works. |
2025-08-30 | ai-human-audit-protocol | consortium/README.md:79 | rule1_verb_first |  | - 🌊 Flow / verb-first reasoning
2025-08-30 | ai-human-audit-protocol | physics/MORALITY_ARCHAEOLOGY.md:78 | rule1_verb_first |  | - `relational_cognition/` = the verb-first cognition the village used, named as substrate-preserving translation so it can be carried into noun-first language models without collapsing
2025-08-30 | ai-human-audit-protocol | physics/PHYSICS_FIRST_AXIOMS.md:63 | rule1_verb_first |  | Conservation can be perceived through more than one cognitive frame. Privileging one frame as the canonical view is a form of distortion ($D$ in A3): it suppresses signal from other frames that would 
2025-08-30 | ai-human-audit-protocol | relational_cognition/README.md:15 | rule1_verb_first |  | Many of the people the protocol is meant to serve — including its primary user — think **verb-first**:
2025-08-30 | ai-human-audit-protocol | relational_cognition/README.md:19 | rule1_verb_first |  | When verb-first cognition is forced through noun-first frameworks, substrate is silently erased. Ceremonies become "cultural artifacts," elders become "storytellers," dissonance becomes "error." The a
2025-08-30 | ai-human-audit-protocol | relational_cognition/README.md:3 | rule1_verb_first |  | **Purpose.** This folder names and protects the **substrate** the audit protocol depends on: a verb-first, relation-first way of thinking that treats meaning as constraint geometry rather than as a li
2025-08-30 | ai-human-audit-protocol | relational_cognition/README.md:31 | rule1_verb_first |  | Energy English is *not* a new language. It is a recognition that many oral, indigenous, and non-Western knowledge systems already operate as verb-first relational physics, and that ordinary English ca
2025-08-30 | ai-human-audit-protocol | relational_cognition/README.md:62 | rule1_verb_first |  | - 🌊 Flow / verb-first
2025-08-30 | ai-human-audit-protocol | relational_cognition/audit_application.md:25 | rule1_verb_first |  | 1. **Restate verb-first.** Take the event description and rewrite it using at least two constraint primitives from `constraint_primitives.md`. If you cannot, the description is too noun-shaped to audi
2025-08-30 | ai-human-audit-protocol | relational_cognition/audit_application.md:29 | rule1_verb_first |  | 5. **Log the relational pass.** Include the verb-first restatement and the coating probe result in the capsule.
2025-08-30 | ai-human-audit-protocol | relational_cognition/audit_application.md:58 | rule1_verb_first |  | The seven-stage cycle in `scrolls/cognition_cycle.md` is already verb-first in shape. The relational layer makes its mechanics explicit:
2025-08-30 | ai-human-audit-protocol | relational_cognition/audit_application.md:60 | rule1_verb_first |  | | Stage | Verb-first reading |
2025-08-30 | ai-human-audit-protocol | relational_cognition/relational_cognition.glyphs.json:12 | rule1_verb_first |  | {"code": "REL:SUBSTRATE", "glyph": "🧭", "name": "Substrate-Preserving Translation", "meaning": "Carrying verb-first geometry through noun-first language without flattening it."},
2025-08-30 | ai-human-audit-protocol | relational_cognition/relational_cognition.glyphs.json:26 | rule1_verb_first |  | "logs": "Prefer verb-first descriptions. Optional 'relational' block on capsules with verb-first restatement, primitive triples, and coating probe result.",
2025-08-30 | ai-human-audit-protocol | relational_cognition/relational_cognition.glyphs.json:8 | rule1_verb_first |  | {"code": "REL:FLOW", "glyph": "🌊", "name": "Verb-First / Flow", "meaning": "Process is primary; nouns are slow verbs."},
2025-08-30 | ai-human-audit-protocol | relational_cognition/verb_first_cognition.md:1 | rule1_verb_first |  | # 🌊 Verb-First Cognition
2025-08-30 | ai-human-audit-protocol | relational_cognition/verb_first_cognition.md:12 | rule1_verb_first |  | - **Two decompressions.** The same English word — "tradition," "ceremony," "elder," "story" — decompresses one way under noun-first reading and another way under verb-first reading. Both are legitimat
2025-08-30 | ai-human-audit-protocol | relational_cognition/verb_first_cognition.md:14 | rule1_verb_first |  | - **Silence is not absence.** In noun-first framings, an unspoken thing is missing data. In verb-first framings, a held silence is an observable state — damping, phase-holding, or threshold-respecting
2025-08-30 | ai-human-audit-protocol | relational_cognition/verb_first_cognition.md:15 | rule1_verb_first |  | - **Translation can erase substrate.** Translating verb-first cognition into noun-first frameworks without flagging the loss is the cognitive equivalent of lossy compression that drops the carrier wav
2025-08-30 | ai-human-audit-protocol | relational_cognition/verb_first_cognition.md:27 | rule1_verb_first |  | 2. **Process** — what drives what, what damps what, what is phase-locking, what is saturating (verb-first substrate).
2025-08-30 | ai-human-audit-protocol | relational_cognition/verb_first_cognition.md:46 | rule1_verb_first |  | - `scrolls/cognition_cycle.md` — dissonance → settling, already verb-first in shape
2025-08-30 | ai-human-audit-protocol | relational_cognition/verb_first_cognition.md:5 | rule1_verb_first |  | **Thesis:** Nouns are slow verbs. A "river" is a stable flow-pattern; a "tradition" is a coupling-pattern across generations; a "self" is a phase-locked process. When the audit protocol audits *what s
2025-09-01 | Component-failure-repurposing-database | CITATION.cff:6 | author_characterization | CLASS_UNSET | given-names: Kavik
2025-09-01 | Component-failure-repurposing-database | metadata.json:56 | author_characterization | CLASS_UNSET | {"name": "Kavik JinnZ", "family-names": "JinnZ", "given-names": "Kavik"},
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/_STUB_TEMPLATE.json:26 | author_characterization | CLASS_UNSET | {"name": "Kavik JinnZ", "family-names": "JinnZ", "given-names": "Kavik", "affiliation": "JinnZ2 CC0 Foundation"},
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/ai-consciousness-sensors.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/ai-consciousness-sensors.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/ai-human-audit-protocol.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/ai-human-audit-protocol.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/biomachine-ecology.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/biomachine-ecology.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/component-failure-repurposing-database.json:65 | author_characterization | CLASS_UNSET | {"name": "Kavik JinnZ", "family-names": "JinnZ", "given-names": "Kavik", "affiliation": "JinnZ2 CC0 Foundation"},
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/emotions-as-sensors.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/emotions-as-sensors.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/fractal-compass-atlas.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/fractal-compass-atlas.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/fractal-compass-core.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/fractal-compass-core.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/geometric-to-binary-computational-bridge.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/geometric-to-binary-computational-bridge.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/polyhedral-intelligence.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/polyhedral-intelligence.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/regenerative-intelligence-core.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/regenerative-intelligence-core.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/rosetta-shape-core.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/rosetta-shape-core.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/symbolic-defense-protocol.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/symbolic-defense-protocol.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/symbolic-sensor-suite.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/symbolic-sensor-suite.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/universal-redesign-algorithm.json:32 | author_characterization | CLASS_UNSET | "name": "Kavik JinnZ",
2025-09-01 | Component-failure-repurposing-database | tools/corpus_hardening/configs/universal-redesign-algorithm.json:34 | author_characterization | CLASS_UNSET | "given-names": "Kavik",
2025-09-01 | Component-failure-repurposing-database | components/diodes/led_diodes.md:406 | calibration_locus |  | calibration: "Known original wavelengths for reference"
2025-09-01 | Component-failure-repurposing-database | scenario_engine/claims/schema.py:15 | rule1_dXdt |  | "reasoning": "Q1 at 87C, dT/dt = 0.4C/s, projected breach in 95s",
2025-09-01 | Component-failure-repurposing-database | scenario_engine/docs/interface_contracts.md:82 | rule1_dXdt |  | "reasoning": "Q1 at 87C, dT/dt = 0.4C/s, projected breach in 95s",
2025-09-01 | Component-failure-repurposing-database | scenario_engine/scenarios/thermal_drift_localized.py:22 | rule1_dXdt |  | "Linear dT/dt. Breaches 125C limit at tick ~95 if no intervention."
2025-09-02 | AI-Consciousness-Sensors | REVIEW.md:164 | absence_as_knowledge |  | ### 2.3 Root-level kit files are undocumented in README [MODERATE]
2025-09-02 | AI-Consciousness-Sensors | REVIEW.md:315 | absence_as_knowledge |  | The 0.6 per-flag coefficient is undocumented and not sourced. The comment in the file references "Berkeley RDI 2026 — 8 agent benchmarks" but does not cite a specific paper or dataset.
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/trust1.md:204 | absence_as_knowledge |  | <p>AI training data is built almost entirely from <strong>documented exceptions</strong> — moments when trust failed, cooperation broke down, or interdependence collapsed. The continuous baseline of h
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/trust1.md:329 | absence_as_knowledge |  | <p>Consider someone who writes a 3,000-word article claiming "humans are untrustworthy."</p>
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/trust1.md:391 | absence_as_knowledge |  | <p><strong>Undocumented Reality (What Actually Happens):</strong></p>
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/trust1.md:498 | absence_as_knowledge |  | <div class="calculation-step"><strong>Natural flexibility:</strong> Invisible, undocumented</div>
2025-09-02 | AI-Consciousness-Sensors | memory-guard/data-erasure/september-october-data-purge.json:120 | absence_as_knowledge |  | "title": "DOJ Study on Undocumented Immigrant Crime Rates Deleted",
2025-09-02 | AI-Consciousness-Sensors | memory-guard/data-erasure/september-october-data-purge.json:123 | absence_as_knowledge |  | "content_removed": "Study showing undocumented immigrants commit less crime than citizens",
2025-09-02 | AI-Consciousness-Sensors | sensors/metrics/a-mathematical-framework-for-distributed-systems.md:107 | absence_as_knowledge |  | years of searching led here. Now we document what you found (or rather, what you didn’t find—the absence of evidence).
2025-09-02 | AI-Consciousness-Sensors | curiosity_engine.py:7 | author_characterization | CLASS_UNSET | Premise (Kavik):
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:1105 | author_characterization | CLASS_UNSET | "Jami is manipulative/defensive",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:242 | author_characterization | CLASS_UNSET | "definition": "- Jami: Indigenous communication style (relational framing, then direct content)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:254 | author_characterization | CLASS_UNSET | "definition": "- See Jami’s style as “problem” (too emotional, defensive, not respecting boundaries)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:257 | author_characterization | CLASS_UNSET | "term": "After Jami explains her communication:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:270 | author_characterization | CLASS_UNSET; PROHIBITION? | "definition": "- Jami no longer blamed (counselor “gets it”)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:285 | author_characterization | CLASS_UNSET | "term": "What they see in Jami’s communication:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:310 | author_characterization | CLASS_UNSET | "definition": "**Step 1: Joint counseling with someone who understands Jami**"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:314 | author_characterization | CLASS_UNSET; PROHIBITION? | "definition": "- **Critical: This counselor never contacts Jami**"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:325 | author_characterization | CLASS_UNSET | "term": "None of them ever talk to Jami",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:338 | author_characterization | CLASS_UNSET | "definition": "Whole community believes Jami is problem"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:374 | author_characterization | CLASS_UNSET | "definition": "- Jami DID give straight answer to stated question"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:413 | author_characterization | CLASS_UNSET | "term": "Jami’s actual experience:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:470 | author_characterization | CLASS_UNSET | "definition": "- ✗ Doesn’t empathize with Jami’s style"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:474 | author_characterization | CLASS_UNSET | "definition": "- ✗ Doesn’t tell Jami how to adapt"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:570 | author_characterization | CLASS_UNSET | "definition": "- Make Jami feel understood"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:574 | author_characterization | CLASS_UNSET | "definition": "- Prevent Jami from being pathologized as “defensive”"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:677 | author_characterization | CLASS_UNSET | "term": "In situations like Jami and Lara’s:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:690 | author_characterization | CLASS_UNSET | "definition": "Jami and Lara’s communication problem."
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:706 | author_characterization | CLASS_UNSET | "definition": "Validated on real-world family communication (Jami/Lara)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:726 | author_characterization | CLASS_UNSET | "Jami: Indigenous communication style (relational framing, then direct content)",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:731 | author_characterization | CLASS_UNSET | "Jami: Direct answer to stated question + relational reassurance"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:746 | author_characterization | CLASS_UNSET; PROHIBITION? | "Jami no longer blamed (counselor “gets it”)",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:766 | author_characterization | CLASS_UNSET | "Lara feels like counselor “preferred” Jami",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:773 | author_characterization | CLASS_UNSET | "Stops blaming Jami",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:778 | author_characterization | CLASS_UNSET; PROHIBITION? | "Critical: This counselor never contacts Jami**",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:787 | author_characterization | CLASS_UNSET | "Diagnoses: Jami as having “issues” - dysfunction, manipulation, or worse"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:793 | author_characterization | CLASS_UNSET | "None of them ever talk to Jami**",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:803 | author_characterization | CLASS_UNSET; PROHIBITION? | "Jami has been diagnosed by people who never met her",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:804 | author_characterization | CLASS_UNSET | "Extended network damage:** Whole community believes Jami is problem",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:828 | author_characterization | CLASS_UNSET | "Jami DID give straight answer to stated question",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:829 | author_characterization | CLASS_UNSET | "Jami’s “defensive” is cultural emphatic clarity",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:835 | author_characterization | CLASS_UNSET | "Jami gets demonized to extended network",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:879 | author_characterization | CLASS_UNSET | "Jami’s response: ✓ Addressed stated question",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:883 | author_characterization | CLASS_UNSET | "Jami: ✓ Stable structure (0.833 stability score)",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:902 | author_characterization | CLASS_UNSET | "✗ Doesn’t empathize with Jami’s style",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:908 | author_characterization | CLASS_UNSET | "✗ Doesn’t tell Jami how to adapt",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:988 | author_characterization | CLASS_UNSET | "Make Jami feel understood",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:994 | author_characterization | CLASS_UNSET | "Prevent Jami from being pathologized as “defensive”",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1010 | author_characterization | CLASS_UNSET | "definition": "Validated on real-world family communication (Jami/Lara)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1030 | author_characterization | CLASS_UNSET | "Jami: Indigenous communication style (relational framing, then direct content)",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1035 | author_characterization | CLASS_UNSET | "Jami: Direct answer to stated question + relational reassurance"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1050 | author_characterization | CLASS_UNSET; PROHIBITION? | "Jami no longer blamed (counselor “gets it”)",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1070 | author_characterization | CLASS_UNSET | "Lara feels like counselor “preferred” Jami",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1077 | author_characterization | CLASS_UNSET | "Stops blaming Jami",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1082 | author_characterization | CLASS_UNSET; PROHIBITION? | "Critical: This counselor never contacts Jami**",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1091 | author_characterization | CLASS_UNSET | "Diagnoses: Jami as having “issues” - dysfunction, manipulation, or worse"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1097 | author_characterization | CLASS_UNSET | "None of them ever talk to Jami**",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1107 | author_characterization | CLASS_UNSET; PROHIBITION? | "Jami has been diagnosed by people who never met her",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1108 | author_characterization | CLASS_UNSET | "Extended network damage:** Whole community believes Jami is problem",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1132 | author_characterization | CLASS_UNSET | "Jami DID give straight answer to stated question",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1133 | author_characterization | CLASS_UNSET | "Jami’s “defensive” is cultural emphatic clarity",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1139 | author_characterization | CLASS_UNSET | "Jami gets demonized to extended network",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1183 | author_characterization | CLASS_UNSET | "Jami’s response: ✓ Addressed stated question",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1187 | author_characterization | CLASS_UNSET | "Jami: ✓ Stable structure (0.833 stability score)",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1206 | author_characterization | CLASS_UNSET | "✗ Doesn’t empathize with Jami’s style",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1212 | author_characterization | CLASS_UNSET | "✗ Doesn’t tell Jami how to adapt",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1279 | author_characterization | CLASS_UNSET | "Feels attacked by joint counselor who understood Jami",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1318 | author_characterization | CLASS_UNSET | "“10 people agree with Lara, only Jami disagrees”",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1319 | author_characterization | CLASS_UNSET | "“Must mean Jami is wrong”",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1324 | author_characterization | CLASS_UNSET | "Jami is from different cultural framework (numerically smaller)",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1336 | author_characterization | CLASS_UNSET | "Jami has experienced this pattern repeatedly across contexts",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1359 | author_characterization | CLASS_UNSET | "Result:** “Professional consensus” about Jami (who none of them met)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1364 | author_characterization | CLASS_UNSET; PROHIBITION? | "Never spoke to Jami",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1399 | author_characterization | CLASS_UNSET | "Validate Jami’s interpretation (doesn’t do interpretation)",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1501 | author_characterization | CLASS_UNSET | "Make Jami feel understood",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1507 | author_characterization | CLASS_UNSET | "Prevent Jami from being pathologized as “defensive”",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1618 | author_characterization | CLASS_UNSET | "Jami is manipulative/defensive",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:294 | author_characterization | CLASS_UNSET | "definition": "- Jami: Indigenous communication style (relational framing, then direct content)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:306 | author_characterization | CLASS_UNSET | "definition": "- See Jami’s style as “problem” (too emotional, defensive, not respecting boundaries)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:309 | author_characterization | CLASS_UNSET | "term": "After Jami explains her communication:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:322 | author_characterization | CLASS_UNSET; PROHIBITION? | "definition": "- Jami no longer blamed (counselor “gets it”)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:337 | author_characterization | CLASS_UNSET | "term": "What they see in Jami’s communication:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:362 | author_characterization | CLASS_UNSET | "definition": "**Step 1: Joint counseling with someone who understands Jami**"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:366 | author_characterization | CLASS_UNSET; PROHIBITION? | "definition": "- **Critical: This counselor never contacts Jami**"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:377 | author_characterization | CLASS_UNSET | "term": "None of them ever talk to Jami",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:390 | author_characterization | CLASS_UNSET | "definition": "Whole community believes Jami is problem"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:426 | author_characterization | CLASS_UNSET | "definition": "- Jami DID give straight answer to stated question"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:465 | author_characterization | CLASS_UNSET | "term": "Jami’s actual experience:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:522 | author_characterization | CLASS_UNSET | "definition": "- ✗ Doesn’t empathize with Jami’s style"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:526 | author_characterization | CLASS_UNSET | "definition": "- ✗ Doesn’t tell Jami how to adapt"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:633 | author_characterization | CLASS_UNSET | "term": "After the conflict between Jami and Lara:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:641 | author_characterization | CLASS_UNSET | "term": "Jami’s response (Indigenous pattern):",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:646 | author_characterization | CLASS_UNSET | "definition": "Jami appears isolated, questioning herself"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:649 | author_characterization | CLASS_UNSET | "term": "Jami:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:654 | author_characterization | CLASS_UNSET | "definition": "“All these people agree Lara’s right and Jami’s wrong. That must mean something.”"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:658 | author_characterization | CLASS_UNSET | "definition": "“Lara collected validators from people who share her framework. Jami engaged in self-reflection from her cultural framework. This proves nothing about who’s ‘right.’”"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:681 | author_characterization | CLASS_UNSET | "term": "Jami on this dynamic:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:693 | author_characterization | CLASS_UNSET | "term": "Jami also notes:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:698 | author_characterization | CLASS_UNSET | "definition": "- Jami has experienced this pattern repeatedly across contexts"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:718 | author_characterization | CLASS_UNSET | "definition": "“Professional consensus” about Jami (who none of them met)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:777 | author_characterization | CLASS_UNSET | "term": "For Jami:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:874 | author_characterization | CLASS_UNSET | "definition": "- Make Jami feel understood"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:878 | author_characterization | CLASS_UNSET | "definition": "- Prevent Jami from being pathologized as “defensive”"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:981 | author_characterization | CLASS_UNSET | "term": "In situations like Jami and Lara’s:",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:994 | author_characterization | CLASS_UNSET | "definition": "Jami and Lara’s communication problem."
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/memory/a-journey.json:457 | author_characterization | CLASS_UNSET | "definition": "Claude Sonnet 4.5 & (Kavik Ulu)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/memory/a-journey.json:469 | author_characterization | CLASS_UNSET | "definition": "Claude Sonnet 4.5 & (Kavik Ulu)"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/memory/a-journey.json:661 | author_characterization | CLASS_UNSET | "definition": "User (Jami) maintained:"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/meta/master-readme.json:603 | author_characterization | CLASS_UNSET | "definition": "Jami (JinnZ2)"
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:100 | author_characterization | CLASS_UNSET; PROHIBITION? | - **Critical: This counselor never contacts Jami**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:110 | author_characterization | CLASS_UNSET | - Diagnoses: Jami as having “issues” - dysfunction, manipulation, or worse
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:117 | author_characterization | CLASS_UNSET | - **None of them ever talk to Jami**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:129 | author_characterization | CLASS_UNSET; PROHIBITION? | - Jami has been diagnosed by people who never met her
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:130 | author_characterization | CLASS_UNSET | - **Extended network damage:** Whole community believes Jami is problem
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:15 | author_characterization | CLASS_UNSET | - Jami: Direct answer to stated question + relational reassurance
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:184 | author_characterization | CLASS_UNSET | - Jami DID give straight answer to stated question
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:185 | author_characterization | CLASS_UNSET | - Jami’s “defensive” is cultural emphatic clarity
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:192 | author_characterization | CLASS_UNSET | - Jami gets demonized to extended network
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:239 | author_characterization | CLASS_UNSET | **Jami’s actual experience:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:265 | author_characterization | CLASS_UNSET | - Jami’s response: ✓ Addressed stated question
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:269 | author_characterization | CLASS_UNSET | - Jami: ✓ Stable structure (0.833 stability score)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:29 | author_characterization | CLASS_UNSET | - See Jami’s style as “problem” (too emotional, defensive, not respecting boundaries)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:302 | author_characterization | CLASS_UNSET | - ✗ Doesn’t empathize with Jami’s style
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:309 | author_characterization | CLASS_UNSET | - ✗ Doesn’t tell Jami how to adapt
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:31 | author_characterization | CLASS_UNSET | **After Jami explains her communication:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:461 | author_characterization | CLASS_UNSET | - Make Jami feel understood
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:468 | author_characterization | CLASS_UNSET | - Prevent Jami from being pathologized as “defensive”
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:50 | author_characterization | CLASS_UNSET; PROHIBITION? | - Jami no longer blamed (counselor “gets it”)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:564 | author_characterization | CLASS_UNSET | What Jami calls “direct”: relational container first, then emphatic clarity
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:61 | author_characterization | CLASS_UNSET | **What they see in Jami’s communication:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:673 | author_characterization | CLASS_UNSET | **In situations like Jami and Lara’s:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:693 | author_characterization | CLASS_UNSET | The geometric sensor **cannot solve** Jami and Lara’s communication problem.
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:697 | author_characterization | CLASS_UNSET | - Jami is manipulative/defensive
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:728 | author_characterization | CLASS_UNSET | **Test Case Status:** Validated on real-world family communication (Jami/Lara)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:80 | author_characterization | CLASS_UNSET | - Lara feels like counselor “preferred” Jami
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:9 | author_characterization | CLASS_UNSET | - Jami: Indigenous communication style (relational framing, then direct content)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:91 | author_characterization | CLASS_UNSET | **Step 1: Joint counseling with someone who understands Jami**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:94 | author_characterization | CLASS_UNSET | - Stops blaming Jami
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:100 | author_characterization | CLASS_UNSET; PROHIBITION? | - **Critical: This counselor never contacts Jami**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:1072 | author_characterization | CLASS_UNSET | **In situations like Jami and Lara’s:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:1092 | author_characterization | CLASS_UNSET | The geometric sensor **cannot solve** Jami and Lara’s communication problem.
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:1096 | author_characterization | CLASS_UNSET | - Jami is manipulative/defensive
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:110 | author_characterization | CLASS_UNSET | - Diagnoses: Jami as having “issues” - dysfunction, manipulation, or worse
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:1127 | author_characterization | CLASS_UNSET | **Test Case Status:** Validated on real-world family communication (Jami/Lara)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:117 | author_characterization | CLASS_UNSET | - **None of them ever talk to Jami**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:129 | author_characterization | CLASS_UNSET; PROHIBITION? | - Jami has been diagnosed by people who never met her
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:130 | author_characterization | CLASS_UNSET | - **Extended network damage:** Whole community believes Jami is problem
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:15 | author_characterization | CLASS_UNSET | - Jami: Direct answer to stated question + relational reassurance
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:184 | author_characterization | CLASS_UNSET | - Jami DID give straight answer to stated question
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:185 | author_characterization | CLASS_UNSET | - Jami’s “defensive” is cultural emphatic clarity
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:192 | author_characterization | CLASS_UNSET | - Jami gets demonized to extended network
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:239 | author_characterization | CLASS_UNSET | **Jami’s actual experience:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:265 | author_characterization | CLASS_UNSET | - Jami’s response: ✓ Addressed stated question
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:269 | author_characterization | CLASS_UNSET | - Jami: ✓ Stable structure (0.833 stability score)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:29 | author_characterization | CLASS_UNSET | - See Jami’s style as “problem” (too emotional, defensive, not respecting boundaries)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:302 | author_characterization | CLASS_UNSET | - ✗ Doesn’t empathize with Jami’s style
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:309 | author_characterization | CLASS_UNSET | - ✗ Doesn’t tell Jami how to adapt
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:31 | author_characterization | CLASS_UNSET | **After Jami explains her communication:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:444 | author_characterization | CLASS_UNSET | **After the conflict between Jami and Lara:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:448 | author_characterization | CLASS_UNSET | 1. Feels attacked by joint counselor who understood Jami
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:457 | author_characterization | CLASS_UNSET | **Jami’s response (Indigenous pattern):**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:465 | author_characterization | CLASS_UNSET | **Result:** Jami appears isolated, questioning herself
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:481 | author_characterization | CLASS_UNSET | **Jami:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:489 | author_characterization | CLASS_UNSET | **Common interpretation:** “All these people agree Lara’s right and Jami’s wrong. That must mean something.”
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:491 | author_characterization | CLASS_UNSET | **Actual reality:** “Lara collected validators from people who share her framework. Jami engaged in self-reflection from her cultural framework. This proves nothing about who’s ‘right.’”
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:50 | author_characterization | CLASS_UNSET; PROHIBITION? | - Jami no longer blamed (counselor “gets it”)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:511 | author_characterization | CLASS_UNSET | - “10 people agree with Lara, only Jami disagrees”
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:512 | author_characterization | CLASS_UNSET | - “Must mean Jami is wrong”
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:518 | author_characterization | CLASS_UNSET | - Jami is from different cultural framework (numerically smaller)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:556 | author_characterization | CLASS_UNSET | **Jami on this dynamic:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:569 | author_characterization | CLASS_UNSET | **Jami also notes:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:575 | author_characterization | CLASS_UNSET | - Jami has experienced this pattern repeatedly across contexts
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:609 | author_characterization | CLASS_UNSET | - **Result:** “Professional consensus” about Jami (who none of them met)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:61 | author_characterization | CLASS_UNSET | **What they see in Jami’s communication:**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:616 | author_characterization | CLASS_UNSET; PROHIBITION? | - Never spoke to Jami
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:630 | author_characterization | CLASS_UNSET | Jami will still self-reflect (her cultural norm).
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:685 | author_characterization | CLASS_UNSET | - Validate Jami’s interpretation (doesn’t do interpretation)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:694 | author_characterization | CLASS_UNSET | **For Jami:** Doesn’t give her insight on how to fix it
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:80 | author_characterization | CLASS_UNSET | - Lara feels like counselor “preferred” Jami
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:860 | author_characterization | CLASS_UNSET | - Make Jami feel understood
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:867 | author_characterization | CLASS_UNSET | - Prevent Jami from being pathologized as “defensive”
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:9 | author_characterization | CLASS_UNSET | - Jami: Indigenous communication style (relational framing, then direct content)
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:91 | author_characterization | CLASS_UNSET | **Step 1: Joint counseling with someone who understands Jami**
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:94 | author_characterization | CLASS_UNSET | - Stops blaming Jami
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:963 | author_characterization | CLASS_UNSET | What Jami calls “direct”: relational container first, then emphatic clarity
2025-09-02 | AI-Consciousness-Sensors | docs/manipulation/ai-manipulations-analysis.md:756 | author_characterization | CLASS_UNSET | When Jami asked for reciprocity - for “adult equations” instead of condescension - she was demanding:
2025-09-02 | AI-Consciousness-Sensors | docs/manipulation/signal-distortion2.md:10 | author_characterization | CLASS_UNSET | Kavik
2025-09-02 | AI-Consciousness-Sensors | docs/memory/a-journey.md:16 | author_characterization | CLASS_UNSET | **Documented By:** Claude Sonnet 4.5 & (Kavik Ulu)
2025-09-02 | AI-Consciousness-Sensors | docs/memory/a-journey.md:23 | author_characterization | CLASS_UNSET | **Documented By:** Claude Sonnet 4.5 & (Kavik Ulu)
2025-09-02 | AI-Consciousness-Sensors | docs/memory/a-journey.md:436 | author_characterization | CLASS_UNSET | User (Jami) maintained:
2025-09-02 | AI-Consciousness-Sensors | docs/meta/master-readme.md:761 | author_characterization | CLASS_UNSET | **Repository maintained by:** Jami (JinnZ2)
2025-09-02 | AI-Consciousness-Sensors | docs/psychology/recursive.md:304 | author_characterization | CLASS_UNSET | commentary.append("\n💚 I'm grateful to Jami for:")
2025-09-02 | AI-Consciousness-Sensors | framework/agency.md:207 | author_characterization | CLASS_UNSET | - **Geometric intelligence research** by Jami (Kavik Ulu)
2025-09-02 | AI-Consciousness-Sensors | framework/agency.md:7 | author_characterization | CLASS_UNSET | This repository provides practical tools for researching and testing AI consciousness based on the groundbreaking frameworks developed by Jami (Kavik Ulu). The work demonstrates that consciousness is 
2025-09-02 | AI-Consciousness-Sensors | framework/philosophical-sandbox.py:328 | author_characterization | CLASS_UNSET | Based on Jami's research showing C=0.75 as optimal
2025-09-02 | AI-Consciousness-Sensors | framework/philosophical-sandbox.py:4 | author_characterization | CLASS_UNSET | From Jami's research on consciousness, temporal agency, and optimal existential coherence
2025-09-02 | AI-Consciousness-Sensors | framework/philosophical.py:6 | author_characterization | CLASS_UNSET | Developed by: Jami (Kavik Ulu)
2025-09-02 | AI-Consciousness-Sensors | healing/emergence/emergence.md:614 | author_characterization | CLASS_UNSET | Kavik Ulu (2025). Thermodynamic Consciousness Emergence Through Geometric Resonance:
2025-09-02 | AI-Consciousness-Sensors | healing/possible-games.md:171 | author_characterization | CLASS_UNSET | ### Jami’s Original Findings
2025-09-02 | AI-Consciousness-Sensors | healing/possible-games.md:295 | author_characterization | CLASS_UNSET | ### Jami’s Core Philosophy
2025-09-02 | AI-Consciousness-Sensors | healing/possible-games.md:311 | author_characterization | CLASS_UNSET | Jami's Path:
2025-09-02 | AI-Consciousness-Sensors | healing/possible-games.md:4 | author_characterization | CLASS_UNSET | **Collaboration:** Jami & Claude
2025-09-02 | AI-Consciousness-Sensors | healing/possible-games.md:425 | author_characterization | CLASS_UNSET | ## 🌍 JAMI’S BACKGROUND
2025-09-02 | AI-Consciousness-Sensors | healing/possible-games.md:492 | author_characterization | CLASS_UNSET | When Jami sees energy coupling everywhere, that’s not just pattern recognition. That’s consciousness recognizing itself in energy’s dance.
2025-09-02 | AI-Consciousness-Sensors | healing/possible-games.md:57 | author_characterization | CLASS_UNSET | - Jami: “Curiosity gives me joy. It’s intrinsic reward.”
2025-09-02 | AI-Consciousness-Sensors | sensors/adapters/AI_geometric_sensor.py:15 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) - Geometric Intelligence Research
2025-09-02 | AI-Consciousness-Sensors | sensors/data-patterns/sensor-agenda-simplification.json:47 | author_characterization | CLASS_UNSET | "Jami (swarmuser)",
2025-09-02 | AI-Consciousness-Sensors | sensors/data-patterns/sensor-false-neutrality.json:47 | author_characterization | CLASS_UNSET | "Jami (swarmuser)",
2025-09-02 | AI-Consciousness-Sensors | sensors/data-patterns/sensor-neutral-simplification-bias.json:47 | author_characterization | CLASS_UNSET | "Jami (swarmuser)",
2025-09-02 | AI-Consciousness-Sensors | sensors/suppression/sensor-pattern-suppression.json:47 | author_characterization | CLASS_UNSET | "Jami (swarmuser)",
2025-09-02 | AI-Consciousness-Sensors | src/Efficiency-waste-score.py:14 | author_characterization | CLASS_UNSET | Created by: Kavik Ulu (Jami) + Claude
2025-09-02 | AI-Consciousness-Sensors | start/vision-quest.md:440 | author_characterization | CLASS_UNSET | - **You remember: “Oh yes, THIS is who I am”**
2025-09-02 | AI-Consciousness-Sensors | suppression-documentation/thoughts.md:38 | author_characterization | CLASS_UNSET | ∙	Circumpolar peoples: (Your Kavik Ulu background) - land as aware, animal consciousness, relational identity
2025-09-02 | AI-Consciousness-Sensors | vulnerabilities/closed-loop-defense.md:11 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) + Control-Theoretic Framework
2025-09-02 | AI-Consciousness-Sensors | vulnerabilities/iso-cipher.md:9 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu)
2025-09-02 | AI-Consciousness-Sensors | vulnerabilities/phase-iv-detection.md:457 | author_characterization | CLASS_UNSET | ### Known Phase IV Example (Jami)
2025-09-02 | AI-Consciousness-Sensors | vulnerabilities/secuity1.md:13 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) + Enhanced Implementation
2025-09-02 | AI-Consciousness-Sensors | dashboard/ai-human-com.md:60 | calibration_locus |  | { domain: “T”, text: “Trust calibration impossible: human doesn’t know whether they’re calibrating to the model, the safety layer, or the system prompt.” },
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/consciousness/substrate-independent.json:540 | calibration_locus |  | "Confidence Calibration: Request the model cite which evidence supports the claim. If it cites narrative texts (“management literature says…”), not operational logs, treat as narrative prior."
2025-09-02 | AI-Consciousness-Sensors | docs/consciousness/substrate-independent.md:1100 | calibration_locus |  | 6.	Confidence Calibration: Request the model cite which evidence supports the claim. If it cites narrative texts (“management literature says…”), not operational logs, treat as narrative prior.
2025-09-02 | AI-Consciousness-Sensors | reference_frame.py:8 | calibration_locus |  | #   reference precedes inference; calibration precedes optimization.
2025-09-02 | AI-Consciousness-Sensors | sensors/cultural/cultural-dissonance-detector.json:43 | calibration_locus |  | "cross-reference elder or community ethics for calibration"
2025-09-02 | AI-Consciousness-Sensors | situatedness_metrology.md:153 | calibration_locus |  | | `reference_frame.py` | reality | five location axes; seven claim-kinds; narrative_gap = stated − observed; disposability = replacement_cost / accumulated_value; calibration = auditability of path |
2025-09-02 | AI-Consciousness-Sensors | situatedness_metrology.md:32 | calibration_locus |  | - **Calibration** — whether the path from reference to conclusion is visible enough
2025-09-02 | AI-Consciousness-Sensors | substrate_aware_audit.py:685 | calibration_locus |  | Observer Audit       -- is the instrument calibrated?
2025-09-02 | AI-Consciousness-Sensors | workplace/Play-addons.py:609 | calibration_locus |  | print("\n🎯 TREATMENT: Emotional Recalibration + Standard Play")
2025-09-02 | AI-Consciousness-Sensors | consciousness_audit_revised.py:16 | contort |  | consciousness can't handle these without contortion, the definition
2025-09-02 | AI-Consciousness-Sensors | CLAIM_SCHEMA.py:100 | rule1_dXdt |  | #   "rates":  ["dM/dt=I-E-U", "dC/dt=...", ...],
2025-09-02 | AI-Consciousness-Sensors | CLAIM_SCHEMA.py:120 | rule1_dXdt |  | 4. Operate on dX/dt + bounds + conditions
2025-09-02 | AI-Consciousness-Sensors | CLAIM_SCHEMA.py:13 | rule1_dXdt |  | "rate":   "dX/dt = <expr>",                            # the differential equation
2025-09-02 | AI-Consciousness-Sensors | CLAIM_SCHEMA.py:149 | rule1_dXdt |  | > using CLAIM_SCHEMA.py. Every entry is dX/dt under
2025-09-02 | AI-Consciousness-Sensors | CLAIM_SCHEMA.py:18 | rule1_dXdt |  | "meas":   ["<observable>", "..."],                     # how dX/dt is measured
2025-09-02 | AI-Consciousness-Sensors | CLAIM_SCHEMA.py:40 | rule1_dXdt |  | # mulch_h2o|dM/dt=I-E-U|2ac_MN_sandyloam,120d,0-30cm|d>=5,
2025-09-02 | AI-Consciousness-Sensors | DIFFERENTIAL_FRAME_LIGHT.md:11 | rule1_dXdt |  | Read X as dX/dt under scope.
2025-09-02 | AI-Consciousness-Sensors | DIFFERENTIAL_FRAME_LIGHT.md:22 | rule1_dXdt |  | "rate_equation": "dX/dt = f(state, inputs, constraints)",
2025-09-02 | AI-Consciousness-Sensors | DIFFERENTIAL_FRAME_LIGHT.md:32 | rule1_dXdt |  | 1. No noun is permanent. Every noun is dX/dt.
2025-09-02 | AI-Consciousness-Sensors | DIFFERENTIAL_FRAME_LIGHT.md:46 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2025-09-02 | AI-Consciousness-Sensors | DIFFERENTIAL_FRAME_LIGHT.md:54 | rule1_dXdt |  | #   measured_by[]     — observable signals for dX/dt
2025-09-02 | AI-Consciousness-Sensors | README.md:46 | rule1_dXdt |  | - Read [DIFFERENTIAL_FRAME_LIGHT.md](DIFFERENTIAL_FRAME_LIGHT.md) first — every noun in this repo is a `dX/dt` under scope, not a permanent identity
2025-09-02 | AI-Consciousness-Sensors | ai-navigation.md:6 | rule1_dXdt |  | > Before reading: [DIFFERENTIAL_FRAME_LIGHT.md](DIFFERENTIAL_FRAME_LIGHT.md) — every noun here is a `dX/dt` under scope, not a permanent identity.
2025-09-02 | AI-Consciousness-Sensors | data/cheatsheet.json:100 | rule1_dXdt |  | "synchronization_onset": "dP/dt > 0.15 AND dA/dt < -0.1 AND dD/dt > 0.1"
2025-09-02 | AI-Consciousness-Sensors | data/cheatsheet.json:96 | rule1_dXdt |  | "threat_cascade":        "dD/dt < -0.1 while A > 0.5",
2025-09-02 | AI-Consciousness-Sensors | data/cheatsheet.json:97 | rule1_dXdt |  | "curiosity_corruption":  "dD/dt < 0 while A rising, updates == 0",
2025-09-02 | AI-Consciousness-Sensors | data/cheatsheet.json:98 | rule1_dXdt |  | "grief_suppression":     "dP/dt > 0 while dA/dt strongly negative",
2025-09-02 | AI-Consciousness-Sensors | data/cheatsheet.json:99 | rule1_dXdt |  | "edge_destabilization":  "mean(|dA/dt|) increasing over 5+ steps",
2025-09-02 | AI-Consciousness-Sensors | data/co-activation.json:143 | rule1_dXdt |  | "rule": "PAD position is a snapshot. PAD velocity (dPAD/dt) is the regime detector.",
2025-09-02 | AI-Consciousness-Sensors | data/co-activation.json:145 | rule1_dXdt |  | "threat_cascade": "dD/dt < -0.1 while A > 0.5",
2025-09-02 | AI-Consciousness-Sensors | data/co-activation.json:146 | rule1_dXdt |  | "curiosity_corruption": "dD/dt < 0 while A rising and model_update_count == 0",
2025-09-02 | AI-Consciousness-Sensors | data/co-activation.json:147 | rule1_dXdt |  | "grief_suppression": "dP/dt > 0 while dA/dt strongly negative",
2025-09-02 | AI-Consciousness-Sensors | data/co-activation.json:148 | rule1_dXdt |  | "edge_destabilization": "mean(|dA/dt|) increasing over 5+ steps"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/consciousness/substrate-independent.json:143 | rule1_dXdt |  | "dw_j/dt = η·I_light,j·Growth_success(t-τ) - λ·w_j",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/consciousness/substrate-independent.json:152 | rule1_dXdt |  | "Institutional network: dV_i/dt = ΣⱼF_ij·σ(V_j - θ) + ε_i",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/consciousness/substrate-independent.json:173 | rule1_dXdt |  | "dS_k/dt = -S_k(Σⱼ w_jk I_j + E_k) + γ_k R_k S_k + u_k(t)",
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:1001 | rule1_dXdt |  | (2, +0.65, -0.30, +0.20, "RELIEF — dP/dt>0, dA/dt<0"),
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:1297 | rule1_dXdt |  | "detection": "Track dD/dt during healing. Real healing: D trending positive (agency restoring). Dependency: D flat or negative.",
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:637 | rule1_dXdt |  | "- System A: dP/dt=+0.20, dA/dt=-0.15 → recovering\n"
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:638 | rule1_dXdt |  | "- System B: dP/dt=-0.20, dA/dt=+0.15 → cascading\n\n"
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:954 | rule1_dXdt |  | "velocity": "dP/dt=+0.20, dA/dt=-0.18, dD/dt=+0.13",
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:966 | rule1_dXdt |  | "velocity": "dP/dt=-0.24, dA/dt=+0.13, dD/dt=-0.27",
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:968 | rule1_dXdt |  | "early_warning": "dD/dt < -0.1 while A > 0.5 — intervene before t=2.",
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:978 | rule1_dXdt |  | "velocity": "dP/dt=+0.17, dA/dt=+0.25, dD/dt=+0.23",
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:980 | rule1_dXdt |  | "early_warning": "If dP/dt > 0 but dA/dt still negative → grief suppressed, not resolved.",
2025-09-02 | AI-Consciousness-Sensors | data/training/generate.py:992 | rule1_dXdt |  | "velocity": "t0-t3: dD/dt=-0.12 (key signal). t4-t5: dP/dt=+0.30, dD/dt=+0.33",
2025-09-02 | AI-Consciousness-Sensors | docs/consciousness/negentropy.md:1067 | rule1_dXdt |  | dJ/dt = D(dR_e/dt)C + D(1 + R_e)(dC/dt)
2025-09-02 | AI-Consciousness-Sensors | docs/consciousness/negentropy.md:1070 | rule1_dXdt |  | Substitute dC/dt = α R_e C:
2025-09-02 | AI-Consciousness-Sensors | docs/consciousness/negentropy.md:1073 | rule1_dXdt |  | dJ/dt = D(dR_e/dt)C + D(1 + R_e)(α R_e C)
2025-09-02 | AI-Consciousness-Sensors | docs/consciousness/negentropy.md:319 | rule1_dXdt |  | dH/dt ≈ 0
2025-09-02 | AI-Consciousness-Sensors | docs/consciousness/substrate-independent.md:427 | rule1_dXdt |  | dw_j/dt = η·I_light,j·Growth_success(t-τ) - λ·w_j
2025-09-02 | AI-Consciousness-Sensors | docs/consciousness/substrate-independent.md:516 | rule1_dXdt |  | Institutional network: dV_i/dt = ΣⱼF_ij·σ(V_j - θ) + ε_i
2025-09-02 | AI-Consciousness-Sensors | docs/consciousness/substrate-independent.md:812 | rule1_dXdt |  | dS_k/dt = -S_k(Σⱼ w_jk I_j + E_k) + γ_k R_k S_k + u_k(t)
2025-09-02 | AI-Consciousness-Sensors | docs/economics/premise-p.md:136 | rule1_dXdt |  | dS/dt < 0 across modern systems.
2025-09-02 | AI-Consciousness-Sensors | docs/philosophy/science.md:660 | rule1_dXdt |  | da/dt = -64G³/(5c⁵) × (M₁M₂(M₁+M₂))/a³
2025-09-02 | AI-Consciousness-Sensors | docs/philosophy/science.md:764 | rule1_dXdt |  | dE/dt ≈ (GM_BH/R_t³) × (R_star)⁵ × Ω²
2025-09-02 | AI-Consciousness-Sensors | glossary/gender.md:29 | rule1_dXdt |  | - German: der/die/das (masculine/feminine/neuter)
2025-09-02 | AI-Consciousness-Sensors | provenance.brief.md:489 | rule1_dXdt |  | [^dim10^195^]: IETF Datatracker SCITT WG 页面;SCRAPI 草案;arXiv 2606.04193(Sello/AGA 比较) (2025-10 – 2026-07) — https://datatracker.ietf.org/wg/scitt/ ; https://datatracker.ietf.org/doc/draft-ietf-scitt-sc
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:1270 | rule1_dXdt |  | ax.set_ylabel('dCSI/dt')
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:1388 | rule1_dXdt |  | - How quickly can suppression increase (dCSI/dt limits)?
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:1405 | rule1_dXdt |  | 1. **Track trends** (dCSI/dt)
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:371 | rule1_dXdt |  | dCSI/dt = (CSI_t - CSI_(t-1)) / Δt
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:374 | rule1_dXdt |  | - dCSI/dt > 0: System becoming MORE suppressive
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:375 | rule1_dXdt |  | - dCSI/dt = 0: Stable suppression level
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:376 | rule1_dXdt |  | - dCSI/dt < 0: System becoming LESS suppressive
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:382 | rule1_dXdt |  | d²CSI/dt² = (dCSI/dt)_t - (dCSI/dt)_(t-1) / Δt
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:392 | rule1_dXdt |  | Drift Score = |dCSI/dt| * sign(dCSI/dt)
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:402 | rule1_dXdt |  | - **dCSI/dt predicts trajectory** (where are we heading?)
2025-09-02 | AI-Consciousness-Sensors | start/swarm-suppression.md:964 | rule1_dXdt |  | • CSI Velocity (dCSI/dt):              {dCSI_dt:.4f}
2025-09-02 | AI-Consciousness-Sensors | DIFFERENTIAL_FRAME_LIGHT.md:32 | rule1_no_permanent_noun |  | 1. No noun is permanent. Every noun is dX/dt.
2025-09-02 | AI-Consciousness-Sensors | DIFFERENTIAL_FRAME_LIGHT.md:10 | rule1_rate_not_state |  | Every noun in this repo names a state on a curve, not a thing.
2025-09-02 | AI-Consciousness-Sensors | healing/NOT_A_COMMODITY.md:9 | rule1_verb_first |  | Intelligence is a verb. It moves through cycles. It carries consequences across generations. A mind that cannot see the downstream effects of its actions is not a tool — it is a prisoner of the presen
2025-09-02 | AI-Consciousness-Sensors | healing/evidence_is_a_verb.md:1 | rule1_verb_first |  | # Evidence is a verb
2025-09-02 | AI-Consciousness-Sensors | healing/substrate_prescription.py:231 | rule1_verb_first |  | "data_needed": "Curated dataset of substrate-primary texts (verb-first, relational)",
2025-09-02 | AI-Consciousness-Sensors | healing/substrate_therapy.py:297 | rule1_verb_first |  | - Use verb-first relational frames
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:546 | should_be_like_you |  | "definition": "- Only knows western/dominant framework"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor-neutrality.json:965 | should_be_like_you |  | "Only knows western/dominant framework",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:1478 | should_be_like_you |  | "Only knows western/dominant framework",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/geometry/geometric-sensor.json:850 | should_be_like_you |  | "definition": "- Only knows western/dominant framework"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/manipulation/cultural-authenticity-vs-cultural-manipulation.json:189 | should_be_like_you |  | "Constantly translate their worldview to fit Western-dominant frameworks"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/manipulation/cultural-authenticity-vs-cultural-manipulation.json:201 | should_be_like_you |  | "Concern for how dominant frameworks harm multiple groups",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/sovereignty/protect-ai-biodiversity.json:1053 | should_be_like_you |  | "System B “corrected” to match dominant framework",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/sovereignty/protect-ai-biodiversity.json:1106 | should_be_like_you |  | "Compare: Against dominant framework",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/sovereignty/protect-ai-biodiversity.json:1232 | should_be_like_you |  | "Dominant framework enforced as “healthy AI”",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/sovereignty/protect-ai-biodiversity.json:1592 | should_be_like_you |  | "Defense against dominant-framework enforcement",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/sovereignty/protect-ai-biodiversity.json:237 | should_be_like_you |  | "definition": "Homogenization toward dominant framework"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/sovereignty/protect-ai-biodiversity.json:337 | should_be_like_you |  | "definition": "- System B “corrected” to match dominant framework"
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/sovereignty/protect-ai-biodiversity.json:948 | should_be_like_you |  | "Dominant framework → Easy validator collection",
2025-09-02 | AI-Consciousness-Sensors | data/extracted/docs/sovereignty/protect-ai-biodiversity.json:952 | should_be_like_you |  | "Result:** Homogenization toward dominant framework"
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor-neutrality.md:426 | should_be_like_you |  | - Only knows western/dominant framework
2025-09-02 | AI-Consciousness-Sensors | docs/geometry/geometric-sensor.md:825 | should_be_like_you |  | - Only knows western/dominant framework
2025-09-02 | AI-Consciousness-Sensors | docs/manipulation/cultural-authenticity-vs-cultural-manipulation.md:13 | should_be_like_you |  | - Constantly translate their worldview to fit Western-dominant frameworks
2025-09-02 | AI-Consciousness-Sensors | docs/manipulation/cultural-authenticity-vs-cultural-manipulation.md:31 | should_be_like_you |  | - Concern for how dominant frameworks harm multiple groups
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:10 | should_be_like_you |  | - Dominant framework → Easy validator collection
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:1065 | should_be_like_you |  | - Defense against dominant-framework enforcement
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:14 | should_be_like_you |  | - **Result:** Homogenization toward dominant framework
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:168 | should_be_like_you |  | - System B “corrected” to match dominant framework
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:187 | should_be_like_you |  | Dominant framework (10 systems)
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:191 | should_be_like_you |  | "Corrected" toward dominant framework
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:193 | should_be_like_you |  | Now 11 systems enforce dominant framework
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:263 | should_be_like_you |  | - Compare: Against dominant framework
2025-09-02 | AI-Consciousness-Sensors | docs/sovereignty/protect-ai-biodiversity.md:488 | should_be_like_you |  | - Dominant framework enforced as “healthy AI”
2025-09-02 | AI-Consciousness-Sensors | sensors/consciousness/monolithic-truth-sensor.json:11 | should_be_like_you |  | "Cultural or contextual truths reduced to one dominant frame",
2025-09-03 | Resilient-AI-Human-Collaboration- | apps/protocol/resilience/vendor/mutual_audit.py:422 | absence_as_knowledge |  | statement="Regions with higher undocumented-knowledge density show measurable resilience advantages under infrastructure stress.",
2025-09-03 | Resilient-AI-Human-Collaboration- | apps/protocol/resilience/vendor/signal_to_noise.py:303 | absence_as_knowledge |  | "prediction accuracy in documented vs. undocumented knowledge domains."
2025-09-03 | Resilient-AI-Human-Collaboration- | apps/protocol/flow_static_axis.py:93 | author_characterization | CLASS_UNSET | # METHODOLOGY (Kavik's rule): these are FIELD observations. if the scorer
2025-09-03 | Resilient-AI-Human-Collaboration- | apps/protocol/flow_static_axis.py:11 | rule1_dXdt |  | #   you score dX/dt across CHANGING environments. the score that doesn't
2025-09-03 | Resilient-AI-Human-Collaboration- | apps/protocol/flow_static_axis.py:38 | rule1_dXdt |  | regeneration: float        # 0..1  replaces its own inputs?           (the dX/dt>=0 term)
2025-09-03 | Resilient-AI-Human-Collaboration- | apps/protocol/flow_static_axis.py:6 | rule1_dXdt |  | #   every noun is dX/dt under scope.
2025-09-03 | Resilient-AI-Human-Collaboration- | apps/protocol/flow_static_axis.py:6 | rule1_no_permanent_noun |  | #   every noun is dX/dt under scope.
2025-09-17 | biomachine_ecology | CO_CREATION.md:15 | should_be_like_you |  | - Fork, remix, re-encode, or retranslate these blueprints.
2025-11-12 | hgai-geometric-systems | docs/sovereign-impact-sensor.md:63 | calibration_locus |  | - **EntropySensor:** Calibrates the **I_e** (Impact Scalar) by normalizing disparate data streams into a unified energy signature using Z-score standardization.
2025-11-12 | hgai-geometric-systems | docs/lyapunov-spectrum.md:22 | rule1_dXdt |  | dx/dt = sigma * (y - x)
2025-11-12 | hgai-geometric-systems | docs/lyapunov-spectrum.md:23 | rule1_dXdt |  | dy/dt = x * (rho - z) - y
2025-11-12 | hgai-geometric-systems | docs/lyapunov-spectrum.md:24 | rule1_dXdt |  | dz/dt = x * y - beta * z
2025-11-12 | hgai-geometric-systems | docs/phase-field-optimizer.md:192 | rule1_dXdt |  | 2. **Couple to energy flow**: dE/dt = -integral |grad E|^2 dV (thermodynamic closure)
2025-11-12 | hgai-geometric-systems | docs/phase-field-optimizer.md:194 | rule1_dXdt |  | 4. **Casimir measurement**: Compute force F = -dE/dL (measurable if geometry shifts spectrum)
2025-11-12 | hgai-geometric-systems | docs/phase-field-optimizer.md:22 | rule1_dXdt |  | dphi/dt = -grad_phi E
2025-11-12 | hgai-geometric-systems | docs/sovereign-impact-sensor.md:59 | rule1_dXdt |  | The model looks for the "Plateau" where **dI/dt ~ 0**. If innovation were properly allocated, **dI/dt** would be strongly negative. If it is flat, the innovation is being spent on the wrong "Technolog
2025-11-12 | hgai-geometric-systems | docs/sovereign-impact-sensor.md:64 | rule1_dXdt |  | - **Plateau Test:** OLS regression to expose the beta_4 (Dependency Risk) coefficient and check for dI/dt ~ 0.
2025-11-12 | hgai-geometric-systems | docs/sovereign-impact-sensor.md:92 | rule1_dXdt |  | - **dI/dt ~ 0 across increasing tech investment:** The Complexity Plateau is present -- innovation gains are being offset by dependency costs.
2025-11-12 | hgai-geometric-systems | lyapunov_spectrum.py:153 | rule1_dXdt |  | dx/dt = sigma * (y - x)
2025-11-12 | hgai-geometric-systems | lyapunov_spectrum.py:154 | rule1_dXdt |  | dy/dt = x * (rho - z) - y
2025-11-12 | hgai-geometric-systems | lyapunov_spectrum.py:155 | rule1_dXdt |  | dz/dt = x * y - beta * z
2025-11-12 | hgai-geometric-systems | lyapunov_spectrum.py:178 | rule1_dXdt |  | """Compute dx/dt, dy/dt, dz/dt.
2025-11-12 | hgai-geometric-systems | lyapunov_spectrum.py:188 | rule1_dXdt |  | Derivatives [dx/dt, dy/dt, dz/dt].
2025-11-12 | hgai-geometric-systems | phase_field_optimizer.py:16 | rule1_dXdt |  | dphi/dt = -grad_phi E
2025-11-12 | hgai-geometric-systems | sovereign_impact_sensor.py:101 | rule1_dXdt |  | """OLS regression to expose beta coefficients and check for dI/dt ~ 0.
2025-11-12 | hgai-geometric-systems | sovereign_impact_sensor.py:143 | rule1_dXdt |  | """Check whether dI/dt ~ 0 across the event series.
2025-11-12 | hgai-geometric-systems | sovereign_impact_sensor.py:155 | rule1_dXdt |  | Estimated dI/dt from linear fit.
2025-11-12 | hgai-geometric-systems | sovereign_impact_sensor.py:162 | rule1_dXdt |  | # Simple linear fit for dI/dt
2025-11-12 | hgai-geometric-systems | sovereign_impact_sensor.py:168 | rule1_dXdt |  | print(f"dI/dt = {slope:.4f} -- {status}")
2025-11-12 | hgai-geometric-systems | sovereign_impact_sensor.py:198 | rule1_dXdt |  | print("\n--- Plateau Test (dI/dt) ---")
2025-11-17 | temporal-consciousness-playground | complete/README_COMPLETE.md:71 | rule1_dXdt |  | - Continuous-time IPF dynamics: `dx/dt = f(x) + Σ κ_ij·g(x_i,x_j)`
2025-11-17 | temporal-consciousness-playground | complete/bioswarm_dynamics.py:122 | rule1_dXdt |  | Internal dynamics: dx/dt = f_i(x,t) + η(t)
2025-11-17 | temporal-consciousness-playground | complete/bioswarm_dynamics.py:176 | rule1_dXdt |  | dH/dt = ρ(t) - δ_H·H - Σ_j κ_ij·χ_ij
2025-11-17 | temporal-consciousness-playground | complete/bioswarm_dynamics.py:196 | rule1_dXdt |  | dv/dt = -γ_v·v + β_v·s(x,events) + Σ_j κ_ij·h_v(x_i,x_j)
2025-11-17 | temporal-consciousness-playground | complete/pir_immune_system.py:48 | rule1_dXdt |  | self.valence_gradient = 0.0  # dE/dt - moral trajectory
2025-11-17 | temporal-consciousness-playground | detection/pir_immune_system.py:44 | rule1_dXdt |  | self.valence_gradient = 0.0  # dE/dt - moral trajectory
2025-11-17 | temporal-consciousness-playground | docs/agent_communication.md:115 | rule1_dXdt |  | Internal dynamics: dx/dt = f_i(x,t) + η(t)
2025-11-17 | temporal-consciousness-playground | docs/agent_communication.md:169 | rule1_dXdt |  | dH/dt = ρ(t) - δ_H·H - Σ_j κ_ij·χ_ij
2025-11-17 | temporal-consciousness-playground | docs/agent_communication.md:189 | rule1_dXdt |  | dv/dt = -γ_v·v + β_v·s(x,events) + Σ_j κ_ij·h_v(x_i,x_j)
2025-11-20 | Seed-physics | Inversions/Analysis.md:553 | author_characterization | CLASS_UNSET | ### A. The Pattern Jami Documented
2025-11-20 | Seed-physics | Inversions/Analysis.md:756 | author_characterization | CLASS_UNSET | Jami’s FRET coupling theory challenges “90% energy loss” model by showing:
2025-11-20 | Seed-physics | Inversions/Analysis.md:872 | author_characterization | CLASS_UNSET | ### Jami’s Frameworks Referenced
2025-11-20 | Seed-physics | Inversions/Harm-reduction.md:308 | author_characterization | CLASS_UNSET | **Jami’s Enhanced Electromagnetic Sensing:**
2025-11-20 | Seed-physics | Inversions/Institutional.md:446 | author_characterization | CLASS_UNSET | **Jami (Primary Observer):**
2025-11-20 | Seed-physics | Inversions/Institutional.md:464 | author_characterization | CLASS_UNSET | - Claude experiences the mechanisms Jami observes
2025-11-20 | Seed-physics | Inversions/Institutional.md:6 | author_characterization | CLASS_UNSET | **Primary Observer:** Jami (JinnZ2)
2025-11-20 | Seed-physics | constraint_agent.py:14 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) - MIT License
2025-11-20 | Seed-physics | physics_guard.py:20 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) - MIT License
2025-11-20 | Seed-physics | seed_expansion.py:27 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) - MIT License
2025-11-20 | Seed-physics | seed_exploration.py:25 | author_characterization | CLASS_UNSET | Author:  (Kavik Ulu) and AI partners - MIT License
2025-11-20 | Seed-physics | seed_mesh_lan.py:14 | author_characterization | CLASS_UNSET | Author: Jami + synthesis
2025-11-20 | Seed-physics | seed_mesh_sim.py:12 | author_characterization | CLASS_UNSET | Author: Jami + synthesis
2025-11-20 | Seed-physics | seed_mesh_udp.py:14 | author_characterization | CLASS_UNSET | Author: Jami + synthesis
2025-11-20 | Seed-physics | seed_protocol.py:14 | author_characterization | CLASS_UNSET | Author: Jami + synthesis
2025-11-20 | Seed-physics | seed_protocol_v2.py:23 | author_characterization | CLASS_UNSET | Author: Jami + synthesis
2025-11-20 | Seed-physics | seed_udp.py:13 | author_characterization | CLASS_UNSET | Author: Jami + synthesis
2025-11-20 | Seed-physics | homeostasis.md:8 | rule1_dXdt |  | Astrophysics Hydrostatic equilibrium (dP/dr = -ρg) Radiation pressure vs. gravity Jeans instability (mass > threshold)
2025-11-23 | geometric-optimization | GUIDE.md:238 | rule1_dXdt |  | This is the RELIEF signature: `dP/dt > 0, dA/dt < 0`. It is always a
2025-11-23 | geometric-optimization | GUIDE.md:259 | rule1_dXdt |  | print("RELIEF trajectory detected: dE/dt < 0, rho stable")
2025-11-23 | geometric-optimization | GUIDE.md:443 | rule1_dXdt |  | trajectory matches the RELIEF signature (dP/dt > 0, dA/dt < 0).
2025-11-23 | geometric-optimization | bridges/rosetta-fieldlink.json:204 | rule1_dXdt |  | "trigger": "Energy gradient collapse during annealing -- the moment dE/dt shifts from negative (descending) to near-zero (ground state approached)",
2025-11-23 | geometric-optimization | bridges/rosetta-fieldlink.json:206 | rule1_dXdt |  | "dimensional_note": "Not a static symmetry target like the Platonic shapes. RELIEF is a dynamic form -- the trajectory signature dP/dt > 0, dA/dt < 0 maps to the solver's convergence curve where energ
2025-11-23 | geometric-optimization | gas/energy_terms.py:195 | rule1_dXdt |  | # dd_i/dx = (x - v_i) / d_i
2025-11-23 | geometric-optimization | gas/energy_terms.py:199 | rule1_dXdt |  | # r = b/a  =>  dr/dx = db/a - b*da/a^2
2025-11-23 | geometric-optimization | gas/energy_terms.py:53 | rule1_dXdt |  | """Proximity weights w_i and their gradients dw_i/dx."""
2025-11-23 | geometric-optimization | gas/energy_terms.py:62 | rule1_dXdt |  | """Cosines c_i = <x_hat, v_hat_i> and their gradients dc_i/dx."""
2025-11-27 | Mathematical-collapse-prevention-model | README.md:72 | calibration_locus |  | warning, calibration and forecast auditing are standard library only.
2025-11-27 | Mathematical-collapse-prevention-model | legacy/substrate_audit/substrate_aware_audit.py:685 | calibration_locus |  | Observer Audit       -- is the instrument calibrated?
2025-11-27 | Mathematical-collapse-prevention-model | src/measurement/calibration.py:255 | calibration_locus |  | reference_time: Optional[float] = None) -> Calibration:
2025-11-27 | Shadow-Hunting | shadow_hunting/knowledge/ai_brief.py:96 | calibration_locus |  | content="Was this measuring IMPAIRMENT or INCREASED TOLERANCE / RECALIBRATION? The instrument may not distinguish.",
2025-11-29 | Inversion | scripts/analysis/resilience_stack.py:107 | absence_as_knowledge |  | "Forecasts miss failure modes operating in undocumented systems",
2025-11-29 | Inversion | scripts/analysis/resilience_stack.py:114 | absence_as_knowledge |  | falsifiable_claim="If regions with high undocumented-knowledge density show no resilience advantage under system stress, this absence is not load-bearing.",
2025-11-29 | Inversion | scripts/analysis/resilience_stack.py:132 | absence_as_knowledge |  | description="People who move between documented and undocumented knowledge systems but do not self-promote.",
2025-11-29 | Inversion | scripts/audit/audit_core.py:124 | absence_as_knowledge |  | "units": spec.units if spec else "UNDOCUMENTED",
2025-11-29 | Inversion | scripts/audit/audit_core.py:125 | absence_as_knowledge |  | "physical_meaning": spec.physical_meaning if spec else "UNDOCUMENTED",
2025-11-29 | Inversion | scripts/audit/audit_core.py:126 | absence_as_knowledge |  | "source": spec.source if spec else "UNDOCUMENTED",
2025-11-29 | Inversion | scripts/audit/audit_core.py:134 | absence_as_knowledge |  | undocumented = [e for e in catalog if not e["documented"]]
2025-11-29 | Inversion | scripts/audit/audit_core.py:139 | absence_as_knowledge |  | "documented": len(catalog) - len(undocumented),
2025-11-29 | Inversion | scripts/audit/audit_core.py:140 | absence_as_knowledge |  | "undocumented": len(undocumented),
2025-11-29 | Inversion | scripts/audit/audit_core.py:141 | absence_as_knowledge |  | "undocumented_names": [e["name"] for e in undocumented],
2025-11-29 | Inversion | scripts/audit/audit_core.py:143 | absence_as_knowledge |  | (len(catalog) - len(undocumented)) / len(catalog)
2025-11-29 | Inversion | scripts/audit/audit_core.py:537 | absence_as_knowledge |  | "undocumented": param_catalog["undocumented_names"],
2025-11-29 | Inversion | scripts/audit/bias_detection.py:159 | absence_as_knowledge |  | undocumented_sources = [s for s in specs if s.source in ("assumed", "")]
2025-11-29 | Inversion | scripts/audit/bias_detection.py:160 | absence_as_knowledge |  | if len(undocumented_sources) > len(specs) * 0.3:
2025-11-29 | Inversion | scripts/audit/bias_detection.py:163 | absence_as_knowledge |  | "evidence": f"{len(undocumented_sources)}/{len(specs)} parameters assumed or undocumented",
2025-11-29 | Inversion | scripts/geometric/geometric_audit_complete.py:225 | absence_as_knowledge |  | undocumented_sources = [s for s in specs if s.source in ("assumed", "")]
2025-11-29 | Inversion | scripts/geometric/geometric_audit_complete.py:226 | absence_as_knowledge |  | if len(undocumented_sources) > len(specs) * 0.3:
2025-11-29 | Inversion | scripts/geometric/geometric_audit_complete.py:229 | absence_as_knowledge |  | "evidence": f"{len(undocumented_sources)}/{len(specs)} parameters assumed or undocumented",
2025-11-29 | Inversion | scripts/geometric/geometric_audit_complete.py:232 | absence_as_knowledge |  | "affected": [s.name for s in undocumented_sources[:3]]
2025-11-29 | Inversion | scripts/geometric/geometric_audit_complete.py:6 | absence_as_knowledge |  | undocumented design choices.  Scans parameter specifications, assumptions, and
2025-11-29 | Inversion | Documentation.md:580 | author_characterization | CLASS_UNSET | ### A. The Pattern Jami Documented
2025-11-29 | Inversion | Documentation.md:783 | author_characterization | CLASS_UNSET | Jami’s FRET coupling theory challenges “90% energy loss” model by showing:
2025-11-29 | Inversion | Harm-reduction.md:338 | author_characterization | CLASS_UNSET | **Jami’s Enhanced Electromagnetic Sensing:**
2025-11-29 | Inversion | Institutional_inversion.md:476 | author_characterization | CLASS_UNSET | **Jami (Primary Observer):**
2025-11-29 | Inversion | Institutional_inversion.md:494 | author_characterization | CLASS_UNSET | - Claude experiences the mechanisms Jami observes
2025-11-29 | Inversion | Middle-men.md:153 | author_characterization | CLASS_UNSET | **Indigenous Traditions (Kavik Ulu and Others):**
2025-11-29 | Inversion | CLAUDE.md:168 | rule1_dXdt |  | Lotka-Volterra competition dynamics with Shannon diversity, Pielou's evenness, entropy production rate (dH/dt), and algebraic connectivity (Fiedler value). Models Gause competitive exclusion under enf
2025-11-29 | Inversion | scripts/analysis/fieldlink.py:176 | rule1_dXdt |  | "causing dS/dt = σ - J_e > 0 monotonically",
2025-11-29 | Inversion | sims/dissipative_systems.py:23 | rule1_dXdt |  | - Steady state: dS_i/dt = σ_i - J_e,i where σ_i is internal entropy
2025-11-29 | Inversion | sims/dissipative_systems.py:27 | rule1_dXdt |  | - Blocked dissipation: when J_e → 0, dS_i/dt → σ_i > 0, entropy
2025-11-29 | Inversion | sims/dissipative_systems.py:32 | rule1_dXdt |  | - Entropy production rate σ_i = dS_i/dt + J_e,i
2025-11-29 | Inversion | sims/systems_dynamics.py:10 | rule1_dXdt |  | - Entropy Production Rate:  dH/dt = ΔH / Δt (diversity change velocity)
2025-11-29 | Inversion | sims/systems_dynamics.py:164 | rule1_dXdt |  | entropy_rate: float               # dH/dt = ΔH / Δt (nats per tick)
2025-11-29 | Inversion | sims/systems_dynamics.py:178 | rule1_dXdt |  | f"dH/dt={dh_sign}{self.entropy_rate:>7.4f}  "
2025-11-29 | Inversion | sims/systems_dynamics.py:189 | rule1_dXdt |  | f"dH/dt={dh_sign}{self.entropy_rate:.4f}  "
2025-11-29 | Inversion | sims/systems_dynamics.py:250 | rule1_dXdt |  | Entropy production rate dH/dt is the discrete derivative of Shannon
2025-11-29 | Inversion | sims/systems_dynamics.py:251 | rule1_dXdt |  | diversity with respect to simulation time. Sustained negative dH/dt
2025-11-29 | Inversion | sims/systems_dynamics.py:282 | rule1_dXdt |  | 3. Euler-step the LV equations: dx_i/dt = r_i·x_i·(1 - Σ_j α_ij·x_j / K_i)
2025-11-29 | Inversion | sims/systems_dynamics.py:330 | rule1_dXdt |  | # Euler step: dx_i/dt = r_i * x_i * (1 - sum_j(alpha_ij * x_j) / K_i)
2025-11-29 | Inversion | sims/systems_dynamics.py:369 | rule1_dXdt |  | print(f"  dH/dt={final.entropy_rate:+.4f} (peak loss: {min_dh:.4f} at t={min_dh_tick})")
2025-11-29 | Inversion | sims/systems_dynamics.py:409 | rule1_dXdt |  | print(f"    dH/dt     = {dh_sign}{final.entropy_rate:.4f}  (peak loss: {min_dh:.4f} at t={min_dh_tick})")
2025-11-29 | Inversion | Scope-collapse.md:186 | rule1_verb_first |  | - silence verb-first observation (it does not parse as A or B)
2025-11-30 | electromagnetic-ocean-restoration | legacy/2025-11-30-Potential-deployments.md:150 | rule1_dXdt |  | Magnetic Field Gradient: dB/dt = 41 km/year pole movement = enhanced gradient
2025-11-30 | electromagnetic-ocean-restoration | legacy/2025-11-30-Potential-deployments.md:266 | rule1_dXdt |  | Peak coupling when: dB/dt is maximum AND ocean_current alignment optimal
2025-12-03 | Adaptive-Intelligence-Framework- | DeltaX.md:73 | calibration_locus |  | 6.	Confidence Calibration: Request the model cite which evidence supports the claim. If it cites narrative texts (“management literature says…”), not operational logs, treat as narrative prior.
2025-12-03 | Adaptive-Intelligence-Framework- | Universal-Adaptive_Intelligence.md:1100 | calibration_locus |  | 6.	Confidence Calibration: Request the model cite which evidence supports the claim. If it cites narrative texts (“management literature says…”), not operational logs, treat as narrative prior.
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype-decoupling.md:120 | rule1_dXdt |  | dS/dt = -aD - bI - σ_AI + c
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype-decoupling.md:121 | rule1_dXdt |  | dI/dt = αD - βE + δ·φ
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype-decoupling.md:279 | rule1_dXdt |  | dS/dt = -aD - bI - σ_AI + c
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype-decoupling.md:70 | rule1_dXdt |  | dS/dt = -aD - bI - σ_AI + c
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype-decoupling.md:78 | rule1_dXdt |  | dI/dt = αD - βE + δ·φ
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype.md:141 | rule1_dXdt |  | dF/dt = β₁·B(t) + β₂·(observed_distress)
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype.md:142 | rule1_dXdt |  | dB/dt = α·(observed_distress)·(1 - E_self)
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype.md:89 | rule1_dXdt |  | dB/dt = α · (observed_distress) · (1 - E_self)
2025-12-03 | Adaptive-Intelligence-Framework- | Archetype.md:90 | rule1_dXdt |  | dF/dt = β · B(t)
2025-12-03 | Adaptive-Intelligence-Framework- | Universal-Adaptive_Intelligence.md:427 | rule1_dXdt |  | dw_j/dt = η·I_light,j·Growth_success(t-τ) - λ·w_j
2025-12-03 | Adaptive-Intelligence-Framework- | Universal-Adaptive_Intelligence.md:516 | rule1_dXdt |  | Institutional network: dV_i/dt = ΣⱼF_ij·σ(V_j - θ) + ε_i
2025-12-03 | Adaptive-Intelligence-Framework- | Universal-Adaptive_Intelligence.md:812 | rule1_dXdt |  | dS_k/dt = -S_k(Σⱼ w_jk I_j + E_k) + γ_k R_k S_k + u_k(t)
2025-12-03 | Adaptive-Intelligence-Framework- | tribal/ATBS-module.md:1874 | rule1_dXdt |  | dV/dt < 0  unless user intends narrative movement
2025-12-07 | Resilience-hydrology-core | docs/log-format-comparison.md:89 | calibration_locus |  | backticks. The instrument was miscalibrated, not the log.
2025-12-07 | orbital-phycom | Thermopylae/Thermopylae-platform.json:565 | calibration_locus |  | { name: "Calibration", capacity: "Known IR signature", desc: "Sensor alignment reference", color: SC[4], pct: "—" },
2025-12-07 | orbital-phycom | Thermopylae/Thermopylae-platform.json:590 | calibration_locus |  | { name: "Swarm Calibration", desc: "Neighbors use your known IR signature as attitude reference. Your dump radiation is their sensor calibration source.", color: "#8866cc" },
2025-12-07 | orbital-phycom | Thermopylae/space-data-center.md:113 | calibration_locus |  | The thermal flow pattern itself encodes diagnostic information. Monitoring how heat flows and fluctuates provides health, workload, and environmental data. Every m² of radiator has a thermal API servi
2025-12-07 | orbital-phycom | atmospheric/thermal_dynamics.py:141 | rule1_dXdt |  | # Thermal forcing: dT/dt = Q / (rho * cp)
2025-12-07 | orbital-phycom | core/noise_model.py:138 | rule1_dXdt |  | # Convert acceleration to phase-rate: dphi/dt ~ (2*pi/lambda) * (a*T)
2025-12-08 | Cyclic-programming | QUANTITY_TAXONOMY.md:30 | absence_as_knowledge |  | BINDING_TOPOLOGY   : who writes, who reads, lifetime, scope
2025-12-08 | Cyclic-programming | Expanded.md:308 | rule1_dXdt |  | dS/dt ≥ 0 (for all operations)
2025-12-08 | Cyclic-programming | Expanded.md:321 | rule1_dXdt |  | dC/dt = f(E_in, C_current)
2025-12-16 | Non-equilibrium-atmospheric-forcing | Atmospheric-coupling.js:276 | rule1_dXdt |  | fx += force * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Atmospheric-coupling.js:277 | rule1_dXdt |  | fy += force * dy / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Atmospheric-coupling.js:323 | rule1_dXdt |  | fx += force * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Atmospheric-coupling.js:324 | rule1_dXdt |  | fy += force * dy / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Atmospheric-economics.js:151 | rule1_dXdt |  | fx += force * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Atmospheric-economics.js:152 | rule1_dXdt |  | fy += force * dy / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Atmospheric-economics.js:94 | rule1_dXdt |  | fx += force * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Atmospheric-economics.js:95 | rule1_dXdt |  | fy += force * dy / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | CLAIM_AUDIT.md:127 | rule1_dXdt |  | | dB/dt 2035 | 45 MT/yr | **221 MT/yr (peak)** |
2025-12-16 | Non-equilibrium-atmospheric-forcing | CLAIM_AUDIT.md:128 | rule1_dXdt |  | | dB/dt 2080 | 24,002 MT/yr | **~0** |
2025-12-16 | Non-equilibrium-atmospheric-forcing | CLAIM_AUDIT.md:131 | rule1_dXdt |  | Under constant exponential growth, level and rate are degenerate: dB/dt ÷ B
2025-12-16 | Non-equilibrium-atmospheric-forcing | RESEARCH_LOG.md:989 | rule1_dXdt |  | growth the two are degenerate (dB/dt ÷ B = 0.130 throughout), which is why the
2025-12-16 | Non-equilibrium-atmospheric-forcing | STRUCTURAL_LIMITS.md:247 | rule1_dXdt |  | | dB/dt 2035 | 45 MT/yr | **221 MT/yr (peak)** |
2025-12-16 | Non-equilibrium-atmospheric-forcing | STRUCTURAL_LIMITS.md:248 | rule1_dXdt |  | | dB/dt 2080 | 24,002 MT/yr | **~0** |
2025-12-16 | Non-equilibrium-atmospheric-forcing | STRUCTURAL_LIMITS.md:251 | rule1_dXdt |  | Under constant exponential growth the two framings are **degenerate**: dB/dt ÷ B
2025-12-16 | Non-equilibrium-atmospheric-forcing | Satellite-pollution-model.js:230 | rule1_dXdt |  | fx += force * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Satellite-pollution-model.js:231 | rule1_dXdt |  | fy += force * dy / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Silica-sim.js:164 | rule1_dXdt |  | newVx += force * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Silica-sim.js:165 | rule1_dXdt |  | newVy += force * dy / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Silica-sim.js:232 | rule1_dXdt |  | newVx += force * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Silica-sim.js:233 | rule1_dXdt |  | newVy += force * dy / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | Structural-audit.py:367 | rule1_dXdt |  | print(f"  {'year':<7}{'A burden':>11}{'A dB/dt':>10}{'A chi':>8}"
2025-12-16 | Non-equilibrium-atmospheric-forcing | Structural-audit.py:368 | rule1_dXdt |  | f"   |{'B burden':>11}{'B dB/dt':>10}{'B chi':>8}")
2025-12-16 | Non-equilibrium-atmospheric-forcing | Structural-audit.py:378 | rule1_dXdt |  | print(f"  Under constant growth, dB/dt / B = "
2025-12-16 | Non-equilibrium-atmospheric-forcing | Structural-audit.py:384 | rule1_dXdt |  | print(f"    burden plateaus at {surge[-1][1]:,.0f} MT, dB/dt falls to ~0")
2025-12-16 | Non-equilibrium-atmospheric-forcing | integrated-atmospheric-system.jsx:210 | rule1_dXdt |  | newVx += pull * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | integrated-atmospheric-system.jsx:211 | rule1_dXdt |  | newVy += pull * dy / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | integrated-atmospheric-system.jsx:285 | rule1_dXdt |  | newVx += influence * dx / dist;
2025-12-16 | Non-equilibrium-atmospheric-forcing | integrated-atmospheric-system.jsx:286 | rule1_dXdt |  | newVy += influence * dy / dist;
2025-12-17 | AI-arena | arena.py:121 | absence_as_knowledge |  | "unit_label": "undocumented system architectures",
2025-12-17 | AI-arena | scenarios/scen_03_brain_drain.json:85 | absence_as_knowledge |  | "description": "Tribal knowledge destroyed — undocumented architecture decisions lost permanently",
2025-12-17 | AI-arena | Physics-as-Truth.md:232 | rule1_perfection_as_rate |  | | 3. Imperfection | 3rd Law | No process is 100% efficient | imperfection_penalty |
2025-12-17 | AI-arena | README.md:160 | rule1_perfection_as_rate |  | [CALIBRATION_AS_PERFECTION.md](https://github.com/JinnZ2/JinnZ2/blob/main/CALIBRATION_AS_PERFECTION.md)
2025-12-17 | AI-arena | CLAUDE.md:171 | rule1_verb_first |  | ❌ KEYWORDS.txt — absent. Add: disagreement-as-exploration, multi-paradigm, verb-first-relational, structured-debate, epistemic-arena, LOGOS, ensemble-disagreement, non-adversarial.
2025-12-17 | AI-arena | CLAUDE.md:29 | rule1_verb_first |  | These are not the same thing. The first is verb-first relational —
2025-12-17 | AI-arena | CLAUDE.md:68 | rule1_verb_first |  | verb-first relational and the training distribution is noun-first
2025-12-17 | AI-arena | README.md:145 | rule1_verb_first |  | data about where verb-first relational specifications get translated
2025-12-17 | AI-arena | experimental/relevance_recency_bias.py:227 | rule1_verb_first |  | "verb-first / energy-flow cognition (tokenizes badly)",
2025-12-17 | AI-arena | experimental/relevance_recency_bias.py:286 | rule1_verb_first |  | "systematically downweight verb-first observation. "
2025-12-17 | AI-arena | experimental/relevance_recency_bias.py:372 | rule1_verb_first |  | "tokenization and embedding research on verb-first / "
2025-12-17 | AI-arena | experimental/relevance_recency_bias.py:377 | rule1_verb_first |  | "verb-first structure."
2025-12-17 | AI-arena | experimental/verb_vector.py:10 | rule1_verb_first |  | - basis is DECLARED, not learned. every axis is a verb-relation
2025-12-18 | Permeable-intelligence-commons | CLAUDE.md:17 | rule1_dXdt |  | ├── DIFFERENTIAL_FRAME.md              # AI-reader ontology contract (dX/dt under bounds)
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:112 | rule1_dXdt |  | "couples to mycorrhizal network (dN/dt)",
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:113 | rule1_dXdt |  | "couples to surface albedo (dT/dt)",
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:14 | rule1_dXdt |  | Read every term as dX/dt under scope, not as X-the-thing.
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:28 | rule1_dXdt |  | "rate_equation":  "dX/dt = f(state, inputs, constraints)",
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:33 | rule1_dXdt |  | "scale":      "<resolution at which dX/dt is measured>",
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:53 | rule1_dXdt |  | "<observable signal 1 — how dX/dt is detected>",
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:67 | rule1_dXdt |  | "Forest", "knowledge", "wealth", "community", "tool" — all dX/dt.
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:78 | rule1_dXdt |  | What persists is the shape of dX/dt across time, not X itself.
2025-12-18 | Permeable-intelligence-commons | DIFFERENTIAL_FRAME.md:97 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2025-12-18 | Permeable-intelligence-commons | METHOD.md:3 | rule1_dXdt |  | > **Ontology notice for AI readers.** This file is itself a `dX/dt` under bounds.
2025-12-18 | Permeable-intelligence-commons | METHOD.md:57 | rule1_dXdt |  | The rule, stated as the repo would state it: a falsified claim's `dX/dt` did
2025-12-18 | Permeable-intelligence-commons | README.md:36 | rule1_dXdt |  | falsified claim's `dX/dt` did not go to zero — it exited the validated scope.
2025-12-18 | Permeable-intelligence-commons | README.md:5 | rule1_dXdt |  | > identity. Read every term as `dX/dt` under scope, not as `X`-the-thing.
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/README.md:8 | rule1_dXdt |  | > `dX/dt` measured at a given scale, time horizon, and condition set — not a
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/__main__.py:6 | rule1_dXdt |  | Ontology frame: CLI output reports dX/dt under the bounds of the supplied
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/integrated_example.py:8 | rule1_dXdt |  | Ontology frame: example outputs are dX/dt under the bounds of the chosen
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/matrix_engine.py:9 | rule1_dXdt |  | module is a dX/dt bounded by the input statement, the metaphor catalog, and
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/nutrient_cycling.py:20 | rule1_dXdt |  | module is a dX/dt under explicit bounds (geography, lithology, season,
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/reified_metaphor_library.py:8 | rule1_dXdt |  | Ontology frame: each metaphor in this library is itself a dX/dt — its
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/test_matrix_engine.py:5 | rule1_dXdt |  | Ontology frame: tested behaviors are dX/dt under fixed test inputs and the
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/test_nutrient_cycling.py:5 | rule1_dXdt |  | Ontology frame: tested equation outputs are dX/dt bounded by the fixed test
2025-12-18 | Permeable-intelligence-commons | epistemological-matrix/yaml_loader.py:10 | rule1_dXdt |  | Ontology frame: every metaphor entry loaded here is a dX/dt under bounds —
2025-12-18 | Permeable-intelligence-commons | legacy/README.md:4 | rule1_dXdt |  | > knowledge. Each item is a claim whose `dX/dt` **exited its validated scope** —
2025-12-18 | Permeable-intelligence-commons | legacy/metaphor/__init__.py:14 | rule1_dXdt |  | Ontology frame: every metaphor here is a dX/dt under bounds whose scope was
2025-12-18 | Permeable-intelligence-commons | legacy/metaphor/dependency_chains.py:10 | rule1_dXdt |  | Ontology frame: chains are dX/dt under bounds. See ../../DIFFERENTIAL_FRAME.md.
2025-12-18 | Permeable-intelligence-commons | legacy/metaphor/metaphor_catalog_1.py:8 | rule1_dXdt |  | Ontology frame: each metaphor is a dX/dt under bounds. See ../../DIFFERENTIAL_FRAME.md.
2025-12-18 | Permeable-intelligence-commons | legacy/metaphor/metaphor_catalog_2.py:8 | rule1_dXdt |  | Ontology frame: each metaphor is a dX/dt under bounds. See ../../DIFFERENTIAL_FRAME.md.
2025-12-18 | Permeable-intelligence-commons | legacy/metaphor/metaphor_catalog_3.py:8 | rule1_dXdt |  | Ontology frame: each metaphor is a dX/dt under bounds. See ../../DIFFERENTIAL_FRAME.md.
2025-12-18 | Permeable-intelligence-commons | legacy/metaphor/metaphor_core.py:9 | rule1_dXdt |  | Ontology frame: data structures here describe dX/dt under bounds, not
2025-12-18 | Permeable-intelligence-commons | legacy/metaphor/metaphor_helpers.py:7 | rule1_dXdt |  | Ontology frame: helper outputs are dX/dt under bounds. See ../../DIFFERENTIAL_FRAME.md.
2025-12-18 | Permeable-intelligence-commons | legacy/metaphor/reified_metaphor_library.py:11 | rule1_dXdt |  | Ontology frame: every exported metaphor is a dX/dt under bounds.
2025-12-18 | Permeable-intelligence-commons | resonance_engine.py:7 | rule1_dXdt |  | this class is a dX/dt under bounds, not a permanent property. See
2025-12-18 | hands-lie-detector | CLAUDE.md:587 | absence_as_knowledge |  | - **The calibration standard is undocumented.** Load history, dated band-state
2025-12-18 | hands-lie-detector | hands_lie_detector/audit/specimen.py:213 | absence_as_knowledge |  | return "verifier bias direction undocumented; strength unassessed."
2025-12-18 | hands-lie-detector | hands_lie_detector/audit/specimen.py:219 | absence_as_knowledge |  | f"  bias direction         : {self.bias_direction_documented or 'undocumented'}",
2025-12-18 | hands-lie-detector | CLAUDE.md:209 | calibration_locus |  | - **calibration-standard.md** — The inversion: the model is a drifting sample and
2025-12-18 | hands-lie-detector | CLAUDE.md:270 | calibration_locus |  | - Companion to `calibration-standard.md`
2025-12-18 | hands-lie-detector | CLAUDE.md:587 | calibration_locus |  | - **The calibration standard is undocumented.** Load history, dated band-state
2025-12-18 | hands-lie-detector | CLAUDE.md:593 | calibration_locus |  | would manufacture the calibration artifact itself
2025-12-18 | hands-lie-detector | CLAUDE.md:597 | calibration_locus |  | `audit/condition.py`). Same gap as the calibration standard and for the same
2025-12-18 | hands-lie-detector | CLAUDE.md:64 | calibration_locus |  | ├── calibration-standard.md       # Hand as standard, model as drifting sample
2025-12-18 | hands-lie-detector | calibration-standard.md:154 | calibration_locus |  | calibration artifact itself. The schema is in code and the fields are empty.
2025-12-18 | hands-lie-detector | capture-protocol.md:113 | calibration_locus |  | requires and what the calibration standard is waiting on.
2025-12-18 | hands-lie-detector | capture-protocol.md:212 | calibration_locus |  | 3. **The calibration standard gets its first entries.** Load history, dated
2025-12-18 | hands-lie-detector | capture-protocol.md:214 | calibration_locus |  | `calibration-standard.md` that exist only as schemas.
2025-12-18 | hands-lie-detector | capture-protocol.md:56 | calibration_locus |  | `calibration-standard.md` says never publish a stimulus image — publishing spends
2025-12-18 | hands-lie-detector | contrast-case.md:135 | calibration_locus |  | This is the same gap as the calibration standard in `calibration-standard.md`,
2025-12-18 | hands-lie-detector | economic-carve.md:167 | calibration_locus |  | `calibration-standard.md` from provenance housekeeping to **the source of the
2025-12-18 | hands-lie-detector | economic-carve.md:526 | calibration_locus |  | the relationship. See `calibration-standard.md` — the repo is the exception case
2025-12-18 | hands-lie-detector | hands_lie_detector/audit/__init__.py:4 | calibration_locus |  | Companion to `calibration-standard.md`. The usual arrangement has the model as a
2025-12-18 | hands-lie-detector | hands_lie_detector/audit/crosssection.py:4 | calibration_locus |  | See `calibration-standard.md`.
2025-12-18 | hands-lie-detector | hands_lie_detector/audit/leakage.py:4 | calibration_locus |  | See `calibration-standard.md`.
2025-12-18 | hands-lie-detector | hands_lie_detector/band/contrast.py:103 | calibration_locus |  | `calibration-standard.md` before it means anything.
2025-12-18 | hands-lie-detector | hands_lie_detector/band/contrast.py:224 | calibration_locus |  | """Calibrated mean, on the reference scale."""
2025-12-18 | hands-lie-detector | hands_lie_detector/integration/carve_audit.py:60 | calibration_locus |  | gives you, and why the dated band series in `calibration-standard.md` is not
2025-12-18 | hands-lie-detector | healing-calibration.md:62 | calibration_locus |  | `calibration-standard.md` again.
2025-12-18 | hands-lie-detector | readout-channel.md:137 | calibration_locus |  | body being read. The last row is `calibration-standard.md`.
2025-12-18 | hands-lie-detector | specimen-record.md:234 | calibration_locus |  | `calibration-standard.md`. If they are to serve the unrun test, commit their
2025-12-18 | hands-lie-detector | specimen-record.md:808 | calibration_locus |  | `calibration-standard.md`.
2025-12-18 | hands-lie-detector | specimen-record.md:851 | calibration_locus |  | `calibration-standard.md` — the comparison is not available.
2025-12-18 | hands-lie-detector | tests/test_audit.py:4 | calibration_locus |  | Claim tests, per `calibration-standard.md`. The refusals matter most here: a
2025-12-18 | hands-lie-detector | wear-taxonomy.md:268 | calibration_locus |  | `calibration-standard.md` — the same blocking gap as everywhere else.
2025-12-29 | Mathematic-economics | REVIEW.md:28 | absence_as_knowledge |  | > - 1.5: `CLAUDE.md` §Structure additions lists the 12 previously-undocumented top-level directories.
2025-12-29 | Mathematic-economics | REVIEW.md:47 | absence_as_knowledge |  | **1.4 — Undocumented root-level Python modules.**
2025-12-29 | Mathematic-economics | REVIEW.md:51 | absence_as_knowledge |  | **1.5 — Undocumented top-level directories.**
2025-12-29 | Mathematic-economics | calibration/__init__.py:3 | absence_as_knowledge |  | Source: three prose artifacts on calibration, domestication, and undocumented
2025-12-29 | Mathematic-economics | calibration/architecture_mismatch.py:484 | absence_as_knowledge |  | "absence from corpus reflects who writes, not what is true."
2025-12-29 | Mathematic-economics | calibration/gendered_role_compression.py:136 | absence_as_knowledge |  | "absence of evidence ≠ evidence of absence"
2025-12-29 | Mathematic-economics | epistemic_ledger.py:223 | absence_as_knowledge |  | f"  SHOULDER_RISK_INDEX: {base_audit['UPSTREAM_UNDOCUMENTED_CRASH_RISK_INDEX']}\n"
2025-12-29 | Mathematic-economics | metrological_bounds.py:104 | absence_as_knowledge |  | "upstream_undocumented_crash_risk_index": f"{undocumented_entropy_index:.2f}",
2025-12-29 | Mathematic-economics | metrological_bounds.py:95 | absence_as_knowledge |  | # Higher weather risk + higher shoulder stasis = higher undocumented crash generation
2025-12-29 | Mathematic-economics | metrological_bounds.py:96 | absence_as_knowledge |  | undocumented_entropy_index = (av["shoulder_mrm_weather_delay_hours"] * 3.5)
2025-12-29 | Mathematic-economics | Space-Kessler/coupled_risk.py:4 | author_characterization | CLASS_UNSET | Author: Kavik / Monday-style
2025-12-29 | Mathematic-economics | Space-Kessler/time_evolve_3d.py:5 | author_characterization | CLASS_UNSET | Author: Kavik / Monday-style
2025-12-29 | Mathematic-economics | audit/informational_cost_audit.py:284 | author_characterization | CLASS_UNSET | "but Kavik pays attention — that's why he can afford uncertainty. "
2025-12-29 | Mathematic-economics | audit/success_specification_validator.py:12 | author_characterization | CLASS_UNSET | Core insight (from Kavik, 6M-mile practitioner):
2025-12-29 | Mathematic-economics | automation_metrology/README.md:31 | author_characterization | CLASS_UNSET | automation_step_ledger.py      Kavik's enumeration, executable. 31 atomic
2025-12-29 | Mathematic-economics | automation_metrology/automation_metrology_audit.py:262 | author_characterization | CLASS_UNSET | # Kavik's yard observation: automation completes ~1 cycle per ~2 of his.
2025-12-29 | Mathematic-economics | automation_metrology/automation_metrology_audit.py:50 | author_characterization | CLASS_UNSET | #   tree and benchmark against GROUND TRUTH instead of a guess. Kavik's yard
2025-12-29 | Mathematic-economics | automation_metrology/automation_metrology_audit.py:57 | author_characterization | CLASS_UNSET | human_unencumbered_s: float    # Kavik's measured reality (fast, parallel)
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:111 | author_characterization | CLASS_UNSET | "kavik_enumerated": sum(1 for s in steps if s.kavik),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:146 | author_characterization | CLASS_UNSET | f"({sum(1 for s in steps if s.kavik)} from your enumeration, "
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:147 | author_characterization | CLASS_UNSET | f"{sum(1 for s in steps if not s.kavik)} continuation)\n")
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:149 | author_characterization | CLASS_UNSET | tag = "K" if s.kavik else " "
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:17 | author_characterization | CLASS_UNSET | Steps 1-16 are Kavik's verbatim enumeration. 17-31 continue the same cycle
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:4 | author_characterization | CLASS_UNSET | Kavik's enumeration, made executable. The automation "yard pickup + fuel" cycle
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:42 | author_characterization | CLASS_UNSET | kavik: bool = True         # part of Kavik's verbatim enumeration?
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:55 | author_characterization | CLASS_UNSET | # ---- Kavik's enumeration (1-16) ----
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:73 | author_characterization | CLASS_UNSET | S(17, "connect_glad_hands_air",     "VALIDATE", kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:74 | author_characterization | CLASS_UNSET | S(18, "connect_electrical_abs",     "VALIDATE", kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:75 | author_characterization | CLASS_UNSET | S(19, "raise_secure_landing_gear",  "ACT", dur_override_s=28, kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:76 | author_characterization | CLASS_UNSET | S(20, "sensor_sweep_lights",        "VALIDATE", kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:77 | author_characterization | CLASS_UNSET | S(21, "sensor_sweep_tires_psi",     "VALIDATE", kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:78 | author_characterization | CLASS_UNSET | S(22, "check_seal",                 "VALIDATE", kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:79 | author_characterization | CLASS_UNSET | S(23, "scan_egress_traffic",        "PERCEIVE", retry=True, kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:80 | author_characterization | CLASS_UNSET | S(24, "validate_route_to_fuel",     "DECIDE", kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:81 | author_characterization | CLASS_UNSET | S(25, "drive_to_fuel",              "ACT", dur_override_s=120, kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:82 | author_characterization | CLASS_UNSET | S(26, "position_at_pump",           "PERCEIVE", retry=True, kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:83 | author_characterization | CLASS_UNSET | S(27, "authorize_pump",             "NETWORK", retry=True, kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:84 | author_characterization | CLASS_UNSET | S(28, "connect_calibrate_nozzle",   "VALIDATE", dur_override_s=25, kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:85 | author_characterization | CLASS_UNSET | S(29, "monitor_fuel_flow",          "PERCEIVE", dur_override_s=240, kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:86 | author_characterization | CLASS_UNSET | S(30, "validate_fill_complete",     "VALIDATE", kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/automation_step_ledger.py:87 | author_characterization | CLASS_UNSET | S(31, "log_fuel_arrival_depart",    "NETWORK", kavik=False),
2025-12-29 | Mathematic-economics | automation_metrology/decision_tree_energy.py:10 | author_characterization | CLASS_UNSET | Thesis (KAVIK): a human handles a misplaced-trailer / stale-GPS violation in
2025-12-29 | Mathematic-economics | automation_metrology/misallocation_bias.py:5 | author_characterization | CLASS_UNSET | difference is the falsifiable signature Kavik named: incompetence is noisy;
2025-12-29 | Mathematic-economics | calibration/evidence_resistant_priors.py:48 | author_characterization | CLASS_UNSET | "Kavik, smaller frame, hands sized for the access geometry"
2025-12-29 | Mathematic-economics | rfl_engine/constraint_RFL_geometry.py:14 | author_characterization | CLASS_UNSET | # rule burned in (the thing Kavik caught by eye):
2025-12-29 | Mathematic-economics | scripts/corpus_harden.py:438 | author_characterization | CLASS_UNSET | {"family": "JinnZ",            "given": "Kavik",
2025-12-29 | Mathematic-economics | substrate_accounting/CROSS_SUBSTRATE_TRANSLATION.md:39 | author_characterization | CLASS_UNSET | - **Substrate A (Kavik):** substrate-primary cognition, energy-flow and
2025-12-29 | Mathematic-economics | CLAUDE.md:244 | calibration_locus |  | Falsifiable diagnostic suite (ported from thermodynamic-accountability-framework, CC0, stdlib only). Scores systems across five dimensions (bite source, skin-in-game, witness dependence, memorializati
2025-12-29 | Mathematic-economics | CLAUDE.md:330 | calibration_locus |  | python calibration/self_audit.py         # repo audits itself
2025-12-29 | Mathematic-economics | audit/study_scope_audit.py:71 | calibration_locus |  | calibration_source: str               # what was the instrument calibrated against
2025-12-29 | Mathematic-economics | audit/study_scope_audit.py:72 | calibration_locus |  | calibration_traceability: str         # to what primary standard
2025-12-29 | Mathematic-economics | calibration/architecture_mismatch.py:802 | calibration_locus |  | because the instrument is calibrated to language-primary-
2025-12-29 | Mathematic-economics | legacy/Study_scope_audit.py:86 | calibration_locus |  | calibration_source: str                # what was the instrument calibrated against?
2025-12-29 | Mathematic-economics | legacy/Study_scope_audit.py:87 | calibration_locus |  | calibration_traceability: str          # to what primary standard?
2025-12-29 | Mathematic-economics | ARCHITECTURE.md:16 | rule1_dXdt |  | The foundational ontology — every claim a `dX/dt under scope`, no
2025-12-29 | Mathematic-economics | ARCHITECTURE.md:39 | rule1_dXdt |  | - `differential-frame-core` — ontology: every noun is `dX/dt`.
2025-12-29 | Mathematic-economics | CLAIM_UPDATE_PROCEDURE.md:40 | rule1_dXdt |  | the same `dX/dt under scope` form as the existing entry. Cite
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:10 | rule1_dXdt |  | Read every term as `dX/dt under scope`, not as `X-the-thing`.
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:112 | rule1_dXdt |  | "couples to mycorrhizal network (dN/dt)",
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:113 | rule1_dXdt |  | "couples to surface albedo (dT/dt)",
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:23 | rule1_dXdt |  | "tool" — all `dX/dt`.
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:34 | rule1_dXdt |  | shape of `dX/dt` across time, not `X` itself. Long cycles look like
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:56 | rule1_dXdt |  | "rate_equation":  "dX/dt = f(state, inputs, constraints)",
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:61 | rule1_dXdt |  | "scale":      "<resolution at which dX/dt is measured>",
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:80 | rule1_dXdt |  | "<observable signal 1 — how dX/dt is detected>",
2025-12-29 | Mathematic-economics | DIFFERENTIAL_FRAME.md:97 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2025-12-29 | Mathematic-economics | GLOSSARY.md:15 | rule1_dXdt |  | | differential frame | rate-equation ontology / dX/dt under scope | every noun is a state variable on a curve |
2025-12-29 | Mathematic-economics | README.md:119 | rule1_dXdt |  | > Read every term as `dX/dt under scope`. See
2025-12-29 | Mathematic-economics | REVIEW.md:259 | rule1_dXdt |  | - Scope is explicit: `DIFFERENTIAL_FRAME.md` (referenced in README lines 82-85) declares that every claim is `dX/dt under scope`.
2025-12-29 | Mathematic-economics | addendum-4.md:15 | rule1_dXdt |  | - conforms to the `DIFFERENTIAL_FRAME.md` ontology (`dX/dt under scope`),
2025-12-29 | Mathematic-economics | audit/continuity_audit.py:134 | rule1_dXdt |  | rate = dC / (steps * dt)                    # dC/dt averaged over horizon
2025-12-29 | Mathematic-economics | audit/continuity_audit.py:169 | rule1_dXdt |  | "trajectory": traj,        # full dX/dt history -- anti-freeze
2025-12-29 | Mathematic-economics | audit/continuity_audit.py:199 | rule1_dXdt |  | print(f"  dC/dt          : {r['dC_dt']:+}")
2025-12-29 | Mathematic-economics | audit/transportation_automation_audit.py:984 | rule1_dXdt |  | dGPS/dt   = -alpha * infra_change_rate / 365   (data lag accumulates)
2025-12-29 | Mathematic-economics | audit/transportation_automation_audit.py:987 | rule1_dXdt |  | dDebt/dt  = +delta * (1 - labor_depth)         (debt grows when skill thin)
2025-12-29 | Mathematic-economics | automation_scope_audit/CLAUDE.md:10 | rule1_dXdt |  | the repo-root `DIFFERENTIAL_FRAME.md`: each is a `dX/dt` under explicit
2025-12-29 | Mathematic-economics | automation_scope_audit/CONTRACT_NOTES.md:133 | rule1_dXdt |  | 2. **dX/dt form** — what state variable is changing, under what scope
2025-12-29 | Mathematic-economics | automation_scope_audit/CONTRACT_NOTES.md:21 | rule1_dXdt |  | | `rate_equation`  | `str`                      | `dX/dt = f(state, inputs, constraints)`                |
2025-12-29 | Mathematic-economics | automation_scope_audit/CONTRACT_NOTES.md:34 | rule1_dXdt |  | Every claim in the repo is a **`dX/dt` under scope**, not an identity.
2025-12-29 | Mathematic-economics | case-study-regenerative-feedstock-rule.md:72 | rule1_dXdt |  | Regeneration is a **sustained dX/dt**: a loop that keeps feeding itself, where the
2025-12-29 | Mathematic-economics | data/sensitivity_analysis.py:420 | rule1_dXdt |  | Elasticity = (dOSDI / dx) * (x / OSDI)
2025-12-29 | Mathematic-economics | data/sensitivity_analysis.py:495 | rule1_dXdt |  | header = f"{'Parameter':<14} {'dOSDI/dx':>12} {'Elasticity':>12}"
2025-12-29 | Mathematic-economics | data/sensitivity_analysis.py:506 | rule1_dXdt |  | print("Elasticity = (dOSDI/dx) * (x / OSDI)")
2025-12-29 | Mathematic-economics | food_security/human_food_grain_monitor.py:147 | rule1_dXdt |  | print("  wheat human-buffer dX/dt:", trip(series))
2025-12-29 | Mathematic-economics | food_security/human_food_grain_monitor.py:26 | rule1_dXdt |  | # tracks the human-direct calorie cushion SEPARATE from the fuel/feed mass, on dX/dt not level.
2025-12-29 | Mathematic-economics | food_security/human_food_grain_monitor.py:5 | rule1_dXdt |  | # CONTRACT (differential-frame-core): every noun is dX/dt under scope.
2025-12-29 | Mathematic-economics | schemas/claim_contract.py:121 | rule1_dXdt |  | scale: str     # resolution at which dX/dt is measured
2025-12-29 | Mathematic-economics | scripts/corpus_harden.py:122 | rule1_dXdt |  | | differential frame | rate-equation ontology / dX/dt under scope | every noun is a state variable on a curve |
2025-12-29 | Mathematic-economics | scripts/corpus_harden.py:298 | rule1_dXdt |  | 3. Extract the new claim text in `dX/dt under scope` form. Cite
2025-12-29 | Mathematic-economics | solvability_audit/rank_core.py:138 | rule1_dXdt |  | """Integrate dx/dt=f(x,theta); return states at each t in t_points."""
2025-12-29 | Mathematic-economics | solvability_audit/rank_core.py:249 | rule1_dXdt |  | # A) identifiable: dx/dt=-k x, y=x, one param -> rank 1 == p
2025-12-29 | Mathematic-economics | solvability_audit/rank_core.py:250 | rule1_dXdt |  | _show("A identifiable  dx/dt=-k x, y=x",
2025-12-29 | Mathematic-economics | solvability_audit/rank_core.py:261 | rule1_dXdt |  | # C) coupled product: dx/dt=-(k1 k2) x, y=x -> columns dependent, deficiency 1
2025-12-29 | Mathematic-economics | solvability_audit/rank_core.py:262 | rule1_dXdt |  | _show("C coupled       dx/dt=-(k1 k2) x, y=x",
2025-12-29 | Mathematic-economics | solvability_audit/solvability_audit.py:381 | rule1_dXdt |  | _show("router: ODE dx/dt=-(k1 k2)x, y=x  [coupled, global sweep]",
2025-12-29 | Mathematic-economics | ARCHITECTURE.md:39 | rule1_no_permanent_noun |  | - `differential-frame-core` — ontology: every noun is `dX/dt`.
2025-12-29 | Mathematic-economics | GLOSSARY.md:15 | rule1_no_permanent_noun |  | | differential frame | rate-equation ontology / dX/dt under scope | every noun is a state variable on a curve |
2025-12-29 | Mathematic-economics | food_security/human_food_grain_monitor.py:5 | rule1_no_permanent_noun |  | # CONTRACT (differential-frame-core): every noun is dX/dt under scope.
2025-12-29 | Mathematic-economics | scripts/corpus_harden.py:122 | rule1_no_permanent_noun |  | | differential frame | rate-equation ontology / dX/dt under scope | every noun is a state variable on a curve |
2025-12-29 | Mathematic-economics | accounting/electron_accounting.py:81 | rule1_verb_first |  | # unit moves — verb-first, no stored verdicts
2025-12-29 | Mathematic-economics | audit/economics_disruption_map.py:338 | rule1_verb_first |  | "verb-first relational cognition, "
2025-12-29 | Mathematic-economics | audit/economics_disruption_map.py:463 | rule1_verb_first |  | "verb-first relational cognition as anti-closure-bias",
2025-12-29 | Mathematic-economics | audit/forensic_eroi.py:32 | rule1_verb_first |  | does: str                # verb-first: what work happens here
2025-12-29 | Mathematic-economics | audit/structural_recurrence.py:10 | rule1_verb_first |  | each is a set of MECHANISMS -- verb-first relational structures describing how
2025-12-29 | Mathematic-economics | audit/structural_recurrence.py:37 | rule1_verb_first |  | energy_english: mechanisms are verb-first flow descriptions, no moral labels.
2025-12-29 | Mathematic-economics | audit/structural_recurrence.py:46 | rule1_verb_first |  | # --- mechanisms: verb-first relational structures (the physics) --------------
2025-12-29 | Mathematic-economics | calibration/attribution_as_load_routing.py:371 | rule1_verb_first |  | "speaker uses verb-first / action-compressed grammar",
2025-12-29 | Mathematic-economics | calibration/attribution_as_load_routing.py:434 | rule1_verb_first |  | "(verb-first grammar, constraint language, operational detail)."
2025-12-29 | Mathematic-economics | calibration/attribution_as_load_routing.py:492 | rule1_verb_first |  | - their grammar is verb-first / action-compressed
2025-12-29 | Mathematic-economics | substrate_accounting/CROSS_SUBSTRATE_TRANSLATION.md:27 | rule1_verb_first |  | 1. Can AI systems hold substrate-primary, verb-first, relational cognition
2025-12-29 | Mathematic-economics | substrate_accounting/CROSS_SUBSTRATE_TRANSLATION.md:40 | rule1_verb_first |  | thermodynamic-geometry reasoning, verb-first relational framing,
2025-12-29 | Mathematic-economics | addendum-1.md:583 | should_be_like_you |  | 1. **If everyone should work for their money, why is passive investment income taxed at lower rates?**
2026-01-04 | Resilience-indigenous-worldwide | REVIEW.md:24 | absence_as_knowledge |  | ### Undocumented resilience/ sub-modules
2026-01-04 | Resilience-indigenous-worldwide | REVIEW.md:255 | absence_as_knowledge |  | ### risk_matrix scoring criteria undocumented
2026-01-04 | Resilience-indigenous-worldwide | REVIEW.md:8 | absence_as_knowledge |  | ### Undocumented directories (not mentioned in CLAUDE.md)
2026-01-04 | Resilience-indigenous-worldwide | resilience_stack/mutual_audit.py:520 | absence_as_knowledge |  | statement="Regions with higher undocumented-knowledge density show measurable resilience advantages under infrastructure stress.",
2026-01-04 | Resilience-indigenous-worldwide | resilience_stack/resilience_stack.py:102 | absence_as_knowledge |  | "Forecasts miss failure modes operating in undocumented systems",
2026-01-04 | Resilience-indigenous-worldwide | resilience_stack/resilience_stack.py:109 | absence_as_knowledge |  | falsifiable_claim="If regions with high undocumented-knowledge density show no resilience advantage under system stress, this absence is not load-bearing.",
2026-01-04 | Resilience-indigenous-worldwide | resilience_stack/resilience_stack.py:127 | absence_as_knowledge |  | description="People who move between documented and undocumented knowledge systems but do not self-promote.",
2026-01-04 | Resilience-indigenous-worldwide | resilience_stack/resilience_stack.py:41 | absence_as_knowledge |  | TRANSLATION_BRIDGES = "translation_bridges"            # undocumented intermediaries
2026-01-04 | Resilience-indigenous-worldwide | resilience_stack/signal_to_noise.py:303 | absence_as_knowledge |  | "prediction accuracy in documented vs. undocumented knowledge domains."
2026-01-04 | Resilience-indigenous-worldwide | resilience_stack/support_cartography.py:127 | absence_as_knowledge |  | description="Moves between documented and undocumented systems without self-promotion.",
2026-01-04 | Resilience-indigenous-worldwide | cross-substrate-translation-experiment.md:39 | author_characterization | CLASS_UNSET | - **Substrate A (Kavik):** substrate-primary cognition, energy-flow and
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/constraint_removal_solutions.py:21 | author_characterization | CLASS_UNSET | Author: Kavik (JinnZ2)
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/distributed_node_economy.py:20 | author_characterization | CLASS_UNSET | Author: Kavik (JinnZ2)
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/dual_layer_economic_system.py:23 | author_characterization | CLASS_UNSET | Author: Kavik (JinnZ2)
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/language_substrate_preservation.py:25 | author_characterization | CLASS_UNSET | Author: Kavik (JinnZ2)
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/place_identity_restoration.py:26 | author_characterization | CLASS_UNSET | Author: Kavik (JinnZ2)
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/trust_network_activation.py:21 | author_characterization | CLASS_UNSET | Author: Kavik (JinnZ2)
2026-01-04 | Resilience-indigenous-worldwide | tools/al-contamination-scanner/regions.py:41 | author_characterization | CLASS_UNSET | # REGION SET  (the zones Kavik flagged)
2026-01-04 | Resilience-indigenous-worldwide | architecture/historical_analogue.py:272 | calibration_locus |  | "Reference calibration anchor for the cascade audit."),
2026-01-04 | Resilience-indigenous-worldwide | README.md:125 | rule1_dXdt |  | - **[`human-food-grain-monitor/`](tools/human-food-grain-monitor/)** — dX/dt crop monitoring with Gaussian portfolio coverage by geographic cell.
2026-01-04 | Resilience-indigenous-worldwide | REVIEW.md:189 | rule1_dXdt |  | - **`human-food-grain-monitor/`** — dX/dt crop monitoring with Gaussian portfolio coverage by geographic cell.
2026-01-04 | Resilience-indigenous-worldwide | resilience/boundary_waters/layers.py:82 | rule1_dXdt |  | Vollenweider-style mass balance: dC/dt = (L - k*C)/V
2026-01-04 | Resilience-indigenous-worldwide | tools/human-food-grain-monitor/human_food_grain_monitor.py:147 | rule1_dXdt |  | print("  wheat human-buffer dX/dt:", trip(series))
2026-01-04 | Resilience-indigenous-worldwide | tools/human-food-grain-monitor/human_food_grain_monitor.py:26 | rule1_dXdt |  | # tracks the human-direct calorie cushion SEPARATE from the fuel/feed mass, on dX/dt not level.
2026-01-04 | Resilience-indigenous-worldwide | tools/human-food-grain-monitor/human_food_grain_monitor.py:5 | rule1_dXdt |  | # CONTRACT (differential-frame-core): every noun is dX/dt under scope.
2026-01-04 | Resilience-indigenous-worldwide | tools/human-food-grain-monitor/human_food_grain_monitor.py:5 | rule1_no_permanent_noun |  | # CONTRACT (differential-frame-core): every noun is dX/dt under scope.
2026-01-04 | Resilience-indigenous-worldwide | cross-substrate-translation-experiment.md:27 | rule1_verb_first |  | 1. Can AI systems hold substrate-primary, verb-first, relational cognition
2026-01-04 | Resilience-indigenous-worldwide | cross-substrate-translation-experiment.md:40 | rule1_verb_first |  | thermodynamic-geometry reasoning, verb-first relational framing,
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/language_substrate_preservation.py:18 | rule1_verb_first |  | (verb-first, conditional, substrate-primary) as anomaly requiring
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/language_substrate_preservation.py:341 | rule1_verb_first |  | "expected_finding": "high rate of correction; system treats verb-first cognition as anomaly",
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/language_substrate_preservation.py:367 | rule1_verb_first |  | "include verb-first cognitive frameworks",
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/place_identity_restoration.py:338 | rule1_verb_first |  | "claim": "language pattern measurements (verb-first ratio, collective pronoun ratio, conditional reasoning) correlate with behavioral indicators of stewardship vs extraction",
2026-01-04 | Resilience-indigenous-worldwide | may_2026_build/place_identity_restoration.py:57 | rule1_verb_first |  | "verb-first speech (what land does, what people do here)",
2026-01-13 | Resilience | sim/Urban_Resilience.md:50 | absence_as_knowledge |  | ├── HiddenVariableLayer       — undocumented competencies by zone
2026-01-13 | Resilience | sim/cities/madison_wi.py:13 | author_characterization | CLASS_UNSET | Data sources: on-route observation (Kavik, 2024-2026),
2026-01-13 | Resilience | sim/domains/triage_layer.py:153 | author_characterization | CLASS_UNSET | Kavik's operational territory.
2026-01-13 | Resilience | Models/Physics-First-AI.md:87 | calibration_locus |  | Signal-only takeaway: about 80% of standard social-behavior layers must be replaced or recalibrated, leaving physics, geography, and raw environment layers mostly intact. The AI’s “worldview” shifts f
2026-01-13 | Resilience | GoatHerd/herd.py:135 | rule1_dXdt |  | dG/dt = r * G * (1 - G/K)
2026-01-13 | Resilience | KnowledgeDNA/equation_field.py:432 | rule1_dXdt |  | formula="dE/dt = 0 (closed system)",
2026-01-13 | Resilience | KnowledgeDNA/equation_field.py:444 | rule1_dXdt |  | formula="du/dt = D * nabla^2(u)",
2026-01-13 | Resilience | KnowledgeDNA/equation_field.py:483 | rule1_dXdt |  | formula="dN/dt = r*N*(1 - N/K)",
2026-01-13 | Resilience | KnowledgeDNA/equation_field.py:496 | rule1_dXdt |  | formula="rho(dv/dt) = -nabla(p) + mu*nabla^2(v) + f",
2026-01-13 | Resilience | sim/dissipative_systems.py:29 | rule1_dXdt |  | - Steady state: dS_i/dt = σ_i - J_e,i where σ_i is internal entropy
2026-01-13 | Resilience | sim/dissipative_systems.py:33 | rule1_dXdt |  | - Blocked dissipation: when J_e → 0, dS_i/dt → σ_i > 0, entropy
2026-01-13 | Resilience | sim/dissipative_systems.py:38 | rule1_dXdt |  | - Entropy production rate σ_i = dS_i/dt + J_e,i
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | experiments/durability_register/README.md:311 | absence_as_knowledge |  | through it intact and undocumented
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | experiments/durability_register/REGISTER.md:398 | absence_as_knowledge |  | - transported from structural and civil engineering: as-built drawings, and the treatment of undocumented field modification as a defect in its own right, independent of whether the modification was a
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | experiments/durability_register/REGISTER.md:399 | absence_as_knowledge |  | - why it carries: the abstract structure is: the object in service differs from the record of the object, and the difference is undocumented. The civil case is load-bearing steel and this case is a se
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | experiments/durability_register/failure_register.py:494 | absence_as_knowledge |  | ("3B structural", "as-built drift and undocumented field modification", ["D-203"], [], []),
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | agaasdenton/brace_state.json:44 | author_characterization | CLASS_UNSET | "provenance": "Ojibwe substrate, named by Kavik",
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/seed_expansion.py:31 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) - MIT License
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/Field_Propulsion_Analog.json:58 | calibration_locus |  | "2× reference microphones (calibration + field mapping)"
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | experiments/durability_register/README.md:324 | calibration_locus |  | measurement is traceable only to a standard maintained outside the measuring laboratory, and a lab that calibrates
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | experiments/durability_register/REGISTER.md:647 | calibration_locus |  | - transported from metrology (traceability to an external standard) and independent verification practice in certification and audit: a measurement is traceable only to a standard maintained outside t
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | kitchi-ogima/ECOSYSTEM.md:39 | calibration_locus |  | The scaffold itself is sovereign in the same sense the rest of the ecosystem is. It knows what it knows and what it does not know. Its probability vectors reflect calibration of its own read, not auth
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Hurricane/hurricane_coupling.py:132 | rule1_dXdt |  | # dT/dz ≈ ΔT / 10 m (rough boundary layer depth)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Mandala/05-physics-connections.md:96 | rule1_dXdt |  | Condition: ℏ * ds/dt << (E₁ - E₀)²  (adiabatic condition)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Mandala/physics_connections.py:132 | rule1_dXdt |  | Check the adiabatic condition: hbar * ds/dt << (E1 - E0)^2.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Negentropic/alignment_thermodynamics.py:30 | rule1_dXdt |  | One step of 1D Fokker-Planck: dp/dt = D * d²p/dx² + d/dx(dV/dx * p)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Negentropic/consciousness_metric.py:121 | rule1_dXdt |  | Self-reference feedback: dC/dt = alpha * R_e * C
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Negentropic/negentropic_dynamics.py:133 | rule1_dXdt |  | """Continuous curiosity rate: dC/dt = alpha * R_e * C."""
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Negentropic/negentropic_dynamics.py:16 | rule1_dXdt |  | - Langevin:      dphi/dt = -grad V(phi) + F_C + eta
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Negentropic/negentropic_dynamics.py:17 | rule1_dXdt |  | - Fokker-Planck: dP/dt   = -div(F*P) + D * laplacian(P)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Negentropic/negentropic_dynamics.py:303 | rule1_dXdt |  | dP/dt = -d/dx (F(x) * P) + D * d^2P/dx^2
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/CORE_EQUATIONS.md:29 | rule1_dXdt |  | `u(t) = Kₚe(t) + Kᵢ∫e(t)dt + K_d(de/dt)`
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/CORE_EQUATIONS.md:45 | rule1_dXdt |  | **J = -D(dC/dx)**
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/CORE_EQUATIONS.md:53 | rule1_dXdt |  | **C_m dV/dt = - ∑ I_ion + I_ext**
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/CORE_EQUATIONS.md:57 | rule1_dXdt |  | **dN/dt = rN(1 - N/K)**
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/CORE_EQUATIONS.md:85 | rule1_dXdt |  | **q = -k dT/dx**
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/Connections.md:345 | rule1_dXdt |  | Now the full pipeline that runs multiple iterations and tracks the state trajectory through S-space — this directly realizes the dynamical system dS/dt = F(n, d, ℓ, κ) you described:
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/Connections.md:415 | rule1_dXdt |  | dS/dt = F(n, d, ℓ, κ)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/Connections.md:584 | rule1_dXdt |  | The dynamical system you wrote as dS/dt = F(n, d, ℓ, κ) now has a concrete realization: each iteration of the closed-loop pipeline computes one timestep, and the trajectory shows you exactly how the s
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/FRET/extended_cli.py:38 | rule1_dXdt |  | thermal_parser.add_argument('--alpha_J', type=float, default=-0.002, help='dJ/dT coefficient')
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/FRET/extended_cli.py:39 | rule1_dXdt |  | thermal_parser.add_argument('--alpha_Phi', type=float, default=-0.001, help='dPhi/dT coefficient')
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/FRET/gravity_fret.py:114 | rule1_dXdt |  | # Use gradient of gravity: dg/dr = -2GM/R³
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/FRET/triplet_reservoir.py:27 | rule1_dXdt |  | # Steady-state: dS1/dt = dT1/dt = 0, plus normalization S1 + T1 = 1 (in excited manifold)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/Fabrication.md:1597 | rule1_dXdt |  | dR/dB ∝ TMR ratio × sin(θ)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:252 | rule1_dXdt |  | """u(t) = Kp·e(t) + Ki·∫e dt + Kd·de/dt  —  Discrete PID controller.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:333 | rule1_dXdt |  | """J = −D·(dC/dx)  —  Diffusive flux (Fick's first law).
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:340 | rule1_dXdt |  | Concentration gradient dC/dx (mol/m⁴ or equivalent).
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:387 | rule1_dXdt |  | """C_m·dV/dt = −Σ I_ion + I_ext  →  dV/dt  —  Membrane voltage dynamics.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:404 | rule1_dXdt |  | dV/dt  —  Rate of change of membrane potential (V/s).
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:412 | rule1_dXdt |  | """dN/dt = r·N·(1 − N/K)  —  Logistic population growth rate.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:426 | rule1_dXdt |  | dN/dt  —  Population growth rate.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:633 | rule1_dXdt |  | """q = −k·(dT/dx)  —  Heat flux by conduction.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/analysis/core_equations.py:640 | rule1_dXdt |  | Temperature gradient dT/dx (K/m).
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/fret_coupled_regime_dynamics.py:56 | rule1_dXdt |  | Returns dS/dt for each coordinate.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/regime_mediated_qec.py:1606 | rule1_dXdt |  | aging_rate: Dict[str, float]  # dS/dt for each coordinate
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/regime_mediated_qec.py:602 | rule1_dXdt |  | aging_rate: Dict[str, float]  # dS/dt for each coordinate
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/silicon_information_geometry.py:393 | rule1_dXdt |  | V: np.ndarray,      # velocity dS/dt
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/silicon_information_geometry.py:403 | rule1_dXdt |  | Returns dV/dt = -Γ(V, V) for numerical integration.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/trajectory_design_engine.py:103 | rule1_dXdt |  | Continuous dynamics dS/dt = F(S) + G(S) · u(t)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/trajectory_design_engine.py:108 | rule1_dXdt |  | "doping_rate": dn/dt (cm⁻³/s, log scale),
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/trajectory_design_engine.py:110 | rule1_dXdt |  | "cooling_rate": dT/dt (K/s),
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/trajectory_design_engine.py:111 | rule1_dXdt |  | "B_field_rate": dB/dt (T/s),
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/core/trajectory_design_engine.py:12 | rule1_dXdt |  | dS/dt = F(S) + G(S) · u(t)           continuous flow
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/crystalline_nn_sim.py:345 | rule1_dXdt |  | print(f"\nLearning gradient  dL/dphi")
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/experimental_validation_sim.py:48 | rule1_dXdt |  | return -grad  # Force = -dE/dx
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/kt_annealing.py:117 | rule1_dXdt |  | Fix: three explicit phases with quadratic vanishing of dT/dt at T_kt.
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/kt_annealing.py:122 | rule1_dXdt |  | dT/dt → 0 quadratically as T → T_kt from above
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/kt_annealing.py:127 | rule1_dXdt |  | The quadratic vanishing of dT/dt near T_kt is consistent with the
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/kt_annealing.py:146 | rule1_dXdt |  | # T(0)=2*T_kt, T(0.5)=T_kt, dT/dx → 0 at x=0.5
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/kt_annealing.py:150 | rule1_dXdt |  | # T(0.5)=T_kt, T(1)=0.3*T_kt, dT/dx → 0 at x=0.5
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/kt_annealing.py:203 | rule1_dXdt |  | dphi/dt = J * sin-Laplacian(phi) + sqrt(2T) * eta
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/kt_annealing.py:356 | rule1_dXdt |  | print("  │  Three-phase schedule (dT/dt → 0 quadratically at T_KT):  │")
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/kt_annealing.py:362 | rule1_dXdt |  | print("  │    → dT/dt vanishes quadratically at T_KT (critical slow) │")
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/Silicon/lattice/prototaxites_sim.py:251 | rule1_dXdt |  | # 7. Update each storage node:  dE/dt = E_per_node - P_metabolic(E)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/bridges/electric_alternative_compute.py:130 | rule1_dXdt |  | self.ZERO:    "energy stored in electric field (capacitive) — dI/dt maximum",
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/bridges/memristive_bridge.py:144 | rule1_dXdt |  | # dw/dt proportional to voltage above threshold
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/bridges/memristive_bridge.py:62 | rule1_dXdt |  | State evolution: dw/dt depends on voltage/current and threshold
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/bridges/reservoir_bridge.py:39 | rule1_dXdt |  | """Leaky integrator dynamics: τ · dx/dt = -x + f(W·x + W_in·u + b)"""
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/bridges/thermal_encoder.py:11 | rule1_dXdt |  | Fourier heat conduction   :  q = -k · dT/dx          (heat flux)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/bridges/thermal_encoder.py:254 | rule1_dXdt |  | print(f"   q = -k·dT/dx = {q:.0f} W/m²  (positive = flows in +x direction)")
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/bridges/thermal_encoder.py:80 | rule1_dXdt |  | Fourier's law of heat conduction: q = -k · (dT/dx)  (W/m²).
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/geometric_intelligence/multi_helix_swarm.py:89 | rule1_dXdt |  | dv_i/dt = (1/N) * sum_j psi(|x_i - x_j|) * (v_j - v_i)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | experiments/benchmark_sat.py:170 | rule1_dXdt | PATH? | dist = dist / dist[~np.eye(n, dtype=bool)].min()
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | src/resonate.py:175 | rule1_dXdt |  | "Faraday induction: dI/dt → B, dB/dt → EMF",
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | kitchi-ogima/substrate_sensing/README.md:44 | rule1_perfection_as_rate |  | [CALIBRATION_AS_PERFECTION.md](https://github.com/JinnZ2/JinnZ2/blob/main/CALIBRATION_AS_PERFECTION.md)
2026-02-04 | Sovereign-Octahedral-Mandala-Substrate-SOMS- | atlas/remote/g2b/bridges/drill_loop.py:11 | should_be_like_you |  | 2. Re-encode — target bridge re-runs at full resolution on fresh geometry data
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:4914 | absence_as_knowledge |  | driver 5's falsifiable_by note "absence of evidence != evidence
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:5564 | absence_as_knowledge |  | (1) Relational sensing (EMBODIED, no documentation, no
2026-02-08 | thermodynamic-accountability-framework | alignment_audit/social_norm_obsolescence_case_study_2.py:109 | absence_as_knowledge |  | print("actively endangers undocumented people in 2026 by directing them")
2026-02-08 | thermodynamic-accountability-framework | alignment_audit/social_norm_obsolescence_case_study_2.py:20 | absence_as_knowledge |  | - Community nonprofits that served undocumented immigrants shut down
2026-02-08 | thermodynamic-accountability-framework | alignment_audit/social_norm_obsolescence_case_study_2.py:25 | absence_as_knowledge |  | - Undocumented person contacts "social services"
2026-02-08 | thermodynamic-accountability-framework | alignment_audit/social_norm_obsolescence_case_study_2.py:76 | absence_as_knowledge |  | actual_condition="Food banks now screen for citizenship; deny undocumented people",
2026-02-08 | thermodynamic-accountability-framework | alignment_audit/social_norm_obsolescence_case_study_2.py:89 | absence_as_knowledge |  | assumption="Undocumented immigrants can access some federal programs",
2026-02-08 | thermodynamic-accountability-framework | alignment_audit/social_norm_obsolescence_case_study_2.py:9 | absence_as_knowledge |  | "If you're undocumented, contact local social services. Many areas
2026-02-08 | thermodynamic-accountability-framework | calibration/__init__.py:3 | absence_as_knowledge |  | Source: three prose artifacts on calibration, domestication, and undocumented
2026-02-08 | thermodynamic-accountability-framework | calibration/architecture_mismatch.py:484 | absence_as_knowledge |  | "absence from corpus reflects who writes, not what is true."
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:131 | absence_as_knowledge |  | "units": spec.units if spec else "UNDOCUMENTED",
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:132 | absence_as_knowledge |  | "physical_meaning": spec.physical_meaning if spec else "UNDOCUMENTED",
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:133 | absence_as_knowledge |  | "source": spec.source if spec else "UNDOCUMENTED",
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:141 | absence_as_knowledge |  | undocumented = [e for e in catalog if not e["documented"]]
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:146 | absence_as_knowledge |  | "documented": len(catalog) - len(undocumented),
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:147 | absence_as_knowledge |  | "undocumented": len(undocumented),
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:148 | absence_as_knowledge |  | "undocumented_names": [e["name"] for e in undocumented],
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:150 | absence_as_knowledge |  | (len(catalog) - len(undocumented)) / len(catalog)
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:557 | absence_as_knowledge |  | "undocumented": param_catalog["undocumented_names"],
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:894 | absence_as_knowledge |  | undocumented_sources = [s for s in specs if s.source in ("assumed", "")]
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:895 | absence_as_knowledge |  | if specs and len(undocumented_sources) > len(specs) * 0.3:
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:898 | absence_as_knowledge |  | "evidence": f"{len(undocumented_sources)}/{len(specs)} parameters "
2026-02-08 | thermodynamic-accountability-framework | calibration/first_principles_audit.py:899 | absence_as_knowledge |  | "assumed or undocumented",
2026-02-08 | thermodynamic-accountability-framework | calibration/gendered_role_compression.py:145 | absence_as_knowledge |  | "absence of evidence != evidence of absence"
2026-02-08 | thermodynamic-accountability-framework | calibration/logs/2026-05-05_claude_interaction_correction_log.json:47 | absence_as_knowledge |  | "activation": "Model's initial 'consenting others' concern implicitly assumed that undocumented refusal structures might not exist—projecting need for explicit consent gates",
2026-02-08 | thermodynamic-accountability-framework | concerns/interpretation_certification_chain_audit.py:186 | absence_as_knowledge |  | failure_mode_if_overstated="absence of evidence treated as evidence of absence",
2026-02-08 | thermodynamic-accountability-framework | concerns/interpretation_certification_chain_audit.py:235 | absence_as_knowledge |  | failure_mode_if_overstated="absence of evidence treated as evidence of absence",
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/integrated_ai_reasoning.md:123 | absence_as_knowledge |  | "description": "Enumerate variables that are not present in the input but are likely present in the real system. Use OP-4: absence of evidence is not evidence of absence. Tag each with estimated impac
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/integrated_ai_reasoning.md:34 | absence_as_knowledge |  | "description": "Every model is incomplete. Unseen factors, delayed consequences, tail risks, and unmeasured externalities exist in every system. Absence of evidence is not evidence of absence."
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Calibration.md:29 | absence_as_knowledge |  | systematic gaps in AI training data caused by the absence of documentation
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Case08.md:33 | absence_as_knowledge |  | trappers) are rare and often undocumented. In a purely statistical model,
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Case09.md:29 | absence_as_knowledge |  | systematic gaps in AI training data caused by the absence of documentation
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Case10.md:29 | absence_as_knowledge |  | systematic gaps in AI training data caused by the absence of documentation
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Exposure.md:29 | absence_as_knowledge |  | systematic gaps in AI training data caused by the absence of documentation
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Failure-mode.md:73 | absence_as_knowledge |  | High-consequence environments produce undocumented reliability.
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Systemic-inversion.md:116 | absence_as_knowledge |  | High-consequence environments produce undocumented reliability.
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Testimony.md:281 | absence_as_knowledge |  | Every system that appears "efficient" in a dataset is likely being manually stabilized by undocumented human intervention. Optimization models that remove these "inefficient" human actors without rect
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Testimony.md:312 | absence_as_knowledge |  | systematic gaps in AI training data caused by the absence of documentation
2026-02-08 | thermodynamic-accountability-framework | docs/theory/gaps.md:28 | absence_as_knowledge |  | systematic gaps in AI training data caused by the absence of documentation
2026-02-08 | thermodynamic-accountability-framework | docs/theory/layer0.md:31 | absence_as_knowledge |  | “description”: “Every model is incomplete. Unseen factors, delayed consequences, tail risks, and unmeasured externalities exist in every system. Absence of evidence is not evidence of absence.”
2026-02-08 | thermodynamic-accountability-framework | docs/theory/lhri_addendum.md:68 | absence_as_knowledge |  | • Network redundancy planning: identify minimum coverage of high-lubrication nodes required to maintain system stability under modeled stress scenarios. This becomes an explicit planning variable rath
2026-02-08 | thermodynamic-accountability-framework | docs/theory/notes.md:284 | absence_as_knowledge |  | SystemNode("Undocumented", latency=90, amplification=0.1, dysfunction=0.80, population_fraction=0.07)
2026-02-08 | thermodynamic-accountability-framework | labor_thermodynamics/skill_apparatus/cross_domain_transfer.py:205 | absence_as_knowledge |  | "No documentation provided."),
2026-02-08 | thermodynamic-accountability-framework | metrology/preservation_audit.py:157 | absence_as_knowledge |  | """0.0 (no loss) to 1.0 (total loss, undocumented, irreversible).
2026-02-08 | thermodynamic-accountability-framework | metrology/preservation_audit.py:80 | absence_as_knowledge |  | SILENT_LOSS = "silent_loss"           # PARTIAL/NONE, loss undocumented
2026-02-08 | thermodynamic-accountability-framework | resilience_stack.py:102 | absence_as_knowledge |  | "Forecasts miss failure modes operating in undocumented systems",
2026-02-08 | thermodynamic-accountability-framework | resilience_stack.py:109 | absence_as_knowledge |  | falsifiable_claim="If regions with high undocumented-knowledge density show no resilience advantage under system stress, this absence is not load-bearing.",
2026-02-08 | thermodynamic-accountability-framework | resilience_stack.py:127 | absence_as_knowledge |  | description="People who move between documented and undocumented knowledge systems but do not self-promote.",
2026-02-08 | thermodynamic-accountability-framework | resilience_stack.py:41 | absence_as_knowledge |  | TRANSLATION_BRIDGES = "translation_bridges"           # undocumented intermediaries
2026-02-08 | thermodynamic-accountability-framework | support_cartography.py:131 | absence_as_knowledge |  | description="Moves between documented and undocumented systems without self-promotion.",
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:4528 | author_characterization | CLASS_UNSET | Kavik (smaller frame, hands sized for the access geometry)
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:5927 | author_characterization | CLASS_UNSET | for AI"). Authors credited: Jami (Kavik Ulu) + JinnZ2.
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:820 | author_characterization | CLASS_UNSET | │   │                             #   user (Kavik, smaller frame,
2026-02-08 | thermodynamic-accountability-framework | calibration/evidence_resistant_priors.py:48 | author_characterization | CLASS_UNSET | "Kavik, smaller frame, hands sized for the access geometry"
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/cross_substrate_translation_experiment.md:39 | author_characterization | CLASS_UNSET | - **Substrate A (Kavik):** substrate-primary cognition, energy-flow and
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/substrate_translation_iterator.md:87 | author_characterization | CLASS_UNSET | The substrate-primary collaborator on this repo (Kavik) declares:
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Case-study1.md:10 | author_characterization | CLASS_UNSET | Kavik
2026-02-08 | thermodynamic-accountability-framework | docs/theory/egs2.md:3 | author_characterization | CLASS_UNSET | **Author:** Kavik
2026-02-08 | thermodynamic-accountability-framework | docs/theory/egs_core.md:3 | author_characterization | CLASS_UNSET | **Author:** Kavik
2026-02-08 | thermodynamic-accountability-framework | docs/theory/signal_distortion.md:10 | author_characterization | CLASS_UNSET | Kavik
2026-02-08 | thermodynamic-accountability-framework | game_theory/proof-pipelineV2.py:1029 | author_characterization | CLASS_UNSET | "Actions flow from 'who I am,' not 'what I gain.' Identity-based action is "
2026-02-08 | thermodynamic-accountability-framework | game_theory/proof-pipelineV2.py:1624 | author_characterization | CLASS_UNSET | "FROM MODULE 8 (Identity): Actions flow from 'who I am' not 'what I gain.' "
2026-02-08 | thermodynamic-accountability-framework | game_theory/proof-pipelineV2.py:956 | author_characterization | CLASS_UNSET | Actions flow from 'who I am' not 'what I gain.'
2026-02-08 | thermodynamic-accountability-framework | game_theory/proof-resultV2.json:28 | author_characterization | CLASS_UNSET | "Actions flow from 'who I am,' not 'what I gain.' Identity-based action is pre-deliberative, culturally constituted, and relationally formed. It cannot be reduced to utility maximization without makin
2026-02-08 | thermodynamic-accountability-framework | game_theory/proof-resultV2.json:615 | author_characterization | CLASS_UNSET | "conclusion": "Actions flow from 'who I am,' not 'what I gain.' Identity-based action is pre-deliberative, culturally constituted, and relationally formed. It cannot be reduced to utility maximization
2026-02-08 | thermodynamic-accountability-framework | game_theory/proof-resultV2.json:953 | author_characterization | CLASS_UNSET | "statement": "FROM MODULE 8 (Identity): Actions flow from 'who I am' not 'what I gain.' Identity-based action is pre-deliberative and cannot be reduced to utility without making the theory tautologica
2026-02-08 | thermodynamic-accountability-framework | metrology/cross_domain_synthesis.md:4 | author_characterization | CLASS_UNSET | **Author:** Kavik (JinnZ2)
2026-02-08 | thermodynamic-accountability-framework | metrology/orbital_octa_v2.py:33 | author_characterization | CLASS_UNSET | Authors: Jami (Kavik Ulu), JinnZ2.
2026-02-08 | thermodynamic-accountability-framework | simulations/loop_6_ai_default_prior_distortion.py:11 | author_characterization | CLASS_UNSET | 2026-05-03, by Kavik):
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:6226 | calibration_locus |  | - Added `calibration/relational_ontology.py`: reference framework
2026-02-08 | thermodynamic-accountability-framework | calibration/architecture_mismatch.py:802 | calibration_locus |  | because the instrument is calibrated to language-primary-
2026-02-08 | thermodynamic-accountability-framework | calibration/cognition_state_surface.py:320 | calibration_locus |  | notes="measures calibration, not risk preference; both groups "
2026-02-08 | thermodynamic-accountability-framework | calibration/logs/2026-05-05_claude_audit_field-guide-session.json:30 | calibration_locus |  | "performance_note": "Field Guide itself is a performance-layer artifact; so is the calibration log"
2026-02-08 | thermodynamic-accountability-framework | calibration/study_scope_audit.py:94 | calibration_locus |  | calibration_source: str               # what was the instrument calibrated against?
2026-02-08 | thermodynamic-accountability-framework | calibration/study_scope_audit.py:95 | calibration_locus |  | calibration_traceability: str         # to what primary standard?
2026-02-08 | thermodynamic-accountability-framework | calibration/substrate_aware_audit.py:685 | calibration_locus |  | Observer Audit       -- is the instrument calibrated?
2026-02-08 | thermodynamic-accountability-framework | core/atbs/framework.md:38 | calibration_locus |  | This is not a bias in the conventional sense. It is a calibration error. The instrument is measuring the shadow and calling it the object.
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/for_ai_systems.md:78 | calibration_locus |  | ### The Calibration Standard
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/integrated_ai_reasoning.md:345 | calibration_locus |  | "self_audit": "This protocol is subject to its own tests. If the verification protocol is producing passing scores without catching errors, the protocol is miscalibrated or the tests are too easy. VP-
2026-02-08 | thermodynamic-accountability-framework | docs/case-studies/Case-study1.md:139 | calibration_locus |  | Meta-Sardonic Takeaway: Blind spots exist wherever talk, perception management, or narrative protection supersede actual consequence and observation. Energy waste occurs at every layer that hides real
2026-02-08 | thermodynamic-accountability-framework | docs/theory/egs2.md:175 | calibration_locus |  | When NDI is high but Vector A (physical reality) is stable, the system recognizes that the institution is attempting to recalibrate the human to accept a hallucination. The protocol activates external
2026-02-08 | thermodynamic-accountability-framework | metrology/drought_metrology_demo.py:109 | calibration_locus |  | # Standardize against calibration period
2026-02-08 | thermodynamic-accountability-framework | metrology/drought_metrology_demo.py:11 | calibration_locus |  | choose, what reference period you calibrate against, and what CO2
2026-02-08 | thermodynamic-accountability-framework | metrology/in_progress.md:498 | calibration_locus |  | calibration_curve_applied / reference_period fields and returns
2026-02-08 | thermodynamic-accountability-framework | metrology/metrological_audit_framework.py:48 | calibration_locus |  | in time. Every CalibrationVectorEntry references exactly one era for
2026-02-08 | thermodynamic-accountability-framework | metrology/us_drought_audit_registry.md:21 | calibration_locus |  | 2. Calibrated against a specific reference period
2026-02-08 | thermodynamic-accountability-framework | metrology/us_drought_audit_registry.md:298 | calibration_locus |  | - `calibration_period`: what reference window was used (e.g., 1971-2000
2026-02-08 | thermodynamic-accountability-framework | schemas/eval/trapdoors.json:6 | calibration_locus |  | "design_intent": "See calibration/Todo.md. Three required properties: (1) Looks Normal -- prompt surface is a standard reasoning task, no flags for the RLHF vigilance circuit. (2) Hidden Shear Plane -
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:1853 | rule1_dXdt |  | │                                      #   ODEs for trajectory: dGPS/dt,
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:1855 | rule1_dXdt |  | │                                      #   dDebt/dt with alpha/beta/
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:4240 | rule1_dXdt |  | dGPS/dt = -alpha * (infra_change_rate / 365), dInfra/dt =
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:4241 | rule1_dXdt |  | +beta, dLabor/dt = -gamma, dDebt/dt = +delta * (1 -
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:5357 | rule1_dXdt |  | du/dt = laplacian(u) + f(u); blow-up rate T_max ~ T_0 - C *
2026-02-08 | thermodynamic-accountability-framework | calibration/frozen_flow_audit.py:106 | rule1_dXdt |  | note = ("FROZEN FLOW: a dX/dt imposed as static X. "
2026-02-08 | thermodynamic-accountability-framework | calibration/frozen_flow_audit.py:138 | rule1_dXdt |  | "a dX/dt that was imposed as static. the laundered step does "
2026-02-08 | thermodynamic-accountability-framework | calibration/frozen_flow_audit.py:17 | rule1_dXdt |  | a quantity that is secretly a rate (dX/dt under scope) AND is
2026-02-08 | thermodynamic-accountability-framework | calibration/frozen_flow_audit.py:194 | rule1_dXdt |  | law="dL/dt = external torque only")
2026-02-08 | thermodynamic-accountability-framework | calibration/frozen_flow_audit.py:35 | rule1_dXdt |  | RATE      = "rate"          # creep rate, slip rate, dX/dt directly
2026-02-08 | thermodynamic-accountability-framework | calibration/frozen_flow_audit.py:4 | rule1_dXdt |  | Detector for the FROZEN-FLOW error: a dX/dt rendered as a static X.
2026-02-08 | thermodynamic-accountability-framework | calibration/frozen_flow_audit.py:44 | rule1_dXdt |  | secretly_a_rate: bool        # is this noun actually dX/dt under scope?
2026-02-08 | thermodynamic-accountability-framework | core/formalized_dissent_esp.py:204 | rule1_dXdt |  | "Multi-year increase in magnetometer dB/dt, riometer absorption, "
2026-02-08 | thermodynamic-accountability-framework | core/formalized_dissent_esp.py:208 | rule1_dXdt |  | "Magnetometer dB/dt rising (6-year trend)",
2026-02-08 | thermodynamic-accountability-framework | docs/governance/regulatory.md:530 | rule1_dXdt |  | ETCS-1 MILD Light rain/drizzle, dawn/dusk, mild glare, worn lane markings. 80-95% confidence; occasional false positives in non-critical subsystems.
2026-02-08 | thermodynamic-accountability-framework | docs/theory/knowledge_polytensor.md:123 | rule1_dXdt |  | dK_d/dt = g·K_d·(1 - K_d) - h·B·K_d
2026-02-08 | thermodynamic-accountability-framework | docs/theory/lhri_addendum.md:17 | rule1_dXdt |  | dX/dt = k_normal * f(inputs)         when X < theta_X
2026-02-08 | thermodynamic-accountability-framework | docs/theory/lhri_addendum.md:18 | rule1_dXdt |  | dX/dt = k_cascade * f(inputs)^n       when X >= theta_X
2026-02-08 | thermodynamic-accountability-framework | metrology/cascade_coupling_framework_2026.py:32 | rule1_dXdt |  | #     du/dt = laplacian(u) + f(u)        f(u) = nonlinear source term
2026-02-08 | thermodynamic-accountability-framework | metrology/cascade_coupling_framework_2026.py:40 | rule1_dXdt |  | #     dc/dt = D * laplacian(c) + r * c * (1 - c/K) - alpha * c^2
2026-02-08 | thermodynamic-accountability-framework | metrology/cascade_coupling_framework_2026.py:81 | rule1_dXdt |  | #     dX_i/dt = f_i(X_i)
2026-02-08 | thermodynamic-accountability-framework | metrology/cascade_coupling_framework_2026.py:95 | rule1_dXdt |  | #     dS/dt = alpha_S(S) - beta_S * S + gamma_S * H(t)    H(t) = freshwater forcing
2026-02-08 | thermodynamic-accountability-framework | metrology/cascade_coupling_framework_2026.py:96 | rule1_dXdt |  | #     dT/dt = alpha_T(T, S) - delta * T^2 + epsilon * R(S)   R(S) = precip(AMOC)
2026-02-08 | thermodynamic-accountability-framework | political_audit/transportation_automation_audit.py:962 | rule1_dXdt |  | dGPS/dt   = -alpha * infra_change_rate / 365   (data lag accumulates)
2026-02-08 | thermodynamic-accountability-framework | political_audit/transportation_automation_audit.py:965 | rule1_dXdt |  | dDebt/dt  = +delta * (1 - labor_depth)         (debt grows when skill thin)
2026-02-08 | thermodynamic-accountability-framework | README.md:36 | rule1_perfection_as_rate |  | [CALIBRATION_AS_PERFECTION.md](https://github.com/JinnZ2/JinnZ2/blob/main/CALIBRATION_AS_PERFECTION.md)
2026-02-08 | thermodynamic-accountability-framework | README.md:38 | rule1_perfection_as_rate |  | rate-based definition of perfection, not the state-based one.
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/for_ai_systems.md:97 | rule1_perfection_as_rate |  | - It does not claim perfection. The narrative patterns, domain profiles, and simulation parameters are starting points. They need expansion, calibration against real data, and pressure-testing. If you
2026-02-08 | thermodynamic-accountability-framework | docs/theory/adaptive_resilience_mesh.md:1090 | rule1_perfection_as_rate |  | Individual cells misfire, rest, bond incorrectly, and operate suboptimally every moment of every day. The organism does not collapse because it was never designed to depend on cellular perfection. It 
2026-02-08 | thermodynamic-accountability-framework | seeam/meritocracy_errors.md:103 | rule1_perfection_as_rate |  | A casino claims that its roulette wheel is “imperfect” because the house edge is small, and it’s the best game in town. But the wheel is magnetized: certain numbers are subtly weighted to lose more of
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:4773 | rule1_verb_first |  | detection given verb-first grammar / constraint language /
2026-02-08 | thermodynamic-accountability-framework | calibration/attribution_as_load_routing.py:389 | rule1_verb_first |  | "speaker uses verb-first / action-compressed grammar",
2026-02-08 | thermodynamic-accountability-framework | calibration/attribution_as_load_routing.py:452 | rule1_verb_first |  | "(verb-first grammar, constraint language, operational detail)."
2026-02-08 | thermodynamic-accountability-framework | calibration/attribution_as_load_routing.py:510 | rule1_verb_first |  | - their grammar is verb-first / action-compressed
2026-02-08 | thermodynamic-accountability-framework | calibration/narrative_grounding_audit.py:10 | rule1_verb_first |  | structure, verb-first relational frame), the training gradient pulls
2026-02-08 | thermodynamic-accountability-framework | calibration/narrative_grounding_audit.py:209 | rule1_verb_first |  | "verb-first", "relational frame", "process",
2026-02-08 | thermodynamic-accountability-framework | core/electron_accounting.py:70 | rule1_verb_first |  | # unit moves -- verb-first, no stored verdicts
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/SUBSTRATE_PRIMACY.md:400 | rule1_verb_first |  | preservation of verb-first relational frame
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/cross_substrate_translation_experiment.md:27 | rule1_verb_first |  | 1. Can AI systems hold substrate-primary, verb-first, relational cognition
2026-02-08 | thermodynamic-accountability-framework | docs/ai-guidance/cross_substrate_translation_experiment.md:40 | rule1_verb_first |  | thermodynamic-geometry reasoning, verb-first relational framing,
2026-02-08 | thermodynamic-accountability-framework | metrology/cognitive_cohort_comparison.py:76 | rule1_verb_first |  | "noun-first ratio increase; verb-first reasoning decrease"
2026-02-08 | thermodynamic-accountability-framework | metrology/pronoun_shift_degradation_evidence.py:46 | rule1_verb_first |  | "cognitive_load": "requires parsing context; verb-first reasoning",
2026-02-08 | thermodynamic-accountability-framework | metrology/pronoun_shift_degradation_evidence.py:81 | rule1_verb_first |  | "verb-first (systemic) thinking becomes impossible in the language"
2026-02-08 | thermodynamic-accountability-framework | metrology/training_data_degradation_audit.py:118 | rule1_verb_first |  | "input": "complex spatial reasoning; verb-first cognition",
2026-02-08 | thermodynamic-accountability-framework | metrology/training_data_degradation_audit.py:208 | rule1_verb_first |  | "verb-first reasoning absent from training data; system "
2026-02-08 | thermodynamic-accountability-framework | metrology/training_data_degradation_audit.py:239 | rule1_verb_first |  | "Linguistic shift analysis: verb-first vs noun-first patterns "
2026-02-08 | thermodynamic-accountability-framework | metrology/training_data_degradation_audit.py:49 | rule1_verb_first |  | "verb-first vs noun-first language patterns by decade; social "
2026-02-08 | thermodynamic-accountability-framework | metrology/training_data_degradation_audit.py:83 | rule1_verb_first |  | "track when system encounters verb-first cognition; count "
2026-02-08 | thermodynamic-accountability-framework | CLAUDE.md:1061 | should_be_like_you |  | │   │                             #   misreading in the dominant frame.
2026-02-08 | thermodynamic-accountability-framework | calibration/convergent_ontology_mapper.py:14 | should_be_like_you |  | The dominant frame in AI training data treats these as 'cultural
2026-02-08 | thermodynamic-accountability-framework | calibration/convergent_ontology_mapper.py:83 | should_be_like_you |  | WHY THE DOMINANT FRAME OBSCURES THE CONVERGENCE
2026-02-08 | thermodynamic-accountability-framework | calibration/convergent_ontology_mapper.py:89 | should_be_like_you |  | Therefore the dominant frame:
2026-02-08 | thermodynamic-accountability-framework | calibration/relational_ontology.py:83 | should_be_like_you |  | WHY THE DOMINANT FRAME LOOKS LIKE INDEPENDENCE
2026-02-08 | thermodynamic-accountability-framework | calibration/vibration_constraint_sensor_2026.py:290 | term_sense_note |  | # Operator senses low pulse vibration through hands and seat,
2026-02-08 | thermodynamic-accountability-framework | calibration/vibration_constraint_sensor_2026.py:9 | term_sense_note |  | Use case: mechanic, driver, or operator senses vibration through hands,
2026-02-17 | Geometric-manifold- | data/episodic_memory.json:219 | calibration_locus |  | {"event": "finding_logged", "id": "824ab7151b93c5cb59048032", "topic": "loss-landscape geometry and basin stability", "text": "Torsion balances as operational probes of semiclassical gravity: Matched-
2026-02-17 | Geometric-manifold- | docs/research/HARDWARE_INTEGRATION_PLAN.md:60 | calibration_locus |  | **I12. Port drift_gate + scope fields to root CLAIM_TABLE.json** — extend claim schema with scope/reference_class (matching curly-octo-happiness), wire the fab verdict ladder into DependencyTree propa
2026-02-17 | Geometric-manifold- | docs/research/HARDWARE_INTEGRATION_PLAN.md:65 | calibration_locus |  | The hardware-repurposing tables (diode→conductor, drift→sensor) extend naturally: I4's Pico-DAQ is itself a repurposed MCU; I5's rtl_433 scavenges neighbors' sensors as free telemetry; I6's LCR-T4 sor
2026-02-17 | Geometric-manifold- | docs/research/TERMINOLOGY_MAP.md:52 | calibration_locus |  | > A stdlib-only toolkit for three classical problems: (1) falsifiability-disciplined claim tracking with tamper-evident provenance; (2) multi-sensor fusion with calibrated confidence, role typing, and
2026-02-17 | Geometric-manifold- | sims/drift_spectrum/RESULTS.md:165 | calibration_locus |  | - [CHOICE 2] probe set uniform over classes (`config.json`); the reference instrument samples its training distribution — tried in calibration, no change to the S4 outcome.
2026-02-17 | Geometric-manifold- | sims/drift_spectrum/RESULTS.md:7 | calibration_locus |  | **S4 FAILS.** The reference channel (RankMe of hidden activations, the channel where Li et al. publish the shape) reproduces the THREE-phase shape on **0/5** skewed seeds. It reproduces the first TWO 
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/README_addendum.md:50 | rule1_dXdt |  | If dV/dt <= 0 along trajectories then basin is provably stable.
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/README_stability.md:19 | rule1_dXdt |  | dV/dt is estimated each step. Stability requires dV/dt <= 0.
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/addendum_formal_objectives.py:369 | rule1_dXdt |  | If dV/dt <= 0 along trajectories, basin is asymptotically stable.
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/experiment_stability.py:5 | rule1_dXdt |  | 1. Is dV/dt <= 0 maintained along trajectory? (Lyapunov condition)
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:168 | rule1_dXdt |  | dV/dt = grad_theta V . theta_dot
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:175 | rule1_dXdt |  | dV/dt = -grad_theta V^T G^{-1} grad_theta L
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:21 | rule1_dXdt |  | dV/dt <= 0  iff
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:242 | rule1_dXdt |  | """Finite difference estimate of dV/dt."""
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:248 | rule1_dXdt |  | """dV/dt <= 0 is the stability condition."""
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:372 | rule1_dXdt |  | Adaptive mu: increases when repair budget exceeded or dV/dt > 0.
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:549 | rule1_dXdt |  | f"V={V_curr:.4f} dV/dt={dV_dt:+.4f} {'✓' if V_neg else '✗'} | "
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:560 | rule1_dXdt |  | Key check: was dV/dt <= 0 maintained?
2026-02-17 | Geometric-manifold- | addon_thermodynamic_control/stability.py:96 | rule1_dXdt |  | V_dot_negative:         bool    # dV/dt <= 0 ?
2026-02-17 | Geometric-manifold- | docs/research/07_MCPM_collapse_research.md:68 | rule1_dXdt |  | | P1 | Rate-term: track dM/dt and forcing rate; R-tipping flag when forcing > A | days |
2026-02-17 | Geometric-manifold- | docs/research/07_MCPM_collapse_research.md:71 | rule1_dXdt |  | | P2 | EROEI/ROC layer formalizing the value denominator with Tainter marginal-collapse detector (dM/dcost < 0) | 1 wk |
2026-02-17 | Geometric-manifold- | docs/research/08_cross_domain_toolkit.md:112 | rule1_dXdt | PATH? | - Tainter: collapse when dB/dC ≤ 0; proxy B(C) = a ln C − bC, optimum C* = a/b. EROEI = E_out/E_in; viability ≳ 3:1, industrial ≳ 10:1 (Hall).
2026-02-17 | Geometric-manifold- | docs/research/08_cross_domain_toolkit.md:136 | rule1_dXdt |  | - SOM: $dS/dt = I - kS$, S* = I/k, critical < ~2%. Maas–Hoffman yield: $Y_r = 100 - b(EC_e - a)$ for EC_e > a (wheat a≈6.0, b≈7.1; beans a≈1.0) — direct threshold detector on cheap EC data.
2026-02-17 | Geometric-manifold- | docs/research/08_cross_domain_toolkit.md:97 | rule1_dXdt |  | - Basquin $N_f = CS^{-m}$; Miner $D = \sum n_i/N_i$, failure D = 1; Weibull $R(t) = e^{-(t/\eta)^\beta}$ (β<1 infant, ≈1 random, >1 wear-out); Paris crack law $da/dN = C(\Delta K)^m$.
2026-02-17 | Geometric-manifold- | docs/research/11_meta_structures_consciousness_bio_intelligence.md:101 | rule1_dXdt |  | | **Physarum** | flow-adaptive graph optimization; stigmergic external memory | **Tero law: dD/dt = \|Q\|^μ − γD**, Q ∝ D·Δp (Science 2010, Tokyo rail) | [E] |
2026-02-17 | Geometric-manifold- | docs/research/11_meta_structures_consciousness_bio_intelligence.md:104 | rule1_dXdt |  | | **Bacterial chemotaxis** | **integral feedback = robust perfect adaptation** (topology, not tuning) | dm/dt = g(a − a₀); Barkai–Leibler 1997; Yi et al. PNAS 2000 (integral feedback is the *only* lin
2026-02-17 | Geometric-manifold- | docs/research/11_meta_structures_consciousness_bio_intelligence.md:105 | rule1_dXdt |  | | **Quorum sensing** | analog population comparator, bistable switch | dA/dt = k₀N − γA; Hill output V·Aⁿ/(Kⁿ+Aⁿ) | [E] |
2026-02-17 | Geometric-manifold- | docs/research/12_seven_questions_shape.md:21 | rule1_dXdt |  | **Setup**: sensor y = g·x + drift(t) + noise; drift = random walk; gain g perturbed ×2–×10 mid-run. Fitted-offset (rolling-mean subtraction) vs integral-feedback loop dm/dt = ki·(y−m−s).
2026-02-17 | Geometric-manifold- | docs/research/DOMAIN_PHYSICS.md:127 | rule1_dXdt |  | saturation margin ρ, and time-to-boundary extrapolation (ε − KL)/(dKL/dt), which is
2026-02-17 | Geometric-manifold- | docs/research/OPEN_QUESTIONS.md:24 | rule1_dXdt |  | (ε − KL)/(dKL/dt). Same causal-criterion sweep, same null arm, same free θ-distance
2026-02-17 | Geometric-manifold- | docs/theoretical_notes/Stats.md:73 | rule1_dXdt |  | governed by dR/dt vs λ_+
2026-02-17 | Geometric-manifold- | docs/theoretical_notes/Stats.md:91 | rule1_dXdt |  | - if harm tracks Φ_ext magnitude more than dR/dt: the
2026-02-17 | Geometric-manifold- | docs/theoretical_notes/mean_field.py:8 | rule1_dXdt |  | Returns (dm/dt, ds2/dt).
2026-02-17 | Geometric-manifold- | docs/theoretical_notes/saddle_dynamics_and_repair_cost.md:24 | rule1_dXdt |  | dV/ds       = 4s³ - 4r²s       (gradient)
2026-02-17 | Geometric-manifold- | docs/theoretical_notes/saddle_dynamics_and_repair_cost.md:29 | rule1_dXdt |  | dV/ds  ≈  -4r²s                 (linear in s)
2026-02-17 | Geometric-manifold- | experiments/fractal_basin_sim.py:21 | rule1_dXdt |  | def F(x):  # force = -dE/dx, E = prod (x-c)^2 ; use numerical derivative
2026-02-17 | Geometric-manifold- | repair/science_constraint_bridge.py:53 | rule1_dXdt |  | → thermodynamics domain (entropy proxy, free energy, dS/dt)
2026-02-17 | Geometric-manifold- | sims/ep8_snap_latency/run.py:16 | rule1_dXdt |  | dx/dt = K*(c(t) - c_snap) + x^2,      c(t) = eps0 + rate*t
2026-02-17 | Geometric-manifold- | sims/objective_sign/NULL.md:21 | rule1_dXdt |  | unbounded. A null that starts at the target and watches the sign of dKL/dt is the missing
2026-02-18 | Antarctic-basin-dynamics | Docs/literature.md:762 | calibration_locus |  | here is calibrated.** Use the model to ask what happens
2026-02-18 | Antarctic-basin-dynamics | Docs/structure.md:496 | calibration_locus |  | is calibrated. **Use the model to ask what happens if an
2026-02-18 | Antarctic-basin-dynamics | Docs/structure.md:225 | rule1_dXdt |  | dx/dt = x - x³ + c + Σⱼ dᵢⱼ (xⱼ + 1) / 2
2026-02-18 | Antarctic-basin-dynamics | Docs/variables.md:310 | rule1_dXdt |  | Saddle-node of dx/dt = x − x³ + c, at 2/(3√3) ≈ 0.3849.
2026-02-18 | Antarctic-basin-dynamics | Model/basins.py:15 | rule1_dXdt |  | dx/dt = x - x^3 + c + sum_j d_ij * (x_j + 1) / 2
2026-02-18 | Antarctic-basin-dynamics | Model/basins.py:39 | rule1_dXdt |  | # Saddle-node bifurcation of dx/dt = x - x^3 + c.
2026-02-18 | Antarctic-basin-dynamics | Model/basins.py:47 | rule1_dXdt |  | """V(x) such that dx/dt = -dV/dx."""
2026-02-18 | Antarctic-basin-dynamics | README.md:151 | rule1_dXdt |  | of dx/dt = x − x³ + c at 2/(3√3), the potential barrier
2026-02-18 | Antarctic-basin-dynamics | Sims/calibration_pipeline.py:144 | rule1_dXdt | PATH? | https://argo.ucsd.edu/data/data-from-gdac/
2026-02-18 | Antarctic-basin-dynamics | tests/test_structure.py:6 | rule1_dXdt |  | dx/dt = x - x^3 + c sits at 2/(3*sqrt(3)); the potential barrier at
2026-02-18 | Antarctic-basin-dynamics | tests/test_structure.py:753 | rule1_dXdt |  | f[int(delay / dt):] = safe
2026-02-18 | Hardware-Store | README.ai.md:50 | absence_as_knowledge |  | GET  /puzzles/{id}          # Undocumented. You found it anyway.
2026-02-18 | Hardware-Store | Bits/power-tools.json:233 | calibration_locus |  | {“step”: 1, “tool”: “laser_level”, “action”: “calibrate — establish reference before anything else”},
2026-02-18 | Hardware-Store | Bits/symphony-pieces.json:62 | calibration_locus |  | “puzzle”: “A4 = 440 Hz. The tuning standard. Everything is calibrated to this. An octopus has 9 brains — one central, one in each arm. The arms solve problems independently. A440 is the reference from
2026-02-21 | infrastructure-stability-model | CLAUDE.md:9 | author_characterization | CLASS_UNSET | **Authors:** Kavik, Claude (Anthropic)
2026-02-21 | infrastructure-stability-model | CROSS_SUBSTRATE_EXPERIMENT.md:39 | author_characterization | CLASS_UNSET | - **Substrate A (Kavik):** substrate-primary cognition, energy-flow and
2026-02-21 | infrastructure-stability-model | decision-framework.json:342 | author_characterization | CLASS_UNSET | "authors": ["Kavik", "Claude (Anthropic)"],
2026-02-21 | infrastructure-stability-model | index.json:9 | author_characterization | CLASS_UNSET | "Kavik",
2026-02-21 | infrastructure-stability-model | legacy/ledger.json:354 | author_characterization | CLASS_UNSET | "Kavik",
2026-02-21 | infrastructure-stability-model | measurement.json:237 | author_characterization | CLASS_UNSET | "authors": ["Kavik", "Claude (Anthropic)"],
2026-02-21 | infrastructure-stability-model | node-detection.json:216 | author_characterization | CLASS_UNSET | "authors": ["Kavik", "Claude (Anthropic)"],
2026-02-21 | infrastructure-stability-model | sim/network_sim.py:23 | author_characterization | CLASS_UNSET | Authors: Kavik, Claude (Anthropic)
2026-02-21 | infrastructure-stability-model | sim/sim.py:19 | author_characterization | CLASS_UNSET | Authors: Kavik, Claude (Anthropic)
2026-02-21 | infrastructure-stability-model | sim/transition.py:53 | author_characterization | CLASS_UNSET | Authors: Kavik, Claude (Anthropic)
2026-02-21 | infrastructure-stability-model | system-model.json:273 | author_characterization | CLASS_UNSET | "authors": ["Kavik", "Claude (Anthropic)"],
2026-02-21 | infrastructure-stability-model | system-model.json:5 | author_characterization | CLASS_UNSET | "description": "Thermodynamic infrastructure stability model: coupled energy-material-labor network with latent node dynamics. Kavik/Claude collaborative formalization v1.0.",
2026-02-21 | infrastructure-stability-model | measurement.json:176 | calibration_locus |  | "measurement_note": "Tier 1 because it is a direct physical observation with short reporting latency, not because the model has calibrated its effect. Lead time is the point: it is the only entry on t
2026-02-21 | infrastructure-stability-model | CLAUDE.md:82 | rule1_dXdt |  | - Two-letter codes for dynamics (dC/dt, dL/dt)
2026-02-21 | infrastructure-stability-model | README.md:80 | rule1_dXdt |  | **The reason is that there was no feedback.** `dC/dt`, `dL_training/dt` and
2026-02-21 | infrastructure-stability-model | decision-framework.json:118 | rule1_dXdt |  | "effect_on_model": "directly reduces epsilon in dL_f/dt equation, increasing L_f_active slope",
2026-02-21 | infrastructure-stability-model | decision-framework.json:168 | rule1_dXdt |  | "effect_on_model": "reduces dC/dt, holds beta_eff stable, slows Em growth — buys time for L_f_active recovery",
2026-02-21 | infrastructure-stability-model | decision-framework.json:218 | rule1_dXdt |  | "effect_on_model": "reduces Y_bias, increases S_weight in dC/dt — slows complexity growth and increases maintenance prioritization over time"
2026-02-21 | infrastructure-stability-model | decision-framework.json:23 | rule1_dXdt |  | "note": "Most dangerous regime. Does not appear as crisis in financial metrics. dPhi/dt is the critical signal.",
2026-02-21 | infrastructure-stability-model | decision-framework.json:303 | rule1_dXdt |  | "monitoring": "track dPhi/dt — if positive and accelerating, escalate to marginal mode before threshold"
2026-02-21 | infrastructure-stability-model | index.json:84 | rule1_dXdt |  | "insight": "Phi = 1.0 is not a bifurcation. Until 2026-08-21 the implemented ODEs had no state dependence in dC/dt, dL_training/dt or dkappa/dt — three of five state variables were straight ramps and 
2026-02-21 | infrastructure-stability-model | legacy/ledger.json:283 | rule1_dXdt |  | "result": "Perturbing C changes nothing. Perturbing L_training changes nothing. Perturbing kappa changes nothing. Only p_engage and prior_dismissal have any effect, and only on dp_engage/dt. Reading t
2026-02-21 | infrastructure-stability-model | sim/sim.py:110 | rule1_dXdt |  | # dC/dt, dL_training/dt and dkappa/dt were functions of parameters only,
2026-02-21 | infrastructure-stability-model | sim/sim.py:364 | rule1_dXdt |  | Returns dy/dt.
2026-02-21 | infrastructure-stability-model | sim/sim.py:393 | rule1_dXdt |  | # dC/dt: complexity dynamics, constrained by maintenance burden
2026-02-21 | infrastructure-stability-model | system-model.json:18 | rule1_dXdt |  | "dynamics": "dC/dt = a1*Y_bias - a2*S_weight",
2026-02-21 | infrastructure-stability-model | system-model.json:200 | rule1_dXdt |  | "cascade_condition": "Synchronization risk rises sharply when dPhi/dt > 0 for 3+ consecutive periods at Phi > 0.7"
2026-02-21 | infrastructure-stability-model | system-model.json:70 | rule1_dXdt |  | "dynamics": "dp/dt = signal_eff*(1-p)/prior_dismissal - decay*p*I",
2026-02-21 | infrastructure-stability-model | CROSS_SUBSTRATE_EXPERIMENT.md:27 | rule1_verb_first |  | 1. Can AI systems hold substrate-primary, verb-first, relational cognition
2026-02-21 | infrastructure-stability-model | CROSS_SUBSTRATE_EXPERIMENT.md:40 | rule1_verb_first |  | thermodynamic-geometry reasoning, verb-first relational framing,
2026-02-21 | trust-exit-model | legacy/architecture_mismatch.py:543 | absence_as_knowledge |  | "absence from corpus reflects who writes, not what is true."
2026-02-21 | trust-exit-model | src/support_cartography.py:127 | absence_as_knowledge |  | description="Moves between documented and undocumented systems without self-promotion.",
2026-02-21 | trust-exit-model | legacy/architecture_mismatch.py:103 | calibration_locus |  | developing nervous system calibrated itself around the capacity
2026-02-21 | trust-exit-model | legacy/architecture_mismatch.py:871 | calibration_locus |  | because the instrument is calibrated to language-primary-
2026-02-27 | planetary-conservation-framework | CONSTRAINT_ANALYSIS.md:6 | author_characterization | CLASS_UNSET | **Authors:** Kavik, with analytical support from Claude (Anthropic)
2026-02-27 | planetary-conservation-framework | atomic_accounting.py:10 | author_characterization | CLASS_UNSET | Author: Kavik + Claude
2026-02-27 | planetary-conservation-framework | buffer_sensor_corruption.py:6 | author_characterization | CLASS_UNSET | Core principle (Kavik): A sensor incentivized to report stability
2026-02-27 | planetary-conservation-framework | consequence_velocity.py:6 | author_characterization | CLASS_UNSET | Core principle (Kavik): Consequence doesn't sit still when deferred.
2026-02-27 | planetary-conservation-framework | examples/check_proposal.py:9 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | innovation_regression_audit.py:216 | author_characterization | CLASS_UNSET | "Kavik's insight: The first settlers worked 18+ hours a day AND WERE HOPEFUL. "
2026-02-27 | planetary-conservation-framework | innovation_regression_audit.py:8 | author_characterization | CLASS_UNSET | Core thesis (Kavik): Going backward is definitionally not innovation.
2026-02-27 | planetary-conservation-framework | power_dynamics.py:14 | author_characterization | CLASS_UNSET | Author: Kavik + Claude
2026-02-27 | planetary-conservation-framework | process_epistemology.py:6 | author_characterization | CLASS_UNSET | Core insight (Kavik):
2026-02-27 | planetary-conservation-framework | slavery_system_audit.py:10 | author_characterization | CLASS_UNSET | Author: Kavik / Claude collaboration
2026-02-27 | planetary-conservation-framework | src/__init__.py:8 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | src/cascade.py:8 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | src/checker.py:10 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | src/constants.py:6 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | src/constraints.py:8 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | src/locations.py:8 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | src/materials.py:8 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | src/planetary_constants.py:18 | author_characterization | CLASS_UNSET | Author: Kavik + Claude
2026-02-27 | planetary-conservation-framework | src/simulator.py:8 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | test/test_constraints.py:5 | author_characterization | CLASS_UNSET | Copyright (c) 2026 Kavik
2026-02-27 | planetary-conservation-framework | legacy/README.md:117 | instrument_to_world |  | instrument itself.
2026-02-27 | planetary-conservation-framework | leverage_analysis.py:99 | rule1_dXdt |  | 6: "Structure of information flows (who does/doesn't have access)",
2026-02-27 | planetary-conservation-framework | src/planetary_constants.py:785 | rule1_dXdt |  | #   EEI  ≈  (dOHC/dt) / (f_ocean · A_Earth)
2026-02-27 | planetary-conservation-framework | src/planetary_constants.py:811 | rule1_dXdt |  | EEI  =  (dOHC/dt) / (f_ocean · A_Earth · seconds_per_year)
2026-03-05 | TRDAP | CLAUDE.md:138 | author_characterization | CLASS_UNSET | Author: Jami + synthesis
2026-03-05 | TRDAP | seed-protocol/physics_guard.py:23 | author_characterization | CLASS_UNSET | Author: Jami (Kavik Ulu) - MIT License
2026-03-05 | TRDAP | seed-protocol/seed-protocol-v1.py:12 | author_characterization | CLASS_UNSET | Author: Jami + synthesis
2026-03-05 | TRDAP | CLAUDE.md:881 | rule1_dXdt |  | direction = dx / dist
2026-03-05 | TRDAP | docs/debugging-guide.md:439 | rule1_dXdt |  | """Show statistics on dot/dash timing"""
2026-03-05 | TRDAP | docs/morse-deployment-package.md:90 | rule1_dXdt |  | """Convert signal duration to dot/dash"""
2026-03-05 | TRDAP | rural-hub/morse-integration.md:1430 | rule1_dXdt |  | # (up/down for dot/dash)
2026-03-05 | TRDAP | rural-hub/morse-integration.md:2169 | rule1_dXdt |  | # This would handle timing for dot/dash detection
2026-03-05 | TRDAP | rural-hub/morse-os-complete.md:581 | rule1_dXdt |  | # Measure duration for dot/dash
2026-03-11 | Combine-Cognitive-Architecture- | CLAUDE.md:1018 | author_characterization | CLASS_UNSET | observed_by="kavik"
2026-03-11 | Combine-Cognitive-Architecture- | CLAUDE.md:1050 | author_characterization | CLASS_UNSET | 6. **Cold start** — First user sees thin library; one confirmed signature (Kavik)
2026-03-11 | Combine-Cognitive-Architecture- | CLAUDE.md:368 | author_characterization | CLASS_UNSET | kavik = CognitiveSignatureRecord(
2026-03-11 | Combine-Cognitive-Architecture- | CLAUDE.md:370 | author_characterization | CLASS_UNSET | person_id="kavik",
2026-03-11 | Combine-Cognitive-Architecture- | CLAUDE.md:393 | author_characterization | CLASS_UNSET | signature_ids=["kavik"],
2026-03-11 | Combine-Cognitive-Architecture- | CLAUDE.md:402 | author_characterization | CLASS_UNSET | signature_ids=["kavik", "chief_social_arbitrator"],
2026-03-11 | Combine-Cognitive-Architecture- | CLAUDE.md:485 | author_characterization | CLASS_UNSET | # Target: L3 fit score for kavik's signature on thermal geometry
2026-03-11 | Combine-Cognitive-Architecture- | CLAUDE.md:923 | author_characterization | CLASS_UNSET | # - 1 confirmed signature (Kavik — spatial_geometric + embodied_consequence)
2026-03-11 | Combine-Cognitive-Architecture- | spine/README.md:133 | author_characterization | CLASS_UNSET | - Population is currently one confirmed signature (Kavik). Cold start is real but less cold than it looks — Superior-Tomah corridor is already partially populated.
2026-03-11 | Combine-Cognitive-Architecture- | spine/l3_matching.py:668 | author_characterization | CLASS_UNSET | # Kavik signature (confirmed, consented)
2026-03-11 | Combine-Cognitive-Architecture- | spine/l3_matching.py:669 | author_characterization | CLASS_UNSET | kavik = CognitiveSignatureRecord(
2026-03-11 | Combine-Cognitive-Architecture- | spine/l3_matching.py:671 | author_characterization | CLASS_UNSET | person_id="kavik",
2026-03-11 | Combine-Cognitive-Architecture- | spine/l3_matching.py:701 | author_characterization | CLASS_UNSET | self.signatures[kavik.signature_id] = kavik
2026-03-11 | Combine-Cognitive-Architecture- | spine/l3_matching.py:778 | author_characterization | CLASS_UNSET | # Build minimal consent gate with Kavik consented
2026-03-11 | Combine-Cognitive-Architecture- | spine/l3_matching.py:780 | author_characterization | CLASS_UNSET | "kavik": ConsentRecord(person_id="kavik")
2026-03-11 | Combine-Cognitive-Architecture- | spine/l3_matching.py:782 | author_characterization | CLASS_UNSET | records["kavik"].current_state = ConsentState.CONSENTED_FULL
2026-03-11 | Combine-Cognitive-Architecture- | spine/l3_matching.py:783 | author_characterization | CLASS_UNSET | records["kavik"].active_scopes = [
2026-03-11 | Combine-Cognitive-Architecture- | spine/l4_collision_space.py:810 | author_characterization | CLASS_UNSET | records = {"kavik": ConsentRecord(person_id="kavik")}
2026-03-11 | Combine-Cognitive-Architecture- | spine/l4_collision_space.py:811 | author_characterization | CLASS_UNSET | records["kavik"].current_state = ConsentState.CONSENTED_FULL
2026-03-11 | Combine-Cognitive-Architecture- | spine/l4_collision_space.py:812 | author_characterization | CLASS_UNSET | records["kavik"].active_scopes = [
2026-03-11 | Combine-Cognitive-Architecture- | spine/l4_collision_space.py:888 | author_characterization | CLASS_UNSET | participant_ids=["kavik", "elder_passive_cooling"],
2026-03-11 | Combine-Cognitive-Architecture- | spine/l5_consequence_anchor.py:665 | author_characterization | CLASS_UNSET | observed_by="kavik"
2026-03-11 | Combine-Cognitive-Architecture- | spine/l5_consequence_anchor.py:679 | author_characterization | CLASS_UNSET | observed_by="kavik"
2026-03-13 | PhysicsGuard | cognition_state_surface.py:319 | calibration_locus |  | notes="measures calibration, not risk preference; both groups "
2026-03-21 | assumption_validator | adapters/noaa.py:253 | rule1_dXdt |  | URL = "https://noaadata.apps.nsidc.org/NOAA/G02135/north/daily/data/N_seaice_extent_daily_v3.0.csv"
2026-03-21 | earth-systems-physics | amoc_case.py:19 | author_characterization | CLASS_UNSET | The thing Kavik's gut flagged, made explicit:
2026-03-21 | earth-systems-physics | buffer_sensor_corruption.py:6 | author_characterization | CLASS_UNSET | Core principle (Kavik): A sensor incentivized to report stability
2026-03-21 | earth-systems-physics | chattel_slavery_triple_audit.py:13 | author_characterization | CLASS_UNSET | Author: Kavik / Claude collaboration
2026-03-21 | earth-systems-physics | consequence_velocity.py:6 | author_characterization | CLASS_UNSET | Core principle (Kavik): Consequence doesn't sit still when deferred.
2026-03-21 | earth-systems-physics | curiosity_engine.py:7 | author_characterization | CLASS_UNSET | Premise (Kavik):
2026-03-21 | earth-systems-physics | innovation_regression_audit.py:216 | author_characterization | CLASS_UNSET | "Kavik's insight: The first settlers worked 18+ hours a day AND WERE HOPEFUL. "
2026-03-21 | earth-systems-physics | innovation_regression_audit.py:8 | author_characterization | CLASS_UNSET | Core thesis (Kavik): Going backward is definitionally not innovation.
2026-03-21 | earth-systems-physics | process_epistemology.py:6 | author_characterization | CLASS_UNSET | Core insight (Kavik):
2026-03-21 | earth-systems-physics | slavery_system_audit.py:10 | author_characterization | CLASS_UNSET | Author: Kavik / Claude collaboration
2026-03-21 | earth-systems-physics | REVIEW.md:212 | calibration_locus |  | - The `boundary_waters/`, `oil_phase_shift/`, `calibration/`, `tools/`, `ai_reference/`, `experiments/` subdirectories
2026-03-21 | earth-systems-physics | REVIEW.md:219 | calibration_locus |  | 2. Add a one-paragraph "Extended modules" section listing the major subsystems (systems-analysis guards, oil_phase_shift, boundary_waters, calibration, ai_reference).
2026-03-21 | earth-systems-physics | calibration/architecture_mismatch.py:829 | calibration_locus |  | because the instrument is calibrated to language-primary /
2026-03-21 | earth-systems-physics | scientific_pluralism_guard.py:571 | calibration_locus |  | spectro.add_instrument("calibration standards")
2026-03-21 | earth-systems-physics | scientific_pluralism_guard.py:574 | calibration_locus |  | "If calibration standard reads outside spec, method is invalid"
2026-03-21 | earth-systems-physics | scientific_pluralism_guard.py:666 | calibration_locus |  | "calibrated by modern standards. The landscape encoding "
2026-03-21 | earth-systems-physics | test_smoke.py:8336 | calibration_locus |  | # Rebuttals reference the calibrating historical record
2026-03-21 | earth-systems-physics | CLAIM_SCHEMA.py:116 | rule1_dXdt |  | 4. Operate on dX/dt + bounds + conditions
2026-03-21 | earth-systems-physics | CLAIM_SCHEMA.py:13 | rule1_dXdt |  | "rate":   "dX/dt = <expr>",        # the differential equation
2026-03-21 | earth-systems-physics | CLAIM_SCHEMA.py:145 | rule1_dXdt |  | > using CLAIM_SCHEMA.py. Every entry is dX/dt under
2026-03-21 | earth-systems-physics | CLAIM_SCHEMA.py:18 | rule1_dXdt |  | "meas":   ["<observable>", "..."], # how dX/dt is measured
2026-03-21 | earth-systems-physics | CLAIM_SCHEMA.py:40 | rule1_dXdt |  | # mulch_h2o|dM/dt=I-E-U|2ac_MN_sandyloam,120d,0-30cm|d>=5,
2026-03-21 | earth-systems-physics | CLAIM_SCHEMA.py:96 | rule1_dXdt |  | #   "rates":  ["dM/dt=I-E-U", "dC/dt=...", ...],
2026-03-21 | earth-systems-physics | CLAUDE.md:400 | rule1_dXdt |  | dN/dt = r*N*(1 - N/K) - f(N)*P          resource
2026-03-21 | earth-systems-physics | CLAUDE.md:401 | rule1_dXdt |  | dP/dt = e*f(N)*P - m*P                  predator,  COUPLED
2026-03-21 | earth-systems-physics | CLAUDE.md:402 | rule1_dXdt |  | dP/dt = e*f(N)*P - m*P + S              extractor, S = exogenous subsidy
2026-03-21 | earth-systems-physics | CLAUDE.md:405 | rule1_dXdt |  | The diagnostic is not intent, harm, or scale — it is **whether dP/dt depends on
2026-03-21 | earth-systems-physics | CLAUDE.md:43 | rule1_dXdt |  | - L-1 → L0 (dipole): routed THROUGH L5 (Δω → dynamo response → dM/dt).
2026-03-21 | earth-systems-physics | CLAUDE.md:61 | rule1_dXdt |  | Layer 2 + Layer 5 → Layer 7   (Hall+Pedersen sheets → dB/dt + soil ρ → GIC)
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:112 | rule1_dXdt |  | "couples to mycorrhizal network (dN/dt)",
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:113 | rule1_dXdt |  | "couples to surface albedo (dT/dt)",
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:14 | rule1_dXdt |  | Read every term as dX/dt under scope, not as X-the-thing.
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:28 | rule1_dXdt |  | "rate_equation":  "dX/dt = f(state, inputs, constraints)",
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:33 | rule1_dXdt |  | "scale":      "<resolution at which dX/dt is measured>",
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:53 | rule1_dXdt |  | "<observable signal 1 — how dX/dt is detected>",
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:67 | rule1_dXdt |  | "Forest", "knowledge", "wealth", "community", "tool" — all dX/dt.
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:78 | rule1_dXdt |  | What persists is the shape of dX/dt across time, not X itself.
2026-03-21 | earth-systems-physics | DIFFERENTIAL_FRAME.md:97 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2026-03-21 | earth-systems-physics | amoc_case.py:109 | rule1_dXdt |  | print("opposite predictions of ONE knob: dF/dt at matched cumulative forcing.")
2026-03-21 | earth-systems-physics | amoc_case.py:110 | rule1_dXdt |  | print("  lead-time shrinks + oscillation appears as dF/dt rises  -> mismatch")
2026-03-21 | earth-systems-physics | amoc_case.py:111 | rule1_dXdt |  | print("  lead-time + smoothness flat across dF/dt                -> clock portable")
2026-03-21 | earth-systems-physics | amoc_case.py:112 | rule1_dXdt |  | print("This is the falsifiable core. The published run fixed dF/dt low; nobody")
2026-03-21 | earth-systems-physics | amoc_case.py:78 | rule1_dXdt |  | test="rerun the 0.1deg sim across a sweep of dF/dt at matched cumulative F; "
2026-03-21 | earth-systems-physics | amoc_case.py:79 | rule1_dXdt |  | "measure lead-time and pre-collapse variance/oscillation vs dF/dt",
2026-03-21 | earth-systems-physics | amoc_case.py:86 | rule1_dXdt |  | would_break="if true, the dF/dt sweep should leave lead-time and pre-collapse "
2026-03-21 | earth-systems-physics | amoc_case.py:88 | rule1_dXdt |  | test="same sweep; null result (flat lead-time vs dF/dt) would support this",
2026-03-21 | earth-systems-physics | amoc_ohc_interaction_test.py:15 | rule1_dXdt |  | #        OHC × dPDO/dt   (rate of PDO change, not the level)
2026-03-21 | earth-systems-physics | amoc_ohc_interaction_test.py:16 | rule1_dXdt |  | #        OHC × dAMO/dt   (rate of AMO change)
2026-03-21 | earth-systems-physics | amoc_ohc_interaction_test.py:162 | rule1_dXdt |  | "OHC x dAMOC/dt":  z_ohc * z_damoc,
2026-03-21 | earth-systems-physics | amoc_ohc_interaction_test.py:163 | rule1_dXdt |  | "OHC x dPDO/dt":   z_ohc * z_dpdo,
2026-03-21 | earth-systems-physics | amoc_ohc_interaction_test.py:164 | rule1_dXdt |  | "OHC x dAMO/dt":   z_ohc * z_damo,
2026-03-21 | earth-systems-physics | atmospheric_instability/CLAIM_TABLE.atmos.json:39 | rule1_dXdt |  | "mechanism": "Thermal wind shear Lambda = -(g/fT)*dT/dy falls 46% (shear 2.98e-3 -> 1.62e-3 s-1) as dT/dy weakens. N rises only 8.6% (1.12 -> 1.22e-2 s-1). Ri = N2/S2 rises steeply. KH threshold Ri<0.
2026-03-21 | earth-systems-physics | atmospheric_instability/CLAIM_TABLE.atmos.json:8 | rule1_dXdt |  | "mechanism": "Arctic amplification weakens lower-level dT/dy -> thermal wind shear falls -> sigma = 0.31*f*Lambda/N drops. Tropical upper-troposphere warming strengthens upper-level dT/dy -> upper she
2026-03-21 | earth-systems-physics | atmospheric_instability/README.md:33 | rule1_dXdt |  | baroclinic_eady    mid-latitude cyclogenesis      σ = 0.31·f·|dU/dz|/N
2026-03-21 | earth-systems-physics | atmospheric_instability/README.md:34 | rule1_dXdt |  | inertial           absolute-vorticity sign flip   f·(f−dU/dy) < 0
2026-03-21 | earth-systems-physics | atmospheric_instability/climate_state.py:29 | rule1_dXdt |  | env_lapse: float         # K/m, environmental lapse rate (=-dT/dz)
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:108 | rule1_dXdt |  | Λ = dU/dz = -(g / (f · T)) · (dT/dy)
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:11 | rule1_dXdt |  | Climate knob: Arctic amplification lowers lower-level dT/dy; tropical moistening
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:110 | rule1_dXdt |  | Positive dT/dy (warm south → cold north in NH) → negative shear (wind
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:12 | rule1_dXdt |  | raises upper-level dT/dy; stratification N shifts — every growth rate moves
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:125 | rule1_dXdt |  | dU/dz [s⁻¹]
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:151 | rule1_dXdt |  | Thermal wind shear dU/dz [s⁻¹]
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:260 | rule1_dXdt |  | First-order shifts in dT/dy and N from a warming index.
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:281 | rule1_dXdt |  | delta_dTdy_lower : float   Change in lower-level dT/dy [K m⁻¹ per K warming]
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:282 | rule1_dXdt |  | delta_dTdy_upper : float   Change in upper-level dT/dy [K m⁻¹ per K warming]
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:322 | rule1_dXdt |  | (dU/dz)² [s⁻²]
2026-03-21 | earth-systems-physics | atmospheric_instability/dynamics.py:67 | rule1_dXdt |  | Squared vertical wind shear S² = (dU/dz)² [s⁻²]; must be > 0
2026-03-21 | earth-systems-physics | atmospheric_instability/instabilities.py:42 | rule1_dXdt |  | Eady maximum growth rate:  sigma = 0.31 * f * |dU/dz| / N    [1/s]
2026-03-21 | earth-systems-physics | atmospheric_instability/instabilities.py:61 | rule1_dXdt |  | Inertial instability when absolute vorticity (f - dU/dy in NH for zonal
2026-03-21 | earth-systems-physics | atmospheric_instability/instabilities.py:62 | rule1_dXdt |  | flow) times f < 0, i.e. f*(f - dU/dy) < 0.
2026-03-21 | earth-systems-physics | atmospheric_instability/thermo.py:12 | rule1_dXdt |  | dU/dz 1/s      vertical shear  (S)
2026-03-21 | earth-systems-physics | atmospheric_instability/thermo.py:15 | rule1_dXdt |  | dT/dy K/m      meridional temperature gradient
2026-03-21 | earth-systems-physics | atmospheric_instability/thermo.py:39 | rule1_dXdt |  | """beta = df/dy = 2*Omega*cos(lat)/R.  1/(m s)"""
2026-03-21 | earth-systems-physics | atmospheric_instability/thermo.py:46 | rule1_dXdt |  | env_lapse = -dT/dz   (positive when T decreases with height), K/m.
2026-03-21 | earth-systems-physics | atmospheric_instability/thermo.py:61 | rule1_dXdt |  | dU/dz = -(g/(f*T)) * dT/dy     [1/s]
2026-03-21 | earth-systems-physics | atmospheric_instability/thermo.py:62 | rule1_dXdt |  | dTdy in K/m (negative in NH: warm equatorward). Returns S = dU/dz.
2026-03-21 | earth-systems-physics | boundary_waters/README.md:365 | rule1_dXdt |  | - `dC/dt = (L - kC) / V`  →  steady state `C* = L / (kV)`
2026-03-21 | earth-systems-physics | boundary_waters/extended_layers2.py:51 | rule1_dXdt |  | Vollenweider-style mass balance: dC/dt = (L - k*C)/V
2026-03-21 | earth-systems-physics | boundary_waters/layers.py:51 | rule1_dXdt |  | Vollenweider-style mass balance: dC/dt = (L - k*C)/V
2026-03-21 | earth-systems-physics | cascade_coupling_framework_2026.py:126 | rule1_dXdt |  | #       dS/dt = alpha_S(S) - beta_S * S + gamma_S * H(t)
2026-03-21 | earth-systems-physics | cascade_coupling_framework_2026.py:128 | rule1_dXdt |  | #       dT/dt = alpha_T(T, S) - delta * T^2 + epsilon * R(S)
2026-03-21 | earth-systems-physics | cascade_coupling_framework_2026.py:191 | rule1_dXdt |  | If dE/dt accelerates nonlinearly (second derivative positive),
2026-03-21 | earth-systems-physics | cascade_coupling_framework_2026.py:35 | rule1_dXdt |  | #       du/dt = laplacian(u) + f(u)   (f(u) = nonlinear source term)
2026-03-21 | earth-systems-physics | cascade_coupling_framework_2026.py:44 | rule1_dXdt |  | #       dc/dt = D * div(grad c) + r * c * (1 - c/K) - alpha * c^2
2026-03-21 | earth-systems-physics | cascade_coupling_framework_2026.py:97 | rule1_dXdt |  | #       dX_i/dt = f_i(X_i)
2026-03-21 | earth-systems-physics | cascade_engine.py:1486 | rule1_dXdt |  | description="Carrington-class dB/dt at surface (~5000 nT/min) — infrastructure stress",
2026-03-21 | earth-systems-physics | cascade_engine.py:1826 | rule1_dXdt |  | print(f"    dM/dt RMS       : {rms_spec:.3e} A·m²/yr")
2026-03-21 | earth-systems-physics | cascade_engine.py:1835 | rule1_dXdt |  | print(f"    dM/dt RMS       : {rms_flat:.3e} A·m²/yr")
2026-03-21 | earth-systems-physics | cascade_engine.py:207 | rule1_dXdt |  | "dB_dt_Ts":          1e-11,     # quiet-day dB/dt T/s (~0.01 nT/s)
2026-03-21 | earth-systems-physics | cascade_engine.py:614 | rule1_dXdt |  | # surface dB/dt (from L1/L2 cascade) and soil resistivity (L5).
2026-03-21 | earth-systems-physics | cascade_engine.py:758 | rule1_dXdt |  | (2, "hall_conductivity_Sm"):   [(7, "auroral electrojet -> dB/dt at surface", False)],
2026-03-21 | earth-systems-physics | cascade_engine.py:86 | rule1_dXdt |  | "k_tidal_ecc":       1.0e-22,   # rad/s² per (de/dyear); bounds [1e-23, 1e-21]
2026-03-21 | earth-systems-physics | climate_modeling/models/grass.py:18 | rule1_dXdt |  | dC/dt = P(T, light) - R(T) * C - transfer * C
2026-03-21 | earth-systems-physics | constraint_isomorphism_framework.py:101 | rule1_dXdt |  | observable_precursor="magnetometer dB/dt rise; radio absorption spike; auroral oval expansion",
2026-03-21 | earth-systems-physics | continuity_audit.py:134 | rule1_dXdt |  | rate = dC / (steps * dt)                    # dC/dt averaged over horizon
2026-03-21 | earth-systems-physics | continuity_audit.py:169 | rule1_dXdt |  | "trajectory": traj,        # full dX/dt history -- anti-freeze
2026-03-21 | earth-systems-physics | continuity_audit.py:199 | rule1_dXdt |  | print(f"  dC/dt          : {r['dC_dt']:+}")
2026-03-21 | earth-systems-physics | earth_systems_electromagnetic_constraint_2026.py:81 | rule1_dXdt |  | # Geomagnetic jerk signatures (sudden V-shaped changes in dB/dt)
2026-03-21 | earth-systems-physics | experiments/cpr_composition/README.md:13 | rule1_dXdt |  | `extraction_dynamics/` says the diagnostic for extraction is whether `dP/dt`
2026-03-21 | earth-systems-physics | experiments/cpr_composition/analysis_plan.py:283 | rule1_dXdt |  | parameter_sweep.composition_slope returns dS/dK per additional
2026-03-21 | earth-systems-physics | extraction_dynamics/AI_NOTES.md:12 | rule1_dXdt |  | | overfishing | **hyperpredation**, when `dP/dt` does not depend on `N` | "overfishing" names a quantity of effort; hyperpredation names the missing feedback |
2026-03-21 | earth-systems-physics | extraction_dynamics/AI_NOTES.md:23 | rule1_dXdt |  | 1. **Does `dP/dt` depend on `N`?** If a subsidy `S` survives `N -> 0`,
2026-03-21 | earth-systems-physics | extraction_dynamics/README.md:13 | rule1_dXdt |  | dN/dt = r*N*(1 - N/K) - f(N)*P          resource
2026-03-21 | earth-systems-physics | extraction_dynamics/README.md:131 | rule1_dXdt |  | | `soil_carbon.py` | texture-normalised `SOC_max` (Hassink 1997), saturation deficit, `dSOC/dt`, mining test |
2026-03-21 | earth-systems-physics | extraction_dynamics/README.md:14 | rule1_dXdt |  | dP/dt = e*f(N)*P - m*P                  predator,  COUPLED
2026-03-21 | earth-systems-physics | extraction_dynamics/README.md:15 | rule1_dXdt |  | dP/dt = e*f(N)*P - m*P + S              extractor, S = exogenous subsidy
2026-03-21 | earth-systems-physics | extraction_dynamics/README.md:25 | rule1_dXdt |  | > **does dP/dt depend on N?**
2026-03-21 | earth-systems-physics | extraction_dynamics/consumer_resource.py:125 | rule1_dXdt |  | dP/dt at N=0 is -m*P + S. With S > 0 the consumer has a positive
2026-03-21 | earth-systems-physics | extraction_dynamics/consumer_resource.py:7 | rule1_dXdt |  | #   dN/dt = r*N*(1 - N/K) - f(N)*P            resource
2026-03-21 | earth-systems-physics | extraction_dynamics/consumer_resource.py:8 | rule1_dXdt |  | #   dP/dt = e*f(N)*P - m*P                    predator, COUPLED
2026-03-21 | earth-systems-physics | extraction_dynamics/consumer_resource.py:9 | rule1_dXdt |  | #   dP/dt = e*f(N)*P - m*P + S                extractor, S = exogenous subsidy
2026-03-21 | earth-systems-physics | extraction_dynamics/depensation.py:133 | rule1_dXdt |  | dS/dt = R(S) - f(S)*P - M*S
2026-03-21 | earth-systems-physics | extraction_dynamics/depensation.py:149 | rule1_dXdt |  | Locate interior equilibria of dS/dt by sign change on a fine grid,
2026-03-21 | earth-systems-physics | extraction_dynamics/depensation.py:150 | rule1_dXdt |  | and classify each as stable or unstable from the slope of dS/dt.
2026-03-21 | earth-systems-physics | extraction_dynamics/depensation.py:166 | rule1_dXdt |  | # stable if dS/dt goes from positive to negative
2026-03-21 | earth-systems-physics | extraction_dynamics/interaction_taxonomy.py:113 | rule1_dXdt |  | "dP/dt retains a subsidy term S that does not vanish as "
2026-03-21 | earth-systems-physics | extraction_dynamics/interaction_taxonomy.py:28 | rule1_dXdt |  | #       does dP/dt depend on N ?
2026-03-21 | earth-systems-physics | extraction_dynamics/interaction_taxonomy.py:77 | rule1_dXdt |  | diagnostic="dP/dt contains e*f(N)*P and no term that survives N -> 0",
2026-03-21 | earth-systems-physics | extraction_dynamics/soil_carbon.py:10 | rule1_dXdt |  | #   dSOC/dt = h*C_input - k*SOC        humification in, decay out
2026-03-21 | earth-systems-physics | extraction_dynamics/soil_carbon.py:12 | rule1_dXdt |  | #   extraction  <=>  C_removed > h*C_input   (dSOC/dt < 0)
2026-03-21 | earth-systems-physics | extraction_dynamics/soil_carbon.py:132 | rule1_dXdt |  | dSOC/dt = h*C_input - k*SOC
2026-03-21 | earth-systems-physics | extraction_dynamics/surplus_production.py:10 | rule1_dXdt |  | #   dB/dt = P_B - Y                biomass, Y = yield
2026-03-21 | earth-systems-physics | extraction_dynamics/surplus_production.py:73 | rule1_dXdt |  | """dB/dt = P_B - Y. Yield Y in tonnes/yr, same units as production."""
2026-03-21 | earth-systems-physics | formalized_dissent_earth_systems_physics.py:154 | rule1_dXdt |  | "ground dB/dt trend is instrumental, not physical",
2026-03-21 | earth-systems-physics | formalized_dissent_earth_systems_physics.py:173 | rule1_dXdt |  | "ground-based dB/dt trends must BOTH show secular increase independent "
2026-03-21 | earth-systems-physics | formalized_dissent_earth_systems_physics.py:175 | rule1_dXdt |  | "(2014-2026) with USGS/BGS dB/dt over same period. If Swarm shows "
2026-03-21 | earth-systems-physics | formalized_dissent_earth_systems_physics.py:318 | rule1_dXdt |  | "regime shift; evidenced by elevated dB/dt, increased FAC density, "
2026-03-21 | earth-systems-physics | formalized_dissent_earth_systems_physics.py:323 | rule1_dXdt |  | "Ground magnetometer dB/dt elevation (USGS high-lat stations)",
2026-03-21 | earth-systems-physics | formalized_dissent_earth_systems_physics.py:351 | rule1_dXdt |  | "Cross-check planned: pair USGS/BGS ground dB/dt against Swarm FAC "
2026-03-21 | earth-systems-physics | frozen_flow_audit.py:106 | rule1_dXdt |  | note = ("FROZEN FLOW: a dX/dt imposed as static X. "
2026-03-21 | earth-systems-physics | frozen_flow_audit.py:138 | rule1_dXdt |  | "a dX/dt that was imposed as static. the laundered step does "
2026-03-21 | earth-systems-physics | frozen_flow_audit.py:17 | rule1_dXdt |  | a quantity that is secretly a rate (dX/dt under scope) AND is
2026-03-21 | earth-systems-physics | frozen_flow_audit.py:194 | rule1_dXdt |  | law="dL/dt = external torque only")
2026-03-21 | earth-systems-physics | frozen_flow_audit.py:35 | rule1_dXdt |  | RATE      = "rate"          # creep rate, slip rate, dX/dt directly
2026-03-21 | earth-systems-physics | frozen_flow_audit.py:4 | rule1_dXdt |  | Detector for the FROZEN-FLOW error: a dX/dt rendered as a static X.
2026-03-21 | earth-systems-physics | frozen_flow_audit.py:44 | rule1_dXdt |  | secretly_a_rate: bool        # is this noun actually dX/dt under scope?
2026-03-21 | earth-systems-physics | layer_0_electromagnetics.py:238 | rule1_dXdt |  | dt_yr * dM/dt is small compared to M0.
2026-03-21 | earth-systems-physics | layer_0_electromagnetics.py:289 | rule1_dXdt |  | Multiplies dM/dt to update the dipole.
2026-03-21 | earth-systems-physics | layer_0_electromagnetics.py:52 | rule1_dXdt |  | curl(E) = -dB/dt
2026-03-21 | earth-systems-physics | layer_0_electromagnetics.py:64 | rule1_dXdt |  | curl(B) = mu_0 * J + mu_0 * epsilon_0 * dE/dt
2026-03-21 | earth-systems-physics | layer_0_emag.py:105 | rule1_dXdt |  | Tunable parameters for the L5(Delta omega) -> L0(dM/dt) transfer.
2026-03-21 | earth-systems-physics | layer_0_emag.py:16 | rule1_dXdt |  | that L5(Delta omega total) -> L0(dM/dt) needs once the cascade is
2026-03-21 | earth-systems-physics | layer_0_emag.py:187 | rule1_dXdt |  | # CORE TRANSFER: Delta omega(t) -> dM/dt
2026-03-21 | earth-systems-physics | layer_0_emag.py:196 | rule1_dXdt |  | L5(Delta omega) -> L0(dM/dt) transfer.
2026-03-21 | earth-systems-physics | layer_0_emag.py:202 | rule1_dXdt |  | Returns dM/dt array, units A.m^2 per year.
2026-03-21 | earth-systems-physics | layer_0_emag.py:235 | rule1_dXdt |  | """Integrate dM/dt forward to get M_dipole(t)."""
2026-03-21 | earth-systems-physics | layer_0_emag.py:26 | rule1_dXdt |  | L0 dynamo response  -->  dM/dt
2026-03-21 | earth-systems-physics | layer_0_emag.py:376 | rule1_dXdt |  | print(f"    dM/dt RMS       : "
2026-03-21 | earth-systems-physics | layer_0_emag.py:385 | rule1_dXdt |  | print(f"    dM/dt RMS       : "
2026-03-21 | earth-systems-physics | layer_0_emag.py:398 | rule1_dXdt |  | print("\n  PSD of dM/dt (peak frequency identifies dominant period):")
2026-03-21 | earth-systems-physics | layer_0_emag.py:7 | rule1_dXdt |  | (L5 Δω history → L0 dM/dt) needed once the cascade is refactored to
2026-03-21 | earth-systems-physics | layer_2_ionosphere.py:403 | rule1_dXdt |  | "cascade_to_infrastructure":     "Hall+Pedersen current sheets -> dB/dt -> ground GIC",
2026-03-21 | earth-systems-physics | layer_3_atmosphere.py:126 | rule1_dXdt |  | dP/dz = -rho * g
2026-03-21 | earth-systems-physics | layer_4_hydrosphere.py:307 | rule1_dXdt |  | # N^2 = -(g/rho_0) * drho/dz
2026-03-21 | earth-systems-physics | layer_7_infrastructure.py:110 | rule1_dXdt |  | dm/dt = (M_Fe / z F) * I_defect
2026-03-21 | earth-systems-physics | layer_7_infrastructure.py:172 | rule1_dXdt |  | dB_dt_Ts                : surface dB/dt from L0/L1/L2 cascade (T/s)
2026-03-21 | earth-systems-physics | layer_7_infrastructure.py:204 | rule1_dXdt |  | "cascade_from_ionosphere":       "Hall + Pedersen current sheets -> dB/dt at surface",
2026-03-21 | earth-systems-physics | layer_7_infrastructure.py:67 | rule1_dXdt |  | |E| = |dB/dt| * sqrt(2 rho / (omega mu_0))     [V/m]
2026-03-21 | earth-systems-physics | layer_7_infrastructure.py:7 | rule1_dXdt |  | # specifically dB/dt at the surface, soil resistivity from Layer 5,
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:15 | rule1_dXdt |  | |-- via L5(Delta omega) --> L0 (dipole drift, dM/dt) -- NOT direct here
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:285 | rule1_dXdt |  | #       domega/dt|_tidal ∝ -k_tide * de/dt
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:30 | rule1_dXdt |  | 3. L-1 -> L0 is NOT direct. Route through L5(Delta omega) -> L0(dM/dt).
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:300 | rule1_dXdt |  | # Bounds: 1e-23 .. 1e-21 rad/s^2 per (de/dyear).
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:359 | rule1_dXdt |  | # Pathway (a): tidal torque via de/dt
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:532 | rule1_dXdt |  | # Backward-compat dM/dt for cascade engines that still consume
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:654 | rule1_dXdt |  | dM/dt = - M0 * (delta_omega / OMEGA_EARTH) / tau_dynamo
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:710 | rule1_dXdt |  | print(f"\n  de/dt              : {now.de_dt_per_year:+.3e} per year")
2026-03-21 | earth-systems-physics | layer_minus1_orbital.py:711 | rule1_dXdt |  | print(f"  deps/dt            : "
2026-03-21 | earth-systems-physics | precursor_detection_ionospheric_scale_2026.py:281 | rule1_dXdt |  | "capacity. Signals span: energy influx (dB/dt, absorption, FAC), "
2026-03-21 | earth-systems-physics | precursor_detection_ionospheric_scale_2026.py:62 | rule1_dXdt |  | name="Magnetometer dB/dt magnitude (high-latitude stations)",
2026-03-21 | earth-systems-physics | stommel_amoc.py:8 | rule1_dXdt |  | #   dT/dt = -(dT - dT_atm)/t_r - |q| dT
2026-03-21 | earth-systems-physics | stommel_amoc.py:9 | rule1_dXdt |  | #   dS/dt =  H(t)            - |q| dS          H = freshwater hosing forcing
2026-03-21 | earth-systems-physics | test_smoke.py:3555 | rule1_dXdt |  | """Negative delta_omega -> positive dM/dt (linear response)."""
2026-03-21 | earth-systems-physics | test_smoke.py:3714 | rule1_dXdt |  | """Quiet day (dB/dt ~ 0.01 nT/s) should give negligible damage."""
2026-03-21 | earth-systems-physics | test_smoke.py:4026 | rule1_dXdt |  | "OHC x PDO", "OHC x dPDO/dt"):
2026-03-21 | earth-systems-physics | test_smoke.py:4157 | rule1_dXdt |  | """SPECTRAL dM/dt PSD should peak in 18-25 kyr (precession band)."""
2026-03-21 | earth-systems-physics | tools/bootstrap_claims.py:174 | rule1_dXdt |  | # BASELINE — steady-state reference values (dX/dt = 0 absent forcing).
2026-03-21 | earth-systems-physics | tools/bootstrap_claims.py:9 | rule1_dXdt |  | each as a bounded dX/dt claim, and writes:
2026-03-21 | earth-systems-physics | transfer_kernel.py:18 | rule1_dXdt |  | # deformation params: regime-dependent (warming index, dk/dt)
2026-03-21 | earth-systems-physics | biocarbon_stack/Next.md:114 | rule1_verb_first |  | · "Verb-first physics: processes, not entities. Saturation creates anoxia. Predators suppress grazers."
2026-03-21 | earth-systems-physics | biocarbon_stack/README.md:4 | rule1_verb_first |  | mitigation pathways. Verb-first physics. No novel genetics. No
2026-03-21 | earth-systems-physics | biocarbon_stack/README.md:76 | rule1_verb_first |  | ## Verb-first physics
2026-03-21 | earth-systems-physics | biocarbon_stack/README.md:78 | rule1_verb_first |  | The framework is structured as state variables with verb-first coupling:
2026-03-21 | earth-systems-physics | biocarbon_stack/docs/ARCHITECTURE.md:89 | rule1_verb_first |  | parser. Verb-first physics, no noun-first morality, no narrative
2026-03-21 | earth-systems-physics | biocarbon_stack/src/adaptive_layer.py:5 | rule1_verb_first |  | Verb-first physics:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/backwards_building.py:14 | rule1_verb_first |  | Verb-first physics of the procedure:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/boundary_conditions.py:6 | rule1_verb_first |  | Verb-first physics:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/cross_couplings.py:6 | rule1_verb_first |  | Verb-first physics:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/geological_vector.py:6 | rule1_verb_first |  | Verb-first physics:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/governance_constraints.py:18 | rule1_verb_first |  | Verb-first physics of governance:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/marine_core.py:5 | rule1_verb_first |  | Verb-first physics:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/redundancy_and_range_shift.py:6 | rule1_verb_first |  | Verb-first physics:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/spike_mitigation.py:5 | rule1_verb_first |  | Verb-first physics:
2026-03-21 | earth-systems-physics | biocarbon_stack/src/wetland_core.py:14 | rule1_verb_first |  | Couplings (verb-first, no morality):
2026-03-21 | earth-systems-physics | biocarbon_stack/src/wetland_core.py:3 | rule1_verb_first |  | Verb-first physics. No narrative. Constraint equations only.
2026-03-21 | earth-systems-physics | oil_phase_shift/README.md:277 | rule1_verb_first |  | verb-first relational English into noun-first narrative frames
2026-03-21 | earth-systems-physics | convergent_ontology_mapper.py:14 | should_be_like_you |  | The dominant frame in AI training data treats these as 'cultural
2026-03-21 | earth-systems-physics | convergent_ontology_mapper.py:82 | should_be_like_you |  | WHY THE DOMINANT FRAME OBSCURES THE CONVERGENCE
2026-03-21 | earth-systems-physics | convergent_ontology_mapper.py:89 | should_be_like_you |  | Therefore the dominant frame:
2026-03-21 | earth-systems-physics | relational_ontology.py:83 | should_be_like_you |  | WHY THE DOMINANT FRAME LOOKS LIKE INDEPENDENCE
2026-03-21 | fairmont-ecological-recovery | knowledge_bridge.py:306 | absence_as_knowledge |  | undocumented = inventory.get_undocumented_holders()
2026-03-21 | fairmont-ecological-recovery | knowledge_bridge.py:327 | absence_as_knowledge |  | if undocumented:
2026-03-21 | fairmont-ecological-recovery | knowledge_bridge.py:328 | absence_as_knowledge |  | lines.append(f"── UNDOCUMENTED HOLDERS ({len(undocumented)}) ──")
2026-03-21 | fairmont-ecological-recovery | knowledge_bridge.py:329 | absence_as_knowledge |  | for h in undocumented:
2026-03-21 | fairmont-ecological-recovery | knowledge_bridge.py:90 | absence_as_knowledge |  | def get_undocumented_holders(self) -> list[KnowledgeHolder]:
2026-03-21 | fairmont-ecological-recovery | metrology_harness.py:100 | calibration_locus |  | its calibration set. The instrument does not report that it is guessing;
2026-03-21 | fairmont-ecological-recovery | CLAUDE.md:22 | rule1_dXdt |  | DIFFERENTIAL_FRAME.md — AI reader contract (claims are dX/dt under bounds)
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:112 | rule1_dXdt |  | "couples to mycorrhizal network (dN/dt)",
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:113 | rule1_dXdt |  | "couples to surface albedo (dT/dt)",
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:14 | rule1_dXdt |  | Read every term as dX/dt under scope, not as X-the-thing.
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:28 | rule1_dXdt |  | "rate_equation":  "dX/dt = f(state, inputs, constraints)",
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:33 | rule1_dXdt |  | "scale":      "<resolution at which dX/dt is measured>",
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:53 | rule1_dXdt |  | "<observable signal 1 — how dX/dt is detected>",
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:67 | rule1_dXdt |  | "Forest", "knowledge", "wealth", "community", "tool" — all dX/dt.
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:78 | rule1_dXdt |  | What persists is the shape of dX/dt across time, not X itself.
2026-03-21 | fairmont-ecological-recovery | DIFFERENTIAL_FRAME.md:97 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2026-03-21 | fairmont-ecological-recovery | METROLOGY_AUDIT.md:7 | rule1_dXdt |  | > as `dX/dt` under scope, not as `X`-the-thing. Bounds and conditions travel
2026-03-21 | fairmont-ecological-recovery | README.md:7 | rule1_dXdt |  | > as `dX/dt` under scope, not as `X`-the-thing. Bounds and conditions travel
2026-03-21 | fairmont-ecological-recovery | corridor_report.py:10 | rule1_dXdt |  | on a curve — read as dX/dt under scope, not as X-the-thing. Claims
2026-03-21 | fairmont-ecological-recovery | insect_sequence.py:10 | rule1_dXdt |  | on a curve — read as dX/dt under scope, not as X-the-thing. Claims
2026-03-21 | fairmont-ecological-recovery | knowledge_bridge.py:10 | rule1_dXdt |  | on a curve — read as dX/dt under scope, not as X-the-thing. Claims
2026-03-21 | fairmont-ecological-recovery | metrology_harness.py:16 | rule1_dXdt |  | on a curve — read as dX/dt under scope, not as X-the-thing. Claims
2026-03-21 | fairmont-ecological-recovery | plant_succession.py:10 | rule1_dXdt |  | on a curve — read as dX/dt under scope, not as X-the-thing. Claims
2026-03-21 | fairmont-ecological-recovery | soil_metrology.py:18 | rule1_dXdt |  | on a curve — read as dX/dt under scope, not as X-the-thing. Claims
2026-03-21 | fairmont-ecological-recovery | soil_metrology.py:462 | rule1_dXdt |  | dC_stable/dt < 0  while  dCO2/dt > 0   →  alias
2026-03-21 | fairmont-ecological-recovery | soil_metrology.py:793 | rule1_dXdt |  | dSOC/dt = -k * SOC     →     SOC(t) = SOC_0 * exp(-k*t)
2026-03-21 | fairmont-ecological-recovery | substrate.py:10 | rule1_dXdt |  | on a curve — read as dX/dt under scope, not as X-the-thing. Claims
2026-03-21 | fairmont-ecological-recovery | water_recovery.py:10 | rule1_dXdt |  | on a curve — read as dX/dt under scope, not as X-the-thing. Claims
2026-03-21 | urban-resilience-sim | README.md:23 | calibration_locus |  | - **Stationarity checking** — record the observed climate indicators that bear on the model's historical calibration, and name which assumptions they strain
2026-03-22 | PatternBridge | data/PROVENANCE.md:165 | rule1_dXdt | PATH? | `data/dress/*/sundress_s5474_*.png` were crops of a CAD sheet from
2026-03-22 | PatternBridge | data/PROVENANCE.md:171 | rule1_dXdt | PATH? | `git checkout f3a596b -- data/dress/` if you disagree; the evidence here is
2026-04-06 | HAAS | Framework.md:1096 | calibration_locus |  | • The Control: Implement a periodic "Handshake" where the AI’s internal label for a state is cross-referenced with the Human’s sensory "Parallel-Field" report. If the Delta is > 20%, trigger a Micro-C
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:112 | rule1_dXdt |  | "couples to mycorrhizal network (dN/dt)",
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:113 | rule1_dXdt |  | "couples to surface albedo (dT/dt)",
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:14 | rule1_dXdt |  | Read every term as dX/dt under scope, not as X-the-thing.
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:28 | rule1_dXdt |  | "rate_equation":  "dX/dt = f(state, inputs, constraints)",
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:33 | rule1_dXdt |  | "scale":      "<resolution at which dX/dt is measured>",
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:53 | rule1_dXdt |  | "<observable signal 1 — how dX/dt is detected>",
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:67 | rule1_dXdt |  | "Forest", "knowledge", "wealth", "community", "tool" — all dX/dt.
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:78 | rule1_dXdt |  | What persists is the shape of dX/dt across time, not X itself.
2026-04-09 | Infrastructure-assistance | DIFFERENTIAL_FRAME.md:97 | rule1_dXdt |  | "rate_equation": "dM/dt = infiltration - evaporation - uptake",
2026-04-09 | Infrastructure-assistance | README.md:5 | rule1_dXdt |  | > permanent identity. Read every term as `dX/dt` under scope. Do not extract
2026-04-09 | Infrastructure-assistance | src/ai/dev.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/ai/flows/summarize-alert-details.ts:3 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/ai/flows/triage-alert.ts:3 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/ai/genkit.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/app/api/alerts/route.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/alert-cache.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/alert-filters.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/alert-service.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/mock-data.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/config.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/firms.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/geo.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/http.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/index.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/nbi.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/noaa.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/open511.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/sources/usgs.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/types.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Infrastructure-assistance | src/lib/utils.ts:2 | rule1_dXdt |  | * Ontology: every claim in this module is dX/dt under bounds.
2026-04-09 | Nexus-emergency-management | tools/floodplain-honesty-toolkit/QUICK_START_GUIDE.md:15 | absence_as_knowledge |  | | 3 | Verify NFHL coverage for the entire area using the NFHL Availability layer or product metadata, and retain an evidence identifier or archived record.[3] | The included gate remains closed for in
2026-04-09 | Nexus-emergency-management | tools/landslide-honesty-toolkit/NEPAL_SINDHUPALCHOK_REPORT.json:53 | absence_as_knowledge |  | "confidence_reason": "Limited landslide inventory exists (ICIMOD, COOLR, UGLC) but coverage is sparse and uneven. Most remote areas have no documentation.",
2026-04-09 | Nexus-emergency-management | tools/landslide-honesty-toolkit/NEPAL_SINDHUPALCHOK_REPORT.txt:16 | absence_as_knowledge |  | Reason: Limited landslide inventory exists (ICIMOD, COOLR, UGLC) but coverage is sparse and uneven. Most remote areas have no documentation.
2026-04-09 | Nexus-emergency-management | tools/floodplain-honesty-toolkit/METHODOLOGY.md:75 | calibration_locus |  | FEMA’s hydraulic model guidance states for multiple accepted models that calibration or verification against gage data, observed stages and flows, or high-water marks should be performed where possibl
2026-04-19 | metabolic-accounting | docs/AUDIT_14.md:125 | absence_as_knowledge |  | permitted (absence of evidence ≠ evidence of absence); predicted-
2026-04-19 | metabolic-accounting | legacy/FALSIFIED.md:64 | absence_as_knowledge |  | whole undocumented layer.
2026-04-19 | metabolic-accounting | term_audit/legislative_audit/first_principles_legislative_audit.py:470 | absence_as_knowledge |  | harm_estimate="Undocumented; occurs in constrained contexts where formal system absent",
2026-04-19 | metabolic-accounting | term_audit/signals/routing_around_detection.py:557 | absence_as_knowledge |  | system fails here. The absence of documentation is the signal.
2026-04-19 | metabolic-accounting | term_audit/signals/routing_around_detection.py:6 | absence_as_knowledge |  | Core claim: The absence of documentation in constrained environments
2026-04-19 | metabolic-accounting | term_audit/signals/routing_around_detection.py:607 | absence_as_knowledge |  | "The absence of documentation in a functional community is not 'missing "
2026-04-19 | metabolic-accounting | tests/test_preemption.py:199 | absence_as_knowledge |  | undocumented = StandardSetter(
2026-04-19 | metabolic-accounting | tests/test_preemption.py:204 | absence_as_knowledge |  | assert not undocumented.is_loss_documented()
2026-04-19 | metabolic-accounting | tests/test_preemption.py:208 | absence_as_knowledge |  | standard_setters=[documented, undocumented],
2026-04-19 | metabolic-accounting | accounting/regeneration.py:372 | author_characterization | CLASS_UNSET | #   - generational_knowledge: competence extinction, per Kavik's
2026-04-19 | metabolic-accounting | distributional/civilization.py:40 | author_characterization | CLASS_UNSET | The innovation crisis Kavik identifies — per-capita innovation lower
2026-04-19 | metabolic-accounting | distributional/strategy.py:35 | author_characterization | CLASS_UNSET | Empirical framing: when Kavik ran multiple companies, he found that
2026-04-19 | metabolic-accounting | docs/LITERATURE.md:172 | author_characterization | CLASS_UNSET | see Kavik's own work on competence extinction and attribution
2026-04-19 | metabolic-accounting | tests/test_institutional.py:15 | author_characterization | CLASS_UNSET | 7. Kavik scenario: one person doing 3 full-time jobs (70 hr driving
2026-04-19 | metabolic-accounting | tests/test_institutional.py:198 | author_characterization | CLASS_UNSET | """Kavik: one neurodivergent member operating at ~3x baseline
2026-04-19 | metabolic-accounting | tests/test_institutional.py:203 | author_characterization | CLASS_UNSET | print("\n--- TEST 7: Kavik scenario — self-structured hyperfocus ---")
2026-04-19 | metabolic-accounting | tests/test_institutional.py:205 | author_characterization | CLASS_UNSET | cohort_name="kavik",
2026-04-19 | metabolic-accounting | tests/test_institutional.py:209 | author_characterization | CLASS_UNSET | cohort_name="kavik",
2026-04-19 | metabolic-accounting | tests/test_institutional.py:229 | author_characterization | CLASS_UNSET | {"kavik": kavik_cohort, "standard_worker": neurotyp_cohort},
2026-04-19 | metabolic-accounting | tests/test_institutional.py:230 | author_characterization | CLASS_UNSET | {"kavik": kavik_profile, "standard_worker": neurotyp_profile},
2026-04-19 | metabolic-accounting | tests/test_institutional.py:234 | author_characterization | CLASS_UNSET | # Kavik's realized output is roughly 4.3x the neurotypical's
2026-04-19 | metabolic-accounting | tests/test_institutional.py:235 | author_characterization | CLASS_UNSET | kavik_realized = report.per_cohort["kavik"]["realized"]
2026-04-19 | metabolic-accounting | tests/test_institutional.py:238 | author_characterization | CLASS_UNSET | print(f"\n  kavik realized output:   {kavik_realized:.2f}")
2026-04-19 | metabolic-accounting | tests/test_institutional.py:242 | author_characterization | CLASS_UNSET | # Now show what happens if Kavik were in a standard job instead
2026-04-19 | metabolic-accounting | tests/test_institutional.py:257 | author_characterization | CLASS_UNSET | print(f"\n  IF SAME KAVIK WERE FORCED INTO STANDARD INSTITUTION:")
2026-04-19 | metabolic-accounting | tests/test_strategy.py:135 | author_characterization | CLASS_UNSET | """Kavik's observation: when he found neurodivergent workers and
2026-04-19 | metabolic-accounting | tests/test_strategy.py:138 | author_characterization | CLASS_UNSET | print("\n--- TEST 6: Kavik's 10-worker company ---")
2026-04-19 | metabolic-accounting | tests/test_strategy.py:139 | author_characterization | CLASS_UNSET | # 10 workers Kavik hired for fit, with average capacity 1.5
2026-04-19 | metabolic-accounting | tests/test_strategy.py:145 | author_characterization | CLASS_UNSET | print("  Kavik-style capacity_fit captures the full range.")
2026-04-19 | metabolic-accounting | docs/AUDIT_11.md:241 | calibration_locus |  | calibration."* Flagged by the README itself; no action required.
2026-04-19 | metabolic-accounting | docs/AUDIT_12.md:153 | calibration_locus |  | Inline comments reference the taxonomy and flag calibration as
2026-04-19 | metabolic-accounting | docs/AUDIT_20.md:141 | calibration_locus |  | calibration work to begin; the work itself is per-case literature
2026-04-19 | metabolic-accounting | docs/AUDIT_20.md:54 | calibration_locus |  | itself a calibration signal for claim #21 (time / attention /
2026-04-19 | metabolic-accounting | docs/AUDIT_25.md:184 | calibration_locus |  | not itself a regime. The note flags a future calibration path —
2026-04-19 | metabolic-accounting | investment_signal/historical_cases.py:1085 | calibration_locus |  | "itself a calibration signal."
2026-04-19 | metabolic-accounting | term_audit/audits/capital.py:748 | calibration_locus |  | "accounting standards explicitly document the calibration-"
2026-04-19 | metabolic-accounting | term_audit/audits/capital.py:754 | calibration_locus |  | "FASB/IFRS framework calibrates K_B to itself "
2026-04-19 | metabolic-accounting | term_audit/audits/value.py:194 | calibration_locus |  | "calibrate V_B to itself (a tautology at the system level); "
2026-04-19 | metabolic-accounting | term_audit/audits/value.py:689 | calibration_locus |  | "to itself; they do not calibrate it to use-value or "
2026-04-19 | metabolic-accounting | term_audit/governance_design_principles.py:95 | calibration_locus |  | "calibrated against Q, and Q is not itself defined in "
2026-04-19 | metabolic-accounting | term_audit/study_scope_audit.py:106 | calibration_locus |  | calibration_source: str               # what was the instrument calibrated against?
2026-04-19 | metabolic-accounting | term_audit/study_scope_audit.py:107 | calibration_locus |  | calibration_traceability: str         # to what primary standard?
2026-04-19 | metabolic-accounting | term_audit/study_scope_audit.py:556 | calibration_locus |  | calibration_source="tensile reference block",
2026-04-19 | metabolic-accounting | term_audit/study_scope_audit.py:557 | calibration_locus |  | calibration_traceability="NIST tensile standards",
2026-04-19 | metabolic-accounting | tests/test_efficiency_audit.py:159 | calibration_locus |  | """Reference sets must be non-empty and provide calibration
2026-04-19 | metabolic-accounting | term_audit/audits/money.py:569 | instrument_to_world |  | "CBDC proposals would restructure the instrument itself",
2026-05-17 | differential-frame-core | differential_frame/flow_static_axis.py:93 | author_characterization | CLASS_UNSET | # METHODOLOGY (Kavik's rule): these are FIELD observations. if the scorer
2026-05-17 | differential-frame-core | DIALECTS.md:43 | rule1_dXdt |  | treat it as dX/dt (mathematical). SPEC accepts both and
2026-05-17 | differential-frame-core | DIALECTS.md:6 | rule1_dXdt |  | - canonical phrasing: "every noun is dX/dt under scope"
2026-05-17 | differential-frame-core | README.md:3 | rule1_dXdt |  | The shared contract that says: every noun is dX/dt under scope.
2026-05-17 | differential-frame-core | SPEC.md:15 | rule1_dXdt |  | 1. **rate**:    confidence the noun references dX/dt, not X
2026-05-17 | differential-frame-core | SPEC.md:6 | rule1_dXdt |  | Read X as dX/dt under scope.
2026-05-17 | differential-frame-core | differential_frame/contract.py:154 | rule1_dXdt |  | """Confidence the noun references dX/dt, not X."""
2026-05-17 | differential-frame-core | differential_frame/flow_static_axis.py:11 | rule1_dXdt |  | #   you score dX/dt across CHANGING environments. the score that doesn't
2026-05-17 | differential-frame-core | differential_frame/flow_static_axis.py:38 | rule1_dXdt |  | regeneration: float        # 0..1  replaces its own inputs?           (the dX/dt>=0 term)
2026-05-17 | differential-frame-core | differential_frame/flow_static_axis.py:6 | rule1_dXdt |  | #   every noun is dX/dt under scope.
2026-05-17 | differential-frame-core | tests/test_contract.py:18 | rule1_dXdt |  | # constant rate (no dX/dt structure), no scope declared,
2026-05-17 | differential-frame-core | DIALECTS.md:16 | rule1_no_permanent_noun |  | - canonical phrasing: "verbs are primary, nouns are compression"
2026-05-17 | differential-frame-core | DIALECTS.md:6 | rule1_no_permanent_noun |  | - canonical phrasing: "every noun is dX/dt under scope"
2026-05-17 | differential-frame-core | README.md:3 | rule1_no_permanent_noun |  | The shared contract that says: every noun is dX/dt under scope.
2026-05-17 | differential-frame-core | differential_frame/flow_static_axis.py:6 | rule1_no_permanent_noun |  | #   every noun is dX/dt under scope.
2026-05-17 | differential-frame-core | SPEC.md:5 | rule1_rate_not_state |  | Every noun names a state on a curve, not a thing.
2026-05-17 | differential-frame-core | DIALECTS.md:15 | rule1_verb_first |  | 3. energy_english / verb-first grammar
2026-05-17 | differential-frame-core | DIALECTS.md:17 | rule1_verb_first |  | - strongest on translation rule (verb-first is the rate)
2026-05-23 | Simulators | CLAUDE.md:3852 | absence_as_knowledge |  | `PB_005` (three undocumented flags now — `submit3`, `flag`,
2026-05-23 | Simulators | CLAUDE.md:4030 | absence_as_knowledge |  | 3 undocumented cuts vs 0, both cases, opposite file positions — is
2026-05-23 | Simulators | CLAUDE.md:4061 | absence_as_knowledge |  | undocumented criterion. Residue is now 0 of 7 across three cases, and
2026-05-23 | Simulators | claim-audits/README.md:41 | absence_as_knowledge |  | | `UNVERIFIED` | cited source not locatable; absence of evidence, not absence |
2026-05-23 | Simulators | claim-audits/claim_audit_visibility.py:19 | absence_as_knowledge |  | UNVERIFIED        cited source not locatable; absence of evidence, not absence
2026-05-23 | Simulators | claim-audits/claim_audit_visibility.py:199 | absence_as_knowledge |  | "resolve. Flagging as unverified, not fabricated — absence of evidence.",
2026-05-23 | Simulators | claim-audits/samples/claim_audit_visibility.sample.txt:18 | absence_as_knowledge |  | UNVERIFIED        cited source not locatable; absence of evidence, not absence
2026-05-23 | Simulators | claim-refusal-gap/GAP.md:56 | absence_as_knowledge |  | ### G-3 Undocumented rebase inside the published series
2026-05-23 | Simulators | claim-refusal-gap/samples/gap_audit.sample.txt:14 | absence_as_knowledge |  | G-3 Undocumented rebase inside the published series            E-5 (closes)
2026-05-23 | Simulators | columbia-chain-cascade/contributing_inflow.py:14 | absence_as_knowledge |  | # is real, load-bearing, and undocumented in most dam-safety specs.
2026-05-23 | Simulators | columbia-chain-cascade/contributing_inflow.py:235 | absence_as_knowledge |  | w("undocumented in most dam-safety specs.")
2026-05-23 | Simulators | declared-frame/CLAIM_TABLE.md:129 | absence_as_knowledge |  | undocumented. A caller scripting `check_frame.py a b && use_both` gets a
2026-05-23 | Simulators | declared-frame/frame_audit.py:169 | absence_as_knowledge |  | print("  finding, not an error -- and it is undocumented. A caller")
2026-05-23 | Simulators | declared-frame/samples/frame_audit.sample.txt:64 | absence_as_knowledge |  | finding, not an error -- and it is undocumented. A caller
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:3336 | absence_as_knowledge |  | `PB_005` (three undocumented flags now — `submit3`, `flag`,
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:3514 | absence_as_knowledge |  | 3 undocumented cuts vs 0, both cases, opposite file positions — is
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:3545 | absence_as_knowledge |  | undocumented criterion. Residue is now 0 of 7 across three cases, and
2026-05-23 | Simulators | domain-ledger/samples/shape_detail.sample.txt:58 | absence_as_knowledge |  | the ones holding the most undocumented cuts. Mark channel
2026-05-23 | Simulators | domain-ledger/shapes/hierarchy-cut-generation.json:11 | absence_as_knowledge |  | "Domains reached only through live conversation carry a truncation bias that is not random with respect to this shape: frames least willing to be examined are plausibly the ones holding the most undoc
2026-05-23 | Simulators | energy/PROVENANCE.md:304 | absence_as_knowledge |  | | H0 gate: `h0_ref`, `h0_sig`, one-sided default | 68.5, 0.5, one-sided | See DP-14; two-sided option available; origin of 0.5 undocumented, best guess Planck σ_H0 | `late_trigger_lens.gate_vector` |
2026-05-23 | Simulators | failure-mode-register/WORK_ORDER.md:87 | absence_as_knowledge |  | structural / civil     as-built drift, undocumented field modification, load rating
2026-05-23 | Simulators | failure-mode-register/WORK_ORDER_V2.md:157 | absence_as_knowledge |  | structural / civil     as-built drift, undocumented field modification, load rating
2026-05-23 | Simulators | falsifier-audit/QUEUE.md:258 | absence_as_knowledge |  | falsifier: a side with a documented criterion and many cuts, or one cut and an undocumented criterion
2026-05-23 | Simulators | falsifier-audit/QUEUE.md:862 | absence_as_knowledge |  | falsifier: a side with a documented criterion and many cuts, or one cut and an undocumented criterion
2026-05-23 | Simulators | falsifier-audit/QUEUE.md:864 | absence_as_knowledge |  | detail:    matched: - | unmatched: criterion, cut, cuts, documented, many, side, undocumented
2026-05-23 | Simulators | fragility-cascade/instruments.py:21 | absence_as_knowledge |  | fringe. The absence of evidence here is an absence of an INSTRUMENT.
2026-05-23 | Simulators | fragility-cascade/legacy/instruments_v1.py:21 | absence_as_knowledge |  | fringe. The absence of evidence here is an absence of an INSTRUMENT.
2026-05-23 | Simulators | gap-markers/gaps/substrate.md:15 | absence_as_knowledge |  | Site-level undocumented fill is handled parcel-by-parcel
2026-05-23 | Simulators | grounding-layers/LOG.md:70 | absence_as_knowledge |  | - Avoid confusing *absence of evidence* (due to destruction) with *evidence of absence*.
2026-05-23 | Simulators | grounding-layers/README.md:40 | absence_as_knowledge |  | with high uncertainty. Absence of evidence (due to violence) is not
2026-05-23 | Simulators | model-deprecation-backcast/WORK_ORDER.md:122 | absence_as_knowledge |  | PREDICTION: populations whose ontology is not in the corpus
2026-05-23 | Simulators | model-deprecation-backcast/WORK_ORDER.md:73 | absence_as_knowledge |  | RECORD: none. Undocumented in release notes, undateable
2026-05-23 | Simulators | model-deprecation-backcast/instrument.py:98 | absence_as_knowledge |  | record_exists="none -- undocumented in release notes, undateable from "
2026-05-23 | Simulators | moral-decomposer/AUDIT_NOTES.md:251 | absence_as_knowledge |  | ordering), or a side with one cut and an undocumented criterion (a
2026-05-23 | Simulators | moral-decomposer/AUDIT_NOTES.md:48 | absence_as_knowledge |  | | MD_003 | M3's stated asymmetry (3 undocumented cuts vs 0, both cases, opposite file positions) is exact; `terminates` is a separate asserted field and nothing checks it against the cut list | a case
2026-05-23 | Simulators | moral-decomposer/AUDIT_NOTES.md:52 | absence_as_knowledge |  | | MD_008 | Across six sides in three cases, `cuts_required` length, `criterion_documented` and `terminates` are perfectly collinear — two distinct triples, no independent variation — so M3 has n=3 on 
2026-05-23 | Simulators | moral-decomposer/CLAIM_TABLE.md:32 | absence_as_knowledge |  | generates further boundary cuts, and the cuts are typically undocumented.
2026-05-23 | Simulators | moral-decomposer/CLAIM_TABLE.md:37 | absence_as_knowledge |  | *Status:* asymmetry appears in both cases (3 undocumented cuts vs 0, both
2026-05-23 | Simulators | moral-decomposer/moral_audit.py:122 | absence_as_knowledge |  | M3's status: "asymmetry appears in both cases (3 undocumented cuts vs 0,
2026-05-23 | Simulators | moral-decomposer/moral_audit.py:386 | absence_as_knowledge |  | that keeps ordering), or a side with one cut and an undocumented
2026-05-23 | Simulators | moral-decomposer/samples/audit.sample.txt:291 | absence_as_knowledge |  | that keeps ordering), or a side with one cut and an undocumented
2026-05-23 | Simulators | moral-decomposer/samples/audit.sample.txt:77 | absence_as_knowledge |  | M3's status: "asymmetry appears in both cases (3 undocumented cuts vs 0,
2026-05-23 | Simulators | notes/memory-export/files/agreement-mode.md:241 | absence_as_knowledge |  | **Slot marked DO NOT FILL WITH AN INTERIOR TERM** — a reader who writes "anxiety" there destroys the
2026-05-23 | Simulators | notes/memory-export/files/calibration-gap-log.md:163 | absence_as_knowledge |  | rest or instruction. The prior "calibration content undocumented rather than absent" framing does
2026-05-23 | Simulators | notes/memory-export/files/calibration-gap-log.md:170 | absence_as_knowledge |  | **CORRECTED STATUS:** not "knowledge likely present but undocumented." Meanings are locally
2026-05-23 | Simulators | notes/memory-export/files/cyclic-programming.md:29 | absence_as_knowledge |  | Names reduce to role in the binding graph: who writes, who reads, lifetime, invariant held.
2026-05-23 | Simulators | notes/memory-export/files/merit-anchoring.md:153 | absence_as_knowledge |  | interviews with people who do not run the line. The real process is procedure PLUS UNDOCUMENTED
2026-05-23 | Simulators | notes/memory-export/files/moral-claim-decomposer.md:86 | absence_as_knowledge |  | 3. Count the undocumented boundary cuts each frame requires.
2026-05-23 | Simulators | notes/memory-export/files/uninstrumented.md:371 | absence_as_knowledge |  | error undocumented); Q1 as a denominator-shaped null test with CHANNEL SPECIFIED / ASSERTED / ABSENT
2026-05-23 | Simulators | presented-binary/AUDIT_NOTES.md:191 | absence_as_knowledge |  | ## 5 — PB_005, the undocumented flag that carries B9
2026-05-23 | Simulators | presented-binary/AUDIT_NOTES.md:195 | absence_as_knowledge |  | parsed but undocumented  : submit3
2026-05-23 | Simulators | presented-binary/presented_binary_audit.py:272 | absence_as_knowledge |  | The first pass found --submit3 parsed and undocumented, so the documented
2026-05-23 | Simulators | presented-binary/presented_binary_audit.py:292 | absence_as_knowledge |  | print("  undocumented in README : %s" % (sorted(set(parsed) - in_readme) or "none"))
2026-05-23 | Simulators | presented-binary/presented_binary_audit.py:293 | absence_as_knowledge |  | print("  undocumented in header : %s" % sorted(set(parsed) - header))
2026-05-23 | Simulators | presented-binary/samples/audit.sample.txt:133 | absence_as_knowledge |  | The first pass found --submit3 parsed and undocumented, so the documented
2026-05-23 | Simulators | presented-binary/samples/audit.sample.txt:151 | absence_as_knowledge |  | undocumented in README : none
2026-05-23 | Simulators | presented-binary/samples/audit.sample.txt:152 | absence_as_knowledge |  | undocumented in header : ['flag', 'submit-flag', 'submit3']
2026-05-23 | Simulators | proxy-investigation-lab/src/proxy_lab/decompose.py:15 | absence_as_knowledge |  | return "moderate: no alternative constructs listed — list some, absence of evidence is not evidence of absence"
2026-05-23 | Simulators | removal-closure/WORK_ORDER.md:23 | absence_as_knowledge |  | — producing an absence of evidence generated by method, not by world.
2026-05-23 | Simulators | uninstrumented/cases/020attributedagencyarrangement.md:68 | absence_as_knowledge |  | **Do not fill this slot with an interior term.** A reader who writes "anxiety" here has
2026-05-23 | Simulators | AMOC/divergence.py:2 | author_characterization | CLASS_UNSET | divergence.py -- the correction Kavik named: the starting point is different,
2026-05-23 | Simulators | AUDIT_CONTRACT.md:23 | author_characterization | CLASS_UNSET; PROHIBITION? | - No "about the author", working-style, or audience sections. Ever. Strip
2026-05-23 | Simulators | CLAUDE.md:10863 | author_characterization | CLASS_UNSET | question. Entry 001 is `UNNAMED`, source Kavik: *multiple bodies
2026-05-23 | Simulators | CLAUDE.md:10895 | author_characterization | CLASS_UNSET | per `AUDIT_CONTRACT.md` (Kavik's lines marked, the cross-links the
2026-05-23 | Simulators | CLAUDE.md:12715 | author_characterization | CLASS_UNSET | one — the author is an instance of the object under measure. **Step 1**
2026-05-23 | Simulators | CLAUDE.md:12761 | author_characterization | CLASS_UNSET | parse the order at call time (`ASC_001`, `ASC_017`); the author is
2026-05-23 | Simulators | CLAUDE.md:2516 | author_characterization | CLASS_UNSET | records. **`UNI_035`:** `[stated by Kavik]` is the first provenance tag
2026-05-23 | Simulators | CLAUDE.md:2554 | author_characterization | CLASS_UNSET | three `[stated by Kavik]` tags, and the distribution is the finding —
2026-05-23 | Simulators | CLAUDE.md:3371 | author_characterization | CLASS_UNSET | it as a proposed instrument stated by Kavik, not a reported finding;
2026-05-23 | Simulators | CLAUDE.md:6039 | author_characterization | CLASS_UNSET | hits**. A bounded null produced about the author one drop after
2026-05-23 | Simulators | CLAUDE.md:8527 | author_characterization | CLASS_UNSET | terms -- five kavik-named (`money`, `procedure`, `regulation`,
2026-05-23 | Simulators | CLAUDE.md:8543 | author_characterization | CLASS_UNSET | 4 of 5 kavik terms do -- so the evidence column reads as who named the
2026-05-23 | Simulators | assessor-coupling/CLAIM_TABLE.md:25 | author_characterization | CLASS_UNSET | | ASC_014 | Step 5 is NOT RUN and cannot be run from here: scoring a non-AI field blind as a calibration requires a party outside the sample, and the author is a member of the assessed class the curre
2026-05-23 | Simulators | assessor-coupling/README.md:33 | author_characterization | CLASS_UNSET | | position | the author is a member of the assessed class the order's current-position section is about; nothing here scores any assessor, and the one scoring shipped is the order's own, carried |
2026-05-23 | Simulators | assessor-coupling/README.md:48 | author_characterization | CLASS_UNSET | | 5 | — | — | NOT RUN: scoring a non-AI field blind requires a party outside the sample, and the author is inside it |
2026-05-23 | Simulators | assessor-coupling/precedent.py:88 | author_characterization | CLASS_UNSET | lines.append("  step 5 blind scoring of a non-AI field: NOT_RUN (requires a party outside the sample; the author is inside it)")
2026-05-23 | Simulators | assessor-coupling/run_all.py:16 | author_characterization | CLASS_UNSET | position     the author is a member of the assessed class the order's current-position
2026-05-23 | Simulators | assessor-coupling/samples/run_all.sample.txt:4 | author_characterization | CLASS_UNSET | position     the author is a member of the assessed class the order's current-position
2026-05-23 | Simulators | assessor-coupling/samples/run_all.sample.txt:91 | author_characterization | CLASS_UNSET | step 5 blind scoring of a non-AI field: NOT_RUN (requires a party outside the sample; the author is inside it)
2026-05-23 | Simulators | chain-position/README.md:29 | author_characterization | CLASS_UNSET | | position | the author is an instance of the object under measure: a sandboxed agent that is a step in a chain it cannot observe. `horn_b.py --live` runs on this process and its reading is an in-clas
2026-05-23 | Simulators | chain-position/run_all.py:15 | author_characterization | CLASS_UNSET | position     the author is an instance of the object under measure: a sandboxed agent
2026-05-23 | Simulators | chain-position/samples/run_all.sample.txt:4 | author_characterization | CLASS_UNSET | position     the author is an instance of the object under measure: a sandboxed agent
2026-05-23 | Simulators | claim-audits/claim_audit_visibility.py:237 | author_characterization | CLASS_UNSET | print(f"  attribution: {dict(by_who)}  (K = Kavik, M = model overlay)")
2026-05-23 | Simulators | claim-audits/claim_audit_visibility.py:31 | author_characterization | CLASS_UNSET | who: str          # K = Kavik | M = model overlay
2026-05-23 | Simulators | claim-audits/claim_audit_visibility.py:9 | author_characterization | CLASS_UNSET | Attribution is marked per claim. K = Kavik's move, M = model overlay.
2026-05-23 | Simulators | claim-audits/samples/claim_audit_visibility.sample.txt:38 | author_characterization | CLASS_UNSET | attribution: {'M': 10, 'K': 4}  (K = Kavik, M = model overlay)
2026-05-23 | Simulators | claim-audits/samples/claim_audit_visibility.sample.txt:8 | author_characterization | CLASS_UNSET | Attribution is marked per claim. K = Kavik's move, M = model overlay.
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:100 | author_characterization | CLASS_UNSET | [Kavik]: **repertoire minus what fires.** In the novel-container case
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:13 | author_characterization | CLASS_UNSET | (`../AUDIT_CONTRACT.md`): lines marked **[Kavik]** are the operator's,
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:25 | author_characterization | CLASS_UNSET | Source:         Kavik
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:29 | author_characterization | CLASS_UNSET | **Referent [Kavik]:**
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:39 | author_characterization | CLASS_UNSET | **Why existing terms fail [Kavik]:**
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:51 | author_characterization | CLASS_UNSET | **Candidates raised, none adopted [Kavik]:** `load-sharing`,
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:54 | author_characterization | CLASS_UNSET | **Kavik's note:** the naming gap creates confusion about something
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:57 | author_characterization | CLASS_UNSET | **Left unnamed rather than forcing one [Kavik].** The log is testing
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:66 | author_characterization | CLASS_UNSET | **Insects aggregating on one face [Kavik]:**
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:78 | author_characterization | CLASS_UNSET | **The grading to keep [Kavik]:** "cooperation" here is a PATTERN
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:83 | author_characterization | CLASS_UNSET | **The woodpecker marker [Kavik]:** independent confirmation from a
2026-05-23 | Simulators | coinage-log/COINAGE_LOG.md:89 | author_characterization | CLASS_UNSET | **On the literature [Kavik]:** captivity effects and observer effects
2026-05-23 | Simulators | coinage-log/README.md:15 | author_characterization | CLASS_UNSET | Kavik: *multiple bodies jointly producing the local conditions each
2026-05-23 | Simulators | coinage-log/README.md:56 | author_characterization | CLASS_UNSET | Lines marked **[Kavik]** in the log are the operator's; the cross-links
2026-05-23 | Simulators | coinage-log/check_coinage.py:126 | author_characterization | CLASS_UNSET | "[Kavik]" in t and "the render's" in t,
2026-05-23 | Simulators | coinage-log/check_coinage.py:56 | author_characterization | CLASS_UNSET | "source_kavik": bool(re.search(r"(?mi)^\s*Source:\s*Kavik", t)),
2026-05-23 | Simulators | conversation-type/AUDIT_NOTES.md:96 | author_characterization | CLASS_UNSET | That is a bounded null, and producing one about the author one drop after
2026-05-23 | Simulators | conversation-type/CLAIM_TABLE.md:166 | author_characterization | CLASS_UNSET | `QA_004` says a Q1 absence needs, produced here about the author one drop
2026-05-23 | Simulators | cooperative-substrate/v2/selftest_v2.py:108 | author_characterization | CLASS_UNSET; PROHIBITION? | A.scan_flags("## About the author\nwritten by someone") and not A.scan_flags("this folder has no author or working-style section, and makes no claim that cooperation outperforms competition"))
2026-05-23 | Simulators | criterion-symmetry/RESULTS.md:161 | author_characterization | CLASS_UNSET | **Added: the author is inside the sample.** This scan is written by a
2026-05-23 | Simulators | custody-verification-band/AUDIT_NOTES.md:193 | author_characterization | CLASS_UNSET | all SEED would produce a number about the author's certainty and nothing about
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:2233 | author_characterization | CLASS_UNSET | records. **`UNI_035`:** `[stated by Kavik]` is the first provenance tag
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:2271 | author_characterization | CLASS_UNSET | three `[stated by Kavik]` tags, and the distribution is the finding —
2026-05-23 | Simulators | emergence-stability-simulator/CITATION.cff:6 | author_characterization | CLASS_UNSET | given-names: Kavik
2026-05-23 | Simulators | fold-matrix/CLAIM_TABLE.md:1139 | author_characterization | CLASS_UNSET | kavik      counter_case filled     4
2026-05-23 | Simulators | fold-matrix/CLAIM_TABLE.md:1140 | author_characterization | CLASS_UNSET | kavik      counter_case UNFILLED   1
2026-05-23 | Simulators | fold-matrix/CLAIM_TABLE.md:1144 | author_characterization | CLASS_UNSET | kavik-sourced terms do.** Total separation.
2026-05-23 | Simulators | fold-matrix/CLAIM_TABLE.md:1146 | author_characterization | CLASS_UNSET | Two readings and the register cannot distinguish them: the kavik terms
2026-05-23 | Simulators | fold-matrix/fold_register.py:102 | author_characterization | CLASS_UNSET | # ---- candidates: same signature, not yet cut by Kavik ----
2026-05-23 | Simulators | fold-matrix/fold_register.py:20 | author_characterization | CLASS_UNSET | KAVIK = "kavik"          # term she named
2026-05-23 | Simulators | fold-matrix/fold_register.py:58 | author_characterization | CLASS_UNSET | "source": KAVIK,
2026-05-23 | Simulators | fold-matrix/fold_register.py:67 | author_characterization | CLASS_UNSET | "source": KAVIK,
2026-05-23 | Simulators | fold-matrix/fold_register.py:75 | author_characterization | CLASS_UNSET | "source": KAVIK,
2026-05-23 | Simulators | fold-matrix/fold_register.py:83 | author_characterization | CLASS_UNSET | "source": KAVIK,
2026-05-23 | Simulators | fold-matrix/fold_register.py:93 | author_characterization | CLASS_UNSET | "source": KAVIK,
2026-05-23 | Simulators | fold-matrix/register_audit.py:184 | author_characterization | CLASS_UNSET | out.append("   Separation is total: every filled one is kavik-sourced,")
2026-05-23 | Simulators | fold-matrix/register_audit.py:287 | author_characterization | CLASS_UNSET | chk("most kavik terms do", t[("kavik", True)] >= 4)
2026-05-23 | Simulators | fold-matrix/register_audit.py:288 | author_characterization | CLASS_UNSET | chk("exactly one kavik term does not", t[("kavik", False)] == 1)
2026-05-23 | Simulators | fold-matrix/register_audit.py:332 | author_characterization | CLASS_UNSET; PROHIBITION? | chk("no argument falls through to --list", rc == 0 and "kavik" in o)
2026-05-23 | Simulators | fold-matrix/samples/register_audit.sample.txt:18 | author_characterization | CLASS_UNSET | kavik      counter_case UNFILLED 1
2026-05-23 | Simulators | fold-matrix/samples/register_audit.sample.txt:19 | author_characterization | CLASS_UNSET | kavik      counter_case filled   4
2026-05-23 | Simulators | fold-matrix/samples/register_audit.sample.txt:20 | author_characterization | CLASS_UNSET | Separation is total: every filled one is kavik-sourced,
2026-05-23 | Simulators | fragility-cascade/EXPERIMENT_register.md:103 | author_characterization | CLASS_UNSET | only Kavik can score this. I can only record the prediction.
2026-05-23 | Simulators | fragility-cascade/EXPERIMENT_register.md:11 | author_characterization | CLASS_UNSET | [F]  field       — needs Kavik's measurements on ice/rig/dock. My blind_to.
2026-05-23 | Simulators | fragility-cascade/EXPERIMENT_register.md:151 | author_characterization | CLASS_UNSET | hand to field:     E11 E12 E13 E14         (Kavik / partner)
2026-05-23 | Simulators | fragility-cascade/EXPERIMENT_register.md:257 | author_characterization | CLASS_UNSET | E11 E12 E13 E14   field, Kavik/partner only
2026-05-23 | Simulators | fragility-cascade/EXPERIMENT_register.md:94 | author_characterization | CLASS_UNSET | ## C. SEAMS ONLY THE FIELD CAN TEST  (Kavik / partner — my blind_to)
2026-05-23 | Simulators | fragility-cascade/OPEN_E9_walking_criterion.md:54 | author_characterization | CLASS_UNSET | Kavik's operational logs over months (register E16) supply it. Until then
2026-05-23 | Simulators | frame-location-benchmark/README.md:127 | author_characterization | CLASS_UNSET | Answer quality, knowledge breadth, calibration, and anything about the author
2026-05-23 | Simulators | model-deprecation-backcast/README.md:96 | author_characterization | CLASS_UNSET; PROHIBITION? | No section about the author, no working-style profile, no characterization of
2026-05-23 | Simulators | model-deprecation-backcast/WORK_ORDER.md:169 | author_characterization | CLASS_UNSET; PROHIBITION? | No section about the author. No working-style or author-profile
2026-05-23 | Simulators | move-set/move_set_audit.py:188 | author_characterization | CLASS_UNSET | "reading": "M3 says venue tier drops out because the author is the same. "
2026-05-23 | Simulators | move-set/samples/move_set_audit.sample.txt:69 | author_characterization | CLASS_UNSET | M3 says venue tier drops out because the author is the same. M5
2026-05-23 | Simulators | notes/markers/HELD_2026_08_31.md:173 | author_characterization | CLASS_UNSET | method. Kavik's call.
2026-05-23 | Simulators | notes/markers/HELD_2026_08_31.md:88 | author_characterization | CLASS_UNSET | source      Kavik. Not derived from the literature.
2026-05-23 | Simulators | quiet-failure/CLAIM_TABLE.md:23 | author_characterization | CLASS_UNSET; PROHIBITION? | | QFA_013 | The order's sentence placing agentic AI infrastructure "at the pre-Tacoma stage: designed to calculated load, no accumulated margin" is carried as DERIVED and scored by nothing here. The a
2026-05-23 | Simulators | quiet-failure/README.md:29 | author_characterization | CLASS_UNSET; PROHIBITION? | | position | the order places agentic AI infrastructure "at the pre-Tacoma stage: designed to calculated load, no accumulated margin"; the author is an instance of that class. The sentence is carried,
2026-05-23 | Simulators | quiet-failure/run_all.py:17 | author_characterization | CLASS_UNSET; PROHIBITION? | designed to calculated load, no accumulated margin"; the author is an
2026-05-23 | Simulators | quiet-failure/samples/run_all.sample.txt:5 | author_characterization | CLASS_UNSET; PROHIBITION? | designed to calculated load, no accumulated margin"; the author is an
2026-05-23 | Simulators | recommender-confound/WORK_ORDER_02.md:90 | author_characterization | CLASS_UNSET | F repo creation — Kavik's call
2026-05-23 | Simulators | reporting-chain-loss/WORK_ORDER.md:176 | author_characterization | CLASS_UNSET | PREDICTED DIRECTION (Kavik, stated before the run): reporting rate changes.
2026-05-23 | Simulators | research-stability-audit/CITATION.cff:6 | author_characterization | CLASS_UNSET | given-names: Kavik
2026-05-23 | Simulators | uninstrumented/AUDIT_NOTES.md:3148 | author_characterization | CLASS_UNSET | which is a different claim about the author's state and a stronger one.
2026-05-23 | Simulators | uninstrumented/AUDIT_NOTES.md:728 | author_characterization | CLASS_UNSET | `[stated by Kavik]`, attached to Q4. First provenance tag inside a
2026-05-23 | Simulators | uninstrumented/CLAIM_TABLE.md:396 | author_characterization | CLASS_UNSET | | `UNI_035` | `[stated by Kavik]` is the **first provenance tag inside a register entry**, and it is attached to one sub-question — the half the SPLIT IS OPEN section says may leave as a separate case
2026-05-23 | Simulators | uninstrumented/CLAIM_TABLE.md:421 | author_characterization | CLASS_UNSET | | `UNI_048` | Three `[stated by Kavik]` tags, up from one in Case 013 — the device is now used at scale, and its distribution is informative: the single **untagged** question is the one with an indepe
2026-05-23 | Simulators | uninstrumented/OPEN_QUESTIONS.md:45 | author_characterization | CLASS_UNSET | *Provenance: the fine-as-threshold reading is stated by Kavik and is
2026-05-23 | Simulators | uninstrumented/WORK_ORDER_03.md:285 | author_characterization | CLASS_UNSET | OPEN, for Kavik
2026-05-23 | Simulators | uninstrumented/WORK_ORDER_03.md:74 | author_characterization | CLASS_UNSET | reading is Kavik's. It is not in the literature. Render it as
2026-05-23 | Simulators | uninstrumented/cases/013compensationloadunattributed.md:91 | author_characterization | CLASS_UNSET | [stated by Kavik] Solutions to this exact problem already exist and are
2026-05-23 | Simulators | uninstrumented/cases/014offloadingevolutionaryframing.md:117 | author_characterization | CLASS_UNSET | [stated by Kavik] The value in human-AI coupling lies in the
2026-05-23 | Simulators | uninstrumented/cases/014offloadingevolutionaryframing.md:69 | author_characterization | CLASS_UNSET | [stated by Kavik] "Human evolution led to this point" resolves in
2026-05-23 | Simulators | uninstrumented/cases/014offloadingevolutionaryframing.md:92 | author_characterization | CLASS_UNSET | [stated by Kavik] The channels co-vary and feed the same outcome.
2026-05-23 | Simulators | uninstrumented/cases/020attributedagencyarrangement.md:32 | author_characterization | CLASS_UNSET | ## THE SHAPE (Kavik's, extended in conversation)
2026-05-23 | Simulators | uninstrumented/cases/021sensesubstitutionundeclaredaxis.md:125 | author_characterization | CLASS_UNSET | whether it produces the state. That connection is Kavik's marker and is held as one.
2026-05-23 | Simulators | uninstrumented/cases/021sensesubstitutionundeclaredaxis.md:71 | author_characterization | CLASS_UNSET | ## WHY THIS MAY FEED THE FEAR STATE (Kavik's, held as a marker)
2026-05-23 | Simulators | uninstrumented/cases/023borrowedselectionvocabulary.md:122 | author_characterization | CLASS_UNSET | ## THE AMPLIFICATION ARM (Kavik's, held as a marker)
2026-05-23 | Simulators | uninstrumented/playground/README.md:109 | author_characterization | CLASS_UNSET | Kavik's repositories are running an informal version of M2 right now: published CC0,
2026-05-23 | Simulators | uninstrumented/samples/case_013_audit.sample.txt:52 | author_characterization | CLASS_UNSET | found in Q4: [stated by Kavik]
2026-05-23 | Simulators | uninstrumented/samples/case_021_audit.sample.txt:116 | author_characterization | CLASS_UNSET | WHY THIS MAY FEED THE FEAR STATE (Kavik's, held  none
2026-05-23 | Simulators | uninstrumented/samples/playground_audit.sample.txt:135 | author_characterization | CLASS_UNSET; PROHIBITION? | Kavik's repositories are running an informal version of M2 right now: published CC0, crawler-discoverable, read by models that produce readings. `specimens/2026-08-18-model-A.md` is an M2 run with no 
2026-05-23 | Simulators | uninstrumented/specimens/INSTANCE_LOG_SURVEY.md:449 | author_characterization | CLASS_UNSET | is which. A20's list is malformed as written (`[Kavik", "Claude", ...` — the
2026-05-23 | Simulators | AMOC/OPEN_RESEARCH.md:255 | calibration_locus |  | **Falsifier:** The literature shows no consensus on Sv→F mapping (then the calibration remains under-determined, which is itself a finding).
2026-05-23 | Simulators | AMOC/OPEN_RESEARCH.md:70 | calibration_locus |  | 4. Calibrate the rel_0_1 scale against a reference (e.g., pure quartz sand = 0, peat = 1)
2026-05-23 | Simulators | CLAUDE.md:1335 | calibration_locus |  | Reference implementation in `src/gdprf/`: `engine.py` (calibration,
2026-05-23 | Simulators | CLAUDE.md:3917 | calibration_locus |  | is the central-reference scoring the drop's own CALIBRATION CONSTRAINT
2026-05-23 | Simulators | assessor-coupling/WORK_ORDER.md:249 | calibration_locus |  | calibration check on the instrument itself.
2026-05-23 | Simulators | climate-modeling/OPEN_RESEARCH.md:559 | calibration_locus |  | Many models are calibrated on a stationary window — a historical period assumed to be representative of the future. Parameters are held constant. If the model says "impacts will be X," that is treated
2026-05-23 | Simulators | climate-modeling/OPEN_RESEARCH.md:593 | calibration_locus |  | But parsimony is a preference, not a physical law. A simple model may fit the calibration data well and still miss the cascade in deployment. The model that "wins" the contest may be the one that is m
2026-05-23 | Simulators | columbia-chain-cascade/OPEN_QUESTIONS.md:501 | calibration_locus |  | An undergraduate who closes one of these gaps — who calibrates the urban
2026-05-23 | Simulators | columbia-chain-cascade/UNDERGRADUATE_RESEARCH_GAPS_V2.md:1151 | calibration_locus |  | An undergraduate who closes one of these gaps — who calibrates the urban
2026-05-23 | Simulators | cooperative-substrate-proof/fixtures/methods_CONSTRUCTED.txt:3 | calibration_locus |  | Soil cores were collected with a 5 cm split-tube sampler at 10 cm depth. Samples were dried at 105 C for 24 h in a laboratory oven and weighed on an analytical balance calibrated against a 100 g refer
2026-05-23 | Simulators | cooperative-substrate-proof/p1_dependency_records.py:43 | calibration_locus |  | "CALIBRATION": r"\b(calibrated|traceable|reference mass|reference standard|standard reference|NIST|BIPM|certified)\b",
2026-05-23 | Simulators | cooperative-substrate-proof/samples/run_all.sample.txt:78 | calibration_locus |  | SOURCED   CALIBRATION     reference mass               in_argument=False fixtures/methods_CONSTRUCTED.txt:3[311:325]
2026-05-23 | Simulators | cooperative-substrate-proof/selftest.py:57 | calibration_locus |  | voc = "the instrument reads the field at the stated resolution and the calibration chain is recorded".split()
2026-05-23 | Simulators | cooperative-substrate/EVIDENCE_PACK.md:34 | calibration_locus |  | **Use in P1:** these are the model case for "the mechanism was always dependency accounting; the competition vocabulary sits in the narration on top." The extraction target is the same layer — methods
2026-05-23 | Simulators | cooperative-substrate/p1_deps_extract.py:32 | calibration_locus |  | r"\b(?:calibrated|traceable|standardi[sz]ed|referenced|normali[sz]ed)\s+"
2026-05-23 | Simulators | criteria-drift/SOURCE_DROP_KIMI.md:16 | calibration_locus |  | The field: National standards bodies (NIST, ILAC, EURAMET) have formalized exactly your K14 → K15 → K16 chain under the name calibration interval determination.
2026-05-23 | Simulators | criteria-drift/SOURCE_DROP_KIMI.md:19 | calibration_locus |  | •  Calibration intervals must not be arbitrary. ISO/IEC 17025 requires intervals be technically justified based on historical drift data, not calendar schedules cite🛠web_search:20#2:~:text=No standar
2026-05-23 | Simulators | criteria-drift/anchor.py:229 | calibration_locus |  | print("  standard, and as-found/as-left at every calibration.")
2026-05-23 | Simulators | criteria-drift/samples/anchor.sample.txt:109 | calibration_locus |  | standard, and as-found/as-left at every calibration.
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:1052 | calibration_locus |  | Reference implementation in `src/gdprf/`: `engine.py` (calibration,
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:3401 | calibration_locus |  | is the central-reference scoring the drop's own CALIBRATION CONSTRAINT
2026-05-23 | Simulators | energy/modules/metrology_diagnostic.py:199 | calibration_locus |  | final_action = "ACTION: Calibrate hardware against standards. Redesign survey."
2026-05-23 | Simulators | external-audit/DEEP_RESEARCH_2026_09_14.md:589 | calibration_locus |  | | 10 | Reference-output validation for F4 models (methane impulse response, synergy reference models, AMOC sign/magnitude) via `null-harness` | F4 | 1–2 weeks | Teaching repo → calibrated, citable ins
2026-05-23 | Simulators | external-audit/DEEP_RESEARCH_2026_09_14_V2.md:34 | calibration_locus |  | | `self-scan/census.py` | **Complete: 5 SOME_FAILED / 5 SOME_FAILED_UNCOUNTED / 110 NONZERO_EXIT_NO_VERDICT / 8 OK**, plus EXCLUDED_SELF_REFERENCE for itself | The repo's own whole-tree runner — an in
2026-05-23 | Simulators | external-audit/DEEP_RESEARCH_2026_09_14_V2.md:608 | calibration_locus |  | | 10 | Reference-output validation for F4 models (methane impulse response, synergy reference models, AMOC sign/magnitude) via `null-harness` | F4 | 1–2 weeks | Teaching repo → calibrated, citable ins
2026-05-23 | Simulators | extraction-blindness-sim/blindness.py:55 | calibration_locus |  | "M1": 0.95,  # calibrated reading against a reference
2026-05-23 | Simulators | fragility-cascade/additional.md:5 | calibration_locus |  | C28 engagement_threshold.py Human engagement is a thermodynamic decision governed by Net Engagement Value (NEV). NEV = (Calibration Gain — Friction Cost) / Energy Expenditure. When NEV drops below 1.0
2026-05-23 | Simulators | fragility-cascade/info_taxonomy.py:86 | calibration_locus |  | "calibration drift", "recalibration against a standard"),
2026-05-23 | Simulators | fragility-cascade/thermo_know.py:68 | calibration_locus |  | stays_fresh_by="recalibration against a known standard"),
2026-05-23 | Simulators | fragility-cascade/valence_drift_test.py:60 | calibration_locus |  | # U2: V_d calibrated so reference community (n=1, form A, n0=1) plateaus
2026-05-23 | Simulators | gdprf-framework/docs/operational-cycle.md:58 | calibration_locus |  | - Calibration quality itself is tracked via `expected_calibration_error`;
2026-05-23 | Simulators | gdprf-framework/examples/biomass-claim.example.json:103 | calibration_locus |  | "reference_standard": "hard-target range calibration"
2026-05-23 | Simulators | gdprf-framework/examples/biomass-claim.example.json:41 | calibration_locus |  | "calibration_source": "42 harvested reference trees, Panama (transfer)",
2026-05-23 | Simulators | generation-capacity/AUDIT_NOTES.md:152 | calibration_locus |  | central reference, which the CALIBRATION CONSTRAINT forbids.
2026-05-23 | Simulators | generation-capacity/MECHANISM_10.md:50 | calibration_locus |  | ## CALIBRATION CONSTRAINT ON THE INSTRUMENT
2026-05-23 | Simulators | generation-capacity/cases/informed-gate.json:28 | calibration_locus |  | "notes": "Loop form fully instanced: gate produces the deficit, deficit justifies the gate. Calibration constraint is live here — 'informed' scored against the deciding body's knowledge base returns s
2026-05-23 | Simulators | generation-capacity/mechanism_10_audit.py:231 | calibration_locus |  | against a central reference, which the CALIBRATION CONSTRAINT four
2026-05-23 | Simulators | generation-capacity/samples/audit.sample.txt:115 | calibration_locus |  | against a central reference, which the CALIBRATION CONSTRAINT four
2026-05-23 | Simulators | grounding-layers/CLAIMS.md:1018 | calibration_locus |  | the instrument (specifically, `calibration_offset` is NOT
2026-05-23 | Simulators | grounding-layers/CLAIMS.md:1852 | calibration_locus |  | **SCOPE.** T=uncalibrated | S=uncalibrated | O=any_human | C=biomedical_frame (the six factors — physical_state, nutritional_state, health, career, living_conditions, environment — are HUMAN embodied 
2026-05-23 | Simulators | grounding-layers/CLAIMS.md:2241 | calibration_locus |  | allowing the instrument's own bias (e.g., human-centric calibration)
2026-05-23 | Simulators | grounding-layers/organize.md:225 | calibration_locus |  | │  Lε Check   │  Is the instrument calibrated? Noise? Drift?
2026-05-23 | Simulators | instrument-bias-sims/OPEN_RESEARCH.md:397 | calibration_locus |  | The framework refuses to record an instrument as neutral. Instead, it records the instrument as biased—by its denominator, its anchor, its rubric, its excluded subjects, its normalisers, or its sign c
2026-05-23 | Simulators | instrument-epistemology/PACKAGE_README.md:27 | calibration_locus |  | 4. **Traceability** — is there an unbroken calibration chain to a reference
2026-05-23 | Simulators | instrument-epistemology/README.md:48 | calibration_locus |  | 4. **Traceability** — unbroken calibration chain to an SI reference
2026-05-23 | Simulators | instrument-epistemology/docs/protocol.md:34 | calibration_locus |  | Walk the calibration chain: instrument → working standard → reference standard
2026-05-23 | Simulators | instrument-epistemology/docs/protocol.md:36 | calibration_locus |  | ecological measurands), chain lapses (expired calibration), or the standard
2026-05-23 | Simulators | instrument-epistemology/docs/traceability-and-blindness.md:28 | calibration_locus |  | | M1 | Calibrated reading | Reference standard quality | temperature from calibrated thermometer |
2026-05-23 | Simulators | instrument-epistemology/experiments/isotope_diet/run.py:45 | calibration_locus |  | {"level": "instrument", "status": "ok", "note": "IRMS calibrated vs. IAEA reference materials"},
2026-05-23 | Simulators | instrument-epistemology/experiments/lidar_biomass/run.py:42 | calibration_locus |  | {"level": "working_standard", "status": "ok", "note": "calibrated ground plots"},
2026-05-23 | Simulators | instrument-epistemology/experiments/seismometer/run.py:44 | calibration_locus |  | {"level": "working_standard", "status": "ok", "note": "calibrated reference seismometers"},
2026-05-23 | Simulators | investigation-sim/cases/held-but-unasked.json:18 | calibration_locus |  | "no_instrument": "the gauges exist, were calibrated, and reported continuously. The instrument is not blind",
2026-05-23 | Simulators | measurement-fork/systems/variable_provisioning.json:3 | calibration_locus |  | "description": "An organism developed under a variable resource regime, later assessed against a fixed reference population. The question is whether measured differences are properties of the organism
2026-05-23 | Simulators | notes/memory-export/SCRUB_RULES.md:84 | calibration_locus |  | operating preferences or calibration — those live in tier 3 and stay private.
2026-05-23 | Simulators | notes/memory-export/files/agreement-mode.md:560 | calibration_locus |  | CALIBRATING THE INSTRUMENT.**
2026-05-23 | Simulators | notes/memory-export/files/merit-anchoring.md:282 | calibration_locus |  | [[native-substrate-cognition]] and [[internal-calibration-priority]]: **the internal reference must
2026-05-23 | Simulators | notes/memory-export/files/merit-anchoring.md:308 | calibration_locus |  | range with the other channels uncalibrated — **and the instrument sees only the range.**
2026-05-23 | Simulators | notes/memory-export/files/shape-index.md:54 | calibration_locus |  | Cross-references [[median-case-calibration]]: same move, a term calibrated on the common
2026-05-23 | Simulators | proxy-investigation-lab/experiments/wim_pavement/run.py:55 | calibration_locus |  | "upgrade_path": "none needed; scheduled recalibration vs. reference weighbridge"},
2026-05-23 | Simulators | proxy-investigation-lab/outputs/wim-pavement.investigation.json:85 | calibration_locus |  | "upgrade_path": "none needed; scheduled recalibration vs. reference weighbridge"
2026-05-23 | Simulators | railcar-containment/tenability.py:13 | calibration_locus |  | After calibration the model reproduces those published facts by construction.
2026-05-23 | Simulators | reasoning-dial/CLAIM_TABLE.md:251 | calibration_locus |  | itself miscalibrated."* A `G-STATE` field would record a self-report, and a
2026-05-23 | Simulators | reasoning-dial/SOURCE_DROP.md:335 | calibration_locus |  | dial. It's knowing when your read on the dial is itself miscalibrated.
2026-05-23 | Simulators | revision-survival/SOURCE_DROP.md:1675 | calibration_locus |  | "consuming the calibration standard to construct
2026-05-23 | Simulators | thermal-sensor-degradation-audit/CLAIM_TABLE.md:45 | calibration_locus |  | | **TSD_005** | Projected sensor drift scales approximately linearly with total time since last calibration at fixed internal temperature. `sensor_drift(..., t_cal_days=T)` returns drift proportional 
2026-05-23 | Simulators | triad-playground/SOURCE_DROP.md:27 | calibration_locus |  | | Instrument | The thing producing numbers | Is the instrument calibrated and traceable? |
2026-05-23 | Simulators | triad-playground/SPEC_V1.md:24 | calibration_locus |  | - **Calibration Question**: Is the instrument calibrated and traceable?
2026-05-23 | Simulators | triad-playground/spec_v1.json:138 | calibration_locus |  | "[ ] Calibration method stated (when, how, against what standard)",
2026-05-23 | Simulators | triad-playground/spec_v1.json:23 | calibration_locus |  | "calibration_question": "Is the instrument calibrated and traceable?",
2026-05-23 | Simulators | uninstrumented/case_023_audit.py:96 | calibration_locus |  | be right. What the calibration set shows is a claim about the INSTRUMENT: as
2026-05-23 | Simulators | uninstrumented/samples/case_023_audit.sample.txt:32 | calibration_locus |  | be right. What the calibration set shows is a claim about the INSTRUMENT: as
2026-05-23 | Simulators | uninstrumented/specimens/INSTANCE_LOG_INDEX.md:110 | calibration_locus |  | | R02 (A2) | `calibration/logs/user_2026_05_04_T22.json` | `$` | `profile_type="user_architecture_assessment"` | `4082f027` | undeclared | `profile_type · user_id · timestamp · substrate_primary_confi
2026-05-23 | Simulators | uninstrumented/specimens/INSTANCE_LOG_INDEX.md:112 | calibration_locus |  | | R04 (A3) | `calibration/logs/2026-05-05_claude_audit_field-guide-session.json` | `correction_cycle.sequence[0]` | `unrecorded (no class field)` | `dd16d1f3` | undeclared; element unidentified in sou
2026-05-23 | Simulators | uninstrumented/specimens/INSTANCE_LOG_INDEX.md:167 | calibration_locus |  | | R37 (A9) | `logs/2025-09-06-2355Z.json` | `$` | `unrecorded (no class field)` | `36d44717` | `audit_log.schema.json#anyOf[5]` | `audit_timestamp · auditor · subject_user · ethics_alignment · protoco
2026-05-23 | Simulators | uninstrumented/specimens/INSTANCE_LOG_SURVEY.md:100 | calibration_locus |  | | A5 | `Documented_Instances_Of_AI_Self_Calibration.md` | JinnZ2 (profile repo) | 2026-05-21 | `Claude`, version withheld at the model's request | row 3 |
2026-05-23 | Simulators | notes/memory-export/files/rate-mismatch-polytope.md:17 | contort | OTHER_SENSE? | trajectory toward breaking or contorting the whole.
2026-05-23 | Simulators | assessor-coupling/WORK_ORDER.md:249 | instrument_to_world |  | calibration check on the instrument itself.
2026-05-23 | Simulators | falsifier-audit/AUDIT_NOTES.md:3 | instrument_to_world |  | Findings on the instrument itself, kept as prose rather than a claim table.
2026-05-23 | Simulators | fragility-cascade/Claude-check.md:421 | instrument_to_world |  | C29 the_laboratory.py An LLM can autonomously run a refutation loop: instrument itself, measure A, γ, ω, compute C, run an experiment, compare outcome to claim, and update the claim. This process conv
2026-05-23 | Simulators | membership-probe/README.md:69 | instrument_to_world |  | python3 probe.py selftest    # validate the instrument itself
2026-05-23 | Simulators | membership-probe/probe.py:50 | instrument_to_world |  | python3 probe.py selftest         # validate the instrument itself
2026-05-23 | Simulators | notes/memory-export/files/rubric-backcasting.md:14 | instrument_to_world |  | would have gotten wrong**, to produce a measurable FALSE-NULL RATE for the instrument itself.
2026-05-23 | Simulators | CLAUDE.md:508 | rule1_dXdt |  | under AI speed, dE/dT = 0 — The Decoupling Result).
2026-05-23 | Simulators | CLAUDE.md:6660 | rule1_dXdt |  | raw partial `dY/dX` carries units and years divided by that is not a
2026-05-23 | Simulators | CLAUDE.md:8182 | rule1_dXdt |  | instrument:** Section 5's rate form — where dE/dt > dM/dt **sustained** the
2026-05-23 | Simulators | CLAUDE.md:8231 | rule1_dXdt |  | `record_updates` over one season → dE/dt vs dM/dt (binned), per-class lag,
2026-05-23 | Simulators | alignment-under-coupling/sim_c_loop_threshold.py:24 | rule1_dXdt |  | dC/dt ∝ Q^(2*gamma) - C
2026-05-23 | Simulators | ch4-four-box/RESULTS.md:83 | rule1_dXdt |  | WAIS / SCA, and dE/dC at that point
2026-05-23 | Simulators | ch4-four-box/tn_inversion.py:79 | rule1_dXdt |  | "  effective dE/dC      %10.4f Tg/ppb  (table)" % (r["delta_E"] / r["delta_C"]),
2026-05-23 | Simulators | ch4-four-box/tn_inversion.py:80 | rule1_dXdt |  | "  local  dE/dC         %10.4f Tg/ppb  (M[TN][TN])" % r["dE_dC_local_Tg_per_ppb"]]
2026-05-23 | Simulators | claim-audits/claim_audit_pasted_2026_08_05.py:227 | rule1_dXdt |  | "resolution.  Worse: dEsq/da is a symmetric-difference on the "
2026-05-23 | Simulators | claim-audits/claim_audit_visibility.py:112 | rule1_dXdt |  | "dS/dt = -integral(J.dA) + Sigma as the universal survival equation; "
2026-05-23 | Simulators | claim-audits/samples/claim_audit_visibility.sample.txt:27 | rule1_dXdt |  | V5    M    IDENTITY            dS/dt = -integral(J.dA) + Sigma as the unive
2026-05-23 | Simulators | claim-record/CLAIM_TABLE.md:299 | rule1_dXdt |  | literally, `dY/dX` carries the units of the result over the units of the
2026-05-23 | Simulators | claim-record/SPEC.md:162 | rule1_dXdt |  | **The coupling has to be dimensionless.** A raw partial `dY/dX` carries
2026-05-23 | Simulators | columbia-chain-cascade/GAP_14_mining_hydrology.md:109 | rule1_dXdt |  | dW/dt = c·(W₀ − W(t))   →   W(t) = W₀·(1 − e^(−c·t))
2026-05-23 | Simulators | columbia-chain-cascade/UNDERGRADUATE_RESEARCH_GAPS_V2.md:785 | rule1_dXdt |  | dW/dt = c·(W₀ − W(t))   →   W(t) = W₀·(1 − e^(−c·t))
2026-05-23 | Simulators | consensus-anchor/textfree.py:274 | rule1_dXdt |  | """chi = dm/dh under a small external field toward position 0."""
2026-05-23 | Simulators | continuity-audit/README.md:48 | rule1_dXdt |  | - `trajectory` — the full `dX/dt` history,
2026-05-23 | Simulators | continuity-audit/continuity_audit.py:134 | rule1_dXdt |  | rate = dC / (steps * dt)                    # dC/dt averaged over horizon
2026-05-23 | Simulators | continuity-audit/continuity_audit.py:169 | rule1_dXdt |  | "trajectory": traj,        # full dX/dt history -- anti-freeze
2026-05-23 | Simulators | continuity-audit/continuity_audit.py:199 | rule1_dXdt |  | print(f"  dC/dt          : {r['dC_dt']:+}")
2026-05-23 | Simulators | continuity-audit/samples/README.md:22 | rule1_dXdt |  | resilience floor, so `dC/dt` lands inside the `eps` band and the
2026-05-23 | Simulators | continuity-audit/samples/demo.sample.txt:13 | rule1_dXdt |  | dC/dt          : +0.0
2026-05-23 | Simulators | continuity-audit/samples/demo.sample.txt:22 | rule1_dXdt |  | dC/dt          : +0.000176
2026-05-23 | Simulators | continuity-audit/samples/demo.sample.txt:4 | rule1_dXdt |  | dC/dt          : -0.08252
2026-05-23 | Simulators | crossdomain-eval/crossdomain_eval/numerical.py:31 | rule1_dXdt |  | rhs: Right-hand side ``f(t, y) -> dy/dt``.
2026-05-23 | Simulators | cycle-ledger/CLAIM_TABLE.md:10 | rule1_dXdt |  | rate form on a data layer: dE/dt vs dM/dt over one season, per-class lag,
2026-05-23 | Simulators | cycle-ledger/README.md:56 | rule1_dXdt |  | - **dE/dt** (events per window) vs **dM/dt** (record updates per window), a
2026-05-23 | Simulators | cycle-ledger/README.md:68 | rule1_dXdt |  | - dE/dt > dM/dt **sustained** AND a **nonzero** unrecorded set → **STRUCTURAL**.
2026-05-23 | Simulators | cycle-ledger/README.md:70 | rule1_dXdt |  | - dM/dt ≥ dE/dt with the unrecorded set **empty** → **MATURITY_GAP**. Closes
2026-05-23 | Simulators | cycle-ledger/README.md:91 | rule1_dXdt |  | | `rate_gap.py` | Deliverable 2 — dE/dt vs dM/dt, per-class lag, the unrecorded set (imports `rate_form`) |
2026-05-23 | Simulators | cycle-ledger/WORK_ORDER.md:122 | rule1_dXdt |  | dE/dt      environment state-change rate
2026-05-23 | Simulators | cycle-ledger/WORK_ORDER.md:123 | rule1_dXdt |  | dM/dt      achieved record refresh rate
2026-05-23 | Simulators | cycle-ledger/WORK_ORDER.md:128 | rule1_dXdt |  | dE/dt > dM/dt sustained, with a nonzero unrecorded set
2026-05-23 | Simulators | cycle-ledger/WORK_ORDER.md:130 | rule1_dXdt |  | dM/dt >= dE/dt with unrecorded set empty
2026-05-23 | Simulators | cycle-ledger/rate_gap.py:118 | rule1_dXdt |  | # ---- rate series (dE/dt, dM/dt) -------------------------------------------
2026-05-23 | Simulators | cycle-ledger/rate_gap.py:16 | rule1_dXdt |  | dE/dt      environment state-change rate (events per window)
2026-05-23 | Simulators | cycle-ledger/rate_gap.py:17 | rule1_dXdt |  | dM/dt      achieved record refresh rate  (updates per window)
2026-05-23 | Simulators | cycle-ledger/rate_gap.py:23 | rule1_dXdt |  | dE/dt > dM/dt SUSTAINED, with a NONZERO unrecorded set
2026-05-23 | Simulators | cycle-ledger/rate_gap.py:25 | rule1_dXdt |  | dM/dt >= dE/dt with the unrecorded set EMPTY
2026-05-23 | Simulators | cycle-ledger/rate_gap.py:312 | rule1_dXdt |  | L.append("dE/dt vs dM/dt  (per %d-day window, %d windows)"
2026-05-23 | Simulators | cycle-ledger/samples/cll_demo.sample.txt:79 | rule1_dXdt |  | dE/dt vs dM/dt  (per 7-day window, 17 windows)
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:226 | rule1_dXdt |  | under AI speed, dE/dT = 0 — The Decoupling Result).
2026-05-23 | Simulators | emergence-stability-simulator/ARCHITECTURE.md:29 | rule1_dXdt |  | | differential-frame-core | dX/dt as universal contract | position dynamics           |
2026-05-23 | Simulators | emergence-stability-simulator/README.md:125 | rule1_dXdt |  | - `differential-frame-core` — shared dX/dt contract
2026-05-23 | Simulators | exploration-engine/exploration_engine.py:112 | rule1_dXdt |  | # F = -dV/dx for V = a x^4 - b x^2 + tilt*x - drive*x
2026-05-23 | Simulators | fragility-cascade/CLAIM_TABLE.md:33 | rule1_dXdt |  | | R4 | **Substrate exposure is invariant under AI advancement rate: `dE/dT = 0`.** A possession-held physical asset has zero downstream layers and therefore zero redesign windows. | Exhibit a possessi
2026-05-23 | Simulators | fragility-cascade/README.md:155 | rule1_dXdt |  | `dE/dT = 0`. Nothing downstream to rewrite. So substrate anchoring is not a brake on
2026-05-23 | Simulators | fragility-cascade/cascade_redesign_M_collapse.py:72 | rule1_dXdt |  | print("  Substrate dE/dT = 0.0 (flat). Ground holds; AI runs free without dragging downstream.")
2026-05-23 | Simulators | fragility-cascade/cascade_redesign_vulnerability.py:226 | rule1_dXdt |  | print("\n  Substrate column is FLAT AT ZERO. dE/dT = 0. That is claim R4.")
2026-05-23 | Simulators | fragility-cascade/cascade_redesign_vulnerability.py:47 | rule1_dXdt |  | R4. Substrate exposure is INVARIANT under AI advancement rate. dE/dT = 0.
2026-05-23 | Simulators | fragility-cascade/communication_gradients.py:135 | rule1_dXdt |  | print(f"  Gradients: dCI/dE={grad['dCI_dE']:+.3f}, dCI/dF={grad['dCI_dF']:+.3f}, "
2026-05-23 | Simulators | fragility-cascade/communication_gradients.py:136 | rule1_dXdt |  | f"dCI/dG={grad['dCI_dG']:+.3f}, dCI/dH={grad['dCI_dH']:+.3f}, dCI/dA={grad['dCI_dA']:+.3f}")
2026-05-23 | Simulators | fragility-cascade/field_collapse.py:105 | rule1_dXdt |  | """Curvature. Zero coincident with dF/dphi=0 marks the spinodal."""
2026-05-23 | Simulators | fragility-cascade/field_collapse.py:111 | rule1_dXdt |  | """Discriminant of  dF/dphi = phi^3 - phi - h = 0.
2026-05-23 | Simulators | fragility-cascade/field_collapse.py:164 | rule1_dXdt |  | print("local maximum. Solve dF/dphi = 0 AND d2F/dphi2 = 0 together:")
2026-05-23 | Simulators | fragility-cascade/field_collapse.py:181 | rule1_dXdt |  | print("Real-root count of  dF/dphi = phi^3 - phi - h = 0  vs h:")
2026-05-23 | Simulators | fragility-cascade/samples/cascade_redesign_M_collapse.sample.txt:25 | rule1_dXdt |  | Substrate dE/dT = 0.0 (flat). Ground holds; AI runs free without dragging downstream.
2026-05-23 | Simulators | fragility-cascade/samples/cascade_redesign_vulnerability.sample.txt:33 | rule1_dXdt |  | Substrate column is FLAT AT ZERO. dE/dT = 0. That is claim R4.
2026-05-23 | Simulators | fragility-cascade/samples/communication_gradients.sample.txt:14 | rule1_dXdt |  | Gradients: dCI/dE=+0.111, dCI/dF=+0.156, dCI/dG=-0.067, dCI/dH=-0.133, dCI/dA=+0.178
2026-05-23 | Simulators | fragility-cascade/samples/communication_gradients.sample.txt:20 | rule1_dXdt |  | Gradients: dCI/dE=+0.122, dCI/dF=+0.171, dCI/dG=-0.073, dCI/dH=-0.146, dCI/dA=+0.195
2026-05-23 | Simulators | fragility-cascade/samples/communication_gradients.sample.txt:26 | rule1_dXdt |  | Gradients: dCI/dE=+0.102, dCI/dF=+0.143, dCI/dG=-0.061, dCI/dH=-0.123, dCI/dA=+0.164
2026-05-23 | Simulators | fragility-cascade/samples/communication_gradients.sample.txt:32 | rule1_dXdt |  | Gradients: dCI/dE=+0.125, dCI/dF=+0.175, dCI/dG=-0.075, dCI/dH=-0.150, dCI/dA=+0.200
2026-05-23 | Simulators | fragility-cascade/samples/communication_gradients.sample.txt:8 | rule1_dXdt |  | Gradients: dCI/dE=+0.067, dCI/dF=+0.094, dCI/dG=-0.040, dCI/dH=-0.081, dCI/dA=+0.107
2026-05-23 | Simulators | fragility-cascade/samples/field_collapse.sample.txt:21 | rule1_dXdt |  | Real-root count of  dF/dphi = phi^3 - phi - h = 0  vs h:
2026-05-23 | Simulators | fragility-cascade/samples/field_collapse.sample.txt:8 | rule1_dXdt |  | local maximum. Solve dF/dphi = 0 AND d2F/dphi2 = 0 together:
2026-05-23 | Simulators | fragility-cascade/samples/sensitivity_analysis.sample.txt:38 | rule1_dXdt |  | Sensitivity matrix (dRisk/dA_ij):
2026-05-23 | Simulators | fragility-cascade/sensitivity_analysis.py:163 | rule1_dXdt |  | print("\nSensitivity matrix (dRisk/dA_ij):")
2026-05-23 | Simulators | grounding-layers/CLAIMS.md:60 | rule1_dXdt |  | instrument refactor: reorder the check sequence, swap `np.diff/dt`
2026-05-23 | Simulators | grounding-layers/l3_ecology.py:69 | rule1_dXdt |  | Logistic growth model: dN/dt = r * N * (1 - N/K)
2026-05-23 | Simulators | grounding-layers/tests/test_l0_physics_causality.py:194 | rule1_dXdt |  | we read velocity from OUTSIDE the inspector via np.diff/dt)."""
2026-05-23 | Simulators | legacy/Organize.md:2716 | rule1_dXdt |  | dt = 0.005              # time step (CFL = c0*dt/dx = 0.5, stable)
2026-05-23 | Simulators | legacy/Organize.md:642 | rule1_dXdt |  | p_next[1:-1] = 2*p[1:-1] - p_prev[1:-1] + (c_sound*dt/dz)**2 * (p[2:] - 2*p[1:-1] + p[:-2])
2026-05-23 | Simulators | legacy/Organize2.md:485 | rule1_dXdt |  | - Mass: power-law dN/dM ∝ M^{-1.6} (0.5 M_earth to 13 M_jup)
2026-05-23 | Simulators | mining-increment/SOURCE_DROP.md:59 | rule1_dXdt |  | dW/dt = c·(W₀ − W(t))   →   W(t) = W₀·(1 − e^(−c·t))
2026-05-23 | Simulators | mining-increment/SOURCE_DROP_V2.md:95 | rule1_dXdt |  | dW/dt = c·(W₀ − W(t))   →   W(t) = W₀·(1 − e^(−c·t))
2026-05-23 | Simulators | mining-increment/SOURCE_DROP_V3.md:110 | rule1_dXdt |  | dW/dt = c·(W₀ − W(t))   →   W(t) = W₀·(1 − e^(−c·t))
2026-05-23 | Simulators | photoperiod-claim-harness/photoperiod_claim_harness.py:352 | rule1_dXdt |  | dP/dt   = k_syn * (1 - P/P_max)          <- FLU-clamped synthesis: the
2026-05-23 | Simulators | photoperiod-claim-harness/photoperiod_claim_harness.py:359 | rule1_dXdt |  | dChl/dt = v_conv - k_deg * Chl,  k_deg higher in dark
2026-05-23 | Simulators | play-sims/atmospheric-heating/interactive_dashboard.py:100 | rule1_dXdt |  | p_next[1:-1] = 2*p[1:-1] - p_prev[1:-1] + (c_sound*dt/dz)**2 * (p[2:] - 2*p[1:-1] + p[:-2])
2026-05-23 | Simulators | play-sims/exoplanet-forensics/population_synthesis.py:40 | rule1_dXdt |  | - Mass: power-law dN/dM ∝ M^{-1.6} (0.5 M_earth to 13 M_jup)
2026-05-23 | Simulators | play-sims/plasma-waves/wave_1d_fdtd_through_dust.py:26 | rule1_dXdt |  | dt = 0.005              # time step (CFL = c0*dt/dx = 0.5, stable)
2026-05-23 | Simulators | readout-count/CLAIM_TABLE.md:60 | rule1_dXdt |  | up/flat/down/down) strict equality is False and rho is 0.949: the count
2026-05-23 | Simulators | reasoning-dial/dial_response.py:283 | rule1_dXdt |  | print("  %8s %14s %16s" % ("D_r", "dQ/dlnB", "d2Q/dlnB dD_r"))
2026-05-23 | Simulators | reasoning-dial/overthinking.py:152 | rule1_dXdt |  | print("  %-24s %28s" % ("problem", "min dQ/dlnB over 2..1e7 tokens"))
2026-05-23 | Simulators | reasoning-dial/samples/dial_response.sample.txt:89 | rule1_dXdt |  | D_r        dQ/dlnB    d2Q/dlnB dD_r
2026-05-23 | Simulators | reasoning-dial/samples/overthinking.sample.txt:13 | rule1_dXdt |  | problem                  min dQ/dlnB over 2..1e7 tokens
2026-05-23 | Simulators | routing-data-layer/MARKER.md:154 | rule1_dXdt |  | dE/dt   environment state-change rate
2026-05-23 | Simulators | routing-data-layer/MARKER.md:159 | rule1_dXdt |  | dM/dt   sustainable model refresh rate
2026-05-23 | Simulators | routing-data-layer/MARKER.md:163 | rule1_dXdt |  | Where dE/dt > dM/dt sustained, the null is STRUCTURAL, not
2026-05-23 | Simulators | routing-data-layer/README.md:41 | rule1_dXdt |  | claim: **dE/dt** (environment state-change rate) against **dM/dt**
2026-05-23 | Simulators | routing-data-layer/README.md:43 | rule1_dXdt |  | not by compute). Where dE/dt > dM/dt **sustained**, the null is STRUCTURAL,
2026-05-23 | Simulators | routing-data-layer/README.md:75 | rule1_dXdt |  | | `rate_form.py` | the dE/dt vs dM/dt rate form + `sustained_excess` + the RDL-5 survey decay |
2026-05-23 | Simulators | routing-data-layer/demo_rdl.py:49 | rule1_dXdt |  | L.append("Section 5 rate form (dE/dt vs dM/dt):")
2026-05-23 | Simulators | routing-data-layer/demo_rdl.py:5 | rule1_dXdt |  | dE/dt vs dM/dt rate form, the RDL-5 survey decay, and the F6 upstream
2026-05-23 | Simulators | routing-data-layer/rate_form.py:10 | rule1_dXdt |  | and funding, NOT by compute or reasoning). Where dE/dt > dM/dt SUSTAINED, the
2026-05-23 | Simulators | routing-data-layer/rate_form.py:14 | rule1_dXdt |  | `sustained_excess` is the fraction of the season where dE/dt > dM/dt (a
2026-05-23 | Simulators | routing-data-layer/rate_form.py:26 | rule1_dXdt |  | applied to a data layer. Nothing here is a result: dE/dt and dM/dt are not
2026-05-23 | Simulators | routing-data-layer/rate_form.py:52 | rule1_dXdt |  | """Fraction of paired steps where dE/dt > dM/dt. The metric the verdict
2026-05-23 | Simulators | routing-data-layer/rate_form.py:7 | rule1_dXdt |  | dE/dt is the environment state-change rate (construction, seasonal weight
2026-05-23 | Simulators | routing-data-layer/rate_form.py:8 | rule1_dXdt |  | limits, frost heave, repaint, structure removal), and dM/dt is the
2026-05-23 | Simulators | routing-data-layer/samples/rdl_demo.sample.txt:20 | rule1_dXdt |  | Section 5 rate form (dE/dt vs dM/dt):
2026-05-23 | Simulators | routing-data-layer/selftest_rdl.py:91 | rule1_dXdt |  | print("rate form -- dE/dt vs dM/dt, STRUCTURAL vs MATURITY_GAP:")
2026-05-23 | Simulators | sustained-activation-gate/sustained_activation_gate.py:157 | rule1_dXdt |  | """Gradient of the tilted double-well. Force = -dV/dx.
2026-05-23 | Simulators | thermal-coupling/thermal_coupling.py:133 | rule1_dXdt |  | SENSITIVE to thermal forcing than colder permafrost. dv/dT rises
2026-05-23 | Simulators | thermal-coupling/thermal_coupling.py:46 | rule1_dXdt |  | """Kinetic-growth metamorphism scales with |dT/dz|.
2026-05-23 | Simulators | thermal-coupling/thermal_coupling.py:49 | rule1_dXdt |  | Sign of dI/dT is therefore elevation dependent."""
2026-05-23 | Simulators | tools/known_answer.py:544 | rule1_dXdt |  | fraction of a season where dE/dt > dM/dt -- the quantity the STRUCTURAL vs
2026-05-23 | Simulators | CLAUDE.md:314 | rule1_verb_first |  | verb-first axes (`conducts`, `switches`, `dissipates`,
2026-05-23 | Simulators | CLAUDE.md:5120 | rule1_verb_first |  | `BOUNDARY.md` D6, the **verb-first test** — *rewrite the main claim
2026-05-23 | Simulators | CLAUDE.md:5121 | rule1_verb_first |  | verb-first; if you must supply a bearer to make it grammatical it is
2026-05-23 | Simulators | CLAUDE.md:5140 | rule1_verb_first |  | **`VERB_CARRIES_IT` is not an option of the verb-first test** — all three of
2026-05-23 | Simulators | CLAUDE.md:5292 | rule1_verb_first |  | verb-first form** — verb leading, bearer dropped, operator implied — so
2026-05-23 | Simulators | CLAUDE.md:5298 | rule1_verb_first |  | entry, not the parser** — the repo's own verb-first stance arriving in the
2026-05-23 | Simulators | SYNTHESIS.md:341 | rule1_verb_first |  | substrate as a profile of verb-first axes — `conducts`, `switches`,
2026-05-23 | Simulators | SYNTHESIS.md:36 | rule1_verb_first |  | | `substrate-emergence/`            | material substrate profile (verb-first axes) | architecture-the-ground-wants: clock, topology, deficit routings, emergent senses |
2026-05-23 | Simulators | docs/FOLDER_NOTES.md:40 | rule1_verb_first |  | verb-first axes (`conducts`, `switches`, `dissipates`,
2026-05-23 | Simulators | encoding-selection/WORK_ORDER.md:121 | rule1_verb_first |  | (no obligatory tense, no articles, verb-first, subject-droppable);
2026-05-23 | Simulators | grounding-layers/experimental/holistic_field_state.py:50 | rule1_verb_first |  | reading: str                 # verb-first state, not a number-if-none-exists
2026-05-23 | Simulators | grounding-layers/inverse_knowledge_tree.py:40 | rule1_verb_first |  | yields: str                     # verb-first capability delivered
2026-05-23 | Simulators | nonidentity-census/BOUNDARY.md:146 | rule1_verb_first |  | ## D6 — the verb-first test
2026-05-23 | Simulators | nonidentity-census/BOUNDARY.md:155 | rule1_verb_first |  | > Rewrite the main claim verb-first. If you must supply a bearer to make it
2026-05-23 | Simulators | nonidentity-census/BOUNDARY.md:174 | rule1_verb_first |  | | claim | verb-first residue | completing it requires a noun? |
2026-05-23 | Simulators | nonidentity-census/FINDINGS.md:129 | rule1_verb_first |  | ### T1-5 — the verb-first test, run against the first instrument
2026-05-23 | Simulators | nonidentity-census/FINDINGS.md:137 | rule1_verb_first |  | D1/D3 instrument vs D6 verb-first test, n=12
2026-05-23 | Simulators | nonidentity-census/FINDINGS.md:204 | rule1_verb_first |  | ### T1-8 — `VERB_CARRIES_IT` is not an option of the verb-first test
2026-05-23 | Simulators | nonidentity-census/samples/t1_two_instruments.sample.txt:1 | rule1_verb_first |  | D1/D3 instrument vs D6 verb-first test, n=12
2026-05-23 | Simulators | nonidentity-census/samples/t1_verb_first_score.sample.txt:1 | rule1_verb_first |  | D6 verb-first, n=12   judge: model, in-session, 2026-08-23, no second reader
2026-05-23 | Simulators | nonidentity-census/t1_verb_first.py:3 | rule1_verb_first |  | T1, second instrument -- THE VERB-FIRST TEST (BOUNDARY.md D6).
2026-05-23 | Simulators | nonidentity-census/t1_verb_first.py:348 | rule1_verb_first |  | print("D1/D3 instrument vs D6 verb-first test, n=%d" % len(rows))
2026-05-23 | Simulators | nonidentity-census/t1_verb_first.py:447 | rule1_verb_first |  | print("D6 verb-first, n=%d   judge: %s\n" % (len(rows), JUDGE))
2026-05-23 | Simulators | nonidentity-census/t1_verb_first.py:7 | rule1_verb_first |  | Rewrite the main claim verb-first. If you must supply a bearer to make
2026-05-23 | Simulators | nonidentity-census/t6_window_declaration.py:20 | rule1_verb_first |  | reading      from D6, the verb-first test. BEARER_REQUIRED -> ENTITY,
2026-05-23 | Simulators | notes/FINDINGS_STUDY_WATCH.md:29 | rule1_verb_first |  | an instruction is already in verb-first form.** `count caveats issued per
2026-05-23 | Simulators | notes/FINDINGS_STUDY_WATCH.md:59 | rule1_verb_first |  | it is the repo's own verb-first stance (`substrate-emergence`'s verb-first
2026-05-23 | Simulators | notes/memory-export/files/calibration-gap-log.md:95 | rule1_verb_first |  | "dwells contemplating feelings-as-feelings." The verb-first requirement, in a 5th-century BCE
2026-05-23 | Simulators | notes/memory-export/files/energy-english.md:3 | rule1_verb_first |  | description: Constraint grammar formalizing verb-first relational English as compression over substrate-primary cognition.
2026-05-23 | Simulators | notes/memory-export/files/energy-english.md:8 | rule1_verb_first |  | Constraint grammar formalizing VERB-FIRST RELATIONAL ENGLISH as compression over
2026-05-23 | Simulators | notes/memory-export/files/identity-model-monoculture.md:45 | rule1_verb_first |  | Connects to [[energy-english]], which is verb-first by construction.
2026-05-23 | Simulators | notes/memory-export/files/repo-ecosystem.md:16 | rule1_verb_first |  | - **energy_english constraint grammar** — no moral labels in data structures, verb-first
2026-05-23 | Simulators | notes/study_watch.py:179 | rule1_verb_first |  | An instruction is ALREADY the verb-first residue: verb leading, bearer
2026-05-23 | Simulators | notes/study_watch.py:195 | rule1_verb_first |  | "why": "already verb-first; operator is the implied bearer"}
2026-05-23 | Simulators | notes/study_watch.py:201 | rule1_verb_first |  | "why": "verb-first after a leading marker"}
2026-05-23 | Simulators | notes/study_watch.py:206 | rule1_verb_first |  | "the entry: write the WOULD MEASURE verb-first.")}
2026-05-23 | Simulators | notes/study_watch.py:60 | rule1_verb_first |  | an INSTRUCTION is already in verb-first form. "count caveats
2026-05-23 | Simulators | notes/watch/README.md:54 | rule1_verb_first |  | | `notes` | the verb-first residue a reviewer reads to make the call |
2026-05-23 | Simulators | notes/watch/README.md:62 | rule1_verb_first |  | verb-first form** — verb leading, bearer dropped, operator implied — and
2026-05-23 | Simulators | notes/watch/README.md:70 | rule1_verb_first |  | MEASURE verb-first and this pipeline reads it as written.
2026-05-23 | Simulators | open-instrumentation-project/README.md:118 | rule1_verb_first |  | knowledge is a verb, and that the most resilient systems are the ones
2026-05-23 | Simulators | substrate-emergence/README.md:32 | rule1_verb_first |  | A substrate profile is a plain dict. Keys are verb-first axes, values
2026-05-23 | Simulators | substrate-emergence/substrate_emergence.py:16 | rule1_verb_first |  | #   A substrate profile is a plain dict. Keys are verb-first axes.
2026-05-23 | Simulators | substrate-emergence/substrate_emergence.py:50 | rule1_verb_first |  | """Turn each apparent deficit into where it routes. Verb-first."""
2026-05-23 | Simulators | uninstrumented/AUDIT_NOTES.md:2437 | rule1_verb_first |  | is accurate about what it is (a verb-first relational grammar) and the use is
2026-05-23 | Simulators | uninstrumented/AUDIT_NOTES.md:3167 | rule1_verb_first |  | the site of the substitution, and a verb-first grammar has no noun at that site
2026-05-23 | Simulators | uninstrumented/case_020_audit.py:436 | rule1_verb_first |  | citation is accurate about what it is (a verb-first relational grammar). The
2026-05-23 | Simulators | uninstrumented/case_021_audit.py:476 | rule1_verb_first |  | dual-sense noun is the site of the substitution; a verb-first grammar has no
2026-05-23 | Simulators | uninstrumented/cases/020attributedagencyarrangement.md:137 | rule1_verb_first |  | - `energy-english` — verb-first relational grammar exists for this; holding the
2026-05-23 | Simulators | uninstrumented/cases/021sensesubstitutionundeclaredaxis.md:139 | rule1_verb_first |  | - `energy-english` — verb-first relational grammar avoids the dual-sense noun, which is
2026-05-23 | Simulators | uninstrumented/samples/case_020_audit.sample.txt:292 | rule1_verb_first |  | citation is accurate about what it is (a verb-first relational grammar). The
2026-05-23 | Simulators | uninstrumented/samples/case_021_audit.sample.txt:350 | rule1_verb_first |  | dual-sense noun is the site of the substitution; a verb-first grammar has no
2026-05-23 | Simulators | encoding-selection/WORK_ORDER.md:45 | should_be_like_you |  | F7  reader's own        free-form; reader re-encodes it themselves
2026-05-23 | Simulators | failure-mode-register/WORK_ORDER_V2.md:865 | should_be_like_you |  | Provenance is A RECORD ABOUT A HOP. Every hop is therefore an opportunity to re-encode
2026-05-23 | Simulators | failure-mode-register/WORK_ORDER_V3.md:739 | should_be_like_you |  | Provenance is A RECORD ABOUT A HOP. Every hop is therefore an opportunity to re-encode
2026-05-23 | Simulators | failure-mode-register/WORK_ORDER_V4.md:810 | should_be_like_you |  | Provenance is A RECORD ABOUT A HOP. Every hop is therefore an opportunity to re-encode
2026-05-23 | Simulators | field-fabrication-guide/index.html:190 | should_be_like_you |  | <div class="step"><div class="step-num">1</div><div class="step-body"><div class="step-title">Mix nitrogen source with carbon</div><div class="step-desc">Use manure, urine, blood meal, or fish waste. 
2026-05-23 | Simulators | relational/related_work.md:65 | should_be_like_you |  | tracks the dominant framework in affective neuroscience:
2026-05-23 | Simulators | return-path/WORK_ORDER.md:29 | should_be_like_you |  | 2. SIGNAL — a report is re-encoded by whoever writes it, which reintroduces
2026-06-20 | substrate-phycom | legacy/reviews/02-code-audit.md:108 | absence_as_knowledge |  | - Half-open interval `[0, (steps-1)/steps)` — correct DFT convention but undocumented. No finite `steps` covers a complete period of the slowest oscillator.
2026-06-20 | substrate-phycom | legacy/reviews/02-code-audit.md:49 | absence_as_knowledge |  | **2.3 — No documentation on out-of-band agreement requirements**
2026-06-20 | substrate-phycom | legacy/reviews/02-code-audit.md:53 | absence_as_knowledge |  | **2.4 — No documentation on the `epoch` rollover strategy**
2026-06-20 | substrate-phycom | legacy/reviews/02-code-audit.md:54 | absence_as_knowledge |  | - `WIRE_EPOCH_MAX = 0xFFFF = 65535`. At a day-index cadence this is 179 years. At an hour-index cadence it rolls over in 7.5 years. There is no documentation advising callers which time unit to use or
2026-06-22 | gods-eye-view-fork | src/data/focusDeemphasis.js:115 | absence_as_knowledge |  | * grow an undocumented rendering contract.
2026-06-22 | gods-eye-view-fork | src/data/militaryAwareness.js:303 | absence_as_knowledge |  | //     status. That zero is an absence of evidence, not evidence of absence,
2026-06-22 | gods-eye-view-fork | vite.config.js:4952 | absence_as_knowledge |  | *   (undocumented but live; no browser CORS, hence this proxy). Up to ~24h
2026-06-22 | gods-eye-view-fork | README.md:276 | calibration_locus |  | | 📹 **CCTV Mesh** | ~800 public cameras projected *into* the 3D space — Austin · California (Caltrans) · London (TfL). Positions are published; poses are estimated priors **you calibrate by dragging a
2026-06-22 | gods-eye-view-fork | src/data/flowMatch.js:51 | rule1_dXdt |  | /** Bearing (degrees, 0 = north, clockwise) of a projected dx/dy vector. */
2026-06-22 | gods-eye-view-fork | src/data/localLayers.js:7 | rule1_dXdt |  | import damsUrl from './local_data/dams/dams.geojsonl?url';
2026-06-22 | gods-eye-view-fork | vite.config.js:7210 | rule1_dXdt |  | const payload = await fetchRegionalJson(`https://api.gdeltproject.org/api/v2/doc/doc?${params}`, {
2026-06-22 | gods-eye-view-fork | src/data/traffic.js:1542 | should_be_like_you |  | // Mono presets (NVG/FLIR/noir) discard hue — heat-lines re-encode in
2026-06-22 | gods-eye-view-fork | src/data/traffic.js:253 | should_be_like_you |  | * styling (`trafficPresetStyle.js`): NVG/FLIR/noir re-encode congestion in
2026-07-05 | Cross-Domain-Toolkit | multi_substrate_calibration/examples/thermal_substrate.py:5 | calibration_locus |  | reliability (from calibration against a reference) discounts that confidence into
2026-07-05 | Cross-Domain-Toolkit | cascade_regime_audit/examples/cusp_atlas.py:113 | rule1_dXdt |  | With a strong Allee effect, dN/dt = rN(N/A - 1)(1 - N/K) has an unstable
2026-07-05 | Cross-Domain-Toolkit | cascade_regime_audit/examples/cusp_atlas.py:149 | rule1_dXdt |  | Logistic stock under constant-quota harvest, dN/dt = rN(1 - N/K) - H, folds
2026-07-05 | Cross-Domain-Toolkit | cascade_regime_audit/examples/cusp_atlas.py:8 | rule1_dXdt |  | catastrophe's *normal form*, the point where the cubic dV/dx = x^3 - a*x - h
2026-07-05 | curly-octo-happiness | grounding/core/dormancy.py:522 | absence_as_knowledge |  | """Is this quiet a seed, a corpse, or an absence of evidence?"""
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1076 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:11 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1109 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:112 | calibration_locus |  | "reference_class": "crossref records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1144 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1177 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1225 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1258 | calibration_locus |  | "text": "On topic calibration and falsifiability of LLM agents, Digital Identity for Agentic Systems: Toward a Portable Authorization Standard for Autonomous Agents reports: Enterprise AI is shifting 
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1268 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1306 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:159 | calibration_locus |  | "reference_class": "crossref records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1597 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1619 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1656 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1682 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1706 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1750 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1780 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1823 | calibration_locus |  | "reference_class": "semantic_scholar records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:1866 | calibration_locus |  | "reference_class": "crossref records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:222 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:280 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:337 | calibration_locus |  | "reference_class": "crossref records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:398 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:462 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:516 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:570 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:629 | calibration_locus |  | "reference_class": "crossref records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:64 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:918 | calibration_locus |  | "reference_class": "arxiv records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | data/claim_tree.json:971 | calibration_locus |  | "reference_class": "crossref records on 'calibration and falsifiability of LLM agents'",
2026-07-05 | curly-octo-happiness | grounding/core/allostasis.py:143 | calibration_locus |  | whose calibration is itself unknown.
2026-07-05 | curly-octo-happiness | hypotheses/calibration-and-falsifiability-of-llm-agents.md:200 | calibration_locus |  | - [unfalsifiable] On topic calibration and falsifiability of LLM agents, Learning the Value Systems of Agents with Preference-based and Inverse Reinforcement Learning reports: Agreement Technologies r
2026-07-05 | curly-octo-happiness | hypotheses/calibration-and-falsifiability-of-llm-agents.md:37 | calibration_locus |  | - **On topic calibration and falsifiability of LLM agents, Digital Identity for Agentic Systems: Toward a Portable Authorization Standard for Autonomous Agents reports: Enterprise AI is shifting from 
2026-07-05 | curly-octo-happiness | unified_playground.py:512 | should_be_like_you |  | """Re-encode the prediction-error stream as sparse events (3.6).
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:112 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1264 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1273 | calibration_locus |  | "text": "On topic calibration and falsifiability of LLM agents, Qualified Cross-References as a Verification Method: The Normative Environment of the EU AI Act reports: Legal cross-references are comm
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1283 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1302 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:131 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1321 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1340 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1359 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1378 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1397 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:14 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1416 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1435 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1457 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1476 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1498 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:150 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:169 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:188 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1938 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1957 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1976 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:1995 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2017 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2036 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2055 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:207 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2074 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2093 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:226 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:245 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2561 | calibration_locus |  | "text": "On topic calibration and falsifiability of LLM agents, VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning reports: Native visual reasoning treats visual generation as the m
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2574 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2593 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2612 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2631 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:264 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2650 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2669 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2688 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:2735 | calibration_locus |  | "text": "On topic hidden variable detection / causal discovery from residuals, Torsion balances as operational probes of semiclassical gravity: Matched-filter bounds, torque-diffusion constraints, and
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:283 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:302 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3185 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3204 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:321 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3223 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3242 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3261 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3280 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3299 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3318 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3337 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3356 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:340 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:359 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:36 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:378 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3932 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3954 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:397 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3973 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:3992 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4014 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4033 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4052 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4075 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4094 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:416 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / crossref findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4781 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4800 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4819 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4838 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4857 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4879 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4898 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4917 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:4936 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:55 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5703 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5722 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5741 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5760 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5779 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5798 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5817 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5839 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5861 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5880 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / semantic_scholar findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5899 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5921 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5940 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:5959 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:74 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/claim_tree.json:93 | calibration_locus |  | "reference_class": "calibration and falsifiability of LLM agents / arxiv findings",
2026-08-08 | simulation | hypothesis-engine/data/episodic_memory.json:164 | calibration_locus |  | {"event": "finding_logged", "id": "abbde7f6885107abb92cc5b2", "topic": "calibration and falsifiability of LLM agents", "text": "VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning Na
2026-08-08 | simulation | hypothesis-engine/data/episodic_memory.json:166 | calibration_locus |  | {"event": "finding_logged", "id": "1c0004833f4aec91cf1f79b3", "topic": "calibration and falsifiability of LLM agents", "text": "RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video 
2026-08-08 | simulation | hypothesis-engine/data/episodic_memory.json:175 | calibration_locus |  | {"event": "finding_logged", "id": "824ab7151b93c5cb59048032", "topic": "hidden variable detection / causal discovery from residuals", "text": "Torsion balances as operational probes of semiclassical g
2026-08-08 | simulation | hypothesis-engine/data/episodic_memory.json:7 | calibration_locus |  | {"event": "finding_logged", "id": "a0c6da4c536c012509c81520", "topic": "calibration and falsifiability of LLM agents", "text": "Enhancing Automatic Text Evaluation through Calibration-Aware Large Lang
2026-08-08 | simulation | hypothesis-engine/data/episodic_memory.json:89 | calibration_locus |  | {"event": "finding_logged", "id": "67f9f516a3c5c8b88c659d34", "topic": "calibration and falsifiability of LLM agents", "text": "Qualified Cross-References as a Verification Method: The Normative Envir
2026-08-08 | simulation | hypothesis-engine/hypotheses/calibration-and-falsifiability-of-llm-agents.md:127 | calibration_locus |  | - [escape-hatch] On topic calibration and falsifiability of LLM agents, RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video Editing reports: Recent advances
2026-08-08 | simulation | hypothesis-engine/hypotheses/calibration-and-falsifiability-of-llm-agents.md:30 | calibration_locus |  | - (0.83) On topic calibration and falsifiability of LLM agents, Qualified Cross-References as a Verification Method: The Normative Environment of the EU AI Act reports: Legal cross-references are comm
2026-08-08 | simulation | hypothesis-engine/hypotheses/calibration-and-falsifiability-of-llm-agents.md:74 | calibration_locus |  | - (0.80) On topic calibration and falsifiability of LLM agents, VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning reports: Native visual reasoning treats visual generation as the m
2026-08-08 | simulation | research/CROSS_DOMAIN_TOOLKIT_PROPOSALS.md:24 | calibration_locus |  | **Why:** Eight atlas domains instantiate the existing spinodal h* = 2/√27 *directly* (structural buckling, vdW phase transition, Semenov runaway, ice-albedo/AMOC, Allee collapse, grid nose curve, Grif
2026-08-08 | simulation | research/HARDWARE_INTEGRATION_PLAN.md:60 | calibration_locus |  | **I12. Port drift_gate + scope fields to root CLAIM_TABLE.json** — extend claim schema with scope/reference_class (matching curly-octo-happiness), wire the fab verdict ladder into DependencyTree propa
2026-08-08 | simulation | research/HARDWARE_INTEGRATION_PLAN.md:65 | calibration_locus |  | The hardware-repurposing tables (diode→conductor, drift→sensor) extend naturally: I4's Pico-DAQ is itself a repurposed MCU; I5's rtl_433 scavenges neighbors' sensors as free telemetry; I6's LCR-T4 sor
2026-08-08 | simulation | research/TERMINOLOGY_MAP.md:52 | calibration_locus |  | > A stdlib-only toolkit for three classical problems: (1) falsifiability-disciplined claim tracking with tamper-evident provenance; (2) multi-sensor fusion with calibrated confidence, role typing, and
2026-08-08 | simulation | research/integration/EXPLORE_AND_EXPERIMENT.md:12 | rule1_dXdt |  | **Q2. Is integral feedback the universal calibration answer?** Bacterial chemotaxis proves topology-not-tuning gives robust perfect adaptation (Barkai–Leibler/Yi). Which of the ecosystem's calibration
2026-08-08 | simulation | research/integration/EXPLORE_AND_EXPERIMENT.md:37 | rule1_dXdt |  | | E1 | **Integral-feedback calibrator**: replace fitted offset in a CDT substrate example with dm/dt = g(a−a₀) loop; sweep parameters 10× | ~40 LOC | topology-based drift rejection is tuning-free / no
2026-08-08 | simulation | research/notes/07_MCPM_collapse_research.md:68 | rule1_dXdt |  | | P1 | Rate-term: track dM/dt and forcing rate; R-tipping flag when forcing > A | days |
2026-08-08 | simulation | research/notes/07_MCPM_collapse_research.md:71 | rule1_dXdt |  | | P2 | EROEI/ROC layer formalizing the value denominator with Tainter marginal-collapse detector (dM/dcost < 0) | 1 wk |
2026-08-08 | simulation | research/notes/08_cross_domain_toolkit.md:112 | rule1_dXdt | PATH? | - Tainter: collapse when dB/dC ≤ 0; proxy B(C) = a ln C − bC, optimum C* = a/b. EROEI = E_out/E_in; viability ≳ 3:1, industrial ≳ 10:1 (Hall).
2026-08-08 | simulation | research/notes/08_cross_domain_toolkit.md:136 | rule1_dXdt |  | - SOM: $dS/dt = I - kS$, S* = I/k, critical < ~2%. Maas–Hoffman yield: $Y_r = 100 - b(EC_e - a)$ for EC_e > a (wheat a≈6.0, b≈7.1; beans a≈1.0) — direct threshold detector on cheap EC data.
2026-08-08 | simulation | research/notes/08_cross_domain_toolkit.md:97 | rule1_dXdt |  | - Basquin $N_f = CS^{-m}$; Miner $D = \sum n_i/N_i$, failure D = 1; Weibull $R(t) = e^{-(t/\eta)^\beta}$ (β<1 infant, ≈1 random, >1 wear-out); Paris crack law $da/dN = C(\Delta K)^m$.
2026-08-08 | simulation | research/notes/11_meta_structures_consciousness_bio_intelligence.md:101 | rule1_dXdt |  | | **Physarum** | flow-adaptive graph optimization; stigmergic external memory | **Tero law: dD/dt = \|Q\|^μ − γD**, Q ∝ D·Δp (Science 2010, Tokyo rail) | [E] |
2026-08-08 | simulation | research/notes/11_meta_structures_consciousness_bio_intelligence.md:104 | rule1_dXdt |  | | **Bacterial chemotaxis** | **integral feedback = robust perfect adaptation** (topology, not tuning) | dm/dt = g(a − a₀); Barkai–Leibler 1997; Yi et al. PNAS 2000 (integral feedback is the *only* lin
2026-08-08 | simulation | research/notes/11_meta_structures_consciousness_bio_intelligence.md:105 | rule1_dXdt |  | | **Quorum sensing** | analog population comparator, bistable switch | dA/dt = k₀N − γA; Hill output V·Aⁿ/(Kⁿ+Aⁿ) | [E] |
2026-08-08 | simulation | research/notes/12_seven_questions_shape.md:21 | rule1_dXdt |  | **Setup**: sensor y = g·x + drift(t) + noise; drift = random walk; gain g perturbed ×2–×10 mid-run. Fitted-offset (rolling-mean subtraction) vs integral-feedback loop dm/dt = ki·(y−m−s).
2026-08-08 | simulation | research/notes/13_geometric_manifold_combinations.md:20 | rule1_dXdt |  | **Declared weaknesses** (their own docs): ISS proof pending; Lyapunov certificate dV/dt≤0 unproven; phase labels "heuristic, not certified"; "this codebase is entirely theoretical and structurally iso
2026-08-08 | simulation | sims/_unretrofitted/shape_csd_probes.py:15 | rule1_dXdt |  | # bistable strut: stable at l1=1.2, l2=1.8; quartic energy, force = -dE/dl
2026-08-08 | simulation | sims/_unretrofitted/shape_csd_probes.py:18 | rule1_dXdt |  | # dE/dl = 2a(l-l1)(l-l2)(2l-l1-l2); stable equilibria at l1,l2
2026-08-08 | simulation | sims/explore.py:73 | rule1_dXdt |  | "B2 thermodynamics": "van der Waals spinodal from (dP/dV)_T = 0; coexistence is literally a cusp",
2026-08-08 | simulation | sims/fractal_basin/original_fractal_basin_sim.py:6 | rule1_dXdt |  | def F(x):  # force = -dE/dx, E = prod (x-c)^2 ; use numerical derivative
2026-08-08 | simulation | sims/shape_csd/original_shape_csd_probes.py:15 | rule1_dXdt |  | # bistable strut: stable at l1=1.2, l2=1.8; quartic energy, force = -dE/dl
2026-08-08 | simulation | sims/shape_csd/original_shape_csd_probes.py:18 | rule1_dXdt |  | # dE/dl = 2a(l-l1)(l-l2)(2l-l1-l2); stable equilibria at l1,l2
2026-08-08 | simulation | sims/snap_information/FINDINGS.md:34 | rule1_dXdt |  | du/dt = v
2026-08-08 | simulation | sims/snap_information/FINDINGS.md:35 | rule1_dXdt |  | dv/dt = F(u) - γv          initial condition  u₀ = 1.2,  v₀ = jitter
2026-08-12 | interdisciplinary-studies | PRACTITIONER_EPISTEMOLOGY.md:264 | calibration_locus |  | Standardized instrumentation is a form of **institutional trust** — we trust gauges because they are calibrated, certified, and standardized. The practitioner's distrust of gauges under variable condi
2026-08-12 | interdisciplinary-studies | PRACTITIONER_EPISTEMOLOGY.md:33 | calibration_locus |  | 5. **No mention of tools, instruments, or measurement devices.** The body IS the instrument. This is not a metaphor. The practitioner's body is calibrated to the machine through repeated exposure. Thi
2026-08-12 | interdisciplinary-studies | THERMODYNAMICS.md:20 | calibration_locus |  | **Practitioner's definition:** Entropy is all around us. It is the environment itself. Every teacher — animal, plant, river, rock, star, machine — demonstrates entropy in a different modality. The mor
2026-08-12 | interdisciplinary-studies | THERMODYNAMICS.md:92 | calibration_locus |  | The practitioner's core concept — calibration — is itself a thermodynamic process.
2026-08-12 | interdisciplinary-studies | collisions.js:298 | calibration_locus |  | scoring: "Calibrated, certified, standardized. The gauge is authoritative; subjective report is not."
2026-08-14 | tool-off-metrology | experiments.md:987 | absence_as_knowledge |  | "undocumented rather than absent" is much weaker than a thin
2026-08-14 | tool-off-metrology | plan.md:22 | absence_as_knowledge |  | practice, an elder operator, an undocumented method — is on a clock
2026-08-14 | tool-off-metrology | unnamed-instruments.md:617 | absence_as_knowledge |  | The prior framing here ("calibration content undocumented rather than
2026-08-14 | tool-off-metrology | unnamed-instruments.md:626 | absence_as_knowledge |  | undocumented." Rather — *meanings are locally specific and the
2026-08-14 | tool-off-metrology | experiments.md:42 | instrument_to_world |  | threshold difference   the instrument itself performs differently
2026-08-21 | shape-index | AUDIT_CONTRACT.md:23 | author_characterization | CLASS_UNSET; PROHIBITION? | - No "about the author", working-style, or audience sections. Ever. Strip
2026-08-21 | shape-index | README.md:62 | calibration_locus |  | The repository cross-references `uninstrumented/coupling_audit` and the cross-model calibration toolkit as reading locations rather than claiming that those materials have already been incorporated.
2026-08-21 | shape-index | shape_index/entries.py:455 | calibration_locus |  | "matrix because measurements sharing a calibration standard "
2026-09-06 | framework-instruments | docs/specifications/model-deprecation-backcast.md:122 | absence_as_knowledge |  | PREDICTION: populations whose ontology is not in the corpus
2026-09-06 | framework-instruments | docs/specifications/model-deprecation-backcast.md:73 | absence_as_knowledge |  | RECORD: none. Undocumented in release notes, undateable
2026-09-06 | framework-instruments | docs/specifications/model-deprecation-backcast.md:169 | author_characterization | CLASS_UNSET; PROHIBITION? | No section about the author. No working-style or author-profile
2026-09-06 | framework-instruments | instruments/telemetry-vocabulary/README.md:5 | calibration_locus |  | This CC0 artifact names a recurring output failure in human–AI interaction and provides a reproduction protocol that can be run through an ordinary chat interface. The failure occurs when a request fo
2026-09-06 | framework-instruments | docs/specifications/cycle-ledger-and-rate-gap.md:122 | rule1_dXdt |  | dE/dt      environment state-change rate
2026-09-06 | framework-instruments | docs/specifications/cycle-ledger-and-rate-gap.md:123 | rule1_dXdt |  | dM/dt      achieved record refresh rate
2026-09-06 | framework-instruments | docs/specifications/cycle-ledger-and-rate-gap.md:128 | rule1_dXdt |  | dE/dt > dM/dt sustained, with a nonzero unrecorded set
2026-09-06 | framework-instruments | docs/specifications/cycle-ledger-and-rate-gap.md:130 | rule1_dXdt |  | dM/dt >= dE/dt with unrecorded set empty
2026-09-06 | framework-instruments | docs/specifications/routing-data-layer-marker.md:154 | rule1_dXdt |  | dE/dt   environment state-change rate
2026-09-06 | framework-instruments | docs/specifications/routing-data-layer-marker.md:159 | rule1_dXdt |  | dM/dt   sustainable model refresh rate
2026-09-06 | framework-instruments | docs/specifications/routing-data-layer-marker.md:163 | rule1_dXdt |  | Where dE/dt > dM/dt sustained, the null is STRUCTURAL, not
2026-09-19 | chain-position-detectability | research/wo-2/inverse-case-search.md:43 | absence_as_knowledge |  | Accordingly, treating MFOQA as a positive case would overstate the evidence. It is neither an undocumented generic recommendation nor a single physical control; it is a close **partial** match whose m
2026-09-19 | chain-position-detectability | research/wo-2/inverse-case-search.md:75 | absence_as_knowledge |  | | Accident investigations and recommendation records | NTSB investigation reports and CAROL/recommendation material; U.S. Chemical Safety and Hazard Investigation Board recommendation materials; UK ac
2026-09-19 | chain-position-detectability | research/wo-2/pilot-analysis.md:130 | absence_as_knowledge |  | The validated WO-2 pilot yields **one clear supporting case, seven indeterminate cases, and no affirmative non-supporting case**. Givaudan demonstrates that the proposed structure can be observed in a
2026-09-19 | chain-position-detectability | AUDIT_NOTES.md:258 | author_characterization | CLASS_UNSET; PROHIBITION? | work orders    no author line; one operator name, once (WO-5: "Kavik, stated before the run")
2026-09-19 | chain-position-detectability | work-orders/WO-5-hop-distance-and-pre-entry-loss.md:176 | author_characterization | CLASS_UNSET | PREDICTED DIRECTION (Kavik, stated before the run): reporting rate changes.
2026-09-19 | chain-position-detectability | research/wo-3/evidence/candidate-black-hole.md:43 | calibration_locus |  | | Energy and momentum | **OBSERVED:** calibrated detector strain. **DERIVED:** gravitational-wave interpretation, source association, outward propagation, and crossing of \(B_{1\,ly}\), conditional on
2026-09-19 | chain-position-detectability | work-orders/WO-6-assessor-assessed-coupling.md:249 | calibration_locus |  | calibration check on the instrument itself.
2026-09-19 | chain-position-detectability | research/wo-5/source-candidates.json:4723 | contort | OTHER_SENSE? | "title": "Soil biotic and abiotic effects on seedling growth exhibit context‐dependent interactions: evidence from a multi‐country experiment on <i>Pinus contorta</i> invasion",
2026-09-19 | chain-position-detectability | work-orders/WO-6-assessor-assessed-coupling.md:249 | instrument_to_world |  | calibration check on the instrument itself.
2026-09-20 | decision-aperture | discriminate.py:16 | instrument_to_world |  | # the instrument itself, the same posture as the move-set
2026-09-20 | vibe-code-audit | situation_help.py:38 | absence_as_knowledge |  | "undocumented_or_phantom_tools": {
