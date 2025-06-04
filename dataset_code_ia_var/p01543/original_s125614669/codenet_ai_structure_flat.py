import sys

sys.setrecursionlimit(10 ** 9)
INF = 10 ** 18
MOD = 10 ** 9 + 7

input = sys.stdin.readline
N = int(input().strip())
write = []
for _ in range(N):
    write.append(list(map(int, input().split())))
erase = []
for _ in range(N):
    erase.append(list(map(int, input().split())))
grid = []
for _ in range(N):
    grid.append(list(input().strip()))

G = []
for _ in range(2 * N + 2):
    G.append([])

s = 2 * N
t = 2 * N + 1
erasesm = 0

for i in range(N):
    G[s].append([i, 1, 0, len(G[i])])
    G[i].append([s, 0, 0, len(G[s]) - 1])

    G[N + i].append([t, 1, 0, len(G[t])])
    G[t].append([N + i, 0, 0, len(G[N + i]) - 1])
    for j in range(N):
        if grid[i][j] == 'o':
            erasesm += erase[i][j]
            G[i].append([N + j, 1, -erase[i][j], len(G[N + j])])
            G[N + j].append([i, 0, erase[i][j], len(G[i]) - 1])
        else:
            G[i].append([N + j, 1, write[i][j], len(G[N + j])])
            G[N + j].append([i, 0, -write[i][j], len(G[i]) - 1])

f = N
N2 = 2 * N + 2
prv_v = [0] * N2
prv_e = [0] * N2
res = 0
while f:
    dist = [INF] * N2
    dist[s] = 0
    update = True
    while update:
        update = False
        for v in range(N2):
            if dist[v] == INF:
                continue
            for i in range(len(G[v])):
                to, cap, cost, _ = G[v][i]
                if cap > 0 and dist[to] > dist[v] + cost:
                    dist[to] = dist[v] + cost
                    prv_v[to] = v
                    prv_e[to] = i
                    update = True
    if dist[t] == INF:
        res = -1
        break
    d = f
    v = t
    while v != s:
        d = min(d, G[prv_v[v]][prv_e[v]][1])
        v = prv_v[v]
    f -= d
    res += d * dist[t]
    v = t
    while v != s:
        e = G[prv_v[v]][prv_e[v]]
        e[1] -= d
        G[v][e[3]][1] += d
        v = prv_v[v]

res += erasesm

written = set()
for fr in range(N):
    for ed in range(len(G[fr])):
        to, cap, cost, _ = G[fr][ed]
        if cap == 0 and N <= to < N * 2:
            written.add((fr, to - N))
            break

ans = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 'o' and (i, j) not in written:
            ans.append((i + 1, j + 1, 'erase'))
        if grid[i][j] == '.' and (i, j) in written:
            ans.append((i + 1, j + 1, 'write'))
print(res)
print(len(ans))
for i, j, s in ans:
    print(i, j, s)