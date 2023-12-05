#!/usr/bin/python3
""" a class based on prev class """


BaseGeometry_7 = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry_7):
    """ a class based on prev class """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
