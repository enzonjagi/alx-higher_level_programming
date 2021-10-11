#!/usr/bin/python3
"""
Module contains a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly)from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """
    a function that returns True
    if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class ;
    otherwise False.
    """

    if isinstance(obj, a_class) and not(obj.__class__ == a_class):
        return True
    else:
        return False
