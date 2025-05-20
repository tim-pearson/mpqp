# Subject 9 - BB84 Quantum Key Distribution Protocol
 
Difficulty: 3/5
 
## Introduction
 
The BB84 protocol, introduced by Charles Bennett and Gilles Brassard in 1984, is the first quantum cryptographic protocol. It allows two parties—traditionally called Alice and Bob—to establish a shared secret key using the principles of quantum mechanics. The key idea is that any eavesdropping attempt by a third party (Eve) can be detected due to the no-cloning theorem and the disturbance measurement causes on quantum states.
 
BB84 represents a foundational milestone in quantum information theory and is widely regarded as a starting point for the study of quantum cryptography.
 
## Goals of the project
 
The first goal is to study and understand the BB84 protocol in detail, including how quantum mechanics ensures the security of the key distribution.
 
The second goal is to implement the protocol using MPQP. This includes:
- Alice preparing and sending a sequence of qubits encoded in randomly chosen bases.
- Bob measuring the received qubits using his own randomly chosen bases.
- A classical post-processing phase in which Alice and Bob communicate (classically) to determine the subset of bits to be used for the final key.
 
The third goal is to simulate the presence of an eavesdropper (Eve) who intercepts and measures qubits in transit. Students will analyze how Eve's interference affects the quantum bit error rate and assess how Alice and Bob can detect her presence.
 
## Resources
 
- https://en.wikipedia.org/wiki/BB84
- https://www.youtube.com/watch?v=2kdRuqvIaww
- Nielsen & Chuang, Quantum Computation and Quantum Information (Chapter 12)
 
 
## Expected deliverables
 
A report explaining the BB84 protocol, including how it allows for secure key distribution and why any attempt to eavesdrop is detectable.
 
A working implementation in MPQP simulating Alice, Bob, and optionally Eve. The code should include:
- Random bit and basis generation.
- Qubit preparation and measurement.
- Key reconciliation and error checking.
 
A main function that demonstrates the full execution of the protocol with and without an eavesdropper.