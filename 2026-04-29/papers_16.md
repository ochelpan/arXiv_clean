# Daily arXiv Report

[← Index](index.md)

[← Previous](papers_15.md)
[Next →](papers_17.md)

## Papers 301–320


<a id="paper-2604.24858"></a>


### [Absence of Quasi-Majorana False Positives in Full-Shell Hybrid Nanowires](http://arxiv.org/abs/2604.24858v1)

**Authors:** Carlos Payá, César Robles, Pablo San-Jose, Elsa Prada

**Type:** theory · **Category:** disordered systems and neural networks · **PDF:** <https://arxiv.org/pdf/2604.24858v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.24858_figures/2604.24858_fig1.jpg" width="500"><br>

<sub>FIG. 1. Smooth electrostatic confinement in par- tial and full-shell nanowires. (a) Schematic of a local spectroscopy setup for a semi-infinite partial-shell nanowire threaded by a magnetic field B and with an insulating tunnel barrier U(z) that leaks into the nanowire over a length χ. In panel (a1), given a chemical potential µbulk, a Zeeman field VZ greater than a critical value V c Z drives the entire wire into the topological regime, developing a Majorana zero mode (MZM) at its end (red wave function). For a weaker field, in (a2), only a region of the wire becomes topological, developing quasi- Majorana zero modes (Q-MZMs) at its boundaries (red/green overlapping wave functions). (b)...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24858_figures/2604.24858_fig2.jpg" width="500"><br>

<sub>FIG. 2. Detection of MZM versus quasi-MZMs. LDOS of the mJ = 0 sector versus smoothness parameter χ and energy ω at the end of a semi-infinite partial-shell (a,b) and full-shell (c,d) hybrid nanowires. The left (right) column cor- responds to the Majorana (quasi-Majorana) case. In (d), the visibility of low-energy states is lost before the Q-MZM peak if formed. Parameters taken at the green and blue marks of Fig. 1(c,h), respectively. Other parameters in Appendix E.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24858_figures/2604.24858_fig3.jpg" width="500"><br>

<sub>FIG. 3. Same as Fig. 2 but in the presence of short-range disorder. Parameters are given in Appendix E.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24858_figures/2604.24858_fig4.jpg" width="500"><br>

<sub>FIG. 4. Origin of the trivial skin. (a) Schematic repre- sentation of the topological filling of the first radial subband (mr = 0) of a full-shell nanowire as a function of angular mo- mentum mL ∈Z with ∆0 = 0, Φ = 0.5Φ0 and kz = 0. As the chemical potential µ increases, various mL are occupied. A topological transition can only occur for specific mL modes (highlighted in red). Consequently, µ must reach a threshold value µts, which in turn generates a trivial skin at the hybrid nanowire’s end. (b) Same as (a) but for the second radial sub- band (mr = 1). Notice that (a) [(b)] represents a case with unrealistically strong (realistically small) SOC. (c) Topologi- cal phase diagram as a...</sub>

</details>

**Main problem.**

The difficulty in distinguishing true Majorana zero modes (MZMs) from 'quasi-Majorana' false positives in tunneling spectroscopy due to smooth electrostatic disorder at the ends of partial-shell nanowires.

**Main result.**

Full-shell hybrid nanowires prevent false positives because a 'trivial skin' forms at the wire end, which hides quasi-Majorana states from local probes while allowing true MZMs to remain detectable.

**Method.**

Numerical simulations using the Quantica.jl package to calculate the Bogoliubov-de Gennes Hamiltonian, local density of states, and topological invariants.

**Summary.**

This paper addresses the critical issue of false-positive Majorana signatures in hybrid nanowires. It demonstrates that while smooth disorder can create fake Majorana-like states in conventional partial-shell wires, a full-shell nanowire design inherently suppresses these signals. By creating a 'trivial skin' that masks non-topological states, the full-shell architecture makes tunneling spectroscopy a much more reliable tool for detecting true Majorana zero modes.

<details><summary>Detailed structure</summary>

**Model / system.**

A comparison between partial-shell and full-shell Al/InAs hybrid nanowires, where the full-shell geometry acts as a synthetic vortex with fluxoid quantization and radial confinement.

**Key observables.**

Local Density of States (LDOS), Zero-Energy Peaks (ZEPs), and topological phase diagrams.

**Important parameters / regimes.**

Zeeman field (V_Z), magnetic flux (Phi), chemical potential (mu), spin-orbit coupling (alpha), and electrostatic smoothness parameter (chi).

**Assumptions / limitations.**

The electrostatic potential is modeled as an exponentially decaying profile; the superconducting shell is treated via an effective self-energy approximation.

**Figures summary.**

Fig 1 shows schematics and phase diagrams for both wire types, including DOS and wavefunctions; Fig 3 compares the impact of strong short-range disorder on MZM vs Q-MZM visibility.

**Paper structure.**

The paper introduces the MZM detection problem, compares partial-shell and full-shell geometries, details the emergence of the 'trivial skin' in full-shell wires, and evaluates the robustness of this protection against disorder.

</details>

<details><summary>Abstract</summary>

Tunneling spectroscopy cannot be used as an unambiguous detection tool for Majorana zero modes (MZMs) in conventional partial-shell nanowires. The presence of smooth confinement at the end of the hybrid wire (among other sources of disorder) can create exponentially pinned zero-energy states, called quasi-MZMs, that mimic all local signatures of MZMs but lack topological protection. We find that this ambiguity in MZM detection does not occur in full-shell hybrid nanowires, an alternative nanowire design where a superconducting shell fully surrounds the semiconductor core. Acting as a synthetic vortex, a full-shell hybrid nanowire hosts Caroli-de Gennes-Matricon analog states. In the presence of smooth confinement, these states create a topologically trivial skin at the wire's end that prevents the local probe from detecting quasi-MZMs. Conversely, the trivial skin disappears when true MZMs form at the edge. This renders tunneling spectroscopy a reliable MZM detection technique for full-shell hybrid nanowires in the presence of smooth disorder.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25568"></a>


### [Benchmarking bandgap prediction in semiconductors under experimental and realistic evaluation settings](http://arxiv.org/abs/2604.25568v1)

**Authors:** Haolin Wang, Xianyuan Liu, Anna Jungbluth, Alexandra J. Ramadan, Robert D. J. Oliver, Haiping Lu

**Type:** both · **Category:** disordered systems and neural networks · **PDF:** <https://arxiv.org/pdf/2604.25568v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25568_figures/2604.25568_fig1.jpg" width="500"><br>

<sub>Figure 1. Overview of the RealMat-BaG benchmark design. a, Schematic overview of the benchmark pipeline. The dataset is constructed across two fidelity levels: a computational dataset derived from the Materials Project and an experimental dataset compiled from Zhuo et al. (2018)42, BandgapDatabase128, and DS217. Two modalities, crystal structure and elemental property information, are incorporated for model training. Model performance is evaluated under an in-distribution random split as well as multiple out-of-distribution (OOD) settings. Interpretability is analyzed using graph-based gradient saliency methods for GNNs and SHapley Additive exPlanations (SHAP) for atomic feature importance...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25568_figures/2604.25568_fig2.jpg" width="500"><br>

<sub>Figure 2. Effect of computational pretraining on data efficiency and robustness in experimental bandgap prediction. a, Effect of pretraining across experimental training data fractions. Test mean relative absolute error (MRAE) of six models as a function of the fraction of available experimental training data (full training set, n = 1,534), evaluated on a fixed hold-out test set shared across all experiments. Solid lines denote models initialized with computational pretraining (the 0% point corresponds to direct transfer), whereas dashed lines indicate models without pretraining. The inset shows the mean performance across five GNN models, with shaded regions indicating the standard...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25568_figures/2604.25568_fig3.jpg" width="500"><br>

