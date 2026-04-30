# Daily arXiv Report

[← Index](index.md)

[← Previous](papers_08.md)
[Next →](papers_10.md)

## Papers 161–180


<a id="paper-2604.25333"></a>


### [Sign Embedding Quantum Algorithms for Matrix Equations and Matrix Functions](http://arxiv.org/abs/2604.25333v1)

**Authors:** Yanqiao Wang, Jin-Peng Liu

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25333v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `methods for driven-dissipative` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25333_figures/2604.25333_fig1.jpg" width="500"><br>

<sub>Figure 1: method overview</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25333_figures/2604.25333_fig2.jpg" width="500"><br>

<sub>Figure 2: shift-rotation and common scaling</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25333_figures/2604.25333_fig3.jpg" width="500"><br>

<sub>Figure 3: Roadmap for the three ordinary Sylvester regimes treated in Section 6.</sub>

</details>

**Main problem.**

Developing a systematic quantum algorithmic framework for solving various matrix equations (such as Sylvester, Lyapunov, and Riccati equations) and computing matrix functions (such as square roots and geometric means) in an operator-output setting.

**Main result.**

The authors introduce a 'sign-embedding' framework that provides explicit block-encodings for a wide array of structured matrix problems, achieving query complexity that is linear in inverse-conditioning parameters and logarithmic in error tolerance.

**Method.**

The framework uses a three-step pipeline: compressing the target operator into a matrix sign object, applying a logarithmic-sinc quadrature rule for rational approximation, and implementing the resulting shifted inverses using Quantum Singular Value Transformation (QSVT).

**Summary.**

This paper presents a unified quantum computing framework for solving complex matrix equations and computing matrix functions. By using a 'sign-embedding' technique, the authors can transform difficult matrix problems into a standardized form that is easier to implement on a quantum computer. The method is particularly powerful because it works for non-normal and non-diagonalizable matrices, provided certain spectral gaps are known. The resulting algorithms are highly efficient, scaling logarithmically with the required precision.

<details><summary>Detailed structure</summary>

**Model / system.**

The paper focuses on mathematical operators including the Sylvester operator (AX + XB = C), the Lyapunov equation, the Continuous-time Algebraic Riccati Equation (CARE), and matrix functions like the principal square root and matrix geometric means.

**Important parameters / regimes.**

Field-of-Values (FoV) gap, strip-resolvent bounds, error tolerance (epsilon), and conditioning parameters (mu, gamma, and kappa).

**Assumptions / limitations.**

The algorithms rely on the existence of a Field-of-Values gap or a strip-resolvent hypothesis to ensure error control and handle non-normal or non-diagonalizable matrices.

**Figures summary.**

Figure 1 illustrates the algorithmic pipeline from sign function to QSVT implementation; Figure 2 shows the transformation of matrices to separate their numerical ranges along the real axis.

**Paper structure.**

The paper introduces the sign-embedding framework, details the mathematical construction of the augmented matrices for various equations, describes the log-sinc approximation and QSVT implementation, provides complexity analysis for different regimes (FoV gap and strip-resolvent), and concludes with a comparative analysis against existing quantum algorithms.

**Why it may be interesting.**

This is highly relevant for researchers in open quantum systems and many-body dynamics, as the ability to efficiently solve Riccati and Lyapunov equations is fundamental to studying master equations, stability, and control in quantum systems.

</details>

<details><summary>Abstract</summary>

We develop a systematic sign-embedding framework of operator-output quantum algorithms for matrix equations and matrix functions. Differing from the contour-integral treatment, we start with the matrix-sign embedding route: an augmented matrix $M$ whose half-plane matrix sign compresses the target operator either as a block of $\text{sign}(M)$ or, in projector form, through $(I-\text{sign}(M))/2$; we then construct a logarithmic-sinc approximation for the half-plane sign operator and combine it with structure-aware scaled multiplexing and nodewise rebalancing of shifted inverse families. For ordinary Sylvester equations, we offer an explicit block-encoding of the target matrix solution with query complexity linear in the inverse-conditioning parameters and logarithmic in the target error tolerance, under non-normal and non-diagonalizable settings given a field-of-values (FoV) gap or strip-resolvent hypotheses. These algorithms propagate the same overlap-based normalization bookkeeping to ordinary and generalized Sylvester equations, generalized Lyapunov equations, principal square roots and inverse square roots, matrix geometric means, and continuous-time algebraic Riccati equations (CARE). These results identify matrix-sign embeddings and nodewise rebalancing as reusable design principles for structured operator-output quantum linear algebra.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24871"></a>


### [Six textbook mistakes in quantum field theory](http://arxiv.org/abs/2604.24871v1)

**Authors:** Alexandros Gezerlis

**Type:** theory · **Category:** other · **PDF:** <https://arxiv.org/pdf/2604.24871v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `Keldysh / 2PI / non-Gaussian methods` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.24871_figures/2604.24871_fig1.jpg" width="500"><br>

<sub>FIG. 1: Connected, momentum-space, second-order Feynman diagrams representing the S-matrix in a 2 →2 process (for a quartic interaction) in the s, t, and u channels.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24871_figures/2604.24871_fig2.jpg" width="500"><br>

<sub>FIG. 2: Contour of integration for Wick rotation, relevant to the 2 →2 process of Fig. 1 for the cases of: (a) k2 + ∆&gt; 0, and (b) k2 + ∆&lt; 0.</sub>

</details>

**Main problem.**

The paper identifies and corrects widespread conceptual errors and pedagogical 'muddledness' found in introductory Quantum Field Theory (QFT) textbooks and research literature.

**Main result.**

The author provides rigorous corrections to six specific themes, including the validity of relativistic quantum mechanics, the derivation of Noether's theorem, the proper promotion of fields to operators, particle localization, normal ordering, and the nature of Wick rotation.

**Method.**

The author uses a comparative approach, quoting specific textbook mistakes and providing mathematically rigorous corrections using canonical quantization, contour integration, and the Newton-Wigner position operator.

**Summary.**

This paper serves as a pedagogical critique of common misconceptions in Quantum Field Theory textbooks. The author identifies six specific areas where introductory texts often sacrifice mathematical rigor for simplicity, potentially leading to fundamental misunderstandings. By providing corrected derivations and physical insights, the work aims to prevent the propagation of these errors in the physics literature. It is particularly useful for instructors and graduate students seeking a deeper, more accurate foundation in QFT.

<details><summary>Detailed structure</summary>

**Model / system.**

The discussion focuses on relativistic scalar field theory (Klein-Gordon field) and scalar electrodynamics, specifically examining the transition from classical Lagrangian/Hamiltonian density to the interacting S-matrix.

**Key observables.**

S-matrix (scattering amplitude), Feynman propagator, probability density, and conserved currents.

**Important parameters / regimes.**

Mass (m), coupling constant (lambda), momentum (k, p, q), and the infinitesimal epsilon (i-epsilon prescription).

