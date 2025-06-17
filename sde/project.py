from mpqp import QCircuit
from mpqp.gates import H, CNOT, X, Z
from mpqp.measures import BasisMeasure
from mpqp.execution import run
from mpqp.execution.devices import AWSDevice

# Alice encodes her 2 classical bits using quantum gates
def alice_encode(bits):
    gates = []
    if bits == "00":
        pass
    elif bits == "01":
        gates.append(X(0))
    elif bits == "10":
        gates.append(Z(0))
    elif bits == "11":
        gates.extend([X(0), Z(0)])
    else:
        raise ValueError("Bits must be '00', '01', '10', or '11'")
    return gates

# Bob applies decoding gates
def bob_decode():
    return [CNOT(0, 1), H(0)]

def main():
    bits = "10"  # Message Alice wants to send
    circuit = QCircuit()

    # 1. Create entangled Bell pair
    circuit.add(H(0))
    circuit.add(CNOT(0, 1))

    # 2. Alice encodes
    for gate in alice_encode(bits):
        circuit.add(gate)

    # 3. Bob decodes
    for gate in bob_decode():
        circuit.add(gate)

    # 4. Measure
    circuit.add(BasisMeasure([0, 1], shots=1))

    # 5. Run
    device = AWSDevice.BRAKET_LOCAL_SIMULATOR
    result = run(circuit, device)

    print(f"Alice sent bits: {bits}")
    print("Bob received:")
    print(result)
    print("\nCircuit:")
    print(circuit)

if __name__ == "__main__":
    main()

