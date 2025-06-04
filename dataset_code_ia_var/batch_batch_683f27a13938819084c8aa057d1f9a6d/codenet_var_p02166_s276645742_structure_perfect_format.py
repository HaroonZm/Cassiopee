#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    return int(sys.stdin.readline())

def LS():
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    return [I() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    def add(i):
        while i <= n:
            bit[i] += 1
            i += i & -i

    def sum_(i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & -i
        return res

    n, k = LI()
    p = LI()
    if n > k:
        if k % 2 == 0:
            print("Yes")
        else:
            a = 0
            bit = [0] * (n + 1)
            for i in range(n):
                a ^= (i - sum_(p[i])) & 1
                add(p[i])
            if a:
                print("No")
            else:
                print("Yes")
        return
    else:
        for i in range(n):
            if p[i] == 1:
                break
        for j in range(n):
            if p[(j + i) % n] != j + 1:
                print("No")
                return
        print("Yes")
    return

if __name__ == "__main__":
    solve()