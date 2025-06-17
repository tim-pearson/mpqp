# %%
import matplotlib.pyplot as plt
from mpqp import QCircuit
from mpqp.gates import H, CNOT, X, Z
from mpqp.measures import BasisMeasure
from mpqp.noise import Depolarizing
from mpqp.execution import run
from mpqp.execution.devices import AWSDevice

# Re-define prepare_bell_pairs, AliceEncodeCircuit, BobDecodeCircuit, and SuperdenseProtocol here or import if available
# For brevity, assuming they are imported or already defined in the environment

def prepare_bell_pairs(n_pairs: int) -> QCircuit:
    circuit = QCircuit()
    for i in range(n_pairs):
        circuit.add(H(2 * i))
        circuit.add(CNOT(2 * i, 2 * i + 1))
    return circuit

class AliceEncodeCircuit(QCircuit):
    def __init__(self, bits: str):
        super().__init__()
        if len(bits) % 2 != 0:
            raise ValueError("Number of bits must be even")
        n_pairs = len(bits) // 2
        for i in range(n_pairs):
            pair_bits = bits[2 * i : 2 * i + 2]
            target_qubit = 2 * i + 1
            if pair_bits == "01":
                self.add(X(target_qubit))
            elif pair_bits == "10":
                self.add(Z(target_qubit))
            elif pair_bits == "11":
                self.add(X(target_qubit))
                self.add(Z(target_qubit))

class BobDecodeCircuit(QCircuit):
    def __init__(self, n_pairs: int):
        super().__init__()
        for i in range(n_pairs):
            self.add(CNOT(2 * i, 2 * i + 1))
            self.add(H(2 * i))

class SuperdenseProtocol:
    def __init__(self, bits: str, noise=None):
        if len(bits) % 2 != 0:
            raise ValueError("Number of bits must be even for superdense coding")
        self.n_pairs = len(bits) // 2
        self.bits = bits
        self.noise = noise
        self.bell_prep = prepare_bell_pairs(self.n_pairs)
        self.alice = AliceEncodeCircuit(bits)
        self.bob = BobDecodeCircuit(self.n_pairs)
        self.circuit = QCircuit()
        for gate in self.bell_prep.gates:
            self.circuit.add(gate)
        for gate in self.alice.gates:
            self.circuit.add(gate)
        if self.noise is not None:
            qubits = list(range(2 * self.n_pairs))
            self.circuit.add(Depolarizing(self.noise, qubits))
        for gate in self.bob.gates:
            self.circuit.add(gate)
        self.circuit.add(BasisMeasure(list(range(2 * self.n_pairs)), shots=1000))

    def run_and_get_results(self, device=AWSDevice.BRAKET_LOCAL_SIMULATOR):
        result = run(self.circuit, device)
        counts = result.counts
        total_counts = sum(counts)
        max_index = counts.index(max(counts))
        bitstring = format(max_index, f"0{2*self.n_pairs}b")
        probability = counts[max_index] / total_counts
        return {
            "bitstring": bitstring,
            "probability": probability,
            "counts": counts,
            "raw_result": result,
        }

# %%
# Plot 1: Histogram of counts for 6 bits with noise level 0.1

bits = "110011"  # 6 bits (3 pairs)
noise_level = 0.1

protocol = SuperdenseProtocol(bits, noise=noise_level)
result = protocol.run_and_get_results()

counts = result["counts"]
num_qubits = 2 * protocol.n_pairs

# Plot histogram of counts
plt.figure(figsize=(10, 6))
plt.bar(range(len(counts)), counts)
plt.xticks(
    range(len(counts)),
    [format(i, f"0{num_qubits}b") for i in range(len(counts))],
    rotation=90,
    fontsize=8,
)
plt.xlabel("Measured bitstrings")
plt.ylabel("Counts")
plt.title(f"Measurement Counts for bits '{bits}' with noise={noise_level}")
plt.tight_layout()
plt.show()

# %%
# Plot 2: Effect of noise on correct bitstring probability
import numpy as np
import matplotlib.pyplot as plt

def bitwise_accuracy(sent_bits, measured_bits):
    matches = sum(s == m for s, m in zip(sent_bits, measured_bits))
    return matches / len(sent_bits)

noise_values = np.linspace(0, 0.3, 10)
correct_probabilities = []
avg_accuracies = []

for p in noise_values:
    protocol = SuperdenseProtocol(bits, noise=p)
    result = protocol.run_and_get_results()
    counts = result["counts"]
    total_counts = sum(counts)

    # Exact correct bitstring probability
    if result["bitstring"] == bits:
        correct_probabilities.append(result["probability"])
    else:
        correct_probabilities.append(0.0)

    # Average bitwise accuracy weighted by counts
    avg_accuracy = 0.0
    for idx, count in enumerate(counts):
        measured = format(idx, f"0{len(bits)}b")
        acc = bitwise_accuracy(bits, measured)
        avg_accuracy += (count / total_counts) * acc
    avg_accuracies.append(avg_accuracy)

plt.figure(figsize=(10, 6))
plt.plot(noise_values, correct_probabilities, marker='o', label="Exact bitstring probability")
plt.plot(noise_values, avg_accuracies, marker='x', label="Average bitwise accuracy")
plt.xlabel("Depolarizing noise parameter p")
plt.ylabel("Accuracy")
plt.title(f"Noise impact on superdense coding accuracy (bits='{bits}')")
plt.legend()
plt.grid(True)
plt.show()

