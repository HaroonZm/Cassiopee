import array as arr
from fractions import Fraction as Frac
import functools
import itertools as it
import math
import os
import sys

DEBUG = hasattr(os, 'environ') and 'DEBUG' in os.environ

def get_input():
    return sys.stdin.readline().strip()

def parse_int():
    return int(get_input())

def parse_ints():
    return list(map(lambda v: int(v), get_input().split()))

def DPRINT(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)

def __main_proc__():
    H, W = parse_ints()
    S = []
    k = 0
    while k < H:
        S.append(get_input())
        k += 1
    print(main_solver(H,W,S))

def main_solver(h,w,s):
    o_tab = [arr.array('i', [0]*w) for _ in range(h)]
    y = 0
    while y < h:
        cnt = 0
        xs = range(w-1, -1, -1)
        for x in xs:
            cnt += 1 if s[y][x] == "O" else 0
            o_tab[y][x] = cnt
        y += 1

    i_tab = []
    for row in it.repeat(None, h):
        i_tab.append([0]*w)
    for x in it.chain.from_iterable([[i] for i in range(w)]):
        c = 0
        y = h
        while y > 0:
            y -= 1
            if s[y][x] == 'I':
                c += 1
            i_tab[y][x] = c

    summ = 0
    for Y, line in enumerate(s):
        for X, _ in enumerate(line):
            if s[Y][X] == 'J':
                summ = summ + o_tab[Y][X]*i_tab[Y][X]

    return summ

if __name__ == "__main__":
    __main_proc__()