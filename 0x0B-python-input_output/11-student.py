#!/usr/bin/python3
"""
A module containing:
a class Student that defines a student
"""


class Student:
    """
    a class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Class attribute instantiation
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves
        a dictionary representation of a Student instance
        """

        this_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in attrs:
                try:

                    this_dict[i] = self.__dict__[i]
                except:  # catch the keyword error
                    pass
            return this_dict

    def reload_from_json(self, json):
        """
        A function that replaces all attributes of Student instance
        """

        