#!/usr/bin/python3
"""Open and Read files"""


def read_file(filename=""):
	"""function that reads a text file (UTF8) and prints it to stdout"""
	with open(filename, encoding= 'UTF-8') as f:
		print(f.read(), end="")

