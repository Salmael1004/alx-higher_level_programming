#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        zb1 = add(a, b)
        for i in range(4, 6):
            zb1 = add(zb1, i)
        return zb1
    else:
        return sub(a, b)
