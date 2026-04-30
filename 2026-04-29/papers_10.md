# Daily arXiv Report

[← Index](index.md)

[← Previous](papers_09.md)
[Next →](papers_11.md)

## Papers 181–200


<a id="paper-2604.25058"></a>


### [A SWAP-free Framework for QAOA](http://arxiv.org/abs/2604.25058v1)

**Authors:** Thiago Assis, Pedro Baptista, Laila Lopes, Diego Ferreira, Gabriel Coutinho

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25058v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25058_figures/2604.25058_fig1.jpg" width="500"><br>

<sub>Figure 1: Comparison of heuristics. The plots show how normalized lambda and optimality gap vary with graph density for n = 8.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25058_figures/2604.25058_fig2.jpg" width="500"><br>

<sub>Figure 2: Optimality gap as a function of n for four algorithms: Perron Con- nected, Perron Disconnected, Laplacian Connected, and ideal QAOA with SWAP errors.</sub>

</details>

**Main problem.**

The performance of QAOA on NISQ devices is degraded by SWAP gates required to implement non-native interactions on sparse hardware topologies. The paper seeks to determine if a hardware-compatible approximation of the cost Hamiltonian can outperform an exact but noisy implementation.

**Main result.**

The authors propose a SWAP-free framework that uses a Mixed-Integer Semidefinite Program (MISDP) to optimize qubit mapping and Hamiltonian approximation. They demonstrate that for larger problem sizes (n > 20), this hardware-aware approximation significantly outperforms the standard SWAP-induced noise baseline.

**Method.**

The framework uses an MISDP formulation to simultaneously select a hardware-compatible cost matrix and optimize qubit allocation. For larger instances, the authors introduce spectral-based heuristics (e.g., Perron and Laplacian-based) to solve the optimization problem efficiently.

**Summary.**

This paper addresses the high error rates in NISQ-era quantum computing caused by SWAP gates during algorithm transpilation. Instead of using an exact Hamiltonian that requires many noisy gates, the authors propose modifying the problem itself to fit the hardware's native connectivity. By using a mathematical framework to find the best hardware-compatible approximation, they show that an imprecise but 'SWAP-free' algorithm can actually produce more accurate results than an exact but heavily noisy one as the number of qubits increases.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on the Quantum Approximate Optimization Algorithm (QAOA) applied to Quadratic Unconstrained Binary Optimization (QUBO) problems, specifically cardinality-constrained models. The physical model involves an XY-type mixer Hamiltonian and a cost Hamiltonian implemented on a hardware graph representing NISQ device connectivity.

**Key observables.**

The deviation/error between original and embedded cost matrices (lambda), the optimality gap, and the normalized lambda objective value.

**Important parameters / regimes.**

Graph density (d), number of qubits (n), cardinality constraint (k), number of QAOA layers (l), and CNOT error rate (0.33%).

**Assumptions / limitations.**

The study assumes perfect classical optimization of the variational parameters (beta and gamma) to isolate the effects of qubit allocation and noise.

**Figures summary.**

Figure 1 compares various spectral heuristics against a brute-force benchmark for small n; Figure 2 shows the optimality gap of the proposed heuristics compared to the SWAP-based baseline as a function of problem size n.

**Paper structure.**

The paper introduces the problem of SWAP-induced noise, formulates the SWAP-free framework as an MISDP, proves the NP-completeness of the decision problem, provides theoretical bounds using the Lovasz number, introduces spectral heuristics for scalability, and benchmarks the approach against SWAP-based noise using a financial index-tracking problem.

</details>

<details><summary>Abstract</summary>

The performance of the Quantum Approximate Optimization Algorithm (QAOA) on noisy intermediate-scale quantum (NISQ) devices is strongly limited by sparse qubit connectivity. When interactions required by QAOA Hamiltonians are not aligned to the hardware topology, transpilation introduces SWAP gates, increasing circuit depth and noise. We propose a SWAP-free QAOA framework based on modifying the cost Hamiltonian so that it can be implemented natively on the hardware. We formulate this as a mixed-integer semidefinite program (MISDP) that selects a hardware-compatible approximation of the original cost matrix and optimizes the allocation of logical variables to physical qubits. We prove that the associated decision problem is NP-complete and derive theoretical guarantees relating the MISDP objective to the loss in the original optimization problem through the Lovász number of the hardware graph. Since solving MISDPs is practical only for small instances, we introduce heuristics based on spectral properties of the problem matrix and hardware graph. Our experiments on a cardinality-constrained quadratic optimization model for index tracking show competitive performance against a baseline representing ideal QAOA under SWAP-induced noise. These results indicate that, on sparse NISQ architectures, a hardware-aware approximation of the objective may be more effective than an exact but heavily transpiled Hamiltonian implementation.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24973"></a>


### [Approximate Sparse State Preparation with the Grover-Rudolph Algorithm](http://arxiv.org/abs/2604.24973v1)

**Authors:** Debora Ramacciotti, Martin Steinbach, Bence Temesi, Andreea-Iulia Lefterovici, Antonio F. Rotundo

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.24973v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.24973_figures/2604.24973_fig1.jpg" width="500"><br>

<sub>Fig. 1: Circuit diagram of a uniformly controlled y-rotation on three qubits. We indicate the Ry rotation just by the applied angle to simplify the notation.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24973_figures/2604.24973_fig2.jpg" width="500"><br>

<sub>Fig. 2: Preparation tree for the state |ψ⟩= a |001⟩+ b |011⟩+ c |100⟩. The highlighted leaves are the nonzero basis states of the target state, while faded nodes indicate zero-amplitude branches. The non-faded nodes correspond to the nonzero prefix sets Sk. The coarse-grained state |ψ(2)⟩, for instance, is given by a |00⟩+ b |01⟩+ c |10⟩.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24973_figures/2604.24973_fig3.jpg" width="500"><br>

<sub>Fig. 3: Example of optimization procedure. Here, θ(2) 11 = θ(2) 10 = θ(2) 1e = θ.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24973_figures/2604.24973_fig4.jpg" width="500"><br>

<sub>Fig. 4: CNOT reduction due to the exact merges. We plot the ratio of the CNOT count after the merging procedure to that before the merging procedure, using the single-rotation decomposition in both cases, against the sparsity percentage D = d/2n. The number of qubits is fixed at n = 20 qubits, and each point is averaged across 20 repetitions.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.24973_figures/2604.24973_fig5.jpg" width="500"><br>

<sub>Fig. 5: Comparison between the uniform rotation algorithm (blue), single rotations after merges (pink), and the exact algorithm (green). We plot the CNOT gate count against the sparsity percentage D = d/2n, for simulation of n = 20 qubits and average across 20 repetitions.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.24973_figures/2604.24973_fig6.jpg" width="500"><br>

<sub>Fig. 6: Performance assessment of the overlap estimation. The number of qubits is fixed to 15, and the number of intervals to M = 20, while the sparsity percentage D is varied. The two columns show, respectively, Fest −F and F −FLB as functions of the minimum allowed overlap Fmin, where FLB is the lower bound of Thm. 8, and F is the true overlap. The curves represent averages over 20 random real instances, while the shaded areas show the minimum and maximum values observed across repetitions.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.24973_figures/2604.24973_fig7.jpg" width="500"><br>

<sub>Fig. 7: Comparison between the exact and approximate al- gorithms. The number of qubits is fixed to n = 20, and the number of intervals to M = 20, while the sparsity percentage D is varied. The plot shows the ratio of the number of CNOTs in the approximate algorithm to that in the exact scheme. Each data point corresponds to an average over 20 repetitions, with 10 points plotted per curve.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.24973_figures/2604.24973_fig8.jpg" width="500"><br>

<sub>Fig. 8: Comparison between the exact and the approximate algorithm for different values of M. The number of qubits is fixed to n = 20, and the sparsity percentage to D = 5 · 10−5. The plot shows the ratio of the number of CNOTs in the approximate algorithm to that in the exact scheme. Each data point corresponds to an average over 20 repetitions, with 10 points plotted per curve.</sub>

