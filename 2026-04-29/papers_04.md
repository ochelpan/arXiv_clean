# Daily arXiv Report

[← Index](index.md)

[← Previous](papers_03.md)
[Next →](papers_05.md)

## Papers 61–80


<a id="paper-2604.25863"></a>


### [MCMit: Mid-Circuit Measurement Error Mitigation](http://arxiv.org/abs/2604.25863v1)

**Authors:** Emmanouil Giortamis, Felix Gust, Aleksandra Świerkowska, Sandra Stankovic, Innocenzo Fulginiti, Yanbin Chen, Xiaorang Guo, Benjamin Lienhard, Martin Schulz, Pramod Bhatotia

**Type:** both · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25863v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `QC/QI experiment` **4/5** · `quantum measurements` **3/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25863_figures/2604.25863_fig1.jpg" width="500"><br>

<sub>Figure1:Superconductingreadout(§2.1). (a)SuperconductingqubitreadoutpipelineonanFPGAcontroller.(b)TheMCMinatele- portation circuit can produce a readout trace of 1𝜇𝑠: 500 samples spaced 2ns apart. (c) The readout trace is input to a Feed-forward Neural Network comprising N layers. The network discriminates 0 and 1 using a decision boundary that separates the states.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25863_figures/2604.25863_fig2.jpg" width="500"><br>

<sub>Figure 2: MECH [112] performance analysis. (a) Impact of MCM errors as a ratio to the 2-qubit gate errors. (b) Impact of MCM latency as a ratio to the 2-qubit gate latency. (c) Impact of classical feedback latency as a ratio to the 2-qubit gate latency. There is a linear performance improvement with MCM error and (classical) latency reduction.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25863_figures/2604.25863_fig3.jpg" width="500"><br>

<sub>Figure 3: Logical error rate of the surface code on the Google Sycamore architecture [6]. (a) Increasing with the MCM error rate. (b) Increasing with the MCM duration. Green marks durations available with MCMit; red marks those available with HERQULES [68].</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25863_figures/2604.25863_fig4.jpg" width="500"><br>

<sub>Figure 5: MCMit workflow (§ 4.2). (a) Compile-time workflow and (b) runtime workflow.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25863_figures/2604.25863_fig5.jpg" width="500"><br>

<sub>Figure 4: MCMit overview (§ 4). MCMit comprises the error mitigation software and the FPGA controller.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25863_figures/2604.25863_fig6.jpg" width="500"><br>

<sub>Fig. 5 shows the compile-time and runtime workflows of MCMit. The software layer operates only at compile-time, while the FPGA controller layer operates only at runtime. Compile-time workflow. To apply the first stage to the input quan- tum circuit, dynamic circuit simplification, we execute three sub- stages: (1) we identify and remove up to 𝑀MCMs, where 𝑀dictates the computational complexity of our static analysis tool, and (2), we simplify the control logic that is based on those MCMs. This removes some operands (e.g., XOR) in subsequent branch instructions or elim- inates the branches entirely, effectively reducing classical latency. (3) We apply the measurement hardening pass, which...</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25863_figures/2604.25863_fig7.jpg" width="500"><br>

<sub>Fig. 4 shows the MCMit architecture, comprising the MCMit soft- ware layer for circuit-level error mitigation and the MCMit FPGA controller, which integrates the fast multi-qubit branching logic and the high-accuracy qubit-state discriminator model. Fastclassicalfeedback.MCMitintroducesafastmulti-qubitbranch instruction, which executes scalable conditional logic based on the</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25863_figures/2604.25863_fig8.jpg" width="500"><br>

<sub>Figure 6: MCMit controller (§ 5). Blue boxes show modified components, yellow boxes show ADC/DAC components, and green boxes show example data tables. Steps (1)-(8) are executed for a conditional feedback operation based on an MCM result.</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25863_figures/2604.25863_fig9.jpg" width="500"><br>

<sub>Fig. 6 shows the design of our FPGA controller, based on the open- source Qubic framework [107]. At a high level, the controller com- prises a function processor, a distributed processor, a set of buffers, and a set of interfaces. Function processor. The function processor is responsible for ap- plying processing functions to qubit readout results and, as such, supports an interface between external components, such as state discriminators or dedicated QEC decoders, if needed. Distributed processor. The distributed processor comprises mul- tiple cores, each managing interfaces to the function processor and inter-core synchronization. Cores execute programs featuring pre- cisely timed pulse...</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25863_figures/2604.25863_fig10.jpg" width="500"><br>

<sub>Figure 7: The MCMit qubit-state discriminators (§ 6).</sub>

</details>

**Main problem.**

Mid-circuit measurements (MCMs) and classical feedback latency/errors create significant bottlenecks in dynamic quantum circuits, leading to increased decoherence and branching errors in QEC and DQC.

**Main result.**

The MCMit co-design reduces feedback latency by up to 70%, improves circuit depth by up to 7x, and achieves up to 80% lower logical error rates in surface codes through improved state discrimination and hardware-software mitigation.

**Method.**

A hardware-software co-design featuring an FPGA-based controller with a multi-control branch instruction and neural network discriminators (Transformer and CNN) paired with software-level MCM elimination and stochastic branching.

**Summary.**

This paper presents MCMit, a holistic hardware-software co-design to mitigate errors and latency in mid-circuit measurements. By combining an FPGA-based controller with new neural network-based state discriminators and software-level error mitigation, the authors significantly reduce the overhead of dynamic quantum circuits. The approach improves readout accuracy for short durations and reduces logical error rates in quantum error correction. This is crucial for the advancement of distributed quantum computing and scalable fault-tolerant architectures.

<details><summary>Detailed structure</summary>

**Model / system.**

The implementation uses the Qubic 2.0 open-source framework on an Xilinx Alveo FPGA, evaluated using experimentally extracted readout traces from a five-qubit superconducting QPU and simulated surface code patches.

**Key observables.**

MCM error rates (bit-flips), readout fidelity, classical feedback latency, circuit depth, and logical error rates in surface codes.

**Important parameters / regimes.**

Readout durations (250ns to 2000ns), signal-to-noise ratio (SNR), and surface code distances (d=7, 9, 11).

**Assumptions / limitations.**

The evaluation assumes realistic noise models derived from IBM Heron processors and the effectiveness of the hardware-software co-design scales with the reduction of measurement-induced errors.

**Figures summary.**

Figure 1 shows the readout pipeline and neural network architectures; Figure 2 analyzes the impact of MCM error and latency on performance; Figure 6 illustrates the modified controller architecture; Figure 7 details the Transformer and CNN designs; Figure 8 demonstrates dynamic circuit simplification.

**Paper structure.**

The paper introduces the bottleneck of MCMs, proposes the MCMit co-design (hardware and software layers), details the implementation on FPGA, evaluates performance using experimental traces and QEC simulations, and concludes with a discussion on scalability and future directions.

</details>

<details><summary>Abstract</summary>

Distributed Quantum Computing (DQC) and Quantum Error Correction (QEC) rely on dynamic circuits that include Mid-Circuit Measurements (MCMs) and classical feedback. These operations present a major bottleneck: MCMs suffer from high error rates that lead to real-time branching errors, while MCM and classical feedback latencies amplify decoherence errors. Current hardware controllers, qubit-state discriminators, and software error mitigation techniques fail to address these challenges holistically.   We propose MCMit, a hardware-software co-design to mitigate branching and latency-induced errors. MCMit introduces a scalable, constant-latency multi-control branch instruction for faster classical feedback and two qubit-state discriminators, a transformer, and a CNN, with high accuracy even under short measurement durations. On the software side, static MCM elimination and stochastic branching complement the hardware by mitigating residual branching errors that persist despite hardware improvements.   We implement MCMit on Qubic and evaluate it using experimentally extracted QPU readout traces. Our branch instruction reduces feedback latency by up to 70\%, improving circuit depths by up to $7\times$ over Qubic. Our CNN discriminator achieves 37-73\% higher accuracy for short measurement durations than the baselines, leading to up to 80\% lower logical error rates in QEC. Last, our software mitigation improves fidelity by 18--30\% over baseline methods.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25883"></a>


### [Optimized thermal control of a dual-wavelength-resonant nonlinear cavity](http://arxiv.org/abs/2604.25883v1)

**Authors:** Fabian Meylahn, Henning Vahlbruch, Benno Willke

