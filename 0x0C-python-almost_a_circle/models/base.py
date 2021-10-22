#!/usr/bin/python3
'''
This module contains the "base" class of all classes
in the project.
The goal is to manage the id attribute and DRY
'''


import json


class Base:
    '''
    the "base" class of all classes
    in the project.
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Instantiation of id based off certain values
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)


if __name__ == '__main__':
    from base import Base
    from rectangle import Rectangle
    r1 = Rectangle(10, 7, 2, 8)
    dictionary = r1.to_dictionary()
    json_dictionary = Base.to_json_string([dictionary])
    print(dictionary)
    print(type(dictionary))
    print(json_dictionary)
    print(type(json_dictionary))
