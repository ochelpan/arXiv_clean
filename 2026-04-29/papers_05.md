# Daily arXiv Report

[← Index](index.md)

[← Previous](papers_04.md)
[Next →](papers_06.md)

## Papers 81–100


<a id="paper-2604.25095"></a>


### [Markovian thermodynamics of non-Markovian Langevin equations](http://arxiv.org/abs/2604.25095v1)

**Authors:** Andreas Dechant, Kiyoshi Kanazawa

**Type:** theory · **Category:** statistical mechanics · **PDF:** <https://arxiv.org/pdf/2604.25095v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `entanglement & information structure` **3/5** · `non-equilibrium dynamics` **3/5** · `Keldysh / 2PI / non-Gaussian methods` **2/5** · `correlated / nonlocal dissipation` **2/5** · `methods for driven-dissipative` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25095_figures/2604.25095_fig1.jpg" width="500"><br>

<sub>FIG. 1. Markovian and non-Markovian EPR for a particle in a trap with periodically varying trap stiffness. Left: As a function of time for one period of the driving (indicated by the dashed vertical lines). The red line is the Markovian EPR Eq. (6), the blue line the apparent non-Markovian EPR Eq. (7). The light blue lines are the information flow Eq. (38) (dashed), the heat flow due to the interaction with the auxiliary mode Eq. (19) (dotted) and the sum of both terms (dash-dotted). Right: As a function of the decay rate (top) and magnitude (bottom) of the memory friction. The solid lines are the time-averaged EPRs, the shaded area indicates the range of the EPRs over one period of the...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25095_figures/2604.25095_fig2.jpg" width="500"><br>

<sub>FIG. 2. Heat flow for a driven particle with power-law memory. Left: Position of the trap λ(t) (purple) and the resulting mean position of the particle ⟨xs(t)⟩(red). Right: Markovian heat flow in Eq. (6) (red) and non-Markovian heat flow in Eq. (7) (blue), as well as the rate of change of interaction energy ˙EM,int = dt U int (red dashed). Parameters are γs = 0.1, γNM = 100, ks = 1, while the power-law memory is given by Eq. (22) with τ0 = 0.01, τ1 = 1000 and β = 0.5, and we use da = 8 exponential modes to fit it.</sub>

</details>

**Main problem.**

Addressing thermodynamic inconsistencies in non-Markovian systems, specifically the apparent violation of the second law where entropy production can transiently decrease.

**Main result.**

The authors show that a Markovian embedding provides a unique and physically consistent thermodynamic description where entropy production increases monotonically, resolving apparent violations through heat and information exchange with auxiliary degrees of freedom.

**Method.**

The study uses an 'inverse coarse-graining' technique to embed non-Markovian Generalized Langevin Equations (GLE) into a high-dimensional Markovian representation using auxiliary degrees of freedom and matrix decomposition.

**Summary.**

This paper develops a consistent thermodynamic framework for non-Markovian Langevin equations by embedding them into a higher-dimensional Markovian system. It demonstrates that while non-Markovian entropy production can appear to decrease, this is simply due to uncaptured heat and information exchange with auxiliary environmental degrees of freedom. The authors prove that the resulting Markovian thermodynamic quantities are unique and independent of the specific embedding choice. This approach provides a way to recover the monotonic increase of entropy required by the second law of thermodynamics.

<details><summary>Detailed structure</summary>

**Model / system.**

A target system with degrees of freedom x_s(t) evolving via a non-Markovian GLE with a memory kernel and thermal noise, embedded into an extended system with auxiliary degrees of freedom x_a and a quadratic interaction potential.

**Key observables.**

Entropy production (Markovian and non-Markovian), heat flow (interaction and total), work, information flow, and mutual information.

**Important parameters / regimes.**

Memory kernel decay rates, friction coefficients, temperature, and the number of auxiliary modes used for power-law approximation.

**Assumptions / limitations.**

The memory kernel is linear and satisfies the fluctuation-dissipation relation; forces are conservative; the noise acting on the target and auxiliary systems is independent.

**Figures summary.**

Figure 1 and 2 show the evolution of particle position in a time-dependent trap, comparing Markovian and non-Markovian heat flows and the rate of change of interaction energy.

**Paper structure.**

The paper introduces the problem of non-Markovian thermodynamics, develops the Markovian embedding construction, proves the uniqueness of thermodynamic quantities, and applies the framework to specific models like power-law memory and time-dependent traps.

**Why it may be interesting.**

This work is highly relevant for open quantum systems and many-body dynamics as it provides a rigorous thermodynamic framework for systems with memory, resolving how information exchange with an environment can mimic entropy-decreasing processes.

</details>

<details><summary>Abstract</summary>

We develop the thermodynamics of non-Markovian generalized Langevin equations by embedding them in a high-dimensional Markovian representation involving auxiliary degrees of freedom. If the memory is linear and satisfies detailed balance with the noise, we provide an explicit construction of the embedding for non-Markovian dynamics with many degrees of freedom and hydrodynamic interactions. Moreover, while the embedding is generally not unique, we show that it results in unique values of thermodynamic quantities of the Markovian system. This allows us to define the Markovian entropy production of a non-Markovian system, which, in contrast to the definition based directly on the non-Markovian dynamics, is guaranteed to increase monotonically with time. Moreover, the Markovian representation allows us to identify the apparent decrease in the non-Markovian entropy with heat and information exchange between the system and the auxiliary degrees of freedom.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25801"></a>


### [Pseudo-Hermiticity of the Nakajima-Zwanzig Projected Liouvillian in the Jaynes-Cummings Model](http://arxiv.org/abs/2604.25801v1)

**Authors:** Kejun Liu

**Type:** theory · **Category:** other · **PDF:** <https://arxiv.org/pdf/2604.25801v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `methods for driven-dissipative` **3/5** · `Tavis-Cummings & cavity-many-emitter` **2/5** · `driven-dissipative phase transition` **2/5** · `non-equilibrium dynamics` **2/5** · `non-equilibrium universality` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25801_figures/2604.25801_fig1.jpg" width="500"><br>

<sub>FIG. 1. Re-entrant pseudo-Hermitian phase of QLQ un- der counter-rotating deformation. At λ = 0 (JC), pro- tection is U(1); at λ = 1 (Rabi), protection is Z2. The complex-spectrum window is bracketed by EP boundaries at λ(1) c ≈0.39 and λ(2) c ≈0.88. Top panel: maximum imaginary part of QLQ eigenvalues. Bottom panel: condition number κ(η) of the metric on a log scale, diverging at the boundaries. An interior EP at λ ≈0.60 produces a secondary κ spike.</sub>

</details>

**Main problem.**

The paper seeks to resolve the unexplained anomaly where the non-Hermitian Nakajima-Zwanzig projected Liouvillian (QLQ) in the Jaynes-Cummings model exhibits a purely real spectrum.

**Main result.**

The authors prove that QLQ is pseudo-Hermitian in the Mostafazadeh sense, meaning a positive-definite metric exists that ensures a real spectrum. They also identify a re-entrant pseudo-Hermitian phase during the transition from the Jaynes-Cummings to the Rabi model.

