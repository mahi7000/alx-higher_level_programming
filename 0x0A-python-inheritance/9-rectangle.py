#!/usr/bin/python3
""" sub class of base geometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle that inherits from BaseGeometry """
    def __init__(self, width, height):
        """ Rectangle initializer """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns area of rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ returns this """
        return f"[Rectangle] {self.__width}/{self.__height}"
