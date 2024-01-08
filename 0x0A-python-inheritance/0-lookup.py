#!/usr/bin/python3
"""Class named lookup return information about object"""


def lookup(obj):
    """
    Arguments:
        obj: object i want it's information
    Returns the list of available attributes and methods of an object
    """
    return dir(obj)
