#!/usr/bin/env python3
import sys, math, bisect
from collections import deque as q, defaultdict as dd
from heapq import heappush as push, heappop as pop
from itertools import permutations as perm, accumulate as acc

int_lines = lambda: list(map(int, sys.stdin.buffer.readline().split()))
single_int = lambda: int(sys.stdin.buffer.readline())
str_grid = lambda: [list(s) for s in sys.stdin.readline().split()]
str_chars = lambda: list(sys.stdin.readline().rstrip('\n'))
ints_n = lambda n: [single_int() for _ in range(n)]
int_lines_n = lambda n: [int_lines() for _ in range(n)]
str_chars_n = lambda n: [str_chars() for _ in range(n)]
str_grid_n = lambda n: [str_grid() for _ in range(n)]

sys.setrecursionlimit(10**6)
MODULUS = 10**9+7

def problem():
    N = single_int()
    A = input()
    B = input()
    C = input()
    res = 0
    idx = 0
    while idx < N:
        chars = {A[idx], B[idx], C[idx]}
        ln = len(chars)
        if ln == 1:
            pass
        elif ln == 2:
            res += 1
        else:
            res += 2
        idx += 1
    print(res)

if __name__ == "__main__":
    [_ for _ in [problem()]]