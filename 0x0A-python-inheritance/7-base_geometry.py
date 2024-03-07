#!/usr/bin/python3
""" Base Geometry class """


class BaseGeometry:
    """ Base geometry class parent class """
    def area(self):
        """ the area of the geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (type(value) is not int):
            raise TypeError(name + " must be an integer")
        elif (value <= 0):
            raise ValueError(name + " must be greater than 0")
