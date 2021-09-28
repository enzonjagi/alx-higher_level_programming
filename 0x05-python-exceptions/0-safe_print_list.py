#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    b = x
    c = 0
    try:
        for i in my_list:
            if (i <= b):
                print("{}".format(i), end="")
            c += 1
        print("")
    except IndexError:
        print("")
    finally:
        if (b > c):
            return (c)
        return (b)
