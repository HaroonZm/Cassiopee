#!/usr/bin/env python

from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
from sys import stdin

L = []
while True:
    line = stdin.readline()
    if line.startswith('0,0'):
        break
    L.append(tuple(int(s) for s in line.split(',')))

L.sort(key=lambda (id, point): point, reverse=True)
for line in stdin:
    n = int(line)
    order = 0
    p = 0
    for id, point in L:
        if p != point:
            p = point
            order += 1
        if n == id:
            break
    print(order)