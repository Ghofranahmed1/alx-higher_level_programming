#!/usr/bin/python3
""" creat a square class"""


class square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    attribute:
        size: size of a square(1 side).
        """

    def __init__(self, size=0):
        """
        creat new instance of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
