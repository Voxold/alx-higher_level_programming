#!/usr/bin/python3
"""models/base.py"""
import json
from turtle import * 


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """function that returns the JSON representation
        of an object (string)"""
        if list_dictionaries is None:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """function that writes an Object to a text file,
        using a JSON representation"""
        filename = cls.__name__ + ".json"
        new_list = []
        if list_objs:
            for i in list_objs:
                json_dict = cls.to_dictionary(i)
                new_list.append(json_dict)
        js_str = cls.to_json_string(new_list)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(js_str)

    @staticmethod
    def from_json_string(json_string):
        """function that writes an Object to a text file,
        using a JSON representation"""

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """function that writes an Object to a text file,
        using a JSON representation"""
        instance = None
        if cls.__name__ == "Rectangle":
            instance = cls(1, 1)
        else:
            instance = cls(1)
        instance.update(**dictionary)

        return instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        new_list = []
        try:
            with open(filename, "r", encoding='utf-8') as file:
                json_load = cls.from_json_string(file.read())
                for item in json_load:
                    new_list.append(cls.create(**item))
                return new_list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        bgcolor("black")
        hideturtle()
        for rec1 in list_rectangles:
            rec = rec1
            color('red', '#19ee69')
            speed(1)
            penup()
            if rec.x != 0:
                setx(rec.x)
            if rec.y != 0:
                sety(rec.y)
            pendown()
            begin_fill()
            for i in range(2):
                fd(rec.width)
                lt(90)
                fd(rec.height)
                lt(90)
            end_fill()
        for sq1 in list_squares:
            sq = sq1
            speed(1)
            color('red')
            penup()
            if sq.x != 0:
                setx(sq.x)
            if sq.y != 0:
                sety(sq.y)
            pendown()
            for i in range(4):
                fd(sq.size)
                lt(90)
