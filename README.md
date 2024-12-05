# pCUT Code: Perturbative Continuous Unitary Transformation for Quantum Lattice Models

This repository contains the implementation of the **perturbative Continuous Unitary Transformation (pCUT)** method, combining C++ and Python tools to study quantum lattice models. The pCUT framework transforms many-body Hamiltonians into effective quasi-particle Hamiltonians, enabling efficient computation of physical observables. The Python scripts included here simplify generating coefficients for specific models.

---

## Features

- **pCUT Framework in python:** Perform high-order perturbative expansions of quantum Hamiltonians.
- **Python Coefficient Generator:** Simplifies coefficient generation for specific models, like Ising or Heisenberg.
- **Lattice Model Support:** Applicable to transverse field Ising, SU(2), and custom lattice systems.
- **Customizable Orders:** Compute effective Hamiltonians up to user-defined expansion orders.
- **Observables Calculation:** Derive excitation spectra and analyze energy gaps.

---

## Getting Started

### **Prerequisites**

Ensure you have the following installed:


- **Python 3.7+** with libraries:
  - **NumPy**
  - **SymPy** (for symbolic calculations)

Install Python dependencies with:

```bash
pip install numpy sympy
