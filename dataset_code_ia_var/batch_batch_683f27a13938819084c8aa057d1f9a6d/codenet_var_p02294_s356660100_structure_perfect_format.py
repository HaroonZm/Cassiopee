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
    a = p1 - p0
    b = p2 - p0
    if cross(a, b) > EPS:
        flag = 1
    elif cross(a, b) < -EPS:
        flag = -1
    elif dot(a, b) < -EPS:
        flag = 2
    elif abs(a) < abs(b):
        flag = -2
    else:
        flag = 0
    return flag

def check_intersection(_lines):
    for line in _lines:
        line = tuple(map(int, line))
        p0 = line[0] + line[1] * 1j
        p1 = line[2] + line[3] * 1j
        p2 = line[4] + line[5] * 1j
        p3 = line[6] + line[7] * 1j
        ccw1 = check_ccw(p0, p1, p2)
        ccw2 = check_ccw(p0, p1, p3)
        ccw3 = check_ccw(p2, p3, p0)
        ccw4 = check_ccw(p2, p3, p1)
        flag = (ccw1 * ccw2 <= 0) and (ccw3 * ccw4 <= 0)
        if flag:
            print('1')
        else:
            print('0')
    return None

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    l_num = int(_input[0])
    lines = map(lambda x: x.strip().split(), _input[1:])
    check_intersection(lines)