import sys

N, M = map(int, sys.stdin.readline().split())
adj = []
for i in range(N+1):
    adj.append([])

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

deg = []
for i in range(N+1):
    deg.append(len(adj[i]))

f = []
ok = False
for i in range(1, N+1):
    if deg[i] % 2 == 1:
        print('No')
        sys.exit()
    elif deg[i] >= 6:
        ok = True
    elif deg[i] == 4:
        f.append(i)

if ok:
    print('Yes')
    sys.exit()

if len(f) >= 3:
    print('Yes')
    sys.exit()

if len(f) <= 1:
    print('No')
    sys.exit()

t1 = f[0]
t2 = f[1]
seen = [0] * (N+1)
seen[t1] = 1
seen[t2] = 1
stack = [t1]

while stack:
    v = stack.pop()
    for u in adj[v]:
        if seen[u] == 0:
            seen[u] = 1
            stack.append(u)

if sum(seen) != N:
    print('Yes')
else:
    print('No')