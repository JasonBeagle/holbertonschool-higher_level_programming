#!/usr/bin/python3
"""task 7-base_geometry
    creates an empty class BaseGeometry with
    instance def area(self), raises exception: area() is not implemented
    instance def integer_validator(self, name, value) and
    raise type and values errors accordingly"""


class BaseGeometry:
    """empty class:
        BaseGeometry"""

    def area(self):
        """public instance method area,
            or raise exception"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """public instance method for validating value
            return TypeError if not given int
            return ValueError if not positive"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
