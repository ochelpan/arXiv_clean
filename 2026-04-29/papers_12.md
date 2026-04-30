# Daily arXiv Report

[← Index](index.md)

[← Previous](papers_11.md)
[Next →](papers_13.md)

## Papers 221–240


<a id="paper-2604.25125"></a>


### [Identifying strong correlation using only the Kohn-Sham density of one-electron states](http://arxiv.org/abs/2604.25125v1)

**Authors:** Daniel D. Rivera, Gustavo M. Dalpian, John P. Perdew

**Type:** theory · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25125v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25125_figures/2604.25125_fig1.jpg" width="500"><br>

<sub>FIG. 1. Spin symmetry breaking effect on the density of states. The green shaded region marks the vicinity of the Fermi level. Positive/red (negative/blue) density of states correspond to spin up (down). The figure illustrates that symmetric states exhibit a larger number of degenerate elec- tronic states near the Fermi level. Symmetry breaking reduces the number of quasi-degenerate states in this region, thereby reducing the effective impact of the missing electron–electron interactions at the non-interacting level.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25125_figures/2604.25125_fig2.jpg" width="500"><br>

<sub>FIG. 3. Densities of states for (a) symmetric (nonmagnetic) and (b) symmetry-broken (antiferromagnetic) NiO. The den- sity of states is plotted upward for spin ↑and downward for spin ↓.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25125_figures/2604.25125_fig3.jpg" width="500"><br>

<sub>FIG. 2. Densities of states for (a) symmetric (nonmagnetic) and (b) symmetry-broken (ferromagnetic) Fe. The density of states is plotted upward for spin ↑and downward for spin ↓.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25125_figures/2604.25125_fig4.jpg" width="500"><br>

<sub>FIG. 4. Density of states for symmetric (nonmagnetic) Cu.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25125_figures/2604.25125_fig5.jpg" width="500"><br>

<sub>FIG. 5. ∆E vs Γ plot. Green (red) region is for strongly (normally) correlated system.</sub>

</details>

**Main problem.**

Developing a practical, computable indicator to identify strongly correlated electronic systems using only the Kohn-Sham density of one-electron states.

**Main result.**

The authors introduce a correlation parameter (Gamma) based on the density of states at the Fermi level that successfully distinguishes between normally correlated and strongly correlated regimes.

**Method.**

Spin Density Functional Theory (spin-DFT) using the r2SCAN meta-GGA functional within the VASP/PAW framework, comparing symmetric and symmetry-broken configurations.

**Summary.**

This paper proposes a new way to identify strongly correlated materials without needing expensive beyond-DFT methods like DFT+U. By looking at the density of states in a standard Kohn-Sham calculation, the authors show that a specific parameter (Gamma) can predict whether a system will require explicit treatment of electron correlation. The method works by observing how spin symmetry breaking lifts degeneracies, effectively transforming a strongly correlated system into a normally correlated one. This provides a practical diagnostic tool for researchers to determine the reliability of standard DFT for new materials.

<details><summary>Detailed structure</summary>

**Model / system.**

A diverse set of electronic systems including transition metals (Ni, Fe, Co, Pd, Cu, Ag, Zn, Cd), oxides (NiO, VO2), and rare-earth compounds (EuB6, SmB6, Gd).

**Key observables.**

Correlation parameter (Gamma), energy difference between symmetric and symmetry-broken states (Delta E), and the ratio of density of states at the Fermi level.

**Important parameters / regimes.**

Gamma (ratio of KS DOS to uniform electron gas DOS), Gaussian-smeared Gamma_g, and the energy width (delta) for integrating states around the Fermi level.

**Assumptions / limitations.**

The energy difference between symmetric and symmetry-broken states serves as a proxy for correlation energy; the approach is subject to standard DFT limitations like self-interaction error.

**Figures summary.**

Figure 1 shows how spin symmetry breaking reduces near-degenerate states; Figure 2 and 3 illustrate the reduction of DOS at the Fermi level and band-gap opening in Fe and NiO, respectively; Supplemental figures show DOS changes for various other materials.

**Paper structure.**

The paper introduces the problem of identifying strong correlation, proposes the Gamma parameter, tests it against a wide range of metals and oxides, validates it using a Gaussian-smeared version (Gamma_g), and compares the results to the Stoner criterion and Hubbard model.

</details>

<details><summary>Abstract</summary>

Strongly correlated systems have long been a central and highly non-trivial topic in condensed matter physics. At the non-interacting level, strong correlation can be associated with powerful (near) degeneracies between occupied and unoccupied states, which leads to a high density of states near the Fermi level in metallic configurations. Such regimes are commonly treated with beyond-density functional theory (DFT) approaches, such as DFT+U or DFT+DMFT while maintaining symmetric configurations. Here, we explore the hypothesis that symmetry breaking in the Kohn-Sham (KS) non-interacting system can qualitatively account for the energetic effects of strong correlation in the corresponding interacting system within standard DFT. By lifting near-degeneracies around the Fermi level, symmetry breaking diminishes the potential correlation effects, reducing the need for an explicit treatment of electron correlation, transforming an otherwise strongly correlated symmetric configuration into a normally correlated one, thus avoiding the need for interacting methods beyond DFT. This naturally connects nonmagnetic to magnetic states. We apply this idea to both strongly and normally correlated metals and observe that spin symmetry breaking leads to a pronounced reduction of the density of states at the Fermi level and a significant lowering of the total energy in strongly correlated cases. To describe the degree of correlation that the interacting system would have relative to the KS state, we introduce a correlation parameter ($Γ$), defined as the ratio between the Kohn-Sham density of one-electron states at the Fermi level and that of a corresponding uniform electron gas. This parameter distinguishes strongly correlated systems, which would require explicit treatment, from normally correlated ones, which do not.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25094"></a>


### [INJEQT: Improved Magic-State Injection Protocol for Fault-Tolerant Quantum Extractor Architectures](http://arxiv.org/abs/2604.25094v1)

**Authors:** Sayam Sethi, Sahil Khan, Aditi Awasthi, Abhinav Anand, Jonathan Mark Baker

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25094v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25094_figures/2604.25094_fig1.jpg" width="500"><br>

<sub>Fig. 1: Overview of magic state injection techniques. (a) Baseline standard injection: Represented by the Tour de Gross architecture, which relies on multiple high-error inter-module operations. (b) Surface code Rz-factory: Illustration of the Clifford+T decomposition of the Rz-state and the synthesis of an Rz-factory within the surface code using multiple |T⟩- factories. (c) Proposed qLDPC injection: Our method injects the prepared Rz-state into the qLDPC code, utilizing a single inter-module operation and fault-tolerant lattice surgery operations on surface code. (d) Time-efficient injection (INJEQT): Simultaneous preparation of multiple Rz-states required for post-injection corrections,...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25094_figures/2604.25094_fig2.jpg" width="500"><br>

<sub>Fig. 2: The two magic-state injection techniques considered in this work. |m⟩is the magic state being injected which can be either of T |+⟩or Rz(θ) |+⟩depending on the factory choice.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25094_figures/2604.25094_fig3.jpg" width="500"><br>

<sub>Fig. 3: Illustration of circuits across different abstraction layers. (a) Standard Circuit Model illustrating single and two- qubit unitary gates followed by measurements. (b) Pauli- Based Computing Model representing the computation as a sequence of Clifford and non-Clifford measurements. (c) Tour de Gross ISA, showing the modular instruction set architecture including In-module, Inter-module measurement and magic state preparation. For further details on the exact compilation process, see Ref. [14] and Ref. [31].</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25094_figures/2604.25094_fig4.jpg" width="500"><br>

