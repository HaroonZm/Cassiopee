#!/usr/bin/env python3
import sys
from functools import lru_cache

input = sys.stdin.readline

sys.setrecursionlimit(1 << 25)
MOD = 10**9 + 7

def ints():
    return map(int, input().split())

def int1():
    return int(input())

def intn(n):
    return [int1() for _ in range(n)]

def lint(n):
    return [list(map(int, input().split())) for _ in range(n)]

@lru_cache(maxsize=None)
def grundy(w, b):
    s = set()
    if w > 0:
        s.add(grundy(w - 1, b))
    if b > 0:
        s.add(grundy(w + 1, b - 1))
    m = min(w, b)
    s.update(grundy(w, b - i) for i in range(1, m + 1))
    g = 0
    while g in s:
        g += 1
    return g

def solve():
    n = int1()
    ans = 0
    for _ in range(n):
        w, b = ints()
        ans ^= grundy(w, b)
    print(int(ans == 0))

if __name__ == "__main__":
    solve()