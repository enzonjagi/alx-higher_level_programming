#!/usr/bin/python3
"""
module to check if object is an instance of a class
or its subclass
"""


def is_kind_of_class(obj, a_class):
    """
    Implementation of the isinstance()
    return: True or False
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
