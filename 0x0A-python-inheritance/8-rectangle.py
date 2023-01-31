#!/usr/bin/python3
"""task 8 - creates Rectangle subclass
    Rectangle inherits from imported BaseGeometry
    within Rectangle instantiate width and height
        def __init__(self, width, height):
    then validate with integer_validator"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """class Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):

        """validate and initialize width and height"""

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
