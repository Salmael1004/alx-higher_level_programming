#!/usr/bin/python3
"""
Create Rectangle
"""


class Rectangle:
    """Define rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize data"""
        self._width = width
        self._height = height

    @property
    def width(self):
        """Get width"""
        return self._width

    @width.setter
    def width(self, value):
        """Set width"""
        if type(value) is not int:
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get height"""
        return self._height

    @height.setter
    def height(self, value):
        """Set height"""
        if type(value) is not int:
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self._height = value

    def area(self):
        """Return rectangle area"""
        return self._width * self._height

    def perimeter(self):
        """Return rectangle perimeter"""
        return 2 * (self._width + self._height)

    def __str__(self):
        """Print rectangle"""
        if self._width == 0 or self._height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self._height):
            rectangle_str += "#" * self._width + "\n"
        return rectangle_str