</details>

**Main problem.**

The challenge of reducing the circuit complexity, specifically the CNOT gate count, for preparing sparse quantum states using the Grover-Rudolph algorithm.

**Main result.**

The proposed exact optimization reduces CNOT counts by up to 90% for highly sparse states, while an additional approximate variant provides a further 20-30% reduction with controllable error.

**Method.**

The authors propose an exact gate-merging and control-stripping procedure and an approximate greedy optimization strategy that merges rotations with similar angles based on a classically computable overlap estimator.

**Summary.**

This paper presents two new optimization techniques for the Grover-Rudolph algorithm to make sparse quantum state preparation more efficient. The first method uses exact gate merging to significantly reduce CNOT counts without any loss in fidelity. The second method introduces an approximate approach that allows for even greater gate reductions by merging similar rotation angles, provided the resulting error stays below a user-defined threshold. These improvements are particularly valuable for implementing quantum algorithms on early fault-tolerant quantum computers.

<details><summary>Detailed structure</summary>

**Model / system.**

The work focuses on the preparation of sparse quantum states where the number of non-zero amplitudes d is much smaller than the Hilbert space dimension 2^n.

**Key observables.**

CNOT gate count, state overlap (fidelity), and the error in the overlap estimator.

**Important parameters / regimes.**

Sparsity (d/2^n), minimum allowed overlap threshold (F_min), and the number of threshold steps (M) in the greedy procedure.

**Assumptions / limitations.**

The analysis is limited to real, positive quantum states; the locations and number of non-zero entries are known a priori; and the approximate method introduces a small, controllable infidelity.

**Figures summary.**

Circuit diagrams of rotations, illustrations of preparation trees and gate merging, plots of CNOT reduction versus sparsity, and performance assessments of the overlap estimator and greedy algorithm.

**Paper structure.**

The paper introduces the problem of sparse state preparation, details an exact optimization method via gate merging and control stripping, presents an approximate greedy optimization strategy with an overlap estimator, provides complexity analysis and numerical validation, and discusses limitations.

</details>

<details><summary>Abstract</summary>

Sparse quantum state preparation is a common subroutine in quantum algorithms, where classical data with few nonzero entries must be loaded into a quantum state. In this work, we consider the Grover-Rudolph algorithm, which has recently been shown to efficiently prepare sparse states, and we propose two improvements. First, we extend an existing gate-merging procedure by allowing rotations to merge with virtual zero-angle gates on unreachable branches of the preparation tree, reducing the number of CNOTs and control qubits. Second, we introduce an approximate variant in which rotations with similar but not identical angles are merged at the cost of a small, controllable error in the prepared state. We derive a classically computable estimate of the resulting overlap with the target state, which is used to guide the merging decisions.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25760"></a>


### [Beyond Single Trajectories: Optimal Control and Jordan-Lie Algebra in Hybrid Quantum Walks for Combinatorial Optimization](http://arxiv.org/abs/2604.25760v1)

**Authors:** Tianen Chen, Yun Shang

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25760v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25760_figures/2604.25760_fig1.jpg" width="500"><br>

<sub>FIG. 1. Schematic of a p-layer QAOA. |s⟩= |+⟩⊗n is the ini- tial state. ⟨Hc⟩= ⟨ψ(β, γ)|Hc|ψ(β, γ)⟩is the objective func- tion. Each yellow area is corresponding to a layer of QAOA which alternately applies e−iHcγi and e−iHbβi.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25760_figures/2604.25760_fig2.jpg" width="500"><br>

<sub>FIG. 2. Schematic of a p-step HQW. |0⟩⊗|s⟩= |0⟩⊗|+⟩⊗n</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25760_figures/2604.25760_fig3.jpg" width="500"><br>

<sub>FIG. 3. The function graph of y1(t) (blue), y2(t) (red) and y3(t) (green) with respect to u(t).</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25760_figures/2604.25760_fig4.jpg" width="500"><br>

<sub>FIG. 4. Geometric interpretation of the Jordan product’s role. (Left) When Nmin ≈0, the QAOA manifold MQ is nearly flat. (Right) When Nmin ≪0, the HQW manifold MH becomes highly curved, with transverse directions (red arrows) generated by the Jordan product i{Hc, Hb}.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25760_figures/2604.25760_fig5.jpg" width="500"><br>

<sub>FIG. 5. Correlation between Jordan negativity Nmin and HQW performance advantage. The solid line shows a linear fit y = 0.430x −0.010 with correlation coefficient r = 0.9605 (p = 7.15 × 10−11).</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25760_figures/2604.25760_fig6.jpg" width="500"><br>

<sub>FIG. 7. Distribution of HQW’s relative improvement over QAOA across 50 8-vertex graphs with 18-23 edges for the average-performance comparison. Mean: 11.63%, median: 11.93%.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25760_figures/2604.25760_fig7.jpg" width="500"><br>

<sub>FIG. 6. Scatter plot of average 1 −r (over 100 initializa- tions) for QAOA vs. HQW on 50 8-vertex graphs with 18-23 edges. Each point corresponds to one graph; the diagonal line indicates equal performance. Both axes show 1 −r on a log- arithmic scale.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25760_figures/2604.25760_fig8.jpg" width="500"><br>

<sub>FIG. 8. Scatter plot of average 1 −r (over 100 initializa- tions) for QAOA vs. HQW on 50 8-vertex graphs with 24-28 edges. Each point corresponds to one graph; the diagonal line indicates equal performance. Both axes show 1 −r on a log- arithmic scale.</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25760_figures/2604.25760_fig9.jpg" width="500"><br>

<sub>FIG. 9. Distribution of HQW’s relative improvement over QAOA across 50 8-vertex graphs with 24-28 edges for the average-performance comparison. Mean: 28.26%, median: 20.80%.</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25760_figures/2604.25760_fig10.jpg" width="500"><br>

<sub>FIG. 10. The 8-vertex graph for the Max-Cut problem.</sub>

</details>

**Main problem.**

The standard QAOA is limited by a single, fixed evolution path, which prevents the coherent superposition of multiple trajectories. The authors aim to develop a more expressive Hybrid Quantum Walk (HQW) ansatz that can superpose multiple Hamiltonian-driven paths to improve combinatorial optimization.

**Main result.**

The HQW framework systematically outperforms QAOA in convergence speed, solution accuracy, and robustness for Max-Cut and Maximum Independent Set problems. This advantage is theoretically linked to the larger Jordan-Lie algebra generated by HQW and the 'negativity of the Jordan product' in its dynamical Lie algebra.

**Method.**

The authors use Pontryagin's Minimum Principle to derive the optimal dynamical coin operator and employ Dynamical Lie Algebra (DLA) and Jordan-Lie algebra analysis to characterize the algorithm's expressivity. Numerical performance is evaluated using the Adam optimizer on PennyLane simulations.

**Summary.**

This paper introduces a Hybrid Quantum Walk (HQW) ansatz that generalizes the QAOA by allowing for the coherent superposition of multiple evolution trajectories. By using a dynamical coin operator, the HQW accesses a larger Jordan-Lie algebraic structure than the standard QAOA. Numerical experiments on Max-Cut and Maximum Independent Set problems demonstrate that this approach leads to superior convergence and accuracy. The performance gain is fundamentally linked to the algebraic incompatibility of the Hamiltonians, quantified by the negativity of the Jordan product.

<details><summary>Detailed structure</summary>

**Model / system.**

A Hybrid Quantum Walk (HQW) model acting on a composite Hilbert space of a coin space and a position (graph) space. The system involves non-commuting cost and mixer Hamiltonians, where the coin operator controls the superposition of different evolutionary paths.

**Key observables.**

Approximation ratio error (1-r), ground state probability, Jordan product negativity (Nmin), and the sensitivity vector for the coin operator.

**Important parameters / regimes.**

QAOA depth (p), HQW steps (2p), graph edge density, and the learning rate of the Adam optimizer.