**Assumptions / limitations.**

The discussion is limited to the core aspects of QFT relevant to a first-semester graduate course and assumes familiarity with basic relativistic quantum mechanics.

**Figures summary.**

Figure 1 shows momentum-space second-order Feynman diagrams for a 2 to 2 process; Figure 2 illustrates the integration contour in the complex k0 plane for different pole configurations.

**Paper structure.**

The paper begins with a notation summary, followed by a systematic presentation of six thematic errors, each containing a textbook quote, a mathematical correction, and references to authoritative literature, concluding with a pedagogical reflection.

</details>

<details><summary>Abstract</summary>

This article discusses incorrect statements appearing in textbooks on quantum field theory (QFT); some of these mistakes also appear in the research literature. The focus is not on errors made by an individual author, but on conceptual muddledness that is widespread in introductory textbooks. We start from a bare-bones summary of QFT, meant to establish the notation. We then turn to our six paradigmatic themes, in each case quoting a specific example of the textbook mistake, a summary of material that is known to experts but is frequently mishandled in introductory works, pointers to authoritative references where the relevant concept is handled properly, as well as a concise correction that rectifies any issues. The goal of this work is to warn readers of the existence of several pitfalls and thereby stop these errors from further propagating in the literature on QFT.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25060"></a>


### [Statistical mechanics in continuous space with tensor network methods](http://arxiv.org/abs/2604.25060v1)

**Authors:** Gunhee Park, Tomislav Begušić, Si-Jing Du, Johnnie Gray, Garnet Kin-Lic Chan

**Type:** theory · **Category:** numerical methods · **PDF:** <https://arxiv.org/pdf/2604.25060v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `methods for driven-dissipative` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25060_figures/2604.25060_fig1.jpg" width="500"><br>

<sub>FIG. 2. (a) Diagrammatic representation of the factor graph for the hard disk partition function, where the on-site and pairwise terms are shown as pink circles and blue squares, respectively. (b) When the pair connectivity is restricted to nearest-neighbor and next-nearest-neighbor interactions, the factor graph can be transformed into an equivalent represen- tation where tensors are placed at the original lattice sites and at the centers of the square units.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25060_figures/2604.25060_fig2.jpg" width="500"><br>

<sub>FIG. 1. (a) Particles in a box. (b) Same system in the site rep- resentation, where colors denote occupied lattice grid points. (c) Grid points in a cell are coarse-grained into one effective site.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25060_figures/2604.25060_fig3.jpg" width="500"><br>

<sub>FIG. 3. 2 × 2 unit cell structure for the transfer matrix of the partition function composed of S and T tensors in the infinite tensor network. Its boundary MPS is characterized by two alternating two-site uniform MPS with tensors (A11, A12) and (A21, A22).</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25060_figures/2604.25060_fig4.jpg" width="500"><br>

<sub>FIG. 4. Within the infinite TN framework, the density is plot- ted as a function of MPS bond dimension using the boundary contraction method. The reference MC data is shown as the dashed lines, where the MC is performed on a finite system with L = 28 using periodic boundary conditions.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25060_figures/2604.25060_fig5.jpg" width="500"><br>

<sub>FIG. 5. Spatially resolved densities in a finite box with open boundary conditions at µ = 2, 6, 10, and 12.</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25060_figures/2604.25060_fig6.jpg" width="500"><br>

<sub>FIG. 6. Pair correlation functions computed from infinite TN and MC calculations. For the MC reference, the GCMC data from both the continuous space (red dotted) and the discretized lattice (black dashed) are presented.</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25060_figures/2604.25060_fig7.jpg" width="500"><br>

<sub>FIG. 7. (a) Free energy convergence using the TN boundary contraction method as a function of MPS bond dimension for various system sizes. Free energy convergence is quantified by the computed free energy density difference between the given bond dimension and the maximum bond dimension, χmax = 600. Free energy density values for different system sizes are plotted in the inset. (b) The number of Monte Carlo steps in the Wang-Landau algorithm as a function of area. The inset shows a comparison of the free energy density calculated via the TN and MC methods. See the main text for the details of the Monte Carlo procedures.</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25060_figures/2604.25060_fig8.jpg" width="500"><br>

<sub>FIG. 8. Density as a function of lattice discretization constant compared to density in the continuum, indicated as dashed lines, at three different chemical potential values.</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25060_figures/2604.25060_fig9.jpg" width="500"><br>

<sub>Fig. 8 shows the convergence of the density values as a function of the lattice discretization in the lattice GCMC calculations compared to GCMC in the contin- uum, where the smallest lattice discretization used in the plot corresponds to the lattice discretization value used in this work.</sub>

</details>

**Main problem.**

Extending tensor network (TN) methods, which are traditionally limited to lattice models, to simulate interacting particle systems in continuous space.

**Main result.**

The developed TN framework accurately reproduces local observables and captures liquid-to-solid phase transitions in 2D hard-disk systems, offering a deterministic alternative to Monte Carlo methods with linear scaling of computational cost relative to system size.

**Method.**

A real-space discretization and cell-based coarse-graining scheme are used to map continuous particles onto an effective lattice model, which is then solved using TN boundary contraction via Matrix Product States (MPS) and Matrix Product Operators (MPO).

**Summary.**

This paper presents a new way to use tensor networks to study classical statistical mechanics in continuous space. By discretizing space into a grid and using a coarse-graining scheme, the authors transform a continuous particle problem into an effective lattice model. This allows for the deterministic calculation of absolute free energies and local observables, such as density and pair correlation functions. The method is shown to be highly efficient, scaling linearly with system size, and successfully captures the liquid-to-solid phase transition in hard-disk systems.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on 2D hard-disk systems with a pairwise repulsive potential, where continuous coordinates are mapped to a fine grid and grouped into cells to create an effective lattice representation.

**Key observables.**

Density, pair correlation functions, and absolute free energy density.

**Important parameters / regimes.**

Inverse temperature (beta), chemical potential (mu), lattice constant (a), and tensor network bond dimension (D).

**Assumptions / limitations.**

The method assumes a discretization of continuous space and uses a coarse-graining approximation where each cell contains at most one particle; the current scope is limited to 2D and short-range potentials.

**Figures summary.**

Figure 1 shows the mapping from particles to a coarse-grained cell model; Figure 2 illustrates the factor graph and TN representation; Figure 3 shows the unit cell structure; Figure 4 shows density convergence with bond dimension; Figure 5 displays spatially resolved densities in a finite box; Figure 6 compares pair correlation functions with GCMC; Figure 7 compares free energy convergence and computational scaling; Figure 8 demonstrates convergence to the continuum limit.

**Paper structure.**

The paper introduces the problem of continuous-space simulation, details the discretization and coarse-graining methodology, describes the construction of the tensor network, presents benchmark results against Monte Carlo simulations (density, correlation, and free energy), and concludes with scaling analysis and future directions.

</details>

<details><summary>Abstract</summary>

