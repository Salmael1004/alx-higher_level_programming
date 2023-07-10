#!/usr/bin/python3
""" Creating Mylist class """


class MyList(list):
    """
    MyList class
    """
    def print_sorted(self):
        """Prints the list in sorted order.
        """
        print(sorted(self))
