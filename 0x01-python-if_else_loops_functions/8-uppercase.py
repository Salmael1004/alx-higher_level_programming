#!/usr/bin/python3
def uppercase(str):
    for z in str:
        if ord(z) >= ord('a') and ord(z) <= ord('z'):
            char = chr(ord(z) - 32)
        else:
            char = z
        print("{:s}".format(char), end="")
    print('')
