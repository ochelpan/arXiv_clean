# Daily arXiv Report

[← Index](index.md)

[← Previous](papers_12.md)
[Next →](papers_14.md)

## Papers 241–260


<a id="paper-2604.25807"></a>


### [Proof of the Error Scaling for Universally Robust Dynamical Decoupling Sequences](http://arxiv.org/abs/2604.25807v1)

**Authors:** Domenico D'Alessandro, Phattharaporn Singkanipa, Daniel Lidar

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25807v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25807_figures/2604.25807_page2.jpg" width="500"><br>

<sub>Low-resolution page preview, page 2</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25807_figures/2604.25807_page3.jpg" width="500"><br>

<sub>Low-resolution page preview, page 3</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25807_figures/2604.25807_page4.jpg" width="500"><br>

<sub>Low-resolution page preview, page 4</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25807_figures/2604.25807_page5.jpg" width="500"><br>

<sub>Low-resolution page preview, page 5</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25807_figures/2604.25807_page6.jpg" width="500"><br>

<sub>Low-resolution page preview, page 6</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25807_figures/2604.25807_page7.jpg" width="500"><br>

<sub>Low-resolution page preview, page 7</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25807_figures/2604.25807_page8.jpg" width="500"><br>

<sub>Low-resolution page preview, page 8</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25807_figures/2604.25807_page9.jpg" width="500"><br>

<sub>Low-resolution page preview, page 9</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25807_figures/2604.25807_page10.jpg" width="500"><br>

<sub>Low-resolution page preview, page 10</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25807_figures/2604.25807_page11.jpg" width="500"><br>

<sub>Low-resolution page preview, page 11</sub>

</details>

**Main problem.**

The paper seeks to provide a rigorous mathematical proof for the claimed error scaling of Universally Robust (URn) dynamical decoupling sequences, specifically proving that for even n, the fidelity error scales as O(epsilon^n).

**Main result.**

The authors establish that the URn phase prescription satisfies the necessary and sufficient conditions to cancel error coefficients up to order n-1, and they identify the specific leading-order error term at order epsilon^n.

**Method.**

The work employs a Taylor series expansion of the Hilbert-Schmidt overlap, using algebraic tools like trace identities, matrix-product generating functions, and Fourier-type identities to prove the vanishing of error coefficients.

**Summary.**

This paper provides the first rigorous mathematical proof that Universally Robust (URn) dynamical decoupling sequences achieve high-order error suppression. By analyzing the Taylor expansion of the quantum fidelity, the authors prove that for even-length sequences, error coefficients are cancelled up to order n-1. This establishes that the fidelity error scales as O(epsilon^n). The work also identifies the specific mathematical structure responsible for this robustness and shows that the error cannot be suppressed beyond order n.

<details><summary>Detailed structure</summary>

**Model / system.**

The study uses an effective pulse-cycle model for quantum information processing, involving a sequence of n imperfect pulses separated by free evolution periods, where pulses are characterized by an error parameter epsilon and controlled phases.

**Key observables.**

Fidelity (F) and the normalized Hilbert-Schmidt overlap (G(epsilon)).

**Important parameters / regimes.**

Error parameter epsilon, number of pulses n (even), control phases phi_k, and rotation angles alpha and beta.

**Assumptions / limitations.**

The sequence length n is an even integer; the environment's correlation time is longer than the sequence duration (coherent evolution); and pulses are identical except for controlled phase shifts.

**Paper structure.**

The paper begins by defining the URn problem and the pulse model, then moves to establishing necessary and sufficient conditions for coefficient cancellation via Taylor expansion, followed by the use of combinatorial and Fourier-type identities to prove the vanishing of specific error terms, and concludes by identifying the non-vanishing leading-order error.

**Why it may be interesting.**

This provides the fundamental mathematical foundation for a class of robust control sequences used to protect qubits from noise, which is critical for scaling quantum computing and improving the coherence of quantum sensors.

</details>

<details><summary>Abstract</summary>

Universally robust dynamical decoupling (UR$n$) sequences were proposed to compensate pulse imperfections arising from arbitrary experimental parameters while achieving high-order error suppression with only a linear increase in the number of pulses. Although their performance was supported by analytical arguments, numerical simulations, and experiments, a complete mathematical proof of the claimed order of error compensation has been absent. In this work, we present a rigorous proof for UR$n$ DD sequences with even $n$. Using a series expansion of a quantity whose modulus is the fidelity $F$, we derive necessary and sufficient conditions for the cancellation of its coefficients up to, but not including, order $n$. The UR$n$ phase prescription satisfies these conditions, and therefore $1-F=O(ε^n)$. Our results establish the UR$n$ construction on firm analytical grounds and clarify the structure responsible for its high-order robustness.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25573"></a>


### [Quantum annealing inspired algorithms for the NISQ Era](http://arxiv.org/abs/2604.25573v1)

**Authors:** Rijul Sachdeva, Vrinda Mehta, Manpreet Singh Jattana, Kristel Michielsen, Fengping Jin

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25573v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25573_figures/2604.25573_fig1.jpg" width="500"><br>

<sub>FIG. 1: Success probability of AQA with first-order approximation: variation with time step (τ) and number of steps (p). Red lines denote constant total annealing time τ p.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25573_figures/2604.25573_fig2.jpg" width="500"><br>

<sub>FIG. 3: Success probability of QAOA initialized with AQA parameters: τ ∈[0.05,1.5], p ∈[10,1000], capped at 8000 function evaluations.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25573_figures/2604.25573_fig3.jpg" width="500"><br>

<sub>FIG. 2: Overlap of the instantaneous state of an 8-variable system evolving under AQA with the (a) ground state E0(s) and (b) the lowest three energy states of the instantaneous QA Hamiltonian H(s) given by Eq. (3) for ta = 25 and various τ.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25573_figures/2604.25573_fig4.jpg" width="500"><br>

<sub>FIG. 4: Expectation value of H(sj) with respect to the final state at each step j under the EHQO algorithm using the QAOA ansatz with p = 25 and Ns = 10,20.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25573_figures/2604.25573_fig5.jpg" width="500"><br>

<sub>FIG. 5: Overlaps in EHQO for an 8 and 12 -qubit Hamiltonian of the initial wavefunction (i.e., using parameters from the previous optimization process) with the ground state and the first excited state of the intermediate Hamiltonians. Also depicted are the final success probabilities after optimization at each point.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25573_figures/2604.25573_fig6.jpg" width="500"><br>