**Method.**

The study uses biorthonormal diagonalization of the QLQ matrix, construction of a symmetrizing metric from left eigenvectors, and a continuous lambda-deformation to scan parameter regimes.

**Summary.**

This paper resolves why the non-Hermitian Nakajima-Zwanzig projected Liouvillian in the Jaynes-Cummings model has a real spectrum by demonstrating its pseudo-Hermiticity. By finding a positive-definite metric that intertwines the operator with its adjoint, the authors explain the spectral reality and explore how this property persists or breaks during the transition to the Rabi model. The study also identifies specific regimes of broken pseudo-Hermiticity and characterizes the nature of exceptional points in the thermodynamic limit. This provides a deep mathematical foundation for the analyticity of memory kernels in quantum optical models.

<details><summary>Detailed structure</summary>

**Model / system.**

The system is the Jaynes-Cummings model and its deformation into the full Rabi model, describing a single-mode cavity coupled to a two-level atom in an open quantum dynamics framework using the Nakajima-Zwanzig projection formalism.

**Key observables.**

The spectrum of the projected Liouvillian (real vs. complex eigenvalues), the intertwining residual, the condition number of the metric, and the scaling of the critical exponent at exceptional points.

**Important parameters / regimes.**

Coupling strength (g), detuning (omega_0/omega_c), deformation parameter (lambda) ranging from 0 to 1, bath temperature (beta), and Hilbert space truncation (N_max).

**Assumptions / limitations.**

The analysis assumes a truncation of the Hilbert space (N_max) and considers vacuum or thermal baths.

**Figures summary.**

The figures (implied by tables) present convergence data for the intertwining residual, verification of the metric across various JC scenarios, a scan of the lambda-deformation showing PH and complex regimes, and critical-exponent fits for eigenvalue coalescence.

**Paper structure.**

The paper identifies the spectral anomaly, introduces the mathematical framework of pseudo-Hermiticity, presents numerical verification of the metric and its stability, analyzes the transition from JC to Rabi models, and discusses the scaling of exceptional points.

**Why it may be interesting.**

This is highly relevant for researchers in open quantum systems and quantum optics as it provides a fundamental structural reason (pseudo-Hermiticity) for the stability of real spectra in non-Hermitian generators, which is crucial for understanding memory kernels and dissipation.

</details>

<details><summary>Abstract</summary>

The Nakajima-Zwanzig projected Liouvillian QLQ, the generator of the exact memory kernel in open quantum dynamics, is manifestly non-Hermitian yet has been reported to possess a purely real spectrum in the Jaynes-Cummings model -- an anomaly unexplained since observation. We resolve this anomaly by showing that QLQ is pseudo-Hermitian in the Mostafazadeh sense: a positive-definite metric eta>0 exists such that (QLQ)^dag eta = eta (QLQ), forcing the spectrum to be real. The pseudo-Hermiticity is genuine: the Delta N = 0 and Delta N = +/-2 sectors are individually non-Hermitian (residuals 1.70 and 5.06, respectively), yet the global spectrum is protected by eta. The metric survives the bath-truncation limit (N_max = 3--20, matrix dimension up to 1764 x 1764) with intertwining residual <10^{-11}. A continuous deformation to the full Rabi model reveals a re-entrant pseudo-Hermitian phase with two exceptional-point boundaries, in which the metric condition number diverges. The result supplies a structural reason for Hardy-space analyticity of the memory kernel in the canonical quantum-optical model.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25749"></a>


### [Hierarchical Reconstruction of Time-arrow from Multi-time Correlations](http://arxiv.org/abs/2604.25749v1)

**Authors:** Yijia Cheng, Ruicheng Bao, Zhonghuai Hou

**Type:** both · **Category:** statistical mechanics · **PDF:** <https://arxiv.org/pdf/2604.25749v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `methods for driven-dissipative` **3/5** · `non-equilibrium dynamics` **3/5** · `entanglement & information structure` **2/5** · `quantum measurements` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25749_figures/2604.25749_fig1.jpg" width="500"><br>

<sub>FIG. 1. (a) From observations to observation slices. The evolving observables are sampled at time points tk, forming observation slices. (b) From observation slices to reconstruction. Multi-time correlations are constructed from selections of each slice, then we can obtain the reconstruction. (c) Hierarchical reconstruction of the time-arrow. Each additional sampling time point (step) adds temporal information and tightens the reconstruction, bringing it closer to the whole time-arrow. When n →∞and ˙σinn = ˙σtrans = 0, the reconstruction reaches the true EPR.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25749_figures/2604.25749_fig2.jpg" width="500"><br>

<sub>FIG. 2. (a) Biomolecular process with many-to-many state- signal correspondence. Each microscopic state (circles in shades of blue) can emit photons detected in different color channels (colored arrows), with probabilities pmap J←i satisfying P</sub>

</details>

**Main problem.**

How to reconstruct the true Entropy Production Rate (EPR) and quantify thermodynamic irreversibility from partially observed, coarse-grained, or noisy experimental data.

**Main result.**

The authors establish a monotonic hierarchy of lower bounds on the EPR, where increasing the order of multi-time correlations systematically provides tighter bounds that converge to the true EPR under ideal conditions.

**Method.**

A hierarchical reconstruction framework using multi-time correlation functions of state observables, optimized via a search over time intervals and observation thresholds, and analyzed using the data-processing inequality.

**Summary.**

This paper presents a new method for estimating the entropy production rate (EPR) from experimental observations. By using higher-order multi-time correlations, the authors create a hierarchy of increasingly accurate lower bounds on the true thermodynamic irreversibility. They demonstrate that as more temporal information is included, the estimate converges toward the true EPR. The framework is particularly useful for systems with coarse-grained or noisy data, such as single-molecule fluorescence experiments.

<details><summary>Detailed structure</summary>

**Model / system.**

The framework is applied to Markovian jump processes and encompasses overdamped Langevin dynamics, with specific illustrative models involving three-state biomolecular processes and single-molecule Fluorescence Correlation Spectroscopy (FCS).

**Key observables.**

Multi-time correlation functions, Entropy Production Rate (EPR), and composition-like macroscopic observables.

**Important parameters / regimes.**

Number of observation slices (n), time interval (delta t), intermediate measurement times (qk), and the recoloring matrix (R) representing observation ambiguity.

**Assumptions / limitations.**

Assumes non-equilibrium steady states (NESS), 'composition-like' observables with constant sums, and stationarity of the processes.

**Figures summary.**

Figure 1 illustrates the transition from raw observables to multi-time correlations and the hierarchical tightening of bounds; Figure 2 shows the impact of observation ambiguity (recoloring) and the convergence of the hierarchy; Figure S1 shows the optimization landscape for parameters.

**Paper structure.**

The paper introduces the problem of EPR estimation, defines the mathematical framework for multi-time correlation reconstruction, proves the hierarchical lower-bound property using the data-processing inequality, demonstrates optimization strategies for time intervals, and compares the method's performance against existing bounds like the pseudo-EPR.

**Why it may be interesting.**

