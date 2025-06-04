import sys
from functools import reduce
from math import gcd
from operator import mul

def lcm(a, b):
    return a * b // gcd(a, b)

def solve():
    readline = sys.stdin.readline
    write = sys.stdout.write
    N, M = map(int, readline().split())
    A = list(map(int, readline().split()))
    P = [p / 100 for p in map(int, readline().split())]

    N2 = 1 << N
    L = [1] * N2
    Q = [1.0] * N2
    C = [0] * N2

    for i in range(N):
        idx = 1 << i
        L[idx] = A[i]
        Q[idx] = P[i]

    ans = 0.0
    for state in range(1, N2):
        b = state.bit_length() - 1
        prev_state = state ^ (1 << b)
        L[state] = lcm(L[prev_state], L[1 << b])
        Q[state] = Q[prev_state] * Q[1 << b]
        C[state] = C[prev_state] + 1
        contrib = Q[state] * (M // L[state])
        if C[state] & 1:
            ans += contrib
        else:
            ans -= contrib

    write(f"{ans:.16f}\n")

solve()