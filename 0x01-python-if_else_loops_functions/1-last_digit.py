#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    number *= -1
    n = number % 10
    n *= -1
    number *= -1
else:
    n = number % 10

if n == 0:
    print(f"Last digit of {number} is 0 and is 0")
elif n > 5:
    print(f"Last digit of {number} is {n} and is greater than 5")
else:
    print(f"Last digit of {number} is {n} and is less than 6 and not 0")
