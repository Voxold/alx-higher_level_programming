#!/usr/bin/python3
"""Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Calss"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")

    def area(self):
        return (self.__size ** 2)
