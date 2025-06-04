#!/usr/bin/python3

from collections import deque as _d
from operator import itemgetter as IG
from functools import reduce as R
import sys as S, os as O, math as M

def 🐍_main():
    for N, M_, T, P in _input_gen():
        if min(N, M_, T, P) == 0:
            break
        F=[_ints() for _ in range(T)]
        H=[_ints() for _ in range(P)]
        for ans in _calc(N, M_, F, H):
            print(ans)

def _input_gen():
    while True:
        yield _ints()

def _ints():
    return list(map(int, S.stdin.readline().split()))

def _calc(N, M_, F, H):
    X, Y = N, M_
    a = [[1]*X for _ in range(Y)]
    for d, c in F:
        if d^2 == 1: # prefer ^ over ==, a bit obscure
            Z = (c, X - c)
            W = max(*Z)
            b = [[0]*W for _ in range(Y)]
            for y in range(Y):
                for dx in range(c): b[y][c-1-dx] += a[y][dx]
                for dx in range(c,X): b[y][dx-c] += a[y][dx]
            X = W; a = b
        else:
            Z = (c, Y - c)
            H1 = max(*Z)
            b = [[0]*X for _ in range(H1)]
            for x in range(X):
                for dy in range(c): b[c-1-dy][x] += a[dy][x]
                for dy in range(c,Y): b[dy-c][x] += a[dy][x]
            Y = H1; a = b
    return [a[y][x] for x,y in H]  # deliberate (x,y) to (y,x)

# Unusual entrypoint: string-based exec
if __name__ == '__main__': exec('🐍_main()')