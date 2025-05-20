# Subject 3 - Implement HHL's algorithm with MPQP

**Difficulty:** 4/5

HHL allows you to solve linear systems of the form $A\vec{x\;}=\vec{b\;}$ more
efficiently than its classical counterpart, given a few constraints. More
precisely, HHL will not return $\vec{x\;}$, but for an arditrary observable $M$,
it will return the expectation value of the measure of $\vec{x\;}$ by this 
observable, $\langle M|\vec{x\;}|M\rangle$.

HHL is a quite complex algorithm, in order to implement it, here is a list of
suggested steps.

1. In grover's algorithm, a crucial step is the *amplitude amplification*
  implement this step, and make sure to understand how it works (try to get an
  intuition for it)
2. The algorithm start from $|b\rangle$, the quantum encoding of the right hand
  side of the linear system $\vec{b\;}$. $|b\rangle$ is an arbitrary state, but
  before starting from a generic implementation, start from an hardcoded initial
  state. Similarly, you can start from hardcoded versions of $A$ and $M$.
3. Before evaluating the expectation value of $|x\rangle$ as expected in HHL,
  make sure it has the shape you are expecting

Your final work is an implementation of HHL as general as possible. Good luck!