This work provides a systematic way to extract thermodynamic information from time-series data, which is highly relevant for characterizing dissipation and irreversibility in open quantum systems and driven many-body dynamics where full state knowledge is unavailable.

</details>

<details><summary>Abstract</summary>

The entropy production rate (EPR), a key measure of thermodynamic irreversibility in stochastic thermodynamics, is difficult to determine directly in experiments, motivating lower-bound-based estimation from observations. However, a systematic framework for organizing increasing amounts of the irreversibility information in experimental state observables into progressively tighter bounds remains lacking. Here, we show that multi-time correlations of a class of state observations naturally encode this information to provide a hierarchy. By defining a reconstruction operation as a combination of correlations, we obtain a sequence of lower bounds on the EPR. Correlations of higher order capture the thermodynamic information at greater temporal depth, thereby capturing more irreversibility and yielding tighter bounds. Under ideal conditions, this hierarchy converges to the full EPR in the limit of infinitely dense observations over a finite time window.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25245"></a>


### [Hierarchy of entropy production and thermodynamic trade-off relations in non-Markovian systems](http://arxiv.org/abs/2604.25245v1)

**Authors:** Ken Funo, Tan Van Vu, Keiji Saito

**Type:** theory · **Category:** statistical mechanics · **PDF:** <https://arxiv.org/pdf/2604.25245v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `methods for driven-dissipative` **3/5** · `non-equilibrium dynamics` **3/5** · `correlated / nonlocal dissipation` **2/5** · `entanglement & information structure` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25245_figures/2604.25245_fig1.jpg" width="500"><br>

<sub>FIG. 1. Hierarchy of entropy production under Markovian embedding. a Original non-Markovian description (1) with the entropy production Σ and heat Qsys based on system observables. b Equivalent Markovian embedded description (3), in which the bath is given by auxiliary modes A and a residual Markovian bath. The inner system-bath boundary recovers (Σ, Qsys), whereas the outer embedding boundary gives (Σemb, Qemb). c The difference between Σ and Σemb is the non-negative memory contribution Σmem between the system and auxiliary modes, yielding the hierarchy Σ ≥Σemb (5). We plot Σ and Σemb by varying a parameter ϵ that controls Σmem (see Methods for details).</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25245_figures/2604.25245_fig2.jpg" width="500"><br>

<sub>FIG. 2. Memory-assisted heat exchange with sup- pressed dissipation. a Schematic of the model. b Nu- merical plot showing the scaling of R τ 0 dt| ˙Qsys| = O(1) (blue curve) and R τ 0 dt| ˙Qemb| = O(ϵ) (black curve). c Plot of ˙Qsys(t) (blue curve) and ˙Qemb(t) (red curve), by choosing ϵ = 1, 0.1, 0.01 (dashed, dashdot, solid curves, respectively). A near-reversible exchange of heat between the system and auxiliary modes is realized in the limit of ϵ →0, while dis- sipation is strongly suppressed, as ˙Qemb and Σ scale as O(ϵ) (see also Fig. 1c).</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25245_figures/2604.25245_fig3.jpg" width="500"><br>

<sub>FIG. 3. Effect of memory on the transient TUR. a Precision-to-dissipation ratio Q defined in Eq. (16) as a function of the coupling c to the non-Markovian bath. The ratio can be enhanced relative to the Markovian limit c = 0. b The entropy production Σ (black solid curve) and apparent Markovian entropy production ΣM (orange dashed curve); their separation reflects the negative correction ΣNM ≤0. c Variance of the current Var[J S τ ]. The green shaded region marks the range of c for which memory suppresses both Σ and Var[J S τ ] relative to the Markovian limit c = 0.</sub>

</details>

**Main problem.**

The paper investigates how non-Markovian memory effects modify fundamental thermodynamic trade-off relations, such as the Thermodynamic Uncertainty Relation (TUR), speed limits, and power-efficiency trade-offs.

**Main result.**

The authors establish a hierarchy of entropy production where the true non-Markovian entropy production upper bounds that of its Markovian embedding, and use this to derive non-Markovian extensions of key thermodynamic bounds.

**Method.**

The study employs a Markovian embedding technique to represent non-Markovian dynamics as an enlarged Markovian system, using relative entropy and the Cauchy-Schwarz inequality to decompose and bound entropy production.

**Summary.**

This paper establishes a fundamental hierarchy of entropy production for non-Markovian systems by using a Markovian embedding technique. It proves that the entropy production of a non-Markovian system is always greater than or equal to its embedded Markovian counterpart. Using this hierarchy, the authors derive new versions of the Thermodynamic Uncertainty Relation, thermodynamic speed limits, and power-efficiency trade-offs. The results show that memory effects can be exploited to enhance the precision of currents relative to dissipation. The findings apply to both classical Langevin dynamics and quantum master equations.

<details><summary>Detailed structure</summary>

**Model / system.**

The model consists of non-Markovian open systems described by generalized Langevin dynamics (Zwanzig model) coupled to structured Gaussian baths, including both underdamped and overdamped regimes and extensions to the quantum regime via the GKSL master equation.

**Key observables.**

Entropy production, heat current, power, efficiency, Thermodynamic Uncertainty Relation (TUR) precision, and thermodynamic speed limits.

**Important parameters / regimes.**

Memory kernel, spectral density (Drude-Lorentz, super-Ohmic), temperature, coupling strength, and the underdamped/overdamped regimes.

**Assumptions / limitations.**

The derivation assumes specific initial conditions, such as the system and bath being in a conditional thermal state or a product state with vanishing initial interaction.

**Figures summary.**

Figure 1 illustrates the entropy production hierarchy and decomposition into embedded and memory-induced parts; Figure 2 shows memory-assisted heat exchange with suppressed dissipation; Figure 3 demonstrates the application of the current definition in a harmonic potential.

**Paper structure.**

The paper introduces the problem of memory-induced irreversibility, develops the Markovian embedding framework, establishes the entropy production hierarchy, derives various non-Markovian thermodynamic trade-off relations, and discusses extensions to the quantum regime and specific bath models.

**Why it may be interesting.**

This paper is highly relevant for researchers in open quantum systems as it provides a quantitative framework to treat bath memory as a thermodynamic resource and establishes new bounds for precision and efficiency in non-Markovian environments.

</details>

<details><summary>Abstract</summary>

Non-Markovian dynamics arise when a system is coupled to a bath with finite correlation time, giving rise to memory effects that allow the bath to temporarily store and return excitations. However, how memory modifies irreversibility and whether it can be exploited to improve thermodynamic performance is not well established. We address this question by employing a Markovian embedding of generalized Langevin dynamics, in which bath memory is encoded in auxiliary modes and irreversible dissipation in a residual Markovian bath. Here we show that the entropy production defined for the original non-Markovian system upper bounds that of the embedded system, thereby establishing a hierarchy of entropy production under Markovian embedding. Leveraging this hierarchy, we derive non-Markovian extensions of the thermodynamic uncertainty relation, speed limit, and power-efficiency trade-off. For underdamed generalized Langevin systems, sufficiently structured baths allow finite heat currents at vanishingly small entropy production, whereas Carnot efficiency at finite power remains unattainable for ordinary spectral densities. In the overdamped regime, memory effects can simultaneously reduce entropy production and current fluctuations, thereby enhancing the precision-to-dissipation ratio. We further discuss the extension of the hierarchy to generic bath models and the quantum regime. These results provide a quantitative framework for exploiting memory as a thermodynamic resource and for designing energy-efficient protocols in structured environments.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24976"></a>


