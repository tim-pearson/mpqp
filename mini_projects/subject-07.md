# Subject 7 - Exporting MPQP QCircuit to OpenQASM2

**Difficulty:** 4/5

## Introduction

`OpenQASM` is a quantum assembly language that became a standard in the quantum
computing community. Developed initially by QiskitIt, it describes quantum
circuits and basic operations at a very low lever. The current version is 3.0,
but we are interested, for this project, in the version 2.0 (the first one,
don't ask me why it starts from 2).

## Goal of the project

The goal is to implement the possibility to export a given ``QCircuit`` to
``OpenQASM2.0`` code, without using any external function and SDK. Currently, we
use the fact that we can interface an MPQP ``QCircuit`` with a Qiskit
``QuantumCircuit``, and use their function to retrieve the equivalent
``OpenQASM2.0`` code. This is done in the method ``QCircuit.to_qasm2()``. The
goal of the project is then to modify this method to parse the mpqp circuit and
generate the corresponding ``OpenQASM2.0`` string, that can be used later.

You will probably have to define for each gate or instruction a specific method
that returns the equivalent ``OpenQASM2.0`` code. Feel free to adapt the rest of
the code base to facilitate the implementation of this export.

## Resources

- OpenQASM2 original article : https://arxiv.org/pdf/1707.03429
- Link to the standard library "qelib1.inc" : https://github.com/openqasm/openqasm/blob/OpenQASM2.x/examples/qelib1.inc
- MPQP documentation website (QCircuit) : https://mpqpdoc.colibri-quantum.com/circuit

## Expected deliverables

A new implementation of the method `to_qasm2()` of the class `QCircuit` (and possibly of the class `Instruction`, 
if it makes sense for you), that exports your circuit as an OpenQASM2 string. You can either fork the mpqp project on your
own Git, or send us the whole source folder contaning all the modifications you did to incorporate this function.
Your program must handle all possible cases, natives gates, measurements etc. When a component (instruction or noise 
model) doesn't make sense in OpenQASM2, ignore it in the export and warn the user (you can create a custom class for 
this Warning in mpqp.tools.errors). Don't forget to consider special and extreme cases in your implementation.
