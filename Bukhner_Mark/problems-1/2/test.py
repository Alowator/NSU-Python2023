import unittest

from main import fit


class TestStringMethods(unittest.TestCase):

    def test_zero(self):
        lst = []
        fit(lst, 10, 20)
        self.assertEqual([], lst)

    def test_simple(self):
        lst = [-1, 3, 6, 15]
        fit(lst, 2, 10)
        self.assertEqual([2, 3, 6, 10], lst)

    def test_float(self):
        lst = [-1., 3., 6., 15.]
        fit(lst, 2., 10.)
        self.assertEqual([2., 3., 6., 10.], lst)

    def test_b_lower_than_a(self):
        lst = [-1, 3, 6, 15]
        self.assertRaises(ValueError, fit, lst, 10, 2)

    def test_b_equals_a(self):
        lst = [-1, 3, 6, 15]
        fit(lst, 10, 10)
        self.assertEqual([10] * len(lst), lst)


if __name__ == '__main__':
    unittest.main()
