#!/usr/bin/python3
for tebahpla in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(tebahpla, chr(tebahpla - 33)), end="")