Tensor network (TN) methods are well established for computing partition functions in statistical mechanics, though this use has traditionally been limited to lattice models. We extend the scope of TN methodology to interacting particle systems in continuous space. Through a real-space discretization combined with a cell-based coarse-graining scheme, we formulate an effective lattice model that explicitly preserves spatial locality. The partition function of this model is represented as a TN, and the thermodynamic quantities are computed via boundary contraction. We apply this framework to the two-dimensional hard-disk problem and demonstrate the strengths of the TN formulation compared to existing Monte Carlo simulations.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.24847"></a>


### [The Classification of Pauli Stabilizer Codes: A Lattice and Continuum Treatise](http://arxiv.org/abs/2604.24847v1)

**Authors:** Bowen Yang, Matthew Yu

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.24847v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `entanglement & information structure` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.24847_figures/2604.24847_page2.jpg" width="500"><br>

<sub>Low-resolution page preview, page 2</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.24847_figures/2604.24847_page3.jpg" width="500"><br>

<sub>Low-resolution page preview, page 3</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.24847_figures/2604.24847_page4.jpg" width="500"><br>

<sub>Low-resolution page preview, page 4</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.24847_figures/2604.24847_page5.jpg" width="500"><br>

<sub>Low-resolution page preview, page 5</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.24847_figures/2604.24847_page6.jpg" width="500"><br>

<sub>Low-resolution page preview, page 6</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.24847_figures/2604.24847_page7.jpg" width="500"><br>

<sub>Low-resolution page preview, page 7</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.24847_figures/2604.24847_page8.jpg" width="500"><br>

<sub>Low-resolution page preview, page 8</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.24847_figures/2604.24847_page9.jpg" width="500"><br>

<sub>Low-resolution page preview, page 9</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.24847_figures/2604.24847_page10.jpg" width="500"><br>

<sub>Low-resolution page preview, page 10</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.24847_figures/2604.24847_page11.jpg" width="500"><br>

<sub>Low-resolution page preview, page 11</sub>

</details>

**Main problem.**

The classification of mobile Pauli stabilizer codes up to gapped interfaces and coarse-graining, and establishing the relationship between these lattice models and continuum framed TQFTs.

**Main result.**

The authors establish a bulk-boundary correspondence where the equivalence class of a Pauli stabilizer code is described by a Clifford QCA in one dimension higher, and identify qualitative distinctions between lattice and continuum theories regarding gapped boundaries.

**Method.**

The study utilizes algebraic L-theory, surgery theory, and homological algebra within a categorical framework of perfect chain complexes and quadratic functors.

**Summary.**

This paper provides a rigorous mathematical classification of Pauli stabilizer codes using the framework of algebraic L-theory. It establishes a fundamental link between lattice-based stabilizer codes and continuum-based topological quantum field theories (TQFTs). A key finding is a bulk-boundary correspondence relating stabilizer codes to Clifford Quantum Cellular Automata. The work also highlights how lattice theories can admit gapped boundaries in dimensions where continuum TQFTs cannot.

<details><summary>Detailed structure</summary>

**Model / system.**

The system consists of Pauli stabilizer codes defined by commuting subgroups of the Pauli operator algebra on a spatial lattice Z^n, specifically focusing on translation-invariant, mobile excitations.

**Key observables.**

Topological charges (point-like, string-like, and membrane-like excitations) and their braiding relationships.

**Important parameters / regimes.**

Lattice dimension n, Krull dimension of excitations (restricted to zero for mobile codes), and the prime p for qudit systems.

**Assumptions / limitations.**

The work assumes translation invariance and restricts the scope to 'mobile' stabilizer codes where excitations have Krull dimension zero.

**Figures summary.**

Table 1 provides a structural analogy between Pauli stabilizer codes, TQFTs, and manifold theory, mapping physical concepts like mobile excitations to mathematical concepts like n-morphisms.

**Paper structure.**

The paper introduces the algebraic framework for stabilizer codes, develops a classification using L-theory, establishes a bulk-boundary correspondence with Clifford QCAs, and concludes by comparing the results to the classification of framed TQFTs.

</details>

<details><summary>Abstract</summary>

We classify mobile Pauli stabilizer codes up to gapped interfaces and coarse-graining using the framework of algebraic $\mathrm{L}$-theory. We compare this classification with that of framed TQFTs, theories that arise naturally in the continuum, highlighting a close structural relationship between the two. Our approach is formulated in the category of perfect chain complexes equipped with quadratic functor over the Laurent polynomial ring $R = \mathbb{Z}/p[x_1^{\pm 1}, \ldots, x_n^{\pm 1}]$, within which the collection of topological operators of Pauli stabilizer codes arise naturally as objects. In particular, we establish a bulk-boundary correspondence for lattice theories: the equivalence class of a Pauli stabilizer code up to gapped interface is described by a Clifford QCA in one dimension higher. This is done using the universal target category for stabilizer codes, which is the categorical spectrum whose existence and universal properties are introduced in this work. We conclude by highlighting subtle differences between the classification of Pauli stabilizer codes and TQFTs, leading to qualitative distinctions between lattice and continuum theories.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25790"></a>


### [The mixed-dimensional quantum MacWilliams identity: bounds for codes and absolutely maximally entangled states in heterogeneous systems](http://arxiv.org/abs/2604.25790v1)

**Authors:** David González-Lociga, Simeon Ball

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25790v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `entanglement & information structure` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25790_figures/2604.25790_fig1.jpg" width="500"><br>

<sub>FIG. 1. Existence of mixed-dimensional AME states formed by qubits and qutrits based on the positivity of shadow multiset enumerators. Green squares represent potentially existing states, while red squares indicate states strictly forbidden by negative shadow enumerators. Blue squares are already existing states in homogeneous systems [21, 22]. The seven-qubit AME state was ruled out by [23], marked with a cross. Purple squares represent existing AME states in heterogeneous scenarios. The C2 ⊗C3 has the trivial AME 1 √</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25790_figures/2604.25790_fig2.jpg" width="500"><br>

<sub>FIG. 2. Existence of mixed-dimensional AME states based on the positivity of shadow multiset enumerators for qutrits and ququarts. Green squares represent potentially existing states, while red squares indicate states strictly forbidden by negative shadow enumerators. Blue squares are already existing states in homogeneous systems [21, 22]. Purple squares represent existing AME states in heterogeneous scenarios given in Eqs. (A1) and (A2). The AME formed by a single qutrit and single ququart is trivial.</sub>

</details>

**Main problem.**

The lack of a formal mathematical framework to characterize quantum error-correcting codes (QECC) and absolutely maximally entangled (AME) states in heterogeneous quantum architectures where local dimensions vary across subsystems.

**Main result.**

The derivation of a mixed-dimensional quantum MacWilliams identity and shadow identity, which allows for the formulation of generalized Hamming, Singleton, and Scott bounds, as well as a new tighter Singleton bound for pure codes.

**Method.**

