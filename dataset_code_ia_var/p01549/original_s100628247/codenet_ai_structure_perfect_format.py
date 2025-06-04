import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 13
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    return print(s, flush=True)

def main():
    rr = []

    def f(n):
        d = {}
        for _ in range(n):
            c, a, b = LS()
            s = set()
            for i in range(int(a), int(b) + 1):
                s.add(i)
            d[c] = s
        m = I()
        aa = LS()
        st = []
        for c in aa:
            if re.match(r'^\d+$', c):
                st.append(set([int(c)]))
            elif c in d:
                st.append(d[c])
            else:
                a, b = st[-2:]
                st = st[:-2]
                t = set()
                if c == '/':
                    if 0 in b:
                        return 'error'
                    for ai in a:
                        for bi in b:
                            t.add((ai // bi) % 256)
                elif c == '+':
                    for ai in a:
                        for bi in b:
                            t.add((ai + bi) % 256)
                elif c == '-':
                    for ai in a:
                        for bi in b:
                            t.add((ai - bi) % 256)
                else:
                    for ai in a:
                        for bi in b:
                            t.add((ai * bi) % 256)
                st.append(t)
        return 'correct'

    while True:
        n = I()
        rr.append(f(n))
        break

    return '\n'.join(map(str, rr))

print(main())