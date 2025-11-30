"""This module defines the TestRectangle class.

Usage: 
    To execute all tests in the terminal execute the following command:

    $ python -m unittest tests/test_rectangle.py
"""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

import unittest
from shape.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        self.rectangle = Rectangle("Blue", 10, 15)

    def test_init_attributes_set_to_assigned_values(self):
        rectangle = Rectangle("Blue", 10, 15)

        self.assertEqual(rectangle._color, "Blue")  
        self.assertEqual(rectangle._Rectangle__length, 10)  
        self.assertEqual(rectangle._Rectangle__width, 15)     

    def test_init_exception_raised_for_blank_color(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("", 10, 15)
        self.assertEqual(str(context.exception), "Color cannot be blank")

    def test_init_exception_raised_for_non_integer_length(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("Blue", "ten", 15)
        self.assertEqual(str(context.exception), "Length must be numeric.")

    def test_init_exception_raised_for_non_integer_width(self):
        with self.assertRaises(ValueError) as context:
            Rectangle("Blue", 10, "fiveteen")
        self.assertEqual(str(context.exception), "Width must be numeric.")     

    def test_str_returns_expected_string(self):
        expected = (
            "The shape color is Blue.\n"
            " This rectangle has four sides with the lengths of 10, 15, 10 and 15 centimeters."
        )
        self.assertEqual(str(self.rectangle), expected)
    
    def test_calculate_area_returns_expected_value(self):
        self.assertEqual(self.rectangle.calculate_area(), 150)
    
    def test_calculate_perimeter_returns_expected_value(self):
        self.assertEqual(self.rectangle.calculate_perimeter(), 50)