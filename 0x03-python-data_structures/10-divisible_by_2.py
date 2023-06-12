#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = my_list.copy()
    for zb1 in range(0, len(my_list)):
        if my_list[zb1] % 2 == 0:
            new[zb1] = 1
        else:
            new[zb1] = 0
    return new
