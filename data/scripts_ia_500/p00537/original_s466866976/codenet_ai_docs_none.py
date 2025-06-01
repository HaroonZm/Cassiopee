import sys
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
tbl = []
for i in range(n-1):
    a, b, c = map(int, input().split())
    tbl.append((a, b, c))
f = [0]*n
for i in range(m-1):
    u, v = p[i]-1, p[i+1]-1
    if u > v:
        u, v = v, u
    f[u] += 1
    f[v] -= 1
for i in range(n-1):
    f[i+1] += f[i]
ans = 0
for i in range(n-1):
    cash = tbl[i][0] * f[i]
    ic = tbl[i][1] * f[i] + tbl[i][2]
    ans += min(cash, ic)
print(ans)