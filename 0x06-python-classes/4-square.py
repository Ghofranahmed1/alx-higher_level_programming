#!/usr/bin/python3
"""Define a class square"""


class Square:
    """
    Class that defines properties of square by: (based on 0-square.py).

    Attribute:
        size: size of a square(1 side).
    """
    def __init__(self, size=0):
        """Creats new instance of square.

        Args:
            size: size of square (1 side).
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculation the area of square.

        Return: the current square area.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Return the size of square.
        """
        return self.__size
    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): size of a square (1 side).

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
