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

def set_recursion():
    sys.setrecursionlimit(10 ** 7)

def get_inf():
    return 10 ** 20

def get_eps():
    return 1.0 / 10 ** 13

def get_mod():
    return 10 ** 9 + 7

def get_dd():
    return [(-1,0),(0,1),(1,0),(0,-1)]

def get_ddn():
    return [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x)-1 for x in sys.stdin.readline().split()]

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

def create_xs_ys(a):
    xs = set()
    ys = set()
    for l,t,r,b in a:
        xs.add(l)
        xs.add(r)
        ys.add(t)
        ys.add(b)
    return xs, ys

def create_xd(xs):
    return {x: i for i, x in enumerate(sorted(xs))}

def create_yd(ys):
    return {y: i for i, y in enumerate(sorted(ys))}

def compress_rectangles(a, xd, yd):
    z = []
    for l, t, r, b in a:
        z.append([xd[l], yd[t], xd[r], yd[b]])
    return z

def get_xx_len(xs):
    return len(xs) + 3

def get_yy_len(ys):
    return len(ys) + 3

def create_aa(xx, yy):
    return [[0] * xx for _ in range(yy)]

def calc_ii(n):
    return [2 ** i for i in range(n)]

def fill_aa(aa, z, ii, n):
    for i in range(n):
        l, t, r, b = map(lambda x: x + 1, z[i])
        aa[b][l] += ii[i]
        aa[t][l] -= ii[i]
        aa[b][r] -= ii[i]
        aa[t][r] += ii[i]
    return aa

def get_grid_Ruiwa(aa):
    return Ruiwa(aa)

def get_t(rui):
    return rui.R

def valid_indices(i, j, yy, xx):
    return 0 <= i < yy and 0 <= j < xx

def _f_inner(t, i, j, k, yy, xx, dd):
    if not (0 <= i < yy and 0 <= j < xx):
        return
    if t[i][j] != k:
        return
    t[i][j] = -1
    for di, dj in dd:
        _f_inner(t, i+di, j+dj, k, yy, xx, dd)

def count_regions(t, yy, xx, dd):
    r = 0
    for i in range(yy):
        for j in range(xx):
            if t[i][j] >= 0:
                _f_inner(t, i, j, t[i][j], yy, xx, dd)
                r += 1
    return r

# Ruiwa (2D Prefix Sum)
class Ruiwa():
    def __init__(self, a):
        self.H = h = len(a)
        self.W = w = len(a[0])
        self.R = r = a
        for i in range(h):
            for j in range(1, w):
                r[i][j] += r[i][j-1]
        for i in range(1, h):
            for j in range(w):
                r[i][j] += r[i-1][j]

    def search(self, x1, y1, x2, y2):
        if x1 > x2 or y1 > y2:
            return 0
        r = self.R
        rr = r[y2][x2]
        if x1 > 0 and y1 > 0:
            return rr - r[y1-1][x2] - r[y2][x1-1] + r[y1-1][x1-1]
        if x1 > 0:
            rr -= r[y2][x1-1]
        if y1 > 0:
            rr -= r[y1-1][x2]
        return rr

def process_query(n):
    a = read_rectangles(n)
    xs, ys = create_xs_ys(a)
    xd = create_xd(xs)
    yd = create_yd(ys)
    z = compress_rectangles(a, xd, yd)
    xx = get_xx_len(xs)
    yy = get_yy_len(ys)
    aa = create_aa(xx, yy)
    ii = calc_ii(n)
    aa = fill_aa(aa, z, ii, n)
    rui = get_grid_Ruiwa(aa)
    t = get_t(rui)
    dd = get_dd()
    return count_regions(t, yy, xx, dd)

def read_rectangles(n):
    rects = []
    for _ in range(n):
        rects.append(LI())
    return rects

def read_input_and_solve():
    set_recursion()
    outputs = []
    while True:
        n = I()
        if n == 0:
            break
        outputs.append(process_query(n))
    return '\n'.join(map(str, outputs))

def main():
    res = read_input_and_solve()
    print(res)

main()