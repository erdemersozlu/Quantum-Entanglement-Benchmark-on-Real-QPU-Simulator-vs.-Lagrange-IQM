Certainly! Here is the professionally translated English version of your README. This is perfect for a global audience and will look great on your GitHub profile.

---

# 🌀 Quantum Entanglement: Real Hardware Performance vs. Ideal Simulation

This project implements the fundamental "Hello World" of quantum computing: the **Bell State (Entanglement)**. It features a comparative analysis between an ideal mathematical simulation and a real-world quantum processor (**IQM Spark - Lagrange**).

## 🚀 Project Overview
The core objective of this study is to observe and analyze the differences between theoretical perfection (simulation) and physical reality (hardware). The project explores the concepts of **Quantum Noise** and **Statistical Variance**. Hardware access was provided through the collaboration between **Links Foundation** and **Politecnico di Torino** via the IQM Spark platform.



## 🔬 Quantum Circuit: The $|\Phi^+\rangle$ Bell State
The circuit is designed to create a maximally entangled state between two qubits, represented mathematically as:
$$|\Phi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)$$

* **Hadamard (H) Gate:** Puts the first qubit into a state of superposition.
* **CNOT Gate:** Creates a controlled interaction between the two qubits to generate entanglement.
* **Measurement:** Collapses the quantum state into classical bits (0 or 1).

---

## 📊 Experimental Results (1024 Shots)

The following data showcases the transition from the "perfect" world of simulation to the "noisy" reality of current quantum hardware.

### 1. Real Hardware Data (IQM Lagrange)
| Output State | Count | Percentage (%) | Analysis |
| :--- | :--- | :--- | :--- |
| **00** | **480** | 46.8% | Successful Entanglement |
| **11** | **494** | 48.2% | Successful Entanglement |
| **01** | **30** | 2.9% | **Quantum Noise** |
| **10** | **20** | 1.9% | **Quantum Noise** |

### 2. Ideal Simulation Data (AerSimulator)
* **00:** 536
* **11:** 488

---

## 🧐 Deep Dive & Analysis

### 💡 Understanding Quantum Noise
The appearance of `01` and `10` states in the hardware results is theoretically impossible in an ideal circuit. These results are evidence of the **NISQ** (Noisy Intermediate-Scale Quantum) era limitations:
* **Decoherence:** The loss of quantum information due to environmental interaction.
* **Readout Errors:** Physical limitations during the measurement process where a 0 is misidentified as a 1 (or vice versa).
* **Gate Infidelity:** Microscopic inaccuracies during the application of H and CNOT gates.

### 💡 Statistical Variance (Why not exactly 512-512?)
The simulation results (`536` vs `488`) are not errors, but a **statistical necessity**. Quantum measurement is probabilistic.
Much like flipping a fair coin 1024 times, it is statistically unlikely to get exactly 512 heads and 512 tails. The results fluctuate around the 50% mean. According to the **Law of Large Numbers**, as the number of samples (shots) increases, the distribution will converge closer to the theoretical 50/50 split.



---

## ⚙️ Setup and Security

### Installation
Ensure you have the necessary libraries installed:
```bash
pip install qiskit qiskit-aer iqm-client matplotlib
```

### Security (Token Management)
This project uses a `tokens.json` structure to keep API keys secure.
1. Create a `tokens.json` file in the root directory.
2. Add the file to your `.gitignore` to prevent it from being pushed to GitHub.

---

## 📄 License
This project is licensed under the **MIT License**.

---
