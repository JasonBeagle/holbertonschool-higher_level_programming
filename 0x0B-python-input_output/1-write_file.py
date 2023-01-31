#!/usr/bin/python3
"""task 1-write_file
    writes a string to a file and returns char count"""


def write_file(filename="", text=""):
    """filename and string to concatenate within"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return(f.write(text))
