from sys import stdin
from itertools import starmap

N, M = map(int, stdin.readline().split())
ds = []
for line in stdin:
    s, t, e = map(int, line.split())
    if s == t == e == 0:
        break
    ds.append((s-1, t-1, e))
L = int(stdin.readline())
for _ in range(L):
    b = list(map(int, stdin.readline().split()))
    c = [0] * N
    for s, t, e in ds:
        c[s] += e * b[t]
    print(*c)