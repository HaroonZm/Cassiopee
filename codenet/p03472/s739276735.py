import sys

# import re
import math
import collections
# import decimal
import bisect
import itertools
import fractions
# import functools
import copy
import heapq
import decimal
# import statistics
import queue

sys.setrecursionlimit(10000001)
INF = 10 ** 16
MOD = 10 ** 9 + 7

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))

# ===CODE===

def main():
    n, h = ns()
    a = []
    b = []
    for i in range(n):
        ai, bi = ns()
        a.append((ai, i))
        b.append((bi, i))

    a = sorted(a, key=lambda x: x[0], reverse=True)
    b = sorted(b, key=lambda x: x[0], reverse=True)

    a_max = a[0][0]
    a_max_idx = a[0][1]

    sum_b = 0
    b_cnt = 0
    for i in range(n):
        if b[i][0] > a_max:
            b_cnt += 1
            sum_b += b[i][0]

    cnt = 0
    if sum_b <= h:
        cnt += (h - sum_b + a_max - 1) // a_max
        cnt += b_cnt
    else:
        for i in range(n):
            h -= b[i][0]
            cnt += 1
            if h <= 0:
                break

    print(cnt)

if __name__ == '__main__':
    main()