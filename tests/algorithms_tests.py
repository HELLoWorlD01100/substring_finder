import unittest
from algorithms.brut_force import BrutForceAlgorithm
from model import Model


class brut_force_tests(unittest.TestCase):
    def setUp(self) -> None:
        self.brut_force = BrutForceAlgorithm("abcb", "b")

    def test_one_step(self):
        expected = []
        actual = self.brut_force.pass_one_step()
        self.assertEqual(expected, actual.found_indexes)

        expected = []
        actual = self.brut_force.pass_one_step()
        self.assertEqual(expected, actual.found_indexes)

        expected = [1]
        actual = self.brut_force.pass_one_step()
        self.assertEqual(expected, actual.found_indexes)

        expected = [1]
        actual = self.brut_force.pass_one_step()
        self.assertEqual(expected, actual.found_indexes)

        expected = [1]
        actual = self.brut_force.pass_one_step()
        self.assertEqual(expected, actual.found_indexes)

        expected = [1, 3]
        actual = self.brut_force.pass_one_step()
        self.assertEqual(expected, actual.found_indexes)


if __name__ == '__main__':
    unittest.main()
