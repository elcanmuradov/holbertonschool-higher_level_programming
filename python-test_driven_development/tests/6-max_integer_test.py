#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with a regular list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-5]), -5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -5, -3, -8]), -3)
        self.assertEqual(max_integer([-100]), -100)

    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([5, -10, 3, -2]), 5)
        self.assertEqual(max_integer([-5, -2, 0, -1]), 0)

    def test_duplicates(self):
        """Test with duplicate numbers"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 1, 2, 2]), 2)
        self.assertEqual(max_integer([3, 1, 3, 1]), 3)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)
        self.assertEqual(max_integer([100, 50, 25]), 100)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
        self.assertEqual(max_integer([25, 50, 100]), 100)

    def test_max_in_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 10, 2, 3]), 10)
        self.assertEqual(max_integer([25, 100, 50]), 100)

    def test_two_elements(self):
        """Test with two elements"""
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([2, 1]), 2)
        self.assertEqual(max_integer([-1, -2]), -1)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000000, 999999, 1000001]), 1000001)
        self.assertEqual(max_integer([2**31 - 1, 2**31 - 2]), 2**31 - 1)

    def test_zero_and_positive(self):
        """Test with zero and positive numbers"""
        self.assertEqual(max_integer([0, 1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1, 0]), 3)
        self.assertEqual(max_integer([0, 0, 1]), 1)

    def test_zero_and_negative(self):
        """Test with zero and negative numbers"""
        self.assertEqual(max_integer([0, -1, -2, -3]), 0)
        self.assertEqual(max_integer([-3, -2, -1, 0]), 0)
        self.assertEqual(max_integer([0, 0, -1]), 0)

    def test_all_zeros(self):
        """Test with all zeros"""
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertEqual(max_integer([0]), 0)

    def test_long_list(self):
        """Test with a longer list"""
        long_list = list(range(100))
        self.assertEqual(max_integer(long_list), 99)
        
        long_list_reversed = list(range(99, -1, -1))
        self.assertEqual(max_integer(long_list_reversed), 99)

    def test_float_like_integers(self):
        """Test with integer values that could be confused with floats"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
        # Note: The function expects integers, so we test with integers only

    def test_identical_elements(self):
        """Test with all identical elements"""
        self.assertEqual(max_integer([7, 7, 7]), 7)
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)

    def test_ascending_order(self):
        """Test with list in ascending order"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-5, -3, -1, 0, 2]), 2)

    def test_descending_order(self):
        """Test with list in descending order"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([2, 0, -1, -3, -5]), 2)

    def test_random_order(self):
        """Test with randomly ordered lists"""
        self.assertEqual(max_integer([3, 1, 4, 1, 5, 9, 2, 6]), 9)
        self.assertEqual(max_integer([10, 3, 7, 1, 9, 4]), 10)


if __name__ == '__main__':
    unittest.main()