#!/usr/bin/python3
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return Python object that representation of a JSON string."""
    return json.loads(my_str)
