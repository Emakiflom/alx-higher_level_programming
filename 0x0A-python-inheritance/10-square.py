#!/usr/bin/python3
"""Defines a Rectangle subclass Square for this proect."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square class defnition."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