**Type:** experiment · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25883v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `quantum optics experiment` **4/5** · `QC/QI experiment` **3/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25883_figures/2604.25883_fig1.jpg" width="500"><br>

<sub>Fig. 1. Configuration of the bow-tie cavity, for dispersion-control enabled co-resonance and, thus, for high nonlinear interaction. The periodically poled potassium titanyl phosphate (PPKTP) crystal is mounted on a bimetallic heat sink, creating a constant- temperature zone and an adjustable thermal gradient zone via thermoelectric coolers (TECs). Two piezoelectric elements (PZTs) attached to the convex coupling mirrors enable resonator length tuning. A bright 532 nm pump beam and a weak 1064 nm seed beam (at half the pump-light frequency) are combined on a dichroic beam splitter and injected through the same input port. This port exhibits a power transmission (T) of 300 parts per million...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25883_figures/2604.25883_fig2.jpg" width="500"><br>

<sub>Fig. 2. Finite element simulations of temperature distributions in the heat sink and the nonlinear PPKTP crystal. a) Gradient heating: A controlled temperature gradient applied to the right heat sink surface propagates through the bimetallic construction to the crystal. Primary heat flow occurs through the heat sink and the generated temperature gradient is adapted by the crystal b) Segmented heating: The crystal itself forms the only thermal bridge across an air gap between two temperature zones. Heat flow through the crystal creates a strong thermal gradient that peaks at the air-gap position and close to the heat sink interface.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25883_figures/2604.25883_fig3.jpg" width="500"><br>

<sub>Fig. 3. Measured temperature distribution along the beam propagation axis for different heating schemes (inset images). The phase-matching constant-temperature zone is maintained at 33.7 ◦C in all configurations. The gradient heating scheme exhibits a 2.7 ◦C/mm thermal gradient. For segmented heating, a steep thermal slope develops across the thermal isolation layer here simulated as an air gap when bridged by the thin polyamide layer, with an even steeper gradient observed without this interfacial layer. The second temperature zone in segmented heating is set to 24.7 ◦C. Thermal images were corrected for a slight spurious gradient caused by camera temperature non-uniformity, verified...</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25883_figures/2604.25883_fig4.jpg" width="500"><br>

<sub>Fig. 4. Plot showing the distance between the fundamental resonances of the TEM00 mode of 1064 nm light from 532 nm light, normalized by the free spectral range (FSR) of the 532 nm light, color-coded as a function of the phase matching temperature and temperature gradient settings. White lines represent linear fits to co-resonance conditions (red dots). The results show a required temperature gradient along the steel section of −2.07 ◦C/mm to −2.32 ◦C/mm per degree change in phase matching temperature (temperature of the cooper section). The inset shows measurement points (white) with red markers indicating the positions closest to the co-resonance.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25883_figures/2604.25883_fig5.jpg" width="500"><br>

<sub>Fig. 5. Detailed mapping of double-resonance conditions across phase-matching temperatures from 29 ◦C to 35 ◦C. The inset displays measurement data points (white) with red markers indicating positions closest to co-resonance. Co-resonance conditions exhibit a near-linear dependence on temperature gradient, with the white fit line showing a slope of −2.29 ◦C/(mm ◦C).</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25883_figures/2604.25883_fig6.jpg" width="500"><br>

<sub>Fig. 6. Upper: Parametric gain color coded versus phase-matching temperature and temperature gradient. The inset displays the measurement step size (white points). Lower: Parametric gain values per phase-matching temperature. The fitted model yields a peak gain of 16.91 at an optimal temperature of 32.7 ◦C with a full width at half maximum of 6.3 ◦C</sub>

</details>

**Main problem.**

The dispersion of optical resonators often prevents the simultaneous resonance (co-resonance) of multiple interacting wavelengths, which is essential for efficient nonlinear processes like squeezing and parametric amplification.

**Main result.**

The authors demonstrate a novel thermal control method using a monolithic bimetallic heat sink that creates a controlled temperature gradient to achieve precise dispersion control and co-resonance.

**Method.**

A bimetallic heat sink (copper and stainless steel) is used to generate a longitudinal temperature gradient across a PPKTP crystal, validated by FEM simulations and experimental thermal imaging.

**Summary.**

This paper presents a new way to control the dispersion in nonlinear optical cavities using a bimetallic heat sink. By creating a shallow temperature gradient across a nonlinear crystal, the researchers can achieve simultaneous resonance for two different wavelengths. This method reduces mechanical and thermal stress compared to traditional heating methods. The technique is highly relevant for improving the efficiency of devices used in quantum optics and precision measurements.

<details><summary>Detailed structure</summary>

**Model / system.**

A traveling-wave bow-tie resonator containing a 11.5 mm PPKTP crystal, operating at 1064 nm and 532 nm wavelengths.

**Key observables.**

Parametric gain, temperature gradient (°C/mm), resonance positions, and predicted squeezing/anti-squeezing levels.

**Important parameters / regimes.**

Temperature stability (300 ppm), pump parameter (x = 0.77), and quantum efficiency (97.5%).

**Assumptions / limitations.**

Predictions for squeezing assume high quantum efficiency and negligible phase noise during detection.

**Figures summary.**

Fig 2 compares bimetallic vs. segmented heating stress; Fig 3 shows experimental thermal profiles; Fig 4 and 5 map the double-resonance conditions and frequency deviations.

**Paper structure.**

Introduction of the dispersion problem, description of the bimetallic heat sink design, FEM simulation results, experimental validation of thermal gradients, demonstration of dual-wavelength co-resonance, and discussion of applications.

**Why it may be interesting.**

This work provides a practical engineering solution for stabilizing the nonlinear optical platforms required for generating squeezed light and high-gain parametric amplification, which are foundational for continuous-variable quantum information and gravitational wave detection.

</details>

<details><summary>Abstract</summary>

Optical resonator-enhanced nonlinear interactions are of great importance for the efficient generation of continuous-wave second harmonic generation, optical parametric oscillation, frequency mixing, and the generation of squeezed light. In order to maximize these interactions within the intra-cavity nonlinear material, high intensities, optimal phase matching, and simultaneous resonance of all interacting fields are required. However, the dispersion of the optical resonator often prevents the co-resonance of multiple wavelengths. Here, we present a novel implementation using a monolithic bimetallic heat sink for controlling the resonator dispersion based on a shallow temperature gradient directly applied to a section of the nonlinear crystal. This method enables precise dispersion control and is designed to minimize mechanical and thermal stresses in the nonlinear crystal, thus providing an additional method for designing highly efficient and reliable resonator-enhanced nonlinear devices for demanding applications such as gravitational wave detection, quantum optics, and frequency conversion.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25195"></a>


### [A simple method to fabricate Josephson junctions](http://arxiv.org/abs/2604.25195v1)

**Authors:** Imran Mahboob, Satoshi Sasaki, Takaaki Takenaka

**Type:** experiment · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25195v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `QC/QI experiment` **4/5** · `quantum optics experiment` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25195_figures/2604.25195_fig1.jpg" width="500"><br>

<sub>FIG. 1: (a) The aluminum pattern of the base layer (blue) is deposited on a silicon substrate. Photoresist (pink) is pat- terned with 365nm UV light, and the resultant pattern is de- picted by the hollow boxes (black lines). The overlap between the resist pattern and the base aluminum layer deﬁnes the JJ. (b) The deposition of the top metal layer (blue) is preceded by argon milling to expose pristine aluminum which is then oxidized (red) where the aluminum sandwich deﬁnes the JJ. A zoom of the junction region where the vertical component of the JJ makes an insigniﬁcant contribution to the overall junction resistance.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25195_figures/2604.25195_fig2.jpg" width="500"><br>

<sub>FIG. 2: (a) Optical micrographs, acquired with Keyence VHX-7000 digital microscope, reveal JJs from this simple fabrication method can be successfully fabricated, even with an area as small as 1 × 1 µm2, with excellent alignment between base and top aluminum layers. (c) Room temperature JJ resistance as a function of junction size for test patterns (circles) and functional SQUID resonator devices (squares) all with 10 minutes oxidation with a range of pressures. All error bars correspond to 1 standard deviation and are invisible for the largest junctions.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25195_figures/2604.25195_fig3.jpg" width="500"><br>

