"""This module defines the TestTriangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_triangle.py
"""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

import unittest
from shape.triangle import Triangle

class TestTriangle(unittest.TestCase):

    def setUp(self):
        self.triangle = Triangle("Red", 4, 5, 6)

    def test_init_attributes_set_to_assigned_values(self):
        triangle = Triangle("Red", 4, 5, 6)

        self.assertEqual(triangle._color, "Red")  
        self.assertEqual(triangle._Triangle__side_1, 4)  
        self.assertEqual(triangle._Triangle__side_2, 5)     
        self.assertEqual(triangle._Triangle__side_3, 6)

    def test_init_exception_raised_for_blank_color(self):
        with self.assertRaises(ValueError) as context:
            Triangle("", 4, 5, 6)
        self.assertEqual(str(context.exception), "Color cannot be blank")

    def test_init_exception_raised_for_non_integer_side_1(self):
        with self.assertRaises(ValueError) as context:
            Triangle("Red", "four", 5, 6)
        self.assertEqual(str(context.exception), "Side 1 must be numeric.")

    def test_init_exception_raised_for_non_integer_side_2(self):
        with self.assertRaises(ValueError) as context:
            Triangle("Red", 4, "five", 6)
        self.assertEqual(str(context.exception), "Side 2 must be numeric.")     

    def test_init_exception_raised_for_non_integer_side_3(self):
        with self.assertRaises(ValueError) as context:
            Triangle("Red", 4, 5, "six")
        self.assertEqual(str(context.exception), "Side 3 must be numeric.")

    def test_init_exception_raised_triangle_inequality_theorem(self):
        with self.assertRaises(ValueError) as context:
            Triangle("Red", 1, 2, 3)
        self.assertEqual(str(context.exception), "The sides do not satisfy the Triangle Inequality Theorem.")

    def test_str_returns_expected_string(self):
        expected_string = "The shape color is Red.\n This triangle has three sides with lengths of 4, 5 and 6 centimeters."
        self.assertEqual(str(self.triangle), expected_string)
    
    def test_calculate_area_returns_expected_value(self):
        self.assertEqual(self.triangle.calculate_area(), 9.921567416492215)

    
    
