from mpqp import QCircuit
from mpqp.gates import H, CNOT, X, Z
from mpqp.measures import BasisMeasure
from mpqp.noise import Depolarizing
from mpqp.execution import run
from mpqp.execution.devices import AWSDevice


class AliceEncodeCircuit(QCircuit):
    def __init__(self, bits: str):
        super().__init__()
        if bits == "00":
            pass
        elif bits == "01":
            self.add(X(0))
        elif bits == "10":
            self.add(Z(0))
        elif bits == "11":
            self.add(X(0))
            self.add(Z(0))
        else:
            raise ValueError("Bits must be '00', '01', '10', or '11'")


class BobDecodeCircuit(QCircuit):
    def __init__(self):
        super().__init__()
        self.add(CNOT(0, 1))
        self.add(H(0))


class SuperdenseProtocol(QCircuit):
    def __init__(self, bits: str, noise=False):
        super().__init__()
        self.add(H(0))
        self.add(CNOT(0, 1))

        alice_circuit = AliceEncodeCircuit(bits)
        for gate in alice_circuit.gates:
            self.add(gate)

        if noise:
            # Add depolarizing noise on qubit 0 and qubit 1 after Alice encoding
            self.add(Depolarizing(0.1, [0]))
            self.add(Depolarizing(0.1, [1]))

        bob_circuit = BobDecodeCircuit()
        for gate in bob_circuit.gates:
            self.add(gate)

        self.add(BasisMeasure([0, 1], shots=1000))

    def run_and_get_results(self, device=AWSDevice.BRAKET_LOCAL_SIMULATOR):
        result = run(self, device)
        counts = result.counts
        total_counts = sum(counts)
        max_index = counts.index(max(counts))
        bitstring = format(max_index, f"0{self.measurements[0].nb_qubits}b")
        probability = counts[max_index] / total_counts
        return {
            "bitstring": bitstring,
            "probability": probability,
            "counts": counts,
            "raw_result": result,
        }


def main():
    bits = "11"

    print("Running noiseless simulation...")
    protocol = SuperdenseProtocol(bits, noise=False)
    result = protocol.run_and_get_results()
    print(f"Alice sent bits: {bits}")
    print(
        f"Noiseless output: {result['bitstring']} with probability {result['probability']}"
    )
    print(f"Counts: {result['counts']}")
    print()

    # Run with noise
    print("Running noisy simulation with Depolarizing noise...")
    protocol_noisy = SuperdenseProtocol(bits, noise=True)
    result_noisy = protocol_noisy.run_and_get_results()
    print(
        f"Noisy output: {result_noisy['bitstring']} with probability {result_noisy['probability']}"
    )
    print(f"Counts: {result_noisy['counts']}")


if __name__ == "__main__":
    main()
