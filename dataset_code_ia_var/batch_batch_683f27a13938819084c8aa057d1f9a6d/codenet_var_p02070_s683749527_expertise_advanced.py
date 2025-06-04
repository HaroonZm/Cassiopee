from sys import stdin
from functools import reduce

def extgcd(a, b):
    if not b:
        return (a, 1, 0)
    g, y, x = extgcd(b, a % b)
    return (g, x, y - (a // b) * x)

def crt_pair(A, B, a, b):
    g, x, y = extgcd(B, b)
    diff = a - A
    if diff % g:
        return (0, 0)
    m = diff // g
    x = (x * m) % (b // g)
    nB = B * (b // g)
    res = (A + B * x) % nB
    return (res, nB)

N = int(stdin.readline())
P = [int(x) - 1 for x in stdin.readline().split()]
Q = [int(x) - 1 for x in stdin.readline().split()]

ap = [[-1] * N for _ in range(N)]
b = [0] * N
p = P[:]
for i in range(N + 1):
    for j in range(N):
        pj = p[j]
        if ap[j][pj] >= 0:
            if not b[j]:
                b[j] = i - ap[j][pj]
        else:
            ap[j][pj] = i
        p[j] = Q[pj]

a = [ap[i][i] for i in range(N)]
if any(x < 0 for x in a):
    print(-1)
else:
    def reducer(state, idx):
        A, B = state
        res, nB = crt_pair(A, B, a[idx], b[idx])
        if not nB:
            raise ValueError
        return (res, nB)
    try:
        A, _ = reduce(reducer, range(N), (0, 1))
        print(A)
    except ValueError:
        print(-1)