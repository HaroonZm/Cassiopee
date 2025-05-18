from collections import deque

n, q = map(int, (input().split()))

t = [[] for i in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, (input().split()))
    t[a].append(b)
    t[b].append(a)

cnt = [0 for i in range(n + 1)]
for i in range(q):
    p, x = map(int, (input().split()))
    cnt[p] += x

d = deque()
d.append(1)
chked = set()
while d:
    stat = d.pop()
    chked.add(stat)
    for v in t[stat]:
        if v not in chked:
            d.append(v)
            cnt[v] += cnt[stat]

print(*cnt[1:])