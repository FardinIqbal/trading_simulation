# tests/test_utils.py

import unittest
from trading_simulation.utils import calculate_probability

class TestUtils(unittest.TestCase):
    def test_calculate_probability(self):
        self.assertEqual(calculate_probability(500, 1000), 0.5)
        self.assertEqual(calculate_probability(0, 1000), 0)
        self.assertEqual(calculate_probability(1000, 1000), 1)

if __name__ == '__main__':
    unittest.main()
