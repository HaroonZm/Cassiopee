#!/usr/bin/env python3
import sys
import numpy as np

sys.setrecursionlimit(1_000_000)
MOD = 10**9 + 7

def input_ints():
    return list(map(int, sys.stdin.readline().split()))

def input_int():
    return int(sys.stdin.readline())

def input_matrix(n):
    return np.array([input_ints() for _ in range(n)], dtype=np.int64)

def solve(n):
    b = input_matrix(n)
    if b[0, 0] > b[0, 1]:
        print(f"NG 1")
        return

    dp = np.full((n, 4), np.inf, dtype=np.float64)
    dp[0, 1] = b[0, 0]

    for i in range(n - 1):
        x, t = b[i]
        nx, nt = b[i + 1]
        for a in range(4):
            if dp[i, a] == np.inf:
                continue
            if a < 3:
                na = a + 1
                T = t + na * abs(nx - x)
                if T <= nt:
                    nd = dp[i, a] + abs(nx - x)
                    if nd < dp[i + 1, na]:
                        dp[i + 1, na] = nd
            na = 1
            T = t + (a + 1) * x + nx
            if T <= nt:
                nd = dp[i, a] + nx + x
                if nd < dp[i + 1, na]:
                    dp[i + 1, na] = nd

    final = np.min(dp[-1] + b[-1, 0])
    if np.isinf(final):
        for i, row in enumerate(dp):
            if np.all(np.isinf(row)):
                print(f"NG {i + 1}")
                return
    print(f"OK {int(final)}")

def main():
    for n in iter(input_int, 0):
        solve(n)

if __name__ == "__main__":
    main()