#!/usr/bin/env python

from collections import deque
import itertools as it
import sys

sys.setrecursionlimit(1000000)

def d_num(num):
    ret = 0
    s = str(num)
    d = len(s)
    if d == 1:
        return num
    for i in range(d - 1):
        ret += (i + 1) * 9 * 10 ** i
    return ret + d * (num - 10 ** (d - 1) + 1)

def search(num, l, r):
    if r - l <= 1:
        return l, num - d_num(l)
    mid = (l + r) / 2
    if d_num(mid) > num:
        r = mid
    else:
        l = mid
    return search(num, l, r)

while True:
    K, N = map(int, raw_input().split())
    if K == 0:
        break
    '''
    S = ''
    for i in range(10000):
        S += str(i)
    print S[K:K + N]
    '''
    p = search(K - 1, 0, 10 ** 18)

    S = ''
    for i in range(p[0] + 1, p[0] + 101):
        S += str(i)
    print S[p[1]:p[1] + N]