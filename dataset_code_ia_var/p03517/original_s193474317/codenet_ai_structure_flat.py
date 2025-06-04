N, M, K = map(int, input().split())
C = [int(i) for i in input().split()]
table = []
t = K
for i in range(len(C)):
    if C[i]==0:
        t+=1
        C[i]=t

par = [i for i in range(t+1)]
rank = [0] * (t+1)

def find(x):
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x

for i in range(M):
    s, u, c = map(int, input().split())
    a, b = C[s-1], C[u-1]
    table.append((c, a, b))

table.sort()
ct = K - 1
ans = 0
for c, a, b in table:
    pa = find(a)
    pb = find(b)
    if pa != pb and ct > 0:
        if rank[pa] < rank[pb]:
            par[pa] = pb
        else:
            par[pb] = pa
        if rank[pa] == rank[pb]:
            rank[pa] += 1
        ans += c
        ct -= 1

if ct > 0:
    print(-1)
else:
    print(ans)