<sub>Figure 3. Model generalization under domain-based out-of-distribution (OOD) evaluation settings. a-b, Category leave-one-material-out (LOMO) evaluation with a shared color scale, where lower MRAE indicates better performance. Each cell reports the test MRAE on one held-out material category, and the value shown at the right of each row is the average across categories. In both panels, the material categories on the horizontal axis are ordered by sample count in descending order, and the number in parentheses indicates the number of compounds in that category. Panel a, shows pretrained models, whereas panel b, shows the corresponding models without pretraining and additionally includes SVR...</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25568_figures/2604.25568_fig4.jpg" width="500"><br>

<sub>Figure 4. Effect of atomic encoding across evaluation settings, and model interpretability at the structural level. Comparison of test MRAE under atomic number (Z) and elemental property (Prop) encodings across four GNN models. a, Random split. b, Feature-based out-of-distribution (OOD) split. c, Crystal-system-based split. d, Category-level leave-one-material-out (LOMO) results, shown as a heatmap of ∆MRAE (Prop −Z) to provide a clearer view of patterns across models and categories. Supplementary Table 13 reports the full results for each model and category. e, Node- and edge-level gradient saliency maps (atoms and interatomic bonds, respectively) for two representative materials SnGeS3...</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25568_figures/2604.25568_fig5.jpg" width="500"><br>

<sub>Figure 5. SHAP-based interpretation of elemental-property atomic encoding in SVR. Mean signed SHAP values for four representative input properties, averaged over 10-fold cross-validation under the random split: a, block, b, period number, c, first ionization energy, and d, electronegativity. Positive SHAP values indicate that increasing the proportion of atoms within the corresponding interval increases the predicted bandgap, whereas negative values indicate the opposite trend. Error bars represent the standard deviation across folds. The color of each point indicates the data density (non-zero proportion) within the corresponding interval, categorized as low (&lt;33%), medium (33%–67%), and...</sub>

</details>

**Main problem.**

Machine learning models trained on computational DFT data struggle to generalize to experimental semiconductor bandgap measurements due to data fidelity gaps and distribution shifts.

**Main result.**

The authors introduce RealMat-BaG, a benchmark revealing that while computational pretraining improves performance in data-scarce regimes, current models face fundamental generalization limits in specific chemical families like silicides and antimonides.

**Method.**

The study uses a new benchmark framework (RealMat-BaG) to evaluate GNNs and classical ML models across random, feature-based, and structural (LOMO) splits, incorporating SHAP and gradient saliency for interpretability.

**Summary.**

This paper addresses the reliability gap between computational material predictions and experimental reality. By introducing the RealMat-BaG benchmark, the authors systematically evaluate how well machine learning models predict semiconductor bandgaps when faced with unseen chemistries and structures. They find that while pretraining on large DFT datasets helps, certain material classes remain highly unpredictable. The work provides a roadmap for developing more robust AI tools for materials discovery.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system consists of inorganic semiconductors (oxides, chalcogenides, etc.). The models evaluated include Graph Neural Networks (CGCNN, ALIGNN, CHGNet, LEFTNet, CartNet) and classical baselines (SVR, RFR, LR).

**Key observables.**

Semiconductor bandgap (eV), Mean Relative Absolute Error (MRAE), and Mean Absolute Error (MAE).

**Important parameters / regimes.**

Chemical composition, crystal systems, and elemental properties (electronegativity, ionization energy, etc.).

**Assumptions / limitations.**

The use of CGCNN-derived embeddings as a valid proxy for the feature space; the assumption that computational pretraining can be effectively transferred to experimental domains.

**Figures summary.**

Figure 1 shows the RealMat-BaG pipeline and data distribution mismatches; Figure 2 illustrates the impact of pretraining on error across data fractions; Figure 3 shows MRAE across various OOD splits; Figure 4 compares elemental encodings and saliency maps; Figure 5 presents SHAP-based feature importance for classical models.

**Paper structure.**

Introduction of the generalization gap; presentation of the RealMat-BaG benchmark and dataset; evaluation of GNN and classical models under various OOD splits; analysis of pretraining utility; interpretability analysis via saliency and SHAP; discussion of limitations and future directions.

</details>

<details><summary>Abstract</summary>

Accurate bandgap prediction is crucial for semiconductor applications, yet machine learning models trained on computational data often struggle to generalize to experimental bandgap measurements. Challenges related to data fidelity, domain generalization, and model interpretability remain insufficiently addressed in existing evaluation frameworks. To bridge this gap, we introduce RealMat-BaG, a benchmark for assessing model reliability under experimentally relevant conditions. We curate an open-access dataset of experimental bandgaps with aligned crystal structures and compare graph neural networks as well as classical machine learning baselines. Our framework evaluates performance across statistical and domain-based splits, examines transfer from DFT-computed to experimental bandgaps, and analyzes interpretability at both elemental-property and structural levels. Our results reveal the fundamental generalization limitations of current bandgap prediction models and establish a benchmark aligned with experimental measurements for developing more reliable learning strategies for materials discovery.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25262"></a>


### [Benchmarking Universal Machine-Learned Interatomic Potentials for High-Temperature Metal-Organic Framework Chemistry](http://arxiv.org/abs/2604.25262v1)

**Authors:** Connor W. Edwards, Jack D. Evans

**Type:** theory · **Category:** disordered systems and neural networks · **PDF:** <https://arxiv.org/pdf/2604.25262v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25262_figures/2604.25262_fig1.jpg" width="500"><br>

<sub>Figure 1: a) Temperature profiles for 40 ps AIMD simulations at 300, 1000 and 2000 K. b) Initial and final structures of UiO-66 taken from a 40 ps AIMD simulation at 2000 K. Zirconium is teal, carbon is black, oxygen is red and hydrogen is pink.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25262_figures/2604.25262_fig2.jpg" width="500"><br>

<sub>Figure 2: a) RDF of initial crystalline CALF-20 MOF with RDFs from the final structures after 40 ps at 300, 1000 and 2000 K. RDFs are averaged over 50 fs. b) Analysis of CALF-20 linker size over time showing decomposition of oxalate pillar into CO2 and the azolate linker persisting during a 40 ps AIMD simulation at 2000 K.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25262_figures/2604.25262_fig3.jpg" width="500"><br>

<sub>Figure 3: Mean absolute error (MAE) in energy, force, and stress for five uMLIPs benchmarked against nine MOFs at 300, 1000, and 2000 K. a) MAE values averaged across all MOFs at each temperature. b) MAE values averaged across temperatures (300, 1000, and 2000 K) for each MOF.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25262_figures/2604.25262_fig4.jpg" width="500"><br>

<sub>Figure 4: a) Temperature profile during a 1 ns simulation produced with ORB-v3. b) Loss during the 1 ns simulation, showing agreement with AIMD validation tests at low temperature but higher loss as temperature increases.</sub>

</details>

**Main problem.**

The unreliability of universal machine-learned interatomic potentials (uMLIPs) for simulating high-temperature decomposition and non-equilibrium events in Metal-Organic Frameworks (MOFs).

**Main result.**

While ORB-v3 and fairchem OMAT perform well near equilibrium, all tested uMLIPs exhibit significant error accumulation (generative error) during high-temperature MD, failing to accurately capture structural decomposition and bond-breaking.

**Method.**

