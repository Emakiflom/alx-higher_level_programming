#!/usr/bin/python3
"""Defines the string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return JSON representation of a string object just for json."""
    return json.dumps(my_obj)
