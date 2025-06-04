#!/usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return list(map(int, sys.stdin.readline().split()))

def I():
    return int(sys.stdin.readline())

def LS():
    return list(map(list, sys.stdin.readline().split()))

def S():
    return list(sys.stdin.readline())[:-1]

def IR(n):
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = I()
    return l

def LIR(n):
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = LI()
    return l

def SR(n):
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = S()
    return l

def LSR(n):
    l = [None for _ in range(n)]
    for i in range(n):
        l[i] = LS()
    return l

sys.setrecursionlimit(1000000)
mod = 1000000007

# 1: combinatorial

# 1_A
"""
n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [float("inf") for _ in range(n+1)]
dp[0] = 0
for i in range(n):
    for j in c:
        if i + j <= n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)
print(dp[n])
"""

# 1_B
"""
n, w = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(w+1)]
memo = [[] for _ in range(w+1)]
for i in range(w):
    for j in range(n):
        if i + b[j][1] <= w and j not in memo[i]:
            if dp[i + b[j][1]] > dp[i] + b[j][0]:
                continue
            else:
                memo[i + b[j][1]] = memo[i] + [j]
                dp[i + b[j][1]] = dp[i] + b[j][0]
print(max(dp))
"""

# 1_C
"""
n, w = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(w+1)]
for i in range(w):
    for j in b:
        if i + j[1] <= w:
            dp[i + j[1]] = max(dp[i + j[1]], dp[i] + j[0])
print(dp[w])
"""

# 1_D
"""
import bisect

n = int(input())
s = [int(input()) for _ in range(n)]
dp = [float("INF") for _ in range(n)]
for i in range(n):
    dp[bisect.bisect_left(dp, s[i])] = s[i]
print(bisect.bisect_left(dp, 100000000000000))
"""

# 1_E
"""
s1 = input()
s2 = input()
n = len(s1)
m = len(s2)
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = i
for j in range(m + 1):
    dp[0][j] = j
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cost = 0 if s1[i - 1] == s2[j - 1] else 1
        dp[i][j] = min(
            dp[i - 1][j] + 1,
            dp[i][j - 1] + 1,
            dp[i - 1][j - 1] + cost
        )
print(dp[n][m])
"""

# 1_F
"""
import bisect

n, W = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
dp = [float("INF") for _ in range(10001)]
dp[0] = 0
for v, w in b:
    for i in range(10001):
        if 10000 - i + v < 10001:
            dp[10000 - i + v] = min(dp[10000 - i + v], dp[10000 - i] + w)
for i in range(1, 10000):
    dp[10000 - i] = min(dp[10000 - i], dp[10001 - i])
print(bisect.bisect_right(dp, W) - 1)
"""

# 1_G
"""
n, W = LI()
g = LIR(n)
"""

# 1_H

# 2: permutation/path

# 2_A
"""
n, e = LI()
v = [[] for _ in range(n)]
f = [-1 for _ in range(n)]
for _ in range(e):
    s, t, d = LI()
    v[s].append([t, d])
    if t == 0:
        f[s] = d
po = [1 for _ in range(n + 1)]
for i in range(n):
    po[i + 1] = po[i] * 2
dp = [[float("inf") for _ in range(po[n])] for _ in range(n)]
dp[0][1] = 0
for j in range(po[n]):
    for x in range(n):
        if po[x] & j:
            for y, d in v[x]:
                if not po[y] & j:
                    dp[y][j | po[y]] = min(dp[y][j | po[y]], dp[x][j] + d)
ans = float("inf")
for i in range(n):
    if f[i] != -1:
        ans = min(ans, dp[i][-1] + f[i])
if ans == float("inf"):
    print(-1)
else:
    print(ans)
"""

# 3: pattern

# 3_A
"""
h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(h)]
dp = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    dp[i][0] = 1 if c[i][0] == 0 else 0
for i in range(w):
    dp[0][i] = 1 if c[0][i] == 0 else 0
for i in range(1, h):
    for j in range(1, w):
        if c[i][j] == 0:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
ans = 0
for i in dp:
    for j in i:
        ans = max(ans, j)
print(ans ** 2)
"""

# 3_B

# 4: counting

# 4_A
"""
n, v = LI()
a = LI()
b = LI()
c = LI()
d = LI()
p = defaultdict(int)
q = defaultdict(int)
for i in a:
    for j in b:
        if i + j <= v - 2:
            p[i + j] += 1
for i in c:
    for j in d:
        if i + j <= v - 2:
            q[i + j] += 1
ans = 0
for i, j in p.items():
    ans += j * q[v - i]
print(ans)
"""

# 5: Twelvedfold_Way

# 5_A
"""
n, k = map(int, input().split())
ans = k
for _ in range(n - 1):
    ans *= k
    ans %= 1000000007
print(ans)
"""

# 5_B
"""
import sys
sys.setrecursionlimit(10000)
memo = [1, 1]
def fact(a):
    if len(memo) > a:
        return memo[a]
    b = a * fact(a - 1)
    memo.append(b)
    return b
n, k = map(int, input().split())
if n > k:
    ans = 0
else:
    ans = fact(k) // fact(k - n)
print(ans % 1000000007)
"""

# 5_C
"""
def comb(a, b):
    return fac[a] * inv[b] * inv[a - b] % mod
n, k = LI()
if n < k:
    print(0)
    quit()
fac = [1 for _ in range(k + 1)]
for i in range(k):
    fac[i + 1] = fac[i] * (i + 1) % mod
inv = [None for _ in range(k + 1)]
inv[k] = pow(fac[k], mod - 2, mod)
for i in range(k)[::-1]:
    inv[i] = inv[i + 1] * (i + 1) % mod
ans = 0
for i in range(k + 1):
    if i % 2:
        ans -= comb(k, i) * pow(k - i, n, mod) % mod
    else:
        ans += comb(k, i) * pow(k - i, n, mod) % mod
    ans %= mod
print(ans)
"""

# 5_D
"""
n, k = map(int, input().split())
import sys
sys.setrecursionlimit(10000)
memo = [1, 1]
def fact(a):
    if len(memo) > a:
        return memo[a]
    b = a * fact(a - 1)
    memo.append(b)
    return b
ans = fact(n + k - 1) // (fact(n) * fact(k - 1)) % 1000000007
print(ans)
"""

# 5_E
"""
def comb(a, b):
    return fac[a] * inv[b] * inv[a - b] % mod
n, k = LI()
if n > k:
    print(0)
    quit()
fac = [1 for _ in range(k + 1)]
for i in range(k):
    fac[i + 1] = fac[i] * (i + 1) % mod
inv = [None for _ in range(k + 1)]
inv[k] = pow(fac[k], mod - 2, mod)
for i in range(k)[::-1]:
    inv[i] = inv[i + 1] * (i + 1) % mod
print(comb(k, n))
"""

# 5_F
def comb(a, b):
    return fac[a] * inv[b] * inv[a - b] % mod

n, k = LI()
if n < k:
    print(0)
    quit()
fac = [1 for _ in range(n + 1)]
for i in range(n):
    fac[i + 1] = fac[i] * (i + 1) % mod
inv = [None for _ in range(n + 1)]
inv[n] = pow(fac[n], mod - 2, mod)
for i in range(n)[::-1]:
    inv[i] = inv[i + 1] * (i + 1) % mod
print(comb(n - 1, n - k))

# 5_G

# 5_H

# 5_I

# 5_J

# 5_K

# 5_L