#!/usr/bin/python3
from sys import argv
dice = 0
for s in argv[1:]:
    dice += int(s)
print("{:d}".format(dice))
