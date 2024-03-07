#!/usr/bin/python3
""" square inheriting from rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square inheriting form a rectangle """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ returns the area of the square """
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
