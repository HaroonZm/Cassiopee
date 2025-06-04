#!/usr/bin/env python3
import sys
import math
import bisect
import random
from collections import defaultdict, deque
from heapq import heappush, heappop

def LI():
    # retourne une liste d'entiers, utile
    return list(map(int, sys.stdin.readline().split()))

def I():
    # je préfère parfois input(), mais bon
    return int(sys.stdin.readline())

def LS():
    # lit une ligne et la découpe, puis découpe les chaines en listes 
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    # retourne une ligne sous forme de liste de caractères, je ne m'en sers jamais en vrai
    res = list(sys.stdin.readline())
    if len(res) > 0 and res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    # une liste de n entiers
    line = []
    for _ in range(n):
        line.append(I())
    return line

def LIR(n):
    # n lignes d'entiers
    arr = []
    for _ in range(n):
        arr.append(LI())
    return arr

def SR(n):
    # n lignes, chacune transformée par S()
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(999999)
mod = 10 ** 9 + 7

# A
def A():
    n = I()
    a = LI()
    s = sum([v % 2 for v in a]) # nombre d'impairs
    if s == 0 or s == n:
        print(0)
    else:
        print(n - 2 + (s & 1))
    # pas sûr pourquoi on retourne rien mais bon
    return

# B
def B():
    n, Q, L, R = LI()
    a = LI()
    a.sort()
    query = LIR(Q)
    l = -1
    r = n
    while r - l > 1:
        m = (l + r) // 2
        am = a[m]
        for q, x, s, t in query:
            if q == 1:
                if am < x:
                    continue
                am += s
                am *= t
            else:
                if am > x:
                    continue
                am -= s
                if am < 0:
                    am = -((-am) // t)
                else:
                    am //= t
        if am < L:
            l = m
        else:
            r = m
    left = r
    l = 0
    r = n
    while r - l > 1:
        m = (l + r) // 2
        am = a[m]
        for q, x, s, t in query:
            if q == 1:
                if am < x:
                    continue
                am += s
                am *= t
            else:
                if am > x:
                    continue
                am -= s
                if am < 0:
                    am = -((-am) // t)
                else:
                    am //= t
        if am <= R:
            l = m
        else:
            r = m
    print(r - left)
    return

# C
def C():
    n, m = LI()
    lis = set()
    f = defaultdict(lambda: 0)
    for _ in range(n):
        l, r = LI()
        f[l] += 1  # début d'intervalle
        f[r + 0.1] -= 1  # fin bidon, pourquoi 0.1 ???
        lis.add(l)
        lis.add(r)
        lis.add(r + 0.1)
    tmp = list(lis)
    tmp.sort()
    k = len(tmp)
    for idx in range(k - 1):
        f[tmp[idx + 1]] += f[tmp[idx]]
    s = [0, 0]
    for x in tmp:
        j = f[x]
        if s[1] < j:
            s = [x, j]
        elif s[1] == j:
            if s[1] % 2:
                s = [x, j]

    if s[1] % 2:
        # je suppose que c'est comme ça, pas sûr du calcul
        print((s[1] // 2) * 2 * m + round(s[0]))
    else:
        print(s[1] * m - round(s[0]))
    return

# D
def D():
    n = I()
    # pas fait
    return

# E
def E():
    n = I()
    # pas regardé
    return

# F
def F():
    n = I()
    # non plus
    return

# G
def G():
    n = I()
    # peut-être une prochaine fois
    return

# H
def H():
    n = I()
    # ... 
    return

# I (pas possible, donc I_)
def I_():
    n = I()
    # visiblement rien ici
    return

# J
def J():
    n = I()
    return

if __name__ == '__main__':
    C()  # pour l'instant juste C, à adapter selon le problème