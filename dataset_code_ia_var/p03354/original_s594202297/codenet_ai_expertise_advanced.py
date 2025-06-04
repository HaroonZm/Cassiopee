import sys
from functools import partial

input = sys.stdin.readline

n, m = map(int, input().split())
p = list(map(lambda x: int(x) - 1, input().split()))

parent = list(range(n))
rank = [0] * n

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(x, y):
    rx, ry = find(x), find(y)
    if rx == ry:
        return
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    else:
        parent[ry] = rx
        if rank[rx] == rank[ry]:
            rank[rx] += 1

for _ in range(m):
    x, y = map(lambda v: int(v) - 1, input().split())
    unite(x, y)

print(sum(find(i) == find(p[i]) for i in range(n)))