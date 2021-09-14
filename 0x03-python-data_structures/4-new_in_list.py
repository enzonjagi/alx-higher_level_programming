#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # rethink
    length = len(my_list)
    copyL = my_list[:]
    if (idx < 0) or (idx >= (length)):
        return my_list
    else:
        copyL[idx] = element
        return copyL
