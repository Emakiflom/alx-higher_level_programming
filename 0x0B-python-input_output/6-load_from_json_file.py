#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from the JSON file in this project."""
    with open(filename) as f:
        return json.load(f)
