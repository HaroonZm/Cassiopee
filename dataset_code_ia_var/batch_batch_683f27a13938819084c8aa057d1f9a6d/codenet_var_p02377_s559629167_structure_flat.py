import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n, m, f = map(int, readline().split())

G = [[] for i in range(n)]

for _ in range(m):
    u, v, cap, cost = map(int, readline().split())
    G[u].append([v, cap, cost, len(G[v])])
    G[v].append([u, 0, -cost, len(G[u])-1])

INF = 10**18
s = 0
t = n-1

prevv = [0]*n
preve = [0]*n
res = 0

while f:
    dist = [INF]*n
    dist[s] = 0
    update = 1
    while update:
        update = 0
        for v in range(n):
            if dist[v] == INF:
                continue
            gv = G[v]
            for i in range(len(gv)):
                to, cap, cost, rev = gv[i]
                if cap > 0 and dist[v] + cost < dist[to]:
                    dist[to] = dist[v] + cost
                    prevv[to] = v
                    preve[to] = i
                    update = 1
    if dist[t] == INF:
        print(-1)
        sys.exit()
    d = f
    v = t
    while v != s:
        d = min(d, G[prevv[v]][preve[v]][1])
        v = prevv[v]
    f -= d
    res += d * dist[t]
    v = t
    while v != s:
        e = G[prevv[v]][preve[v]]
        e[1] -= d
        G[v][e[3]][1] += d
        v = prevv[v]
print(res)