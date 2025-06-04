from sys import stdin
from itertools import islice

N, K = map(int, next(stdin).split())
D = N + 1
W = 1 << N

def read_input():
    lines = islice(stdin, D)
    d = [0] * (D * W)
    for i, line in enumerate(lines):
        for j, c in enumerate(line.rstrip()):
            if c == '1':
                d[i*W + j] = 1
    return d

d = read_input()
f = [0] * (D * W)

for i in range(1, D):
    for j in range(1 << i):
        t = (j >> (i-1)) & 1
        r = 0
        val = j
        while r < i and ((val >> (i-1 - r)) & 1) == t:
            r += 1
        f[i*W + j] = r

found = False
for i in range(D):
    for ii in range(i+1, D):
        z = ii - i
        mask = (1 << z) - 1
        shift = ii * W
        for j in range(1 << ii):
            dj = d[shift + j]
            d[i*W + (j >> z)] += dj
            r = f[z*W + (j & mask)]
            if r != z:
                idx = (ii - r)*W + (((j >> z) << (z - r)) | (j & ((1 << (z - r)) - 1)))
                d[idx] += dj
    for j in range(1 << i):
        if d[i*W + j] >= K:
            I, J = i, j
            found = True
            break
    if found:
        break

print('' if I == J == 0 else format(J, f'0{I}b'))