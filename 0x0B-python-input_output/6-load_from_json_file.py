#!/usr/bin/python3
"""task 6-load_from_json
    function creates a Python object from a JSON file"""

import json


def load_from_json_file(filename):
    """creates a Python obj from JSON file"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
