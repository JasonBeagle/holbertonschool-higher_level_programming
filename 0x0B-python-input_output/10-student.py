#!/usr/bin/python3
"""task 10-student
    creates class Student
        attributes:
            first_name
            last_name
            age
        method:
            def to_json(self)
                retrieves dict representation of Student"""


class Student():
    """creation of class"""

    def __init__(self, first_name, last_name, age):
        """attribute initialization"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dictionary description retrieval"""

        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if hasattr(self, att):
                    dic[att] = getattr(self, att)
            return dic
