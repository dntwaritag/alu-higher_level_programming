#!/usr/bin/python3
""""
It defines a rectangle with private attributes and public methods for area, perimeter,
and string representation.
"""


class Rectangle:
    """
    This is the Rectangle class.
    It defines a rectangle with private attributes and public methods for area, perimeter,
    and string representation.
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
        set  the width attribute.
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

    def area(self):
        """
        Calculates and returns the rectangle area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the rectangle perimeter.
        If width or height is equal to 0, perimeter is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))
