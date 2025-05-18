import bisect
import os

import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(10 ** 9)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

# MOD = 998244353

N, M = list(map(int, sys.stdin.buffer.readline().split()))
AB = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(N)]
LR = [list(map(int, sys.stdin.buffer.readline().split())) for _ in range(M)]

AB.sort()
odd = 0
# 偶奇が変わる値
nums = [(0, 0)] + AB + [(INF, 0)]
A = [a for a, b in nums]
B = [b for a, b in nums]

size = len(nums)
graph = [[] for _ in range(size)]
for i, (l, r) in enumerate(LR, start=1):
    # l 未満が全部変わる
    v = bisect.bisect_left(A, l) - 1
    # r 以下が全部変わる
    u = bisect.bisect_right(A, r) - 1

    graph[v].append((u, i))
    graph[u].append((v, i))

parity = [0] * size
for i, (b1, b2) in enumerate(zip(B, B[1:])):
    if b1 == 0 and b2 == 1:
        parity[i] = 1
    if b1 == 1 and b2 == 0:
        parity[i] = 1

# 適当に全域木を作って 1 を押し出していけばいい
seen = [False] * size
trees = []
for root in range(size):
    if seen[root] or not graph[root]:
        continue
    edges = []
    seen[root] = True
    stack = [root]
    while stack:
        v = stack.pop()
        for u, i in graph[v]:
            if seen[u]:
                continue
            seen[u] = True
            stack.append(u)
            edges.append((v, u, i))

    # 頂点が1つしかない
    if not edges and parity[root] == 1:
        print(-1)
        exit()
    trees.append(edges)

graph = [[] for _ in range(size)]
degrees = [0] * size
for edges in trees:
    for v, u, i in edges:
        graph[v].append((u, i))
        graph[u].append((v, i))
        degrees[v] += 1
        degrees[u] += 1

ans = []
seen = [False] * size
stack = []
for v, d in enumerate(degrees):
    if d == 1:
        stack.append(v)
while stack:
    v = stack.pop()
    if degrees[v] == 0:
        continue
    assert degrees[v] == 1
    if seen[v]:
        continue
    seen[v] = True
    degrees[v] = 0
    # 葉っぱから内側にずらしてく
    for u, i in graph[v]:
        if seen[u]:
            continue
        if parity[v] == parity[u] == 1:
            parity[u] = parity[v] = 0
            ans.append(i)
        elif parity[v] == 1 and parity[u] == 0:
            parity[u] = 1
            parity[v] = 0
            ans.append(i)
        degrees[u] -= 1
        if degrees[u] == 1:
            stack.append(u)

if 1 in parity:
    print(-1)
else:
    print(len(ans))
    print(*sorted(ans))