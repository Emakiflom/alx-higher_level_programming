#!/usr/bin/python3
"""Defines class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent this rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle for the first time.

        Args:
            width (int): The width of the new Rectangle argument.
            height (int): The height of the new Rectangle argument.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
