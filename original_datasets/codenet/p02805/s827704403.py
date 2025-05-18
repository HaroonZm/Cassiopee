from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import bisect
import random
from itertools import permutations, accumulate, combinations, product
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor, gcd, sqrt
from operator import mul
from functools import reduce
from operator import mul
from pprint import pprint

sys.setrecursionlimit(2147483647)
INF = 10 ** 20
def LI(): return list(map(int, sys.stdin.buffer.readline().split()))
def I(): return int(sys.stdin.buffer.readline())
def LS(): return sys.stdin.buffer.readline().rstrip().decode('utf-8').split()
def S(): return sys.stdin.buffer.readline().rstrip().decode('utf-8')
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
def MSRL(n): return [[int(j) for j in list(S())] for i in range(n)]
mod = 1000000007

def f(i, j, k):
    x1, y1 = L[i]
    x2, y2 = L[j]
    x3, y3 = L[k]
    # length of each side to the second power and area of the triangle
    a2 = (x2 - x3) ** 2 + (y2 - y3) ** 2
    b2 = (x1 - x3) ** 2 + (y1 - y3) ** 2
    c2 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    area = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2

    # not on the same line please
    if area == 0:
        return INF
    x = (a2 * (b2 + c2 - a2) * x1 + b2 * (c2 + a2 - b2) * x2 + c2 * (a2 + b2 - c2) * x3) / (16 * area * area)
    y = (a2 * (b2 + c2 - a2) * y1 + b2 * (c2 + a2 - b2) * y2 + c2 * (a2 + b2 - c2) * y3) / (16 * area * area)
    r = sqrt((x1 - x) ** 2 + (y1 - y) ** 2)
    for d in range(n):
        if d in (i, j, k):
            continue
        ax, ay = L[d]
        if (ax - x) ** 2 + (ay - y) ** 2 > r ** 2:
            return INF
    return r

def diametercircle(ax, ay, bx, by):
    X = (ax + bx) / 2
    Y = (ay + by) / 2
    R = sqrt((X - ax) * (X - ax) + (Y - ay) * (Y - ay))
    return X, Y, R

def distance(ax, ay, bx, by):
    return sqrt((ax - bx) ** 2 + (ay - by) ** 2)

n = I()
L = []
for _ in range(n):
    x, y = LI()
    L += [(x, y)]

ans = INF
for i, j, k in combinations(range(n), 3):

    ans = min(ans, f(i, j, k))

for l, m in combinations(range(n), 2):
    lx, ly = L[l]
    mx, my = L[m]
    mid_x = (lx + mx) / 2
    mid_y = (ly + my) / 2
    r_s = (mid_x - lx) ** 2 + (mid_y - ly) ** 2
    for i in range(n):
        if i == l or i == m:
            continue
        zx, zy = L[i]
        if (zx - mid_x) ** 2 + (zy - mid_y) ** 2 > r_s:
            break
    else:
        ans = min(ans, sqrt(r_s))

print(ans)