**Assumptions / limitations.**

The study assumes the context of the NISQ era and focuses on small-scale graph instances (up to 12 vertices) for numerical validation.

**Figures summary.**

Figure 1 shows a QAOA circuit schematic; Figure 2 shows the HQW circuit; Figure 3 displays Hamiltonian component weights; Figure 4 provides a geometric interpretation of the manifold curvature; Figure 5 shows the correlation between Jordan negativity and performance advantage; Figure 18 and 19 show statistical performance distributions and win rates.

**Paper structure.**

The paper introduces the limitation of QAOA, proposes the HQW ansatz, derives the optimal control for the coin operator using PMP, provides an algebraic analysis using Jordan-Lie algebra to explain the enhanced expressivity, and concludes with numerical benchmarks on combinatorial optimization problems.

</details>

<details><summary>Abstract</summary>

The Quantum Approximate Optimization Algorithm (QAOA) follows a single, fixed evolution path, overlooking the potential computational advantage of coherently superposing multiple trajectories. Here we overcome this limitation with a hybrid quantum walk (HQW) ansatz that super poses multiple Hamiltonian-driven paths coherently within each circuit layer via a dynamical coin operator. QAOA emerges as a special case of this framework with a static Pauli-X coin. Using Pontryagin's minimum principle, we derive the optimal form of the coin operator, demonstrating that it generally differs from a constant gate. A dynamical Lie algebra analysis reveals that HQW generates a strictly larger Jordan-Lie algebra, providing an algebraic foundation for its enhanced expressivity. Especially, we reveal the connection between the unique Jordan product negativity in HQW's DLA and its performance advantages. Numerical experiments on Max-Cut and Maximum Independent Set problems show that HQW systematically outperforms QAOA in convergence speed, solution accuracy, and robustness. Our work establishes a path-superposition paradigm for quantum optimization, combining optimal control theory with algebraic structure to guide the design of advanced quantum algorithms.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24995"></a>


### [Bridging the Quantum Divide: A Learning-Centric Quantum Hackathon for Underrepresented Students (Extended Version)](http://arxiv.org/abs/2604.24995v1)

**Authors:** Fahimeh Bayeh, Linh Dinh, Dongho Lee, Scott Wesley

**Type:** experiment · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.24995v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.24995_figures/2604.24995_fig1.jpg" width="500"><br>

<sub>Fig. 1: An example of unclear documentation in Quirk.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24995_figures/2604.24995_fig2.jpg" width="500"><br>

<sub>Fig. 2: The objective structure for a teleportation challenge.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24995_figures/2604.24995_fig3.jpg" width="500"><br>

<sub>Fig. 4: The visit to Ultrafast Quantum Control Lab.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24995_figures/2604.24995_fig4.jpg" width="500"><br>

<sub>Fig. 5: The second day of the event: The competition</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.24995_figures/2604.24995_fig5.jpg" width="500"><br>

<sub>Fig. 8: Adding a new wire in Qiskit Composer.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.24995_figures/2604.24995_fig6.jpg" width="500"><br>

<sub>Fig. 6: An example of control misuse in Qiskit Composer.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.24995_figures/2604.24995_fig7.jpg" width="500"><br>

<sub>Fig. 7: An example of control use in Quirk.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.24995_figures/2604.24995_fig8.jpg" width="500"><br>

<sub>Fig. 9: Modifying controls in Qiskit Composer.</sub>

</details>

**Main problem.**

Designing an effective, inclusive, and accessible quantum computing hackathon for underrepresented high school students to bridge the diversity gap in quantum education.

**Main result.**

The hackathon successfully increased students' recognition of quantum vocabulary and shifted interest in quantum and STEM careers toward higher levels, while effectively reaching target demographics.

**Method.**

The authors implemented a two-day hackathon using the Integrated Course Design (ICD) framework, mastery learning, and specification grading, utilizing the Quirk circuit simulator for hands-on learning.

**Summary.**

This paper details the creation of a learning-centric quantum computing hackathon designed specifically for underrepresented high school students in Nova Scotia. By using a 'backwards design' approach and visual tools like the Quirk simulator, the program aims to lower the barrier to entry for complex quantum concepts. The results demonstrate measurable increases in student interest in quantum technologies and improved recognition of fundamental quantum terms. The study highlights how pedagogical choices in software and grading can promote inclusivity in the quantum workforce.

<details><summary>Detailed structure</summary>

**Model / system.**

The educational platform uses quantum circuit-based computational thinking tools, specifically the Quirk simulator, to teach concepts like qubits, entanglement, and quantum teleportation.

**Key observables.**

Student STEM affinity (via Likert scales), recognition of quantum vocabulary (e.g., superposition, entanglement), and demographic representation.

**Important parameters / regimes.**

Target demographics (Indigenous, African Nova Scotian, and female students), two-day duration, and use of visual/block-based programming abstractions.

**Assumptions / limitations.**

Assumes students have only basic algebra and general science knowledge; assumes the effectiveness of visual simulators like Quirk for novices without physics backgrounds.

**Figures summary.**

Figure 1 shows unclear documentation in Quirk; Figure 2 outlines the structure of a teleportation challenge; Figure 3 shows a physical Bloch sphere model; Figures 6-9 compare the interface friction and error-prone nature of Qiskit Composer versus Quirk.

**Paper structure.**

The paper introduces the diversity gap in quantum computing, describes the pedagogical frameworks (ICD, mastery learning), details the curriculum design and tool selection (Quirk vs. Qiskit), presents the hackathon implementation, and concludes with an analysis of student feedback and learning outcomes.

</details>

<details><summary>Abstract</summary>

This paper describes the design and implementation of a two-day quantum hackathon for underrepresented high school students in Nova Scotia, Canada. The first day of the hackathon is spent introducing students to quantum computing through hands-on activities, whereas the second day teaches students to apply this knowledge through guided challenges. Both days are informed by the theory of mastery learning and specification grading, with the full curriculum being crafted within the Integrated Course Design framework. This requires identifying situational factors unique to our target demographics, from which we develop learning outcomes, and then work backwards to a full curriculum with educative assessments. A novel aspect of our hackathon is that all circuit simulations are performed within Quirk: a decision based on best practices in computer science education. Based on feedback from students, we conclude that our hackathon successfully introduced students to the basics of quantum computing, and was able to reach most of our target demographics.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25638"></a>


### [Collective and separate metal-insulator transitions in correlated vanadium dioxide](http://arxiv.org/abs/2604.25638v1)

**Authors:** Xuanchi Zhou, Xiaohui Yao, Wentian Lu, Chunwei Yao, Xiaomei Qiao

**Type:** both · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25638v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25638_figures/2604.25638_fig1.jpg" width="500"><br>

<sub>Fig. 1 | Collective and separate metal-insulator transition (MIT) in correlated VO2. a, Schematic of band-filling control over electronic band structure of correlated electronic system. b, Collective and separate MIT properties in correlated system. c, Realizing the collective and separate MIT in VO2/TiO2/VO2-x system through inserting an electronically insulating TiO2. d, High-resolution transmission electron microscopy (HRTEM) images for VO2/TiO2/VO2-x trilayer. e, Zoom-in images for cross-sectional HRTEM and respective Fast Fourier Transform (FFT) images for VO2/TiO2/VO2-x trilayer. f, Vanadium, titanium and aluminum elementary distributions for as-grown VO2/TiO2/VO2-x trilayer...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25638_figures/2604.25638_fig2.jpg" width="500"><br>

<sub>Fig. 2 | The facile switching between collective and separative MIT in VO2. a, Temperature dependence of material resistivity (ρ-T) as compared for VO2/VO2-x bilayer and VO2/TiO2/VO2-x trilayer. b, Raman spectra compared for VO2 and oxygen-deficient VO2-x in VO2/VO2-x bilayer and VO2/TiO2/VO2-x trilayer. c, Temperature coefficient of material resistivity compared for VO2 monolayer, VO2/VO2-x bilayer and VO2/TiO2/VO2-x trilayer. d, The collective length scale achievable in VO2/VO2-x system, in comparison with other quantum material systems, covering superconducting, ferroic and phase change materials.36-40</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25638_figures/2604.25638_fig3.jpg" width="500"><br>