<sub>FIG. 7: Scaling of mean success probability for 100 instances of 8-18 qubit 2-SAT problems for AQA (green triangles) and EHQO (blue circles).</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25573_figures/2604.25573_fig7.jpg" width="500"><br>

<sub>FIG. 6: Quartiles of success probabilities for different types of EHQO for (a) 8-qubit and (b) 12-qubit Hamiltonian using both BFGS and Nelder-Mead.</sub>

</details>

**Main problem.**

The difficulty of implementing faithful Quantum Annealing on NISQ devices due to high circuit depth and noise, necessitating more resource-efficient, QA-inspired hybrid algorithms.

**Main result.**

The study identifies that Approximate Quantum Annealing (AQA) parameters can serve as an effective warm start for QAOA, and introduces EHQO, a multi-step variational scheme that shows improved scaling and performance on hard 2-SAT instances.

**Method.**

The authors use a discretized annealing ansatz (AQA) and a multi-step variational scheme (EHQO) based on the Suzuki-Trotter product formula, evaluated via numerical simulations on the JUQCS simulator.

**Summary.**

This paper proposes new variational quantum algorithms inspired by the physics of quantum annealing to better suit the limitations of NISQ hardware. It introduces Approximate Quantum Annealing (AQA) to find efficient parameter regimes for QAOA initialization and presents Evolving Hamiltonian Quantum Optimization (EHQO) as a way to guide optimization through a sequence of intermediate Hamiltonians. Numerical tests on 2-SAT problems demonstrate that these methods can improve success probabilities and offer better scaling than standard QAOA. The work provides a practical strategy for leveraging annealing-like dynamics to enhance hybrid quantum-classical optimization.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on combinatorial optimization problems formulated as Ising Hamiltonians, specifically using ensembles of hard 2-SAT instances with 8 to 18 variables.

**Key observables.**

Success probability (median and mean), expectation value of the Hamiltonian, and overlap with ground and excited states.

**Important parameters / regimes.**

Trotterization time step (tau), number of layers (p), annealing schedule functions (A(s) and B(s)), and the number of intermediate steps (Ns).

**Assumptions / limitations.**

The algorithms are evaluated on relatively small problem sizes (up to 18 qubits) and assume the availability of classical optimizers like BFGS.

**Figures summary.**

Figure 1 shows a parameter scan of success probability vs. tau and p; Figure 4 shows expectation energy evolution during EHQO; Figure 5 illustrates state overlap loss during anti-crossings; Figure 6 compares success probabilities across algorithms; Figure 7 shows the scaling of success probability with problem size.

**Paper structure.**

The paper introduces the problem of NISQ-era annealing, defines the AQA and EHQO algorithms, presents parameter scans to identify operational regimes, details the EHQO multi-step framework, provides numerical benchmarks on 2-SAT instances, and concludes with scaling analysis.

</details>

<details><summary>Abstract</summary>

We study algorithms inspired by quantum annealing that are suited for the NISQ era. First, we analyze approximate quantum annealing (AQA), which employs a discretized annealing ansatz in which the time step and the number of layers are allowed to deviate from a faithful implementation of quantum annealing. Parameter scans identify regimes that reproduce annealing-like behavior with reduced resources, making them more suitable for NISQ devices. The resulting parameters can then be used as an effective warm start for the quantum approximate optimization algorithm (QAOA), improving its performance compared to random initializations. We also introduce evolving Hamiltonian quantum optimization (EHQO), a multistep variational scheme that guides the optimization process through intermediate Hamiltonians derived from the standard annealing Hamiltonian. Numerical simulations on sets of hard 2-SAT instances suggest that quantum annealing-inspired algorithms provide practical strategies for enhancing variational quantum optimization.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25854"></a>


### [Quantum channels preserving sigma-additivity and Ulam measurable cardinals](http://arxiv.org/abs/2604.25854v1)

**Authors:** S. V. Dzhenzher

**Type:** theory · **Category:** other · **PDF:** <https://arxiv.org/pdf/2604.25854v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25854_figures/2604.25854_fig1.jpg" width="500"><br>

<sub>Figure 1. Obvious relations between measurability of caridinals. MC is measurable cardinal. UMC is Ulam measurable cardinal. RVMC is real-valued measurable cardinal. URVMC is Ulam real-valued measurable cardinal</sub>

</details>

**Main problem.**

The paper investigates the relationship between the properties of quantum states on infinite-dimensional Hilbert spaces and the set-theoretic existence of Ulam measurable cardinals.

**Main result.**

The author proves that any sigma-additive state on the diagonal algebra is representable as a Pettis integral and constructs a quantum channel that maps normal states into a singular sigma-additive state, effectively archiving information in the singular sector.

**Method.**

The study utilizes set-theoretic tools including sigma-complete ultrafilters and large cardinal axioms, alongside mathematical frameworks like the Pettis integral and Yosida-Hewitt decomposition.

**Summary.**

This paper explores the mathematical intersection of quantum state theory and large cardinal axioms in set theory. It specifically looks at quantum states on infinite-dimensional Hilbert spaces where the dimension is an Ulam measurable cardinal. The author demonstrates how quantum channels can be constructed to move information from normal, local states into a 'singular' sector that is invisible to compact operators. This provides a formal mathematical framework for the concept of information archiving within the non-normal sector of a state space.

<details><summary>Detailed structure</summary>

**Model / system.**

The system consists of a Hilbert space l2(kappa) where kappa is an Ulam measurable cardinal, focusing on the diagonal algebra of operators and the distinction between normal and singular states.

**Key observables.**

Projectors representing diagonal operators and the induced measures on the power set of the index set.

**Important parameters / regimes.**

The cardinality kappa (specifically when it is an Ulam measurable cardinal) and the property of sigma-additivity.

**Assumptions / limitations.**

The results assume the framework of ZFC set theory and the existence of large cardinals (Ulam measurable cardinals); the scope is restricted to the diagonal algebra D(H).

**Figures summary.**

A diagram illustrating the hierarchical relationships between different types of large cardinals, such as Measurable, Ulam real-valued measurable, and Ulam measurable cardinals.

**Paper structure.**

The paper begins by establishing the representation of states via Pettis integrals, moves to characterizing singular states through their induced measures, and concludes with the construction and analysis of a quantum channel that transforms normal states into singular states.

</details>

<details><summary>Abstract</summary>

