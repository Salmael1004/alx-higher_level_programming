#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        zb1 = a / b
    except (ZeroDivisionError, TypeError):
        zb1 = None
    finally:
        print("Inside result: {}".format(zb1))
        return zb1
