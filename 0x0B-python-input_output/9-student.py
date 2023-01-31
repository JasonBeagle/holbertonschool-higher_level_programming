#!/usr/bin/python3
"""task 9-student
    creates class Student
        attributes:
            first_name
            last_name
            age
        method:
            def to_json(self)
                retrieves dict representation of Student"""


class Student:
    """creation of class"""

    def __init__(self, first_name, last_name, age):
        """attribute initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """dictionary representation retrieval"""

        return self.__dict__
