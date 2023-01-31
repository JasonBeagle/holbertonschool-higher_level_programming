#!/usr/bin/python3
"""task 0-read_file
    reads a text file and prints to stdout"""


def read_file(filename=""):
    """reading file"""
    with open(filename, encoding='utf-8') as f:
        read_words = f.read()
        print(read_words)