This paper investigates the interplay between the properties of quantum states on the Hilbert space \(\ell_2(κ)\) and the set-theoretic nature of the cardinal $κ$.   We focus on the existence of singular $σ$-additive states~ -- functionals whose induced measures are $σ$-additive yet vanish on singletons.   While the existence of such states is known to be equivalent to the Ulam measurability of $κ$, their structural and dynamical properties remain largely unexplored.   We prove that any $σ$-additive state on the diagonal algebra is representable as a Pettis integral over a singular $σ$-additive measure, extending the classical representation theory to the non-normal sector.   Furthermore, we construct a class of quantum channels using $σ$-complete ultrafilters that map normal states to singular $σ$-additive states, effectively <<archiving>> information into the singular part of the state space.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24840"></a>


### [Quantum Rotors on the Fuzzy Sphere and the Cubic CFT](http://arxiv.org/abs/2604.24840v1)

**Authors:** Andreas Stergiou

**Type:** theory · **Category:** statistical mechanics · **PDF:** <https://arxiv.org/pdf/2604.24840v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.24840_figures/2604.24840_fig1.jpg" width="500"><br>

<sub>Fig. 1: Finite-size dependence of hopt(N) for w = 0.6. Filled circles are the DMRG values obtained via the secant method applied to gS(hopt) = 0; open circles are extrapolated using the fit (3.9) with (3.10).</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24840_figures/2604.24840_fig2.jpg" width="500"><br>

<sub>Fig. 2: Finite-size dependence of ∆X and ∆Z at w = 0.6. Both dimensions decrease monotonically towards</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24840_figures/2604.24840_fig3.jpg" width="500"><br>

<sub>Fig. 3: Finite-size dependence of ∆S at w = 0.6. The dashed line shows the Monte Carlo determination</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24840_figures/2604.24840_fig4.jpg" width="500"><br>

<sub>Fig. 4: Finite-size dependence of ∆Tµν at w = 0.6. The dashed line marks the exact protected value</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.24840_figures/2604.24840_fig5.jpg" width="500"><br>

<sub>Fig. 5: Finite-size dependence of ∆Aµ at w = 0.6. The dashed line marks the protected dimension ∆Jµ =</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.24840_figures/2604.24840_fig6.jpg" width="500"><br>

<sub>Fig. 6: Finite-size dependence of ∆S′ at w = 0.6. The dashed line shows the Monte Carlo determination</sub>

</details>

**Main problem.**

The difficulty of non-perturbatively studying the 3D cubic conformal field theory (CFT) because its observables are numerically very close to the more symmetric O(3) model, making it hard to isolate the cubic fixed point.

**Main result.**

The fuzzy sphere regularization successfully isolates the cubic critical point, demonstrating the lifting of degeneracy in the rank-two symmetric tensor and providing scaling dimensions consistent with Monte Carlo and conformal perturbation theory benchmarks.

**Method.**

The study uses the fuzzy sphere regularization method combined with Exact Diagonalization (ED) and the Density Matrix Renimormalization Group (DMRG) implemented in the FuzzifiED Julia package.

**Summary.**

This paper presents a method to study the 3D cubic conformal field theory by using a fuzzy sphere regularization to prevent the system from reverting to O(3) symmetry. By 'hard-coding' cubic symmetry into the Hamiltonian, the authors successfully isolate the cubic critical point. Using ED and DMRG, they calculate scaling dimensions that align with established Monte Carlo and conformal perturbation theory results. This demonstrates that the fuzzy sphere is a powerful tool for resolving closely spaced universality classes.

<details><summary>Detailed structure</summary>

**Model / system.**

A quantum rotor model on a fuzzy sphere, where the O(3) symmetric Hamiltonian is deformed by adding a cubic-invariant two-body interaction to break continuous rotational symmetry down to the cubic group (Oh).

**Key observables.**

Scaling dimensions of key operators (scalar singlets, spin-one primary, and stress-energy tensor) and the splitting of the O(3) rank-two traceless symmetric tensor into Eg and T2g representations.

**Important parameters / regimes.**

Moment of inertia (I), Heisenberg coupling (J), cubic anisotropy strength (w), and the kinetic energy tuning parameter (h).

**Assumptions / limitations.**

The model uses a truncated rotor basis (l=0 and l=1 only), and results are subject to finite-size effects with non-rigorous thermodynamic limit extrapolations.

**Figures summary.**

Figures show the finite-size dependence of operator dimensions, specifically the monotonic decrease of the S' operator dimension and the convergence of the X and Z operators.

**Paper structure.**

The paper introduces the problem of symmetry enhancement, describes the fuzzy sphere construction and Hamiltonian deformation, details the numerical methods (ED and DMRG), presents the results for various operator dimensions, and compares them to existing benchmarks.

</details>

<details><summary>Abstract</summary>

The three-dimensional cubic conformal field theory governs the critical behaviour of Heisenberg magnets with cubic anisotropy. Studying this theory non-perturbatively is challenging, because its most easily accessible observables are numerically very close to those of the more symmetric $O(3)$ model. In this work, we overcome this difficulty using the fuzzy sphere regularisation method. By adding a cubic-invariant two-body interaction to the quantum rotor Hamiltonian used for the $O(3)$ model, we break the continuous rotational symmetry by construction and unambiguously isolate the cubic critical point. Using exact diagonalisation and the density matrix renormalisation group, we calculate the scaling dimensions of several key operators, including the leading scalar singlets, and resolve the splitting of the $O(3)$ rank-two traceless symmetric tensor into the $E_g$ and $T_{2g}$ representations of the cubic group. Our results are consistent with existing Monte Carlo, conformal perturbation theory, and $\varepsilon$ expansion benchmarks, demonstrating the power of the fuzzy sphere in resolving closely spaced universality classes.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25503"></a>


### [Quantum-Accelerated Gowers $U_2$ Norm for Bent Boolean Functions](http://arxiv.org/abs/2604.25503v1)

**Authors:** Rajdeep Dwivedi, C. A Jothishwaran, Sugata Gangopadhyay, Vishvendra Singh Poonia

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25503v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25503_figures/2604.25503_fig1.jpg" width="500"><br>

<sub>Figure 1: Fitness evolution for n = 6 variables. The theoretical bent threshold is U2(f)4 = 0.3536. Both methods converge to this vicinity; the quantum run exhibits wider generation-to- generation variation due to finite-sample shot noise.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25503_figures/2604.25503_fig2.jpg" width="500"><br>

