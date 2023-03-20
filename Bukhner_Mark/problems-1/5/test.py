import unittest

from main import prime_factors


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual([], prime_factors(1))

    def test_2(self):
        self.assertEqual([[2, 1]], prime_factors(2))

    def test_3(self):
        self.assertEqual([[3, 1]], prime_factors(3))

    def test_12(self):
        self.assertEqual([[2, 2], [3, 1]], prime_factors(12))


if __name__ == '__main__':
    unittest.main()
