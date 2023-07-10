#!/usr/bin/python3
"""
Return Only sub class of a class
"""


def inherits_from(obj, a_class):
    """return True if an object is an instance of a class
    that inherited from"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