<sub>Figure 2: Fitness evolution for n = 8 variables. The classical GA converges to best fitness U2(f)4 = 0.2500 the exact theoretical bent threshold by around generation 165, and holds steady thereafter. The quantum run (250 generations) reaches U2(f)4 ≈0.2829, consistent with the classical trajectory at the same generation count.</sub>

</details>

**Main problem.**

Finding bent Boolean functions, which are maximally nonlinear and resistant to affine approximation, is computationally hard for large numbers of variables due to the exponential cost of evaluating fitness metrics.

**Main result.**

The authors demonstrate a quantum-accelerated genetic algorithm that uses a quantum circuit to evaluate the Gowers U2 norm, providing a superpolynomial complexity advantage for n > 25.

**Method.**

A hybrid quantum-classical genetic algorithm (GA) is proposed, utilizing a 3n-qubit quantum circuit as an evolutionary fitness function to estimate the Gowers U2 norm.

**Summary.**

This paper presents a hybrid quantum-classical genetic algorithm designed to find bent Boolean functions more efficiently than classical methods. By using a quantum circuit to evaluate the Gowers U2 norm, the authors show that the computational cost can be reduced from exponential to polynomial for large numbers of variables. The study validates that this quantum-assisted approach can successfully navigate the search space to reach theoretical optimality. This provides a clear roadmap for using future fault-tolerant quantum computers to solve hard combinatorial optimization problems in Boolean algebra.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on Boolean functions f: F2^n -> F2 and uses a quantum circuit model with three n-qubit registers (X, A, B) and a phase-oracle Uf to encode function values as phases.

**Key observables.**

Gowers U2 norm (fitness metric), Walsh-Hadamard spectral flatness, and the bent threshold (2^-n/4).

**Important parameters / regimes.**

Number of variables (n=6, n=8), crossover point (n approx 25), number of shots (M=1000), and mutation rate (pm=0.8).

**Assumptions / limitations.**

The performance advantage assumes the availability of fault-tolerant quantum hardware and is subject to finite-sampling (shot) noise.

**Figures summary.**

Figure 1 shows the fitness evolution for n=6, illustrating convergence and the impact of shot noise; Figure 2 shows the fitness evolution for n=8, demonstrating the classical GA reaching the exact theoretical threshold.

**Paper structure.**

The paper introduces the problem of bent function construction, proposes a hybrid quantum-classical GA, provides a complexity analysis comparing quantum and classical scaling, validates the method via simulations for n=6 and n=8, and discusses future extensions to larger n and higher-order norms.

</details>

<details><summary>Abstract</summary>

Bent Boolean functions extremal objects that maximally resist affine approximation are   notoriously hard to construct for large numbers of variables.   We propose a hybrid quantum-classical genetic algorithm (GA) that uses a   \emph{quantum circuit} to evaluate the Gowers $U_2$ norm as the evolutionary   fitness function.   Our central contribution is a complexity-theoretic separation: the quantum evaluation   circuit requires only $3n$ qubits and $\bigO(n^2)$ two-qubit gates per function query,   whereas the classical computation of the exact Gowers $U_2$ norm demands   $\bigO(2^{2n})$ arithmetic operations an exponential overhead that renders it   infeasible for $n \gtrsim 25$.   We validate the framework on $n=6$ and $n=8$ variable systems.   For $n=8$, our classical GA run extended to 1000 generations achieves best fitness   $\Utwof = 0.250000$ \emph{exactly} the theoretical bent threshold $2^{-n/4}$ with   average fitness $0.257267$, confirming that the Gowers $U_2$ norm is a superior   fitness criterion over Walsh-Hadamard spectral flatness.   Quantum-assisted evaluation faithfully reproduces the classical trajectory up to   finite-sampling noise, and our complexity analysis demonstrates that for   $n > 25$ the quantum evaluator provides a decisive computational advantage   on fault-tolerant hardware.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25103"></a>


### [Rethinking Dimensional Regularization in Critical Phenomena](http://arxiv.org/abs/2604.25103v1)

**Authors:** P. Beretta, A. Codello

**Type:** theory · **Category:** statistical mechanics · **PDF:** <https://arxiv.org/pdf/2604.25103v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25103_figures/2604.25103_fig1.jpg" width="500"><br>

<sub>FIG. 1. Convergence in successive truncations of the critical exponents ν and ω in d = 3. Comparison is shown among the FDR-LPA (magenta) and NPRG-LPA (teal). We also report ε-expansion and CB values for comparison.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25103_figures/2604.25103_fig2.jpg" width="500"><br>

<sub>FIG. 2. Convergence of the critical exponent η in the FDR approximation discussed in the text (magenta) in d = 3. We also display reference results from state-of-the-art CB [31]; second order of the derivative expansion of the NPRG (teal), with the Θ2 cutoff [35]; and the m →∞limit of PTRG [28]. Dashed lines report ε-expansion O(ε2) and O(ε3) results (without re-summation).</sub>

</details>

**Main problem.**

The paper addresses the limitations of the standard epsilon-expansion in critical phenomena and the scheme dependencies/complexities introduced by mass cutoffs in existing functional Renormalization Group (RG) frameworks.

**Main result.**

The authors propose a new 'Functional Dimensional Regularization' (FDR) scheme that combines the agility of DR with the generality of functional RG, achieving faster convergence and critical exponent estimates that rival or exceed state-of-the-art methods.

**Method.**

The FDR method constructs beta functions by summing DR beta functions over all critical dimensions (d_c = 0, 2, 4, ...), effectively treating all poles in the complex d-plane as fundamental to the flow.

**Summary.**

This paper introduces Functional Dimensional Regularization (FDR), a new renormalization group scheme for studying critical phenomena. By summing dimensional regularization beta functions over all critical dimensions, the authors create a method that avoids the need for explicit mass cutoffs. The FDR approach shows remarkable accuracy in calculating critical exponents for the 3D Ising model, even at low orders of approximation. It effectively bridges the gap between the simplicity of the epsilon-expansion and the power of functional RG.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on scalar field theory (specifically lambda-phi^4 theory) and its application to the Ising universality class and Wilson-Fisher fixed point in three dimensions.

**Key observables.**

Critical exponents (nu, omega, eta), RG spectrum (scaling dimensions/eigenvalues), and beta functions.

**Important parameters / regimes.**

Dimension d, coupling constants (lambda_2, lambda_4, lambda_6, ...), and the DR mass scale mu.

**Assumptions / limitations.**

The current analysis is primarily restricted to one-loop master formulas and focuses on even couplings to avoid complexity; the method is tested via the Local Potential Approximation (LPA) and derivative expansions.

