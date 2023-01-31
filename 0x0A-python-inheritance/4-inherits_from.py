#!/usr/bin/python3
"""task 4 - returns True if object is an instance
    that inherits from a specified class, returns False otherwise"""


def inherits_from(obj, a_class):

    """ returns True if obj is instance of class
        that it inherits, directly or indirectly from a class,
        returns false otherwise"""

    return (type(obj) is not a_class and issubclass(type(obj), a_class))