<sub>FIG. 3: (a) and (b) BF and HAADF STEM with only the base 120 nm thick aluminum (Al) layer deposited on the argon etched silicon (Si) substrate. (c) and (d) BF and HAADF STEM following the completed device with the highly uniform 1-2 nm thick JJ clearly resolvable (red arrow). Also visible in the BF STEM images is the ∼2 nm thick oxide (Ox) cap (blue arrows). The carbon paste is employed as a conductive adhesive layer during focused ion beam milling used to access the JJ’s cross-section for STEM.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25195_figures/2604.25195_fig4.jpg" width="500"><br>

<sub>FIG. 4: (a) A SQUID based 2D resonator’s response to magnetic ﬂux bias is measured via a capacitively coupled 3D cavity at millikelvin temperatures. This device was repeatedly measured with more than 10 thermal cycles in a 6-month period, and it sustained a nominally unchanged ﬂux response thus indicating the stability of the JJs in the SQUID. (b) Parametric ampliﬁcation is measured with a ﬂux bias of 0.16 mA that is combined with microwave modulation at ∼16.6 GHz with increasing power from -33 to -26 dBm (orange to black lines) yielding a gain of almost 40 dB. The cavity is continuously probed with approximately 10 photons where the bare response (with microwave ﬂux modulation deactivated)...</sub>

</details>

**Main problem.**

The difficulty and high resistance variation associated with fabricating reliable Al/AlOx/Al Josephson junctions using complex electron-beam lithography techniques like the Dolan bridge.

**Main result.**

A simplified photolithography-based fabrication method was demonstrated that achieves significantly lower resistance variation (25% vs 200%) and high stability for SQUIDs and parametric amplifiers.

**Method.**

A minimal approach using maskless photolithography, argon etching to remove contaminants, and controlled in-situ oxidation followed by electron-beam evaporation.

**Summary.**

This paper presents a simplified, scalable method for fabricating Al/AlOx/Al Josephson junctions using standard photolithography instead of complex e-beam lithography. The technique significantly reduces resistance variation and improves device uniformity across multiple chips. The researchers demonstrated the method's effectiveness by creating stable SQUIDs and a Josephson parametric amplifier with 40 dB of gain. This approach could be pivotal for the widespread production of superconducting quantum technologies.

<details><summary>Detailed structure</summary>

**Model / system.**

The experimental platform consists of Al/AlOx/Al Josephson junctions and SQUIDs integrated into 2D resonators and 3D cavities for quantum-limited parametric amplification.

**Key observables.**

Junction resistance (Rjj), flux response symmetry/periodicity, parametric amplification gain, and transmission electron microscopy (TEM) structural analysis.

**Important parameters / regimes.**

Junction areas of 1 to 6 um^2, oxidation pressures from 0.5 to 7 Torr, and amplification gains of approximately 40 dB.

**Assumptions / limitations.**

The method assumes that the argon milling step effectively removes contaminants to ensure pristine interfaces for the oxide barrier.

**Figures summary.**

Fig 1 shows the fabrication schematic; Fig 2 displays optical micrographs and resistance vs. area plots; Fig 3 presents STEM images of the junction structure; Fig 4 shows SQUID resonator response and parametric amplification gain.

**Paper structure.**

The paper introduces a new fabrication protocol, details the experimental steps and structural characterization via TEM, demonstrates device performance through resistance tuning and stability tests, and concludes with a demonstration of quantum-limited parametric amplification.

**Why it may be interesting.**

The development of more scalable and reproducible hardware for superconducting circuits is crucial for the realization of large-scale quantum processors and high-fidelity quantum-limited amplifiers.

</details>

<details><summary>Abstract</summary>

A minimal method to fabricate Al/AlO$_x$/Al Josephson junctions (JJs) using photolithography and argon etching, before metallization and oxidation, is demonstrated. JJs with areas ranging from 1 to 6 $μ$m$^2$ can be fabricated and, with the appropriate oxidation conditions, the junction resistance can be varied by $\sim$2 orders of magnitude. Transmission electron microscopy reveals the successful fabrication of JJs with few grain boundaries suggesting reduced energy loss from two-level-systems. Superconducting QUantum Interference Devices (SQUIDs) fabricated from this methodology exhibit reduced resistance variation of over multiple chips, compared with electron beam lithography, and the devices can sustain repeated thermal cycles to 10 mK with the excellent flux response remaining unchanged. The quantum applications of this technology are demonstrated by embedding a SQUID resonator into a 3D cavity and parametrically amplifying low photon numbers with gains of $\sim$40 dB. This work establishes the simplest approach to fabricating JJs to date, and it could prove pivotal to the widespread utilization of superconducting circuit-based quantum technologies.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25034"></a>


### [Bell Test of Photons from Electron-Positron Annihilation via POVM-based Compton Polarimetry](http://arxiv.org/abs/2604.25034v1)

**Authors:** Jack Clarke, Preslav Asenov, Jesse Smeets, Jia-Shian Wang, David B. Cassidy, Alessio Serafini

**Type:** both · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25034v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `quantum measurements` **4/5** · `entanglement & information structure` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25034_figures/2604.25034_fig1.jpg" width="500"><br>

<sub>FIG. 1. (a) The Bloch sphere in polarization space (ϑ, φ). States along the equator of the Bloch sphere represent linearly polarized states. The north and south poles represent the circularly polarized eigenstates, which Compton polarimetry cannot distinguish. (b) POVM-based Compton polarimetry. Following a Compton scattering event, two polarization-insensitive detectors separated by azimuthal angle ∆ϕ = π/2 realize non-projective measurements of orthogonal linear polarization states. Detection at arbitrary (θ, ϕ) corresponds to the POVM element Π(1)(θ, ϕ). In the KUW Bell test, a value ±1 is assigned to detection at (θ, ϕ±) with ϕ+ = ϕ and ϕ−= ϕ + π/2, corresponding to the dichotomic,...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25034_figures/2604.25034_fig2.jpg" width="500"><br>

<sub>FIG. 2. Plot of the CHSH function optimized over polar scattering angles ∣S(θopt, ϕ)∣for N = 1 to N = 100 scattering events. Even for N = 2, the LHV bound = 2 is exceeded around ϕ = (2m + 1)π/8 with m ∈Z, and as N increases Tsirelson’s bound of 2 √</sub>

</details>

**Main problem.**

The inability to conclusively demonstrate polarization entanglement in MeV-scale photons from electron-positron annihilation due to the lack of ideal projective-polarization measurements.

**Main result.**

The authors show that using sequential Compton scattering events (N >= 2) allows the measurement to converge toward an ideal projective measurement, enabling the violation of CHSH inequalities.

**Method.**

A POVM-based framework using the Stokes-Mueller formalism to model sequential Compton scattering, supplemented by Geant4 Monte Carlo simulations for experimental feasibility.

**Summary.**

This paper addresses the difficulty of verifying entanglement in high-energy gamma-ray photons. By applying the POVM formalism to Compton polarimetry, the authors demonstrate that while a single scattering event is too weak to violate Bell inequalities, increasing the number of sequential scattering events improves measurement sharpness. This approach allows for a robust, model-independent certification of entanglement that can rule out local hidden variable models in electron-positron annihilation processes.

<details><summary>Detailed structure</summary>

**Model / system.**

The system consists of entangled photon pairs produced from electron-positron annihilation at the MeV scale, analyzed via Compton polarimetry involving multiple sequential scattering events.

**Key observables.**

CHSH function (S), Compton analyzing power (beta), polarization correlations, and coincidence count rates.

**Important parameters / regimes.**

Number of scattering events (N), photon energy (511 keV), azimuthal angles (phi), and polar scattering angles (theta).

**Assumptions / limitations.**

Assumes each scattering event is independent with no quantum coherence between involved electrons; assumes a simplified dichotomic, normalized POVM.

**Figures summary.**

Fig 1 shows the Bloch sphere, a schematic of the POVM-based polarimetry, and the Bell test setup; Fig 2 plots the optimized CHSH function violation as a function of the number of scattering events N.

**Paper structure.**

The paper introduces the problem of high-energy entanglement certification, develops a POVM mathematical framework for sequential scattering, analyzes the convergence of measurement sharpness (beta) toward ideal projection, and concludes with experimental feasibility simulations.

**Why it may be interesting.**