**Figures summary.**

Figure 1 compares convergence of critical exponents; Figure 3 and 4 illustrate the Feynman diagrams contributing to the standard two-loop DR flow versus the one-loop FDR flow.

**Paper structure.**

The paper introduces the limitation of existing RG methods, proposes the FDR framework, demonstrates its mathematical construction via summing critical dimensions, validates it by reproducing known epsilon-expansion results, and compares its convergence and accuracy against NPRG and Conformal Bootstrap methods.

</details>

<details><summary>Abstract</summary>

We show that it is possible to use dimensional regularization (DR) beyond the usual $\varepsilon$-expansion in the context of renormalization group (RG) calculations in Critical Phenomena. Based on this fact, we propose a new functional RG scheme - Functional Dimensional Regularization (FDR) - and apply it to a scalar theory in three dimensions. We compute the critical exponents of the Ising universality class directly in $d=3$ under various typical approximations. The method that emerges combines the agility typical of DR with the generality proper of functional RG. Moreover, at a given order of approximation, FDR seems to provide faster convergence and better estimates than other functional RGs.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25488"></a>


### [Robust Metal-Insulator Transition Despite Surface Dead-Layer Growth in Sub-10-nm Cr-Doped V2O3 Nanocrystals](http://arxiv.org/abs/2604.25488v1)

**Authors:** Yoichi Ishiwata, Ichidai Harada, Masaki Imamura, Kazutoshi Takahashi, Hirofumi Ishii, Masato Yoshimura, Nozomu Hiraoka, Yuji Inagaki, Kenta Akashi, Tatsuya Kawae, Tetsuya Kida, Masashi Nantoh

**Type:** experiment · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25488v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25488_figures/2604.25488_fig1.jpg" width="500"><br>

<sub>FIG. 1. TEM images for Cr-doped V2O3 NCs with average sizes of (a) 21.8 ± 3.8 nm, (b) 7.7 ± 2.1 nm, and (c) 5.6 ± 2.0 nm. (d) Synchrotron XRD pattern of the 5.6 nm sample with Rietveld reﬁnement conﬁrming the corundum structure.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25488_figures/2604.25488_fig2.jpg" width="500"><br>

<sub>FIG. 2. Temperature-dependent magnetic susceptibility of Cr-doped V2O3 NCs with sizes of 5.6 nm, 7.7 nm, and 21.8 nm. Warming curves exhibit a clear increase near 155 K, in- dicative of the antiferromagnetic-to-paramagnetic transition.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25488_figures/2604.25488_fig3.jpg" width="500"><br>

<sub>FIG. 3. Photoemission spectra of the 21.8 nm sample. (a) SXPES valence-band spectra showing temperature-induced changes, including the emergence of a shoulder feature near EF above 170 K. (b) HAXPES spectra revealing a clear metal- lic response at 200 K. (c,d) V 2p and O 1s core-level spectra, which exhibit temperature-dependent changes consistent with the MIT.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25488_figures/2604.25488_fig4.jpg" width="500"><br>

<sub>FIG. 5. Photoemission spectra of the 5.6 nm sample. (a) SXPES valence-band spectra remain insulating-like across all temperatures, indicating that the probed region is entirely within the insulating surface layer. (b) HAXPES spectra show a slight increase in spectral weight near EF at 200 K, suggesting that the NC interior undergoes a MIT even at this extreme size. (c,d) V 2p and O 1s core-level spectra exhibit subtle changes between 80 and 200 K, conﬁrming the persis- tence of the MIT internally.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25488_figures/2604.25488_fig5.jpg" width="500"><br>

<sub>FIG. 4. Photoemission spectra of the 7.7 nm sample. (a) SXPES valence-band spectra showing minimal temperature- induced changes across the measured range. (b) HAXPES spectra reveal a metallic response at 200 K despite strong surface suppression. (c,d) V 2p and O 1s core-level spectra exhibit small but discernible changes between 80 and 200 K, consistent with a weakened MIT signature.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25488_figures/2604.25488_fig6.jpg" width="500"><br>

<sub>FIG. 6. Schematic illustration of the two-layer model: an insulating surface layer surrounds a metallic interior in Cr- doped V2O3 NCs. As size decreases, the insulating layer thickens and strongly inﬂuences both surface-sensitive and deeper-probing photoemission spectra.</sub>

</details>

**Main problem.**

Investigating whether the metal-insulator transition (MIT) in Cr-doped V2O3 nanocrystals is intrinsically suppressed by extreme size reduction or if it persists in the particle interior despite the growth of an insulating surface dead-layer.

**Main result.**

The MIT persists down to an average particle size of 5.6 nm, with the transition occurring in the nanocrystal interior while an insulating surface dead-layer grows and suppresses quasiparticle weight as size decreases.

**Method.**

The study uses synchrotron-based photoemission spectroscopy (SXPES for surface sensitivity and HAXPES for deep probing) combined with magnetic susceptibility measurements and structural characterization (TEM, XRD).

**Summary.**

This study examines the stability of the Mott metal-insulator transition in Cr-doped V2O3 nanocrystals as they are scaled down to the sub-10-nm regime. By comparing surface-sensitive and deep-probing photoemission spectroscopy, the researchers found that while an insulating 'dead-layer' grows at the surface as particles shrink, the metallic phase persists in the nanocrystal interior. The results show that the fundamental limit for the transition is approximately 5 nm, though the shrinking conductive core poses practical challenges for electronic device applications.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system consists of Cr-doped V2O3 nanocrystals with average particle sizes of 5.6 nm, 7.7 nm, and 21.8 nm, modeled as a two-layer system with an insulating surface dead-layer surrounding a metallic core.

**Key observables.**

Transition temperature (T_MIT), magnetic susceptibility (chi), quasiparticle (QP) weight, and spectral weight near the Fermi level.

**Important parameters / regimes.**

Particle sizes (5.6 nm to 21.8 nm), probing depths (1.1 nm for SXPES and 7.8 nm for HAXPES), and a fundamental size limit of approximately 5 nm.

**Assumptions / limitations.**

The thickness of the effective surface layer may be influenced by local surface morphology, and the transition is discussed within the context of the Mott criterion.

**Figures summary.**

Fig 1 shows TEM images and XRD patterns for size characterization; Fig 2 displays temperature-dependent magnetic susceptibility showing the transition near 155 K; Fig 3 shows valence-band spectra comparing SXPES and HAXPES.

**Paper structure.**

