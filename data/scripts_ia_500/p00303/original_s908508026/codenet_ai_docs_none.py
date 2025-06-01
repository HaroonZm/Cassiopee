N = int(input())
G = [[] for i in range(200)]
U = [0]*200
for i in range(N):
    u, r, v = input().split()
    u = int(u)-1
    v = int(v)-1
    U[u] = U[v+100] = 1
    if r == 'lock':
        G[u].append(v+100)
    else:
        G[v+100].append(u)
used = [0]*200
hold = [0]*200
def dfs(v):
    if used[v]:
        return 0
    r = 0
    hold[v] = 1
    for w in G[v]:
        if hold[w]:
            r = 1
            continue
        r |= dfs(w)
    hold[v] = 0
    used[v] = 1
    return r
for i in range(200):
    if not U[i]:
        continue
    if dfs(i):
        print(1)
        break
else:
    print(0)