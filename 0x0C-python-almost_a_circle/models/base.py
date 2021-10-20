#!/usr/bin/python3
'''
This module contains the "base" class of all classes
in the project.
The goal is to manage the id attribute and DRY
'''


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
