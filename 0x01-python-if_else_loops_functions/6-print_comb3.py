#!/usr/bin/python3
for digit in range(0, 8):
	for duo in range(digit + 1, 10):
		print("{:d}{:d}".format(digit, duo), end=', ')
print("{:d}{:d}".format(digit + 1, duo))
