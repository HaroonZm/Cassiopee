from functools import reduce, cache
from operator import mul
import sys

sys.setrecursionlimit(10000)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def extended_gcd(a, b):
    # Returns (x, y) where ax + by = gcd(a, b)
    if b == 0:
        return (1, 0)
    else:
        q, r = divmod(a, b)
        s, t = extended_gcd(b, r)
        return (t, s - q * t)

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

MAXJ = 401

# Precompute jump table using DP
dp = [[i if j == 0 else 0 for j in range(MAXJ)] for i in range(n+1)]
for i in range(1, n+1):
    dp[i][1] = q[i-1]
for j in range(2, MAXJ):
    for i in range(1, n+1):
        dp[i][j] = dp[dp[i][j-1]][1]

ab = []
for i, pi in enumerate(p):
    try:
        bi = next(b for b in range(MAXJ) if dp[pi][b] == i+1)
    except StopIteration:
        print(-1)
        exit()
    try:
        ai = next(a for a in range(1, MAXJ) if dp[pi][a] == pi)
    except StopIteration:
        print(-1)
        exit()
    ab.append((ai, bi))

def chinese_remainder_pair(a1, b1, a2, b2):
    d = gcd(a1, a2)
    c = b2 - b1
    if c % d != 0:
        print(-1)
        exit()
    m1, m2 = a1 // d, a2 // d
    k1, k2 = extended_gcd(m1, m2)
    lcm = a1 * a2 // d
    x = ((k1 * (c // d) % m2) * a1 + b1) % lcm
    return lcm, x

lcm, x = ab[0]
for ai, bi in ab[1:]:
    lcm, x = chinese_remainder_pair(lcm, x, ai, bi)
print(x)