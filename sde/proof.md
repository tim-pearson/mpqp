# Limitation: Why I Cannot Transmit More Than 2 Classical Bits by Sending One Qubit

## 1. Recap Superdense Coding

- Superdense coding is a simple but surprising application illustrating quantum mechanics ideas.
- Alice and Bob, far apart, want to exchange information.
- Goal: Alice transmits two classical bits (00, 01, 10, or 11) to Bob by sending only one qubit.
- Alice and Bob share an entangled state:
$$
|\psi\rangle = \frac{|0_A\rangle \otimes |0_B\rangle + |1_A\rangle \otimes |1_B\rangle}{\sqrt{2}} = \frac{|0_A 0_B\rangle + |1_A 1_B\rangle}{\sqrt{2}} = \frac{|00\rangle + |11\rangle}{\sqrt{2}}
$$

- Alice's procedure:
  - Send '00': Alice does nothing.
  - Send '01': Alice applies the Z operator to her qubit.
  - Send '10': Alice applies the X operator to her qubit.
  - Send '11': Alice applies $iY$ to her qubit.

- Quantum states associated with each classical bit:
$$00 -> |\psi_1\rangle = (I \otimes I)|\psi\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$
$$01-> |\psi_2\rangle = (Z \otimes I)|\psi\rangle = \frac{|00\rangle - |11\rangle}{\sqrt{2}}$$
$$10-> |\psi_3\rangle = (X \otimes I)|\psi\rangle = \frac{|10\rangle + |01\rangle}{\sqrt{2}}$$
$$11-> |\psi_4\rangle = (iY \otimes I)|\psi\rangle = \frac{|01\rangle - |10\rangle}{\sqrt{2}}$$
- These four states are the **Bell basis** or **EPR pairs**.
- Bell states form an orthonormal basis.
- Alice sends her qubit to Bob.
- Bob measures in the Bell basis to determine the two-bit string Alice sent.
- Alice, by interacting with a single qubit, transmits two bits of information.

---

## Why Not More Than 2 Bits?

*Dimension of the Hilbert space**  
   The total state space of two qubits is $4$-dimensional.
   The maximum number of **perfectly distinguishable** orthogonal 
   states is exactly $4$.  
   Since classical information is encoded in orthogonal quantum 
   states for perfect distinguishability, the maximum classical 
   information encoded is $\log_2(4) = 2$ bits.

**Alice sends only one qubit**  
   Although the combined state space of two qubits has 
   dimension 4, Alice physically sends only *one* qubit to Bob. 
   The other qubit remains with Bob.  
   This shared entanglement enables transmission of 2 bits by sending 
   one qubit, but the limitation comes from the Hilbert space dimension
   of a single qubit: a single qubit lives in a 2-dimensional Hilbert 
   space.  
   You cannot reliably encode more than 2 bits (4 distinct orthogonal 
   states) into a single qubit.

### **Holevo bound**  
The Holevo theorem puts a fundamental limit on the amount of  
classical information that can be retrieved from a quantum state:  

$$
H(X : Y) \leq \chi = S(\rho) - \sum_i p_i S(\rho_i)
$$

where

- $H(X : Y)$ is the mutual classical information between sender's classical variable $X$ and receiver's measurement outcome $Y$,
- $\{p_i, \rho_i\}$ is an ensemble of quantum states prepared with probability $p_i$,
- $\rho = \sum_i p_i \rho_i$ is the average (mixed) state,
- $S(\sigma) = -\mathrm{Tr}(\sigma \log_2 \sigma)$ is the von Neumann entropy.

The Holevo quantity $\chi$ bounds the accessible classical information.

Since the von Neumann entropy of a density matrix $\rho$ acting on a Hilbert space of dimension $d$ satisfies

$$
S(\rho) \leq \log_2(d),
$$

the Holevo bound implies

$$
\chi \leq \log_2(d).
$$

For a single qubit, the Hilbert space dimension is $d = 2$, so the maximum classical information that can be extracted *without entanglement* is

$$
\chi \leq \log_2(2) = 1 \text{ bit}.
$$

---

#### **Superdense coding case:**  

Alice and Bob share an entangled two-qubit state, so the combined system lives in a Hilbert space of dimension

$$
d = 2 \times 2 = 4.
$$

Hence, the Holevo bound on the joint system is

