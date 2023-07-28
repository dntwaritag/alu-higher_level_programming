#!/usr/bin/python3
"""
Module: 1-rectangle

This is the Rectangle module.
It defines a rectangle with private attributes and property getters/setters.
"""


class Rectangle:
    """
    This is the Rectangle class.
    It defines a rectangle with private attributes and property getters/setters.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with the given width and height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter method to retrieve the width attribute.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method to set the width attribute.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method to retrieve the height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method to set the height attribute.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