<sub>Fig. 4: Fraction of the total program infidelity (error) that comes from Rz injections across all benchmarks. INJEQT reduces the error contribution from Rz for all factory types.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25094_figures/2604.25094_fig5.jpg" width="500"><br>

<sub>Fig. 5: Illustration of magic state injection techniques within the Tour de Gross (TDG) ISA. (a) Magic state preparation represented as a primitive within the TDG instruction set architecture. (b) Direct injection of an Rz magic state sourced from a dedicated Rz-factory, followed by necessary feed- forward corrections. (c) Sequential injection of magic states as a series of T-gates from a T-factory to realize non-Clifford rotations, including subsequent adaptive Clifford correction.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25094_figures/2604.25094_fig6.jpg" width="500"><br>

<sub>Fig. 6: Execution of the 2-level INJEQT factory where we perform multiple sequential injections onto the auxiliary code. Each injection can be done either via lattice surgery or transversal CNOT (Figure 2). Once the Rz(θ) state is prepared in this auxiliary code, it is then injected onto the extractor module via an inter-module measurement.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25094_figures/2604.25094_fig7.jpg" width="500"><br>

<sub>Fig. 7: INJEQT pre-fetching technique using R copies of the 2-level factories. All R factories begin preparing different Rz(θi = 2i−1θ) states. Once the Rz(θ) state completes preparation in F1, it is injected onto the extractor module. If the measurement result indicates that a correction is required, then the already prepared Rz(2θ) state is injected, and so on. Simultaneously, F1 begins preparing the next un-prepared state, i.e., the Rz(2R+1θ) state. The execution may stall if the preparation time for F1 exceeds the time taken to inject the previous R states.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25094_figures/2604.25094_fig8.jpg" width="500"><br>

<sub>Fig. 8: Improvements gained by INJEQT∗over TDG across different metrics for the entire benchmark suite for the distillation factory. We also report the mean improvement at the end.</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25094_figures/2604.25094_fig9.jpg" width="500"><br>

<sub>Fig. 9: Improvements gained by INJEQT∗over TDG across different metrics for the entire benchmark suite for the cultivation factory. We also report the mean improvement at the end.</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25094_figures/2604.25094_fig10.jpg" width="500"><br>

<sub>Fig. 10: Improvements gained by INJEQT∗over TDG across different metrics for the entire benchmark suite for the STAR factory. We use the better of distillation or cultivation for the corresponding TDG metric. We also report the mean improvement at the end.</sub>

</details>

**Main problem.**

In near-term fault-tolerant quantum computing (FTQC) extractor architectures, the 'synthillation' process (combining T-state preparation and injection) is the primary source of error, specifically due to expensive and error-prone inter-module measurements.

**Main result.**

The proposed INJEQT protocol reduces overall error rates by up to 22x and improves wall-clock time by up to 13x by using an auxiliary code to synthesize Rz states with fewer inter-module measurements.

**Method.**

The authors propose a 2-factory design that uses an auxiliary code (like the surface code) to synthesize Rz(theta) states, combined with a pre-fetching strategy to prepare states in parallel to mitigate latency.

**Summary.**

This paper addresses the critical error bottleneck in fault-tolerant quantum computing architectures that rely on 'extractor' modules. By introducing the INJEQT protocol, the authors demonstrate a way to synthesize rotation states in an auxiliary code to minimize the most error-prone inter-module measurements. Their approach significantly reduces both the error budget and the execution time of quantum programs. The results show substantial improvements in efficiency and robustness across different quantum error correction codes and hardware models.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on extractor-based architectures using qLDPC codes (such as the Gross code) and evaluates performance using Pauli-Based Computing (PBC) models, including lattice surgery and transversal CNOT-based injection.

**Key observables.**

Total program error rate, wall-clock time, physical qubit count, and space-time cost.

**Important parameters / regimes.**

Logical error rates, code distances (d), number of INJEQT factories (R), and precision scales (epsilon_synth) ranging from 10^-8 to 10^-10.

**Assumptions / limitations.**

Assumes the validity of the extractor-based architecture and specific error profiles for inter-module measurements; neglects trivial operations like syndrome extraction due to negligible error contribution.

**Figures summary.**

Figure 1 compares four injection techniques; Figure 2 illustrates two injection techniques; Figure 6 shows the 2-level INJEQT factory process; Figure 7 shows the pre-fetching technique; Figures 8-10 plot improvements in error, time, and space-time metrics for various factory types (Distillation, Cultivation, STAR).

**Paper structure.**

The paper identifies the bottleneck in FTQC architectures, introduces the INJEQT protocol and pre-fetching strategy, provides a theoretical derivation for Rz injection efficiency, evaluates the protocol across various factory types and injection models, and concludes with a robustness analysis.

</details>

<details><summary>Abstract</summary>

Near-term FTQC system designs are constrained by limited error budgets and largely sequential execution of non-Clifford gates. As a result, reducing the number of the most-error prone instructions becomes critical for successful program execution. In this work, we study the extractor architecture, a recently proposed FTQC design that enables universal quantum computation on spatially-efficient QEC codes such as the BB code family. In these architectures, over $90\%$ of the total program error arises from the synthillation process, which involves $\lvert T\rangle$-state preparation and injection to implement non-Clifford gates. We observe that standard Rz synthillation requires multiple sequential $\lvert T\rangle$-state injections, each incurring an inter-module measurements, the most expensive instruction in the architecture, which cumulatively dominate the overall error budget.   To address this bottleneck, we propose INJEQT, a $2$-factory design that uses an auxiliary code capable of synthesizing $Rz(θ)$ states with lower error rates. These states are then injected into the extractor modules using only a constant number of inter-module measurements. This approach reduces overall error rates by up to $22\times$. We further reduce the time overhead by a pre-fetching strategy that prepares the Rz states and their correction states in parallel. This approach improves the wall-clock time by up to $13\times$ and reduces the space-time cost by up to $7.2\times$, for an optimal choice of the number of INJEQT factories for each metric. We evaluate INJEQT for multiple state preparation techniques such as distillation, cultivation and STAR, and model the execution times for both lattice surgery-based and transversal CNOT based injections. Our results demonstrate that INJEQT is robust across factory choices and device technologies, enabling more efficient architectural designs for FTQC.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25365"></a>


### [Intrinsic magnetotransport and orientation dependent topological Hall effect in EuAuBi](http://arxiv.org/abs/2604.25365v1)

**Authors:** Lipika, Sneh, Shobha Singh, Ralf Koban, Walter Schnelle, Kaustuv Manna

**Type:** experiment · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25365v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25365_figures/2604.25365_fig1.jpg" width="500"><br>

<sub>FIG. 1. (a) Crystal structure of EuAuBi, the blue, pink, and brown represents Eu,Bi, and Au atoms respectively. The hexagonal shaped crystal (grown using Bi flux) of approxi- mately 2mm is shown (b) X-ray diffraction θ - 2θ plot (in logarithmic scale) of EuAuBi crystal grown using Bi flux, the primary peaks corresponds to the (001) planes of EuAuBi and the peaks indicated by red asterisk corresponds to the Au2Bi impurity phase formed in the crystal, Temperature-dependent (c) resistivity, and (d) magnetization in the presence of dif- ferent magnetic fields.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25365_figures/2604.25365_fig2.jpg" width="500"><br>

