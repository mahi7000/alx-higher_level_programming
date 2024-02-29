#!/usr/bin/python3
""" class with instantiation optional and more complicated """


class Square:
    """ inputing size is optional size is checked """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    """ property position """
    @property
    def position(self):
        return self.__position

    """ position setter """
    @position.setter
    def position(self, value):
        if ((not isinstance(value[0], int)) or
            ((not isinstance(value[1], int)) or
                value[1] < 0 or value[0] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """ finds the area of the square """
    def area(self):
        return (self.__size ** 2)

    """ prints the square with # """
    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            k = 0
            while (k < self.__position[1]):
                print()
                k += 1
            i = 0
            while (i < self.__size):
                k = 0
                while (k < self.__position[0]):
                    print(" ", end='')
                    k += 1
                j = 0
                while (j < self.__size):
                    print("#", end='')
                    j += 1
                print()
                i += 1