The paper introduces the problem of nanoscaling in Mott systems, describes the synthesis and characterization of V2O3 nanocrystals, presents magnetic and spectroscopic evidence for the persistence of the MIT, discusses the growth of the surface dead-layer, and concludes with the implications for device miniaturization.

</details>

<details><summary>Abstract</summary>

We investigated the size dependence of the metal-insulator transition (MIT) in Cr-doped V2O3 nanocrystals by photoemission spectroscopy using complementary probing depths, together with magnetic susceptibility measurements. Photoemission spectra show that MIT signatures persist down to an average particle size of 5.6 nm, and magnetic susceptibility measurements exhibit a nearly size-invariant transition onset. The contrast between surface-sensitive and deeper-probing photoemission spectra reveals that the transition survives in the nanocrystal interior. At the same time, the spectra indicate a systematic suppression of coherent quasiparticle weight with decreasing size, pointing to the growth of an insulating surface dead layer. These results demonstrate that nanoscaling does not intrinsically eliminate the MIT itself, but progressively enhances the influence of surface-driven insulating behavior, thereby providing insight into the practical limits of miniaturizing Mott-based devices.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25494"></a>


### [Sector-dominant graph-local drivers for path-window barrier Hamiltonians on the Boolean hypercube](http://arxiv.org/abs/2604.25494v1)

**Authors:** Takiko Sasaki, Tetsuji Tokihiro

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25494v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25494_figures/2604.25494_fig1.jpg" width="500"><br>

<sub>Figure 1: Locality diagnostics for the strict sector-snake ordering and the fast 𝑣2 ordering in the regenerated 𝑛≤8 benchmark. The strict ordering keeps all adjacent moves at Hamming distance one in these checked cases. The 𝑣2 ordering preserves the skeleton and fixed prefix but introduces longer adjacent jumps.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25494_figures/2604.25494_fig2.jpg" width="500"><br>

<sub>Figure 2: Regenerated 𝑛= 8 baseline and best-hybrid comparison for the non-diagonal target classes in table 5. The sector-dominant hybrid improves the window-barrier targets, while standard TF remains very strong for sector/path mixture controls.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25494_figures/2604.25494_fig3.jpg" width="500"><br>

<sub>Figure 3 illustrates the role of the mixing parameters. The best region is not 𝛼= 1, which would be a path-only driver. Instead, the high-fidelity region keeps a large sector component and uses the path-window term as an additional geometry-aware component. This observation is the basis for the phrase “sector-dominant hybrid driver” used throughout the paper.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25494_figures/2604.25494_fig4.jpg" width="500"><br>

<sub>Figure 3: Regenerated heatmap for the centered original-window barrier target with driver window 𝑤= 4. The useful region is sector-dominant with a substantial but not standalone path-window component and a small transverse-field catalyst.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25494_figures/2604.25494_fig5.jpg" width="500"><br>

<sub>Figure 4: Distributional path-order controls. Boxplots show 64 sampled random permutations and 64 sampled sector-preserving random orderings; single points show TF, sector-only, and deterministic orderings. Left: matched target/driver controls. Right: strict target with varied catalyst path.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25494_figures/2604.25494_fig6.jpg" width="500"><br>

<sub>Figure 5: Left: driver ablation. The path-window graph is weak as a standalone driver, while the full sector-dominant hybrid is strongest. Right: anneal-time dependence. The full hybrid becomes clearly advantageous at intermediate and long anneal times, while all broad drivers approach high fidelity for 𝑇= 160.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25494_figures/2604.25494_fig7.jpg" width="500"><br>

<sub>Figure 6: Left: regenerated grid-based minimum gaps for selected drivers on the 𝑛= 8 original- window barrier target. Right: finite-size summary for selected drivers over 𝑛= 5, . . . , 8 at 𝑇= 80. The path-only driver deteriorates strongly, while sector-dominant hybrids remain high at the tested finite sizes.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25494_figures/2604.25494_fig8.jpg" width="500"><br>

<sub>Figure 7: Representative rows of table 9. The strict ordering is extremely effective for Hamiltonians whose off-diagonal support is local in the strict path coordinate. It is not the best ordering for ordinary 1D hopping or pair creation, where a different locality is more natural.</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25494_figures/2604.25494_fig9.jpg" width="500"><br>

<sub>Figure 8: Ground-state-preparation fidelity for the staged sensor-placement benchmark. The sector-dominant hybrid driver improves over TF-only and sector-only, whereas the path-window driver alone remains weak.</sub>

</details>

**Main problem.**

Designing problem-dependent, graph-local adiabatic drivers to improve ground-state preparation fidelity in quantum annealing on Boolean hypercubes.

**Main result.**

A hybrid driver combining sector, path-window, and transverse-field components significantly improves fidelity for non-diagonal target Hamiltonians aligned with the driver's geometry, though it provides no advantage for standard diagonal-cost annealing.

**Method.**

Numerical simulations of the time-dependent Schrodinger equation using finite-size studies (up to n=8) and ablation controls to identify the roles of different driver components.

**Summary.**

This paper investigates how to design specialized 'drivers' for quantum annealing that are tailored to the specific structure of a problem. By using a hybrid approach that combines Hamming-weight sectors with specific path-window coordinates, the authors show they can significantly improve the success rate of finding ground states for certain classes of non-diagonal Hamiltonians. While not a universal solution for all quantum annealing problems, it provides a design principle for using graph-local information to guide quantum dynamics.

<details><summary>Detailed structure</summary>

**Model / system.**

Quantum annealing on an n-dimensional Boolean hypercube using a time-dependent Hamiltonian consisting of a hybrid driver and a non-diagonal target Hamiltonian with path-window barrier structures.

**Key observables.**

Ground-state preparation fidelity, energy residual, minimum spectral gap, and MeanBand (matrix bandwidth metric).

**Important parameters / regimes.**

Number of qubits (n up to 8), annealing time (T), driver window width (w), and mixing parameters (alpha, epsilon).

**Assumptions / limitations.**

The study is limited to finite-size systems (n <= 8) and the effectiveness is conditional on the target Hamiltonian's geometry being aligned with the driver's coordinates.

**Figures summary.**

Boxplots comparing different path-order controls, ablation studies showing the necessity of each driver component, and performance comparisons for sensor-placement benchmarks.

**Paper structure.**

The paper introduces the sector/path coordinate construction, presents numerical experiments on fidelity and spectral gaps, performs ablation studies to isolate driver mechanisms, and concludes with validation via specific benchmark problems.

</details>

