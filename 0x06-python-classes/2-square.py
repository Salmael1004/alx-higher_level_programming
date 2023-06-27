#!/usr/bin/python3
""" Create a square """


class Square:
    """ Define a square """
    def __init__(self, size=0):
        """ Initialize data
        Args: size=0
         """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
