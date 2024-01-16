#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base

class Rectangle(Base):
    """Class initilaize a rectangle"""

    def __init__(self, width, height, x = 0, y = 0, id=None):
        """calss constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width_getter(self):
        return self.__width
    @width.setter
    def width(self, value):
        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height_getter(self):
        return self.__height

    @property
    def x_getter(self):
        return self.__x

    @property
    def y_getter(self):
        return self.__y

    @height.srtter
    def height(self, value):
        self.validate_int('height', value, False)
        self.__height = value

    @x.srtter
    def x(self, value):
        self.validate_int('x', value)
        self.__x = value

    @y.srtter
    def y(self, value):
        self.validate_int('y', value)
        self.__y = value

    def validate_int(self, name, value, eq=True):
        if type(value) != int:
            raise ValueError("{} must be an integer".format(name))
        if eq and value <= 0:
            raise ValueError ("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

