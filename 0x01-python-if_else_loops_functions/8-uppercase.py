#!/usr/bin/python3
def uppercase(c):
    for i in c:
        if (ord(i) >= 97) and (ord(i) <= 122):
            print("{}".format(chr(ord(i) - 32)), end="")
        else:
            print("{}".format(i), end="")
    print("")
