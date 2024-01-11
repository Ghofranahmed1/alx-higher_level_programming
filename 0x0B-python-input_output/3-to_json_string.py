#!/usr/bin/python3
import json
"""function returns the JSON representation"""


def to_json_string(my_obj):
	"""
	function that returns the JSON representation of an object
	Args: 
	    my_obj: the object need to convert
	Returns:
	    converted data
	"""
	return json.dumps(my_obj)
