#!/usr/bin/python3
"""
This module contains:
a script that adds all arguments to a Python list,
and then save them to a file:
"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


empty_list = []
output_list = []
# Add the arguments to the list
for i in range(1, len(sys.argv)):
    empty_list.append(sys.argv[i])
# checking if the list is populated
# print(empty_list)
# TODO Work on case where items are added one at a time
# TIP: Save the current list somewhere and display that
# Saving to JSON File
my_file = "add_item.json"
save_to_json_file(empty_list, my_file)

# Load from JSON file
output_list = load_from_json_file(my_file)
