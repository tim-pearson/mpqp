# test_superdense.py

from project import run_superdense_protocol  # assumes function is defined in project.py
import sys

def test_case(bits):
    print(f"Running test for bits: {bits}")
    received_bits = run_superdense_protocol(bits)
    assert received_bits == bits, f"❌ Test failed: Sent {bits}, but received {received_bits}"
    print(f"✅ Test passed: {bits} -> {received_bits}")

def run_all_tests():
    all_bits = ["00", "01", "10", "11"]
    failed = False

    for bits in all_bits:
        try:
            test_case(bits)
        except AssertionError as e:
            print(e)
            failed = True

    if failed:
        print("\n❌ Some tests failed.")
        sys.exit(1)
    else:
        print("\n✅ All tests passed successfully.")

if __name__ == "__main__":
    run_all_tests()

