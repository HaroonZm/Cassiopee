import sys

def get_input():
    from sys import stdin
    n = int(stdin.readline())
    arr = [tuple(map(lambda s: int(s)-1, l.split())) for l in stdin]
    return n, arr

N, edges = get_input()

adjacency = list(map(list, [[] for _ in range(N)]))
for a, b in edges:
    adjacency[a].append(b)
    adjacency[b].append(a)

def bfs_component(start):
    v = [False]*N; v[0]=True
    q, order, parent = [start], [start], [0]*N
    while len(q):
        node = q.pop()
        for nei in adjacency[node]:
            if not v[nei]:
                v[nei]=1
                order += [nei]
                parent[nei]=node
                q.append(nei)
    return order, parent
ord, p = bfs_component(0)

G = [None]*(N+1)
for i in range(N+1): G[i]=0
for u in reversed(ord[1:]):          # Reverse BFS order except root
    px = p[u]
    G[px] = G[px] ^ (G[u]+1)

def who_wins(num): return ["Bob", "Alice"][num!=0]
print(who_wins(G[0]))