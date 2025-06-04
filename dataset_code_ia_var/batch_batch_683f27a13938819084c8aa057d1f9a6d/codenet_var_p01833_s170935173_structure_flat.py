import sys
from collections import deque
INF = 10**9

readline = sys.stdin.readline
write = sys.stdout.write

N_A_B_C = readline().split()
N = int(N_A_B_C[0])
A = int(N_A_B_C[1])
B = int(N_A_B_C[2])
C = int(N_A_B_C[3])

LS = list(range(N))

LA = list(map(int, readline().split()))
ga = min(LA) - 1
for i in LA:
    LS[i - 1] = ga

LB = list(map(int, readline().split()))
gb = min(LB) - 1
for i in LB:
    LS[i - 1] = gb

LC = list(map(int, readline().split()))
gc = min(LC) - 1
for i in LC:
    LS[i - 1] = gc

G = [set() for _ in range(N)]
M = int(readline())
for _ in range(M):
    x, y = map(int, readline().split())
    lx = LS[x - 1]
    ly = LS[y - 1]
    G[lx].add(ly)
    G[ly].add(lx)

dist_a = [INF] * N
la = list(range(N))
dist_a[ga] = 0
queue = deque([ga])
while queue:
    v = queue.popleft()
    d = dist_a[v] + 1
    l = la[v]
    for w in G[v]:
        if dist_a[w] == INF:
            dist_a[w] = d
            la[w] = min(l, la[w])
            queue.append(w)
        elif dist_a[w] == d:
            la[w] = min(l, la[w])

dist_b = [INF] * N
lb = list(range(N))
dist_b[gb] = 0
queue = deque([gb])
while queue:
    v = queue.popleft()
    d = dist_b[v] + 1
    l = lb[v]
    for w in G[v]:
        if dist_b[w] == INF:
            dist_b[w] = d
            lb[w] = min(l, lb[w])
            queue.append(w)
        elif dist_b[w] == d:
            lb[w] = min(l, lb[w])

dist_c = [INF] * N
lc = list(range(N))
dist_c[gc] = 0
queue = deque([gc])
while queue:
    v = queue.popleft()
    d = dist_c[v] + 1
    l = lc[v]
    for w in G[v]:
        if dist_c[w] == INF:
            dist_c[w] = d
            lc[w] = min(l, lc[w])
            queue.append(w)
        elif dist_c[w] == d:
            lc[w] = min(l, lc[w])

ans = INF
k = -1
for i in range(N):
    d = dist_a[i] + dist_b[i] + dist_c[i]
    if d <= ans:
        l = min(la[i], lb[i], lc[i])
        if d < ans:
            ans = d
            k = l
        else:
            k = min(l, k)

write("%d %d\n" % (ans, k + 1))