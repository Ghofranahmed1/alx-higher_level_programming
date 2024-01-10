#!/usr/bin/python3
"""Import class inherted from"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Class inherteed"""


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Method to redefine a area method in the parent class"""

        return self.__width * self.__height
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
