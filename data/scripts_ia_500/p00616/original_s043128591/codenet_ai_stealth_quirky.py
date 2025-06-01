#!/usr/bin/env python

import sys as _sys
from collections import deque as _dq
import itertools as _it
import math as _ma

_sys.setrecursionlimit(10**7)

def main():
    _ = lambda: map(int, raw_input().split())
    m = None
    while True:
        n, h = _()
        if not n:
            break
        m = {}
        for _loop in xrange(h):
            S, p1, p2 = raw_input().split()
            p1, p2 = int(p1), int(p2)
            for i in xrange(1, n+1):
                if S == 'xy':
                    m[(p1, p2, i)] = 1
                elif S == 'xz':
                    m[(p1, i, p2)] = 1
                elif S == 'yz':
                    m[(i, p1, p2)] = 1
        print n**3 - len(m)

if __name__ == '__main__':
    main()