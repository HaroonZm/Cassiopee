def dist2(A, B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2
def cross(A, B, C):
    return (B[0]-A[0])*(C[1]-A[1]) - (C[0]-A[0])*(B[1]-A[1])
def convex_hull(PS):
    n = len(PS)
    PP = sorted([p + [i] for i, p in enumerate(PS)])
    Q = []
    for i in range(n):
        while len(Q) > 1 and cross(PP[Q[-2]], PP[Q[-1]], PP[i]) >= 0:
            Q.pop()
        Q.append(i)
    k = len(Q)
    for i in range(n-2, -1, -1):
        while len(Q) > k and cross(PP[Q[-2]], PP[Q[-1]], PP[i]) >= 0:
            Q.pop()
        Q.append(i)
    return list(PP[i][2] for i in Q)

from math import sqrt
v, r = map(int, input().split())
PS = [list(map(int, input().split())) for i in range(v)]
CH = convex_hull(PS)

*parent, = range(v)
def root(x):
    if x == parent[x]:
        return x
    parent[x] = root(parent[x])
    return parent[x]
def unite(x, y):
    px = root(x); py = root(y)
    if px < py:
        parent[py] = px
    else:
        parent[px] = py

ans = 0
for i in range(len(CH)-1):
    unite(CH[i], CH[i+1])
    ans += sqrt(dist2(PS[CH[i]], PS[CH[i+1]]))
R = [list(map(int, input().split())) for i in range(r)]
R.sort(key=lambda x: dist2(PS[x[0]-1], PS[x[1]-1]))
for s, t in R:
    if root(s-1) != root(t-1):
        unite(s-1, t-1)
        ans += sqrt(dist2(PS[s-1], PS[t-1]))
print(ans)