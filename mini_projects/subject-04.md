# Subject 4 - Implement Bernstein-Vazirani's algorithm with MPQP

**Difficulty:** 2/5

The Bernstein–Vazirani algorithm aims at finding the string encoded in a
function.

Create a function that takes in a string and returns this string, by first
encoding it in the function as $f_s(x)=s\cdot x$, then encoding this function in
an oracle, and then running Bernstein-Vazirani's algorithm with this oracle.

![](resources/print_with_extra_steps.jpg)