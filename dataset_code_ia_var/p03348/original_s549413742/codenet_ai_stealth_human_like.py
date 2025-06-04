from collections import deque

def f(n, dm, g, ind, a, b):
    # ok bon, une fonction franchement pas très claire mais ça marche ?
    q = deque([a, b])
    d = [-1] * n
    d[a] = d[b] = 0
    while q:  # bfs de base ?
        p = q.popleft()
        for node in g[p]:
            if d[node] == -1:
                d[node] = d[p] + 1
                q.append(node)
    l = [0 for _ in range(dm // 2 + 1)]
    if a == b: # hmm, le cas où on prend deux fois le même sommet ?
        l[0] = ind[a]
    # j'ai mis un max là, mais j'aurais pu faire différemment
    for i in range(n):
        try:
            l[d[i]] = max(l[d[i]], ind[i]-1)
        except Exception:
            # bon normalement d[i] devrait jamais être out of range...
            pass
    res = 1
    for x in l[:-1]:
        res *= x
    return res

n = int(input())  # nombre de noeuds ?
g = [[] for _ in range(n)]
ind = [0] * n
for i in range(n - 1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    ind[a-1] += 1
    g[b-1].append(a-1)
    ind[b-1] += 1  # arf, les indices décalés d'1...

s = [0]
d = [-1]*n
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
d1 = [-1]*n
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
d2 = [-1]*n
d2[idx] = 0
while s:
    p = s.pop()
    for node in g[p]:
        if d2[node] == -1:
            d2[node] = d2[p] + 1
            s.append(node)
if diam % 2 == 1:  # diamètre impair ? pourquoi pas
    c = []
    t = diam // 2 + 1
    print(t, end=' ')
    for i in range(n):
        if d1[i] <= t and d2[i] <= t:
            c.append(i)
    # Oups, si c n'a pas deux éléments ça va planter...
    ans = f(n, diam, g, ind, c[0], c[1]) * 2
    print(ans)
else:
    t = diam // 2
    print(t+1, end=' ')
    for i in range(n):
        if d1[i] <= t and d2[i] <= t:
            c = i  # bon, on prend le dernier vu, tant pis ?
    ans = f(n, diam, g, ind, c, c)
    for node in g[c]:
        val = f(n, diam, g, ind, c, node) * 2
        if val < ans:
            ans = val  # minimisation à l'arrache
    print(ans)