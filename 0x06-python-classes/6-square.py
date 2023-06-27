#!/usr/bin/python3
""" Create square """


class Square:
    """ Define square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initiate """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ size of square """
        return self.__size

    @size.setter
    def size(self, value):
        """ size value """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Position value """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ square area """
        return self.__size ** 2

    def my_print(self):
        """ Print square to stdout """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