<sub>Fig. 3 | Tunable two-step MIT in VO2 system through hydrogenation. a, Comparing the X-ray diffraction (XRD) patterns for VO2/TiO2/VO2-x trilayer through hydrogenation. b, ρ-T tendency compared for hydrogenated VO2/TiO2/VO2-x system. c, Raman spectra for VO2/TiO2/VO2-x system via hydrogenation. d, Reversible electronic phase modulations in VO2/TiO2/VO2-x system via hydrogenation. e, Temporal evolution for hydrogen-induced variation in material resistivity (RH/R0) in hydrogenated VO2/TiO2/VO2-x system. f, Three-dimensional ToF-SIMS hydrogen element maps for hydrogenated VO2/TiO2/VO2-x trilayer. g, Depth-profile of the hydrogen elementary distribution in VO2/TiO2/VO2-x trilayer. h, Schematic...</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25638_figures/2604.25638_fig4.jpg" width="500"><br>

<sub>Fig. 4 | Hydrogen-triggered electronic orbital reconfiguration in VO2. a-b, X-ray photoelectron spectra (XPS) spectra as compared for the a, vanadium and b, oxygen core levels of VO2/TiO2/VO2-x system under different hydrogenation conditions. c-d, c, V-L edge and d, O-K edge of soft X-ray absorption spectra (sXAS) for VO2/TiO2/VO2-x through hydrogenation. e, Calculated density of states (DOS) of VO2 film c, before and after hydrogenation. d-e, Calculated fat band structure for VO2/TiO2/VO2-x system through hydrogenation.</sub>

</details>

**Main problem.**

Understanding and actively controlling the interplay between collective and separate metal-insulator transitions (MIT) in correlated electron systems.

**Main result.**

The researchers achieved reversible, on-demand manipulation of the MIT in VO2 heterostructures, transitioning between one-step collective and two-step separate transitions via oxygen vacancy engineering and hydrogen-induced band-filling.

**Method.**

Experimental techniques include laser molecular beam epitaxy, HRTEM, XPS, sXAS, and ToF-SIMS, complemented by DFT calculations using the GGA+U approach.

**Summary.**

This paper demonstrates a method to control the metal-insulator transition in vanadium dioxide by engineering its heterostructure. By using a TiO2 interlayer and introducing mobile hydrogen, the researchers can switch between a collective transition and a two-step separate transition. This is achieved by manipulating the electronic band-filling and orbital reconfiguration. The work transforms the collective length scale from a fixed property into a dynamic parameter for designing adaptive correlated electronics.

<details><summary>Detailed structure</summary>

**Model / system.**

The study uses VO2/VO2-x homojunctions and VO2/TiO2/VO2-x trilayers grown on c-plane Al2O3 substrates, utilizing TiO2 as an insulating interlayer and mobile hydrogen as a control agent.

**Key observables.**

Temperature-dependent resistivity (rho-T), Raman spectroscopy (V-V dimerization), X-ray absorption spectra (V-L and O-K edges), and elemental depth profiling.

**Important parameters / regimes.**

Collective length scale (~5-10 nm), transition temperature (T_MIT), oxygen deficiency (x), and hydrogen-related band filling.

**Assumptions / limitations.**

The use of the GGA+U approach assumes a Hubbard U of 3.32 eV for V-3d states to accurately model electron correlations.

**Figures summary.**

Fig 1: Structural characterization and elemental mapping of the trilayer; Fig 2: Comparison of resistivity and Raman spectra showing collective vs. separate MIT; Fig 3: Effects of hydrogenation on lattice and transport properties; Fig 4: Electronic structure analysis via XPS, sXAS, and DFT.

**Paper structure.**

The paper begins with structural and chemical validation of the heterostructures, moves to demonstrating the switching between collective and separate MIT regimes, explores the reversible control via hydrogenation, and concludes with the underlying orbital and electronic band-filling mechanism.

</details>

<details><summary>Abstract</summary>

Deciphering the complicated interplay between collective and separate behaviors lies at the heart of first-order metal-insulator transition (MIT) in correlated electron systems, enabling the rational design of exotic electronic states and functionalities. The critical balance between collective and separate behaviors defines a fundamental collective length scale, typically shorter than 5 nm, that governs emergent quantum orders, yet active control over this dichotomy remains elusive. Here, we realize on-demand manipulation of the collective and separate MIT within the correlated VO2 system in a reversible fashion. Artificially designing the oxygen deficiency in VO2/VO2-x homojunction fosters a collective MIT with an extended collective length scale, whereas the introduction of a TiO2 interlayer drives a crossover from this collective to a two-step separate MIT via decoupling of the electronic order parameter. Incorporating mobile hydrogens into the VO2/TiO2/VO2-x trilayer enables reversible control over electronic phase modulations, transitioning a two-step MIT towards either a one-step MIT or collective electron localization. This ionic control over the electronic band structure of VO2 flexibly triggers multi-state MIT, a process governed by hydrogen-related band filling. Our findings transform the collective length scale from a passive threshold into a dynamic design parameter, establishing a viable handle for engineering collective and separate MIT for adaptive correlated electronics.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25500"></a>


### [Critical Role of Hydrogen in Unconventional Superconductors: The Case of Hydrogenated FeSe Layers](http://arxiv.org/abs/2604.25500v1)

**Authors:** Lan-Lin Du, Yang Yang, Shiqi Hu, Sheng Meng

**Type:** theory · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25500v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25500_figures/2604.25500_fig1.jpg" width="500"><br>

<sub>FIG. 1. (a) Fatbands near the Fermi level from DFT, composed of Fe 𝑑orbitals (blue), Se 𝑝orbitals (red), and H 𝑠orbitals (black). (b) Atomic configuration of FeSeH. (c) Phonon dispersions of FeSeH, with the EPC strength (𝜆𝑞,𝜈) (represented in colorbar). (d) Total and atom-resolved phonon density of states. Band structure from DFT of (e) FeSeH and (f) bulk FeSe.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25500_figures/2604.25500_fig2.jpg" width="500"><br>

<sub>FIG. 2. (a) FeSeH’s superconducting gap Δ(𝑘) as a function of electron momentum 𝑘on the Fermi surface at 1 K. The blue square represents the first Brillouin zone. (b) The temperature dependence of the two superconducting gaps. (c) Distribution of the state-resolved EPC strength 𝜆𝑛𝑘. (d) The frequncy dependence of the isotropically averaged Eliashberg spectral function 𝛼2𝐹and the EPC strength 𝜆.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25500_figures/2604.25500_fig3.jpg" width="500"><br>

<sub>FIG. 3. Spectral function from DMFT of (a) FeSeH and (b) bulk FeSe. The gray shaded line is the spectral function of DMFT, and the purple line is the energy band of DFT. (c) Energies of three antiferromagnetic configurations (checkerboard, single- striped and double-striped) of FeSeH with magnetic moments pointing in plane and out of plane. The atomic configuration and arrows in the upper area indicate the direction of the magnetic moments in the in-plane case. 𝐸NM represents the energy of nonmagnetic configuration.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25500_figures/2604.25500_fig4.jpg" width="500"><br>

<sub>FIG. 4. Element-resolved DMFT spectral function for the band structure of FeSeH projected onto (a) Fe, (b) Se, (c) H.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25500_figures/2604.25500_fig5.jpg" width="500"><br>

<sub>FIG. 5. Other configurations we obtained after structure relaxation (Top: top view; Bottom: side view) but with imaginary phonon frequencies. The former three are bulk-type, while the last one is monolayer-type.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25500_figures/2604.25500_fig6.jpg" width="500"><br>

