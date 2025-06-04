from sys import stdin
from itertools import islice

n, C, *H = map(int, stdin.read().split())
dp = [0]
P = [0]

def f(i, h):
    return dp[i] + H[i] * (H[i] - 2 * h)

def is_obsolete(x, y, z):
    # Cross product for convex hull: x,y,z indices
    return (H[y] - H[x]) * (f(y, 0) - f(z, 0)) > (H[z] - H[y]) * (f(x, 0) - f(y, 0))

for i in islice(range(n), 1, None):
    while len(P) > 1 and f(P[0], H[i]) > f(P[1], H[i]):
        P.pop(0)
    dp.append(f(P[0], H[i]) + H[i] ** 2 + C)
    while len(P) > 1 and is_obsolete(P[-2], P[-1], i):
        P.pop()
    P.append(i)

print(dp[-1])