#!/usr/bin/python3

"""Class is_same_class """


def is_same_class(obj, a_class):
    """
    Function return true if the object is an instance of the specified class
     otherwise False.
     Arguments:
        obj: object
        a_class: name of class
    """
    return type(obj) is a_class
