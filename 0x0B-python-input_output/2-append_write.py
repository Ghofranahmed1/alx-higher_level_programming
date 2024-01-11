#!/usr/bin/python3
"""function thar append to a file"""


def append_write(filename="", text=""):
    """
    appends text to a file (UTF8) and returns the number of characters addended.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, mode='a', encoding='UTF-8') as f:
        return f.write(text)

