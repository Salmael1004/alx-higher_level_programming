#!/usr/bin/python3
def magic_calculation(a, b):
    zb1 = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            zb1 += a ** b / i
        except Exception:
            zb1 = b + a
            break
    return zb1
