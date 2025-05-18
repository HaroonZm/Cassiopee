from heapq import heappush, heappop

N, K = map(int, input().split())
a, b = (
    zip(*(map(int, input().split()) for _ in range(N - 1))) if N - 1 else
    ((), ())
)

MOD = 10**9 + 7

G = [set() for _ in range(N + 1)]
for x, y in zip(a, b):
    G[x].add(y)
    G[y].add(x)
q = []
v = [False for _ in range(N + 1)]
heappush(q, (1, 1))
ans = K
v[1] = True
while q:
    i, c = heappop(q)
    X = {x for x in G[i] if not v[x]}
    for l, j in enumerate(X):
        heappush(q, (j, 2))
        ans = (ans * (K - c - l)) % MOD
        v[j] = True

print(ans)