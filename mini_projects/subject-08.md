# Subject 8 – Quantum Random Number Generator with Custom Measurements
 
**Difficulty:** 3/5
 
## Introduction
 
Quantum mechanics allows for the generation of "truly" random numbers, unlike classical pseudo-random algorithms which are ultimately deterministic. The idea of this project is to build a quantum random number generator (QRNG) using MPQP, leveraging the intrinsic uncertainty of quantum measurements.
 
A key aspect of this project is to explore different types of quantum measurements to extract randomness, not just in the standard computational basis, but also in arbitrary bases and via expectation values of randomly chosen observables.
 
## Goal of the project
 
The first goal is to understand and explain how quantum measurements produce randomness, and under what assumptions the output can be considered truly unpredictable.
 
The second goal is to implement a QRNG using MPQP, incorporating at least the following features:
- Use the tools provided in `mpqp.tools.circuit` to generate random circuits
- Perform a `BasisMeasure` of the quantum state in a custom (random) basis (using `Basis`)
- Perform an `ExpectationMeasure` with random Hermitian observables, to generate real-valued outputs.
 
Each type of measurement should be encapsulated in a different generator module (or class), allowing for easy benchmarking and comparison. For instance, the basis measurement can be used to generate and random probability distribution, and the expectation measurements can be post-processed to generate a series of random classical bits.
 
The third goal is to evaluate the randomness quality of each method. You will write basic statistical tests (e.g. frequency test, run test) to compare the distribution of the outputs, and discuss the impact of the measurement strategy on randomness.
 
## Resources
- https://en.wikipedia.org/wiki/Quantum_random_number_generator  
- https://en.wikipedia.org/wiki/Born_rule  
- MPQP documentation on `Basis`, `BasisMeasure`, `ExpectationMeasure`
- Optional: NIST randomness test suite (for bonus analysis)
 
## Expected deliverables
 
- A report summarizing:
  - The principles of quantum randomness
  - How different measurement types affect the output
  - Your implementation strategy and results of statistical tests
 
- A codebase, using MPQP, including:
  - At least two random number generators: one using custom basis measurements, one using expectation values of random observables.
  - A `main` function to generate and output random bitstrings (and optionally compare them).