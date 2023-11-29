#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number)
    n = num % 10
    print(n, end='')
    return n
