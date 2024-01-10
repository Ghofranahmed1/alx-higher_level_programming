#!/usr/bin/python3
"""Import inherted from class"""
Rectangle = __import__('9-rectangle').Rectangle
""" Square claa"""


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] <width>/<height>".format(self.__size, self.__size)
