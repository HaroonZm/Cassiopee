#!/usr/bin/env python

"""
input:
0 0 2 0
3
-1 0
0 0
3 0

output:
ONLINE_BACK
ON_SEGMENT
ONLINE_FRONT
"""

import sys

EPS = 1e-9

def cross(a, b):
    return a.real * b.imag - a.imag * b.real

def dot(a, b):
    return a.real * b.real + a.imag * b.imag

def calc_distance(p_info):
    for point in p_info:
        p2_real, p2_imag = map(int, point)
        p2 = p2_real + p2_imag * 1j
        a = p1 - p0
        b = p2 - p0
        if cross(a, b) > EPS:
            print('COUNTER_CLOCKWISE')
        elif cross(a, b) < -EPS:
            print('CLOCKWISE')
        elif dot(a, b) < -EPS:
            print('ONLINE_BACK')
        elif abs(a) < abs(b):
            print('ONLINE_FRONT')
        else:
            print('ON_SEGMENT')
    return None

if __name__ == '__main__':
    _input = sys.stdin.readlines()
    base_line = tuple(map(int, _input[0].split()))
    p0, p1 = (x + y * 1j for x, y in zip(base_line[::2], base_line[1::2]))

    q_num = int(_input[1])
    q_list = map(lambda x: x.split(), _input[2:])
    calc_distance(q_list)