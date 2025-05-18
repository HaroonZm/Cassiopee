from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque, OrderedDict
from copy import deepcopy
from fractions import gcd
from functools import lru_cache, reduce
from math import ceil, floor
from sys import setrecursionlimit

import heapq
import itertools
import operator

# globals
inf = float('inf')
N, K = [], []
C = []

def set_inputs():
    global N, K, C
    while True:
        n, k = get_li()
        if n == k == 0:
            break
        N.append(n)
        K.append(k)
        c = get_data(k, [int])
        C.append(c)
    return

def sgn(n):
    if n == 0:
        return 0
    if n > 0:
        return 1
    return -1

def main():
    setrecursionlimit(100000)
    set_inputs()
    # ----------MAIN----------
    for n, k, c in zip(N, K, C):
        c.sort()
        ans = 0
        if c[0] == 0:
            tmp = 1
            for v1, v2 in zip(c[1:], c[2:]):
                if v2 - v1 == 1:
                    tmp += 1 * sgn(tmp)
                    if abs(tmp) > abs(ans):
                        ans = tmp
                elif v2 - v1 == 2:
                    if tmp > 0:
                        tmp = -tmp - 2
                    else:
                        tmp = -3
                else:
                    tmp = 1
            if ans > 0:
                ans += 1
            ans = abs(ans)
        else:
            tmp = 1
            for v1, v2 in zip(c, c[1:]):
                if v2 - v1 == 1:
                    tmp += 1
                    ans = max(ans, tmp)
                else:
                    tmp = 1
        print(ans)
    return

def get_int():
    return int(input())

def get_float():
    return float(input())

def get_str():
    return input().strip()

def get_li():
    return [int(i) for i in input().split()]

def get_lf():
    return [float(f) for f in input().split()]

def get_lc():
    return list(input().strip())

def get_data(n, types, sep=None):
    if len(types) == 1:
        return [types[0](input()) for _ in range(n)]
    return list(zip(*(
        [t(x) for t, x in zip(types, input().split(sep=sep))]
        for _ in range(n)
    )))

if __name__ == '__main__':
    main()