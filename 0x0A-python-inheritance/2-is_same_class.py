#!/usr/bin/python3
"""
Defines a class-checking function.
"""


def is_same_class(obj, a_class):
    """Return true if the object is an instance of a class"""

    return type(obj) is a_class
