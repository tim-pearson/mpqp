from mpqp import QCircuit
from mpqp.gates import H, CNOT, X, Z
from mpqp.measures import BasisMeasure
from mpqp.execution import run
from mpqp.execution.devices import AWSDevice


class AliceEncodeCircuit(QCircuit):
    def __init__(self, bits: str):
        super().__init__()
        # Alice's encoding gates depending on the bits
        if bits == "00":
            pass  # no gates
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
        # Bob's decoding gates
        self.add(CNOT(0, 1))
        self.add(H(0))




class SuperdenseProtocol(QCircuit):
    def __init__(self, bits: str):
        super().__init__()
        # Step 1: Create Bell pair
        self.add(H(0))
        self.add(CNOT(0, 1))

        # Step 2: Alice encoding
        alice_circuit = AliceEncodeCircuit(bits)
        for gate in alice_circuit.gates:
            self.add(gate)

        # Step 3: Bob decoding
        bob_circuit = BobDecodeCircuit()
        for gate in bob_circuit.gates:
            self.add(gate)

        # Step 4: Measurement
        self.add(BasisMeasure([0, 1], shots=1000))  # increase shots for stats

        self._result = None  # will hold last run result

    def run_and_get_results(self, device=AWSDevice.BRAKET_LOCAL_SIMULATOR):
        self._result = run(self, device)
        counts = self._result.counts
        total_counts = sum(counts)
        # Find the most probable bitstring and probability
        max_index = counts.index(max(counts))
        bitstring = format(max_index, f'0{self.measurements[0].nb_qubits}b')
        probability = counts[max_index] / total_counts
        return {
            "bitstring": bitstring,
            "probability": probability,
            "counts": counts,
            "raw_result": self._result,
        }


def main():
    bits = "11"
    protocol = SuperdenseProtocol(bits)
    result = protocol.run_and_get_results()
    print(f"Alice sent bits: {bits}")
    print(
        f"Most probable output: {result['bitstring']} with probability {result['probability']}"
    )


if __name__ == "__main__":
    main()
