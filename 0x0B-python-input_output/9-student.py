#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student with some atribute."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student with fname lname and age.

        Args:
            first_name (str): The first name of the student as string.
            last_name (str): The last name of the student as string.
            age (int): The age of the student as intger .
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
