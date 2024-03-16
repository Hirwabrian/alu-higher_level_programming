#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """Return the json representation of a string object."""
    return json.dumps(my_obj)
