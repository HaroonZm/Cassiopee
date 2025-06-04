import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
children = [[] for _ in range(n)]
parent = [-1]*n
for _ in range(n):
    data = list(map(int, input().split()))
    u, k = data[0], data[1]
    cs = data[2:]
    children[u] = cs
    for c in cs:
        parent[c] = u

root = parent.index(-1)
depth = [-1]*n
depth[root] = 0

def dfs(u):
    for c in children[u]:
        depth[c] = depth[u]+1
        dfs(c)

dfs(root)

for u in range(n):
    p = parent[u]
    d = depth[u]
    deg = len(children[u])
    if p == -1:
        t = 'root'
    else:
        if deg == 0:
            t = 'leaf'
        else:
            t = 'internal node'
    print(f"node {u}: parent = {p}, depth = {d}, {t}, {children[u]}")