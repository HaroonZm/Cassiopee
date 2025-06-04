#!/usr/bin/env python

from __future__ import division, absolute_import, print_function, unicode_literals
from sys import stdin

for line in stdin:
    date = tuple(int(s) for s in line.split())
    if date < (1868, 9, 8):
        print('pre-meiji')
    elif date < (1912, 7, 30):
        print('meiji', date[0] - 1867, date[1], date[2])
    elif date < (1926, 12, 25):
        print('taisho', date[0] - 1911, date[1], date[2])
    elif date < (1989, 1, 8):
        print('showa', date[0] - 1925, date[1], date[2])
    else:
        print('heisei', date[0] - 1988, date[1], date[2])