#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
""" Class inherteed"""


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
