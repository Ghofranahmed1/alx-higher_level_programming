#!/usr/bin/python3
"""class  that defines a rectangle
"""


class Rectangle:
    """
    At this stage the class only creates private instance attributes
    Args:
        width (int): horizontal dimension of rectangle, defaults to 0
        height (int): vertical dimension of rectangle, defaults to 0
        """
    """ A class variable, counting the number of rectanglers"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
        # i can use self.__class__.number_of_instances += 1

    @property
    def width(self):
        """__width getter. so i can call the vaiable
           and when we use this method th get or set a vaiable
           we use private variable __width

        Returns:
            __width (int): horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): horizontal dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): vertical dimension of rectangle

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): vertical dimension of rectangle

        Attributes:
            __height (int): vertical dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """
        Public instance method that returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
         should print the rectangle with the character #
         which creates a string
        representation of the rectangle suitable for printing.
        """
        rec = ''
        if self.__height == 0 or self.__width == 0:
            return rec
        for i in range(self.__height):
            for j in range(self.__width):
                rec += '#'
            if (i < (self.__height - 1)):
                rec += '\n'
        return (rec)

    def __repr__(self):
        """
        Allows use of eval().

        Returns:
            A string of the code needed to create the insta
        """
        return ":Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    # need to convrt it from classtatic into classmethod
    def __del__(cls):
        """
        no need to self parameter
        "Prints message upon deletion of instance."""
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the area of two instances and returns the larger of the two.

        Args:
            rect_1 (Rectangle object): first instance to be compared
            rect_2 (Rectangle object): second instance to be compared

        Raises:
            TypeError: if `rect_1` or `rect_2` is not an instance of cls.

        Returns:
            `rect_1` if `rect_1` has an area larger than or equal to `rect_2`,
        or `rect_2` if it has the larger area

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