The authors generated a high-temperature benchmark dataset using 40 ps ab initio molecular dynamics (AIMD) trajectories at 300, 1000, and 2000 K and evaluated five leading uMLIPs.

**Summary.**

This paper provides a critical benchmark for universal machine-learned interatomic potentials applied to Metal-Organic Frameworks under extreme thermal conditions. By simulating MOFs at temperatures up to 2000 K, the authors demonstrate that current models fail to accurately capture the chemistry of structural decomposition and bond breaking. They highlight a significant 'validation gap' where errors during long-duration molecular dynamics far exceed errors found in static validation. The work emphasizes the need for new training datasets that include high-energy, non-equilibrium, and amorphous states.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on nine chemically diverse zinc- and zirconium-based MOFs, including ZIF-8, CALF-20, MOF-5, and UiO-66, and benchmarks models such as ORB-v3, MACE-MP-0a, and fairchem OMAT.

**Key observables.**

Energy, force, and stress Mean Absolute Errors (MAE); Radial Distribution Functions (RDF); Root Mean Square Displacement (RMSD); metal-ligand bond lengths; and gas species formation.

**Important parameters / regimes.**

Temperatures of 300 K, 1000 K, and 2000 K; 40 ps AIMD trajectories; 1 ns temperature ramp simulations.

**Assumptions / limitations.**

The study assumes that the accuracy of uMLIPs can be assessed by comparing their predictions against DFT-level reference data (PBE/DFT-D3).

**Figures summary.**

Figure 1 shows temperature profiles for the AIMD simulations and a visual comparison of the initial and final structures of UiO-66 at 2000 K.

**Paper structure.**

The paper introduces the problem of high-temperature MOF simulation, describes the generation of the AIMD benchmark dataset, presents the performance evaluation of various uMLIPs across different temperature regimes, analyzes the discrepancy between static and generative errors, and concludes with future directions for training potentials on non-equilibrium states.

</details>

<details><summary>Abstract</summary>

Universal machine-learned interatomic potentials (uMLIPs) offer a promising approach to performing atomistic simulations at near-DFT accuracy with greatly reduced computational cost. Here, we present a new high-temperature benchmarking dataset of 40~ps ab~initio molecular dynamics (AIMD) trajectories simulated at 300, 1000, and 2000 K for nine zinc- and zirconium-based metal-organic frameworks (MOFs): ZIF-8, CALF-20, MOF-10, MOF-5, MIP-206, UiO-66, UiO-67, UiO-66-NH2, and NU-1000. These trajectories capture equilibrium dynamics, thermally induced distortions, and early-stage decomposition events, including linker degradation and metal node aggregation. Subsequently, we use this dataset to benchmark five leading uMLIPs: ORB-v3, MACE-MP-0a, MACE-MPA-0, fairchem ODAC23, and fairchem OMAT. Our results reveal that ORB-v3 and fairchem OMAT achieve the lowest energy, force, and stress errors across all temperatures. However, all models exhibit significant error under high-temperature conditions. Long-timescale molecular dynamics simulations produced with ORB-v3 demonstrate that the generative error of uMLIPs far exceeds model losses captured during static validation, highlighting the limitations of current universal models for simulating high-temperature MOF dynamics. This work provides a benchmark for assessing the robustness of uMLIPs in extreme regimes and guides future development of potentials capable of accurately modeling the chemistry of high-temperature MOF dynamics.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25633"></a>


### [Binary topological logic gates in Kane-Mele nanostructures via local control of edge-state transport](http://arxiv.org/abs/2604.25633v1)

**Authors:** K. Zberecki

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25633v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25633_figures/2604.25633_fig1.jpg" width="500"><br>

<sub>Fig. 1 A localized control patch modifies the local Hamiltonian in a branched honeycomb device and redirects the dominant edge-current path between complementary outputs and . The logical input A is encoded in the inactive/active state of the patch, while the logical output is assigned from the branch receiving the dominant transmitted current. In this way, binary logic is realized by local control of edge-state transport rather than by fine-tuned interference.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25633_figures/2604.25633_fig2.jpg" width="500"><br>

<sub>Fig. 2 Generic device blueprint and notation for the Kane–Mele nanostructure family used for binary topological logic. The common multiterminal platform consists of a honeycomb-lattice scattering region connected to a source lead X, complementary logical collectors and , and an optional auxiliary drain D. Logical inputs are encoded through spatially fixed local control patches, denoted and , whose Hamiltonian parameters are switched between discrete states without changing the device geometry. The logical output is assigned from the branch receiving the dominant transmitted current. This common notation underlies both the single-patch NOT device and the two-stage AND architecture.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25633_figures/2604.25633_fig3.jpg" width="500"><br>

<sub>Fig. 3 Kane–Mele nanostructure used for the binary NOT gate. The honeycomb-lattice scattering region is connected to one source lead and two output branches. The highlighted upper and lower block patches indicate the localized regions used to shape the accessible edge-current paths; the upper patch is the input-dependent active control region, while the lower patch acts as an auxiliary static region that improves branch discrimination.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25633_figures/2604.25633_fig4.jpg" width="500"><br>

<sub>Fig. 4 Real-space current maps for the Kane–Mele NOT gate for the two binary input states. For</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25633_figures/2604.25633_fig5.jpg" width="500"><br>

<sub>Fig. 5 Geometry of the Kane–Mele nanostructure used for the binary AND gate. The highlighted internal regions mark the functional control patches: stage-A upper and lower blocking zones (orange shades) and stage-B regions associated with the collector and the complementary sector (blue and green, respectively). The device operates through sequential modification of the accessible edge-current paths inside the multiterminal nanostructure.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25633_figures/2604.25633_fig6.jpg" width="500"><br>

<sub>Fig. 6 Local current maps for the binary AND gate at the selected operating point. The four panels correspond to the input combinations , , , and . Only the configuration supports a continuous transmitting path toward the collector, whereas the remaining three cases are redirected into the complementary sector.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25633_figures/2604.25633_fig7.jpg" width="500"><br>

<sub>Fig. 7 Disorder robustness of the primitive NOT and AND gates. (a) Full-pass fraction as a function of the disorder strength W. Both gates reproduce the correct truth table for all tested disorder realizations across the entire scanned range. (b) Mean minimum margin and worst minimum margin versus . The NOT gate retains a large logical margin throughout the scan, whereas the AND gate remains logically correct but exhibits a more pronounced degradation of the margin at stronger disorder.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25633_figures/2604.25633_fig8.jpg" width="500"><br>

<sub>Fig. 8 Operating-window robustness of the primitive NOT and AND gates. (a) Minimum logical margin for the NOT gate as a function of the operating energy E and blocking amplitude . (b) Worst-case minimum logical margin for the AND gate as a function of E and the stage-A amplitude</sub>

</details>

**Main problem.**

Designing simple and physically transparent binary logic gates (NOT and AND) using topological edge states in Kane-Mele nanostructures, moving away from fine-tuned interference-based mechanisms.

**Main result.**

Demonstration of functional NOT and AND gates that operate via the controlled real-space rerouting of edge currents, showing robustness against static disorder and parameter drift.

**Method.**

Numerical transport modeling using the Landauer-Büttiker framework and the Kwant package to calculate terminal transmission and bond-current maps.

**Summary.**

This paper proposes a new way to build primitive binary logic gates using the edge states of topological insulators. Instead of relying on delicate quantum interference, the authors show that logic can be achieved by simply rerouting edge currents using local electrical or magnetic perturbations. They successfully demonstrate NOT and AND gates that are robust against small amounts of disorder. This provides a transparent and scalable framework for developing post-CMOS topological computing components.

