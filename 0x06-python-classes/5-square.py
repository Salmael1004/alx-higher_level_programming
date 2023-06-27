#!/usr/bin/python3
""" Create square """


class Square:
    """ Define square """
    def __init__(self, size=0):
        """ Initialize data
        Args: size=0
         """
        self.__size = size

    @property
    def size(self):
        """ square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set size """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return area result """
        return (self.__size ** 2)

    def my_print(self):
        """ Printing the square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
