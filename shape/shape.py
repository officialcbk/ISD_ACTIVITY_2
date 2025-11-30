"""This module defines the Shape class."""

__author__ = "Emmanuel Eze"
__version__ = "1.0.0"


from abc import ABC, abstractmethod

class Shape(ABC):
    """
     A method that represents the shape of an object
    """

    def __init__(self,color:str):
        """
        Initializes a Shape instance with the specified color.
        
        Args:
            color(str): The color of the shape

        Raises:
            ValueError: If the color is not a string
        """

        if len(color.strip()) == 0:
            raise ValueError("Color cannot be blank")
        self._color = color
    
    @property
    def color(self) -> str:
        """
        Returns the color of the shape.

        Returns:
            str: The color of the shape.
        """
        return self._color

    def __str__(self) -> str:
        """
        Returns a string representation of the Shape instance.

        Returns:
            str: A string describing the shape's color.
        """
        return f"The shape color is {self._color}"
    
    @abstractmethod
    def calculate_area(self) -> float:
        """
        Abstract method to calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        """
        Abstract method to calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass





