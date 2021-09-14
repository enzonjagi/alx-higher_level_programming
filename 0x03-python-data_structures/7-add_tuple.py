#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    item1 = 0
    item2 = 0
    if (len(tuple_a) >= 2) and (len(tuple_b) >= 2):
        item1, item2 = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1])
    elif (len(tuple_a) < 2):
        if (len(tuple_a) == 0):
            item1, item2 = (0 + tuple_b[0]), (0 + tuple_b[1])
        else:
            item1, item2 = (tuple_a[0] + tuple_b[0]), (0 + tuple_b[1])
    elif (len(tuple_b) < 2):
        if len(tuple_b) == 0:
            item1, item2 = (tuple_a[0] + 0), (tuple_a[1] + 0)
        else:
            item1, item2 = (tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0)
    else:
        item1, item2 = 0, 0
    tuple_c = item1, item2
    return tuple_c
