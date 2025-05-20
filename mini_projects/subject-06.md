# Subject 6 - Parsing OpenQASM2 to generate an MPQP QCricuit

**Difficulty:** 4/5

## Introduction

`OpenQASM` is a quantum assembly language that became a standard in the quantum
computing community. Developed initially by QiskitIt, it describes quantum
circuits and basic operations at a very low lever. The current version is 3.0,
but we are interested, for this project, in the version 2.0 (the first one,
don't ask me why it starts from 2).

## Goal of the project

The goal of the project is to provide a function that can parse a string
containing an `OpenQASM2` code, and return the corresponding mpqp `QCircuit`.

Your program must be able to translate a large set of `OpenQASM2` code, and thus
support almost the whole standard, from native to custom gates, as well as
barriers, includes and measurements. You may avoid the `reset` and `if`
statements since resets and conditional instructions are not available for
`QCircuit`. Don't forget to consider special and extreme cases in your
implementation.

## Resources

- OpenQASM2 original article : https://arxiv.org/pdf/1707.03429
- Link to the standard library "qelib1.inc" : https://github.com/openqasm/openqasm/blob/OpenQASM2.x/examples/qelib1.inc
- MPQP documentation website (QCircuit) : https://mpqpdoc.colibri-quantum.com/circuit

You can also reuse part of the code used for implementing the converter from
OpenQASM2.0 to OpenQASM3.0, especially the parser of OpenQASM2.0 code that
extracts each instruction or block of instructions. You can have a look at the
documentation here: https://mpqpdoc.colibri-quantum.com/qasm

## Expected deliverables

You must produce a .py file containing all the functions needed for this
translation. Your code should be documented(docstring, accordingly to the rest
of the mpqp library) and commented (when needed). Apart from the algorithm
itself, you should also provide a set of functional tests (that can be run on
pytest), insuring that your function converts correctly an OpenQASM2 code to a
`QCircuit`. Your tests should be as independent as possible from actual code, so
I would not recommend the use of `QCircuit.to_qasm2()` for checking that you
retrieve an equivalent result to the input.
