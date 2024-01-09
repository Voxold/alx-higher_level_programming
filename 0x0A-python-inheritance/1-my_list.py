#!/usr/bin/python3
"""MyList calss"""


class MyList(list):
    """class MyList that inherits from list"""

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
