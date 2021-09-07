#!/usr/bin/python3
def uppercase(c):
    for i in c:
        print(
            "{}".format(chr(ord(i) - 32))
            if (ord(i) >= 97) and (ord(i) <= 122)
            else "{}".format(i), end="")
    print("")