<sub>FIG. 6. Atomic resolved bands contributed by (a) Fe, (b) Se, (c) H from DFT calculations.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25500_figures/2604.25500_fig7.jpg" width="500"><br>

<sub>FIG. 7. Changes of DMFT spectral functions near the Fermi surface under the perturbation of the fifteen optical phonon modes. Orange color represents the initial spectral function, while blue represents the one after perturbation. The numbers are indices of the optical phonon modes ranging from 4 to 18.</sub>

</details>

**Main problem.**

Understanding the microscopic role of hydrogen in tuning superconductivity in unconventional, strongly correlated superconductors like FeSe.

**Main result.**

Hydrogenation of FeSe creates a stable FeSeH phase where electronic correlations drive hydrogen-derived spectral weight toward the Fermi surface, significantly enhancing electron-phonon coupling and predicting a Tc exceeding 40 K.

**Method.**

First-principles calculations using DFT and DFPT, combined with Dynamical Mean Field Theory (DMFT) to treat strong correlations and anisotropic Eliashberg theory for superconductivity.

**Summary.**

This paper investigates how adding hydrogen to FeSe layers enhances superconductivity. The authors find that strong electronic correlations play a critical role by shifting hydrogen-related electronic states toward the Fermi surface, which boosts the electron-phonon coupling. This mechanism leads to a predicted superconducting transition temperature of over 40 K and a two-gap state. The work provides a new microscopic perspective on pairing in strongly correlated systems and identifies FeSeH as a platform for future superconducting quantum devices.

<details><summary>Detailed structure</summary>

**Model / system.**

A hydrogenated FeSe monolayer (FeSeH) with 1:1:1 stoichiometry, modeled using an 18-band s-p-d model involving Fe d-orbitals, Se p-orbitals, and H s-orbitals.

**Key observables.**

Superconducting transition temperature (Tc), electron-phonon coupling strength (lambda), Fermi surface topology, superconducting gap structure, and Eliashberg spectral function.

**Important parameters / regimes.**

Tc > 40 K, EPC strength lambda (ranging from 0.15 in bulk to 2.23 with DMFT), and a two-gap superconducting state.

**Assumptions / limitations.**

The study assumes the validity of the DMFT-corrected EPC within the Migdal-Eliashberg formalism and focuses on the 1:1:1 stoichiometry.

**Figures summary.**

Fig 1 shows orbital composition, atomic configuration, and phonon dispersions; Fig 2 displays the superconducting gap, temperature dependence, and Eliashberg spectral function; Fig 3 compares DMFT and DFT spectral functions.

**Paper structure.**

The paper introduces the problem of hydrogen in unconventional superconductors, presents the structural and electronic properties of FeSeH via DFT, applies DMFT to reveal correlation-enhanced EPC, calculates superconducting properties via Eliashberg theory, and concludes with implications for quantum devices.

</details>

<details><summary>Abstract</summary>

Hydrogenation is known to tune superconductivity in a wide range of materials. While its microscopic role has been clarified in phonon-mediated superconductors such as hydrogenated MgB2, LaH10, and H3S, much less is known for hydrogenated cuprates and iron-based superconductors, where even the underlying structural motifs remain elusive. Using hydrogenated FeSe as a prototypical example, we reveal how hydrogen affects superconductivity in the presence of strong electronic correlations: correlation-induced orbital renormalization shifts hydrogen-derived spectral weight from the high-energy region toward the Fermi surface (FS), remarkably enhancing the electron-phonon coupling (EPC). We predict a structurally stable FeSeH phase where, compared to bare FeSe, hydrogen incorporation reshapes the FS topology and increases the number of channels for electron-phonon scattering, while simultaneously introducing high-frequency phonons that strengthen pairing. First-principles EPC calculations combined with dynamical mean field theory (DMFT) yield a superconducting transition temperature (Tc) exceeding 40 K. Fully anisotropic Eliashberg theory reveals a two-gap superconducting state, consistent with the gap structure experimentally observed in doped FeSe. Our findings identify correlation-enhanced EPC as a plausible microscopic mechanism for iron-based superconductivity and offer a new perspective on pairing in strongly correlated systems. In addition, this work establishes hydrogenated FeSe as a promising platform for engineering two-dimensional superconductors and superconducting quantum devices.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24951"></a>


### [Crystal-Field Symmetry Constraints in Layered Honeycomb ErBr$_3$](http://arxiv.org/abs/2604.24951v1)

**Authors:** Biaoyan Hu, Mingyuan Hu, Franz Demmel, Andrey A. Podlesnyak, Jiaqing He, Liusuo Wu

**Type:** both · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.24951v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.24951_figures/2604.24951_fig1.jpg" width="500"><br>

<sub>FIG. 1. (a) Three-dimensional crystal structure of ErBr3, showing stacked honeycomb layers of Er3+ ions separated along the crystallographic c axis. The interlayer spacing is indicated. (b) Top view of a single honeycomb layer in the ab plane, with the nearest-neighbor Er–Er distance labeled. (c) Field-dependent magnetization measured at 1.8 K for magnetic fields applied parallel to the honeycomb plane (H ∥ab) and along the crystallographic c axis (H ∥c), demonstrating pronounced magnetic anisotropy. (d) Local coordination environment of an Er3+ ion, illustrating the ErBr6 octahedron. (e) CEF energy-level scheme of the Er3+ ion. The J = 15/2 multiplet is split into a series of Kramers...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24951_figures/2604.24951_fig2.jpg" width="500"><br>

<sub>FIG. 2. (a) Elastic-channel neutron scattering intensity of ErBr3 measured with an Al holder at T = 2 K in the (H, K, 0) plane. The white dots mark the momentum positions at which the constant-Q energy cuts shown in (b) and (c) were taken. (b),(c) Constant-Q energy cuts measured at representative wave vectors along (1.5 −K/2, K, 0) and (H, 0, 0), respectively. Successive curves are vertically offset for clarity. In both momentum directions, peaks are observed near 1.5 and 3 meV, highlighted by the gray shaded regions. The nearly unchanged peak positions for different wave vectors indicate no detectable dispersion within experimental resolution.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24951_figures/2604.24951_fig3.jpg" width="500"><br>

<sub>FIG. 3. (a) Specific heat C(T), (b) C(T)/T, and (c) entropy S(T) of ErBr3 at representative magnetic fields applied within the honeycomb plane (H ∥ab). Vertical dashed red lines mark the thermodynamic anomalies. The horizontal dashed blue line indicates the entropy R ln 2 expected for a Kramers doublet ground state.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24951_figures/2604.24951_fig4.jpg" width="500"><br>

<sub>FIG. 4. Field evolution of the thermodynamic response of ErBr3 for magnetic fields applied within the honeycomb plane (H ∥ab). (a) Field dependence of the specific heat measured at selected temperatures, vertically offset for clarity. A sharp anomaly associated with the thermodynamic phase boundary is observed, together with a broader crossover feature. (b) Field– temperature (H–T) color map of the specific heat C of ErBr3 for H ∥ab. Open triangles mark the low-field anomalies and define the black phase-boundary curve. Open squares mark the high-field anomalies, and the straight Zeeman-scale guide with g ≈13 is drawn through them. (c) Magnetocaloric-effect measurements of ErBr3 during...</sub>

</details>

**Main problem.**

Investigating how local crystal-field (CEF) symmetry constraints in the rare-earth magnet ErBr3 govern low-energy dynamics and field-dependent thermodynamic responses.

**Main result.**

The local CEF symmetry enforces a vanishing leading-order transverse matrix element within the ground-state Kramers doublet, suppressing transverse magnetic excitations and resulting in a thermodynamic response that splits into a phase boundary and a crossover line under an in-plane field.

**Method.**

The study combines thermodynamic measurements (specific heat, magnetocaloric effect, magnetization) with inelastic neutron scattering (INS) and crystal-field analysis using the McPhase package.

**Summary.**

