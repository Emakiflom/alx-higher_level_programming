#!/usr/bin/python3
"""Defines a class & inherited class-checking function instance of a class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or instance of a class.

    Args:
        obj (any): The object to be check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
