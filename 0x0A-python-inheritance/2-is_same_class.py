#!/usr/bin/python3
"""Defines a class-checking function instance of a_class ."""


def is_same_class(obj, a_class):
    """Check if an object is exactly as instance of a given class.

    Args:
        obj (any): The object to be check.
        a_class (type): The class to match the type of obj for check.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
