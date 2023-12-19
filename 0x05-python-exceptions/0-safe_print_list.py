#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    cnt = 0
    try:
        while (x > cnt):
            print(my_list[cnt], end="")
            cnt += 1
    except IndexError:
        print()
        return (cnt)
    print()
    return (cnt)
