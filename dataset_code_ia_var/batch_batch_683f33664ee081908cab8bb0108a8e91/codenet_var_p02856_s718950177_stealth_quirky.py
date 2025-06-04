#!/usr/bin/env python3
import sys as _s
I = _s.stdin.readline

N = int(I())
A, S = 0, 0
for _ in range(N):
    D, C = map(int, I().split())
    A, S = A + C, S + D * C

def _f(a, s):
    return (a - 1) + (s // 9) - int(s % 9 == 0)

print(_f(A, S))