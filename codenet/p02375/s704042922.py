from collections import deque
import sys
from typing import List

sys.setrecursionlimit(200000)

N = int(input())
G: List[List[int]] = [[0]] * N
for i in range(N):
    k, *c = map(lambda x: int(x), input().split())
    G[i] = c

H = [0] * N
prv = [None] * N

def dfs(v):
    s = 1
    heavy = None
    m = 0
    for w in G[v]:
        prv[w] = v
        c = dfs(w)
        if m < c:
            heavy = w
            m = c
        s += c
    H[v] = heavy
    return s

dfs(0)

SS: List[List[int]] = []
D: List[int] = []
L = [0] * N
I = [0] * N  # noqa: E741
que = deque([(0, 0)])
while que:
    v, d = que.popleft()
    S: List[int] = []
    k = len(SS)
    while v is not None:
        I[v] = len(S)
        S.append(v)
        L[v] = k
        h = H[v]
        for w in G[v]:
            if h == w:
                continue
            que.append((w, d + 1))
        v = h
    SS.append(S)
    D.append(d)

C = list(map(len, SS))
DS0 = [[0] * (c + 1) for c in C]
DS1 = [[0] * (c + 1) for c in C]

def add(K, data, k, x):
    while k <= K:
        data[k] += x
        k += k & -k

def get(K, data, k):
    s = 0
    while k:
        s += data[k]
        k -= k & -k
    return s

def query_add(v, x):
    while v is not None:
        l = L[v]  # noqa: E741
        i = I[v]
        add(C[l], DS1[l], i + 1, -x)
        add(C[l], DS1[l], 1, x)
        add(C[l], DS0[l], i + 1, x * (i + 1))
        v = prv[SS[l][0]]

def query_sum(v):
    s = - get(C[0], DS1[L[0]], 1) - get(C[0], DS0[L[0]], 1)
    while v is not None:
        l = L[v]  # noqa: E741
        i = I[v]
        s += get(C[l], DS1[l], i + 1) * (i + 1) + get(C[l], DS0[l], i + 1)
        v = prv[SS[l][0]]
    return s

Q = int(input())
ans = []
for q in range(Q):
    t, *cmd = map(lambda x: int(x), input().split())
    if t:
        ans.append(str(query_sum(cmd[0])))
    else:
        v, w = cmd
        query_add(v, w)
print("\n".join(ans))