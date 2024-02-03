#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):

    def test_max_in_pos(self):
        """ Tests for the maximum number in a list of positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_max_in_single(self):
        """ Tests for the maximum number in a list of just one integer """
            
        self.assertEqual(max_integer([5]), 5)

    def test_max_in_neg(self):
        """ Tests for the maximum number in a list of negative integers """

        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    
    def test_max_in_mixed(self):
        """ returns the maximum number in a list of positive and negative integers """
        self.assertEqual(max_integer([-1, 3, 4, -3, 9]), 9)
    
    def test_list_length(self):
        """ checks if list passed is empty and resurns None"""

        self.assertEqual(max_integer([]), None)
    
    def test_not_none_in_pos(self):
        """ Test that the maximum number in a list of positive numbers is not None"""
            
        self.assertNotEqual(max_integer([1, 2, 3]), None)

    def test_not_none_in_neg(self):
        """ Test that the maximum num in a list of negative numbers is not None"""

        self.assertNotEqual(max_integer([-1, -2, -3]), None)

    def test_not_none_in_mixed(self):
        """ Test that the max number in a list of mixed integers is not None"""
        
        self.assertNotEqual(max_integer([1, -2, 3, -4]), None)


    def test_list_with_floats(self):
        """Tests a list with float point numbers """
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 2.0]), 3.2)
    
    def test_large_num(self):
        """ Test for the max num in a list of large integeres"""

        self.assertEqual(max_integer([100000, 200000, 300000, 400000]), 400000)
        

    def test_different_types(self):

        with self.assertRaises(TypeError):
            max_integer([1, 'apple', 3, 7, 'banana'])