### [Nonlocal correlations for bosonic fields in black hole quantum atmosphere](http://arxiv.org/abs/2604.24976v1)

**Authors:** Adam Z. Kaczmarek, Johann Gil, Zygmunt Bąk, Ewa A. Drzazga-Szczȩśniak, Dominik Szczȩśniak

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.24976v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `entanglement & information structure` **3/5** · `correlated / nonlocal dissipation` **2/5** · `non-equilibrium dynamics` **2/5** · `quantum measurements` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.24976_figures/2604.24976_fig1.jpg" width="500"><br>

<sub>FIG. 1: (A) The measurement-induced nonlocality (MIN) for the physically accessible bosonic quantum modes as a function of the scaled distance (r/rH) and (B) as a function of scaled temperature THH/TH, for the selected values of the so-called Hartle-Hawking constant (DHH) and Ω= 1.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24976_figures/2604.24976_fig2.jpg" width="500"><br>

<sub>FIG. 2: (A)-(D) The measurement-induced nonlocality of the physically accessible bosons (MIN(ρABI)) on a plane characterized by the distance from a black hole (r) and the event horizon size (rH). The results are depicted for the set of selected values of constant (DHH ∈{23.03, 40, 60, 80}). The diagrams are plotted for the Ω= 1.</sub>

</details>

**Main problem.**

Investigating how the 'quantum atmosphere' (the spatially extended thermal region surrounding a black hole) influences nonlocal quantum correlations in bosonic fields.

**Main result.**

Bosonic nonlocal correlations exhibit a pronounced degradation at a finite radial distance from the event horizon and eventually vanish, showing a more sensitive response to radiation compared to fermionic systems.

**Method.**

The study uses Measurement-Induced Nonlocality (MIN) as a quantifier, employing a single-mode approximation and Bogoliubov-style transformations within the Kruskal basis to analyze the Hartle-Hawking vacuum.

**Summary.**

This paper examines how the thermal environment of a black hole's 'quantum atmosphere' affects nonlocal correlations in bosonic fields. Unlike fermionic fields, which show a gradual degradation due to the Pauli exclusion principle, bosonic fields exhibit a much more rapid loss of nonlocality at a specific radial distance. The researchers found that as the thermal effects increase, the region where quantum correlations can be effectively utilized shrinks. This suggests that while bosonic systems are highly sensitive probes of black hole radiation, they are also more easily decohered by the surrounding environment.

<details><summary>Detailed structure</summary>

**Model / system.**

A bipartite system of two observers (Alice and Bob) sharing a maximally entangled Bell state of a massless bosonic scalar field in a Schwarzschild black hole spacetime, specifically within the Hartle-Hawking vacuum.

**Key observables.**

Measurement-Induced Nonlocality (MIN)

**Important parameters / regimes.**

Scaled radial distance (r/rH), scaled Hartle-Hawking temperature (THH/TH), and the Hartle-Hawking constant (DHH).

**Assumptions / limitations.**

The study assumes a massless scalar field, a Schwarzschild black hole geometry, and utilizes a single-mode approximation for the bosonic bipartite states.

**Figures summary.**

Figure 1 shows MIN as a function of normalized radius and scaled temperature; Figure 2 displays the MIN on a plane of distance (r) and horizon size (rH) for various DHH values, illustrating the shrinkage of the correlation region.

**Paper structure.**

The paper introduces the concept of the quantum atmosphere, defines the bosonic field model in Schwarzschild spacetime, applies the MIN quantifier to evaluate correlations, compares bosonic results to previous fermionic studies, and concludes with the implications for using bosonic probes.

**Why it may be interesting.**

It explores how curved spacetime and thermal environments (open quantum system dynamics) affect entanglement and nonlocality, specifically highlighting how different quantum statistics (Bose vs. Fermi) lead to different degradation patterns in quantum correlations.

</details>

<details><summary>Abstract</summary>

Recent theoretical studies propose that Hawking radiation may not emerge strictly at the event horizon but rather from the spatially extended region surrounding a black hole, commonly referred to as the quantum atmosphere. In this work, we explore how this concept influences nonlocal quantum correlations in a bosonic bipartite system located at certain distance from a Schwarzschild black hole. By employing the measurement-induced nonlocality (MIN), as a quantifier of quantum correlations, we analyze the response of bosonic fields to the thermal and geometric characteristics associated with the Hartle-Hawking vacuum. In this manner, we extend previous studies that primarily focused on the fermionic systems. Our results reveal that, when quantum atmosphere is taken into account, the behavior of MIN departs from its conventional near-horizon profile. In particular, bosonic nonlocal correlations are found to exhibit a pronounced degradation at a finite radial distance from the event horizon and to ultimately vanish as scaled distance increases further. To some extent this behavior contrasts with the previously considered fermionic case, indicating that bosonic fields provide potentially stronger response to the quantum atmosphere.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25475"></a>


### [Polarization-preserving wavefront rotator](http://arxiv.org/abs/2604.25475v1)

**Authors:** Suman Karan, Aman Srivastava, Pratham Sachin Todkar, Anand K. Jha

**Type:** both · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25475v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `interference shaping light` **3/5** · `quantum optics experiment` **3/5** · `QC/QI experiment` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25475_figures/2604.25475_fig1.jpg" width="500"><br>

<sub>Fig. 1. Three-dimensional model of the home-built polarization-preserving wavefront rotator (PPWR) device for wavefront rotation. It consists of a K-mirror with two half- wave plates (HWP), HWP1 and HWP2, placed before and after the K-mirror, respectively. Both HWPs and the K-mirror are mounted on a common rotation stage driven by a stepper mo- tor. The HWPs rotate at half the rotation angle of the K-mirror. The inset shows the conceptual schematic.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25475_figures/2604.25475_fig2.jpg" width="500"><br>

<sub>Fig. 2. Numerically simulated plot of mean polarization er- rors ¯D in % as a function of the retardance errors ϵ1 and ϵ2 of HWP1 and HWP2, respectively, for a linearly polarized input state. The yellow dot marks the operating point corresponding to commercially available Thorlabs HWPs.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25475_figures/2604.25475_fig3.jpg" width="500"><br>

<sub>Fig. 3. Schematic of the experimental setup to measure the transmitted state of polarization at different rotation angles of the polarization-preserving wavefront rotator (PPWR) device. P1, P2: polarizers; Q1, Q2: quarter-wave plates.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25475_figures/2604.25475_fig4.jpg" width="500"><br>

<sub>Fig. 4. Poincaré sphere representation of the transmitted states of polarization at different rotation angles of the PPWR device for three different input states of polarization: (a) linear, (c) elliptical, and (e) circular. The corresponding normalized Stokes parameters are shown in (b), (d), and (f), respectively. The incident state of polarization in each case is shown in the inset.</sub>

</details>

