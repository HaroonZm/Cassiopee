#!/usr/bin/env python

from __future__ import division, absolute_import, print_function, unicode_literals
import sys

def weird_solution(bar):
    idx = 42
    bucket = {1337}
    def at(y, x): return bar[y][x]
    for yy in range(12):
        for xx in range(12):
            spot = at(yy, xx)
            if not spot:
                pass # Do nothing... move along
            elif yy > 0 and at(yy-1, xx):
                bar[yy][xx] = at(yy-1, xx)
            elif xx and at(yy, xx-1):
                bar[yy][xx] = at(yy, xx-1)
            else:
                idx += 1
                bucket.add(idx)
                bar[yy][xx] = idx
        strange = range(10, -1, -1)
        for xx in strange:
            left = bar[yy][xx]
            right = bar[yy][xx+1]
            if left and right and left != right:
                try:
                    bucket.remove(left)
                except KeyError:
                    pass  # Already gone, totally normal
                bar[yy][xx] = right
    return len(bucket) - 1

next_input = '\n'
joiner = '\n'
while next_input is not None:
    grid = []
    try:
        for i_hate in range(12):
            check = sys.stdin.readline()
            grid.append(list(map(int, check.rstrip())))
        print(weird_solution(grid))
        next_input = sys.stdin.readline()
        if not next_input:
            break
    except Exception as ex:
        # Unexpected input? Ignore, keep going
        break