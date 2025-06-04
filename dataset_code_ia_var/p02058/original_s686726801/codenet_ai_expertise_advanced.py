import sys
from collections import deque
from itertools import islice

def getpar(edge, root):
    n = len(edge)
    par = [-1]*n
    par[root] = -1
    stack = [root]
    visited = {root}
    while stack:
        v = stack.pop()
        for u in edge[v]:
            if u not in visited:
                visited.add(u)
                par[u] = v
                stack.append(u)
    return par

def topo_sort_tree(edge, root):
    order = []
    stack = [root]
    visited = {root}
    while stack:
        v = stack.pop()
        order.append(v)
        stack.extend(u for u in edge[v] if u not in visited and not visited.add(u))
    return order

mod = 998244353
N, K = map(int, sys.stdin.readline().split())

seg = 110
lim = K + 1
M = (1 << (lim * seg)) - 1
segb = (1 << seg) - 1
fold = 47
tm = pow(2, fold, mod)
bfilter = sum(((1 << fold) - 1) << (i * seg) for i in range(lim))
cfilter = M ^ bfilter

def modulo(x):
    x &= M
    for _ in range(3):
        b = x & bfilter
        c = ((x & cfilter) >> fold) * tm
        x = b + c
    return x

Edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    Edge[a].append(b)
    Edge[b].append(a)

P = getpar(Edge, 0)
L = topo_sort_tree(Edge, 0)

dp1 = [1 << seg] * N
dp2 = [1] * N

for l in reversed(L[1:]):
    p = P[l]
    dp1[p] = modulo(dp1[p] * ((dp1[l] >> seg) + dp1[l] + dp2[l]))
    dp2[p] = modulo(dp2[p] * (dp1[l] + dp2[l]))

res1 = (dp1[0] >> (K * seg)) & segb
res2 = (dp2[0] >> (K * seg)) & segb
print((res1 + res2) % mod)