#!/usr/bin/python3
"""task 3-class_to_json
    returns a dictionary description for JSON
    serialization of an object"""


def class_to_json(obj):
    """creates a dictionary description of object"""

    return obj.__dict__
