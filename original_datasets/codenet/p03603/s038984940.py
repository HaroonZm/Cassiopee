from bisect import bisect_right

N = int(input())
P = list(map(int, input().split()))
X = [0] + list(map(int, input().split()))

C = [[] for _ in range(N+1)]
for i in range(N-1):
    C[P[i]].append(i+2)
W = [(-1, -1)] * (N+1)

def solve(v):
    if not C[v]:
        return (X[v], 0)
    A = []
    total = 0
    for u in C[v]:
        A.append(W[u])
        total += sum(W[u])
    n = len(A)
    dp = [set() for _ in range(N+1)]
    dp[0].add(0)
    for i in range(n):
        x, y = A[i]
        for z in dp[i]:
            dp[i+1].add(x + z)
            dp[i+1].add(y + z)
    B = sorted(dp[n])
    idx = bisect_right(B, X[v]) - 1
    if idx == -1:
        print("IMPOSSIBLE")
        exit()
    x, y = X[v], total - B[idx]
    return (x, y)

def rec(v, prex):
    for u in C[v]:
        rec(u, v)
    W[v] = solve(v)

rec(1, 0)
print("POSSIBLE")