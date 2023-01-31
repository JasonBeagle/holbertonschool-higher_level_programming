#!/usr/bin/python3
"""task 2-append_write
    concatenates a string onto the end of a file
    if file doesn't exist it will be created"""


def append_write(filename="", text=""):
    """adds string to end of a file
        if file doesn't exist, create one
        returns char count"""
    with open(filename, "a", encoding="utf-8") as f:
        return(f.write(text))