<details><summary>Abstract</summary>

We study finite-size adiabatic state preparation on Boolean hypercubes using graph-local drivers built from sector/path coordinates related to monotone Gray-code representatives. The construction is not presented as a new all-$n$ Gray-code existence theorem; rather, it provides finite representatives, explicitly checked through the cases used in the numerical experiments, for testing problem-dependent graph-local drivers. For ordinary diagonal-cost transverse-field annealing, the ordering does not yield a robust advantage, and we include this negative result as a baseline. For non-diagonal target Hamiltonians whose geometry is expressed in the same sector/path coordinates, hybrid drivers combining sector, path-window, and small transverse-field components can substantially improve the final ground-state fidelity in centered barrier instances. Reproduction runs from the accompanying code confirm a representative centered original-window barrier value of approximately \(0.9799\) for the fixed-control hybrid parameters \((w,α,ε)=(8,0.50,0.15)\), while also showing that the improvement is target-class dependent. Randomized and ablation controls indicate that the dominant contribution is the sector-preserving skeleton, with strict one-bit completion acting as a secondary refinement. We provide code, finite certificates, CSV files, validation logs, and reproduction scripts to make the finite-size claims traceable.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25581"></a>


### [Self-consistent vertex corrected $GW$ with static and dynamic screening using tensor hypercontraction: assessment of molecular ionization potentials](http://arxiv.org/abs/2604.25581v1)

**Authors:** Munkhorgil Wang, Ming Wen, Pavel Pokhilko, Chia-Nan Yeh, Miguel A. Morales, Dominika Zgid

**Type:** theory · **Category:** numerical methods · **PDF:** <https://arxiv.org/pdf/2604.25581v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25581_figures/2604.25581_fig1.jpg" width="500"><br>

<sub>Figure 1: Hedin’s Pentagon. The interacting one-body Green’s function G, the vertex func- tion Γ, the irreducible polarizability P, the dynamically screened Coulomb interaction W and the self-energy Σ</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25581_figures/2604.25581_fig2.jpg" width="500"><br>

<sub>Figure 2: Skeleton Feynman diagrams for the self-energy approximations considered in this work. Panel (a) shows the GW self-energy, and panel (b) shows the interaction decomposition introduced in Eq. (26). Panels (c)–(f) depict the vertex self-energies, ˜ΣSOX(U(1),U(2)), of SOX, SOSEX, 2SOSEX, and G3W2, respectively. For each vertex-corrected approximation, both the compact form in terms of the full screened interaction W and the expanded form obtained by substituting Eq. (26)—with terms written explicitly in v and ˜W—are shown. Bold wavy lines denote the full screened interaction W, while double-wavy lines denote the screening contribution ˜W.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25581_figures/2604.25581_fig3.jpg" width="500"><br>

<sub>Figure 3: Basis set convergence of Etot, Estat 1b and Edyn 2b using the logarithmic scale, with respect to αIpts for selected molecules. The energy contributions are calculated at the THC- scGW/cc-pVQZ level. For clarity, energy differences smaller than 10−12 a.u. are set to zero. All 29-molecules are reported in Supporting Information Figs. S1 and S2</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25581_figures/2604.25581_fig4.jpg" width="500"><br>

<sub>Figure 4: The convergence behavior of the trace of the imaginary part of the dynamic self- energy ImTr(Σ(ωn)) with respect to αIpts for selected molecules. Only the spin α component of the self-energy is printed. The calculations were performed at the THC-scGW /cc-pVQZ level.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25581_figures/2604.25581_fig5.jpg" width="500"><br>

<sub>Figure 5: The trace of the imaginary part of the dynamic self-energy ImTr[Σ(ωn)] as a function of frequency ωn for various vertex methods listed</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25581_figures/2604.25581_fig6.jpg" width="500"><br>

<sub>Figure 6: The trace of the real part of the dynamic self-energy ReTr(Σ(ωn)) as a function of frequency ωn for various vertex methods listed</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25581_figures/2604.25581_fig7.jpg" width="500"><br>

<sub>Figure 7: Upper panel: The first IP differences in eV for the G0W0Γ29 data set evaluated w.r.t. ∆CCSD(T). Lower panel: The first IP differences in eV for the G0W0Γ29 data set evaluated w.r.t. experimental values. Comparisons in cc-pVQZ basis set are made for THC- scGW and all the vertex schemes discussed in this work. Experimental values marked * for respective molecular cases correspond to vertical ionization energies.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25581_figures/2604.25581_fig8.jpg" width="500"><br>

<sub>Figure 8: The convergence of the first IP value for water produced for all six THC-scGWΓ variants using different convergence thresholds. On the y-axis, we report the absolute differ- ence of IP when compared with the one obtained with 10−7 a.u convergence threshold. Both the x- and y-axes are in logarithmic scale.</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25581_figures/2604.25581_fig9.jpg" width="500"><br>

<sub>Figure 9: The first IP values calculated by THC-scGW and six THC-scGWΓ variants for the GW100 set. All molecules are categorized into ten groups. The ∆CCSD(T) results were used as the standard reference. The dagger sign † showcase the failure of convergence in SOX. Horizontal lines represent ±0.3 eV error range from the reference values.</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25581_figures/2604.25581_fig10.jpg" width="500"><br>

<sub>Figure 10: Imaginary part of the trace self-energy, ImTr[Σ(iωn)], for six selected molecules: ammonia, carbon oxysulfide, magnesium chloride, tetrafluoromethane, lithium fluoride, and krypton. Across these representative systems, the imaginary part preserves a robust screening-controlled ordering over Matsubara frequency.</sub>

</details>

**Main problem.**

The high computational cost of implementing fully self-consistent vertex-corrected GW (scGWGamma) methods for realistic molecular systems and the need to evaluate if Tensor Hypercontraction (THC) can accelerate these calculations without introducing significant errors.

**Main result.**

THC decomposition introduces negligible errors into scGW ionization potentials, proving it is a reliable acceleration route, though vertex corrections primarily cause systematic shifts in IPs rather than consistent accuracy improvements.

**Method.**

Self-consistent GW (scGW) and vertex-corrected scGWGamma using Tensor Hypercontraction (THC) for acceleration, incorporating various vertex approximations like SOX, SOSEX, and G3W2.

**Summary.**