The authors introduce a framework based on dimension multisets and multivariate weight enumerators, utilizing linear programming and a combinatorial grid method for state construction.

**Summary.**

This paper develops a new mathematical language to describe quantum error correction in heterogeneous systems, such as networks combining qubits and higher-dimensional qudits. By replacing standard scalar weights with dimension multisets, the authors establish a mixed-dimensional version of the MacWilliams identity. This allows them to derive new, tighter bounds on code parameters and identify specific configurations where absolutely maximally entangled states are physically impossible. The work provides a systematic way to evaluate the viability of complex, multi-dimensional quantum architectures.

<details><summary>Detailed structure</summary>

**Model / system.**

Mixed-dimensional Hilbert spaces formed by the tensor product of subsystems with varying local dimensions (e.g., combinations of qubits, qutrits, and ququarts) representing heterogeneous quantum networks.

**Key observables.**

Shor-Laflamme enumerators, unitary weight enumerators, shadow weight enumerators, and dimensional minimum distance.

**Important parameters / regimes.**

Code dimension (K), dimensional minimum distance (D), dimension multisets, and the AME threshold (Delta).

**Assumptions / limitations.**

The framework assumes a 'nice error basis' closed under multiplication and that the operators used in the weight enumerators are Hermitian.

**Figures summary.**

Heatmaps showing the existence/non-existence landscape of AME states for varying qubit/qutrit/ququart configurations, and combinatorial grids used for state construction.

**Paper structure.**

The paper begins by introducing the dimension multiset framework, moves to the derivation of the mixed-dimensional MacWilliams and shadow identities, establishes generalized bounds (Hamming, Singleton, Scott) and a feasibility linear program, and concludes with the analysis and construction of AME states.

</details>

<details><summary>Abstract</summary>

As emerging quantum architectures evolve into heterogeneous networks combining different physical substrates, such as qubits for logic and higher-dimensional qudits for robust communication, the traditional scalar metrics of quantum error correction become insufficient. To address this, we introduce a mathematical framework based on dimension multisets to characterize quantum error-correcting codes (QECC) and absolutely maximally entangled (AME) states in mixed-dimensional Hilbert spaces. By replacing scalar weights with multisets, we accurately capture the exact physical composition of error supports across these diverse systems. Our central result is the mixed-dimensional quantum MacWilliams identity, which establishes the formal algebraic relationship between Shor-Laflamme enumerators and unitary weight enumerators. From this foundation, we deduce the mixed-dimensional shadow identity and derive rigorous, generalized constraints on code parameters, explicitly formulating the mixed-dimensional quantum Hamming, Singleton and Scott bounds, and developing a linear program to systematically evaluate code viability. For the Singleton bound, a tighter bound that has no homogeneous analogue is derived for pure mixed-dimensional codes. Finally, we deploy this enumerator machinery to thoroughly analyze AME states, utilizing shadow inequalities to constrain their existence and introducing a combinatorial grid method for the explicit construction of mixed-dimensional tripartite AME states.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25115"></a>


### [Tunable thermal conductivity through dual spin-phonon coupling in van der Waals ferromagnetic insulator Cr2Ge2Te6](http://arxiv.org/abs/2604.25115v1)

**Authors:** Zhongbin Wang, Wenlong Tang, Simin Pang, Hongxing Zhu, Renkang Fan, Baohai Jia, Junxue Li, Ben Xu, Jun Zhang, Lin Xie, Jiaqing He

**Type:** experiment · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25115v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `spintronics-quantum-optics interface` **2/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25115_figures/2604.25115_fig1.jpg" width="500"><br>

<sub>Fig. 1: Magnetothermal transport in the dual magnon-phonon coupling regime of Cr2Ge2Te6 (CGT).</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25115_figures/2604.25115_fig2.jpg" width="500"><br>

<sub>Fig.2: High-field resonance dip originating from magnon-phonon hybridization.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25115_figures/2604.25115_fig3.jpg" width="500"><br>

<sub>Fig. 3: Low-field anisotropic magnetothermal conductivity originating from magnetic anisotropy</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25115_figures/2604.25115_fig4.jpg" width="500"><br>

<sub>Fig. 4: Magnetothermal transport phase diagram Δκ(H, θ) at low temperatures.</sub>

</details>

**Main problem.**

The difficulty of actively manipulating phonon transport due to the charge-neutral nature of heat carriers and the lack of a unified framework for controlling them via spin-phonon coupling.

**Main result.**

Discovery of two distinct magnetic-field-tunable regimes in thermal conductivity: a high-field regime driven by isotropic magnon-phonon hybridization (magnon polarons) and a low-field regime driven by anisotropic magnon gap softening.

**Method.**

Integration of four-probe longitudinal thermal conductivity measurements with Brillouin light scattering (BLS) and ferromagnetic resonance (FMR) spectroscopy.

**Summary.**

This paper demonstrates a method to control heat transport in a 2D magnetic insulator using magnetic fields. The researchers identified two different ways that spin-phonon coupling affects thermal conductivity: one at high fields through the creation of hybrid magnon-phonon particles, and another at low fields through the rotation of magnetization. This work provides a framework for using magnetic field magnitude and direction as 'knobs' to engineer phonon transport in van der Waals materials.

<details><summary>Detailed structure</summary>

**Model / system.**

The physical system is Cr2Ge2Te6 (CGT), a two-dimensional van der Waals ferromagnetic insulator with strong magnetocrystalline anisotropy.

**Key observables.**

Thermal conductivity (kappa), relative change in thermal conductivity (delta-kappa/kappa0), magnon frequency, and magnetic anisotropy gap.

**Important parameters / regimes.**

Magnetic field magnitude (H), field orientation (theta), temperature (T), and the saturation field (Hs).

**Assumptions / limitations.**

The study assumes the validity of the magnon polaron model for high-field resonance and uses an empirical exponential function to approximate the monotonic background of thermal conductivity.

**Figures summary.**

Fig 1: Measurement setup and temperature/field dependence of kappa showing ballistic, AMTC, and MPH regimes. Fig 2: Evidence of high-field resonance dips and calculated magnon-phonon dispersion relations. Fig 3: Low-field AMTC analysis including angular dependence and BLS spectra. Fig 4: Magnetothermal transport phase diagram and thermal quenching of SPC features.

**Paper structure.**

The paper introduces the challenge of phonon manipulation, presents experimental thermal transport data, identifies two anomalous magnetic field regimes, uses spectroscopic techniques (BLS/FMR) to reveal the microscopic origins (magnon-phonon hybridization and gap softening), and concludes with a phase diagram and implications for phonon engineering.

</details>

<details><summary>Abstract</summary>

