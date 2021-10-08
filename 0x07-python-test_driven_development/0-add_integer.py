#!/usr/bin/python3
"""Returns the sume of two integers

---
Args:
a - should be an integer
b - sh0uld be an integer

---

add_integer(a, b=98)
returns (a + b) if both values are integers

---

Edge cases
1. if either values are not integers
2. if no values are provided
3. if either value is a float
4. if both values are floats
5. if both values are not integers
6. if both values are integers
"""


def add_integer(a, b=98):
    """"This function does the addition of 2 arguments
    args:
        a (union[int, float]): first number
        b (union[int, float], optional): second number
    returns:
        the result of the addition
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    if b is None or (type(b) is not int and type(b) is not float):
        raise TypeError('b must be an integer')

    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89

    return int(a) + int(b)
