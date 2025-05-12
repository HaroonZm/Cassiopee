#!/usr/bin/env python3
# DSL_5_B: The Maximum Number of Overlaps

from itertools import accumulate
import sys

if __name__ == '__main__':
    n = int(input())

    ys = [0] * 1001
    rects = [None] * 2 * n
    i = 0
    for line in sys.stdin:
        x1, y1, x2, y2 = [int(j) for j in line.split()]
        rects[i] = (x2, -1, y1, y2)
        rects[i+n] = (x1, 1, y1, y2)
        i += 1

    rects.sort(key=lambda x: x[0])

    max_overlap = 0
    for x, t, y1, y2 in rects:
        if t > 0:
            ys[y1] += 1
            ys[y2] -= 1
        else:
            overlap = max(accumulate(ys))
            if overlap > max_overlap:
                max_overlap = overlap
            ys[y1] -= 1
            ys[y2] += 1

    print(max_overlap)