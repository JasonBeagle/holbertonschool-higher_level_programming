#!/usr/bin/python3
"""task 7-add_item
    adds arguments to Python list and saves in a file"""


import sys
import os.path
import json


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


my_file = "add_item.json"
my_list = []


if os.path.exists(my_file):
    my_list = load_from_json_file(my_file)

for elem in range(1, len(sys.argv)):
    my_list.append(sys.argv[elem])

save_to_json_file(my_list, my_file)
