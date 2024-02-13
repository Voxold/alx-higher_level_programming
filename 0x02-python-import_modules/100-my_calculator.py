#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, div, mul, sub
    len = len(argv) - 1
    op = ['+', '-', '/', '*']
    fun = [add, sub, div, mul]
    if len != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        for i in range(4):
            if argv[2] == op[i]:
                print('{} {} {} = {}'.format
                      (argv[1], argv[2], argv[3],
                       fun[i](int(argv[1]), int(argv[3]))))
                exit(0)