This paper demonstrates how the local symmetry of the crystal field in ErBr3 suppresses the lowest-order transverse magnetic fluctuations. By using neutron scattering and thermodynamic measurements, the authors show that the ground-state Kramers doublet's symmetry prevents certain magnetic transitions. This leads to a unique thermodynamic phase diagram where an in-plane magnetic field separates a phase boundary from a broader crossover. The study provides a clear link between single-ion symmetry and collective magnetic behavior in 2D honeycomb lattices.

<details><summary>Detailed structure</summary>

**Model / system.**

ErBr3, a layered honeycomb magnet with a rhombohedral BiI3-type structure where Er3+ ions (J=15/2) reside in a trigonal crystal-field environment.

**Key observables.**

Magnetization, specific heat, magnetocaloric effect, and inelastic neutron scattering intensity.

**Important parameters / regimes.**

Effective g-factor of approximately 13; CEF energy scales near 1.5 and 3 meV; zero-field thermodynamic anomalies at 0.375 K and 0.2 K.

**Assumptions / limitations.**

The analysis assumes the ground-state doublet belongs to a specific symmetry class determined by the mJ composition of the wave function.

**Figures summary.**

Fig 1 shows the crystal structure, magnetic anisotropy, and CEF energy levels; Fig 3 displays field-dependent specific heat and magnetocaloric effect maps showing phase boundaries and crossovers.

**Paper structure.**

The paper introduces the material and its structural properties, presents thermodynamic measurements under magnetic fields, details neutron scattering results, and concludes by relating the observed dynamics to the underlying crystal-field symmetry constraints.

</details>

<details><summary>Abstract</summary>

We show that the local crystal-field symmetry of ErBr$_3$ enforces $\langle ψ_\pm | J^{\pm} | ψ_\mp \rangle = 0$ within the ground-state Kramers doublet, thereby removing the lowest-order transverse channel from the low-energy sector. Thermodynamic measurements reveal two zero-field anomalies. Under an in-plane magnetic field, the thermodynamic response separates into a phase boundary and a broader crossover line. Consistently, inelastic neutron scattering measurements above the ordering temperature reveal no well-defined low-energy dispersive magnetic modes. These results show that the crystal-field ground-state symmetry strongly constrains the low-energy dynamics and provides a natural framework for understanding the field-dependent thermodynamic response of ErBr$_3$.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25524"></a>


### [Defect-Adaptive Lattice Surgery on Irregular Boundary Surface-Code Patches](http://arxiv.org/abs/2604.25524v1)

**Authors:** GunSik Min, Yujin Kang, Jun Heo

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25524v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25524_figures/2604.25524_fig1.jpg" width="500"><br>

<sub>FIG. 1. Boundary data-qubit defects during an XL ⊗XL merge. (a) A representative seam-boundary defect pair destroys the native seam region of the intended merge, so the regular defect-free seam picture no longer applies. (b) The broken neighborhood is reconstructed in terms of locally available gauge fragments and defect-adapted effective checks. (c) A naive opposite-type completion is invalid because the required cross-patch gauge bridge is not source-admissible. The surviving reduced opposite-type fragments are therefore left individually incompatible with the candidate X-type seam super-check. (d) The merge must therefore be carried out on the boundary-deformed patch using a...</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25524_figures/2604.25524_fig2.jpg" width="500"><br>

<sub>FIG. 2. Seam-check ancilla defect and support-preserving seam reconstruction. (a) A defective seam ancilla removes one native seam measurement from the merge interface while leaving the intended data-qubit support intact. (b) The missing seam measurement is replaced by a pair of repurposed local gauge measurements whose product reconstructs the seam value. (c) The adjacent opposite-type larger checks are promoted to gauges, and their product defines an induced super-stabilizer that restores the local commutation structure. In contrast to the boundary data-qubit defect in Fig. 1, this case is handled primarily by support-preserving measurement reconstruction rather than by a larger boundary...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25524_figures/2604.25524_fig3.jpg" width="500"><br>

<sub>FIG. 4. Compile yield versus defect rate (XX merge). The proposed method (solid, circles) consistently outperforms the standard method (dashed, squares) across all distances. At q = 0.5%, the proposed yield ranges from 0.968 to 0.995, compared with 0.826 to 0.920 for the standard method. At q = 2.0%, the proposed yield remains in the range 0.741– 0.904, whereas the standard method drops to 0.524–0.695. The gain reflects additional instances recovered by GF(2)- certified seam super-check reconstruction.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25524_figures/2604.25524_fig4.jpg" width="500"><br>

<sub>FIG. 3. Distance preservation under boundary defects for the compiled XX merge. (a) Average effective X-distance loss, d −deff, as a function of defect rate for the proposed method and the standard method. (b) Distance saved by the proposed method relative to the standard method, de- fined as (d −deff)std −(d −deff)prop. The increasing separa- tion with defect rate and distance shows that certified fused seam-super-check reconstruction mitigates geometry-induced distance degradation.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25524_figures/2604.25524_fig5.jpg" width="500"><br>

<sub>Figure 4 shows the compile yield as a function of defect rate for both methods across all five distances. At q = 0.5%, the proposed method achieves compile yield 0.968– 0.995, whereas the standard method gives 0.826–0.920, corresponding to a gain of +7–14 percentage points. This gap widens with increasing defect rate: at q = 2.0%, the proposed method yields 0.741–0.904 while the standard method yields only 0.524–0.695, i.e., a gain of +21–24 percentage points across the full distance range. The advantage is consistent across all studied dis- tances. The yield gain measures how often recovered seam rows turn an otherwise unavailable merge parity into a compilable one. Within our row-space...</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25524_figures/2604.25524_fig6.jpg" width="500"><br>

<sub>Figure 3 shows the average X-distance loss d −deff and the distance saved by the proposed method over the standard method. As plotted, this figure reports the XX- merge X-distance metric. Both methods incur larger ab- solute distance loss as the defect rate q increases and as the target distance d becomes larger. However, the proposed method consistently preserves more distance at every (d, q) point. The distance improvement comes from instances in which a broken native seam row would otherwise be re- moved from the effective seam family, but can instead</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25524_figures/2604.25524_fig7.jpg" width="500"><br>

<sub>FIG. 5. Logical performance of the compiled defect-adaptive XX merge at qdata = 1% and qanc = 0.5% under the SI1000- MR noise model. For each successful defect instance, the sampled circuit uses the synthesized seam-measurement rule and the merge-parity observable returned by the compiler. (a) Success-conditioned logical error rate, LER | compile success, as a function of physical error rate p for the proposed method and the defect-free merge reference. (b) LER ratio, defined as (LERproposed)/(LERdefect-free). The ratios remain modest at high p, while larger excursions in the lowest-LER regime are consistent with finite-sampling fluctuations. The largest ratio excursions occur at the...</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25524_figures/2604.25524_fig8.jpg" width="500"><br>

<sub>FIG. 6. Success-conditioned logical error rate for the compiled defect-adaptive ZZ merge. Solid curves show the proposed defect-adaptive merge and dashed curves show the defect-free ZZ-merge reference. The simulation uses the transposed seam geometry with the same synthesized-observable construction as the XX-merge sampling. The close, approximately par- allel curves provide a direct check that the certified parity- extraction rule carries over to the X ↔Z transposed merge under the i.i.d. defect model.</sub>

</details>

**Main problem.**

How to perform fault-tolerant lattice surgery (specifically the merge operation) when hardware defects like broken boundaries or missing ancillas disrupt the standard seam geometry.

**Main result.**

The introduction of a defect-adaptive compiler that uses GF(2) synthesis to reconstruct logical parities, achieving significantly higher compile yield and preserved code distance with minimal logical error overhead.

**Method.**

A three-layer synthesis approach (identification, certification, and extraction) that formulates parity reconstruction as a GF(2) binary-support synthesis problem and uses fused seam-super-check constructions.

**Summary.**

