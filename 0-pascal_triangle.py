#!/usr/bin/python3

def pascal_triangle(n):
    """ return list of lists of integers in Pascal Triangle Format"""
    initial_list = []

    if n <= 0:
        return initial_list

    for i in range(n):
        print(' '*(num - i), end='')
        print(' '.join(map(str, str(11**i))))


