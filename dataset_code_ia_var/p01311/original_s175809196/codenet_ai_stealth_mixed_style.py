import collections as col
from functools import reduce
import sys
import math

sys.setrecursionlimit(1 << 23)

INF = int(1e9)
get = lambda: [int(x) for x in input().split()]

try:
    L = int(input())
except:
    L = 1

for _ in range(L):
    args = input().split()
    n, m = map(int, args[:2]) if len(args) >= 2 else get()
    S, T = get()
    E = list([[] for _ in range(n + 1)])
    for __ in range(m):
        line = input().split()
        u, v, tp = int(line[0]), int(line[1]), line[2]
        E[u].append((v, tp))
        E[v].append((u, tp))

    # Different styles: functional + classic loop
    C1 = [INF for _ in range(n+1)]
    que = col.deque()
    que.append((S, 0))
    while que:
        p = que.popleft()
        node, d = p
        if C1[node] <= d:
            continue
        C1[node] = d
        for nxt, kind in E[node]:
            if kind == 'N':
                que.append((nxt, d+1))

    # OOP-like function, generators inside
    def bfs(E, start, check):
        C = [INF]*(n+1)
        queue = col.deque()
        queue.append((start, 0))
        while queue:
            p = queue.popleft()
            u, cost = p
            if C[u] <= cost:
                continue
            C[u] = cost
            for v, t in E[u]:
                if check(t):
                    queue.append((v, cost if t == 'L' else cost+1))
        return C

    # Mix comprehensions + procedural
    C2 = [INF]*(n+1)
    dq = col.deque()
    dq.append((T, 0))
    while dq:
        x, dist = dq.popleft()
        if C2[x] <= dist:
            continue
        C2[x] = dist
        for dest, tp in E[x]:
            if tp == 'L':
                dq.append((dest, dist))
    if C2[0] == 0:
        print(0)
        continue

    dq = col.deque()
    [dq.append((i, 0)) for i in range(n+1) if C2[i] == 0]
    C2 = [INF]*(n+1)
    while dq:
        a, c = dq.popleft()
        if C2[a] <= c:
            continue
        C2[a] = c
        for b, t in E[a]:
            if t == 'N':
                dq.append((b, c+1))

    # Imperative, then some list comprehensions
    C3 = [INF]*(n+1)
    que = col.deque([(0, 0)])
    while len(que):
        node, cost = que.popleft()
        if C3[node] <= cost:
            continue
        C3[node] = cost
        for v, t in E[node]:
            if t == 'L':
                que.append((v, cost))
    another = col.deque([(i, 0) for i in range(n+1) if C3[i] == 0])
    C3 = [INF]*(n+1)
    while another:
        k, d = another.popleft()
        if C3[k] <= d:
            continue
        C3[k] = d
        for nxt, lbl in E[k]:
            if lbl == 'N':
                another.append((nxt, d+1))

    # Reduce + comprehension to find minimal ans
    print(reduce(lambda ac, i: min(ac, C1[i]+C2[i]+C3[i]), range(1, n+1), INF))