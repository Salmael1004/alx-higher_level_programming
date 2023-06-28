#!/usr/bin/python3
"""Magic class ByteCode."""
import math


class MagicClass:
    """Initialize  MagicClass."""
    def __init__(self, radius=0):
        """Initialize of the data."""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """Calculate area."""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """Calculate  perimeter."""
        return 2 * math.pi * self._MagicClass__radius