It provides a novel application of POVM formalism and quantum state discrimination theory to high-energy physics, demonstrating how non-projective measurements can be transformed into Bell-violating measurements through sequential interactions.

</details>

<details><summary>Abstract</summary>

Quantum entanglement between gamma-ray photons emitted following electron-positron annihilation is expected to be maximal and may be characterized via non-classical polarization correlations. However, this is difficult to verify experimentally because there are no established schemes that approach ideal projective-polarization measurements for high-energy photons. Hence, polarization entanglement between MeV-scale annihilation photons has not yet been conclusively demonstrated. We develop here a framework that models polarization measurements of high-energy photons via Compton polarimetry, employing the formalism of positive operator-valued measures (POVMs). We extend the POVM description to sequences of repeated interactions and show that the measurement converges toward an ideal projective measurement of linear polarization as the number of interactions increases. We demonstrate that this progressive improvement in measurement sharpness can enable the experimental violation of CHSH inequalities.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25753"></a>


### [Numerically-Exact Quantum-Simulation Approach for Two-Dimensional Spectroscopy of Open Quantum Systems](http://arxiv.org/abs/2604.25753v1)

**Authors:** Yi-Xuan Yao, Hao-Yue Zhang, Cheng-Ge Liu, Rong-Hang Chen, Qing Ai, Franco Nori

**Type:** theory · **Category:** numerical methods · **PDF:** <https://arxiv.org/pdf/2604.25753v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `methods for driven-dissipative` **4/5** · `non-equilibrium dynamics` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25753_figures/2604.25753_fig1.jpg" width="500"><br>

<sub>FIG. 1. Schematic of 2DS and its application for enantiodetection of chiral molecules. (a) The four-level structure in a left-handed chiral molecule with three control ﬁelds applied for distinguishing the two chiral forms. The diﬀerence between the two chiral forms lies in the fact that the transition dipole moments between |eL 2 ⟩↔|eL 3 ⟩and |eR 2 ⟩↔ |eR 3 ⟩are opposite in sign, resulting in ΩL 32 = −ΩR 32 = −Ω32. The incident probe pulses with wave vectors ⃗kp (p = a, b, c) are applied to induce the transition between |gα⟩and |eα 1 ⟩ with Rabi frequency Ωp. (b) Schematic illustration of 2DS. The detection pulses employ the square-wave approximation, and the curve represents the signal.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25753_figures/2604.25753_fig2.jpg" width="500"><br>

<sub>FIG. 2. Double-sided Feynman diagrams for the (a) rephasing and (b) non-rephasing signals. The arrows represent the incident probe pulses and the signals.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25753_figures/2604.25753_fig3.jpg" width="500"><br>

<sub>FIG. 3. The rephasing signals of the 2DS simulated by the BET with (left) linear χ(t), (right) nonlinear χ(t) at population time T = 0. In the linear case, the parameters are γ/2π = 0.1 MHz, Aj = 8 MHz, nc = 750, ω0/2π = 1 kHz, while in the nonlinear case, the parameters are Aj = 350 MHz, nc = 750, ω0/2π = 25 Hz. For both cases, the ensemble size is N = 6000.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25753_figures/2604.25753_fig4.jpg" width="500"><br>

<sub>FIG. 4. The top-right diagonal peak in the absorptive 2DS of pure left-handed chiral molecules simulated by the BET at population time T = 0, 4, 8 µs. The red (blue) dotted lines are the center lines for ωτ (ωt). The red (blue) solid lines are the least-squares ﬁtting of the center lines for ωτ (ωt). The parameters of the TCF are ∆= 1 MHz and τc = 4 µs, while the other parameters are Aj = 1 MHz, nc = 3.6 × 104, ω0/2π = 125 Hz and the ensemble size is N = 6000.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25753_figures/2604.25753_fig5.jpg" width="500"><br>

<sub>FIG. 5. Comparison of the CLS with TCF. (a) The dependence of the CLS on the population time T . The red diamonds, blue squares and green triangle are the CLS with respect to ωτ and ωt, and their average. The red dashed-dotted line, blue dashed line, and the green dotted line are the corresponding ﬁtted results. (b) Comparison of the normalized ﬁtted results with the TCF plotted as the black solid line.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25753_figures/2604.25753_fig6.jpg" width="500"><br>

<sub>FIG. 6. (a) The energy-level structure of the RDC. The solid (dashed) arrows represent the allowed (forbidden) transitions. (b) The absorptive 2DS at T = 0 obtained by the BET-based quantum-simulation approach.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25753_figures/2604.25753_fig7.jpg" width="500"><br>

<sub>FIG. 7. The top-right diagonal peak in the rephasing signal of the 2DS simulated by the BET at population times (a) T = 0 µs, (b) T = 4 µs, (c) T = 8 µs. The red (blue) dotted lines are the center lines for ωτ (ωt). The red (blue) solid lines are the least-squares ﬁtting of the center lines for ωτ (ωt). The parameters are the same as in Fig. 4.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25753_figures/2604.25753_fig8.jpg" width="500"><br>

<sub>FIG. 8. (a) The dependence of the CLS, extracted from the rephasing signal of the 2DS, on the population time T . The red diamonds (blue squares) are the CLS corresponding to ωτ (ωt). CLSave is the average of CLSωt and CLSωτ . The red dashed-dotted line, blue dashed line, and the green dotted line are the corresponding ﬁtted results. (b) The normalized CLSs are compared with the TCF denoted by the black solid line. The parameters are the same as in Fig. 4.</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25753_figures/2604.25753_fig9.jpg" width="500"><br>

<sub>FIG. 9. The top-right diagonal peak in the non-rephasing signal of the 2DS simulated by the BET at population times (a) T = 0 µs, (b) T = 4 µs, (c) T = 8 µs. The red (blue) dotted lines are the center lines for ωτ (ωt). The red (blue) solid lines are the least-squares ﬁtting of the center lines for ωτ (ωt). The parameters are the same as in Fig. 4.</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25753_figures/2604.25753_fig10.jpg" width="500"><br>

<sub>FIG. 11. Comparison between Csim(t) by the BET and the preset TCF C(t). The parameters are the same as those in Fig. 4.</sub>

</details>

**Main problem.**

The need for numerically-exact and computationally-efficient theoretical simulations of Two-Dimensional Spectroscopy (2DS) to interpret complex dynamics in open quantum systems, especially when conventional perturbative methods fail.

**Main result.**

The authors propose a quantum-simulation approach based on the bath-engineering technique (BET) that accurately reproduces 2DS patterns and demonstrates that the bath's time correlation function (TCF) can be extracted from the absorptive spectrum.

**Method.**

A quantum-simulation approach using the Bath-Engineering Technique (BET), which replaces complex system-bath interactions with a noise Hamiltonian containing time-dependent stochastic variables.

**Summary.**

This paper introduces a new numerical framework for simulating Two-Dimensional Spectroscopy in open quantum systems using the bath-engineering technique. By replacing complex environments with a stochastic noise Hamiltonian, the method achieves numerical exactness more efficiently than traditional hierarchical methods. The authors demonstrate that this approach can accurately model chiral enantiodetection and complex molecular dynamics in chloroform. Furthermore, they show that while individual 2D signals are insufficient for extracting bath correlations, the combined absorptive spectrum allows for the successful reconstruction of the bath's time correlation function.

<details><summary>Detailed structure</summary>

**Model / system.**

The study utilizes a Brownian Oscillator Model for the bath and applies the method to a four-level system for chiral enantiodetection and a six-level system representing RDC dissolved in chloroform.

**Key observables.**

2D spectra (rephasing and non-rephasing signals), absorptive 2DS, time correlation functions (TCFs), and center-line slope (CLS).

**Important parameters / regimes.**

Spectral density, Rabi frequencies, transition dipole moments, coherence time, population time, and signal time.

**Assumptions / limitations.**

Square-pulse approximation, Rotating-Wave Approximation (RWA), short-time approximation for the line-shape function, and the high-temperature limit where the TCF is real.

**Figures summary.**

Figure 1 shows the chiral molecule structure and 2DS process; Figures 7-10 illustrate 2DS peak dynamics and CLS behavior; Figures 11-14 demonstrate the convergence of the BET method with respect to ensemble size and time step.

**Paper structure.**

