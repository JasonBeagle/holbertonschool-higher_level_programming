#!/usr/bin/python3
""" defines the class square"""


class Square:
    """represents a square"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):  # retrieves squares size
        return self.__size

    @size.setter
    def size(self, value):  # change squares size
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """prints square to stdout w/ character #"""
        if self.__size == 0:
            print("")
        for row in range(self.__size):
            for elem in range(self.__size):
                print("#", end="")
            print("")
