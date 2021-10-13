#!/usr/bin/python3
"""
This module contains a function that
Opens a text file,
Overwrites it
"""


def write_file(filename="", text=""):
    """
    Executing the purpose of this module:
    Write to a text file(overwrite)
    """

    with open(filename, mode='w', encoding='utf-8') as f:
        write_data = f.write(text)
    return write_data
