"""This module defines the Triangle class."""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

from shape.shape import Shape
import math

class Triangle(Shape):
    """
    A class that represent a triangle shape
    """

    def __init__(self,color:str, side_1:int, side_2:int, side_3:int):
        """
        Initializes a Triangle instance with the specified color and side lengths.
        
        Args:
            color(str): The color of the triangle
            side_1(int): The length of the first side of the triangle
            side_2(int): The length of the second side of the triangle
            side_3(int): The length of the third side of the triangle

        Raises:
            ValueError: 
                If the color is not a string
                If side_1 is not an integer
                If side_2 is not an integer
                If side_3 is not an integer
                If the three sides do not satisfy the requirements of the 
                Triangle Inequality Theorem
        """
        super().__init__(color)
       
        if not isinstance(side_1, int):
            raise ValueError("Side 1 must be numeric.")

        if not isinstance(side_2, int):
            raise ValueError("Side 2 must be numeric.")

        if not isinstance(side_3, int):
            raise ValueError("Side 3 must be numeric.")

        if not (side_1 + side_2 > side_3 and side_1 + side_3 > side_2 \
                and side_2 + side_3 > side_1):
            raise ValueError("The sides do not satisfy the Triangle Inequality Theorem.")
        
        self.__side_1 = side_1
        self.__side_2 = side_2
        self.__side_3 = side_3

    def __str__(self) -> str:
        """
        Returns a string representation of the Triangle instance.

        Returns:
            str: A string describing the triangle's color and side lengths.
        """
       
        return (
            f"The shape color is {self.color}.\n"
            f"This triangle has three sides with lengths of "
            f"{self.__side_1}, {self.__side_2} and {self.__side_3} "
            f"centimeters."
        )

    def calculate_area(self):
        """
        Calculates the area of the triangle.

        Returns:
            float: The area of the triangle in square centimeters.
        """
        semi_perimeter = (self.__side_1 + self.__side_2 + self.__side_3) / 2
        area = math.sqrt(semi_perimeter * (semi_perimeter - self.__side_1) * \
                         (semi_perimeter - self.__side_2) * (semi_perimeter - self.__side_3))
        
        return area
    
    def calculate_perimeter(self):
        """
        Calculates the perimeter of the triangle.

        Returns:
            float: The perimeter of the triangle in centimeters.
        """
        perimeter = self.__side_1 + self.__side_2 + self.__side_3
        
        return perimeter
    
