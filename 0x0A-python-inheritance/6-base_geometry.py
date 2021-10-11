#!/usr/bin/python3
"""
This module series contains a class and some inheritance
"""


class BaseGeometry:
    """
    A class containing a method that throws an Exception
    """

    def area(self):
        raise Exception("area() is not implemented")