The paper introduces the BET-based simulation approach, demonstrates its application to a four-level chiral system, validates the extraction of TCFs via CLS theory, applies the method to a complex molecular system (RDC), and concludes with convergence and scalability analyses.

**Why it may be interesting.**

It provides a powerful, numerically-exact alternative to HEOM for simulating non-Markovian dynamics in large, complex systems, which is highly relevant for researchers in open quantum systems and quantum optics.

</details>

<details><summary>Abstract</summary>

Two-dimensional spectroscopy (2DS) is a powerful ultrafast technique for probing electronic and vibrational dynamics in complex microscopic systems. Extracting detailed information on system dynamics and system-bath interactions from 2DS experiments requires precise theoretical simulations for comparison, which motivates the development of numerically-exact and computationally-efficient simulation approaches. Here, we propose a quantum-simulation approach for 2DS based on the bath-engineering technique (BET), which has been successfully employed in quantum simulations of open quantum dynamics. To demonstrate our approach, we first simulate the 2DS of a driven four-level system in chiral enantiodetection, where we also assess the applicability of the center-line slope (CLS) method for extracting time correlation functions (TCFs) from the 2DS. We further apply our approach to the 2DS of ${\rm Rh(CO)_2C_5H_7O_2}$ (RDC) dissolved in chloroform, where the results reproduce the main spectral patterns observed in experiments. Our work provides a numerically-exact and efficient framework for simulating 2DS, and can offer additional insight into the dynamics of open quantum systems.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25429"></a>


### [Deterministic Realization of Classical Dissipation on Quantum Computers](http://arxiv.org/abs/2604.25429v1)

**Authors:** Muhammad Idrees Khan, Sauro Succi, Hua-Dong Yao

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25429v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `methods for driven-dissipative` **4/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25429_figures/2604.25429_fig1.jpg" width="500"><br>

<sub>Figure 1: Block-encoding-free CPTP realization of the diagonal MRT dissipative update. The classical nonequilibrium moment δmr is mapped onto two rails (p+ r , p− r ) by the signed population encoding (7). Each rail is damped by an amplitude-damping channel with survival |λr|, and a rail SWAP is applied when λr &lt; 0; the decoder (9) reads off δm′ r = λr δmr exactly (Theorem 3.3). The boxed region is trace-preserving by construction, so the per-application success probability is unity: no heralding, post-selection, or amplitude amplification is required, in contrast to block-encoded realizations of the same contraction (Section 4). The SWAP branch is selected by the classical sign of λr and...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25429_figures/2604.25429_fig2.jpg" width="500"><br>

<sub>Figure 2: Gate-level realization of the CPTP channel Er of Figure 1. Each amplitude-damping box is opened into its Stinespring dilation: a fresh ancilla |0⟩a±, a rail-controlled rotation Ry(θr) with θr = 2 arccos p</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25429_figures/2604.25429_fig3.jpg" width="500"><br>

<sub>Figure 3: Register-level block diagram of the hybrid Carleman–CPTP collision step (26), realizing specialization (U3) of the host-agnostic schema (23). The outer dashed frames mark the induced grouping Upre =(H1)◦(H2)◦(H3) and Upost =(H5)◦(H6). The orange block (H4) is the CPTP open channel of Theorem 3.3, whose signed two-rail internal structure is detailed in Figures 1– 2 (block and gate level). The dashed arrow entering (H4) from below carries the classical side information   sign(δmr), Sr(x, t), sign(λr)  realizing the bookkeeping items (T1)–(T3) of Section 4.3 (encoding-scale choice: Remark 3.1; adaptive scaling: Proposition 3.6).</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25429_figures/2604.25429_fig4.jpg" width="500"><br>

<sub>Figure 4: Dissipative-mode audit maxr∈D, sites |δm′ r −λrδmr| versus advective LBM time for the run defined in Section 6.1. The error stays at the IEEE-754 double-precision floor throughout.</sub>

</details>

**Main problem.**

Quantum Lattice Boltzmann Methods (QLBM) suffer from an exponential decay in success probability because implementing the dissipative collision step via standard block-encoding or LCU requires post-selection.

**Main result.**

The authors present a deterministic, block-encoding-free construction using a CPTP channel that achieves a success probability of 1 for the dissipative MRT block.

**Method.**

The method uses a signed two-rail population encoding and an amplitude-damping quantum channel to realize the relaxation, effectively replacing post-selection with classical bookkeeping.

**Summary.**

This paper solves a major scalability bottleneck in quantum fluid dynamics simulations. By replacing probabilistic block-encoding with a deterministic CPTP channel using a two-rail encoding, the authors eliminate the multiplicative decay of success probability during the dissipative collision step. This allows for much larger and longer-running quantum Lattice Boltzmann simulations. The method is proven to be accurate to machine precision and is compatible with various quantum computing architectures.

<details><summary>Detailed structure</summary>

**Model / system.**

The paper focuses on the Multiple-Relaxation-imTime (MRT) Lattice Boltzmann Method (LBM) for fluid dynamics, specifically implementing the dissipative collision step in moment space.

**Key observables.**

Non-equilibrium moments (delta m_r), rail number operators, and the pointwise residual error of the dissipative update.

**Important parameters / regimes.**

Relaxation parameters (lambda_r), overrelaxation regime (lambda_r < 0), and the encoding scale (S_r).

**Assumptions / limitations.**

The construction assumes a modewise diagonal collision operator and does not cover block-coupled collision matrices or the full Carleman-linearized collision step.

**Figures summary.**

Figure 1 shows the high-level pipeline from classical moments to decoded updates; Figure 2 displays the gate-level circuit; Figure 3 illustrates the hybrid Carleman-CPTP collision pipeline; Figure 4 shows the error evolution in a 3D Taylor-Green vortex simulation.

**Paper structure.**

The paper introduces the QLBM bottleneck, proposes a two-rail CPTP construction, provides formal proofs for the deterministic update (Theorem 3.3) and success probability (Corollary 3.4), details the gate-level implementation, and validates the method through 3D lattice and synthetic numerical audits.

**Why it may be interesting.**

This is highly relevant for researchers in open quantum systems as it provides a way to implement non-unitary, dissipative dynamics deterministically using CPTP maps and amplitude damping, avoiding the probabilistic overhead of standard gate-based methods.

</details>

<details><summary>Abstract</summary>

Lattice Boltzmann (LB) on quantum devices must reconcile unitary gate evolution with the dissipative \emph{collision} step. In the multiple-relaxation-time (MRT) class, we work in the common setting of \emph{modewise diagonal} moment relaxation, $δm_r'=λ_r\,δm_r$ with $λ_r\in[-1,1]$ (overrelaxation if $λ_r<0$). Embedding that contraction in a unitary by block encoding or a linear combination of unitaries (LCU) typically yields subunitary success probability that decays multiplicatively across modes, sites, and time, a key bottleneck for quantum LB. \emph{For the dissipative MRT block alone} we give a \emph{block-encoding-free} construction: a signed \emph{two-rail} population encoding, then a completely positive trace-preserving (CPTP) map (per-rail amplitude damping with survival $|λ_r|$ and, if $λ_r<0$, a rail SWAP) so that, after the decode, the map agrees with classical MRT relaxation exactly (expectations of the rail number operators, common encoding--decode scale). Trace preservation gives success probability $1$ for that substage. The main result is the dissipative MRT block; construction of the equilibrium moment vector~$m^{\mathrm{eq}}=Mf^{\mathrm{eq}}$ (prescribed~$f^{\mathrm{eq}}$, host moment matrix~$M$; notation as in Section~\ref{subsec:generic-mrt}), moment transforms, streaming, and boundaries are composed with it as in a standard host pipeline and lie outside the scope of the formal theorem. Hybrid and fully coherent encodings, adaptive scales, Carleman-based context, and a one-rail no-go in the same nonnegative population framework are in the main text. Audits of the open-channel map on a long LBM collide-stream simulation and on stencil-free inputs both match the target to machine precision.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25162"></a>


### [Experimental Workflows for Combinatorial Optimization: Towards Quantum Advantage](http://arxiv.org/abs/2604.25162v1)

**Authors:** Prashanti Priya Angara, Luis F. Rivera, Ulrike Stege, Hausi Müller, Ibrahim Shehzad

**Type:** both · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25162v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `QC/QI experiment` **4/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25162_figures/2604.25162_fig1.jpg" width="500"><br>

