#!/usr/bin/python3
""" class with instantiation optional and more complicated """


class Square:
    """ inputing size is optional size is checked """
    def __init__(self, size=0):
        self.size = size

    """ size getter """
    @property
    def size(self):
        return self.__size

    """ size setter """
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ finds the area of the square """
    def area(self):
        return (self.__size ** 2)

    """ prints the square with # """
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            i = 0
            while (i < self.__size):
                j = 0
                while (j < self.__size):
                    print("#", end='')
                    j += 1
                print()
                i += 1
