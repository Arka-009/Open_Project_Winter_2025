# Quantum Measurement Dataset Foundations
Week 1 – Quantum State Tomography

## Overview
This repository contains my Week 1 submission for the Quantum Measurement Dataset
Foundations assignment.

The project implements a complete single-qubit Quantum State Tomography (QST)
pipeline using simulated Pauli measurements. The workflow starts from measurement
theory and ends with validated density matrix reconstruction.

The repository is organized according to the required submission format.
https://colab.research.google.com/github/Arka-009/Open_Project_Winter_2025/blob/main/week1_quantum_topography.ipynb
---

## Repository Structure
.
├── src/
│   └── tomography.py
│
├── notebooks/
│   └── week1_quantum_topography.ipynb
│
├── docs/
│   ├── README.md
│   └── methodology.md
│
├── README.md
├── LICENSE
|---single_qubit_results.zip
|---requirements.txt

---

## Features Implemented
- Pauli measurement operators (X, Y, Z)
- Born-rule probability computation
- Shot-based measurement sampling
- Density matrix reconstruction
- Fidelity and trace distance validation
- 3D density matrix visualization (magnitude + phase)

---

## Quantum States Reconstructed
- |0⟩ , |1⟩
- |+⟩ , |−⟩
- (|0⟩ + i|1⟩) / √2

---

## Tools Used
- PennyLane
- NumPy
- SciPy
- Plotly
- Jupyter Notebook

---

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Open the notebook:
   jupyter notebook notebooks/week1_quantum_topography.ipynb

3. Run all cells top to bottom.

---

## Notes
- Core tomography logic is implemented in src/tomography.py
- The notebook demonstrates the full workflow and validation
- Detailed theory and methodology are documented in docs/

---

## Author
Arkaprava Biswas


---

## License
This project is licensed under the included LICENSE file.
