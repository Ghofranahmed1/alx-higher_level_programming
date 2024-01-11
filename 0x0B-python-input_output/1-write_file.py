#!/usr/bin/python3
"""i/o operation"""


def write_file(filename="", text=""):
	"""function that writes  to a text file (UTF8)
	and returns the number of characters written"""
    with open(filename, mode='w', encoding='UTF-8') as f:
	return f.write(text)
