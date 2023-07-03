#!/usr/bin/python3
"""
Create Rectangle.
"""


class Rectangle:
    """Define rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle."""
        return cls(size, size)

    @staticmethod
    def compare_area(rect_1, rect_2):
        """Compare areas of two rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return None

    def __init__(self, width=0, height=0):
        """Initialize data"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Prints a string if deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Print rectangle."""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for _ in range(self.__height))
        return string

    def __repr__(self):
        """Return string representation of the rectangle."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
