from sys import stdin
from itertools import accumulate
from functools import lru_cache

R = range
N, K = map(int, stdin.readline().split())
Q = R(N + 1)
d = [bytearray(1 << i) for i in Q]
f = [bytearray(1 << i) for i in Q]

for i, s in enumerate(map(str.rstrip, (stdin.readline() for _ in Q))):
    d[i][:len(s)] = map(int, s)

for i in R(1, N + 1):
    fi = f[i]
    for j in R(1 << i):
        t = (j >> (i - 1)) & 1
        r = 0
        while r < i and ((j >> (i - 1 - r)) & 1) == t:
            r += 1
        fi[j] = r

for i in Q:
    for k in R(i + 1, N + 1):
        z = k - i
        m = (1 << z) - 1
        dk, fi_z, di = d[k], f[z], d[i]
        for j in R(1 << k):
            di[j >> z] += dk[j]
            r = fi_z[j & m]
            if r != z:
                d[k - r][(j >> z) << (z - r) | (j & ((1 << (z - r)) - 1))] += dk[j]
    I = J = None
    for j, v in enumerate(d[i]):
        if v >= K:
            I, J = i, j
            break
    if I is not None:
        break

print('' if (I == 0 and J == 0) else format(J, '0{}b'.format(I)))