The active manipulation of phonon transport remains a central challenge in phononics and spin caloritronics due to the charge-neutral nature of heat carriers. Spin-phonon coupling (SPC) offers a promising route for the dynamic control of heat carriers, yet its progress has been limited due to the lack of a unified framework and suitable material platforms. Here, we report on the magnetic field-tunable phonon transport behavior in the ferromagnetic insulator Cr2Ge2Te6. We observed two distinct anomalous regimes at both the high and low fields that were governed by isotropic magnon-phonon hybridization and an anisotropic magnon softening process, respectively. By integrating detailed transport behavior with Brillouin light scattering and ferromagnetic resonance, we uncovered the microscopic origins of these anomalous regimes and demonstrated that both the field magnitude and orientation could act as versatile tuning knobs to manipulate the thermal conductivity. Our findings provide experimental evidence of the SPC effect on phonon transport, demonstrating the dual impact of SPC within a unified system. This work will not only broaden the fundamental understanding of quasiparticle interactions but also establish a viable framework for dynamic phonon engineering. Furthermore, the characteristics of this system highlight the potential for achieving field-tunable phonon transport in similar platforms such as two-dimensional (2D) magnetic materials.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25436"></a>


### [Highly fluctuating double-$q$ magnetic order in the van der Waals metal CeTe$_3$](http://arxiv.org/abs/2604.25436v1)

**Authors:** Ryutaro Okuma, Yuita Fujisawa, Natsumi Maekawa, Akiko Nakao, Yoshihisa Ishikawa, Riki Kobayashi, Yoshinori Okada, Daichi Ueta

**Type:** both · **Category:** strongly correlated electrons · **PDF:** <https://arxiv.org/pdf/2604.25436v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `Kondo & dissipative impurity` **1/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25436_figures/2604.25436_fig1.jpg" width="500"><br>

<sub>FIG. 1. vdW antiferromagnet CeTe3. (a) Crystal structure, where blue and gold spheres represent Ce and Te atoms, re- spectively. The conducting Te0.5−square nets are stacked along the b axis via vdW coupling and interact with the mag- netic [CeTe]+ layers through Kondo coupling. Crystal struc- ture is drawn by VESTA [17]. (b) Quasi-two-dimensional Fermi surface of CeTe3. The nearly tetragonal slab symme- try gives rise to characteristic nesting vectors along the a∗</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25436_figures/2604.25436_fig2.jpg" width="500"><br>

<sub>FIG. 2. Magnetic order in CeTe3 detected by neutron diffrac- tion. (a) Diffraction patterns in the h5l plane at 0.3 K (left) and 5 K (right). Crossings of the dashed lines indicate the magnetic Bragg peak positions. (b) Diffraction patterns in the h6l plane at 0.3 K (left) and 5 K (right). (c) Tempera- ture dependence of the integrated intensity at (−1, 7, 0)−q+. The transparent red line is a guide to the eye.</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25436_figures/2604.25436_fig3.jpg" width="500"><br>

<sub>FIG. 3. (a,b) Conductance maps near the Fermi level (E −EF = +14 mV) measured (a) above TN1 and (b) below TN2. The set point is -60 mV/200 pA. (c) Schematic of the double-q spin-density-wave (SDW) structure consistent with the neutron and STM experiments, drawn by SpinW[49]. The magnetic moment of the Ce1 site, as defined in Table III, is indicated. (d,e) Corresponding Fourier transform images obtained from (a) and (b), respectively. (f)Charge modulations below TN2 that can be explained by the double-q magnetic structure and CDW order (filled symbols). Experimentally negligible peaks are shown by open symbols. See the main text for the details. Panels (a,b,d,e) are adapted from Ref.[29].</sub>

</details>

**Main problem.**

The study aims to determine the microscopic magnetic structure of the van der Waals metal CeTe3 and understand the interplay between magnetism, c-f hybridization, and charge-density-wave (CDW) instabilities.

**Main result.**

The researchers identified a double-q magnetic order with moments predominantly aligned along the c-axis, where the reduced magnetic moment indicates strong quantum fluctuations driven by c-f hybridization.

**Method.**

The study combines single-crystal neutron diffraction down to 0.3 K with scanning tunneling microscopy (STM) to analyze magnetic Bragg peaks and real-space charge modulations.

**Summary.**

This paper investigates the magnetic ground state of the van der Waals metal CeTe3. Using neutron diffraction and STM, the authors reveal a double-q magnetic order with significantly reduced moments due to quantum fluctuations. They demonstrate that the magnetic structure is intimately linked to the material's itinerant charge degrees of freedom and residual CDW instabilities. This work provides key insights into how magnetism and conduction electrons interact in low-dimensional van der Waals materials.

<details><summary>Detailed structure</summary>

**Model / system.**

The system is CeTe3, a van der Waals antiferromagnet consisting of magnetic [CeTe]+ layers coupled to highly conducting Te0.5- square nets, characterized by a quasi-two-dimensional electronic structure.

**Key observables.**

Magnetic propagation vectors (q_plus and q_minus), magnetic Bragg peaks, ordered magnetic moment, and charge density modulations (FFT peaks).

**Important parameters / regimes.**

Magnetic transition temperatures (TN1 approx 3 K, TN2 approx 1.3 K), propagation vectors q_plus = (0.17, 0, 0.31), and the reduced magnetic moment of approx 0.32 mu_B.

**Assumptions / limitations.**

The magnetic structure refinement was performed using an undistorted Cmcm structure without explicitly including the CDW modulation.

**Figures summary.**

Fig 1 shows the crystal structure, Fermi surface, and neutron diffraction patterns; Fig 2 shows magnetic structure refinement and satellite peaks; Fig 3 presents STM conductance maps and the schematic of the double-q spin-density-wave structure.

**Paper structure.**

The paper introduces the CeTe3 system, presents neutron diffraction data to identify magnetic propagation vectors, uses STM to confirm the double-q nature via charge modulation, and discusses the physical implications of c-f hybridization and CDW coupling.

</details>

<details><summary>Abstract</summary>

CeTe$_3$ is a van der Waals antiferromagnet composed of magnetic [CeTe]$^+$ layers coupled to highly conducting Te$^{0.5-}$ square nets. Its simple quasi-two-dimensional electronic structure and cleavable nature make it an appealing platform for exploring correlated magnetism in reduced dimensions. To clarify the nature of its low-temperature state, we performed single-crystal neutron diffraction down to 0.3 K, complemented by scanning tunneling microscopy. A magnetic transition near 1.5 K gives rise to incommensurate Bragg peaks at $q_{\pm}\sim(\pm0.17,0,0.31)$, consistent with a double-$q$ magnetic order whose moments are predominantly aligned along the $c$ axis. The strongly reduced ordered moment is consistent with enhanced quantum fluctuations driven by $c$-$f$ hybridization, while the deviation of the propagation vectors from simple nesting suggests a coupling to residual charge-density-wave instabilities of the quasi-one-dimensional Te-derived bands. These results indicate that CeTe$_3$ hosts a correlated magnetic ground state where spin and itinerant charge degrees of freedom are intimately linked in the van der Waals limit.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25861"></a>


### [Minimum Toffoli depth for the multi-controlled Toffoli gate via teleportation](http://arxiv.org/abs/2604.25861v1)

