# arxiv digest (quant-ph + cond-mat) — 2026-04-26

*2 papers · 0 relevant · 1 highlighted*  
_⏳ in progress: 2/95 papers processed (file updates after each one)_


## ⭐ Highlighted (1)

*Papers by authors on your watch list. Full entries appear only once in their normal category below.*

- ⭐ [Algorithmic Locality via Provable Convergence in Quantum Tensor Networks](http://arxiv.org/abs/2604.21919v1) — Sarang Gopalakrishnan


## numerical methods (1)

### ⭐ [Algorithmic Locality via Provable Convergence in Quantum Tensor Networks](http://arxiv.org/abs/2604.21919v1)

**Highlighted author(s):** Sarang Gopalakrishnan  
**Authors:** Siddhant Midha, Yifan F. Zhang, Daniel Malz, Dmitry A. Abanin, Sarang Gopalakrishnan  
**Type:** theory · **PDF:** <https://arxiv.org/pdf/2604.21919v1>  
**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.21919_figures/2604.21919_fig1.jpg" width="500"><br>
<sub>FIG. 1. (a) Algorithmic locality in tensor networks: The ef- fect of a perturbation at the center of the network on the fixed-point messages living on edges of the graph decays ex- ponentially with distance from perturbation. Loops (see Eq. (6)) and clusters (see Eq. (7)) built out of the fixed-point mes- sages inherit the locality subsequently. (b) Phase diagram of injective PEPS: Theorem 1 shows existence (for all 0 ≤ε &lt; 1) and uniqueness (for ε &lt; ε∗= O(1/∆)) of fixed points, where ∆is the degree of the graph. Theorem 2 shows convergence of cluster expansion for ε &lt; ε∗∗= O  min{1/D, (D/∆)∆/2} </sub>

</details>

**Main problem.** Establishing rigorous theoretical foundations for Tensor Network Belief Propagation (TN-BP) in higher dimensions, specifically proving the existence, uniqueness, and convergence of fixed points and the validity of cluster expansions.

**Main result.** The authors prove 'algorithmic locality,' demonstrating that local perturbations in strongly injective PEPS lead to exponentially decaying changes in both BP fixed-point messages and local observables, enabling efficient classical simulation.

**Method.** The work utilizes message-passing dynamics, Banach contraction mapping, and cluster expansion techniques from lattice statistical mechanics to analyze the stability and convergence of TN-BP.

**Summary.** This paper provides the first end-to-end theory for Tensor Network Belief Propagation (TN-BP) in higher-dimensional PEPS. It proves that for sufficiently injective states, the BP algorithm converges to a unique fixed point that is stable under local perturbations. The authors introduce 'algorithmic locality,' showing that the impact of a local change decays exponentially with distance. This result justifies the use of local recomputation for efficient classical simulation of many-body quantum systems.

<details><summary>Detailed structure</summary>

**Model / system.** The study focuses on Projected Entangled Pair States (PEPS) defined on arbitrary graphs with a maximum degree and bond dimension, specifically focusing on the class of strongly injective tensors.

**Key observables.** Local expectation values, connected correlation functions, and the norm of the state (partition function).

**Important parameters / regimes.** Injectivity parameter (epsilon), bond dimension (D), maximum vertex degree (Delta), and correlation/decay length scales (xi).

**Assumptions / limitations.** The proofs are restricted to a subclass of PEPS satisfying 'strong injectivity' and assume the bond dimension and vertex degree are O(1).

**Figures summary.** Figure 1(a) illustrates the concept of algorithmic locality via decaying influence of perturbations; Figure 1(b) presents a phase diagram showing thresholds for existence, uniqueness, and cluster expansion convergence.

**Paper structure.** The paper begins with preliminaries on PEPS and Schatten norms, moves to proving the existence and uniqueness of BP fixed points, establishes the decay of loop activities, proves the central theorem of algorithmic locality, and concludes with error decomposition analysis.

**Why it may be interesting.** This provides a rigorous bridge between widely used numerical practices (like TN-BP) and provable algorithmic performance, offering a theoretical guarantee for the efficiency of classical simulations of many-body states.

</details>

<details><summary>Abstract</summary>

Belief propagation has recently emerged as a powerful framework for evaluating tensor networks in higher dimensions, combining computational efficiency with provable analytical guarantees. In this work, we develop the first end-to-end theory of tensor network belief propagation for a class of projected entangled pair states satisfying \emph{strong injectivity}. We show that when the injectivity parameter exceeds a constant threshold, BP fixed points can be found efficiently, and a cluster-corrected BP algorithm computes physical quantities to $1/\mathrm{poly}(N)$ error in $\mathrm{poly}(N)$ time for an $N$ qubit system. We identify a striking phenomenon we term \emph{algorithmic locality}: local perturbations of the tensor network affect the BP fixed point with an influence decaying rapidly with distance. As a result, updates to the fixed point after a local perturbation can be carried out using only local recomputation. Moreover, through the cluster expansion, this locality extends to observables, implying that local expectation values can be approximated from local data with controlled accuracy. Our results provide the first rigorous guarantee for the effectiveness of tensor-network belief propagation on a wide class of many-body states, bridging a gap between widely used numerical practice and provable algorithmic performance.

</details>


## statistical mechanics (1)

### [Subsystem-Resolved Spectral Theory for Quantum Many-Body Hamiltonians](http://arxiv.org/abs/2604.21929v1)

**Authors:** MD Nahidul Hasan Sabit  
**Type:** theory · **PDF:** <https://arxiv.org/pdf/2604.21929v1>  
**Analysis basis:** full PDF text, analyzed in chunks
**Topic relevance:** `kinetically constrained dynamics` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.21929_figures/2604.21929_page2.jpg" width="500"><br>
<sub>Low-resolution page preview, page 2</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.21929_figures/2604.21929_page3.jpg" width="500"><br>
<sub>Low-resolution page preview, page 3</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.21929_figures/2604.21929_page4.jpg" width="500"><br>
<sub>Low-resolution page preview, page 4</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.21929_figures/2604.21929_page5.jpg" width="500"><br>
<sub>Low-resolution page preview, page 5</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.21929_figures/2604.21929_page6.jpg" width="500"><br>
<sub>Low-resolution page preview, page 6</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.21929_figures/2604.21929_page7.jpg" width="500"><br>
<sub>Low-resolution page preview, page 7</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.21929_figures/2604.21929_page8.jpg" width="500"><br>
<sub>Low-resolution page preview, page 8</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.21929_figures/2604.21929_page9.jpg" width="500"><br>
<sub>Low-resolution page preview, page 9</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.21929_figures/2604.21929_page10.jpg" width="500"><br>
<sub>Low-resolution page preview, page 10</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.21929_figures/2604.21929_page11.jpg" width="500"><br>
<sub>Low-resolution page preview, page 11</sub>

</details>

**Main problem.** The global spectrum of a many-body Hamiltonian fails to capture the inherent locality of interactions. The paper seeks to develop a subsystem-resolved spectral framework that organizes spectral data according to the geometry and interaction structure of subsystems.

**Main result.** The authors prove that subsystem Hamiltonians can be locally approximated with exponentially decaying error and that their spectra are stable under such truncations. Furthermore, they show that the spectra of spatially separated subsystems are approximately additive, becoming exact for finite-range interactions.

**Method.** The study uses an operator-algebraic framework, employing interaction norms to measure the decay of interaction strengths and spectral perturbation theory (Hausdorff distance) to relate operator-level approximations to spectral stability.

**Summary.** This paper introduces a new way to study the energy spectra of quantum many-body systems by looking at subsystems rather than just the global Hamiltonian. It demonstrates that the spectrum of a local region can be accurately approximated by looking at a finite neighborhood and that the spectra of two distant regions can be roughly added together. This proves that the locality of physical interactions is directly reflected in the structure of the system's energy levels. The framework provides a mathematical foundation for connecting interaction geometry to spectral behavior.

<details><summary>Detailed structure</summary>

**Model / system.** The framework applies to quantum many-body Hamiltonians acting on a tensor product Hilbert space, where the Hamiltonian is a sum of local interaction terms with exponentially decaying strengths.

**Key observables.** Subsystem spectrum (sigma(H_S)) and the Hausdorff distance between spectra.

**Important parameters / regimes.** Interaction norm (Phi_mu), subsystem radius (r), spatial separation (D), and interaction decay rate (mu).

**Assumptions / limitations.** The system is assumed to have a finite index set and interactions must satisfy a specific exponential decay condition (finite interaction norm).

**Paper structure.** The paper begins by defining a subsystem-based spectral framework and an interaction norm, then moves to proving the local approximability of subsystem Hamiltonians, followed by establishing spectral stability and the approximate additivity of spectra for distant subsystems.

**Why it may be interesting.** This work provides a static analogue to Lieb-Robinson bounds, offering a new way to understand how the geometry of interactions shapes the spectral properties of many-body systems, which is fundamental for understanding correlations and dynamics.

</details>

<details><summary>Abstract</summary>

We study spectral properties of quantum many-body Hamiltonians through a subsystem-based framework. Given a Hamiltonian of the form $H = \sum_{X \subseteq Λ} Φ(X)$ acting on a tensor product Hilbert space, we associate to each subset $S \subseteq Λ$ a subsystem Hamiltonian $H_S$ and its spectrum $\mathcal{S}(S) = σ(H_S)$. This produces a family of spectra indexed by subsystems, allowing spectral data to be organized according to interaction structure. We show that subsystem Hamiltonians admit local approximations: $H_S$ can be approximated by operators supported on finite neighborhoods with an error bounded by $\|H_S - H_{S,r}\| \le |S| e^{-μr} \|Φ\|_μ$. As a consequence, subsystem spectra are stable under truncation in the sense that $d_H(\mathcal{S}(S), σ(H_{S,r})) \le |S| e^{-μr} \|Φ\|_μ.$ We then prove that for disjoint subsets $S_1, S_2 \subseteq Λ$, the subsystem spectrum is approximately additive: $d_H\big(\mathcal{S}(S_1 \cup S_2), \mathcal{S}(S_1) + \mathcal{S}(S_2)\big) \le (|S_1| + |S_2|) e^{-μD} \|Φ\|_μ,$ where $D = d(S_1, S_2)$. In the finite-range case, this relation becomes exact. The results show that spectral properties reflect the locality of interactions not only at the level of operators, but also at the level of spectra. The framework provides a way to study many-body systems in which interaction geometry directly shapes spectral behavior.

</details>
