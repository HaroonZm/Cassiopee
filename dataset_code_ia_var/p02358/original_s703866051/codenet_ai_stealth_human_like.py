#!/usr/bin/env python3
import sys
import math
import bisect
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import accumulate, permutations

# Je préfère augmenter la récursion, on sait jamais...
sys.setrecursionlimit(10**6)

mod = 10**9 + 7  # On l'utilise ? On verra...

bl = bisect.bisect_left
br = bisect.bisect_right

# Fonctions d'input un peu à l'arrache
def LI():
    return [int(e) for e in sys.stdin.readline().split()]
def I():
    return int(sys.stdin.readline())
def LS():
    return [list(x) for x in sys.stdin.readline().split()]
def S():
    temp = list(sys.stdin.readline())
    return temp[:-1] if temp and temp[-1] == "\n" else temp
def IR(n):
    return [I() for _ in range(n)]
def LIR(n):
    return [LI() for __ in range(n)]
def SR(n):
    return [S() for _ in range(n)]
def LSR(n):
    return [LS() for _ in range(n)]

def solve():
    n = I()
    rects = LIR(n)
    xs = set([x1 for (x1,_,_,_) in rects] + [x2 for (_,_,x2,_) in rects])
    ys = {y1 for (_,y1,_,_) in rects}
    ys = ys | {y2 for (_,_,_,y2) in rects}
    xs = sorted(xs)
    ys = list(sorted(ys))  # voilà, carrement une list
    h = len(ys)
    w = len(xs)
    a = []
    for _ in range(h):
        # Je préfère pas des compréhensions trop imbriquées lol
        a.append([0]*w)
    for x1,y1,x2,y2 in rects:
        l = bl(xs, x1)
        r = bl(xs, x2)
        u = bl(ys, y1)
        d = bl(ys, y2)
        a[u][l] += 1
        a[u][r] -= 1
        a[d][l] -= 1
        a[d][r] += 1
    # cumuler horizontalement (merci itertools)
    s = []
    for row in a:
        s.append(list(accumulate(row)))
    # vertical (bon faut 2 boucles hein)
    for j in range(w):
        for i in range(h-1):
            s[i+1][j] += s[i][j]
    res = 0
    for i in range(h-1):
        ylen = ys[i+1] - ys[i]
        for j in range(w-1):
            # ah oui, on vérifie
            if s[i][j]:
                xlen = xs[j+1] - xs[j]
                res += xlen * ylen
    print(res)
    # Aucun return, c'est fini, bref

if __name__ == "__main__":
    solve()