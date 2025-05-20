# Subject 10 - Superdense conding
 
**Difficulty:** 3/5
 
## Introduction
 
This communication protocol was introduce for the first time in 1992 and allows for an encoding and transmission of information more "dense" than usual protocls. More precisely, it allows Alice to transmit 2 bits of classical information to Bob, by only sending one qubit.
 
## Goal of the project
 
The first goal is to study the protocol and to prove that we cannot send more than 2 bits of information by only sending one qubit.
 
The second goal is to implement the protocol using MPQP, and simulate independently the tranmission from Alice, and the decoding by Bob. For that, you will define two indepedent objects (functions/classes): the first one (Alice) preparing the information and sending the corresponding qubit; the second (Bob) only takes as input the qubit transmitted, and retrieves the corresponding classical information sent by Alice.
 
The last goal is to generalize the protocol to any number of classical bit to be transmitted (not only 2).
 
## Resources
https://en.wikipedia.org/wiki/Superdense_coding
https://www.youtube.com/watch?v=UrAZHBwIAFQ
 
 
## Expected deliverables
A report recalling the principle of the protocol, and the associated proofs (goal 1).
 
A code containing the MPQP implementation of the generalized superdense coding protocol, and a `main` function to execute the protocol.