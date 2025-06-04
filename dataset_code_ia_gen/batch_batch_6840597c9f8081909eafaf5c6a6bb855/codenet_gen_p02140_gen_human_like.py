import sys
from collections import deque

MOD = 10**9 + 7
input = sys.stdin.readline

R, C, ai, aj, bi, bj = map(int, input().split())

dist = [[-1]*C for _ in range(R)]
ways = [[0]*C for _ in range(R)]

dist[ai][aj] = 0
ways[ai][aj] = 1
queue = deque()
queue.append((ai, aj))

while queue:
    e, f = queue.popleft()
    d = dist[e][f]
    w = ways[e][f]
    # 4 neighbors
    for ne, nf in [(e+1,f),(e-1,f),(e,f+1),(e,f-1)]:
        if 0 <= ne < R and 0 <= nf < C:
            nd = d+1
            if dist[ne][nf] == -1:
                dist[ne][nf] = nd
                ways[ne][nf] = w
                queue.append((ne,nf))
            elif dist[ne][nf] == nd:
                ways[ne][nf] = (ways[ne][nf] + w) % MOD
    # edges to row edges
    for nf in [0,C-1]:
        if nf != f:
            ne = e
            nd = d+1
            if dist[ne][nf] == -1:
                dist[ne][nf] = nd
                ways[ne][nf] = w
                queue.append((ne,nf))
            elif dist[ne][nf] == nd:
                ways[ne][nf] = (ways[ne][nf] + w) % MOD
    # edges to column edges
    for ne in [0,R-1]:
        if ne != e:
            nf = f
            nd = d+1
            if dist[ne][nf] == -1:
                dist[ne][nf] = nd
                ways[ne][nf] = w
                queue.append((ne,nf))
            elif dist[ne][nf] == nd:
                ways[ne][nf] = (ways[ne][nf] + w) % MOD

print(dist[bi][bj], ways[bi][bj] % MOD)