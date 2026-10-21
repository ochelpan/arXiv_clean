<a id="top"></a>
# Weizmann papers — 2026-10-21

*1 papers with Weizmann affiliations*

<a href="report.html">← Back to main digest</a>

<a id="paper-2610.25518"></a>
### [Randomness Certification from Statistically Hiding Commitments](http://arxiv.org/abs/2610.25518v1)

**Authors:** Ilya Merkulov, Rotem Arnon  
**Type:** theory · **Category:** quantum information and computing · **PDF:** <https://arxiv.org/pdf/2610.25518v1>  
**Analysis basis:** full PDF text, analyzed in chunks
**Topic relevance:** `quantum measurements` **2/5**

<div class="figure-strip-hint">↔ Scroll figures horizontally</div>
<div class="paper-figures-scroll">
<figure class="paper-figure-card">
<img src="2610.25518_figures/2610.25518_fig1.jpg" alt="Figure 1">
<figcaption class="paper-figure-caption"><b>Fig 1.</b> Figure 1: The hidden virtual input is the computational analogue of a Bell measurement setting. Classical hiding excludes efficient classical strategies and yields a PoQ, whereas quantum hiding also protects against the prover’s residual quantum state and enables randomness certification. Our main technical contribution is to establish this stronger guarantee for a commitment-based proof-of-qubit protocol.</figcaption>
</figure>
</div>

**Summary.** This paper develops a protocol to certify genuine randomness from an untrusted quantum device by leveraging cryptographic assumptions. It shows that this requires a stronger security notion, 'quantum virtual-input hiding,' compared to what is needed just to prove the device is quantum. The result provides a path to randomness certification using post-quantum commitment schemes.

**Why it may be interesting.** While focused on cryptography, the core concept of certifying genuine randomness from physical processes (like quantum measurements) is fundamental to quantum information theory and device characterization, which has implications for quantum hardware validation.

<details markdown="1"><summary>Detailed structure</summary>

**Main problem.** The paper addresses randomness certification: guaranteeing that the output of an untrusted quantum device is genuinely random and unpredictable even when the adversary possesses quantum side information.

**Main result.** The authors establish that randomness certification can be achieved using post-quantum statistically hiding bit commitments, requiring only statistical hiding and ordinary computational binding against quantum polynomial-time senders.

**Method.** The work builds upon the framework of Computational Bell Inequalities, distinguishing between classical and quantum virtual-input hiding to upgrade a proof-of-quantumness protocol to a randomness-certification protocol.

**Model / system.** The setting involves a classical verifier interacting with a single, untrusted quantum device. The analysis uses cryptographic primitives like commitment schemes and draws analogies to physical Bell tests via computational analogues.

**Key observables.** Conditional von Neumann entropy, Bell correlation (CHSH tuple), and the success of the commitment opening procedure.

**Important parameters / regimes.** The security relies on the existence of post-quantum statistically hiding bit commitments and the computational power of quantum polynomial-time (QPT) senders.

**Assumptions / limitations.** The protocol assumes the existence of post-quantum statistically hiding bit commitments satisfying computational binding against QPT senders, which is shown to be weaker than stronger notions like sum-binding.

**Figures summary.** Figure 1 illustrates the computational analogue of a Bell measurement setting, showing that classical hiding suffices for Proofs of Quantumness (PoQ), while quantum hiding is necessary for randomness certification.

**Paper structure.** The paper progresses by first establishing the necessity of quantum virtual-input hiding over classical hiding, then providing the main technical contribution by proving this hiding property for a commitment-based protocol, and finally instantiating the construction using specific functions (TCFs) or models (QROM).

</details>

<details markdown="1"><summary>Abstract</summary>

Randomness certification aims to guarantee that the output of an untrusted quantum device contains genuine randomness that remains unpredictable even given quantum side information held by an adversary. For a classical verifier interacting with a single quantum device, such a guarantee cannot rely on the physical separation underlying standard Bell tests and must instead follow from computational restrictions on the prover. Building on the framework of Computational Bell Inequalities, we distinguish classical and quantum virtual-input hiding, showing that the former suffices for proofs of quantumness, whereas the latter enables randomness certification against quantum side information.   Our main technical contribution is to establish quantum virtual-input hiding for a commitment-based protocol derived from the proof of quantumness from one-way-functions by Morimae and Yamakawa. We show that statistical hiding together with ordinary computational binding against quantum polynomial-time senders suffices, without requiring stronger quantum binding notions such as sum-binding or collapse-binding. This yields a randomness-certification protocol from post-quantum statistically hiding bit commitments. In particular, existing constructions of such commitments from post-quantum one-way permutations imply that post-quantum one-way permutations suffice for randomness certification.   We further instantiate our construction using quantum-secure trapdoor claw-free functions, obtaining an efficient classical verifier, and in the quantum random oracle model, obtaining randomness certification without additional computational assumptions but with an inefficient verifier. These instantiations separate the cryptographic properties sufficient for randomness certification from the additional structure required for efficient verification within our commitment-based framework.

</details>

<sub>[↑ back to top](#top)</sub>

<a href="report.html">← Back to main digest</a>