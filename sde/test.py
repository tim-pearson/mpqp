import unittest
from project import (
    SuperdenseProtocol,
)  # assuming your main code is in project.py


class TestSuperdenseProtocol(unittest.TestCase):
    def test_sent_equals_received_noiseless(self):
        test_cases = [
            "00",
            "01",
            "10",
            "11",
            "0000",
            "1101",
            "1010",
            "1111",
            "0011",
        ]
        for bits in test_cases:
            with self.subTest(bits=bits):
                protocol = SuperdenseProtocol(bits, noise=False)
                result = protocol.run_and_get_results()
                self.assertEqual(
                    result["bitstring"],
                    bits,
                    msg=f"Sent bits {bits} != received {result['bitstring']}",
                )

    def test_sent_approx_equals_received_noisy(self):
        test_cases = [
            "00",
            "01",
            "10",
            "11",
            "0000",
            "1101",
            "1010",
            "1111",
            "0011",
        ]
        threshold = 0.2  # minimum probability expected for the correct bitstring under noise
        for bits in test_cases:
            with self.subTest(bits=bits):
                protocol = SuperdenseProtocol(bits, noise=True)
                result = protocol.run_and_get_results()
                self.assertEqual(
                    result["bitstring"],
                    bits,
                    msg=f"Sent bits {bits} != most frequent noisy output {result['bitstring']}",
                )
                self.assertGreaterEqual(
                    result["probability"],
                    threshold,
                    msg=f"Probability {result['probability']:.3f} below threshold for bits {bits}",
                )


if __name__ == "__main__":
    unittest.main()