**Authors:** Spyros Tserkis, Muhammad Umer, Eleftherios Mastorakis, Dimitris G. Angelakis

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25861v1>

**Analysis basis:** full PDF text, analyzed in chunks

**Topic relevance:** `quantum measurements` **1/5**

<details open><summary>📷 Fig 1</summary>

<img src="2604.25861_figures/2604.25861_fig1.jpg" width="500"><br>

<sub>FIG. 1. Quantum circuit representation of an (n+1)-qubit MCT gate.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25861_figures/2604.25861_fig2.jpg" width="500"><br>

<sub>FIG. 2. In panels (a)-(c) we plot the Toffoli depth, the Toffoli count, and the ancilla count, respectively, against the number of control qubits in an MCT gate decomposition. The color code is the same for all three panels. With blue we have the corresponding values for the decomposition by Khattar and Gidney [17]. With orange the corresponding values for the protocol derived by Dutta et al. [18] that uses one ancilla qubit and with green the corresponding protocol by the same authors that uses two ancilla qubits. With red we have the corresponding values for the teleportation-based protocol proposed in this work. With purple there is a trend appearing only on panel (a) corresponding to...</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25861_figures/2604.25861_fig3.jpg" width="500"><br>

<sub>Fig. 2(c) we compare the additional qubits, also known as ancilla qubits, required for each implementation. A detailed analysis of how our proposed decomposition compares with the rest is deferred to section V.</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25861_figures/2604.25861_fig4.jpg" width="500"><br>

<sub>FIG. 4. An MCT5 gate as a unitary operation (left) and through a teleportation-based decomposition (right).</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25861_figures/2604.25861_fig5.jpg" width="500"><br>

<sub>FIG. 3. Protocol for the teleportation of an MCTn+1 gate based on Ref. [32]. The MCTn+1 gate is teleported using m number of MCTk+1 gates and a single MCTm+ℓ+1 gate. The squiggly lines correspond to Bell states of the form |Φ+⟩= (|00⟩+ |11⟩)/ √</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25861_figures/2604.25861_fig6.jpg" width="500"><br>

<sub>FIG. 5. Teleportation-based decomposition of an MCT8 gate. Toffoli gates applied on closest-neighboring qubits are indicated with a red dashed box. In panel (a) the MCT8 gate is depicted as a unitary operation. Panel (b) depicts the teleportation-based decomposition of the MCT8 gate that includes ten ancilla qubits. The Toffoli depth of this circuit is equal to three due to the measurement outcomes required for the conditional gates. Panel (c) depicts the teleportation-based decomposition of the MCT8 gate with Toffoli depth equal to one after classically conditioned gates have been commuted to the right hand-side of the circuit. In the gray box it is shown how four consecutive gates can be...</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25861_figures/2604.25861_fig7.jpg" width="500"><br>

<sub>FIG. 6. Dutta et al. decomposition of an MCT8 gate [18]. Toffoli gates applied on closest-neighboring qubits are placed within a red dashed box. Panel (a) depicts the MCT8 gate as a unitary operation. In panel (b) the Dutta et al. decomposition [18] of the MCT8 gate is depicted that corresponds to the lower bound (purple line) in Fig. 2(a). This decomposition has a Toffoli-depth equal to three, five ancilla qubits, and only two of the Toffoli gates are applied on closest-neighboring qubits. Panel (d) depicts the corresponding circuit where all Toffoli gates have been replaced by circuit primitives, shown in panel (c), that allow for only closest-neighboring interactions based on Ref. [44].</sub>

</details>

<details><summary>📷 Fig 8</summary>

<img src="2604.25861_figures/2604.25861_fig8.jpg" width="500"><br>

<sub>FIG. 7. Panels (a) and (b) depict side by side the upper bound of process fidelity of the Dutta et al. decomposition and the teleportation-based decomposition, respectively. Both are plotted against the Toffoli error rate and the entanglement error rate that range from 10−3 to 10−1. Panel (c) depicts a value called ∆process fidelity, corresponding to the subtraction of the fidelity found for the teleportation-based decomposition from the Dutta et al. decomposition. Red is the region where the Dutta et al. decomposition is preferable and blue the region where the teleportation-based decomposition is preferable. Analogously panels (d) and (e) depicts to the lower bound of the process fidelity...</sub>

</details>

<details><summary>📷 Fig 9</summary>

<img src="2604.25861_figures/2604.25861_fig9.jpg" width="500"><br>

<sub>FIG. 8. Panel (a) depicts the MCT-based construction of the adder operator modulo 24. Panel (b) depicts an analogous construction but substitutes the MCT4 gate with the teleportation-based decomposi- tion according to the protocol discussed in section V. Panel (c) de- picts the adder operator modulo 24 based on Vedral et al. [1].</sub>

</details>

<details><summary>📷 Fig 10</summary>

<img src="2604.25861_figures/2604.25861_fig10.jpg" width="500"><br>

<sub>FIG. 9. The Toffoli depth of the adder operator is plotted for three different decompositions against the total number of register qubits. The decomposition of the adder operator through the teleportation- based decomposition developed in this work is the optimal overall in terms of minimizing Toffoli depth.</sub>

</details>

**Main problem.**

The decomposition of multi-controlled Toffoli (MCT) gates into simpler gates typically results in high circuit depth, which increases susceptibility to decoherence.

**Main result.**

The authors introduce a teleportation-based decomposition that achieves a unit Toffoli depth, independent of the number of controls, while maintaining a relatively low Toffoli count.

**Method.**

A recursive gate teleportation protocol that uses ancilla qubits and Bell states to decompose an (n+1)-qubit MCT gate into smaller MCT gates and measurements.

**Summary.**

This paper presents a new method for decomposing multi-controlled Toffoli gates using quantum teleportation. The proposed technique achieves a constant Toffoli depth that does not increase with the number of control qubits. While it requires a linear increase in ancilla qubits, it offers significant advantages for circuit depth and error resilience in specific noise regimes. The authors demonstrate the utility of this method in optimizing quantum adders, QROM, and quantum machine learning architectures.

<details><summary>Detailed structure</summary>

**Model / system.**

General quantum computing circuits and architectures, specifically focusing on the implementation of MCT gates, quantum adders, QROM, and quantum machine learning primitives.

**Key observables.**

Toffoli depth, Toffoli count, ancilla qubit count, and process fidelity.

**Important parameters / regimes.**

Number of control qubits (n), Toffoli error probability, and entanglement error probability.

**Assumptions / limitations.**

The protocol assumes the ability to distribute entangled pairs across non-neighboring (distant) qubits and assumes a hierarchical error scaling between different gate types.

**Figures summary.**

Figure 1 shows the MCT gate circuit; Figure 2 compares depth, count, and ancilla scaling against existing methods; Figure 3 illustrates the teleportation protocol; Figure 4 and 5 show specific gate decompositions (MCT5, MCT8); Figure 7 shows process fidelity bounds and differences; Figure 8 and 9 compare adder constructions; Figure 10 shows QROM and QML applications.

