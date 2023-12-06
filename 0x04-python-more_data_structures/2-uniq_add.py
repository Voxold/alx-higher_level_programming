#!/usr/bin/python3
def uniq_add(my_list=[]):
    set1 = set(my_list)
    sum = 0
    len1 = len(set1)
    while (len1):
        sum += (set1.pop())
        len1 = len1 - 1
    return sum
