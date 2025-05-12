#!/usr/bin/env python

"""
input:
3
0 0 3 0 1 1 2 -1
0 0 3 0 3 1 3 -1
0 0 3 0 3 -2 5 0

output:
1
1
0
"""

import sys

EPS = 1e-9

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def check_ccw(p0, p1, p2):
    # flag = float('inf')
    a, b = p1 - p0, p2 - p0
    if cross(a, b) > EPS:
        # print('COUNTER_CLOCKWISE')
        flag = 1
    elif cross(a, b) < -1 * EPS:
        # print('CLOCKWISE')
        flag = -1
    elif dot(a, b) < -1 * EPS:
        # print('ONLINE_BACK')
        flag = 2
    elif abs(a) < abs(b):
        # print('ONLINE_FRONT')
        flag = -2
    else:
        # print('ON_SEGMENT')
        flag = 0
    return flag

def check_intersection(_lines):
    for line in _lines:
        line = tuple(map(int, line))
        p0, p1, p2, p3 = (x + y * 1j for x, y in zip(line[::2], line[1::2]))
        flag = (check_ccw(p0, p1, p2) * check_ccw(p0, p1, p3) <= 0) and \
               (check_ccw(p2, p3, p0) * check_ccw(p2, p3, p1) <= 0)

        if flag:
            print('1')
        else:
            print('0')

    return None

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    l_num = int(_input[0])
    lines = map(lambda x: x.split(), _input[1:])

    check_intersection(lines)