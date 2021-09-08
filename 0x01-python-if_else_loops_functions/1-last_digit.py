#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# find last digit
if number == 0:
    x = 0
elif number < 0:
    x = abs(number) % 10
    x = -abs(x)
else:
    x = number % 10
# print message based on the last digit
if x > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, x))
elif x == 0:
    print("Last digit of {} is {} and is 0".format(number, x))
elif (x > 0) and (x < 6):
    print(
        "Last digit of {} is {} and is less than 6 and not 0".format(
            number, x))
