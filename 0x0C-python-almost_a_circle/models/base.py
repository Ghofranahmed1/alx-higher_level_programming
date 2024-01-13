#!/usr/bin/python3
"""Base class"""


class Base():

    __nb_objects = 0
    """ private class attribute"""

    def __init__(self, id=None):
        if not id == None:
            self.id = id
        else:
           Base.__nb_objects += 1
           self.id = Base.__nb_objects

