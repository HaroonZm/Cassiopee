import sys
from collections import defaultdict

input = sys.stdin.readline
n, m, k = map(int, input().split())
d = list(map(int, input().split()))
l = [-1] * n
for i in range(m):
    l[d[i]-1] = i
A = [list(map(int, input().split())) for _ in range(n)]
a = []
for j in range(k):
    line = []
    for i in d:
        idx = A[i-1][j] - 1
        if l[idx] != -1:
            line.append(l[idx])
        else:
            line.append(None)
    a.append(line)
c = [-1] * (1 << m)
c[(1 << m) - 1] = 0
D = []
for i in range(m+1):
    D.append(1 << i)
x = [-1] * m
q = defaultdict(int)
Range = range(m)
K = 0
q[0] = -1
R = 1
while True:
    mask = q[K]
    K += 1
    score = c[mask] + 1
    x = []
    for i in Range:
        if mask & D[i]:
            x.append(i)
    for ai in a:
        tmp = 0
        for j in x:
            aji = ai[j]
            if aji is not None:
                tmp |= D[aji]
        if c[tmp] == -1:
            c[tmp] = score
            q[R] = tmp
            R += 1
            if tmp == 0:
                print(score)
                sys.exit(0)