**Main problem.**

Standard wavefront rotators like K-mirrors introduce rotation-dependent polarization changes, which limits their use in applications like astronomical derotation and OAM spectrum characterization in quantum optics.

**Main result.**

The authors demonstrate that placing half-wave plates before and after a K-mirror and rotating them at half the K-mirror's rotation angle makes the transmitted polarization state independent of the rotation angle.

**Method.**

The study uses Jones matrix analysis for theoretical proof and an experimental setup with a He-Ne laser, polarizers, and a K-mirror to validate the approach.

**Summary.**

This paper presents a new method for creating a polarization-preserving wavefront rotator. By placing half-wave plates before and after a K-mirror and rotating them at half the rotation angle of the mirror, the polarization change becomes independent of the rotation angle. This approach is universal and works for any wavefront rotator. Experimental results show a very low polarization error of approximately 1%, making it highly effective for precision applications in astronomy and quantum information science.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system is a Polarization-Preserving Wavefront Rotator (PPWR) consisting of a K-mirror sandwiched between two half-wave plates (HWPs) mounted on a common rotation stage.

**Key observables.**

Stokes parameters (S0, S1, S2, S3), Poincaré sphere geodesic distance (mean polarization error), and retardance error.

**Important parameters / regimes.**

K-mirror base angle (30 degrees), HWP rotation angle (half the K-mirror angle), and HWP retardance error (epsilon).

**Assumptions / limitations.**

The theoretical ideal assumes perfect half-wave plates (zero retardance error), while the experimental error is limited by the retardance imperfection of commercial HWPs.

**Figures summary.**

Fig 1 shows a 3D model of the PPWR device; Fig 2 plots simulated polarization error vs. HWP retardance error; Fig 3 shows the experimental setup for Stokes parameter measurement; Fig 4 shows Poincaré sphere representations of measured states and normalized Stokes parameters.

**Paper structure.**

The paper introduces the problem of polarization change in K-mirrors, presents a theoretical solution using a HWP sandwich, provides a mathematical proof via Jones matrices, describes the experimental implementation and setup, and concludes with error analysis and experimental validation.

**Why it may be interesting.**

This is highly relevant for quantum optics and photonic quantum technology, as it provides a universal method to rotate wavefronts (e.g., for OAM manipulation) without disturbing the polarization state of qubits or optical modes.

</details>

<details><summary>Abstract</summary>

A K-mirror rotates the wavefront of an incident optical field. However, the rotation always introduces polarization changes in the transmitted field. This is a serious concern for applications ranging from astronomical image derotation to orbital angular momentum spectrum characterization in photonic quantum technology. Recent efforts have shown that the polarization change can be minimized significantly, but these require either a very small base angle that limits the field of view, or mirrors with a customized refractive index. Making the transmitted polarization state completely independent of the rotation angle has remained an open problem. In this work, we show that placing half-wave plates before and after a K-mirror and rotating them synchronously at half the K-mirror rotation angle makes the polarization change in the transmitted field exactly independent of the rotation angle. This works for any wavefront rotator, any base angle, any mirror refractive index, and any input state of polarization. We experimentally demonstrate the approach using a K-mirror with a base angle of $30^{\circ}$, which gives the largest field of view among practical designs, and find a mean polarization error of ~1%, limited only by the retardance imperfection of commercially available half-wave plates. This has significant practical implications for applications that require precise wavefront rotation without polarization change.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25351"></a>


### [Spinodal-like scaling behavior after a temperature quench across the first-order phase transition in three-dimensional $q$-state Potts models](http://arxiv.org/abs/2604.25351v1)

**Authors:** Andrea Pelissetto, Davide Rossini, Ettore Vicari

**Type:** theory · **Category:** statistical mechanics · **PDF:** <https://arxiv.org/pdf/2604.25351v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `non-equilibrium dynamics` **3/5** · `non-equilibrium universality` **3/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25351_figures/2604.25351_fig1.jpg" width="500"><br>

<sub>Figure 1. Post-quench time evolution of the rescaled energy density E(t) for the 3D q = 6 Potts model, versus the time t for several values of δ and L. The data for different sizes and same δ approach an asymptotic curve, which provides an accurate approximation of the time evolution in the thermodynamic limit. Statistical errors are hardly visible in the figure.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25351_figures/2604.25351_fig2.jpg" width="500"><br>

<sub>Figure 2. Post-quench evolution of the q = 6 energy density E(t) in the thermodynamic limit versus ρ = (ln t)3/2δ. The vertical dashed line corresponds to the estimate ρs = 0.391(4) of the asymptotic crossing point (the interval between the dotted lines gives the uncertainty).</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25351_figures/2604.25351_fig3.jpg" width="500"><br>

<sub>Figure 3. The post-quench energy density E(t) versus ρr ≡(ρ −ρs) δ−θ, using the optimal values ρs = 0.391 and θ = 1.8. The data appear to approach an asymptotic scaling curve with decreasing δ.</sub>

</details>

**Main problem.**

Investigating the out-of-equilibrium spinodal-like scaling behavior in 3D systems following a temperature quench across a first-order phase transition.

**Main result.**

The study confirms that post-quench dynamics are driven by droplet nucleation, leading to a predicted scaling variable rho = (ln t)^(3/2 * delta) and a spinodal-like discontinuity in the energy density scaling function.

**Method.**

Monte Carlo simulations using a heat-bath algorithm with a checkerboard update scheme on a 3D q=6 Potts model.

**Summary.**

This paper investigates how a system behaves when suddenly cooled across a first-order phase transition in three dimensions. By studying the 3D q=6 Potts model, the authors show that the energy density follows a specific scaling law related to the time it takes for droplets to nucleate. Their results support a 'spinodal-like' scenario where the phase change is driven by the growth and merging of these droplets. This provides a clearer understanding of non-equilibrium dynamics in systems undergoing discontinuous phase transitions.

<details><summary>Detailed structure</summary>

**Model / system.**

A three-dimensional q-state Potts model (specifically q=6) with a Hamiltonian representing short-range interactions, undergoing a thermal first-order phase transition.

**Key observables.**

Rescaled energy density E(t) and the scaling variable rho = (ln t)^(3/2 * delta).

**Important parameters / regimes.**

The distance from the transition point delta = (beta/beta_fo) - 1, the scaling exponent kappa = 3/2, and the thermodynamic limit.

**Assumptions / limitations.**

The primary assumption is that the nucleation of smooth droplets is the dominant and slowest mechanism driving the post-quance phase change.

**Figures summary.**

Figure 1 shows energy density convergence to the thermodynamic limit; Figure 2 demonstrates a stable crossing point for the scaling variable rho; Figure 3 shows data collapse onto a single curve using a rescaled variable rho_r.

**Paper structure.**

The paper introduces the problem of post-quench dynamics, presents a scaling argument based on droplet nucleation, details the Monte Carlo numerical methodology, provides results for the 3D q=6 model, and concludes with the verification of the spinodal-like scenario.

</details>

<details><summary>Abstract</summary>