This paper addresses the challenge of performing logical operations in surface-code quantum computers when physical defects break the standard lattice geometry. The authors propose a compiler-level method that treats lattice surgery as a parity-synthesis problem, allowing the system to 'reconstruct' the desired logical operations from available, irregular measurements. Their approach significantly improves the success rate (compile yield) of operations on noisy hardware while maintaining the effective code distance. The method is robust enough to handle both missing data qubits and missing measurement ancillas.

<details><summary>Detailed structure</summary>

**Model / system.**

Surface-code-based quantum error correction on imperfect hardware, specifically planar patches with irregular boundaries, data-qubit defects, and ancilla-type defects.

**Key observables.**

Joint logical parity (XX and ZZ merges), gauge outcomes, and effective code distance.

**Important parameters / regimes.**

Physical error rate p (10^-3 to 10^-2), defect rates q (0.5% to 2.0%), and code distances d (9 to 17).

**Assumptions / limitations.**

The framework assumes that a valid defect-adapted patch has already been constructed (the memory problem is solved) and focuses specifically on the merge primitive.

**Figures summary.**

Figure 1 illustrates boundary data-qubit defects and seam reconstruction; Figure 2 shows seam-check ancilla defects and replacement via gauge measurements; Figure 3 shows X-distance loss; Figure 4 plots compile yield vs. defect rate; Figure 5 shows success-conditioned LER.

**Paper structure.**

The paper identifies the seam-boundary defect problem, proposes a unified algebraic synthesis framework, provides a formal theorem for parity execution, and validates the method through circuit-level simulations comparing compile yield, distance preservation, and logical error rates.

</details>

<details><summary>Abstract</summary>

Defect-adaptive surface-code methods have substantially advanced the construction of valid logical patches on imperfect hardware, but fault-tolerant computation also requires executable logical oper ations on the resulting irregular geometries. We formulate the seam-boundary defect problem: how to perform a lattice-surgery merge when the intended seam intersects deformed boundaries, disabled checks, and gauge-inferred super-stabilizers. We introduce a defect-adaptive lattice-surgery method that reconstructs the target joint logical parity from the seam-related measurements available on the irregular merged patch, together with constraints inherited from the separated pre-merge code space. The reconstruction is expressed as a compact GF(2) binary-support synthesis problem. If the requested parity is realizable, the solution gives an executable parity-extraction rule over raw, schedule-tagged gauge outcomes; otherwise, it certifies a parity-synthesis failure rather than conflat ing it with patch invalidity. The framework accommodates boundary data-qubit defects, seam-check ancilla defects, and gauge-inferred seam super-checks within a single synthesis layer. Circuit-level samples of the synthesized merge operation show improved compile yield, preserved effective dis tance, and only modest success-conditioned logical-error overhead relative to the defect-free merge reference; an explicit ZZ-merge sampling check confirms the expected transposed-geometry behav ior under the same success-conditioned observable construction. More broadly, the results identify certified parity synthesis as a compilation layer between defect-adaptive patch construction and executable fault-tolerant logical operations on imperfect surface-code hardware.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24937"></a>


### [Dielectric signatures of crystal-field and low-temperature correlated dynamics in NdMgAl11O19](http://arxiv.org/abs/2604.24937v1)

**Authors:** Sonu Kumar, Gaël Bastien, Maxim Savinov, Małgorzata Śliwińska-Bartkowiak, Ross H. Colman, Stanislav Kamba

**Type:** experiment · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.24937v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.24937_figures/2604.24937_fig1.jpg" width="500"><br>

<sub>FIG. 1. Dielectric response of NdMgAl11O19. (a) Zero-field permittivity ε′ c(T) measured at f = 9 kHz; the solid line is the combined fit using a Barrett background and a term associated with thermal depopulation of the first excited CEF doublet [Eqs. (1)–(3)]. (b,c) Temperature dependence of ε′ c(T) at selected frequencies in (b) µ0H = 0 and (c) µ0H = 9 T.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24937_figures/2604.24937_fig2.jpg" width="500"><br>

<sub>Figure 1(a) shows the temperature dependence of the real part of the dielectric permittivity, ε′ c(T), measured in zero magnetic field at f = 9 kHz up to 275 K. On cool- ing, ε′ c(T) increases, passes through a broad maximum near ∼25–30 K, then decreases and finally shows a fur- ther upturn below a few kelvin. Between approximately 35 and 200 K, the response is nearly frequency indepen- dent within the experimental resolution, indicating that this interval is dominated by the intrinsic high-frequency dielectric background. In this temperature range, the smooth increase of ε′ c(T) on cooling is well described by a Barrett formula [Eq. (1)], as commonly used in incip- ient ferroelectrics and...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24937_figures/2604.24937_fig3.jpg" width="500"><br>

<sub>FIG. 2. Temperature dependence of ε′ c(T) of NdMgAl11O19 in magnetic fields µ0H = 0–9 T: (a) f = 113 Hz, (b) f = 1.6 kHz, (c) f = 35 kHz, and (d) f = 95 kHz.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24937_figures/2604.24937_fig4.jpg" width="500"><br>

<sub>FIG. 3. Field dependence of the real permittivity ε′ c(H) of NdMgAl11O19. Panels (a) and (b) show measurements at several frequencies between 158 Hz and 167 kHz at (a) T = 0.36 K and (b) T = 2 K. Panel (c) compares ε′ c(H) measured at the selected frequency f = 1.6 kHz for T = 0.36 K and T = 2 K. The vertical dashed line marks the crossover field µ0Hc ≃0.85 T.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.24937_figures/2604.24937_fig5.jpg" width="500"><br>

<sub>FIG. 4. Temperature dependence of the loss tangent tan δ(T) of NdMgAl11O19 measured at various frequencies with E ∥H ∥c in (a) µ0H = 0 T and (b) µ0H = 9 T.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.24937_figures/2604.24937_fig6.jpg" width="500"><br>

<sub>FIG. 5. Cole–Cole analysis of the frequency-dependent real permittivity of NdMgAl11O19. Panels (a) and (b) show represen- tative fits of ε′ c(f) using the Cole–Cole form [Eq. (B1)] at selected temperatures in µ0H = 0 and 9 T, respectively. Panels (c) and (d) show the temperature dependence of the characteristic relaxation frequency frel = 1/(2πτ) and the Cole–Cole broad- ening parameter α, respectively, extracted from fits in µ0H = 0, 2, and 9 T.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.24937_figures/2604.24937_fig7.jpg" width="500"><br>

<sub>FIG. 6. Qualitative schematic of broadening and field evolution in the low-energy CEF sector of NdMgAl11O19. Panel (a) shows an idealized single-ion picture without broadening: a degenerate zero-field ground-state doublet evolves into two Zeeman-split branches with increasing field. Panels (b)–(d) illustrate the corresponding broadened low-energy response in the presence of disorder and weak interactions. In panel (b), the zero-field response appears as an unresolved broadened doublet. In panel (c), the applied field separates the low-energy manifold into two partially overlapping broadened branches. In panel (d), the same two branches are more clearly resolved at higher field, approaching...</sub>

</details>

**Main problem.**

The study aims to distinguish between crystal-electric-field (CEF) effects and low-temperature correlated magnetic dynamics in the frustrated magnet NdMgAl11O19.

**Main result.**

The researchers identified three dielectric components: a Barrett-like host background, a CEF-related contribution from the first excited doublet at ~26 K, and a low-temperature dispersive channel driven by AFM correlations and disorder.

**Method.**

Dielectric spectroscopy was performed on single crystals using an impedance analyzer across a wide temperature (0.3 K to 275 K) and magnetic field (up to 9 T) range.

**Summary.**

This paper investigates the dielectric properties of the frustrated magnet NdMgAl11O19. By using dielectric spectroscopy, the authors successfully separate the signatures of high-energy crystal-field excitations from low-energy magnetic correlations. They demonstrate how an applied magnetic field can tune the system from a correlated, disorder-broadened regime to a distinct single-ion regime. This work provides a clear reference for understanding how local structural disorder and exchange interactions compete in Kramers-protected systems.

