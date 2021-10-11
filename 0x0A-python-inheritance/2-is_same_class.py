#!/usr/bin/python3
"""
This module checks has a function checking if
an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """
    Checks if obj isinstance of class
    """

    if not isinstance(obj, a_class):
        return False
    return True
