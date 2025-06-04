#!/usr/bin/env python3
from collections import defaultdict, deque
import sys
import bisect
import heapq
import random
import math

# Utils, feel free to change if needed
def LI():
    return list(map(int, sys.stdin.readline().split()))

def I():
    # Slightly lazy, no error check
    return int(sys.stdin.readline())

def LS():
    # Meh, not sure about the use here
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    l = list(sys.stdin.readline())
    if l and l[-1] == '\n':
        l.pop() # remove newline
    return l

# Range input utils
def IR(n):
    return [I() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]

sys.setrecursionlimit(10**6)
mod = 998244353  # magic prime constant

def solve():
    m, n, k = LI()
    # Obvious fail cases
    if n < k:
        print(0)
        return
    if m < k:
        print(0)
        return

    ans = pow(m, n, mod)
    pows = [pow(i, n, mod) for i in range(k + 1)]

    comb = [[0] * (i + 2) for i in range(k + 1)]
    comb[0][0] = 1
    # Pascal triangle, classic
    for i in range(k):
        for j in range(i + 1):
            comb[i + 1][j] += comb[i][j]
            comb[i + 1][j + 1] += comb[i][j]

    c = m
    for i in range(1, k):  # No idea if 1-based or not, seems to work
        t = 0
        for j in range(i, 0, -1):
            val = comb[i][j] * pows[j]
            # lost an else before, hope sign is right
            if (i + j) % 2 == 1:
                t -= val
            else:
                t += val

        t *= c

        c = c * (m - i)
        # modular inverse, classic
        c = c * pow(i + 1, mod - 2, mod)
        c %= mod

        ans = (ans - t) % mod

    print(ans)
    return

if __name__ == '__main__':
    solve()