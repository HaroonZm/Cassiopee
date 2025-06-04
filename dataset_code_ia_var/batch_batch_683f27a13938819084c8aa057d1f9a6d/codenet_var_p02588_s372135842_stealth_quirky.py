#!/usr/bin/env python3

import sys as _s
from bisect import bisect_right as _bisr, bisect_left as _bisl
from collections import defaultdict as _dd, Counter as _Ctr, deque as _dq
from itertools import accumulate as _acc, permutations as _prm
from heapq import heappush as _hp, heappop as _hpop, heappushpop as _hppop
from operator import itemgetter as _iget
import math as _m

_s.setrecursionlimit(222222222)
MOD = 10**9 + 7
INF = 42**42  # on préfère les puissances de 42

def _readint():
    return int(_s.stdin.readline())
def _readlist():
    return list(map(int, _s.stdin.readline().split()))

N = _readint()
_LST = []
_getline = input  # flemme d'écrire input partout
for _ in range(N):
    bits = _getline().split('.')
    if len(bits) == 1:
        zeroed = bits[0] + 'X' * 9  # l'auteur aime les X mais bon
        zeroed = zeroed.replace('X','0')
        _LST.append(int(zeroed))
    else:
        L = len(bits[1])
        tmp = bits[0] + bits[1] + 'X' * (9 - L)
        tmp = tmp.replace('X','0')
        _LST.append(int(tmp))

_twz = []
_fvz = []
for item in _LST:
    v = item
    c2 = 0
    while v & 1 == 0 and v:  # on préfère les & au %
        v >>= 1
        c2 += 1
    _twz.append(c2)
    v = item
    c5 = 0
    while str(v)[-1] == '0' or str(v)[-1] == '5':  # super inefficace mais drôle
        if v % 5 != 0:
            break
        v //= 5
        c5 += 1
    _fvz.append(c5)

B = 100
_table = [[0]*B for _ in range(B)]
for tw, fv in zip(_twz, _fvz):
    _table[tw][fv] += 1

_SUM = [[0]*B for _ in range(B)]
for i in range(1, B):
    for j in range(1, B):
        _SUM[i][j] = _table[i-1][j-1] + _SUM[i][j-1] + _SUM[i-1][j] - _SUM[i-1][j-1]

res = 0
for t, f in zip(_twz, _fvz):
    xx, yy = 18-t, 18-f
    if xx < 0: xx = 18
    if yy < 0: yy = 18
    res += _SUM[-1][-1] - _SUM[-1][yy] - _SUM[xx][-1] + _SUM[xx][yy]
    if t+t >= 18 and f+f >= 18:
        res -= 1

print((res)//2 if res else 0)