#!/usr/bin/python3

def remove_char_at(string, index):
    if index < 0 or index >= len(string):
        return string
    return string[:index] + string[index+1:]
