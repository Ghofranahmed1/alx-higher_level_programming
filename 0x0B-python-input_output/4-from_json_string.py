#!/usr/bin/python3
"""function returns the reverse JSON representation"""
import json


def from_json_string(my_str):
    """
    function that returns the reverse JSON representation of an object
    Args:
        my_str: the object need to convert
    Returns:
        converted data
    """
    return json.loads(my_str)
