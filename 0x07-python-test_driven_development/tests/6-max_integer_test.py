#!/usr/bin/python3
"""Unittest for maxi([..])
"""
import unittest
maxi = __import__('6-maxi').maxi


class TestMaxInteger(unittest.TestCase):
    """unittest class for maxi"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-maxi').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        f = maxi.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        e = []
        self.assertIsNone(maxi(e))

    def test_no_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(maxi())

    def test_one_element(self):
        """Tests for only one number in the list"""
        o = [1]
        self.assertEqual(maxi(o), 1)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        e = [2, 10, 8, 36, 14, 50]
        self.assertEqual(maxi(e), 50)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        m = [2, 10, 8, 360, 14, 50]
        self.assertEqual(maxi(m), 360)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        b = [200, 10, 8, 36, 14, 50]
        self.assertEqual(maxi(b), 200)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        on = [200, 10, 8, -36, 14, 50]
        self.assertEqual(maxi(on), 200)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        n = [-6, -50, -75, -1, -100]
        self.assertEqual(maxi(n), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            maxi(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Hello", 4, 5]
        with self.assertRaises(TypeError):
            maxi(string)

if __name__ == "__main__":
    unittest.main()
