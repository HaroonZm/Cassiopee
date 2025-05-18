from collections import deque

def f(n, dm, g, ind, a, b):
    q = deque([a, b])
    d = [-1] * n
    d[a] = 0
    d[b] = 0
    while q:
        p = q.popleft()
        for node in g[p]:
            if d[node] == -1:
                d[node] = d[p] + 1
                q.append(node)
    l = [0] * (dm // 2 + 1)
    if a == b:
        l[0] = ind[a]
    for i in range(n):
        l[d[i]] = max(l[d[i]], ind[i] - 1)
    res = 1
    for x in l[:-1]:
        res *= x
    return res

n = int(input())
g = [[] for _ in range(n)]
ind = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    ind[a - 1] += 1
    g[b - 1].append(a - 1)
    ind[b - 1] += 1
s = [0]
d = [-1] * n
d[0] = 0
while s:
    p = s.pop()
    for node in g[p]:
        if d[node] == -1:
            d[node] = d[p] + 1
            s.append(node)
m = max(d)
idx = d.index(m)
s = [idx]
d1 = [-1] * n
d1[idx] = 0
while s:
    p = s.pop()
    for node in g[p]:
        if d1[node] == -1:
            d1[node] = d1[p] + 1
            s.append(node)
diam = max(d1)
idx = d1.index(diam)
s = [idx]
d2 = [-1] * n
d2[idx] = 0
while s:
    p = s.pop()
    for node in g[p]:
        if d2[node] == -1:
            d2[node] = d2[p] + 1
            s.append(node)
if diam & 1:  # 直径が奇数
    c = []
    t = diam // 2 + 1
    print(t, end=' ')
    for i in range(n):
        if d1[i] <= t and d2[i] <= t:
            c.append(i)
    ans = f(n, diam, g, ind, c[0], c[1]) * 2
    print(ans)
else:
    t = diam // 2
    print(t + 1, end=' ')
    for i in range(n):
        if d1[i] <= t and d2[i] <= t:
            c = i
    ans = f(n, diam, g, ind, c, c)
    for node in g[c]:
        ans = min(ans, f(n, diam, g, ind, c, node) * 2)
    print(ans)