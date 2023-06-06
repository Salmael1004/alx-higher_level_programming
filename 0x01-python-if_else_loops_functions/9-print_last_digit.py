#!/usr/bin/python3
def print_last_digit(digit):
	last_digit = abs(digit) % 10
	print(f"{last_digit}", end='')
	return last_digit
