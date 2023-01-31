#!/usr/bin/python3
"""task - 1, create a class MyList
    which inherits from list, and contains
    one public instance, print_sorted(self)"""


class MyList(list):
    """class MyList inherits from list
        public instance method:
        def print_sorted(self)"""
    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