<details><summary>Detailed structure</summary>

**Model / system.**

Kane-Mele nanostructures (honeycomb lattice) in the Quantum Spin Hall regime, featuring localized control patches with electrostatic, exchange-like, and Rashba-type perturbations.

**Key observables.**

Terminal-resolved transmission, logical margin, current maps, edge-weight diagnostic, and truth table classification rate.

**Important parameters / regimes.**

Nearest-neighbor hopping (t=1), intrinsic spin-orbit coupling (0.06), electrostatic amplitudes, and exchange-field amplitudes.

**Assumptions / limitations.**

Coherent transport regime (Landauer-Büttiker), ideal reservoirs, linear-response regime, and absence of edge roughness or finite-temperature effects.

**Figures summary.**

Fig 1: Localized control patch in a branched device. Fig 2: Device blueprint for multi-terminal platforms. Fig 3-4: NOT gate geometry and current maps showing path redirection. Fig 5-6: AND gate architecture and current redistribution. Fig 7: Stability against disorder. Fig 8: Stability against energy and amplitude drift.

**Paper structure.**

The paper introduces the problem of topological logic, describes the Kane-Mele model and control mechanisms, details the design of NOT and AND gate architectures, presents transport results and truth table validation, and concludes with robustness analysis against disorder and parameter fluctuations.

</details>

<details><summary>Abstract</summary>

Topological edge states are an attractive starting point for post-CMOS device concepts, but turning them into elementary logic still requires simple architectures with a clear physical mechanism. Here we investigate binary logic in Kane-Mele nanostructures with spatially localized control regions. Logical inputs are encoded through local electrostatic, exchange-like, and Rashba-type perturbations, while the output is read out from terminal transmission within a coherent Landauer-Büttiker framework. We demonstrate working NOT and AND gates in multiterminal honeycomb geometries and show, with the help of current maps, that their operation is governed by controlled rerouting of edge currents rather than by fine-tuned interference. Robustness tests further indicate a stable operating window within the tested parameter range for the NOT gate and a somewhat narrower but still reliable one for the AND gate. These results identify Kane-Mele nanostructures as a transparent platform for primitive topological binary logic.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25843"></a>


### [Bragg-Williams order competes with superconductivity](http://arxiv.org/abs/2604.25843v1)

**Authors:** Xu Liu, Xu Chen, Chuizhen Chen, Boqin Song, Jing Chen, Xijing Dai, Qinghua Zhang, Feng Jin, Xingya Wang, Weiwei Dong, Dongliang Yang, Gefei Li, Pengju Zhang, Jiangping Hu, Jian-gang Guo, Tianping Ying, Xiaolong Chen

**Type:** both · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25843v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25843_figures/2604.25843_fig1.jpg" width="500"><br>

<sub>FIG 1. a, Schematic of a simplified two-dimensional square model with 50% of atomic occupation,</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25843_figures/2604.25843_fig2.jpg" width="500"><br>

<sub>FIG 2. a, HAADF image and b, indexed SAED image of O-phase. c, Crystal structure of the O-phase. d,</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25843_figures/2604.25843_fig3.jpg" width="500"><br>

<sub>FIG 3. Temperature-dependent resistance of the a-b, O- and c-d, D-phases of In2/3PSe3 with the variation</sub>

</details>

**Main problem.**

The study aims to understand how Bragg-Williams order (BWO), a classical structural order parameter, influences superconductivity and whether it acts as an independent competing order.

**Main result.**

The researchers found that the disordered phase of In2/3PSe3 achieves a significantly higher superconducting transition temperature (11 K) than the ordered phase (7 K), demonstrating that BWO suppresses superconductivity by stiffening phonon modes.

**Method.**

The study combines experimental techniques like high-pressure transport, Raman spectroscopy, and STEM with theoretical frameworks including Ginzburg-Landau phenomenological analysis and BCS-McMillan microscopic theory.

**Summary.**

This paper investigates the competition between structural vacancy ordering and superconductivity in In2/3PSe3. By using thermal treatment to tune the Bragg-Williams order without changing chemical composition, the authors show that a disordered lattice promotes a higher superconducting Tc. The mechanism is identified as a reduction in electron-phonon coupling due to lattice stiffening in the ordered phase. This work extends the concept of competing orders to include classical structural parameters.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system is In2/3PSe3, a member of the MPSe3 family, which can be switched between an ordered (O-phase) and disordered (D-phase) state via thermal treatment.

**Key observables.**

Superconducting transition temperature (Tc), Bragg-Williams order parameter (eta), electron-phonon coupling (lambda), Hall resistance, and Raman-active modes.

**Important parameters / regimes.**

Pressure (up to ~37 GPa), temperature, and the vacancy order parameter (eta).

**Assumptions / limitations.**

The thermodynamic analysis uses a classical solid solution model considering only nearest-neighbor interactions.

**Figures summary.**

Figure 1 shows BWO schematics and crystal structures; Figure 2 displays STEM and SAED images of the O and D phases; Figure S6-S9 include superconducting transitions under magnetic fields, resistance vs. temperature, and Hall resistance.

**Paper structure.**

The paper introduces the BWO concept, describes the experimental platform and phase control, presents high-pressure transport and structural results, provides the theoretical mechanism for competition via phonon stiffening, and concludes with thermodynamic modeling of the order-disorder transition.

</details>

<details><summary>Abstract</summary>

Orderings in charge and spin have been extensively studied to unravel their correlation to emergent superconductivity over the past decades. Bragg-Williams order (BWO), a classical structural order parameter describing site occupancy in alloys, has long been speculated to influence superconducting behavior. Yet, its role still remains ambiguous, largely due to the difficulty of isolating BWO from concomitant charge doping or competing electronic instabilities. Here, we establish In2/3PSe3 as a platform wherein indium vacancies are reversibly configurable between ordered and disordered states via thermal treatment. We show that the disordered phase undergoes a pressure-induced superconducting transition with a Tc of 11 K, significantly higher than the 7 K observed in its ordered counterpart. This constitutes a rare instance in which pure BWO variation drives a substantial shift in Tc. By combining a Ginzburg-Landau phenomenological analysis with a BCS-McMillan microscopic description, we demonstrate that BWO naturally suppresses superconductivity through electron-phonon interactions, a mechanism supported by ultra-low-wavenumber Raman measurements. Our findings support BWO as an independent order parameter that competes directly with superconductivity, extending the concept of competing orders beyond conventional electronic and magnetic degrees of freedom.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25718"></a>


### [Chemical transformation of MgH2/V2O5 composite to Mg-V-O rock salt and its influence on the electrochemical Li conversion and hydrogen storage characteristics of MgH2](http://arxiv.org/abs/2604.25718v1)

**Authors:** D. Pukazhselvan, Ihsan Caha, Francisco J. A. Loureiro, Francis Leonard Deepak, Catarina de Lemos, Aliaksandr L. Shaula, Sergey M. Mikhalev, Duncan Paul Fagg

**Type:** experiment · **Category:** other · **PDF:** <https://arxiv.org/pdf/2604.25718v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25718_figures/2604.25718_fig1.jpg" width="500"><br>

<sub>Fig.1 XRD profiles obtained for the15h ball milled xMgH2+V2O5 (x=0, 0.125, 0.25, 0.5, 2, 4, 6, 8 and 10) composite (V2O5 correspond to x=0).</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25718_figures/2604.25718_fig2.jpg" width="500"><br>

