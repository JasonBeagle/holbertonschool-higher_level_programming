#!/usr/bin/python3
'''prints a square with the # character'''


def print_square(size):
    if size == 0:
        return
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print('\n'.join('#' * size for x in range(size)))
