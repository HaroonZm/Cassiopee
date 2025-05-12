import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n, m = map(int, input().split())

if m % 2 == 1:
    print(-1)
    exit()

AB = [[int(x) for x in input().split()] for _ in range(m)]

# representation matrix
repn = [[] for j in range(n + 1)]
for a, b in AB:
    repn[a].append(b)
    repn[b].append(a)

# Minimum Spanning Tree
tree = [set() for i in range(n + 1)]
visited = [False] * (n + 1)
visited[1] = True
q = deque([1])

while q:
    u = q.popleft()
    for v in repn[u]:
        if visited[v]:
            continue
        visited[v] = True
        tree[u].add(v)
        tree[v].add(u)
        q.append(v)

# define directions of the edges other than that of MST
degree = [0] * (n + 1)
ans = []

for a, b in AB:
    if b in tree[a]:
        continue
    ans.append('{} {}'.format(a, b))
    degree[a] += 1

# defining orientations
def dfs(u = 1, parent = None):
    for v in tree[u]:
        if v == parent:
            continue
        dfs(v, u)
        if degree[v] % 2 == 0:
            ans.append('{} {}'.format(u, v))
            degree[u] += 1
        else:
            ans.append('{} {}'.format(v, u))
            degree[v] += 1

dfs()

print('\n'.join(ans))