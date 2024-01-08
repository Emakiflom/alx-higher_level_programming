#!/usr/bin/python3
"""Defines a class MyInt that inherits from int ofr this proect."""


class MyInt(int):
    """Invert int operators == and != on command."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
