"""This module defines the Rectangle class."""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"

from shape.shape import Shape

class Rectangle(Shape):
    """
      A class that represent a rectangle shape
    """
    def __init__(self,color:str, length:int, width:int):
        """
        Initializes a Rectangle instance with the specified color, length and width.
        
        Attributes:
            color(str): The color of the rectangle
            length(int): The length of the rectangle
            width(int): The width of the rectangle

        Raises:
            ValueError: 
                If the color is not a string
                If length is not an integer
                If width is not an integer
        """
        super().__init__(color)
       
        if not isinstance(length, int):
            raise ValueError("Length must be numeric.")

        if not isinstance(width, int):
            raise ValueError("Width must be numeric.")
        
        self.__length = length
        self.__width = width

    def __str__(self) -> str:
        """
        Returns a string representation of the Rectangle instance.

        Returns:
            str: A string describing the rectangle's color, length and width.
        """
        return f"The shape color is {self.color}.\n This rectangle has four sides with the lengths of {self.__length}, {self.__width}, {self.__length} and {self.__width} centimeters."
        
    def calculate_area(self) -> float:
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        area = self.__length * self.__width
        return area
    
    def calculate_perimeter(self) -> float:
        """
        Calculates the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        perimeter = 2 * (self.__length) + 2 * (self.__width)
        return perimeter