<sub>Fig.2 XPS (a) survey spectra corresponding to xMgH2+V2O5 (x=0.125, 2 and 4). The V2p and O1s high resolution binding energy profiles obtained for the samples, (b) 0.125MgH2+V2O5, (c) 2MgH2+V2O5 and (d) 4MgH2+V2O5.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25718_figures/2604.25718_fig3.jpg" width="500"><br>

<sub>Fig.3 Cyclic voltammetry profiles corresponding to the battery employing (a) 5 wt.% V2O5 added MgH2 as anode active material (battery “A”), (b) 5 wt.% MgxVyOx+y added MgH2 as anode active material (battery “B”), (c) carbon substrate alone as anode active material and (d) pure MgH2 (additive free) as anode active material. Five cycles charge/discharge profiles corresponding to (e) battery “A” and, (f) battery “B”.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25718_figures/2604.25718_fig4.jpg" width="500"><br>

<sub>Fig.4 XRD profiles corresponding to (a) the fresh anode used in battery “A”, (b) recovered anode from “A” after first discharge, (c) recovered anode from “A” after 5th charging cycle, (d) the fresh anode used in battery “B”, (e) recovered anode from “B” after first discharge, (f) recovered anode from “B” after 5th charging cycle. The XRD profile of Cu current collector is provided for comparison.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25718_figures/2604.25718_fig5.jpg" width="500"><br>

<sub>Fig.5 SEM / EDX profiles of anodes employed in battery “A”. Images (a), (b), (c) and (d), fresh anode (surface and cross sections). Images d1, d2, d3 and d4 correspond to EDS maps of cross section region given in “(d)” (d1 is collective distribution of Mg, V, Pt and O, d2 is Pt alone, d3 is Mg alone and d4 is O). In similar sequence images, (e), (f), (g), (h), h1, h2, h3 and h4 correspond to SEM/EDX of electrode recovered from battery “A” after first discharge. The images (i), (j), (k), (l), l1, l2, l3 and l4 correspond to SEM/EDX of electrodes recovered from battery “A” after fifth recharge cycle.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25718_figures/2604.25718_fig6.jpg" width="500"><br>

<sub>Fig.6 SEM / EDX profiles of anodes employed in battery “B”. Images (a), (b), (c) and (d), fresh anode (surface and cross sections). Images d1, d2, d3 and d4 correspond to EDS maps of cross section region given in “(d)” (d1 is collective distribution of Mg, V, Pt and O, d2 is Pt alone, d3 is Mg alone and d4 is O). In similar sequence images, (e), (f), (g), (h), h1, h2, h3 and h4 correspond to SEM/EDX of electrode recovered from battery “B” after first discharge. The images (i), (j), (k), (l), l1, l2, l3 and l4 correspond to SEM/EDX of electrodes recovered from battery “B” after fifth recharge cycle.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25718_figures/2604.25718_fig7.jpg" width="500"><br>

<sub>Figure 7 – (a1), (b1), and (c1) Complex plane impedance spectra obtained for the fleshly-made batteries (the high-magnification inset includes the subtracted polarization branch. The numbers represent the decades (log10f) of the measuring frequency); (a2), (b2), and (c2) the corresponding DFRTs of the polarization branch.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25718_figures/2604.25718_fig8.jpg" width="500"><br>

<sub>Figure 8 – (a1), (b1), and (c1) Complex plane impedance spectra obtained for the 5 cycles batteries (the high-magnification inset includes the subtracted polarization branch. The numbers represent the decades (log10f) of the measuring frequency); (a2), (b2), and (c2) the corresponding DFRTs of the polarization branch.</sub>

</details>

**Main problem.**

Investigating the chemical transformation of MgH2/V2O5 composites into a Mg-V-O rock salt phase and understanding how this interaction affects the electrochemical Li conversion and capacity degradation in Li-ion battery anodes.

**Main result.**

The in-situ formation of a Mg-V-O rock salt phase significantly enhances the initial discharge capacity (up to 1350 mAh/g), but the system still suffers from limited reversibility due to slow charge transfer processes and surface blockage rather than electrolyte degradation or physical swelling.

**Method.**

The study uses planetary ball milling for synthesis, XRD and XPS for structural/chemical characterization, and electrochemical techniques including CV, EIS, and Distribution of Relaxation Times (DRFT) for performance analysis.

**Summary.**

This paper explores how adding vanadium oxide to magnesium hydride creates a new Mg-V-O rock salt phase during processing. This new phase improves the initial lithium discharge capacity in battery anodes. However, the researchers found that the battery still struggles with poor reversibility, which they traced to slow charge transfer and surface blockage rather than physical damage to the material. This work is important for developing more stable high-capacity anode materials for lithium-ion batteries.

<details><summary>Detailed structure</summary>

**Model / system.**

The experimental platform consists of Li-ion coin cells using MgH2-based anodes doped with varying concentrations of V2O5 or the in-situ formed Mg-V-O rock salt phase, with a Li metal counter electrode and 1M LiPF6 in EC/DMC electrolyte.

**Key observables.**

Electrochemical capacity (discharge/recharge), oxidation states of Vanadium, polarization resistance (Rp), ohmic resistance (Rohm), and charge transfer resistance components.

**Important parameters / regimes.**

Additive concentrations (0 to 10 wt.%), discharge/recharge capacity (mAh/g), and time constants/capacitance in the impedance spectra.

**Assumptions / limitations.**

The study assumes that the observed capacity loss is not due to electrolyte degradation or physical detachment of the active material, based on constant ohmic resistance and post-mortem SEM/EDX analysis.

**Figures summary.**

Figures include SEM and EDX maps showing the morphology and elemental distribution of anodes at different cycling stages, and EIS data comparing resistance components for different additive compositions.

**Paper structure.**

The paper begins with the synthesis and structural characterization of the composites, followed by electrochemical performance testing, detailed impedance analysis using DRFT to identify degradation mechanisms, and post-mortem morphological analysis.

</details>

<details><summary>Abstract</summary>

This study investigates the lithium conversion behavior of a hydrogen storage material based on vanadium oxide added magnesium hydride. To understand the chemical interaction between vanadium oxide and magnesium hydride, detailed X ray diffraction and X ray photoelectron spectroscopy analyses were performed on ball milled composites with varying compositions. The results confirm the formation of a combined magnesium vanadium oxide with a rock salt structure, indicating strong chemical interaction between the components. It is further shown that the presence of a small amount of this oxide additive significantly influences the lithium reaction with magnesium hydride, leading to a high initial discharge capacity and limited recharge capacity in lithium ion coin cells. Post use analyses confirm the presence of magnesium hydride, suggesting that volume expansion is not responsible for the observed irreversibility. Electrochemical impedance spectroscopy using differential function of relaxation times indicates that electrolyte degradation is not a major issue. Instead, slow charge transfer processes are identified as the limiting factor, and these are sensitive to the composition of the additive. These findings highlight that improving electrode and electrolyte compatibility is essential for enhancing performance in this system.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25428"></a>


### [Determination of Burgers vectors of dislocations in monoclinic $β$-Ga$_2$O$_3$ crystals by large-angle convergent-beam electron diffraction](http://arxiv.org/abs/2604.25428v1)

**Authors:** Yoshihiro Sugawara, Yongzhao Yao, Yukari Ishikawa

**Type:** experiment · **Category:** other · **PDF:** <https://arxiv.org/pdf/2604.25428v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25428_figures/2604.25428_page2.jpg" width="500"><br>

<sub>Low-resolution page preview, page 2</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25428_figures/2604.25428_page3.jpg" width="500"><br>

