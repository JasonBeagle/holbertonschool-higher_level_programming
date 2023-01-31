#!/usr/bin/python3
"""task 10-square
    creates class Square that inherits
        from subclass Rectangle
    also initializes size and implents area method"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """creates class Square
        inherits from subclass Rectangle"""

    def __init__(self, size):
        """instantiation of size"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """returns name of subclass"""

        return super().__str__()

    def area(self):
        """area of Square
            dimension given squared"""

        return self.__size ** 2
