#!/usr/bin/python3
def fizzbuzz():
    # loop through specified range
    for i in range(1, 101):
        # checks to print Fizz, Buzz, FizzBuzz, or a number
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz", end=" ")
        elif (i % 3 == 0):
            print("Fizz", end=" ")
        elif (i % 5 == 0):
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")
