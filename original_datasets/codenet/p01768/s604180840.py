import sys
from collections import defaultdict,deque
def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def unite(x,y):
    x = root(x)
    y = root(y)
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

f = defaultdict(int)
par = defaultdict(int)
rank = defaultdict(int)
n = int(sys.stdin.readline())
for i in range(n):
    a,x = sys.stdin.readline().split()
    f[a] = int(x)
    par[a] = a
    rank[a] = 0

m = int(sys.stdin.readline())
for i in range(m):
    x,y = sys.stdin.readline().split()
    if root(x) != root(y):
        unite(x,y)

ans = 0
for i in f.keys():
    root(i)
    f[par[i]] = min(f[par[i]],f[i])
for i in f.keys():
    ans += f[root(i)]
print(ans)