We study the out-of-equilibrium spinodal-like behavior of three-dimensional (3D) $q$-state Potts models (for $q\ge 3$), observed when the temperature is quenched across the first-order transition (FOT) point $β_{\rm fo}=T_{\rm fo}^{-1}$. We consider a standard quench protocol, in which high-temperature configurations, thermalized at $β_i<β_{\rm fo}$, are driven across the FOT by a purely relaxational dynamics at $β>β_{\rm fo}$. We focus on the emergence of spinodal-like behaviors in the thermodynamic limit, associated with the dynamic phase change. We argue that, if the nucleation of smooth droplets is the relevant mechanism of the post-quench phase change, for sufficiently small $β_{\rm fo}-β_i>0$, the time-dependent energy density should scale in terms of $ρ= (\ln t)^{3/2} δ$, where $δ= β/β_{\rm fo}-1$, with a discontinuity at a particular value $ρ=ρ_s>0$. This implies the emergence of a spinodal-like behavior, whose time scale $τ$ increases exponentially as $\ln τ\approx (ρ_s/δ)^{2/3}$ in the limit $δ\to 0^+$. We present a numerical analysis of the quench protocol in the 3D $q=6$ Potts model, which supports the above spinodal-like scenario.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25705"></a>


### [Universal Characterization of Classical Qubit Noise](http://arxiv.org/abs/2604.25705v1)

**Authors:** Yuan-De Jin, Zheng-Fei Ye, Wen-Long Ma

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25705v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `methods for driven-dissipative` **3/5** · `quantum measurements` **3/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25705_figures/2604.25705_fig1.jpg" width="500"><br>

<sub>FIG. 1. Schematic of a universal protocol for characterizing a classical stochastic noise process via sequential RIMs on a qubit. (a) A realization of the continuous stochastic noise process. (b) Direct sampling of the noise ﬁeld with sequential RIMs. (c) Evolution of the qubit during a single RIM with φ1 = π/2 and φ2 = π. The free evolution time τ in a RIM should be much shorter than the delay time ∆t.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25705_figures/2604.25705_fig2.jpg" width="500"><br>

<sub>FIG. 2. Reconstruction of (a) the two-point cumulant ˜C(2)(∆t1) and (b) noise spectrum S(1)(ω) of the OU process with three correlation times τC = 1, 0.5, 0.25 µs (red, green, blue line). Solid lines are theoretical results and dots are re- constructed from the RIM outcomes. The inset in (a) shows the three-point cumulant ˜C(3)(2∆t, ∆t2). The parameters are Γ = 1 MHz2, τ = 0.05 µs, ∆t = 0.1 µs, and Ns = 5 × 108.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25705_figures/2604.25705_fig3.jpg" width="500"><br>

<sub>FIG. 3. Reconstruction of (a) three-point cumulant ˜C(3)(∆t1, ∆t2) (MHz3) and (b) bispectrum of a non-Gaussian noise through our method. The noise is produced by three TLFs with the coupling strength λ = 119 kHz and switching rate {Wj} = {4.77, 21.35, 95.49} kHz. Note that the inac- cessible points with ∆t1 = 0, ∆t2 = 0 and ∆t1 = ∆t2 for the reconstructed cumulant are smoothed by the neighbor- hood values. The parameters are τ = 0.15 µs, ∆t=2 µs and Ns = 4 × 108.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25705_figures/2604.25705_fig4.jpg" width="500"><br>

<sub>FIG. 4. Non-Gaussian-to-Gaussian transition in a sparse bath containing Nt TLFs. Here we show the ideal (dashed lines) and reconstructed (points) two-point and three-point cumu- lants with (a-b) diﬀerent ¯ξ and (c-d) diﬀerent Nt. The cou- pling strength is λ = 207/√Nt kHz and the switching rate obeys a log-uniform distribution ranging from 4.77 kHz to 95.49 kHz. The parameters are τ = 0.15 µs, ∆t = 2 µs and Ns = 9 × 108.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25705_figures/2604.25705_fig5.jpg" width="500"><br>

<sub>FIG. 1. Reconstruction of (a) four-point cumulant slice C(4)(2∆t, ∆t2, ∆t3) and (b) trispectrum slice S(3)(ω1, ω2, 0) of a classical noise. The noise is produced by a single TLF with the coupling strength λ = 206 kHz and switching rate Wj = 63 kHz. Note that the inaccessible points are smoothed by the neighborhood values for the reconstructed cumulant. The parameters are τ = 0.25 µs, ∆t=1 µs and Ns = 5 × 108.</sub>

</details>

**Main problem.**

The need for a universal and efficient method to fully characterize classical stochastic noise processes (both Gaussian and non-Gaussian) that cause qubit dephasing without requiring complex dynamical decoupling pulse sequences.

**Main result.**

The authors propose a protocol using repetitive Ramsey interferometry measurements (RIMs) that can directly sample the noise field and reconstruct arbitrary-order correlation functions, including bispectra and trispectra.

**Method.**

A protocol of sequential Ramsey Interferometry Measurements (RIMs) where the phase difference between pulses is tuned to achieve either linear or quadratic response, allowing for the estimation of n-point noise correlations.

**Summary.**

The paper introduces a new method for characterizing qubit dephasing noise using repetitive Ramsey measurements. Unlike traditional spectroscopy, this method does not require complex dynamical decoupling sequences and can directly detect higher-order correlations like the bispectrum and trispectrum. It is shown to be effective for both Gaussian and non-Gaussian noise models and is robust against measurement errors and qubit decoherence. This offers a universal approach for noise spectroscopy across various quantum platforms.

<details><summary>Detailed structure</summary>

**Model / system.**

A single probe qubit subject to pure dephasing caused by a classical stochastic noise process beta(t). Specific noise models tested include the Gaussian Ornstein-Uhlenbeck process and an ensemble of non-Gaussian Two-Level Fluctuators (TLFs).

**Key observables.**

n-point correlation functions of measurement outcomes, n-point noise cumulants, noise power spectrum, bispectrum, and trispectrum.

**Important parameters / regimes.**

Short evolution regime (beta*tau << 1), phase difference (delta_phi), evolution time (tau), and delay time between cycles (delta_t).

**Assumptions / limitations.**

The noise is classical and stochastic with zero mean; the system operates in the short-evolution regime where the noise is approximately constant during the Ramsey time.

**Figures summary.**

Figure 1 shows the reconstruction of 4-point cumulants and trispectra; Figure 2 demonstrates the reconstruction of the 2-point correlation and spectrum for an OU process; Figure 3 shows 3-point cumulant and bispectrum reconstruction for TLFs; Figure 4 shows the transition from non-Gaussian to Gaussian noise.

**Paper structure.**

Introduction of the noise characterization problem, description of the RIM protocol and mathematical framework for n-point correlations, derivation of the direct sampling condition and handling of repeated time indices, numerical validation using Gaussian (OU) and non-Gaussian (TLF) models, and an analysis of robustness against measurement errors.

**Why it may be interesting.**

This paper provides a powerful tool for open quantum systems researchers to characterize complex, non-Gaussian environments using simple measurement sequences, bypassing the need for complex pulse engineering.

</details>

<details><summary>Abstract</summary>

