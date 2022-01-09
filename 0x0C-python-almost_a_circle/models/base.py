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
            list_dictionaries = "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list
        The list contains the string repr of json_string
        """
        # checks if the json string is empty or None
        # then returns an empty list
        if json_string is None or len(json_string) == 0:
            return []
        # else it'll just return the string repr of
        # json_string
        return json.loads(json_string)

    @staticmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        """
        filename = "{}.json".format(cls.__name__)
        empty = []
        if list_objs is not None:
            for i in list_objs:
                empty.append(cls.to_dictionary(i))
        # calling the to_json method and
        # writing the JSON to a file
        with open(filename, mode='w') as f:
            f.write(cls.to_json_string(empty))

    @classmethod
    def create(cls, **dictionary):
        """that returns an instance with all attributes already set:
        **dictionary can be thought of as a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            mk = cls(1,1)
        elif cls.__name__ == "Square":
            mk = cls(1)
        mk.update(**dictionary)
        return mk

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
