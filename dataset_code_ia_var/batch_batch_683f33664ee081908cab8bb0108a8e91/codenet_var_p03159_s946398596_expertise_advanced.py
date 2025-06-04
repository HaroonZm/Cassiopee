import sys
import itertools
from collections import deque

readline = sys.stdin.readline

INF = float('inf')

def merge(d1a, d2a, d1b, d2b):
    la, lb = len(d1a), len(d1b)
    k = la + lb
    res1 = [INF] * k
    res2 = [INF] * k
    # Vectorized inner loop.
    for i, (x1, x2) in enumerate(zip(d1a, d2a)):
        for j, (y1, y2) in enumerate(zip(d1b, d2b)):
            idx = i + j
            vals = [x1 + y1, x1 + y2, x2 + y1]
            res1[idx] = min(res1[idx], *vals)
            res2[idx] = min(res2[idx], x2 + y2)
    # Early pruning in the second pass
    validj = [j for j, (y1, y2) in enumerate(zip(d1b, d2b)) if y1 < 0 or y2 < INF]
    for j in validj:
        for i, (x1, x2) in enumerate(zip(d1a, d2a)):
            res1[i + j + 1] = min(res1[i + j + 1], x1)
            res2[i + j + 1] = min(res2[i + j + 1], x2)
    return res1, res2

def parorder(Edge, root):
    N = len(Edge)
    par = [-1] * N
    order = []
    visited = {root}
    stack = [root]
    while stack:
        vn = stack.pop()
        order.append(vn)
        stack.extend(vf for vf in Edge[vn] if vf not in visited and not visited.add(vf) and not par.__setitem__(vf, vn))
    return par, order

N = int(readline())
A = list(map(int, readline().split()))
Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

P, L = parorder(Edge, 0)

dp1 = [[x if x < 0 else INF] for x in A]
dp2 = [[x if x > 0 else INF] for x in A]

for l in reversed(L[1:]):
    p = P[l]
    dp1[p], dp2[p] = merge(dp1[p], dp2[p], dp1[l], dp2[l])

for idx, (x1, x2) in enumerate(zip(dp1[0], dp2[0])):
    if x1 < 0 or x2 < INF:
        print(idx)
        break
else:
    print(N - 1)