<sub>Fig. 1: End-to-end classical-quantum pipeline for solving combinatorial optimization problems via the profit framework. The pipeline consists of three stages: (1) classical pre-processing to reduce the graph size, (2) hybrid quantum-classical optimization using the unconstrained QAOA solver on the MAXPC formulation, and (3) classical post-processing to obtain feasible solutions for the original problem. The routing diamonds indicate problem-specific transformations applied at the input and output stages.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25162_figures/2604.25162_fig2.jpg" width="500"><br>

<sub>Fig. 2: QAOA solver performance on synthetic graph instances. (a) MAXPC profit comparison for a representative single graph instance: optimal profit, most likely sampled profit, probability-weighted average profit, post-processed profit. (b) Approximation ratio for 3-regular graphs, n = 10. (c) Aggregate summed probability across all synthetic graph instances, with mean &amp; variance of probability mass on optimal &amp; near-optimal solutions (≥90%-optimal, ≥80%-optimal) across QAOA p layers.</sub>

</details>

**Main problem.**

Demonstrating practical quantum advantage for combinatorial optimization by moving beyond standalone algorithms toward end-to-end, integrated hybrid workflows.

**Main result.**

The proposed three-stage pipeline effectively uses classical pre-processing to reduce problem size and post-processing to ensure feasibility, allowing QAOA to produce competitive solutions on real IBM hardware.

**Method.**

A hybrid 'sandbox' workflow involving classical reduction rules (pre-processing), the SCOOP framework to transform constrained problems into unconstrained 'twins', and QAOA execution on IBM quantum hardware.

**Summary.**

This paper presents a complete experimental workflow for solving complex graph optimization problems like Minimum Vertex Cover and Maximum Clique. Instead of focusing solely on the quantum algorithm, the authors integrate classical pre-processing to shrink problem sizes and classical post-processing to ensure solution feasibility. By using the SCOOP framework to avoid difficult penalty terms in the quantum circuit, they demonstrate that QAOA can provide meaningful improvements on real IBM quantum hardware. This approach provides a practical roadmap for achieving quantum utility in combinatorial optimization.

<details><summary>Detailed structure</summary>

**Model / system.**

The study utilizes the IBM Quantum System One at PINQ2, specifically the 156-qubit IBM Heron r2 processor (ibm_quebec) with a heavy-hexagonal lattice topology.

**Key observables.**

Approximation ratios, probability mass of optimal and near-optimal solutions, expected values, and profit gain over random sampling.

**Important parameters / regimes.**

QAOA circuit depth (p up to 8), graph vertex counts (up to 128 on hardware, up to 4,941 in pipeline evaluation), and error suppression strategies (measurement twirling and dynamical decoupling).

**Assumptions / limitations.**

The strategy assumes an 'instance-aware' approach where classical methods exhaust tractable substructures, leaving only hard parts for the quantum processor.

**Figures summary.**

Figure 1 illustrates the end-to-end pipeline; Figure 2 shows the practitioner's decision landscape, approximation ratios for various graphs, and cumulative probability curves for solution quality.

**Paper structure.**

The paper introduces the need for end-to-end workflows, describes the three-stage sandbox platform (pre-processing, quantum solver, post-processing), details the SCOOP framework for unconstrained transformation, presents experimental results on IBM hardware, and concludes with a discussion on the path to quantum utility.

</details>

<details><summary>Abstract</summary>

Demonstrating quantum advantage for combinatorial optimization requires more than standalone algorithmic results; it calls for end-to-end case studies that integrate problem modelling, quantum execution, and classical refinement into practical workflows. This paper presents a sandbox platform for experimenting with hybrid quantum-classical workflows in graph optimization, enabling the systematic study of end-to-end optimization pipelines. Using our platform, we investigate three classically intractable and mutually reducible graph problems -- Minimum Vertex Cover, Maximum Independent Set, and Maximum Clique -- by transforming them into an unconstrained problem and solving the resulting instances with QAOA on IBM platforms. Our workflow combines classical pre-processing to reduce instance size, quantum optimization on the reduced problem, and classical postprocessing to map quantum outputs to high-quality feasible solutions, thereby avoiding direct constraint encoding in the quantum circuit. We evaluate the approach on synthetic graphs, benchmark instances, and real-world networks, and report hardware experiments on IBM Quantum System One at PINQ2 in Bromont, Quebec, powered by IBM's 156-qubit Heron r2 processor on graphs up to 128 vertices, with circuits involving up to 128 qubits and 13,555 two-qubit gates. The results illustrate how sandbox-style end-to-end experimentation can expose bottlenecks, clarify the role of classical-quantum workload partitioning, and provide domain experts and practitioners with a practical guide for interpreting quantum optimization outputs and assessing quantum utility on the road to quantum advantage in combinatorial optimization.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25303"></a>


### [Millikelvin digital-to-analog converter for superconducting quantum processors](http://arxiv.org/abs/2604.25303v1)

**Authors:** Ruizi Hu, Zongyuan Li, Zhancheng Yao, Yufei Wu, Qiang Zhang, Yining Jiao, Quan Guan, Lijing Jin, Wangwei Lan, Chengyao Li, Lu Ma, Liyong Mao, Huijuan Zhan, Ze Zhan, Ran Gao, Lijuan Hu, Kannan Lu, Xizheng Ma, Tenghui Wang, Peng Xiang, Chunqing Deng, Shasha Zhu

**Type:** experiment · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25303v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `QC/QI experiment` **4/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25303_figures/2604.25303_fig1.jpg" width="500"><br>

<sub>FIG. 1. SFQ-programmable DAC architecture and de- vice implementation. a, Conceptual architecture for scal- able qubit control using SFQ-programmable digital-to-analog converters (DACs). b, Circuit-level implementation of the SFQ-programmable flux DAC integrated with a fluxonium qubit. SFQ pulses are generated by a dc/SFQ converter and transmitted through a Josephson transmission line (JTL) to the DAC. A bias current Ibias sets the DAC operating point and provides bias for the dc/SFQ converter and JTL. c, Opti- cal micrograph of the multi-chip module device (left), showing the integration of the qubit chip (right) and the digital con- trol chip (middle).</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25303_figures/2604.25303_fig2.jpg" width="500"><br>

<sub>Figure 1a illustrates the proposed architecture for scal- able static control of superconducting qubits using SFQ- programmable DACs. SFQ pulses generated from a common source are processed by superconducting digital logic and routed through a demultiplexing network, en- abling selective programming of individual DACs. Each DAC converts SFQ pulses into persistent flux stored in a superconducting loop, providing a programmable local flux bias for the qubit; such devices are hereafter referred to as flux DACs. This control architecture is fully com-</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25303_figures/2604.25303_fig3.jpg" width="500"><br>

<sub>FIG. 4. Qubit characterization under DAC control. a, Fluxonium qubit frequency as a function of external flux. Blue circles show spectroscopy measured using a conventional bias line, and the dashed curve is a fit to the fluxonium Hamil- tonian, yielding (EC, EJ, EL)/h = (1.3, 5.08, 0.806) GHz. Or- ange diamonds show the qubit frequencies obtained using the DAC analog output in combination with a fixed conventional bias. Comparing spectroscopy under DAC control with that obtained using conventional bias provides a precise calibra- tion of the DAC analog output. b, Pure dephasing rate Γϕ as a function of first-order flux sensitivity ∂ω01/∂Φqubit. Green and orange squares denote Ramsey and...</sub>

</details>

**Main problem.**

The scalability of superconducting quantum processors is limited by the 'wiring bottleneck,' where the need for individual room-temperature control lines for each qubit leads to excessive heat load and calibration overhead.

**Main result.**

The researchers demonstrated a millikelvin digital-to-analog converter (DAC) integrated with fluxonium qubits that allows for deterministic, quantized flux tuning via SFQ pulses without degrading qubit coherence.

**Method.**

The team used a multi-chip module architecture to integrate an SFQ-based DAC with high-coherence fluxonium qubits, employing single-flux-quantum pulses to program persistent flux states in an rf-SQUID-based storage loop.

**Summary.**

