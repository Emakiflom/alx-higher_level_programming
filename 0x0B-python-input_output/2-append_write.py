#!/usr/bin/python3
"""Defines a file-appending function UTF8 text file."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.


    Args:
        filename (str): The name of the file to append to as arg.
        text (str): The string to append to the file as arg.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
