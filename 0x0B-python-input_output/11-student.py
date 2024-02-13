#!/usr/bin/python3
"""Student Class"""


class Student:
    """class Student that defines a student by"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (attrs is None):
            return (self.__dict__)
        dic = dict()
        for ele in attrs:
            for key in self.__dict__:
                if (ele == key):
                    dic[ele] = self.__dict__[key]
        return (dic)

    def reload_from_json(self, json):
        for ele in self.__dict__:
            for key in json:
                if (ele == key):
                    self.__dict__[key] = json[key]
