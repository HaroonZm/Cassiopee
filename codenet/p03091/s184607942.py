import sys
input = sys.stdin.buffer.readline

N, M = map(int, input().split())
adj = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

deg = [len(A) for A in adj]
f = []
ok = 0
for i in range(1, N+1):
    if deg[i] % 2 == 1:
        print('No')
        exit()
    elif deg[i] >= 6:
        ok = 1
    elif deg[i] == 4:
        f.append(i)

if ok:
    print('Yes')
    exit()

if len(f) >= 3:
    print('Yes')
    exit()

if len(f) <= 1:
    print('No')
    exit()

t1, t2 = f[0], f[1]
seen = [0] * (N+1)
seen[t1] = 1
seen[t2] = 1
st = [t1]
while st:
    v = st.pop()
    for u in adj[v]:
        if seen[u] == 0:
            seen[u] = 1
            st.append(u)

if sum(seen) != N:
    print('Yes')
else:
    print('No')