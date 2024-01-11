#!/usr/bin/python3
""" function that writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON
    Args:
        my_obj: object need to written inside the file
        filename: file object 
    Returns:
        Nothinh
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