This paper evaluates the use of Tensor Hypercontraction (THC) to accelerate expensive self-consistent GW calculations with vertex corrections. The authors demonstrate that THC provides a reliable way to reduce computational scaling without sacrificing the accuracy of molecular ionization potentials. They also find that while vertex corrections are important, they often result in systematic shifts in energy values rather than simple accuracy improvements. This work identifies THC as a key enabling technology for applying high-level many-body perturbation theory to larger molecular systems.

<details><summary>Detailed structure</summary>

**Model / system.**

Small molecular systems benchmarked using the G0W0Gamma and GW100 datasets, treated within a many-body Green's function framework using the Luttinger-Ward formulation in a grand-canonical ensemble.

**Key observables.**

Molecular first ionization potentials (IPs), electron affinities (EAs), and total electronic energy decomposition (one-body and two-body contributions).

**Important parameters / regimes.**

Interpolation-point ratio (alpha_Ipts), frequency grids (real vs. imaginary axis), temperature (beta), and chemical potential (mu).

**Assumptions / limitations.**

The study assumes the validity of the THC decomposition for the dynamic part of the self-energy and focuses on vertex corrections applied only to the self-energy level while keeping polarization at the GW level.

**Figures summary.**

Figure 1 illustrates Hedin's equations; Figure 3 shows logarithmic plots of energy convergence as a function of the THC interpolation-point ratio.

**Paper structure.**

The paper introduces the computational challenge of vertex corrections, establishes the mathematical framework of many-body perturbation theory, details the THC acceleration technique and various vertex approximations, presents benchmark results on molecular datasets, and discusses convergence and error analysis.

**Why it may be interesting.**

The development of efficient numerical scaling via THC for many-body Green's function methods is highly relevant to the advancement of large-scale classical simulations of many-body dynamics and electronic correlations.

</details>

<details><summary>Abstract</summary>

In this work, we benchmark tensor hypercontraction (THC)-accelerated fully self-consistent $GW$ (sc$GW$) and vertex-corrected self-consistent $GW$ (sc$GWΓ$) methods for predicting molecular first ionization potentials (IPs). The vertex function, $Γ$, is inserted into the self-energy in a fully self-consistent manner, and representative sc$GW$ and sc$GWΓ$ variants are assessed across the $G_0W_0\Gamma29$ and $GW100$ data sets. We find that the THC decomposition introduces negligible errors into self-consistent $GW$ ionization potentials, indicating that the acceleration preserves the underlying fully self-consistent results. Across both benchmark sets, vertex-corrected sc$GWΓ$ methods primarily produce systematic shifts in the IPs relative to sc$GW$ rather than consistent accuracy improvements. These results identify THC as a reliable route to lower-cost sc$GW$ and sc$GWΓ$ calculations

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25042"></a>


### [Stabilizers for Compiling Logical Circuits under Hardware Constraints](http://arxiv.org/abs/2604.25042v1)

**Authors:** Jack Weinberg, Narayanan Rengaswamy

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25042v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25042_figures/2604.25042_fig1.jpg" width="500"><br>

<sub>Fig. 1. Toy Connectivity Graph</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25042_figures/2604.25042_fig2.jpg" width="500"><br>

<sub>Fig. 2. Non-Trivial Connectivity Graph</sub>

</details>

**Main problem.**

How to compile arbitrary logical quantum gates on hardware with restricted connectivity and limited accessible Hamiltonians by leveraging the redundancy of error-correcting codes.

**Main result.**

The authors provide a closed-form solution to the compilation problem by formulating it as a least-squares optimization over the stabilizer subalgebra, allowing for the selection of physical Hamiltonians that are easier to implement.

**Method.**

The problem is reduced to a least-squares minimization problem using the Moore-Penrose pseudoinverse within the framework of Lie algebra (su(N)) and the adjoint action.

**Summary.**

This paper presents a novel method for quantum compilation that utilizes the redundancy in error-correcting codes to find physical implementations of logical gates that respect hardware constraints. By treating the choice of stabilizer as a least-squares optimization problem, the authors show how to avoid expensive operations like SWAP gates by instead using naturally accessible physical Hamiltonians. The framework is general for any unitary in the SU(N) group and provides a mathematically precise way to bridge the gap between logical algorithms and physical hardware connectivity.

<details><summary>Detailed structure</summary>

**Model / system.**

The framework applies to quantum error-correcting codes (specifically the [[4, 2, 2]] code) and hardware architectures with restricted connectivity, such as superconducting, trapped ion, or neutral atom platforms.

**Key observables.**

The distance (error) between the target logical Hamiltonian and the accessible physical Hamiltonian, and the fidelity of the implemented unitary.

**Important parameters / regimes.**

The connectivity graph of the hardware, the specific error-correcting code used, and the set of accessible Lie algebra generators.

**Assumptions / limitations.**

The method assumes a fixed error-correcting code and encoding circuit, a predefined set of accessible Hamiltonians, and that the hardware allows for the implementation of the resulting physical Hamiltonian.

**Figures summary.**

Figure 1 shows a toy connectivity graph used for the CNOT implementation example; Figure 2 displays a non-trivial connectivity graph for a 4-qubit system.

**Paper structure.**

The paper introduces the dual problem of fault-tolerance and compilation, develops a mathematical framework using Lie theory to define logical and stabilizer subalgebras, formulates the compilation as a least-squares optimization, provides a closed-form solution via the pseudoinverse, and demonstrates the approach using the [[4, 2, 2]] code.

</details>

<details><summary>Abstract</summary>

To implement quantum algorithms on a quantum computer, we must overcome the twin problems of fault-tolerance -- how can we realize a relatively noiseless computation by cleverly combining noisy components? -- and compilation -- how can we realize an arbitrary quantum algorithm given the basic operations available on the quantum device at hand? We show how treating the former problem via error-correcting codes enables greater flexibility in resolving the latter. Specifically, we explicitly leverage the fact that error-correcting codes introduce redundancy which renders physically distinct operators logically indistinguishable. In terms of computation, it suffices to implement any operator logically equivalent to some target, yet from a compilation perspective, certain choices may be preferable to others. Our novel contribution is making this intuition precise in the general setting of the special unitary group. In particular, we describe how to reduce the problem of making a compilation-ideal choice to a least squares problem and provide a closed form solution thereof. Using our framework, it is possible to circumvent inserting costly swaps to adhere to hardware connectivity; instead, we could realize the logical target through a distinct physical Hamiltonian that is natively accessible. We elucidate our approach using the $[[4,2,2]]$ code. We discuss connections to compressed sensing that may pave the way to efficient compilation leveraging physical degrees of freedom.

</details>

<sub>[↑ back to top](#top)</sub>
