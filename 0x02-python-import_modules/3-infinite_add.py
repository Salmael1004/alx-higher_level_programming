#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    dice = 0
    for i in range(len(sys.argv) - 1):
	    dice += int(sys.argv[i + 1])
    print("{}".format(dice))
