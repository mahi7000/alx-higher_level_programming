#!/usr/bin/python3
""" Test using unittest """
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittests to test max_integer """
    def test_empty_list(self):
        """ tests empty list """
        lists = []
        self.assertIsNone(max_integer(lists))

    def test_no_arguments(self):
        """ tests no arguments """
        self.assertIsNone(max_integer())

    def test_one(self):
        """ tests with one elemnt in list """
        tests = [1]
        self.assertEqual(max_integer(tests), 1)

    def test_postitve_only(self):
        """ test list with only positive elements """
        test = [1, 2, 3, 4]
        self.assertEqual(max_integer(test), 4)

    def test_negative(self):
        """ test list with negative elements """
        test = [-1, -2, -3]
        self.assertEqual(max_integer(test), -1)

    def test_negative_postive(self):
        """ test list with both negative and positive elemnts """
        test = [-1, 4, 56, -2, 3]
        self.assertEqual(max_integer(test), 56)

    def test_integer(self):
        """ test for a non integer """
        non_int = [1, 2, 'hi']
        with self.assertRaises(TypeError):
            max_integer(non_int)


if __name__ == "__main__":
    unittest.main()