<details><summary>Detailed structure</summary>

**Model / system.**

The system is NdMgAl11O19, a magnetoplumbite hexaaluminate featuring Nd3+ moments on a frustrated triangular lattice and a polarizable AlO5 network.

**Key observables.**

Real part of the permittivity (epsilon'_c), loss tangent (tan delta), and the Cole-Cole broadening parameter (alpha).

**Important parameters / regimes.**

CEF energy gap (delta = 25.85 K), crossover magnetic field (mu0Hc = 0.85 T), and the dynamical energy scale (W/kB = 1.9 K).

**Assumptions / limitations.**

The analysis assumes the presence of local structural disorder (Mg/Al site mixing) and uses a qualitative model for the evolution of the CEF sector under magnetic fields.

**Figures summary.**

Figure 1 shows zero-field permittivity vs temperature; Figure 6 provides a qualitative schematic of the CEF doublet evolution from a broadened zero-field state to a resolved single-ion limit in high fields.

**Paper structure.**

The paper introduces the material and its magnetic properties, presents dielectric spectroscopy results across temperature and field, analyzes the CEF energy scales using the Barrett formula, discusses low-temperature dynamics and disorder, and concludes with a schematic model of the field-tuned energy landscape.

</details>

<details><summary>Abstract</summary>

We report dielectric spectroscopy of single-crystalline \ce{NdMgAl11O19}, a magnetoplumbite hexaaluminate in which localized \ce{Nd^{3+}} moments coexist with a polarizable \ce{AlO5} bipyramidal network. The real part of the permittivity, $\varepsilon'_{c}(T)$, measured along the crystallographic $c$ axis, increases as the temperature is lowered from 275~K to 30~K and is frequency-independent between 4~Hz and 50~kHz. At lower temperatures, a frequency-dependent decrease in permittivity is observed, followed by a further upturn below 2~K. The high-frequency $\varepsilon'_{c}(T)$ is described by a Barrett formula supplemented by an effective two-level contribution, yielding a robust gap of $Δ= 25.85 \pm 0.32$~K consistent with the lowest \ce{Nd^{3+}} crystal-electric-field (CEF) splitting. Below $\sim 30$~K, the dielectric response becomes strongly frequency and magnetic-field dependent. Isothermal $\varepsilon_c'(H)$ measurements reveal a reproducible low-field crossover near $μ_0H_c \simeq 0.85$~T, which we attribute to the competition between antiferromagnetic correlations and Zeeman splitting of the ground-state Kramers doublet. \ce{NdMgAl11O19} thus provides a Kramers reference system in which dielectric signatures of the excited-state CEF manifold can be distinguished from those of the field-tuned, correlation-dominated ground-state doublet sector in a centrosymmetric frustrated magnetoplumbite host

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25450"></a>


### [Differentiation of electron doping and oxygen reduction in electron-doped cuprates](http://arxiv.org/abs/2604.25450v1)

**Authors:** M. Miyamoto, M. Horio, K. Moriya, A. Takahashi, K. Tanaka, Y. Koike, T. Adachi, I. Matsuda

**Type:** experiment · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25450v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25450_figures/2604.25450_fig1.jpg" width="500"><br>

<sub>FIG. 1. Characterization of the as-grown sample. (a) Crystal structure of PLCCO with an impurity oxygen atom at the apical site. (b) Fermi surface map of the as-grown PLCCO (x = 0.08) sample. The red curves indicate the result of tight-binding fitting with the √</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25450_figures/2604.25450_fig2.jpg" width="500"><br>

<sub>FIG. 2. Effect of electron doping on the as-grown sample. (a) Schematic illustration of photoemission from the K-dosed surface. The adsorbed K atoms are ionized and donate electrons to the sample surface. (b) Core-level spectra of the as-grown PLCCO (x = 0.08) sample before and after K dosing. (c), (d) Fermi surface maps for the as-grown PLCCO (x = 0.08) samples #1 and #2, respectively. The results of tight-binding fitting (eq. 1) are shown as blue curves. EDCs (e) at the node and (f) at the hot spot taken from the points indicated in (c), (d), and Fig. 1(b).</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25450_figures/2604.25450_fig3.jpg" width="500"><br>

<sub>FIG. 3. Influence of disorder on the pseudogap. (a) Fermi surface map of the annealed PLCCO (x = 0.10) sam- ple. The black curve indicates the result of tight-binding fit- ting (eq. 1). (b) Comparison of Fermi wavenumber kF for the x = 0.10 annealed sample and the K-dosed x = 0.08 as-grown sample. (c) Momentum distribution curves for the two sam- ples at the Fermi level plotted along the BZ boundary [black arrow in (a)]. To alleviate intensity variation due to matrix- element effects, photoemission signals have been symmetrized with respect to the kx + ky = 0 line. (d) EDCs at the hot spot (indicated in the inset) for the two samples.</sub>

</details>

**Main problem.**

The study aims to disentangle whether the pseudogap and superconductivity in electron-doped cuprates are driven by electron concentration (via Ce substitution) or by oxygen non-stoichiometry (via reduction annealing).

**Main result.**

While alkali-metal dosing increases electron concentration and suppresses antiferromagnetic Fermi surface reconstruction, the pseudogap persists, suggesting that the pseudogap is driven by impurity oxygen atoms rather than just carrier density.

**Method.**

The researchers used Angle-Resolved Photoemission Spectroscopy (ARPES) combined with potassium (K) dosing on the surface of PLCCO crystals to inject electrons without changing oxygen content.

**Summary.**

This paper investigates the origin of the pseudogap in electron-doped cuprates by separating the effects of electron doping from oxygen reduction. By using potassium dosing to add electrons to the surface without altering oxygen levels, the authors show that the pseudogap remains even when the Fermi surface reconstruction is suppressed. This leads to the conclusion that apical oxygen impurities are a key factor in the formation of the pseudogap. The findings provide crucial insight into the complex interplay between chemistry and electronic correlations in high-Tc superconductors.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system is the electron-doped cuprate Pr1.3-xLa0.7CexCuO4 (PLCCO), studied using a 2D tight-binding model with sqrt(2) x sqrt(2) antiferromagnetic order to fit Fermi surface data.

**Key observables.**

Fermi surface maps, Energy Distribution Curves (EDCs), Fermi surface area (n_FS), and K 3p core-level spectra.

**Important parameters / regimes.**

Electron concentration (n_FS), spectral gap (Delta), and the presence of apical oxygen impurities.

**Assumptions / limitations.**

The ARPES measurements are surface-sensitive, probing only the topmost CuO2 layer (inelastic mean free path ~5 A).

**Figures summary.**

Fig 1 shows the crystal structure, Fermi surface maps, and EDCs for as-grown samples; Fig 2 shows K-dosing schematics, K 3p spectra, and the resulting increase in electron concentration and Fermi surface changes.

**Paper structure.**

The paper introduces the problem of oxygen vs. doping, describes the K-dosing and ARPES experimental setup, presents results showing the persistence of the pseudogap despite increased doping, and concludes that oxygen impurities are the primary driver of the pseudogap.

</details>

<details><summary>Abstract</summary>

Electron-doped cuprates require not only electron doping by chemical substitution but also post-growth reduction annealing for realizing superconductivity. However, electron concentration can also be varied by reduction annealing, making it challenging to disentangle the respective influences of electron concentration and oxygen non-stoichiometry. Here, by combining alkali-metal dosing and angle-resolved photoemission spectroscopy, we monitored changes in the electronic structure of an electron-doped cuprate while supplying additional electrons to its surface without modifying oxygen content. Whereas a Fermi surface reconstruction due to long-range antiferromagnetic order was suppressed by alkali-metal deposition, the pseudogap -- which is associated with short-range spin/charge correlations and can be suppressed by efficient reduction annealing -- was found to persist. The results highlight significant contribution of impurity oxygen atoms to pseudogap formation in electron-doped cuprates.

</details>

<sub>[↑ back to top](#top)</sub>
