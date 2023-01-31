#!/usr/bin/python3
"""task 5-save_to_json
    writes an object to text file using JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """writes object to file using JSON represenation"""

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
