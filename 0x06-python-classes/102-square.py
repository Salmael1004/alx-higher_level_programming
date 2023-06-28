#!/usr/bin/python3

""" Create Square """


class Square:
    """ Define square """

    def __init__(self, size=0):
        """Initiate data
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """ Set square size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Square area """
        return (self.__size * self.__size)

    def __eq__(self, other):
        """ Define == Square """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Define != Square """
        return self.area() != other.area()

    def __lt__(self, other):
        """ Define < Square """
        return self.area() < other.area()

    def __le__(self, other):
        """ Define <= Square """
        return self.area() <= other.area()

    def __gt__(self, other):
        """ Define > Square """
        return self.area() > other.area()

    def __ge__(self, other):
        """ Define >= Square """
        return self.area() >= other.area()