This paper presents a breakthrough in superconducting quantum hardware by introducing a millikelvin-compatible digital-to-analog converter. By using single-flux-quantum pulses to program local flux storage, the device enables precise, non-volatile tuning of fluxonium qubits. This approach significantly reduces the need for individual room-temperature wires, addressing a major bottleneck in scaling up quantum processors. Crucially, the DAC operates without introducing measurable decoherence to the qubits.

<details><summary>Detailed structure</summary>

**Model / system.**

The system consists of a multi-chip module (MCM) featuring a digital control chip and a qubit chip (fluxonium qubits on sapphire) connected via indium bumps, utilizing an rf-SQUID-based DAC and SFQ logic.

**Key observables.**

Qubit frequency shifts, flux increment steps (approx. 4.8 mPhi0), qubit relaxation time (T1), and dephasing rates (Ramsey and Echo measurements).

**Important parameters / regimes.**

Operating temperature below 20 mK, screening parameter beta_L = 243, storage inductance L = 1 nH, and critical current Ic approx 80-133 uA.

**Assumptions / limitations.**

Assumes that required flux biases across different qubits lie within a narrow range suitable for a shared global coarse bias, and that the reset protocol reliably converges to a deterministic state.

**Figures summary.**

Figure 1 shows the conceptual architecture and circuit implementation; Figure 3 illustrates the linear evolution of DAC output and the programming margin; Figure 4 compares qubit spectroscopy and dephasing rates between conventional and DAC-controlled bias.

**Paper structure.**

The paper introduces the scalability problem, describes the DAC architecture and SFQ-based programming mechanism, presents experimental characterization of flux increments and qubit coherence, and discusses the implications for large-scale integrated control stacks.

</details>

<details><summary>Abstract</summary>

Scaling superconducting quantum processors is increasingly constrained by the wiring, heat load, and calibration overhead associated with delivering high-resolution analog signals from room temperature to qubits at millikelvin temperature. Here we demonstrate a superconducting digital-to-analog converter (DAC) integrated with high-coherence fluxonium qubits in a multi-chip module architecture. The DACs generate persistent analog flux signals for tuning qubit parameters and are programmed deterministically using single-flux-quantum (SFQ) pulses, providing a digital interface compatible with established SFQ routing and demultiplexing technologies. Operating at millikelvin temperature, the DACs enable in-situ tuning of fluxonium qubits without measurable degradation of qubit coherence. The presented device provides a static control primitive for flux-tunable qubits, enabling parameter homogenization and eliminating the need for individual room-temperature DC bias lines. These results establish SFQ-programmable millikelvin DACs as a building block for digitally controlled superconducting quantum processors.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25509"></a>


### [Simon's Algorithm for the Even-Mansour Cipher on Quantum Hardware](http://arxiv.org/abs/2604.25509v1)

**Authors:** Anina Köhler, Jakob Murauer, Tim Heine, Stefan Rosemann, Tobias Hemmert

**Type:** both · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25509v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** 🔥 `QC/QI experiment` **4/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25509_figures/2604.25509_fig1.jpg" width="500"><br>

<sub>Fig. 2. Representation of (a) classical Even-Mansour encryption, (b) secret unitary encryption oracle UEM, (c) synthesized unitary permutation oracle UP .</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25509_figures/2604.25509_fig2.jpg" width="500"><br>

<sub>Fig. 3. Schematic workflow of the attack: Quantum sampling via Simon’s algorithm and final quantum/classical secret key extraction.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25509_figures/2604.25509_fig3.jpg" width="500"><br>

<sub>Fig. 4. Mean relative distribution of five independent 3 and 4-bit trials on ibm miami. Small deviations demonstrate hardware reproducibility, with all individual runs succeeding.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25509_figures/2604.25509_fig4.jpg" width="500"><br>

<sub>Fig. 6. Quantum circuit for the 4-qubit permutation.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25509_figures/2604.25509_fig5.jpg" width="500"><br>

<sub>Fig. 5. Quantum circuit for the 3-qubit permutation.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25509_figures/2604.25509_fig6.jpg" width="500"><br>

<sub>Fig. 7. Schematic result of Simon’s circuit for the 3-bit case. (a) No noise for p = 0, (b) if p &gt; 0, depolarizing noise pulls towards a uniform distribution.</sub>

</details>

**Main problem.**

Evaluating the practical feasibility of implementing Simon's algorithm for quantum cryptanalysis of the Even-Mansour cipher on NISQ-era hardware and investigating the scalability of quantum circuit synthesis tools.

**Main result.**

Successful secret key recovery for N=3 and N=4 bit-length Even-Mansour constructions was demonstrated on the IBM miami processor, though a classical memory bottleneck was identified for N=5.

**Method.**

The researchers implemented Simon's period-finding algorithm using the DORCIS toolchain for circuit synthesis, applied error mitigation techniques like Dynamical Decoupling and Pauli Twirling, and used Gaussian elimination for post-processing.

**Summary.**

This paper presents a proof-of-concept implementation of Simon's algorithm to attack the Even-Mansour symmetric cipher on real NISQ hardware. By using the IBM miami processor, the authors successfully recovered secret keys for very small bit-lengths (N=3 and N=4). The study highlights both the potential for quantum cryptanalysis on current hardware and the significant classical computational bottlenecks in synthesizing larger quantum circuits.

<details><summary>Detailed structure</summary>

**Model / system.**

The experimental platform is the IBM miami NISQ quantum processor, utilizing a quantum encryption oracle representing the Even-Mansour cipher acting on quantum states.

**Key observables.**

Recovery of the secret key vector k1 via the identification of the hidden period, and the frequency distribution of measurement outcomes.

**Important parameters / regimes.**

Key lengths N=3, 4, and 5; circuit depth and T-depth; depolarization parameter p; and the number of shots (10^5 per experiment).

**Assumptions / limitations.**

The attack assumes a quantum oracle model (access to the encryption of quantum states), which is considered impractical in real-world settings.

**Figures summary.**

Figures include schematics of the quantum circuit and the Even-Mansour process, representations of the encryption oracle, workflow diagrams for the attack, and distributions of measurement results comparing ideal vs. noisy outcomes.

**Paper structure.**

The paper introduces the cryptanalytic problem, describes the hardware and circuit synthesis methodology, presents experimental results for small bit-lengths, analyzes noise and collision impacts, and discusses scalability limitations and future work.

</details>

<details><summary>Abstract</summary>

Simon's algorithm is a polynomial period-finding algorithm that has been used to exploit the algebraic structure of specific symmetric ciphers, showing that exponential speedups in their cryptanalysis are theoretically possible. While the theoretical framework for an attack using Simon's algorithm on the Even-Mansour cipher is well-established, practical implementations on noisy intermediate-scale quantum (NISQ) hardware remain limited. This paper presents a proof of concept quantum cryptanalysis of the Even-Mansour cipher using Simon's period-finding algorithm on NISQ hardware. For N = 3 and N = 4, we successfully demonstrate secret key recovery for N-bit constructions on the ibm_miami processor. Our experiments also identify a scaling limitation in the classical pre-processing stage: The DORCIS circuit optimization tool encountered a memory bottleneck at N = 5, preventing the generation of optimized circuits for larger key lengths. Our results suggest firstly that Simon's algorithm is effective for the Even-Mansour cipher for short bit lengths on current quantum hardware. Secondly, while DORCIS is effective for the small-scale S-boxes for which it was designed, there remains a need for the investigation of more scalable and efficient synthesis tools capable of handling larger and more general permutations in the context of Even-Mansour ciphers.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25983"></a>


### [Characterization of Thermalization Behaviour in a Generalized Aubry-André Model](http://arxiv.org/abs/2604.25983v1)

**Authors:** S. Mal, D. K. Nandy, B. K. Sahoo

**Type:** theory · **Category:** disordered systems and neural networks · **PDF:** <https://arxiv.org/pdf/2604.25983v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `analog quantum simulation` **3/5** · `entanglement & information structure` **3/5** · `non-equilibrium dynamics` **3/5** · `scars & prethermalization` **3/5** · `non-equilibrium universality` **2/5** · `driven-dissipative phase transition` **1/5** · `methods for driven-dissipative` **1/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25983_figures/2604.25983_fig1.jpg" width="500"><br>

