#!/usr/bin/python3
""" a module that contains a class rectangle """


class Rectangle:
    """ empty class rectangle """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (not isinstance(value, int)):
            raise TypeError("width must be an integer")
        elif (value < 0):
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (not isinstance(value, int)):
            raise TypeError("height must be an integer")
        elif (value < 0):
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """ returns the rectangle area """
    def area(self):
        return self.height * self.width

    """ returns the rectangle perimeter """
    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        else:
            return (2 * (self.width + self.height))

    def __str__(self):
        if (self.width == 0 or self.height == 0):
            return ""
        rect_str = ""
        for _ in range(self.height):
            if _ == self.height - 1:
                rect_str += "#" * self.width
            else:
                rect_str += "#" * self.width + "\n"
        return rect_str

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        print("Bye rectangle...")
