#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        x = (-(number)) % 10
        print("{}".format(x), end="")
    elif number == 0:
        x = 0
        print("{}".format(x), end="")
    else:
        x = number % 10
        print("{}".format(x), end="")
    return x
