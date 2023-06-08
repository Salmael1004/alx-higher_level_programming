#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    kard = dir()
    for i in range(0, len(kard)):
        if kard[i][0:2] != "__":
            print("{}".format(kard[i]))
