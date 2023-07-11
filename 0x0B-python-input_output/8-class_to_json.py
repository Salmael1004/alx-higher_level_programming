#!/usr/bin/python3
"""Contains "class_to_json" function"""


def class_to_json(obj):
    """Serializes an object"""
    return obj.__dict__
