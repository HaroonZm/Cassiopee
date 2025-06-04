import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N,M= map(int,input().split())
A= list(map(int,input().split()))
intervals = [tuple(map(int,input().split())) for _ in range(M)]

end_at = [-1]*(N+1)
for L,R in intervals:
    if end_at[L-1]<R-1:
        end_at[L-1]= R-1

dp = [0]*(N+1)
max_back = [-1]*(N+1)

for i in range(N):
    dp[i+1] = max(dp[i+1], dp[i])
    if end_at[i]>=0:
        dp[end_at[i]+1] = max(dp[end_at[i]+1], dp[i])
    dp[i+1] = max(dp[i+1], dp[i]+A[i])
print(dp[N])