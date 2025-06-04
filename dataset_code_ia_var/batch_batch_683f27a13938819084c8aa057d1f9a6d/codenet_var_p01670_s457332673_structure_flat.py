from collections import deque
import sys
readline = sys.stdin.readline
write = sys.stdout.write
sys.setrecursionlimit(10**5)
N, M, K = map(int, readline().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, readline().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
D = [len(g) for g in G]
I = list(range(N))
I.sort(key=lambda x: D[x], reverse=True)
INF = 10**9
stack = []
stack.append((0, [0]*N, 0))
res = INF
while stack:
    i, state, c = stack.pop()
    if i == N:
        if c < res:
            res = c
        continue
    v = I[i]
    e1 = []
    for w in G[v]:
        if not state[w]:
            e1.append(w)
    if c + len(e1) <= K:
        for w in e1:
            state[w] = 1
        k = i+1
        while k < N and state[I[k]]:
            k += 1
        stack.append((k, state[:], c+len(e1)))
        for w in e1:
            state[w] = 0
    if len(e1) > 1 and c+1 <= K:
        state[v] = 1
        k = i
        while k < N and state[I[k]]:
            k += 1
        stack.append((k, state[:], c+1))
        state[v] = 0
if res < INF:
    write("%d\n" % res)
else:
    write("Impossible\n")