#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length = len(my_list)
    lsCopy = []
    lsCopy = my_list[:]
    # check idx value
    if (idx < 0) or (idx > length):
        return lsCopy
    else:
        my_list[idx] = element
        return my_list
