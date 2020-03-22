import unittest

from Engine.utils.math_utils import clamp


class MathUtilsTest(unittest.TestCase):

    def test_clamp_min_value(self):
        value = 12
        min_value = 15
        max_value = 20

        expected = min_value
        result = clamp(value, min_value, max_value)

        self.assertEqual(expected, result)

    def test_clamp_max_value(self):
        value = 24
        min_value = 15
        max_value = 20

        expected = max_value
        result = clamp(value, min_value, max_value)

        self.assertEqual(expected, result)

    def test_clamp_value_between_min_and_max(self):
        value = 17
        min_value = 15
        max_value = 20

        expected = value
        result = clamp(value, min_value, max_value)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
