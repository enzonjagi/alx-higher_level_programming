#!/usr/bin/python3
"""
This module contains a function that
Reads a text file,
Prints it out to stdout
"""

def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line)

if __name__ == '__main__':
    read_file("my_file_0.txt")