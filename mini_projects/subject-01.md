# Subject 1 - Implement Deutch-Jozsa's algorithm with MPQP

**Difficulty:** 1/5

The `Deutsch-Jozsa` algorithm is a quantum algorithm designed to solve a specific
problem more efficiently than any classical algorithm. The goal is to determine
whether a given function $f : \{0, 1\}^n \to \{0, 1\}$ is `constant` (i.e., the
same output for all inputs) or `balanced` (i.e., outputs 0 for half of the
inputs and 1 for the other half). This is a problem involving an oracle or black
box.

## Input
- $f: \{0,1\}^n \to \{0,1\}$
- Problem: 
    - $f$ is `constant`
    - $f$ is `balanced` ($|f^{-1}(0)| = |f^{-1}(1)|$)

### Classical Complexity
- Calculate the classical complexity of solving this problem.

## Steps for implementations

![image info](resources/Deutsch-Jozsa_algorithm.png)

1. Initialize the qubits: $|0\rangle^{\otimes n} |1\rangle$.
2. Apply Hadamard gates to all qubits.
3. Apply the oracle $U_f$, you are free to select the function.
4. Apply Hadamard gates to the first $ n $ qubits.
5. Measure the first $n$ qubits.

## Solution

Analyze the amplitude of the measurement results to determine if the function is balanced or constant.
<details>
  <summary>hint</summary>
<ol>
  <li>0 for a solution</li>
  <li>1 or -1 for the other</li>
</ol>
</details>