<sub>FIG. 2. (a) The as-grown rod-shaped crystals (grown using Pb flux) of approximately 2-3 mm are obtained with hexagonal cross-section area, (b) the Laue x-rays diffraction pattern of the crystal, (c) simulated pattern of the laue diffraction matches with the (1-10) plane, (d) the θ - 2θ XRD diffraction pattern shows the (h00) plane of the crystal indicating the crystal is c-oriented, (e) Temperature-dependent resistivity of EuAuBi crystal grown using Pb flux, the drop at 7 K is due to Pb flux [26] that is present over the crystal surface. The inset shows the temperature-dependent resistance of the same crystal measured up to 300 mK. (f) The temperature-dependent magnetization in the presence...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25365_figures/2604.25365_fig3.jpg" width="500"><br>

<sub>FIG. 3. (a) Zero-field cooling (ZFC) and Field-cooled warming (FCW) magnetization curves in the presence of 0.1 T magnetic field applied in-plane of the crystal. (b) Field-dependent magnetization M (B) at different temperatures for B ⊥c. The zoomed in parts of the anomalies are shown in the insets. (c) Temperature-dependent resistivity in the absence of magnetic field for I ∥z is depicted in black color along with the fitting (by red color) obtained using the Eq. 1 in temperature range 100 - 300 K. (d) Field-dependent resistivity ρzz at different temperatures for B ⊥c.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25365_figures/2604.25365_fig4.jpg" width="500"><br>

<sub>FIG. 4. (a) Field-dependent Hall signal ρyz at different temperatures for I ∥z, V ∥y, and B ∥x, (b) Fitting of ρyz using ρO yz + ρA yz at T = 2.5 K. Inset shows the topological Hall effect signal extracted at T = 2.5 K (c) Topological Hall signal, ρT yz extracted from the ρyz by subtracting ρyz O and ρyz A at different temperatures.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25365_figures/2604.25365_fig5.jpg" width="500"><br>

<sub>FIG. 5. (a) Black curve is the experimental data of zero field temperature-dependent specific heat Cp (T) and red curve represents the fitting of experimental curve using con- tributions from electronic and phononic (Debye and Ein- stein) specific heats. (b) Temperature-dependent plot of mag- netic part of specific heat (Cmag/T) and entropy (Smag. (c) Temperature-dependent specific heat at different magnetic fields.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25365_figures/2604.25365_fig6.jpg" width="500"><br>

<sub>Fig. 5(b) presents the temperature dependence of Cmag/T and Smag. The magnetic entropy exhibits a rapid increase up to TN, followed by a gradual rise until it saturates at higher temperature. The entropy saturates at approximately 15.5 J mol−1 K−1, which is close to the expected magnetic entropy Rln(2S+1) = Rln8 J mol−1 K−1 for Eu2+ (S = 7/2). Notably, the magentic entropy is recovered around 25 K, while the TN ∼4.8 K, indicating the presence of short-range correlation above the long-range ordering temperature (TN). This behaviour is similarly observed in other Eu based compounds like EuMg2Sb2, EuCo2P2, EuMg2Bi2, etc [38–40]. The temperature dependence of Cp measured under different applied...</sub>

</details>

**Main problem.**

The study aims to investigate the intrinsic physical properties of the magnetic topological semimetal EuAuBi, specifically determining the origin of previously reported superconductivity and uncovering orientation-dependent topological transport signatures.

**Main result.**

The researchers demonstrate that superconductivity in EuAuBi is extrinsic (due to Au2Bi impurities) and identify a new topological Hall effect (THE) signal that emerges in c-axis oriented crystals during metamagnetic transitions.

**Method.**

The study utilizes a Pb-flux growth method to produce high-quality, impurity-free single crystals, followed by characterization via X-ray diffraction, magnetometry (SQUID), and transport measurements (resistivity and Hall effect).

**Summary.**

This paper reports the successful growth of high-quality EuAuBi single crystals using a Pb-flux method, which eliminates Au2Bi impurities responsible for previously reported superconductivity. By using c-axis oriented crystals, the authors discover a topological Hall effect that appears during metamagnetic transitions. The study links electronic transport anomalies to magnetic reconstruction and non-collinear spin textures. These findings highlight how crystal orientation is crucial for observing topological signatures in magnetic semimetals.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system is EuAuBi, an antiferromagnetic topological semimetal with a hexagonal crystal structure (space group P63mc) and Eu atoms situated along the c-axis.

**Key observables.**

Electrical resistivity, magnetization, Hall resistivity (including decomposition into ordinary, anomalous, and topological components), specific heat, and magnetoresistance.

**Important parameters / regimes.**

Neel temperature (TN approx 4.8 K), Debye temperature (approx 135 K), and metamagnetic transition fields (approx 2 T and 3 T).

**Assumptions / limitations.**

The analysis assumes that the Hall signal can be decomposed into ordinary, anomalous, and topological components and that the superconductivity in previous studies was due to secondary phases.

**Figures summary.**

Figure 1 shows the crystal structure and evidence of impurities in Bi-flux crystals; Figure 2 displays the high-quality Pb-flux grown crystals and their XRD/Laue patterns; Figure 3 presents magnetization and specific heat data showing the antiferromagnetic transition and metamagnetic features.

**Paper structure.**

The paper begins with crystal growth and structural characterization, moves to the investigation of impurities and the debunking of intrinsic superconductivity, then explores transport properties and the discovery of the orientation-dependent topological Hall effect, and concludes with thermodynamic evidence of magnetic reconstruction.

</details>

<details><summary>Abstract</summary>

We report the growth of high-quality single crystals of the magnetic topological semimetal EuAuBi using a Pb flux method, which effectively suppresses the formation of secondary Au2Bi impurity phases that were prevalent in the previously reported Bi flux grown crystals. This growth optimization enables reliable investigation of the intrinsic physical properties of EuAuBi. Importantly, Pb flux growth stablilizes c axis oriented single crystals, enabling Hall measurements in a previously unexplored geometry. In this configuration (I parallel to c, B perpendicular to c), a finite residual Hall contribution, known as topological Hall signal emerges below the antiferromagnetic ordering temperature and within a narrow magnetic field range. This Hall contribution coincides with the metamagnetic transitions, anomalies in magnetoresistance, and an additional feature in field-dependent specific heat, indicating strong coupling between the electronic transport and field induced magnetic reconstructions. Consequently, these findings underscore the significance of crystal orientation in uncovering topological transport signatures in magnetic semimetals such as EuAuBi.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25631"></a>


### [Local tensor-train surrogates for quantum learning models](http://arxiv.org/abs/2604.25631v1)

**Authors:** Sreeraj Rajindran Nair, Christopher Ferrie

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25631v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25631_figures/2604.25631_fig1.jpg" width="500"><br>

<sub>Figure 1: Sample illustration of the local tensor-train surrogates (LTTS): Starting from a function f, we restrict to a local patch and approximate f by a truncated Taylor polynomial. The Taylor coefficients are embedded as a tensor and represented in tensor-train (TT) format with cores A1, . . . , Ak, which serves as an analytical certificate predictor with a known error bound decomposition. An empirical risk minimizer (ERM) then fits a new TT with cores B1, . . . , Bk directly from sampled function values in the local patch that potentially uses the Taylor-TT certificate as a warm-start initialization instead of a random initialization. We present deterministic bounds on the certificate’s...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25631_figures/2604.25631_fig2.jpg" width="500"><br>

<sub>Figure 2: Scatter of minimal TT rank caps (χbox, χ∆) for 176 test cases across four (N, p) configurations. Top row: common-scale criterion ∥A −ATT∥F ≤ε∥Abox∥F ; bottom row: self-relative criterion ∥A − ATT∥F ≤ε∥A∥F . Left column: ε = 10−2; right column: ε = 10−3. Points above the dashed diagonal indicate rank inflation (ρ &gt; 1); points below indicate deflation (ρ &lt; 1). Small random jitter is added for visibility since ranks are discrete. Separable functions cluster above the diagonal at χbox = 1; matched- degree polynomials lie on the diagonal; higher-degree polynomials and additional non-separable families fall below the diagonal under the common-scale criterion and move closer to the...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25631_figures/2604.25631_fig3.jpg" width="500"><br>

<sub>Figure 3: Local TT surrogate (LTTS) validation across two datasets: Top row: synthetic Gaussian classification. Bottom row: UCI Banknote Authentication. Each row shows the same 4-panel diagnostic: (A) error decomposition vs patch radius r at the primary center x0, including an r3 reference, (B) TT coefficient-tensor truncation error ∥C −Cχ∥F /∥C∥F vs rank cap χ across multiple centers; (C) total surrogate RMSE ∥g −Tp,χ∥vs r across centers at the best (largest) χ used; (D) Remark 5.1 proxy, TT/TRUNC = RMSE(Tp −Tp,χ)/RMSE(g −Tp) vs χ at r ≈0.1, with the 10−2 threshold indicating when TT compression error is negligible relative to Taylor truncation.</sub>

</details>

**Main problem.**

The high computational cost of repeated quantum circuit evaluations during the inference phase of Quantum Machine Learning (QML) models.

**Main result.**

The development of a framework for local Tensor-Train (TT) surrogates that provides provable error certificates and statistical guarantees for approximating black-box quantum models.

**Method.**

A combination of Taylor polynomial approximation, Tensor-Train (TT) compression via TT-SVD, and Empirical Risk Minimization (ERM) within local patches of the input space.

**Summary.**

This paper introduces a method to create fast classical 'surrogates' for expensive quantum machine learning models. By using Tensor-Train decomposition and Taylor expansions within local patches of data, the authors create a framework that is much faster than direct circuit evaluation. The method provides mathematical guarantees on the accuracy of these surrogates, effectively separating the complexity of the representation from the complexity of the features. Numerical tests show speedups of up to 400x while maintaining high accuracy.

<details><summary>Detailed structure</summary>

**Model / system.**

Arbitrary trained quantum machine learning models, such as Variational Quantum Algorithms (VQAs) and Parametrized Quantum Circuits (PQCs), treated as black-box functions mapping classical inputs to expectation values.

**Key observables.**

Expectation values of quantum observables (e.g., Z expectation value), RMSE, and TT/TRUNC error ratios.

**Important parameters / regimes.**

Patch radius (r), polynomial degree (p), TT bond dimension (chi), number of data dimensions (N), and sample size (n).

**Assumptions / limitations.**

The target function is locally smooth and continuously differentiable; the input data is sampled i.i.d. from a distribution supported on a local patch; the quantum model is treated as a black-box.

**Figures summary.**

Figure 1 illustrates the LTTS workflow; Figure 3 shows error decomposition, TT compression error vs. rank, and surrogate RMSE vs. patch radius across different datasets.

**Paper structure.**

The paper identifies the QML inference bottleneck, proposes the LTTS framework, establishes a deterministic error certificate via Taylor-TT construction, provides statistical generalization bounds via ERM, analyzes rank scaling, and validates the method with numerical experiments.

</details>

<details><summary>Abstract</summary>

A key bottleneck in quantum machine learning is the computational cost of repeated quantum circuit evaluations during the inference phase. To address this, we present a framework for constructing fast, cheap, provably accurate classical tensor-train surrogates of fully trained quantum machine learning models within local patches of their input data space. The approach combines Taylor polynomial approximation with a tensor-train (TT) representation and embeds it in a statistical learning paradigm via empirical risk minimization. In our analysis, the Taylor-TT construction serves as a deterministic error certificate proving that the TT hypothesis class contains a good approximation; empirical risk minimization then provably recovers a surrogate with controlled generalization error and explicit bounds. This translates into three independently controllable error sources: (i) Taylor truncation error controlled by the patch radius $r$ and polynomial degree $p$, (ii) TT approximation error controlled by the bond dimension $χ$, and (iii) statistical estimation error. While the parameter count scales polynomially in the number of data dimensions $N$, i.e., $d_{\mathrm{eff}} = N(p+1)χ^2$ rather than the naive $(p+1)^N$, the worst-case constants inherit an exponential factor through the tensor-product feature norm during Taylor polynomial embedding onto TT. This cleanly separates representation complexity from feature-induced constants. Our risk bounds and sample complexity depend explicitly on the local patch radius $r$.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24848"></a>


### [Magnetic phases of the anisotropic triangular Hubbard model from the ghost-Gutzwiller approximation in the rotating spin-frame](http://arxiv.org/abs/2604.24848v1)

**Authors:** Azin Kazemi-Moridani, Samuele Giuli, Tsung-Han Lee, A. -M. S. Tremblay, Michel Côté, Nicola Lanatà, Olivier Gingras

**Type:** theory · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.24848v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.24848_figures/2604.24848_fig1.jpg" width="500"><br>

<sub>FIG. 1. Hubbard model and the geometry of the anisotropic triangular lattice. The model contains the nearest-neighbor hoppings t along ±a1 and ±a2, and t′ along ±(a1−a2), along with the double occupation cost U. For t′ = t, the model is isotropic and C6 symmetric, and anisotropic for t′ ̸= t.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24848_figures/2604.24848_fig2.jpg" width="500"><br>

<sub>FIG. 2. (a1, a2) Non-interacting dispersions ε(k) of the triangular lattice for the isotropic (t′/t = 1) and the anisotropic (here t′/t = 0.4) lattice, respectively. The dashed hexagon, full straight lines, and arrow indicate the Brillouin zone, mirror symmetries, and C6 symmetry, respectively. Solid red lines indicate the Fermi surface. The dotted grey line highlights the momentum characteristic of decoupled one-dimensional chains. In the isotropic case, the M and K points are symmetry- equivalent. In the anisotropic case, the M ′ and K′ points are symmetry-equivalent, but inequivalent to the M and K points. (b-e) Real space representation of the different classes of magnetic phases. (b)...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24848_figures/2604.24848_fig3.jpg" width="500"><br>

<sub>FIG. 3. Results for magnetic phases with a wavevector along the Γ −M high-symmetry path. (a) Visual representation of the high-symmetry path. It goes from the zone center at Γ to the middle of a neighboring zone edge at M, going through a corner of the Brillouin zone at K. This path allows us to capture both the AFM state (at M), the spiral state (at K), the quasi-one-dimensional 1DAFM state (at X in the middle), and other generic states in between. (b) Total energy Eq in the grand canonical ensemble along the path Γ −M at fixed U/t = 8 for several t′/t obtained with GA (B = 1). All states with finite t′ display a plateau at small momentum, where the system falls into the metallic solution....</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24848_figures/2604.24848_fig4.jpg" width="500"><br>

<sub>FIG. 4. Results for magnetic states with wavevectors on the full two-dimensional grid. (a) Phase diagram obtained by extracting the magnetic ordering wavevector that minimizes the total energy Eq. The solid colors correspond to the ghost-GA B = 3 phase diagrams, while the hatched regions represent the phases obtained with GA when they differ from ghost-GA. The green color represents the paramagnetic (PM) state, while the color gradient represents the continuous evolution of magnetic states, with yellow, orange, and red the AFM, spiral quasi-1DAFM states, respectively. As in the results depicted in Fig. 3, the magnetic q fall on the high-symmetry path along Γ −X −K −M. The blue squares and...</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.24848_figures/2604.24848_fig5.jpg" width="500"><br>

<sub>FIG. 5. Phase diagram based on the magnetic susceptibility. (a) Largest value in q of the susceptibility χm q defined in Eq. 9, obtain with GA (B = 1) and using ϕx/t = 10−2. As we move away in parameter space from the magnetic dome depicted in Fig. 4, the amplitude of the susceptibility decreases. In the following subfigures, we present χm q on the q-grid for a few examples. (b-e) Magnetic susceptibility at fixed t′/t = 5 along increasing U/t. While χm q starts to look like a vertical line passing through the X-point characteristic of the quasi-1DAFM state, the amplitude is far from diverging. As U/t increases, the amplitude also increases, and the maximum of χm q localizes close to the...</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.24848_figures/2604.24848_fig6.jpg" width="500"><br>

<sub>FIG. 6. Anomalies at the phase boundary between the paramagnetic and magnetic solutions. Some points have a shallow minimum (highlighted by the purple circle) in the q-dependent total energy Eq that is either away from the Γ −M high-symmetry path, or at an unexpected place in the (t′/t, U/t) phase diagram. We discard the shallow minima and believe the unexpected points are due to coarse-graining of the q-mesh. Magnetism becomes very sensitive to this at the phase boundary. (a-c) correspond to some points of the GA phase diagram, while (d) corresponds to the ghost-GA phase diagram.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.24848_figures/2604.24848_fig7.jpg" width="500"><br>

<sub>FIG. 7. Triangular lattice and square lattice with an extra diagonal hopping. Both are topologically equivalent.</sub>

</details>

**Main problem.**

Determining the magnetic phase diagram of the anisotropic triangular Hubbard model and evaluating the accuracy of the ghost-Gutzwiller approximation (ghost-GA) compared to DMFT.

**Main result.**

The ghost-GA achieves near-DMFT accuracy at a fraction of the cost by using auxiliary orbitals to capture dynamical fluctuations, successfully identifying paramagnetic, spiral, and SDW phases while finding that the 1D AFM phase is not stabilized.

**Method.**

The study uses the ghost-Gutzwiller approximation (ghost-GA) combined with a rotating spin-frame formulation for direct total-energy minimization over a high-resolution momentum grid.

**Summary.**

This paper investigates the magnetic phase diagram of the anisotropic triangular Hubbard model using an improved variational method called the ghost-Gutzwiller approximation. By adding 'ghost' orbitals, the authors are able to capture dynamical correlation effects that standard Gutzwiller methods miss, reaching accuracy levels close to much more expensive DMFT calculations. The study maps out various magnetic phases, including spiral and spin-density wave orders, and provides an efficient framework for studying frustrated magnetic systems.

<details><summary>Detailed structure</summary>

**Model / system.**

The half-filled Hubbard model on an anisotropic triangular lattice, characterized by nearest-neighbor hopping t and diagonal hopping t'.

**Key observables.**

Staggered magnetization (Mq), total energy (Eq), magnetic susceptibility (chi_q), and ordering wavevector (q).

**Important parameters / regimes.**

Interaction strength (U/t), anisotropy/frustration ratio (t'/t), and the number of ghost orbitals (B).

**Assumptions / limitations.**

The analysis is restricted to coplanar magnetic configurations; the ghost-GA is a single-site method that neglects non-local correlations.

**Figures summary.**

Fig 1 shows the lattice geometry; Fig 2 shows electronic dispersions and real-space magnetic phases; Fig 3 presents energy curves and the 1D phase diagram; Fig 4 shows the full 2D phase diagram; Fig 5 displays magnetic susceptibility scans; Fig 7 demonstrates the topological equivalence of lattice representations.

**Paper structure.**

The paper introduces the model and geometry, describes the ghost-GA and rotating spin-frame methodology, presents the phase diagram and energy minimization results, compares the accuracy of GA vs ghost-GA vs DMFT, discusses susceptibility behavior, and concludes with a proof of lattice equivalence.

</details>

<details><summary>Abstract</summary>

We investigate the magnetic phase diagram of the half-filled Hubbard model on the anisotropic triangular lattice using the Gutzwiller approximation (GA) and its ghost generalization (ghost-GA). By combining a rotating spin-frame formulation with high-resolution momentum grids, we determine magnetic ground states through direct total-energy minimization over the ordering wavevector. We benchmark standard GA and ghost-GA against dynamical mean-field theory (DMFT) and dual-fermion results. We show that GA already captures the qualitative structure of the phase diagram, but systematically overestimates the stability of magnetic order due to the absence of dynamical fluctuations. We find that introducing a small number of auxiliary ''ghost'' orbitals is sufficient to recover most dynamical effects and significantly improves quantitative agreement with DMFT. Exploring the full Brillouin zone, we obtain a phase diagram comprising paramagnetic and various magnetic phases. In contrast to ladder dual-fermion susceptibility-based predictions, we find that the one-dimensional antiferromagnetic phase is never stabilized, despite being the leading instability in certain regimes. Our results establish ghost-GA as an efficient and systematically improvable framework for studying magnetism in frustrated systems, capable of achieving near-DMFT accuracy at a fraction of the computational cost. They also highlight that standard GA performs qualitatively well for capturing the general phase diagram, enabling the investigation of incommensurate magnetic orders in more complex systems.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25026"></a>


### [Networked Realization of Quantum LDPC Codes](http://arxiv.org/abs/2604.25026v1)

**Authors:** Swayangprabha Shaw, Narayanan Rengaswamy

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25026v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25026_figures/2604.25026_fig1.jpg" width="500"><br>

<sub>Fig. 1: Bivariate bicycle (BB) code [15]: (a) toric representa- tion, (b) Tanner graph, and (c) depth-8 measurement schedule.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25026_figures/2604.25026_fig2.jpg" width="500"><br>

<sub>Fig. 2: Schematic of networked surface code architecture. The hexagonal regions represent individual processors, each con- taining one data qubit. A GHZ state is utilized for syndrome extraction, as illustrated by the dashed lines connecting the GHZ state to specific data qubits within the grid structure.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25026_figures/2604.25026_fig3.jpg" width="500"><br>

<sub>Fig. 3: Balanced graph partitioning of the combined X-Z Tanner graph across two nodes, N1 and N2. The red lines represent bridge edges connecting check qubits and data qubits distributed across the two nodes. We performed balanced graph partitioning on this combined X-Z Tanner graph using pymetis [23]. This assigns every data qubit and every check qubits to one of the two network partitions.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25026_figures/2604.25026_fig4.jpg" width="500"><br>

<sub>Fig. 5: Surface code performance with noisy GHZ (pGHZ = 0.002) under full circuit-level noise. This reproduces the exact performance and ≈7.5% threshold estimated in [1].</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25026_figures/2604.25026_fig5.jpg" width="500"><br>

<sub>Fig. 4: Surface code performance with varying GHZ noise rate (p = 0). A clear threshold is visible, below which logical error rates decrease with increasing code distance.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25026_figures/2604.25026_fig6.jpg" width="500"><br>

<sub>Fig. 6: Logical error-rate comparison between non-partitioned and partitioned BB code implementations for the [[72, 12, 6]], [[90, 8, 10]], and [[144, 12, 12]] codes under circuit-level noise. Solid curves correspond to non-partitioned implementations, while dashed curves correspond to partitioned implementations obtained from a pymetis bipartition of the combined Tanner graph. In the partitioned case, cross-partition interactions are implemented using Bell-pair-assisted bridge operations, and the effect of Bell-link quality is shown for Bell-state fidelities FBell = 0.99 and FBell = 0.96 (equivalently, pBell = 0.0125 and pBell = 0.05). The black dash-dotted line denotes the uncoded...</sub>

</details>

**Main problem.**

The non-local stabilizer connections required by high-performance QLDPC codes like Bivariate Bicycle (BB) codes present significant hardware challenges for monolithic processors. This work investigates whether these codes can be effectively implemented in a networked architecture where qubits are distributed across multiple modules.

**Main result.**

The study finds that a networked implementation of BB codes is viable if Bell pair fidelity is maintained at approximately 99% or higher. It also identifies a local gate noise threshold of roughly 1% for these partitioned codes.

**Method.**

The authors use Stim for circuit-level noise simulations and PyMetis for balanced min-cut partitioning of the X-Z Tanner graph. Decoding is performed using Belief Propagation with Ordered Statistics Decoding (BP-OSD) for BB codes and PyMatching for surface codes.

**Summary.**

This paper explores the feasibility of implementing Bivariate Bicycle QLDPC codes in a distributed quantum network. By partitioning the code across two nodes and using Bell-pair-assisted gates, the authors quantify the noise penalty introduced by the network. They demonstrate that while partitioning increases the error rate, the advantage of QLDPC codes can be preserved provided the inter-node entanglement fidelity remains high (above 99%). This provides a roadmap for scaling quantum error correction using modular hardware.

<details><summary>Detailed structure</summary>

**Model / system.**

A networked quantum architecture consisting of two interconnected nodes. Each node contains a subset of the code's qubits and ancillas, with inter-module operations mediated by teleported CNOT gates using pre-shared Bell pairs.

**Key observables.**

Logical error rate (pL), error thresholds for gate and GHZ noise, and Bell pair demand per syndrome cycle.

**Important parameters / regimes.**

Bell pair fidelity (F_Bell), physical error rate (p), encoding rate, code distance (d), and the number of cut edges (E_cut) in the Tanner graph.

**Assumptions / limitations.**

The noise model assumes stochastic depolarizing errors on all gates, measurements, and resets, and that the network connectivity is limited to the edges defined by the partitioning strategy.

**Figures summary.**

Figure 1 shows the BB code structure and measurement schedule; Figure 2 depicts the networked surface code architecture; Figure 3 illustrates the graph partitioning strategy; Figure 4 and 5 show surface code error thresholds; Figure 6 compares logical error rates for different BB code families.

**Paper structure.**

The paper introduces the challenge of non-local QLDPC codes, establishes a surface code baseline in a networked setting, proposes a partitioning strategy for BB codes, presents circuit-level noise simulations and threshold analyses, and concludes with performance comparisons and future directions.

</details>

<details><summary>Abstract</summary>

Quantum low-density parity-check (QLDPC) codes with good parameters are promising candidates for low-overhead fault-tolerant quantum computing, but their non-local stabilizers require long-range connectivity and frequent qubit movement, introducing practical challenges. Prior work has studied the networked implementation of topological codes, where each node only holds one or a few qubits of the entire code, and demonstrated competitive performance under practical constraints such as the quality of network-provided entanglement. However, since these codes are already geometrically local, such a networked setting might not be essential. In this work, we propose and study the networked implementation of better QLDPC codes, specifically bivariate bicycle codes due to their similarity to surface codes and the controlled amount of long-range connections in their stabilizers. We begin by recreating networked surface codes in Stim, with one code qubit per node, and provide additional insights into their circuit-level noise performance. We then extend this approach to bipartitions of bivariate bicycle codes, using balanced min-cut partitioning on their combined X-Z Tanner graph to identify optimal qubit splits. For stabilizers spanning nodes, we implement teleported CNOTs and vary the Bell pair fidelity enabling these gates. Through circuit-level noise simulations with BP-OSD decoding, we provide the first insights into networked realizations of these codes and compare their performance with monolithic implementations. We conclude by outlining advantages, limitations, and future directions.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25598"></a>


### [Observation and Control of Moiré-Tailored Topological Dirac States](http://arxiv.org/abs/2604.25598v1)

**Authors:** R. Ganser, M. P. T. Masilamani, B. Geldiyev, M. M. Hirschmann, A. Consiglio, J. Schusser, D. Di Sante, M. Ünzelmann, F. Reinert

**Type:** both · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25598v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25598_figures/2604.25598_fig1.jpg" width="500"><br>

<sub>FIG. 1. Structural and electronic characterization of the flat (a-c) and moir´e-modulated (d-f) honeycomb monolayer AgTe on Ag(111). a, A ball model of the flat AgTe/Ag(111), where the surface unit cell is indicated by the yellow rhombus. b, The associated LEED image reveals the ( √</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25598_figures/2604.25598_fig2.jpg" width="500"><br>

<sub>FIG. 2. Formation of moir´e band gaps and Dirac nodal lines from non-symmorphic moir´e superlattice symmetry. a,b ARPES data and c,d continuum model calculations (see text). a, c, Constant energy contours with the top and bottom slices correspond to energies of −0.35 eV and −0.46 eV relative to EF, respectively. b, d, Band structure cuts along the two distinct momentum paths indicated in a (cuts 1 and 2). Key electronic features, i.e., Dirac cone and Dirac nodal line are labeled across all plots for clarity. ARPES data was conducted at 40 K. e Schematic illustrating the emergence of a glide-plane symmetry resulting from the formation of a moir´e superlattice. For better visibility, we here...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25598_figures/2604.25598_fig3.jpg" width="500"><br>

<sub>FIG. 3. Structural tuning of the moir´e electronic band structure via the AgTe coverage and temperature. a–c, ARPES intensity maps recorded at room temperature (RT) (a, b) and at 40 K (c). Black arrows mark the symmetry-enforced Dirac crossings. f, Mutual scaling of the energy gap ∆E (yellow squares) and the energy of the valence band maximum (blue circles) against the moir´e reciprocal lattice vector gmoir´e. The linear trend highlights the systematic response of the AgTe band structure to the moir´e superlattice periodicity. The error bars are derived from the confidence intervals by varying the center position (of the energy peak or Dirac point momentum) within reasonable limits. This is...</sub>

</details>

**Main problem.**

The difficulty of directly observing and distinguishing true gapless moiré-Dirac quasiparticles from trivial photoemission artifacts in moiré heterostructures.

**Main result.**

Direct spectroscopic evidence of topologically protected, moiré-dressed Dirac nodal lines that can be continuously tuned by adjusting the moiré lattice periodicity.

**Method.**

Angle-resolved photoemission spectroscopy (ARPES) and low-energy electron diffraction (LEED) combined with density functional theory (DFT) and a continuum model analysis.

**Summary.**

This paper reports the discovery of topologically protected Dirac nodal lines in a 1D moiré superlattice formed by AgTe on Ag(111). Using ARPES, the researchers demonstrate that these massless Dirac states are protected by the non-symmorphic glide-mirror symmetry of the superlattice. They show that the electronic structure, including the band gaps and Dirac points, can be continuously controlled by tuning the moiré periodicity through temperature or coverage. This work establishes moiré heterostructures as a versatile platform for engineering and controlling topological electronic states.

<details><summary>Detailed structure</summary>

**Model / system.**

An epitaxial surface-moiré heterostructure consisting of a compressed AgTe monolayer on an Ag(111) substrate, characterized by a 1D superlattice potential and non-symmorphic glide-mirror symmetry.

**Key observables.**

Band dispersions, band gaps (approx. 160 meV), bandwidth (approx. 200 meV), and moiré reciprocal lattice vectors.

**Important parameters / regimes.**

Moiré lattice periodicity, temperature (40 K to room temperature), and AgTe coverage.

**Assumptions / limitations.**

The use of a modified nearly-free-electron continuum model and a coupled-chain tight-binding toy model to represent the superlattice potential.

**Figures summary.**

Fig 1 shows structural and electronic characterization of flat vs. moiré AgTe; Fig 3 shows ARPES intensity maps at different temperatures/coverages and a plot of universal scaling behavior for the energy gap and valence band maximum.

**Paper structure.**

The paper introduces the moiré system, presents structural and electronic characterization, details the spectroscopic observation of Dirac states, provides symmetry-based topological analysis, demonstrates tunability via temperature and coverage, and concludes with scaling laws.

</details>

<details><summary>Abstract</summary>

Moiré heterostructures provide a powerful framework for tailoring electronic band structures via controlled long-range periodic superlattice potentials. Beyond widely studied moiré-tailored flat bands, folded band structures can host emergent Dirac states, which have recently attracted considerable interest. Direct momentum-resolved observation of gapless moiré-Dirac quasiparticles, however, is challenging and has so far remained elusive. By performing angle-resolved photoemission spectroscopy measurements on an epitaxial surface-moiré structure, we here provide direct spectroscopic evidence of moiré-dressed Dirac states with topological character. Driven by the one-dimensional superlattice potential, electrons propagate anisotropically with a weak but massless Dirac dispersion along the confinement direction. The observed band crossings belong to topological nodal lines pinned to the mini-Brillouin zone boundaries. As such, they are enforced and robustly protected by the non-symmorphic symmetry of the superlattice. Finally, we demonstrate that the topological excitations can be almost continuously controlled by tuning the moiré lattice periodicity, directly unveiling moiré heterostructures as a promising platform for creating and controlling topological moiré-Dirac states.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25613"></a>


### [One Coordinate at a Time: Convergence Guarantees for Rotosolve in Variational Quantum Algorithms](http://arxiv.org/abs/2604.25613v1)

**Authors:** Sayantan Pramanik, M Girish Chandra

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25613v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25613_figures/2604.25613_fig1.jpg" width="500"><br>

<sub>Fig. 1: Plot of training loss against (a) iterations, and (b) the number of circuit-executions (on a log-scale) for SGD, RCD, RSGF, SPSA, and Rotosolve .</sub>

</details>

**Main problem.**

The paper addresses the open question of whether the Rotosolve algorithm, a popular coordinate-descent method for training parametrized quantum circuits, possesses formal convergence guarantees.

**Main result.**

The authors prove that Rotosolve converges to epsilon-stationary points in non-convex smooth landscapes and to epsilon-suboptimal points under the Polyak-Lojasiewicz condition, providing explicit worst-case convergence rates.

**Method.**

The study uses a rigorous mathematical analysis of the trigonometric structure of the objective function, comparing Rotosolve's performance and shot-complexity against RCD, SGD, SPSA, and RSGF.

**Summary.**

This paper provides the first formal convergence guarantees for the Rotosolve algorithm used in training variational quantum circuits. It proves that the algorithm is effective in both non-convex and PL-condition landscapes, even in the presence of finite-shot noise. The authors demonstrate that Rotosolve is hyperparameter-free and can outperform standard gradient-based methods like SGD in quantum machine learning tasks. This work turns a previously heuristic optimization method into a mathematically grounded tool for quantum computing.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on Variational Quantum Algorithms (VQAs) using parametrized quantum circuits where the objective function is the expectation value of a Hermitian observable.

**Key observables.**

The expectation value of a Hermitian observable H, and the gradient norm for stationarity.

**Important parameters / regimes.**

The number of parameters d, the noise variance sigma^2 in the finite-shot regime, and the Polyak-Lojasiewicz constant mu.

**Assumptions / limitations.**

Assumes the objective function is coordinate-wise smooth, the estimator is unbiased with bounded variance, and the landscape satisfies the Polyak-Lojasiewicz condition almost everywhere.

**Figures summary.**

Figure 1(a) shows training loss vs. iterations for various optimizers, and Figure 1(b) shows training loss vs. number of circuit executions, demonstrating Rotosolve's efficiency.

**Paper structure.**

The paper defines the Rotosolve algorithm and its trigonometric basis, proves convergence theorems for stationary and suboptimal points, compares complexity with RCD, and validates findings via QML numerical experiments.

</details>

<details><summary>Abstract</summary>

In this paper, we resolve an open question in the field of optimization algorithms for training parametrized quantum circuits: Does the popular Rotosolve algorithm converge? Until now, interpolation-based coordinate descent methods such as Rotosolve have mostly been treated as heuristics, lacking any formal convergence guarantees. We rigorously analyze Rotosolve, and show that it converges to $\varepsilon$-stationary points if the optimization landscape is non-convex and smooth; and to $\varepsilon$-suboptimal points if the objective function additionally obeys the Polyak-Lojasiewicz (PL) condition. Further, we derive explicit worst-case rates of convergence in the finite quantum measurement regime. These rates are contrasted against those from a similar coordinate-based method: Randomized Coordinate Descent (RCD). Although in the worst case their rates are, prima facie, equivalent, we present arguments for a more nuanced comparison between the two. We highlight that Rotosolve is hyperparameter-free, and implicitly uses first and second derivatives in its updates. Finally, we supplement our theoretical findings with numerical experiments from Quantum Machine Learning; and compare the performance of Rotosolve against RCD, Stochastic Gradient Descent, Simultaneous Perturbation Stochastic Approximation, and Randomized Stochastic Gradient Free methods.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25282"></a>


### [Piezomagnetic effect of a rare-earth-based altermagnet TbPt6Al3](http://arxiv.org/abs/2604.25282v1)

**Authors:** Ryohei Oishi, Kazunori Umeo, Takuya Aoyama, Takahiro Onimaru, Kaya Kobayashi

**Type:** experiment · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25282v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25282_figures/2604.25282_fig1.jpg" width="500"><br>

<sub>Fig. 1. (Color online) (a) Magnetic structure of TbPt6Al326) in which Pt1, Pt2, Pt4, and Al are omitted for clar-</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25282_figures/2604.25282_fig2.jpg" width="500"><br>

<sub>Fig. 2. (Color online) Temperature dependence of magnetization M(T) of the single crystal of TbPt6Al3 under</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25282_figures/2604.25282_fig3.jpg" width="500"><br>

<sub>Fig. 3. (Color online) Temperature dependence of the piezomagnetic coeﬃcient Q11 of TbPt6Al3. The blue</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25282_figures/2604.25282_fig4.jpg" width="500"><br>

<sub>Fig. 4. (Color online) (a) Temperature dependence of magnetization of TbPt6Al3 at σ1 = 150 MPa and Hmeas ∥</sub>

</details>

**Main problem.**

Investigation of the piezomagnetic (PZM) effect in the rare-earth-based g-wave altermagnet TbPt6Al3 and understanding the origin of its exceptionally large PZM coefficient.

**Main result.**

The study observes a linear PZM effect with a coefficient Q11 that is over two orders of magnitude larger than in other altermagnets, attributed to the strong relativistic spin-orbit coupling of Tb3+ 4f electrons.

**Method.**

Magnetization measurements were performed on single-crystalline samples under uniaxial stress using a superconducting magnetometer and a custom-made pressure cell.

**Summary.**

This paper reports the discovery of an exceptionally large linear piezomagnetic effect in the altermagnet TbPt6Al3. The observed PZM coefficient is more than 100 times larger than those found in transition-metal-based altermagnets. The researchers attribute this massive response to the strong relativistic spin-orbit coupling inherent in the 4f electrons of the terbium ions. This finding provides new insight into how heavy rare-earth elements can be used to enhance magneto-elastic responses in altermagnetic materials.

<details><summary>Detailed structure</summary>

**Model / system.**

The system is TbPt6Al3, a rare-earth-based g-wave altermagnet with a trigonal structure (space group 3-bar c) and collinear antiferromagnetic order.

**Key observables.**

Piezomagnetic coefficient (Q11), Néel temperature (TN), critical exponent (beta), and magnetization (M) under uniaxial stress.

**Important parameters / regimes.**

PZM coefficient Q11 = 9.1 x 10^-3 mu_B/(f.u. MPa) at 2 K; TN = 3.32 K; critical exponent beta = 0.28; poling field = 10,000 Oe.

**Assumptions / limitations.**

Assumes the observed magnetization change is due to the PZM effect and that the single-domain state is achieved via the described poling process.

**Paper structure.**

The paper introduces the material and the PZM effect, describes the experimental setup for applying uniaxial stress, presents the temperature and stress dependence of magnetization, analyzes the critical exponent, and concludes with a discussion on the role of spin-orbit coupling.

</details>

<details><summary>Abstract</summary>

We have investigated the piezomagnetic (PZM) effect of the rare-earth-based g-wave altermagnet TbPt6Al3 by magnetization measurements of single-crystalline samples under uniaxial stress sigma. The magnetization in magnetic field along the trigonal a axis increases linearly with sigma for T < TN, indicating the emergence of PZM effect, while the theoretically predicted nonlinear PZM effect was not observed. PZM coefficient of Q11 at 2 K is obtained as 9.1 times 10^-3 mu_B/(f.u. MPa), which is larger by more than two orders of magnitude than those for other altermagnets and noncollinear antiferromagnets. Temperature dependence of Q11 below TN yielded the critical component beta as 0.28, whose value is close to that of the magnetic moment estimated by the neutron powder diffraction. We propose that the large Q11 and the large poling field of 10000 Oe to achieve the single-domain state in TbPt6Al3 are due to the strong relativistic spin-orbit coupling of the 4f electrons in the Tb3+ ions.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25756"></a>


### [Predicting challenging phase transitions with Bayesian active learning](http://arxiv.org/abs/2604.25756v1)

**Authors:** Lorenzo Bastonero, Gabriel Joalland, Chiara Cignarella, Lorenzo Monacelli, Nicola Marzari

**Type:** theory · **Category:** disordered systems and neural networks · **PDF:** <https://arxiv.org/pdf/2604.25756v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25756_figures/2604.25756_fig1.jpg" width="500"><br>

<sub>FIG. 1. Schematic overview of the presented on-the-fly active learning scheme. Top panels, left to right, the proposed active learning scheme involves: (a) the generation of an ensemble of structures from the nuclear Gaussian density matrix ρRi,Φi at iteration i; (b) the selection of structures based on ML uncertainty, using a sparse Gaussian process force field; (c) DFT labeling, i.e., perform ground-state calculation to assign total energy E, forces, and stress of the selected structures, and use these to update the ML potential. Panel (d) schematically represents the on-the-fly active learning SSCHA with its nested processes. The left gray panel shows the SSCHA minimization workflow,...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25756_figures/2604.25756_fig2.jpg" width="500"><br>

<sub>FIG. 2. Thermodynamic and dynamical properties from the proposed active learning approach. Results of the present active-learning framework applied to (a – c) Li2O and to (d – f) α–CsPbI3 to calculate the equilibrium volume as a function of temperature, and compared to reference SSCHA calculations carried out entirely with DFT (SSCHA-DFT). (a,d) Number of DFT labeling calls during the on-the-fly training as a function of temperature and number of SSCHA minimization steps. Each iteration required the labeling of 200 and 400 configurations, for Li2O and α–CsPbI3 respectively. (b,e) Finite- temperature SSCHA equilibrium volume as obtained from the on-the-fly active learning procedure and...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25756_figures/2604.25756_fig3.jpg" width="500"><br>

<sub>FIG. 3. δ →α phase transition of CsPbI3. SSCHA Gibbs free energy difference between δ and α phase of CsPbI3 as a function of temperature, represented by the gray bullets. The crossing ∆Gδ→α = 0 indicates the predicted phase tran- sition temperature Ttheo, and it is compared with the experi- mental temperature Texp ≃320◦C = 593 K from Ref. 32.</sub>

</details>

**Main problem.**

Accurately predicting crystal thermodynamics and challenging phase transitions in materials with strong anharmonicity is computationally expensive due to the massive number of DFT evaluations required.

**Main result.**

The authors developed an on-the-fly Bayesian active learning framework that reduces the DFT workload by 98.4-99.8% while maintaining first-principles accuracy, successfully predicting the phase transition temperature of CsPbI3.

**Method.**

An iterative active learning workflow combining the Stochastic Self-Consistent Harmonic Approximation (SSCHA) with Sparse Gaussian Process (SGP) machine learning potentials using ACE descriptors.

**Summary.**

This paper presents a new machine learning-driven approach to accelerate the study of materials undergoing complex phase transitions. By using Bayesian active learning, the researchers can train highly accurate interatomic potentials using only a tiny fraction of the computational cost typically required by first-principles methods. The method successfully captures the temperature-dependent stability of perovskites, which is crucial for developing stable solar cells and batteries. This framework provides a scalable way to explore the thermodynamic landscapes of materials under realistic, high-temperature conditions.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on materials with significant anharmonicity, specifically Li2O (a superionic conductor) and CsPb and CsPbI3 (metal-halide perovskites) in their alpha and delta phases.

**Key observables.**

Gibbs free energy difference, phase transition temperature, phonon dispersions, equilibrium volume, and thermal expansion coefficient.

**Important parameters / regimes.**

Temperature (250-450 K for CsPbI3), pressure (ambient), and uncertainty thresholds for active learning selection.

**Assumptions / limitations.**

The nuclear density matrix is assumed to be representable as a multivariate Gaussian.

**Figures summary.**

Figure 1 shows the active learning workflow (ensemble generation, uncertainty selection, and DFT labeling); Figure 2 illustrates SSCHA calculations and temperature ranges; Figure 3(b) displays the Gibbs free energy difference vs. temperature to identify the phase transition.

**Paper structure.**

The paper introduces the problem of anharmonicity, presents the Bayesian active learning framework integrated with SSCHA, demonstrates efficiency and accuracy on Li2O and CsPbI3, and provides a detailed hyperparameter optimization analysis.

</details>

<details><summary>Abstract</summary>

Materials underpin modern technologies, from energy harvesting, storage, and conversion to information and communication technologies. Their functionality is often governed by the interplay between competing phases, as thermodynamic behavior shapes microscopic properties and ultimately determines technological performance; for instance, the light absorption of inorganic metal-halide perovskites in solar cells. Accurately predicting crystal thermodynamics, however, remains a major challenge for computational approaches because strong anharmonic effects require extensive sampling of the potential energy surface. Here, we present an on-the-fly Bayesian framework, combined with the stochastic self-consistent harmonic approximation, for learning first-principles interatomic potentials. This approach enables the prediction of thermodynamic properties over a broad temperature range with first-principles accuracy while requiring training on only a few tens to a few hundreds of atomic configurations. To demonstrate its power, we investigate the thermodynamic and dynamical properties of Li$_2$O, $α$-CsPbI$_3$, and $δ$-CsPbI$_3$, requiring only 44, 256, and 50 total-energy calculations, respectively. Notably, we show that this framework accurately captures the phase diagram of CsPbI$_3$, which explains its spontaneous degradation into the non-absorbing yellow phase, predicting the transition temperature with remarkable accuracy and efficiency. More broadly, the method presented opens a novel route toward accelerated materials engineering under realistic conditions for a wide range of technologically relevant applications, including solid-state batteries, optoelectronic devices, and memristors.

</details>

<sub>[↑ back to top](#top)</sub>
