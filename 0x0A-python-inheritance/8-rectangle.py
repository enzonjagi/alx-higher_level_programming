#!/usr/bin/python3
"""
This module series contains a class and some inheritance
"""


class BaseGeometry:
    """
    A class containing a number of methods:
    area() throws an Exception
    integer_validator() validates that a value is of type int
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is an int
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must greater than 0".format(name))
        else:
            return value


class Rectangle(BaseGeometry):
    """
    Class that is a subclass if the BaseGeometry class
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def integer_validator(self, value):

        self.__width = BaseGeometry.integer_validator("width", self.__width)
        self.__height = BaseGeometry.integer_validator("height", self.__height)
