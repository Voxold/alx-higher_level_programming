#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    len = len(argv) - 1
    print("{} {}{}".format
          (len, 'argument' if len == 1 else 'arguments',
                '.' if len == 0 else ':'))
    for i in range(1, len + 1):
        print("{}: {}".format(i, argv[i]))