<sub>Low-resolution page preview, page 3</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25428_figures/2604.25428_page4.jpg" width="500"><br>

<sub>Low-resolution page preview, page 4</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25428_figures/2604.25428_page5.jpg" width="500"><br>

<sub>Low-resolution page preview, page 5</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25428_figures/2604.25428_page6.jpg" width="500"><br>

<sub>Low-resolution page preview, page 6</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25428_figures/2604.25428_page7.jpg" width="500"><br>

<sub>Low-resolution page preview, page 7</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25428_figures/2604.25428_page8.jpg" width="500"><br>

<sub>Low-resolution page preview, page 8</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25428_figures/2604.25428_page9.jpg" width="500"><br>

<sub>Low-resolution page preview, page 9</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25428_figures/2604.25428_page10.jpg" width="500"><br>

<sub>Low-resolution page preview, page 10</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25428_figures/2604.25428_page11.jpg" width="500"><br>

<sub>Low-resolution page preview, page 11</sub>

</details>

**Main problem.**

The difficulty of accurately determining the Burgers vectors (direction, magnitude, and sense) of dislocations in the non-orthogonal monoclinic crystal structure of beta-Ga2O3.

**Main result.**

The researchers successfully demonstrated that Large-Angle Convergent-Beam Electron Diffraction (LACBED) can be used to unambiguously determine Burgers vectors in beta-Ga2O3, identifying a consistent Burgers vector of b = [010] for dislocations introduced by nanoindentation.

**Method.**

The study uses nanoindentation to introduce dislocations, followed by TEM analysis using LACBED and Weak-Beam Dark-Field (WBDF) imaging, employing a dual-basis mathematical framework to calculate vector inner products without a metric tensor.

**Summary.**

This paper presents a method for determining the Burgers vectors of dislocations in beta-Ga2O3, a material critical for high-voltage power electronics. By using Large-Angle Convergent-Beam Electron Diffraction (LACBED), the authors bypassed the need for a complex metric tensor calculation in non-orthogonal crystal systems. They successfully identified the Burgers vector of nanoindentation-induced dislocations as [010]. The results were validated using Weak-Beam Dark-Field imaging, proving LACBED is an effective tool for characterizing defects in this material.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system consists of monoclinic beta-Ga2O3 single-crystal wafers (Sn-doped) containing dislocations (D-1 through D-8) generated via Berkovich nanoindentation.

**Key observables.**

LACBED node counts (n), dislocation contrast in WBDF images, and reciprocal lattice vectors (g).

**Important parameters / regimes.**

Dislocation density of approximately 10^4 cm^-2, electron beam energy of 200 kV, and nanoindentation load of 50 mN.

**Assumptions / limitations.**

The method assumes the validity of the dual relationship between real and reciprocal lattice bases for non-orthogonal systems and uses the Cherns-Preston rule for sign determination.

**Figures summary.**

Fig 1 shows a BF-STEM image of the indentation site and strain fields; Fig 2 displays LACBED patterns with identified node counts; Fig 3 shows WBDF images demonstrating dislocation contrast under different g-vectors.

**Paper structure.**

The paper introduces the problem of dislocation characterization in beta-Ga2O3, describes the experimental setup (nanoindentation and TEM), presents the mathematical framework for LACBED in monoclinic systems, details the results of Burgers vector determination, and validates the findings against WBDF imaging.

</details>

<details><summary>Abstract</summary>

We demonstrate the applicability of large-angle convergent-beam electron diffraction (LACBED) for Burgers vector determination in monoclinic $β$-Ga$_2$O$_3$. The inner product $g \cdot b$ in this non-orthogonal system can be evaluated without a metric tensor by using the dual relationship between real and reciprocal lattice bases. Based on this framework, Burgers vectors of dislocations introduced by nanoindentation were unambiguously determined from LACBED node counts. The results are consistent with weak-beam dark-field imaging, confirming the effectiveness of LACBED for $β$-Ga$_2$O$_3$.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24967"></a>


### [Entropic Trapping of Hard Spheres in Spherical Confinement](http://arxiv.org/abs/2604.24967v1)

**Authors:** Praveen K. Bommineni, Junwei Wang, Nicolas Vogel, Michael Engel

**Type:** both · **Category:** statistical mechanics · **PDF:** <https://arxiv.org/pdf/2604.24967v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.24967_figures/2604.24967_fig1.jpg" width="500"><br>

<sub>FIG. 1. Examples demonstrating templating of icosahe- dral clusters. (a) Schematic representation of a mixture of many small particles and a few large particles in an emulsion droplet. (b) Scanning electron microscopy observation of the successful diffusion of five large polystyrene colloidal parti- cles (red) into the vertices of the icosahedral cluster. (c) Co- assembly of two types of grafted nanoparticles into a patchy icosahedron in a drying emulsion droplet [29]. Reprinted with permission from AAAS. (d) Molecular crystallization and seg- regation of anionic and cationic surfactants [30]. Copyright 2004 by the National Academy of Sciences.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24967_figures/2604.24967_fig2.jpg" width="500"><br>

<sub>FIG. 2. Layering in confined hard sphere fluids. The left side shows the evolution of radial distance from the confinement center of a randomly chosen test sphere, while the right side displays shell packing fraction profiles in thin spherical shells obtained by averaging over many frames. Insets show typical cross-sectional views of the confined fluids. Clusters are shown at three packing fractions: (a) ϕ = 0.30, (b) ϕ = 0.40, and (c) ϕ = 0.50. Note that layering persists throughout the entire cluster in (c), even though this cluster is not yet crystalline. Simulations were performed with N = 2000 spheres.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24967_figures/2604.24967_fig3.jpg" width="500"><br>

<sub>FIG. 3. Twelve large spheres form a perfect icosahedral frame. (a) Large spheres hop between shells increasing total free volume, which tracks crystallization progress. (b) Histogram showing the evolution of large sphere separations as they settle into the icosahedral frame. Simulation snapshots show: (c) Initial setup with large spheres positioned at the confinement center; (d) Outward diffusion of large spheres; (e) Intermediate state showing a partially formed icosahedral frame; (f) Completed icosahedral frame at the end of the trajectory. EDMD simulations were conducted with NL = 12 large and NS = 1288 small spheres at fluid-solid coexisting packing fraction ϕ = 0.53 and for sphere size...</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24967_figures/2604.24967_fig4.jpg" width="500"><br>

<sub>FIG. 4. Quantification of entropic trapping. (a) Free energy profiles of a single large test particle in a system of NS = 1299 small spheres as a function of radial distance. Radial distance is measured from the confinement center and normalized by the distance accessible to the test sphere. Simulation parameters are α = 0.55 and ϕ ∈[0.30, 0.35, . . . , 0.50] (labelled on the right); the inset corresponds to ϕ = 0.53. For ϕ ≥0.5, we performed ten simulations for each biasing bin to improve statistics. Solid lines are a guide to the eye. Error bars indicate standard errors. (b) Two-dimensional free energy profile on the cluster surface. (c) Simulated cluster with twelve large spheres (red)...</sub>

</details>

**Main problem.**

Understanding the mechanism behind the 'entropic trapping' of large impurity particles at the vertices of icosahedral colloidal clusters under spherical confinement.

**Main result.**

Large spheres are driven by entropic forces from the center to the cluster surface, where they settle into deep free energy minima at icosahedral vertices, forming a stable icosahedral frame.

**Method.**

Event-driven molecular dynamics (EDMD) for trajectories and Monte Carlo umbrella sampling with the Weighted Histogram Analysis Method (WHAM) for free energy landscapes.

