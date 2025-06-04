import sys

f = {}
par = {}
rank = {}

def find(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x

def union(x, y):
    x_root = find(x)
    y_root = find(y)
    if x_root == y_root:
        return
    if rank[x_root] < rank[y_root]:
        par[x_root] = y_root
    else:
        par[y_root] = x_root
        if rank[x_root] == rank[y_root]:
            rank[x_root] += 1

n = int(sys.stdin.readline())
for i in range(n):
    a, x = sys.stdin.readline().split()
    f[a] = int(x)
    par[a] = a
    rank[a] = 0

m = int(sys.stdin.readline())
for i in range(m):
    x, y = sys.stdin.readline().split()
    union(x, y)

min_f = {}
for key in f:
    root = find(key)
    if root not in min_f:
        min_f[root] = f[key]
    else:
        if f[key] < min_f[root]:
            min_f[root] = f[key]

ans = 0
for value in min_f.values():
    ans += value
print(ans)