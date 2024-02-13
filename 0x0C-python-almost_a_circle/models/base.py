#!/usr/bin/python3
"""module contains a class Base"""
import json
from turtle import Turtle, Screen


class Base:
    """This is the base class for all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:

            self.id = id

        else:

            Base.__nb_objects += 1

            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """serialization (conversion of python data structure 2 json string)"""
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to file """
        if list_objs is None:
            return "[]"

        class_name = cls.__name__

        file_name = "{}.json".format(class_name)

        list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(file_name, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Deserialization"""
        if not json_string or json_string is None:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates a file"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 2)

        elif cls.__name__ == "Square":
            dummy_instance = cls(1)

        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)

        return dummy_instance

        obj = Rectangle(2, 5, 2)
        obj.cls.update()

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a JSON file."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, "r") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        list_instances = [cls.create(**item) for item in list_dicts]
        return list_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draws all rectangles and squares"""
        turtle = Turtle()  # creating an instance of the Turtle class

        my_screen = Screen()  # instance of d screen class to pull up a window

        turtle.screen.bgcolor("coral")
        turtle.pensize(3)
        turtle.shape("turtle")
        turtle.color("#ffffff")

        for rect in list_rectangles:
            turtle.showturtle()
            turtle.up()
            turtle.goto(rect.x, rect.y)
            turtle.down()
            for i in range(2):
                turtle.forward(rect.width)
                turtle.left(90)
                turtle.forward(rect.height)
                turtle.left(90)
                turtle.hideturtle()

        turtle.color("#b5e3d8")
        for sq in list_squares:
            turtle.showturtle()
            turtle.up()
            turtle.goto(sq.x, sq.y)
            turtle.down()
            for i in range(2):
                turtle.forward(sq.width)
                turtle.left(90)
                turtle.forward(sq.height)
                turtle.left(90)
            turtle.hideturtle()

        my_screen.exitonclick()
