from sys import stdin
from itertools import islice
from functools import partial

readline = stdin.readline
N, K = map(int, readline().split())
Q = range(N + 1)
bit = 1 << N

d = [[0] * bit for _ in Q]
f = [[0] * bit for _ in Q]

# Reading data with advanced unpacking/map
for i, line in enumerate(islice(stdin, N + 1)):
    d[i][:] = list(map(int, line.strip()))

# Efficient computation of f using comprehension and bitwise operation
for i in range(1, N + 1):
    for j in range(1 << i):
        t = (j >> (i - 1)) & 1
        r = next((r for r in range(i) if ((j >> (i - 1 - r)) & 1) != t), i)
        f[i][j] = r

I = J = 0
for i in Q:
    for k in range(i + 1, N + 1):
        z, m = k - i, (1 << (k - i)) - 1
        for j in range(1 << k):
            dj = d[k][j]
            idx = j >> z
            d[i][idx] += dj
            r = f[z][j & m]
            if r != z:
                mask = (1 << (z - r)) - 1
                target = (j >> z << (z - r)) | (j & mask)
                d[k - r][target] += dj
    # Early break with walrus where possible
    for j in range(1 << i):
        if d[i][j] >= K:
            I, J = i, j
            break
    if I: break

print(bin(J)[2:].zfill(I) if (I or J) else '')