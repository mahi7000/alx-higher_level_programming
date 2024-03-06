#!/usr/bin/python3
""" doctest learning by printing squares """


def print_square(size):
    """ prints a square of size size using # """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    square = ""
    for i in range(size):
        if (i != size - 1):
            square += "#" * size + '\n'
        else:
            square += "#" * size

    print(square)
