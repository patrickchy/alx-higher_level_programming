#!/usr/bin/python3
"""module contains the rectangle class"""
from models.base import Base


class Rectangle(Base):
    """This defines the rectangle class
        Args:
            width - width of the rectangle
            height - height of the rectangle
            x - x coordinate
            y - y coordinate
            id - the id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """init function of the rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def height(self):
        """property getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter"""
        if not isinstance(value, int):

            raise TypeError("height must be an integer")

        if value <= 0:

            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def width(self):
        """property getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter for width"""
        if not isinstance(value, int):

            raise TypeError("width must be an integer")

        if value <= 0:

            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:

            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):

            raise TypeError("y must be an integer")

        if value < 0:

            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """calculates area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle with # character"""
        for row in range(self.y):
            print()
        for col in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for symbol in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ This method assigns an argument to each attribute """
        if args:
            for arguments in range(len(args)):
                if arguments == 0:
                    self.id = args[arguments]
                if arguments == 1:
                    self.__width = args[arguments]
                if arguments == 2:
                    self.__height = args[arguments]
                if arguments == 3:
                    self.__x = args[arguments]
                if arguments == 4:
                    self.__y = args[arguments]

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionatry representation"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width
        }
