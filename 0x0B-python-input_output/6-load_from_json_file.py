#!/usr/bin/python3
"""
Module contains:
a function that creates an Object
from a “JSON file”
"""


import json
from io import StringIO


def load_from_json_file(filename):
    """
    a function that creates an Object
    from a “JSON file”
    """

    with open(filename) as f:
        x = json.load(f)
    return x


if __name__ == '__main__':
    filename = "my_list.json"
    my_list = load_from_json_file(filename)
    print(my_list)
    print(type(my_list))

    filename = "my_dict.json"
    my_dict = load_from_json_file(filename)
    print(my_dict)
    print(type(my_dict))

    try:
        filename = "my_set_doesnt_exist.json"
        my_set = load_from_json_file(filename)
        print(my_set)
        print(type(my_set))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        filename = "my_fake.json"
        my_fake = load_from_json_file(filename)
        print(my_fake)
        print(type(my_fake))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
