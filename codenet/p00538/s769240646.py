import sys
sys.setrecursionlimit(100000)
N, *A = map(int, open(0).read().split())
memo = [[-1]*N for i in range(N)]
for i in range(N):
    memo[i][i] = A[i] if N % 2 else 0
def dfs(p, q, t):
    if memo[p][q] != -1:
        return memo[p][q]
    if t:
        memo[p][q] = r = max(A[p] + dfs((p+1)%N, q, 0), A[q] + dfs(p, (q-1)%N, 0))
    else:
        if A[p] < A[q]:
            memo[p][q] = r = dfs(p, (q-1)%N, 1)
        else:
            memo[p][q] = r = dfs((p+1)%N, q, 1)
    return r
ans = 0
for i in range(N):
    ans = max(ans, A[i] + dfs((i+1)%N, (i-1)%N, 0))
print(ans)