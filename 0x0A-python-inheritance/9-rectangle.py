#!/usr/bin/python3
"""task 9 - creates Rectangle subclass
    Rectangle inherits from imported BaseGeometry
    within Rectangle instantiate width and height
        def __init__(self, width, height):
        then validate with integer_validator
    also implements area method
        def area(self)
    prints area along with name and dimensions"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):

        """validate and initialize width and height"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):

        """implementation of area method"""

        return self.__width * self.__height

    def __str__(self):

        """prints [Rectangle] <width>/<height>"""

        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                         self.__width, self.__height)
