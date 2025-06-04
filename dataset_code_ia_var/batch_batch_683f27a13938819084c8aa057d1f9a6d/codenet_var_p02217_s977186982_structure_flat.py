from collections import deque
import sys

sys.setrecursionlimit(1000000)
mod = 1000000007

n = int(sys.stdin.readline())
f = [0]*n
v = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    a -= 1
    b -= 1
    v[a].append(b)
    v[b].append(a)
    f[a] += 1
    f[b] += 1

a = [int(x) for x in sys.stdin.readline().split()]
b = [int(x) for x in sys.stdin.readline().split()]
c = [b[i]-a[i] for i in range(n)]
d = [0]*n
d[0] = 1
q = deque([0])
while q:
    x = q.popleft()
    nd = d[x] + 1
    for y in v[x]:
        if not d[y]:
            d[y] = nd
            q.append(y)

V = list(range(n))
V.sort(key=lambda x: -d[x])
s = [1]*n
for x in V:
    for y in v[x]:
        if d[y] < d[x]:
            s[y] += s[x]

V = list(range(n))
V.sort(key=lambda x: s[x])
ans = 0
for x in V:
    m = 0
    for y in v[x]:
        if s[y] < s[x]:
            if m < c[y]:
                m = c[y]
    ans += m
    c[x] += m * f[x]
    for y in v[x]:
        if s[y] < s[x]:
            if c[y] < m:
                res = m - c[y]
                ans += res * s[y]
                c[x] -= res
        else:
            c[y] -= m
print(ans)