We propose a general method to fully characterize a classical stochastic noise process causing qubit dephasing through repetitive Ramsey interferometry measurements (RIMs) on the qubit. Compared to filter-function-based spectroscopy, our method does not require complicated dynamical decoupling pulses and can directly detect arbitrary-order correlation functions of such noise processes. We show that each RIM with a short evolution time and suitably chosen control pulses can perform a direct sampling of the noise field and the $n$-point correlations of the RIM outcomes are proportional to the $n$-point correlation functions of the noise processes. Then we numerically demonstrate this method for characterizing two typical examples of classical noises, including the Ornstein-Uhlenbeck processes producing Gaussian noises and an ensemble of TLFs producing non-Gaussian noises. Our method is independent of qubit lifetime and robust against qubit decoherence and measurement errors, thus offering a universal and efficient protocol for qubit noise spectroscopy across diverse platforms.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24912"></a>


### [Data-Driven Hamiltonian Reduction for Superconducting Qubits via Meta-Learning](http://arxiv.org/abs/2604.24912v1)

**Authors:** Arielle Sanford, Andrew T. Kamen, Frederic T. Chong, Andy J. Goldschmidt

**Type:** both · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.24912v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `QC/QI experiment` **3/5** · `methods for driven-dissipative` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.24912_figures/2604.24912_fig1.jpg" width="500"><br>

<sub>Fig. 1. (a) Circuit diagram of the transmon-coupler-transmon architecture: two frequency-tunable transmon qubits (red) capacitively coupled to a tunable coupler (blue). Each mode is characterized by its charging and Josephson energies Ei C, Ei J, with capacitive coupling energies Ejk C setting the inter-mode couplings. The qubit and coupler frequencies are tunable via the SQUID fluxes Φq1, Φq2, Φc1. (b) Effective two-qubit description after coupler elimination: the qubits acquire an effective exchange coupling geff and a residual ZZ interaction ζ.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24912_figures/2604.24912_fig2.jpg" width="500"><br>

<sub>Fig. 2. HAML pipeline: schematic of the two-stage framework. Left: during training, a neural network with shared parameters θ learns to predict effective Hamiltonian coefficients from simulated device parameters and control pulses. Right: during adaptation, the trained network is frozen, and only the device parameter vector ηpred is optimized using hardware measurements.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24912_figures/2604.24912_fig3.jpg" width="500"><br>

<sub>Fig. 3. Raw informativeness of every candidate (initial state, observable) pair, computed as the variance of the predicted expectation value across N = 500 random draws of (η, ϕ) from the training distribution. Rows: candidate initial states, restricted to tensor products of single-qubit states. Columns: single- and two-qubit Pauli observables (excluding the identity). Darker cells are uninformative; brighter cells are sensitive to the learned parameters.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24912_figures/2604.24912_fig4.jpg" width="500"><br>

<sub>Fig. 4. Greedy selection trajectory. Each row corresponds to one (initial state, observable) candidate, ordered by selection (top = first picked); rows below the selected set show the highest-informativeness candidates that were not selected. Gray bars: raw informativeness. Colored bars: marginal informativeness after orthogonalization against previously-selected pairs.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.24912_figures/2604.24912_fig5.jpg" width="500"><br>

<sub>Fig. 5. Predicted vs ground-truth projected Pauli coefficients on 10 held-out, adapted devices. Shown are 300 random control points per device. Color encodes device; dashed line is y = x.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.24912_figures/2604.24912_fig6.jpg" width="500"><br>

<sub>Fig. 7. Infidelity gain of HAML over SWPT, (ISWPT−IFloor)/(ILearned−Ifloor), with fidelity floor Ifloor, as a function of effective coupling geff, per held-out device.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.24912_figures/2604.24912_fig7.jpg" width="500"><br>

<sub>Fig. 6. Perturbative expansion ratio |gqic1/∆qic1| for i = 1 (left) and i = 2 (right), across the 10 held-out devices, at the fast-gate operating flux Φc1 = 1.35. Bars are sorted ascending; bar color identifies the device.</sub>

</details>

**Main problem.**

Accurately mapping the complex multi-mode dynamics of superconducting processors (including couplers and resonators) to an effective qubit-level Hamiltonian, especially in regimes where traditional Schrieffer-Wolff perturbation theory fails.

**Main result.**

The HAML framework achieves a 6x improvement in absolute error and an 8x improvement in relative error compared to Schrieffer-Wolff theory, effectively capturing parasitic ZZ interactions and maintaining accuracy in strong-hybridization regimes.

**Method.**

A two-phase meta-learning framework (HAML) consisting of an offline supervised training phase on simulated devices and an online adaptation phase using a small number of hardware measurements and L-BFGS optimization.

**Summary.**

The paper presents HAML, a meta-learning framework designed to rapidly adapt effective Hamiltonian models for superconducting qubits. By training on simulated data and adapting to real hardware with minimal measurements, the method bypasses the need for complex analytical perturbation theory. It excels in regimes where traditional methods break down, such as strong hybridization and parasitic ZZ interactions. This approach offers a scalable solution for the calibration and control of near-term quantum processors.

<details><summary>Detailed structure</summary>

**Model / system.**

A transmon-coupler-transmon architecture consisting of two frequency-tunable qubits capacitively coupled to a tunable coupler, modeled by an 8-level multi-mode Hamiltonian under the rotating wave approximation.

**Key observables.**

Effective Pauli coefficients (ZI, IZ, XX, YY, ZZ) and expectation values of single- and two-qubit Pauli operators.

**Important parameters / regimes.**

Qubit and coupler frequencies, Josephson and charging energies, capacitive coupling energies, and SQUID fluxes; specifically focuses on the transition from dispersive to strong-hybridization regimes.

**Assumptions / limitations.**

The framework assumes that the dynamics can be effectively captured by a reduced qubit subspace and relies on the availability of simulated data for the initial training phase.

**Figures summary.**

Figure 1 shows the device architecture and effective model; Figure 2 illustrates the HAML training and adaptation pipeline; Figure 3 and 4 demonstrate measurement selection strategies; Figure 5 shows prediction accuracy on held-out devices; Figure 6 and 7 show performance in the strong-hybridization regime and error reduction compared to SWPT.

**Paper structure.**

The paper introduces the problem of Hamiltonian reduction, presents the HAML meta-learning architecture (training and adaptation phases), details the measurement selection strategy, compares performance against Schrieffer-Wolff theory, and evaluates scalability and error characteristics.

**Why it may be interesting.**

This is highly relevant for researchers in open quantum systems and quantum optics as it provides a data-driven way to handle complex, multi-mode dynamics and strong coupling without relying on the validity of perturbative expansions.

</details>

<details><summary>Abstract</summary>