**Paper structure.**

The paper introduces the problem of MCT decomposition, presents a new teleportation-based protocol, provides a comparative analysis of gate metrics (depth, count, ancilla), evaluates noise resilience via fidelity simulations, and demonstrates practical applications in quantum adders, QROM, and quantum machine learning.

</details>

<details><summary>Abstract</summary>

The decomposition of complex quantum operations into experimentally feasible gate sets has been a central challenge since the early development of quantum computing. The multi-controlled Toffoli (MCT) gate is a key example, with applications across a wide range of quantum algorithms, whose decomposition into smaller gates, however, typically leads to deep circuits. In this work, we introduce a teleportation-based decomposition that implements an arbitrary MCT gate with unit Toffoli depth, independent of the number of controls, while maintaining a relatively low Toffoli count compared to existing approaches. This is achieved at the cost of a linear overhead in ancilla qubits and the ability to distribute entangled pairs across distant qubits, a capability already available in several quantum computing platforms. We further demonstrate the advantages of this implementation in circuits that rely on MCT gates, such as the adder operator, quantum read-only memory, quantum neurons, and quantum decision trees.

</details>

<sub>[↑ back to top](#top)</sub>


## Other papers (49)

*Papers from primary archives without highlighted authors or any topic match. Click to expand.*

<details><summary>Show other papers</summary>


<a id="paper-2604.25424"></a>


### [A graph-aware bounded distance decoder for all stabilizer codes](http://arxiv.org/abs/2604.25424v1)

**Authors:** Harikrishnan K J, Amit Kumar Pal

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25424v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25424_figures/2604.25424_fig1.jpg" width="500"><br>

<sub>FIG. 1. (a) The equivalent graph associated with the [[5, 1, 3]] perfect code. See Appendix. B for the stabilizers and a detailed discussion. White node indicate the Hadamard in the Hr. A demonstration of resulting graph syndromes in the case of (b) σz 4 and (c) σx 5 errors where the blue nodes indicates the non-trivial graph generators of α. The corresponding feedforward network corresponding to the minimum weight scenarios (b) σz 4 error where β = 1001, ˜β = 0 and (d) σx 5 error where β = 0011, ˜β = 1.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25424_figures/2604.25424_fig2.jpg" width="500"><br>

<sub>FIG. 2. A demonstration of feedforward network structure of a graph. The graph syndrome nodes (shown in blue) and their neighbors belong to the left most layer L1. Any later layer contains neighbors of preceding layer as well as their neighbors (See Sec. III B). Nodes after Lw[α] can be discarded by virtue of Eq. (40).</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25424_figures/2604.25424_fig3.jpg" width="500"><br>

<sub>FIG. 3. Log-log plot of logical error rate pL against the phys- ical error rate p in the case of optimal codes under depolariza- tion noise corrected with BDD (see Sec. III C and Appendix. C for code details). Errors are sampled according to Eq. (43) with px = py = pz = p/3. Each of the datapoints correspond to 104</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25424_figures/2604.25424_fig4.jpg" width="500"><br>

<sub>FIG. 4. (a) The equivalent bipartite graph associated with smallest [[7, 1, 3]] CSS code. The white nodes indicates Hadamard operations. See Appendix. D for the stabilizers and a detailed discussion. A demonstration of graph syndrome and the corresponding feedforward network corresponding to the trivial logical syndrome in the case of (c) σz 1 (d) σx 1 error.</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25424_figures/2604.25424_fig5.jpg" width="500"><br>

<sub>FIG. 5. Schematics of d = 3, k = 1 (a) triangular color and (b) rotated surface codes with N = 7 and N = 9 physical qubits respectively. The thick pick and green lines represent the logical z and x operators respectively. The log-log plot of pL against p for code distances three to nine of (c) triangular color (d) rotated surface codes. Both of them are under bit flip channel corresponding to py = pz = 0 of Eq. (43). The vertical black dotted line indicates the theoretical known optimal threshold noise strengths popt c = 0.109(2)[78] (popt c = 0.1094(2)[79]) of color (surface) code. The inset shows the data collapse (Eq. (53)) obtained near the BDD threshold physical error probability pc...</sub>

</details>

**Main problem.**

The difficulty of developing efficient, generalized decoding strategies for all stabilizer codes, particularly non-CSS codes, where standard methods like Belief Propagation often fail or are computationally prohibitive.

**Main result.**

The development of a graph-aware Bounded Distance Decoder (BDD) that achieves near-optimal performance for CSS codes and satisfactory performance for non-CSS codes up to distance d=11, accompanied by the QGDecoder open-source library.

**Method.**

The authors leverage the local Clifford equivalence between stabilizer codes and graph states, using a graph-based framework with strategic pruning (via a feed-forward network structure) and structured sampling to reduce the search space.

**Summary.**

This paper presents a new decoding strategy called Graph-Aware Bounded Distance Decoding that works for any stabilizer code by mapping them to graph states. By using graph pruning and structured sampling, the authors significantly reduce the computational complexity of finding the most likely error. The method shows high efficiency for both CSS and non-CSS codes and provides a new open-source tool, QGDecoder, for the quantum error correction community.

<details><summary>Detailed structure</summary>

**Model / system.**

The study focuses on quantum stabilizer codes, including both CSS (surface and color codes) and non-CSS families, subjected to depolarizing and bit-flip error models.

**Key observables.**

Logical error rate (pL), threshold error probability (pc), and critical exponent (nu).

**Important parameters / regimes.**

Code distance (d), physical error rate (p), target weight threshold (T), and number of physical (N) and logical (k) qubits.

**Assumptions / limitations.**

The decoder assumes perfect syndrome measurement and focuses on specific error models like depolarizing and bit-flip noise.

**Figures summary.**

Figure 1 shows the graph representation of the [[5,1,3]] code; Figure 2 illustrates the feed-forward network structure for graph pruning; Figure 3 displays logical error rate vs. physical error rate for non-CSS codes; Figure 4 shows the bipartite graph syndrome for CSS codes; Figure 5 shows code schematics and data collapse plots for threshold estimation.

**Paper structure.**

The paper introduces the decoding bottleneck, establishes the mathematical mapping between stabilizer codes and graph states, proposes the graph-aware BDD algorithm with pruning techniques, demonstrates performance on non-CSS and CSS codes, performs finite-size scaling analysis for thresholds, and introduces the QGDecoder software.

</details>

<details><summary>Abstract</summary>

We formulate a bounded distance decoding strategy applicable to all stabilizer codes including both CSS and non-CSS code-families. The framework emerges out of the local Clifford equivalence between arbitrary stabilizer states and graph states. Using the graphical representation of the stabilizers and the syndromes, we constitute the bounded distance decoding as an adaptable generalization of maximum likelihood decoding, ensuring correction of all errors with weights upper bounded by a target weight. We show that strategic pruning associated with a feed-forward network structure of the graph can reduce the search space and subsequently the runtime of the designed decoder. We demonstrate satisfactory performance of the bounded distance decoder in the case of the optimal non-CSS codes up to distance $d=11$ subjected to the depolarizing error on all qubits, and near-optimal decoding for the color and the surface codes, both belonging to the CSS family, under the bit-flip errors on the qubits. We also develop an open-source library, QGDecoder, enabling the graph-aware bounded distance decoding of arbitrary stabilizer codes.

</details>

<sub>[↑ back to top](#top)</sub>


<a id="paper-2604.25825"></a>


### [A Quantum Spectral Framework for Solving PDEs](http://arxiv.org/abs/2604.25825v1)

**Authors:** Chih-Kang Huang, Giacomo Antonioli, Frédéric Barbaresco

**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2604.25825v1>

**Analysis basis:** full PDF text, analyzed in chunks

<details open><summary>📷 Fig 1</summary>

<img src="2604.25825_figures/2604.25825_fig1.jpg" width="500"><br>

<sub>Figure 4. Quantum circuit for solving the 2D Poisson equation on a 16 × 16 grid using 9 qubits. The circuit consists of a the QFT⊗2, followed by the block encoding of the diagonal filter corresponding to the inverse Laplacian, and concludes with an inverse QFT⊗2 to return to the spatial domain.</sub>

</details>

<details><summary>📷 Fig 2</summary>

<img src="2604.25825_figures/2604.25825_fig2.jpg" width="500"><br>

<sub>Figure 5. Visualizations of the reference, classical, and quantum solutions, along with the absolute errors of the classical and quantum methods relative to the reference for the 2D elliptic case with N = 64 and A =diag(10, 1).</sub>

</details>

<details><summary>📷 Fig 3</summary>

<img src="2604.25825_figures/2604.25825_fig3.jpg" width="500"><br>

<sub>Figure 6. Visualizations of the reference, classical, and quantum solutions, along with the absolute errors of the classical and quantum methods relative to the reference for the 3D elliptic case with N = 16 and A =diag(10, 1, 1).</sub>

</details>

<details><summary>📷 Fig 4</summary>

<img src="2604.25825_figures/2604.25825_fig4.jpg" width="500"><br>

<sub>Figure 7. Visualizations of the reference, classical, and quantum solutions, along with the absolute errors of the classical and quantum methods relative to the reference for the 2D Helmholtz equation with N = 64, k = 2π × 0.5 (Left) and k = 2π × 0.1 (Right).</sub>

</details>

<details><summary>📷 Fig 5</summary>

<img src="2604.25825_figures/2604.25825_fig5.jpg" width="500"><br>

<sub>Figure 8. Visualizations of the reference, classical, and quantum solutions, along with the absolute errors of the classical and quantum methods relative to the reference for the 2D diffusion case with N = 64 and A =diag(10, 1).</sub>

</details>

<details><summary>📷 Fig 6</summary>

<img src="2604.25825_figures/2604.25825_fig6.jpg" width="500"><br>

<sub>Figure 9. Visualizations of the reference, classical, and quantum solutions, along with the absolute errors of the classical and quantum methods relative to reference for the 3D diffusion case with N = 16 and A =diag(1,100, 1).</sub>

</details>

<details><summary>📷 Fig 7</summary>

<img src="2604.25825_figures/2604.25825_fig7.jpg" width="500"><br>

<sub>Figure 10. Evolutions and dissipations of the energy 15 for the diffusion case with (Left) d = 2, N = 64 and A=diag(100, 1); (Right) d = 3, N = 16 and A=diag(1, 100, 1) for the Reference, Classical and Quantum methods. We track log(E(u)−E∞) where E∞is the energy of the steady-state solution, since E can become negative during evolution.</sub>

</details>

**Main problem.**

Addressing the curse of dimensionality in solving Partial Differential Equations (PDEs) by developing a quantum algorithmic alternative to standard matrix inversion methods.

**Main result.**

The authors present a quantum spectral framework that achieves polylogarithmic gate complexity and demonstrates numerical accuracy comparable to classical FFT-based spectral solvers.

**Method.**

The framework utilizes the Quantum Fourier Transform (QFT) combined with Quantum Block Encoding (QBE) and quantum reversible arithmetic to implement an inverse spectral filter.

**Summary.**

This paper introduces a specialized quantum subroutine for solving linear PDEs by exploiting the diagonal structure of differential operators in the Fourier domain. By using Quantum Block Encoding and reversible arithmetic, the authors bypass the high complexity of generic matrix encoding methods. The framework is validated against classical spectral methods for Poisson, Helmholtz, and diffusion equations. This approach offers a path toward efficient quantum simulation of complex physical systems in high dimensions.

<details><summary>Detailed structure</summary>

**Model / system.**

The mathematical models include second-order linear elliptic (Poisson, Helmholtz) and parabolic (anisotropic diffusion) PDEs on a d-dimensional flat torus.

**Key observables.**

Relative L2-errors, energy functional E(u) for dissipation tracking, and error distributions.

**Important parameters / regimes.**

Dimensionality (d), grid size (N), condition number (kappa), and precision (epsilon).

**Assumptions / limitations.**

Periodic boundary conditions, constant coefficients, and a noiseless quantum computing setting with efficient state preparation.

**Figures summary.**

The figures illustrate quantum circuit sequences for controlled rotations and block encoding, the d-dimensional QFT, and visual comparisons of quantum vs. classical solution distributions and energy dissipation trajectories.

**Paper structure.**

The paper progresses from defining the limitations of classical PDE solvers to proposing a quantum spectral framework, detailing the block encoding and arithmetic implementation, providing complexity analysis, and concluding with numerical validation via Qiskit simulations.

</details>

<details><summary>Abstract</summary>

Partial differential equations (PDEs) are fundamental across numerous scientific fields. As these problems scale to high dimensions, classical numerical schemes introduce severe computational bottlenecks, known as the curse of dimensionality. Attempts to solve this problem typically rely on either classical sparsity and low-rank decompositions, or neural network surrogate models. On the other hand, Quantum Computing offers a promising alternative, as it allows us to operate in significantly larger spaces while demanding far fewer resources. In this work, we present a quantum subroutine to solve second-order linear PDEs by exploiting the structural properties of the filter in Fourier space using Quantum Block Encoding (QBE) with quantum reversible arithmetic. This approach serves as a specialized alternative to standard quantum matrix inversion, which typically relies solely on Quantum Singular Value Transformation (QSVT) without exploiting the inherent structural properties of the matrix. We validate the proposed methodology against its classical counterpart to prove its correctness. This framework provides a foundation for extending these methods toward quantum group Fourier transforms, wavelet-based analysis, and equivariant quantum neural networks (EQNNs), offering a promising path toward solving broader classes of problems, including nonlinear PDEs.

</details>

<sub>[↑ back to top](#top)</sub>
