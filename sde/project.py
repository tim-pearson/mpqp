from mpqp import QCircuit
from mpqp.gates import H, CNOT, X, Z
from mpqp.measures import BasisMeasure
from mpqp.noise import Depolarizing
from mpqp.execution import run
from mpqp.execution.devices import AWSDevice


def prepare_bell_pairs(n_pairs: int) -> QCircuit:
    """
    Prepare n_pairs of Bell pairs on qubits [0..2*n_pairs-1].
    Each pair consists of qubits (2*i, 2*i+1).
    """
    circuit = QCircuit()
    for i in range(n_pairs):
        circuit.add(H(2 * i))
        circuit.add(CNOT(2 * i, 2 * i + 1))
    return circuit


class AliceEncodeCircuit(QCircuit):
    def __init__(self, bits: str):
        """
        Alice encodes 2 classical bits per entangled pair using X and Z gates:
        For each 2-bit chunk:
          "00" -> I (do nothing)
          "01" -> X
          "10" -> Z
          "11" -> XZ (or ZX)
        """
        super().__init__()
        if len(bits) % 2 != 0:
            raise ValueError("Number of bits must be even")

        n_pairs = len(bits) // 2
        for i in range(n_pairs):
            pair_bits = bits[2 * i : 2 * i + 2]
            target_qubit = (
                2 * i + 1
            )  # Alice applies gates on her half (second qubit of each pair)

            if pair_bits == "00":
                pass  # Identity, no gates
            elif pair_bits == "01":
                self.add(X(target_qubit))
            elif pair_bits == "10":
                self.add(Z(target_qubit))
            elif pair_bits == "11":
                self.add(X(target_qubit))
                self.add(Z(target_qubit))
            else:
                raise ValueError("Bits must be '00', '01', '10', or '11'")


class BobDecodeCircuit(QCircuit):
    def __init__(self, n_pairs: int):
        """
        Bob decodes the bits by applying CNOT and H on each pair.
        Applies on qubits (2*i, 2*i+1).
        """
        super().__init__()
        for i in range(n_pairs):
            self.add(CNOT(2 * i, 2 * i + 1))
            self.add(H(2 * i))


class SuperdenseProtocol:
    def __init__(self, bits: str, noise=None):
        if len(bits) % 2 != 0:
            raise ValueError(
                "Number of bits must be even for superdense coding"
            )

        self.n_pairs = len(bits) // 2
        self.bits = bits
        self.noise = noise

        # Prepare circuits
        self.bell_prep = prepare_bell_pairs(self.n_pairs)
        self.alice = AliceEncodeCircuit(bits)
        self.bob = BobDecodeCircuit(self.n_pairs)

        # Compose full circuit by concatenation (not literally, we build step by step)
        self.circuit = QCircuit()
        # Add bell pair preparation
        for gate in self.bell_prep.gates:
            self.circuit.add(gate)

        # Alice encoding
        for gate in self.alice.gates:
            self.circuit.add(gate)

        # Add noise if requested on *all* qubits after Alice encoding
        if self.noise:
            qubits = list(range(2 * self.n_pairs))
            self.circuit.add(Depolarizing(noise, qubits))

        # Bob decoding
        for gate in self.bob.gates:
            self.circuit.add(gate)

        # Measurement on all qubits (all pairs)
        self.circuit.add(
            BasisMeasure(list(range(2 * self.n_pairs)), shots=1000)
        )

    def run_and_get_results(self, device=AWSDevice.BRAKET_LOCAL_SIMULATOR):
        result = run(self.circuit, device)
        counts = result.counts
        total_counts = sum(counts)
        max_index = counts.index(max(counts))

        # Each measurement outcome corresponds to 2*n_pairs bits, bits in measurement correspond to qubits 0..N-1
        bitstring = format(max_index, f"0{2*self.n_pairs}b")
        probability = counts[max_index] / total_counts
        return {
            "bitstring": bitstring,
            "probability": probability,
            "counts": counts,
            "raw_result": result,
        }