We introduce HAML (Hamiltonian Adaptation via Meta-Learning), a framework for fast online adaptation of effective Hamiltonian models of superconducting quantum processors. HAML proceeds in two phases. A supervised training phase uses an ensemble of simulated devices to learn an offline map from control inputs and device parameters to effective Hamiltonian coefficients. An online adaptation phase then uses a small number of hardware-accessible measurements to identify the unknown parameters of a new device. By training directly against effective two-qubit coefficients extracted from full multi-mode simulations, HAML implicitly learns the reduction from full multi-mode Hamiltonians to effective qubit descriptions without invoking perturbation theory. We further show that a variance-maximizing greedy selection of measurement configurations boosts online adaptation efficiency. We demonstrate HAML on a transmon-coupler-transmon system, recovering effective two-qubit coefficients across a wide range of operating regimes, including parameter regions where Schrieffer-Wolff perturbation theory (SWPT) breaks down. This establishes a scalable, sample-efficient approach to Hamiltonian reduction and characterization for near-term quantum processors, with direct implications for calibration, control, and error mitigation.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25910"></a>


### [Heralding probability optimization for nonclassical light generated by photon counting measurements on multimode Gaussian states](http://arxiv.org/abs/2604.25910v1)

**Authors:** Jaromír Fiurášek

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25910v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `quantum measurements` **3/5** · `Keldysh / 2PI / non-Gaussian methods` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25910_figures/2604.25910_fig1.jpg" width="500"><br>

<sub>FIG. 1. Scheme for generation of single-mode nonclassical state of light |ψN⟩with stellar rank N by photon counting measure- ments on m heralding modes of m + 1-mode Gaussian state. The Gaussian state has vanishing coherent displacements and can be generated from m+1 single-mode squeezed vaccuum states with suitably chosen squeezing constants rj by their interference in optical interferometer IF.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25910_figures/2604.25910_fig2.jpg" width="500"><br>

<sub>FIG. 2. Scheme for generation of single-mode squeezed superpositions of Fock states. The state generated from Gaussian core state |G⟩can be squeezed by unitary squeezing operation ˆS(r) acting on mode a0. This is equivalent to utilizing a different input multimode Gaussian state | ˜G⟩with modified squeezing properties.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25910_figures/2604.25910_fig3.jpg" width="500"><br>

<sub>FIG. 3. Results of maximization of the heralding probability pS for balanced superposition target states |ψ6⟩(a,b) and |ψ7⟩ (c,d) defined in Eq. (53). For each heralding pattern (n1, n2) considered, six configurations (s1, s2, ν) generating the state were identified and the maximum achievable heralding probability pS for each configuration is plotted. Note that all the plotted pS are nonzero, although some of them are very small. See also Table I in the Appendix B.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25910_figures/2604.25910_fig4.jpg" width="500"><br>

<sub>FIG. 4. (a) Dependence of the heralding probability pS on X1 and X2 is plotted for target state |ψ6⟩, heralding pattern (4, 2), and the optimal configuration s1 = −0.072 −1.199i, s2 = −0.960 −0.109i, ν = 0.859 + 0.913i. The set of points satisfying the squeezing constraint D = 0 is plotted for this configuration in panel (b) for two different squeezing values µ2 = 0.25 (blue solid lines) and µ2 = 0.65 (green dashed line). The red curve represents the physical boundary in the (X1, X2) plane where the largest eigenvalue of AA† becomes equal to 1.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25910_figures/2604.25910_fig5.jpg" width="500"><br>

<sub>FIG. 5. Maximum heralding probability for target state |ψ6⟩defined in Eq. (53) when the maximum squeezing is set to µ2 = tanh2 rmax. The results are plotted for two heralding patterns (3,3) (blue solid line) and (4,2) (red dashed line).</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25910_figures/2604.25910_fig6.jpg" width="500"><br>

<sub>FIG. 6. Optimal heralding probability pS of generation of the entangled two-mode state |Φ(w)⟩is plotted as function of the state parameter w.</sub>

</details>

**Main problem.**

Optimizing the heralding probability for the conditional preparation of non-classical (non-Gaussian) states of light using photon-counting measurements on multimode Gaussian states.

**Main result.**

The authors demonstrate that maximizing the heralting probability can be formulated as solving a system of polynomial equations, providing an efficient way to find optimal configurations and incorporate squeezing constraints.

**Method.**

The optimization is framed using the stellar (Bargmann) representation and solved via algebraic techniques such as Gröbner basis construction and homotopy continuation.

**Summary.**

This paper presents a new method for maximizing the success rate (heralding probability) of generating non-classical light. By transforming the optimization problem into a system of polynomial equations, the authors enable efficient calculation of optimal squeezing and detection parameters. The approach is versatile enough to handle constraints on available squeezing and can be applied to various target states, including Fock state superpositions and single-rail qubits. This is crucial for improving the efficiency of optical quantum information processing.

<details><summary>Detailed structure</summary>

**Model / system.**

The system consists of multimode squeezed Gaussian states where non-Gaussian states (like Fock state superpositions or GKP states) are generated via photon-number measurements on a subset of modes.

**Key observables.**

Heralding probability (p_S), photon number pattern, and photon number parity.

**Important parameters / regimes.**

Squeezing parameters (r_j), photon number pattern (n_1, n_2, ...), and available single-mode quadrature squeezing limits.

**Assumptions / limitations.**

Focuses on Gaussian states with vanishing coherent displacements and assumes the signal mode is directly coupled to all heralding modes.

**Figures summary.**

Figure 1 shows the scheme for generating single-mode nonclassical states; Figure 2 illustrates the generation of squeezed superpositions of Fock states; Figure 3 plots maximum heralding probability for various target states; Figure 4 shows the dependence of p_S on damping parameters.

**Paper structure.**

The paper introduces the problem of state preparation, develops a mathematical framework using polynomial equations, applies the method to various target states (single-mode and multi-mode), incorporates squeezing constraints, and provides specific numerical examples and applications to single-rail qubits.

**Why it may be interesting.**

This is highly relevant for quantum optics and photonic quantum computing, as it provides a scalable mathematical tool to optimize the success rates of generating essential non-Gaussian resources like GKP and cat states.

</details>

<details><summary>Abstract</summary>

Generation of highly non-classical quantum states of light is essential for optical quantum information processing and quantum metrology. Given the lack of sufficiently strong nonlinear interactions between optical fields, the commonly employed optical quantum-state preparation schemes are conditional, based on nonlinearity induced by heralding photon number measurement on a part of a multimode squeezed Gaussian state. Development and optimization of such probabilistic quantum-state engineering schemes represents one of the central challenges in current quantum optics. As technology advances and experiments progress to detection of higher numbers of photons, the maximization of the heralding probability becomes essential to ensure sufficiently high state-preparation rates. Here, we show that for the conditional quantum state preparation schemes based on Gaussian states and photon number measurements the maximization of the heralding probability can be formulated as finding solution to a system of polynomial equations, which offers an efficient way to find the optimal configuration and allows us to apply techniques dedicated specifically to solving such systems of equations. Our approach can seamlessly incorporate bounds on the available single-mode quadrature squeezing, which is highly experimentally relevant. We mainly consider generation of finite superpositions of Fock states but show that the approach can be straightforwardly extended to generation of squeezed superpositions of Fock states. We focus on Gaussian states with vanishing coherent displacements, hence the conditionally generated states have well defined photon number parity. We illustrate our general methodology on examples of generation of single-mode and two-mode states with two heralding modes.

</details>

<sub>[↑ back to top](#top)</sub>
