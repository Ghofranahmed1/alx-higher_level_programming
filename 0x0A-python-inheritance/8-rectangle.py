#!/usr/bin/python3

"""Import inherted from class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class inherted"""


class Rectangle(BaseGeometry):
    """Instantiation with width and height"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height