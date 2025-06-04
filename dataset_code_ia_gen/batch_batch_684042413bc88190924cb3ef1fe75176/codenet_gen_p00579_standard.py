import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

intervals = [[] for _ in range(N+1)]
for _ in range(M):
    L, R = map(int, input().split())
    intervals[R].append(L)

dp = [0]*(N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + A[i-1]
    for L in intervals[i]:
        dp[i] = max(dp[i], dp[L-1]+A[i-1])
print(dp[N])