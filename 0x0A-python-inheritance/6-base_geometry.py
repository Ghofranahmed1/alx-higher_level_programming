#!/usr/bin/python3
""" Empty class"""


class BaseGeometry():
    """one public method"""
    @classmethod
    def area(self):
        raise Exception("area() is not implemented")
