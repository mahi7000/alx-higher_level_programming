#!/usr/bin/python3
""" Divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Divides elements in matrix with div """
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for row in matrix:
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError(
                "Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(row, list) or
            (not isinstance(i, int) and not isinstance(i, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
    return [[round(i / div, 2) for i in row] for row in matrix]
