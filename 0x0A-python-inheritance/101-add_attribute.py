#!/usr/bin/python3
"""Defines the function, adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add  new attribute to the object if possible.

    Args:
        obj (any): The object that add an attribute.
        att (str): The name of the attribute that add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
