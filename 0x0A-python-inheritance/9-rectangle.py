#!/usr/bin/python3
"""Defines this class Rectangle inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent this rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle for the first time.


        Args:
            width (int): The width of the new Rectangle argument.
            height (int): The height of the new Rectangle argument.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle to the main method"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