**Summary.**

This study investigates how large impurity particles are trapped at the vertices of icosahedral clusters in confined hard-sphere systems. Using molecular dynamics and free energy calculations, the authors show that entropic forces drive these impurities to the surface of the cluster. The findings demonstrate that the particles settle into specific energy minima, creating a robust icosahedral frame. This mechanism provides insight into the self-assembly of complex structures in soft matter and potentially biological systems like viral capsids.

<details><summary>Detailed structure</summary>

**Model / system.**

A binary mixture of monodisperse small hard spheres and a small number of larger hard spheres confined within a hard spherical cavity (simulating emulsion droplets).

**Key observables.**

Radial distance, shell packing fraction, total free volume, dimensionless pressure (P*), mean squared displacement (MSD), and spatial separation histograms.

**Important parameters / regimes.**

Size ratio (alpha = 0.55), packing fraction (phi ranging from 0.30 to 0.53), and particle numbers (N_S = 1288, N_L = 12).

**Assumptions / limitations.**

The trapping effect is predominantly entropic due to the hard-sphere nature; the system is in a regime where particles can relax into minimum free energy positions.

**Figures summary.**

Figure 1 shows experimental/schematic motivation; Figure 2 shows the transition from fluid to layered structures; Figure 3 illustrates the progression of large spheres forming an icosahedral frame; Figure 4 quantifies radial and surface free energy profiles.

**Paper structure.**

The paper introduces the experimental phenomenon, describes the hard-sphere model and simulation methods, presents results on structural evolution and layering, quantifies the entropic driving forces via free energy, and concludes with a derivation of the virial pressure for the system.

</details>

<details><summary>Abstract</summary>

Monodisperse spherical colloidal particles confined within emulsion droplets can crystallize into icosahedral clusters. Experimentally it was observed that a few large colloidal particles added as defects preferentially migrate to the vertices of the icoshedral clusters. To understand this structure formation phenomenon, we simulate the confined self-assembly of hard spheres in the presence of a small number of larger particles. The results demonstrate that large spheres are significantly influenced by concentric shells of small spheres near the crystallization transition. Entropic forces drive the large spheres to the cluster surface, where they settle into free energy minima at the icosahedron vertices. Notably, the addition of twelve large spheres results in the formation of a perfect icosahedral frame. Free energy calculations via umbrella sampling are used to quantify this process and show that both the migration to the cluster surface and the trapping at the vertices with trapping strength of multiple $k_\text{B}T$ results from free energy minimization. Moreover, our study reveals that the crystallization pathway and dynamics of large spheres are consistent across different systems, suggesting robustness of entropic trapping.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25460"></a>


### [Excitation of Low-Frequency Modes and the Effects of Protein Dynamics on Spectral Densities of Bacteriochlorophyll Molecules](http://arxiv.org/abs/2604.25460v1)

**Authors:** Sayan Maity, Tristan A. Mauck, Ulrich Kleinekathöfer

**Type:** theory · **Category:** other · **PDF:** <https://arxiv.org/pdf/2604.25460v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25460_figures/2604.25460_fig1.jpg" width="500"><br>

<sub>Figure 1. Two-dimensional chemical structure of the BChl pigment (which is actually a BChl a) present</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25460_figures/2604.25460_fig2.jpg" width="500"><br>

<sub>Figure 2. (A) Gas phase spectral density of the BChl molecule derived from the average of 10 NVE tra-</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25460_figures/2604.25460_fig3.jpg" width="500"><br>

<sub>Figure 3. LH2 complex from the purple bacterium Rs. molischianum (PDB code: 1LGH), showing the</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25460_figures/2604.25460_fig4.jpg" width="500"><br>

<sub>Figure 4. Spectral densities of the studied BChl pigment from the B800 (A, C) and the B850 (B, D) rings</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25460_figures/2604.25460_fig5.jpg" width="500"><br>

<sub>Figure 5. The HOMO and LUMO of the BChl pigments in the B800 and B850 rings were analyzed</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25460_figures/2604.25460_fig6.jpg" width="500"><br>