$$
\chi \leq \log_2(4) = 2 \text{ bits}.
$$

By sending only **one qubit** (Alice's half of the entangled pair) to Bob, they can transmit up to 2 classical bits, saturating this bound. 

This is possible because the entanglement allows the single transmitted qubit to access the larger joint Hilbert space of dimension 4.

**Summary:**

$$
\boxed{
\begin{cases}
\text{No entanglement:} & H(X:Y) \leq 1 \text{ bit per qubit sent} \\
\text{With entanglement (superdense coding):} & H(X:Y) \leq 2 \text{ bits per qubit sent}
\end{cases}
}
$$

This formally proves that superdense coding achieves the maximal classical information transmission rate allowed by quantum mechanics for one qubit.

### **No faster-than-classical communication**  
   Attempting to encode more than 2 classical bits into one qubit sent from Alice to Bob would require more than 4 perfectly distinguishable quantum states, which do not exist.  
   Any attempt to do so results in overlapping, non-orthogonal states that cannot be reliably distinguished, leading to errors.

---

### Summary

- The **maximum classical information transmitted per qubit sent** 
with the help of shared entanglement is **2 bits**.
- This limit is dictated by the dimension of the combined system and 
the Holevo bound.
- Superdense coding *saturates* this limit by leveraging entanglement 
but cannot exceed it.
- Therefore, it is **impossible** to send more than 2 classical bits 
by sending only one qubit, even with quantum tricks.

---






# Superdense Coding with MPQP

## Objectives

1. Study and validate the theoretical limit: that no more than two classical bits can be transmitted per qubit.
2. Implement the protocol using MPQP with clearly separated logic for Alice and Bob.
3. Generalize the implementation to support an arbitrary number of classical bits (in multiples of 2).
4. Evaluate and visualize results of small instances through simulation.

## Implementation Overview

The project is structured around three main components:

- **Entanglement Preparation**: A function that creates `n` Bell pairs.
- **Alice**: A class that encodes 2 classical bits into her half of each Bell pair using a combination of quantum gates.
- **Bob**: A class that performs decoding operations (CNOT and Hadamard) followed by measurement.

Initially, I implemented the protocol for a fixed input of 2 bits to validate the encoding/decoding pipeline. 
After confirming its correctness, I extended the solution to support any even number of bits by processing each pair independently.

### A Small Detour

At first, I tried grouping the bits dynamically and tried to come up with a non-standard method to handle odd-length bitstrings,
but it quickly became messy and ambiguous. 
Eventually, we realized that the simplest and cleanest solution was to **pre-append a zero** when the number of bits is odd. 

### Encoding Rules

Each pair of bits maps to specific gates applied by Alice:

- `"00"` → Do nothing
- `"01"` → Apply `X`
- `"10"` → Apply `Z`
- `"11"` → Apply `X` then `Z`

These transformations modify the state of Alice's qubit in the shared Bell pair. Once Alice sends her qubit to Bob, he applies decoding operations and performs measurement to recover the original classical bits.

## Mathematical Bound

To understand the fundamental limitation, consider the space of quantum states. A single qubit carries a maximum of 1 qubit worth of information, but thanks to prior entanglement, I can encode 4 distinguishable states (00, 01, 10, 11) across the entangled pair. The measurement at Bob's end allows him to distinguish these four outcomes, hence retrieving 2 bits.

This upper bound aligns with Holevo’s theorem, which implies that I cannot extract more than 1 bit of classical information per qubit **unless** we make use of entanglement.

## Results

I simulated the protocol for small inputs, such as 2, 4, and 6 bits. The implementation includes the option to introduce depolarizing noise to test robustness.

An example histogram for the input bits `'11011'` with a noise level of 0.1 is shown below:

![Example Histogram](./Figure_1.png)

In the noiseless case, the most frequent output matches the original input (after padding and decoding), confirming the protocol works correctly.

## Conclusion

I successfully implemented and validated the superdense coding protocol using MPQP. 
The implementation handles any even number of bits, with automatic padding for odd inputs. 
The separation of roles between Alice and Bob made the design modular and easy to test. 

## References

- [Wikipedia: Superdense coding](https://en.wikipedia.org/wiki/Superdense_coding)
- [YouTube: Superdense Coding Explained](https://www.youtube.com/watch?v=UrAZHBwIAFQ)
