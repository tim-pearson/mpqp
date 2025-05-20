from mpqp.measures import pauli_string, Observable
from mpqp.core.languages import Language
from mpqp.measures import I, X, Y, Z
import numpy as np
from mpqp import QCircuit
from mpqp.gates import *
from mpqp.measures import BasisMeasure
from mpqp.noise import Depolarizing
from mpqp.execution import run
from mpqp.execution.devices import AWSDevice
# %% Ex1
p = I @ Z - 3 * Z @ Z + 2* Z @ I
# %%
p1 = 2 *X @X - Y @ Y + Z @ X
p2 = 2 * p1 +Y @ X - 4 * X @ X
print((p2).to_matrix())
mat = [[4, 2, 3, 8], [2, -3, 1, 0], [3, 1, -1, 5], [8, 0, 5, 2]]
obs =Observable(np.array(obs))
print(obs.pauli_string)

# EX2
# %% q1
circ = QCircuit(6)
targets = range(3)
ancillas = range(3,6)
for i in range(3):
    circ.add(CNOT(targets[i], ancillas[i]))
print(circ)
# %% q2
device = AWSDevice.BRAKET_LOCAL_SIMULATOR
result_global = run(circuit, device)
print("after global noise (p=0.05):")
print(result_global)
# %% q3
circuit.add(Depolarizing(0.47, [0]))
# %% q4 
circuit.add(Depolarizing(0.33, [0, 1], dimension=2, gates=[CNOT]))
# %% q5

result = run(circuit, device)
print("\nQubit 0 noise (p=0.47) results:")
print(result)

# %% q7
braket_circuit = circuit.to_other_language(language=Language.BRAKET)
print("\nBraket circuit representation:")
print(braket_circuit)

# EX3
# %%
circ = QCircuit(6)
targets = range(3)
ancillas = range(3,6)
for i in range(3):
    circ.add(CNOT(targets[i], ancillas[i]))
print(circ)
qasm2 = circuit.to_other_language(Language.QASM2)
print(qasm2)
# %%
qasm3 = circuit.to_other_language(Language.QASM3)
print(qasm3)
