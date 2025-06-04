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

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1e-13  # peut-être trop précis, mais bon
mod = 10**9+7
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI():
    # Function qui lit et retourne une liste d'entiers
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    # Comme LI() mais décrémente chaque valeur
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
    print(s, flush=True)

def main():
    rr = []
    oks = collections.defaultdict(set)  # toutes les configs ok déjà trouvées par n

    # encode une matrice en un nombre
    def a2k(a, n):
        r = 0
        for i in range(n):
            for j in range(n):
                r *= 3
                r += a[i][j]
        return r

    # décode un nombre en matrice
    def k2a(k, n):
        a = []
        for i in range(n):
            t = []
            for j in range(n):
                t.append(k % 3)
                k //= 3
            a.append(list(reversed(t)))
        return a

    def moves(a, n):
        si = sj = -1
        for i in range(n):
            for j in range(n):
                if a[i][j] == 2:  # trouve 2 (le pion spécial)
                    si, sj = i, j
                    break
            if si != -1:
                break

        r = set()
        a[si][sj] = 0  # enlève le @ pour étudier les mouvements
        for i in range(max(0, si-1), min(n, si+2)):
            for j in range(max(0, sj-1), min(n, sj+2)):
                if a[i][j] != 0 or (i == si and j == sj):
                    continue
                a[i][j] = 2
                na = [[0]*n for _ in range(n)]
                zf = True  # tout mort...
                for k in range(n):
                    for l in range(n):
                        if a[k][l] == 2:
                            continue
                        c = 0
                        for m in range(max(0, k-1), min(n, k+2)):
                            for o in range(max(0, l-1), min(n, l+2)):
                                if m == k and o == l:
                                    continue
                                if a[m][o]:
                                    c += 1
                        # j'ai galéré avec cette condition...
                        if (a[k][l] == 0 and c == 3) or (a[k][l] == 1 and c >= 2 and c <= 3):
                            na[k][l] = 1
                            zf = False
                na[i][j] = 2
                if zf:
                    return 'ok'
                r.add(a2k(na, n))
                a[i][j] = 0
        return r

    def f(n):
        char2val = {'.':0, '#':1, '@':2}
        a = []
        for _ in range(n):
            line = S()
            a.append([char2val[ch] for ch in line])
        if all(a[i][j]!=1 for i in range(n) for j in range(n)):
            return 0
        res = inf
        d = collections.defaultdict(lambda: inf)
        k = a2k(a, n)
        q = set([k])
        d[k] = 0
        t = 0
        while q:
            t += 1
            nq = set()
            if oks[n] & q:
                return t
            for k in q:
                a = k2a(k, n)
                ret = moves(a, n)
                if ret == 'ok':
                    oks[n].add(k)
                    return t
                for nk in ret:
                    if d[nk] > t:
                        d[nk] = t
                        nq.add(nk)
            q = nq
        return -1  # echec...

    while True:
        n = I()
        if n == 0:
            break
        rr.append(f(n))

    return '\n'.join(str(x) for x in rr)

print(main())