<sub>FIG. 1. A schematic representation of the generalised Aubry- Andr´e model. The maxima and minima of the quasi-periodic potential of the considered system are governed by two pa- rameters α and λ with the quasi-periodic wavenumber given by the irrational number q = ( √</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25983_figures/2604.25983_fig2.jpg" width="500"><br>

<sub>FIG. 2. The average of adjacent gap ratio ⟨r⟩deﬁned in Eq. (2) is presented in the plane of α and λ for diﬀerent values of interaction with L = 14 (upper row) and L = 16 (lower row). For a ﬁxed value of α, we observe ⟨r⟩≈0.53 for smaller values of λ, signifying that the level statistics follow the GOE distribution.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25983_figures/2604.25983_fig3.jpg" width="500"><br>

<sub>FIG. 3. Spectral form factor K(τ) is shown as a function of scaled time τ for diﬀerent values of α = 0 (a, b, c), 0.3 (d, e, f), 0.7 (g, h, i) and λ = 0.65 (a, d, g), 1.35 (b, e, h), 10.15 (c, f, i). The black dashed line corresponds to KGOE(τ) and the dotted vertical line represents the scaled Heisenberg time τH. The Thouless time τT h is identiﬁed as K →KGOE and indicated by the dashed circles. For a lower value of λ, the ratio of Thouless time and Heisenberg time τT h/τH &lt;&lt; 1 for all three values of α. As the value of λ increases, the ratio approaches unity and for large λ goes past unity. The insets represent the magniﬁed images near Thouless time.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25983_figures/2604.25983_fig4.jpg" width="500"><br>

<sub>FIG. 4. The scaled Thouless time τTh is shown as a function of α for three diﬀerent values of λ = 0.65 (a), 1.35 (b) and 10.15 (c) with L = 16 and 17. In the ergodic regime, with λ &lt; 1, τTH increases rapidly as α approaches unity.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25983_figures/2604.25983_fig5.jpg" width="500"><br>

<sub>FIG. 5. Scaled ﬁdelity susceptibility F for the local operator nL/2 (n(L+1)/2) for even (odd) lattice sizes as a function of λ is plotted for diﬀerent values of α. We consider L = 13, 14, 15 and 16 for α = 0.0, 0.3 and 0.7. In the insets, we show the behavior of unscaled ﬁdelity susceptibility eζ. The crossing of the three curves, indicated with the shaded region, speciﬁes the transition λ∗between ergodic and localized phases. With increasing α, λ∗decreases as predicted by the earlier analysis. The dashed line indicates the peak-drift behavior towards higher values of λ as the system size is increased.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25983_figures/2604.25983_fig6.jpg" width="500"><br>

<sub>FIG. 6. Scaled ﬁdelity susceptibility F for the extended AGP operator (P</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25983_figures/2604.25983_fig7.jpg" width="500"><br>

<sub>FIG. 7. Mean level spacing ratio ⟨r⟩for diﬀerent systems sizes L, calculated for α = 0 (a), 0.3 (b) and 0.7 (c). Insets show ⟨r⟩as a function of λ. In the main panels, we plot ⟨r⟩ as a function of scaling parameter Θ = sgn[λ −λ∗]L/ξ, with ξ = ξBKT is a BKT correlation length, assuming the crossing point ansatz λ∗= λ0 + λ1L. The optimal parameters ν, λ0 and λ1 in ξBKT are obtained by minimizing the cost function Cr. The number of data points included in the minimization procedure is Np = 264.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25983_figures/2604.25983_fig8.jpg" width="500"><br>

<sub>FIG. 8. Scaled ﬁdelity susceptibility for extended operator and diﬀerent system sizes are calculated for α = 0, 0.3 and 0.7, and plotted as a function of Θ = sgn[λ −λ∗]L/ξ, with ξ = ξ0 (upper panel) and ξ = ξBKT (lower panel), assuming the crossing point ansatz λ∗= λ0+λ1L. The parameters ν, λ0 and λ1 in ξBKT are obtained by minimizing CF. The dotted vertical line represents the critical point λ = λ∗at which F becomes discontinuous. The number of data points included in the minimization procedure is Np = 240.</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25983_figures/2604.25983_fig9.jpg" width="500"><br>

<sub>FIG. 9. Critical point λ∗as a function of system size L, for the power-law correlation ξ = ξ0 (left) and BKT-type correlation ξ = ξBKT (right) for diﬀerent values of α. λ∗are obtained from the best data collapse of CF. The straight lines represent the linear dependence of critical value λ∗= λ0 + λ1L. The square and circular markers are diﬀerent nonlinear ansatz λ∗= λ0 + λ1/ln(L) and λ∗= λ0 + λ1/L, respectively.</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25983_figures/2604.25983_fig10.jpg" width="500"><br>

<sub>FIG. 10. F for the extended operator are plotted with ξ = ξBKT, assuming the critical ansatz λ∗= λ0 +λ1/ln(L) (upper panel) and λ∗= λ0 + λ1/L (lower panel).</sub>

</details>

**Main problem.**

The study aims to characterize the ergodic-to-many-body localization (MBL) transition in the generalized Aubry-André model (GAA) with interacting spinless fermions.

**Main result.**

The analysis constructs a phase diagram using the fidelity susceptibility ($\chi_n$) and shows that the system exhibits distinct scaling behaviors corresponding to ergodic, intermediate, and localized regimes.

**Method.**

The research employs advanced numerical techniques including Exact Diagonalization (ED), finite-size scaling analysis via cost-function minimization, and diagnostics based on the adjacent gap ratio and spectral form factor.

**Summary.**

This paper investigates the ergodic-to-Many-Body Localization (MBL) transition in the interacting generalized Aubry-André model. The authors utilize sophisticated diagnostics, including the fidelity susceptibility and spectral statistics, alongside finite-size scaling analysis. By mapping out a phase diagram, they characterize the transition point ($\lambda^*$) and demonstrate how the system's thermalization properties change as the disorder strength and quasi-periodic modulation are varied. This work advances the understanding of quantum chaos in complex, disordered quantum systems.

<details><summary>Detailed structure</summary>

**Model / system.**

The system is the generalized Aubry-André model (GAA) Hamiltonian, which includes tunneling ($t$), quasi-periodic modulation ($\lambda$), and nearest-neighbor interactions ($V$). The model is studied for interacting spinless fermions.

**Key observables.**

Fidelity susceptibility ($\chi_n$), adjacent gap ratio ($\langle r 
angle$), Spectral Form Factor (SFF), and the Thouless time ($	au_{Th}$).

**Important parameters / regimes.**

Disorder strength ($\lambda$), quasi-periodic parameter ($\alpha$), system size ($L$), and the critical disorder strength ($\lambda^*$).

**Assumptions / limitations.**

The analysis compares scaling behavior using two correlation length ansatzes: power-law ($\xi_0$) and Berezinskii-Kosterlitz-Thouless (BKT) type ($\xi_{BKT}$).

**Figures summary.**

Figures illustrate phase diagrams in the $\alpha-\lambda$ plane using $\langle r 
angle$, and show scaling collapse plots for the fidelity susceptibility ($F$) using both $\xi_0$ and $\xi_{BKT}$ ansatzes.

**Paper structure.**

The paper systematically analyzes the transition by first establishing the Hamiltonian and then applying multiple diagnostic tools ($\chi_n$, $\langle r 
angle$, SFF) across varying system sizes and parameters to map out the phase diagram and determine scaling laws.

**Why it may be interesting.**

The application of fidelity susceptibility and finite-size scaling to probe the MBL transition in a quasi-periodic interacting system provides a rigorous theoretical framework for understanding quantum chaos in disordered settings.

</details>

<details><summary>Abstract</summary>

Although random matrix theory provides a fundamental framework for characterizing quantum chaos, encompassing both ergodic and localized phases, a comprehensive understanding of the universal features governing the critical transition remains elusive in many disordered and quasi-random systems. In this study, we explore the ergodic-to-many-body localization transition in the generalized Aubry-André model with interacting spinless fermions. Using the concept of Frobenius norm of an adiabatic gauge potential, we construct a phase diagram that captures the sensitivity of the eigenspectrum to infinitesimal adiabatic gauge deformations. To examine the stability of the critical disordered strength with respect to system size, we perform an unbiased finite-size scaling analysis via cost-function minimization techniques. Additionally, by analyzing the adjacent gap ratio and spectral form factor, we determine the scaling behavior of the Thouless time as a function of the disorder strength.

</details>

<sub>[↑ back to top](#top)</sub>