<sub>Figure 6. An example of the trimeric FMO complex from the green sulfur bacterium C. tepidum (PDB</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25460_figures/2604.25460_fig7.jpg" width="500"><br>

<sub>Figure 7. Spectral densities of a BChl pigment in the FMO complex based on DFTB/MM MD (A) and</sub>

</details>

**Main problem.**

The study addresses the failure of classical molecular dynamics and normal mode analysis to accurately capture low-frequency intramolecular vibrational modes of bacteriochlorophyll molecules, which are crucial for exciton transfer.

**Main result.**

The authors demonstrate that Born-Oppenheimer molecular dynamics (BOMD) using the DFTB approach accurately recovers low-frequency spectral density contributions from both protein fluctuations and intrinsic pigment vibrations, whereas classical methods miss the latter.

**Method.**

The researchers use a QM/MM framework employing Born-Oppenheimer molecular dynamics (BOMD) based on density functional-based tight-binding (DFTB3) and compare it with classical MD and Normal Mode Analysis (NMA).

**Summary.**

This paper investigates how low-frequency vibrations in bacteriochlorophyll molecules contribute to the spectral density in photosynthetic complexes. It shows that traditional classical MD and normal mode analysis fail to capture important intrinsic molecular vibrations. By using Born-Oppenheimer molecular dynamics with a tight-binding approach, the authors successfully model both protein-driven and pigment-intrinsic low-frequency modes. This finding is significant for accurately simulating exciton transfer in biological light-harvesting systems.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on light-harvesting complexes, specifically the B800 and B850 rings of the LH2 complex from purple bacteria and the FMO complex from green sulfur bacteria, modeled using a Frenkel Hamiltonian.

**Key observables.**

Spectral densities (J(omega)), site energy fluctuations, reorganization energies, and Huang-Rhys factors.

**Important parameters / regimes.**

Low-frequency vibrational modes (below 235 cm-1), excitation energy gaps, and the influence of the protein electrostatic environment.

**Assumptions / limitations.**

The DFTB method is semi-empirical and may overestimate reorganization energies; the study also notes that the accuracy of intramolecular modes is sensitive to the choice of classical force fields.

**Figures summary.**

Figures include structural representations of the LH2 complex, comparisons of spectral densities across different methods, and analysis of the impact of the protein environment on pigment excitation energies.

**Paper structure.**

The paper introduces the problem of low-frequency mode modeling, describes the QM/MM and BOMD methodology, presents gas-phase benchmarking, extends the analysis to the LH2 and FMO complexes, and concludes with a discussion on environmental impacts and methodological limitations.

**Why it may be interesting.**

This paper is highly relevant to open quantum systems researchers as it provides a more accurate way to model the spectral density of the bath, which is a fundamental input for describing decoherence and energy transfer in biological quantum dynamics.

</details>

<details><summary>Abstract</summary>

In the theory of open quantum systems, spectral densities are key quantities for modeling the dynamics and spectroscopic properties of the system under investigation. In the case of light-harvesting complexes, they encode the frequency-dependent coupling of electronic excitations in pigment molecules to their environment, reflecting contributions from both intrinsic vibrational modes and the protein surrounding. In particular, the low-frequency components of the spectral densities are crucial for exciton transfer between pigment molecules. Apparently, slow internal modes of bacteriocholophyll molecules in the gas phase are less well represented by common force fields based on classical molecular dynamics (MD) simulations. Here, we demonstrate that Born-Oppenheimer molecular dynamics (BOMD) based on the numerically efficient density functional-based tight-binding approach can accurately recover these low-frequency features, whereas normal mode analysis captures them only partially. In contrasting approaches for determining spectral densities, the low-frequency region of the spectral densities obtained is only associated with protein fluctuations; the usage of BOMD, however, also captures the low-frequency contributions arising from slow intramolecular vibrations of the pigment molecules themselves. Notably, this behavior is consistently observed for both the flexible B800 and the more rigid B850 rings in light-harvesting 2 (LH2) complexes of purple bacteria, as well as in the Fenna-Matthews-Olson (FMO) complex of green sulfur bacteria. Interestingly, we also find that the spectral densities of the pigments in the B850 ring of LH2 are not influenced by the environment, i.e., the gaps between ground and first excited state are not changed significantly by the fluctuations of the protein environment.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25497"></a>


### [Fundamental picture of the conduction mechanism in solid-state polymer electrolytes revealed by terahertz spectroscopy](http://arxiv.org/abs/2604.25497v1)

**Authors:** Johanna Weidelt, Jijeesh Ravi Nair, Diddo Diddens, Wentao Zhang, Felix Pfeiffer, Tiago de Oliveira Schneider, Markus Meinert, Tomoki Hiraoka, Linda Nesterov, Masoud Baghernejad, Dmitry Turchinovich, Hassan A. Hafez

**Type:** both · **Category:** disordered systems and neural networks · **PDF:** <https://arxiv.org/pdf/2604.25497v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25497_figures/2604.25497_fig1.jpg" width="500"><br>

<sub>Fig. 1. Schematic illustration of the hopping charge transport in PEO-based electrolytes: intra- and interchain hopping, ei- ther direct or mediated by the salt anions. Black lines represent the PEGDAE chains with the small blue dots corresponding to the comprised oxygen atoms (the chemical structure of PEGDAE is shown on the bottom left). The chemical structure of the anions depends on the comprised salt. Red dashed lines indicate cross-linking.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25497_figures/2604.25497_fig2.jpg" width="500"><br>

<sub>Fig. 2. (a) Real and (b) imaginary part of the frequency-dependent conductivity spectra of bare cross-linked polymer (X), single salt electrolytes (XS1 (LiTFSI) and XS2 (LiDFOB)) and dual salt electrolyte (X(S1+S2) (LiTFSI+LiDFOB)). Symbols for data points obtained by the broadband spintronic emitter, and solid lines to the Lorentzian fit. The error-bars are derived from the thickness uncertainty of the samples along with the standard error of the mean of the data acquired in repeated measurements. (c) Schematic of the dynamics associated with the resonance frequencies: the twisting motion of the poly- mer backbone and the breathing movement of the crown-like oxygen shell around the 𝐋𝐢+....</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25497_figures/2604.25497_fig3.jpg" width="500"><br>

<sub>Fig. 3: DFT predicted resonances with snapshots depicting the associated clusters being a PEO hexamer (a) and Li+ together with the anions TFSI (b) or DFOB (c). Hydrogen atoms have been omitted for clarity. The frequencies associated with the twisting motion of the polymer backbone are marked by black squares while the ones linked to the breathing movement of the crown-ether-like oxygen shell around the 𝐋𝐢+ are represented by black stars.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25497_figures/2604.25497_fig4.jpg" width="500"><br>

<sub>Fig. 4: Temperature-dependent real-valued conductivity. For each sample, the real-valued conductivity spectra as function of frequency at different temperatures are shown in the respective upper panel, while the temperature dependence of the conductivity at selective frequencies indicated by the vertical colored lines is shown in the respective lower panel. [(a), (e)] for X(0), [(b), (f)] for XS1, [(c), (g)] for XS2, and [(d), (h)] for X(S1+S2). Symbols for the data and solid lines for the Lorentz model fitting.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25497_figures/2604.25497_fig5.jpg" width="500"><br>

<sub>Fig. 5: Temperature- and sample dependent Lorentzian fit parameters: (a) the low-frequency resonance 𝒇𝟎,𝟏, (b) the asso- ciated damping rate 𝜸𝟏, (c) the damping rate 𝜸𝟐 belonging to the high frequency resonance 𝒇𝟎,𝟐, and (d) high-frequency dielectric constant. The lines are guide-to-the-eye.</sub>

</details>

**Main problem.**

Understanding the fundamental conduction mechanism and molecular dynamics in solid-state polymer electrolytes (SPEs) and how salt addition affects lithium-ion transport.

**Main result.**

The study identifies that low-frequency polymer vibrations, specifically the twisting of the PEO backbone and the breathing of the Li+ coordination shell, facilitate lithium-ion hopping transport.

**Method.**

Terahertz time-domain spectroscopy (THz-TDS) was used for broadband and temperature-dependent measurements, complemented by Density Functional Theory (DFT) calculations and Electrochemical Impedance Spectroscopy (EIS).

**Summary.**

This paper investigates the conduction mechanism in solid-state polymer electrolytes using terahertz spectroscopy. By analyzing vibrational modes, the researchers show that the movement of the polymer backbone and the coordination shell around lithium ions are directly linked to ionic conductivity. The study uses a combination of THz-TDS, temperature-dependent studies, and DFT calculations to provide a microscopic picture of ion hopping. These findings are crucial for improving the performance of solid-state lithium batteries.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system consists of cross-linked poly(ethylene oxide) (PEO) electrolytes doped with lithium salts (LiTFSI, LiDFOB). The analysis uses a Lorentz oscillator model to describe resonant vibrational modes and DFT to assign molecular motions.

**Key observables.**

THz conductivity spectra, complex refractive index, absorption coefficient, dielectric function, and ionic conductivity.

**Important parameters / regimes.**

Temperature (10 K to 300 K), salt concentration (wt%), and frequency range (0.1 to 8 THz).

**Assumptions / limitations.**

The Drude model was rejected as unsuitable for the observed conductivity; the analysis assumes the absence of significant Fabry-Perot etalon multi-reflections in the THz-TDS measurements.

**Figures summary.**

Fig 1 shows a schematic of Li+ hopping; Fig 2 presents THz conductivity spectra and vibrational mode dynamics; Fig 3 shows DFT-predicted resonances and molecular clusters; Fig 4 displays temperature-dependent conductivity spectra.

**Paper structure.**

The paper introduces the problem of SPE conduction, describes the experimental THz-TDS and cryogenic setups, presents the results of salt-dependent and temperature-dependent conductivity, validates vibrational modes via DFT, and concludes with the correlation between THz vibrations and macroscopic ion transport.

</details>

<details><summary>Abstract</summary>

Solid polymer electrolytes (SPEs) based on cross-linked poly(ethylene oxide) (PEO) encompassing lithium salts have gained significant attention as separators in solid-state lithium metal batteries. Here, we employ terahertz time-domain spectroscopy (THz-TDS), as a noninvasive contact-free technique, to investigate the conduction properties of these cross-linked SPEs and unravel their dependencies on the added lithium salt and the sample temperature. The obtained THz conductivity spectra are dominated by THz absorption bands, which we attribute to resonant vibrations within the polymer matrix of the electrolyte. By careful application of Lorentz model, the conductivity spectra have been analyzed, and the relevant polymer vibration modes have been quantitatively assessed. Calculations based on the density functional theory (DFT) were performed to elucidate the possible microscopic mechanisms of these resonant vibrations. This study sheds light on the relevance of polymer matrix vibrations validating the hopping transport of lithium ions in SPEs which ultimately leads to the technologically relevant ionic conduction in the solid-state polymer-based electrolytes.

</details>

<sub>[↑ back to top](#top)</sub>
