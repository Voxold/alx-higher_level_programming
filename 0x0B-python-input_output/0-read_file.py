#!/usr/bin/python3
"""read_file function"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout:"""

    with open(filename, 'r', encoding='utf-8') as file:
        read_f = file.read()
    print(read_f, end="")
