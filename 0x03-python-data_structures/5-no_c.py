#!/usr/bin/python3
def no_c(my_string):
    new_st = my_string.translate({ord(st): None for st in 'cC'})
    return new_st
