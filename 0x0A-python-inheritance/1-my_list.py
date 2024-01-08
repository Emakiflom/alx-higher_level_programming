#!/usr/bin/python3
"""
contains the MyList class in the first
"""


class MyList(list):
    """a subclass of list in this project"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
