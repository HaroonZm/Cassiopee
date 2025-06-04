inf = 10 ** 9
par = [0] * 5001
rank = [0] * 5001

def init_union_find(V):
    for i in range(V):
        par[i] = i
        rank[i] = 0

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def unite(x, y):
    xroot = find(x)
    yroot = find(y)
    if xroot == yroot:
        return
    if rank[xroot] < rank[yroot]:
        par[xroot] = yroot
    else:
        par[yroot] = xroot
        if rank[xroot] == rank[yroot]:
            rank[xroot] += 1

def same(x, y):
    return find(x) == find(y)

N = int(raw_input())
init_union_find(N)
cost = [0] * N
names = {}
for i in range(N):
    a, x = raw_input().split()
    names[a] = i
    cost[i] = int(x)

M = int(raw_input())
for _ in range(M):
    s, t = raw_input().split()
    unite(names[s], names[t])

ans = 0
ncost = [inf] * N
indexed_cost = []
for i in range(N):
    indexed_cost.append((i, cost[i]))
indexed_cost.sort(key=lambda a: a[1])

for item in indexed_cost:
    i = item[0]
    c = item[1]
    p = find(i)
    if ncost[p] == inf:
        ncost[p] = c
    ans += ncost[p]
print ans