\# Methodology



\## Objectiv# Methodology



\## Objective

The objective of this project is to implement a complete \*\*single-qubit Quantum State Tomography (QST) pipeline\*\* using simulated quantum measurements. The goal is to reconstruct an unknown quantum state from measurement outcomes and validate the reconstruction using quantitative metrics.



---



\## Quantum States Considered

We study the following single-qubit pure states:



\- Computational basis: |0⟩ , |1⟩  

\- Superposition states: |+⟩ , |−⟩  

\- Phase-offset state: (|0⟩ + i|1⟩)/√2  



Each state is represented as a ket vector and converted into a density matrix:

\\\[

\\rho = |\\psi\\rangle \\langle\\psi|

\\]



---



\## Measurement Framework



\### Pauli Measurements

Quantum measurements are performed in the three Pauli bases:



\- \*\*Z basis\*\*: |0⟩⟨0| , |1⟩⟨1|

\- \*\*X basis\*\*: |+⟩⟨+| , |−⟩⟨−|

\- \*\*Y basis\*\*: |+i⟩⟨+i| , |−i⟩⟨−i|



Each measurement basis is defined using projector operators that satisfy:

\\\[

P\_0 + P\_1 = I

\\]



Completeness is verified numerically.



---



\## Measurement Simulation



\### Born Rule

For a given density matrix ρ and projector P, the probability of an outcome is computed using the Born rule:

\\\[

p = \\text{Tr}(P \\rho)

\\]



\### Finite-Shot Sampling

To simulate realistic experiments, measurements are sampled using a finite number of shots (default: 2000). Multinomial sampling is used to generate outcome counts based on theoretical probabilities.



---



\## Expectation Value Estimation

From the sampled measurement counts, expectation values for each Pauli observable are computed as:

\\\[

\\langle \\sigma \\rangle = \\frac{N\_0 - N\_1}{N\_0 + N\_1}

\\]

where \\(N\_0\\) and \\(N\_1\\) are measurement counts for the two outcomes.



---



\## Density Matrix Reconstruction

The single-qubit density matrix is reconstructed using the Pauli expansion:

\\\[

\\rho\_{\\text{reconstructed}} =

\\frac{1}{2} \\left(

I + \\langle X \\rangle X + \\langle Y \\rangle Y + \\langle Z \\rangle Z

\\right)

\\]



This guarantees a Hermitian, trace-one matrix.



---



\## Validation Metrics



\### Fidelity

Fidelity between the true state \\( \\rho \\) and reconstructed state \\( \\hat{\\rho} \\) is computed as:

\\\[

F = \\langle \\psi | \\hat{\\rho} | \\psi \\rangle

\\]

for pure states. Fidelity values close to 1 indicate accurate reconstruction.



---



\### Trace Distance

Trace distance quantifies distinguishability between two quantum states:

\\\[

D(\\rho, \\hat{\\rho}) = \\frac{1}{2} \\| \\rho - \\hat{\\rho} \\|\_1

\\]

where the trace norm is computed via singular values.



---



\## Visualization

Reconstructed density matrices are visualized using 3D histograms:

\- Bar height represents magnitude |ρᵢⱼ|

\- Color represents the complex phase

\- Implemented using Plotly for interactive inspection



---



\## Summary

This methodology demonstrates a full quantum tomography workflow:

1\. State preparation

2\. Measurement simulation

3\. Expectation value estimation

4\. Density matrix reconstruction

5\. Quantitative validation and visualization



The pipeline provides a foundational framework for extending to multi-qubit tomography and machine-learning-based quantum state estimation.



