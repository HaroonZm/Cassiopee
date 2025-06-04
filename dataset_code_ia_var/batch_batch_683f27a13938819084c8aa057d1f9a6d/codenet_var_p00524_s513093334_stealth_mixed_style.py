import sys
from heapq import heappush, heappop

sys.setrecursionlimit(100000000)

(n, m, x) = map(int, input().split())
H = [None] + list(map(int, [input() for _ in range(n)]))
A = [tuple(map(int, input().split())) for _ in range(m)]

INFINITY = float('inf')
g = [[] for _ in range(n+1)]
visited_nodes = [False]*(n+1)
todo = []

def calc():
    heappush(todo, [0, 1, x])
    while len(todo):
        tmp = heappop(todo)
        v, u, height = tmp[1], tmp[0], tmp[2]
        # check goal
        if v == n:
            if height == H[n]: return u
            heappush(todo, [u+H[n]-height, v, H[n]])
            continue
        if visited_nodes[v]: continue
        visited_nodes[v] = True
        # Mix: Use classical for and functional style enumerate
        for idx, edge in enumerate(g[v]):
            nxt, dist = edge
            if 0 <= height - dist <= H[nxt]:
                heappush(todo, [u+dist, nxt, height-dist])
            elif height - dist > H[nxt]:
                heappush(todo, [u+height-H[nxt], nxt, H[nxt]])
            elif H[v] - dist >= 0:
                heappush(todo, [u+dist-height+dist, nxt, 0])
    return -1

# NetworkX style edge construction
for i in range(m):
    a,b,t = A[i]
    g[a].append((b, t)); g[b].append((a, t))

# Introducing a map for output
res = calc()
print(res)