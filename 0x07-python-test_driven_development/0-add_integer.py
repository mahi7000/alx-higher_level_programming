#!/usr/bin/python3
""" adds 2 integers """


def add_integer(a, b=98):
    """ Add function """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
