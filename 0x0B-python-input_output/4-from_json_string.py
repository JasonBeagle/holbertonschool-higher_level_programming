#!/usr/bin/python3
"""task 4-from_json_string
    returns a JSON representation of a object (python data structure)"""

import json


def from_json_string(my_str):
    """returns object represented by a JSON string"""

    return json.loads(my_str)
