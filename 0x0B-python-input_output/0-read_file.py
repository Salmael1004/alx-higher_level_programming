#!/usr/bin/python3
"""function that reads a text file and print it to stdout"""


def read_file(filename=""):
    """reads a text file and print it to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
