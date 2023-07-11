#!/usr/bin/python3
"""Class defination of student"""


class Student:
    """ Defining a class"""
    def __init__(self, first_name, last_name, age):
        """ Initializing student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ converting to json """
        return self.__dict__
