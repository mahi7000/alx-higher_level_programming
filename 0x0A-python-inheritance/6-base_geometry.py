#!/usr/bin/python3
""" Base Geometry class """


class BaseGeometry:
    """ Base geometry class parent class """
    def area(self):
        """ the area of the geometry """
        raise Exception("area() is not implemented")
