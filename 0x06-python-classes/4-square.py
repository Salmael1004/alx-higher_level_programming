#!/usr/bin/python3
""" Create a Square """


class Square:
    """ Define a square
    """

    def __init__(self, size=0):
        """ Initiate """
        self.__size = size

    @property
    def size(self):
        """ Get size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set  size value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return square area """
        return self.__size ** 2
