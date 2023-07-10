#!/usr/bin/python3
"""creating a function that adds new attributes to an object"""


def add_attribute(self, attribute, value):
    """Add attribute if it's possible."""
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
