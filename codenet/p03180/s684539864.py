import sys
def input():
    return sys.stdin.readline()[:-1]

N = int(input())
a = [[int(x) for x in input().split()] for i in range(N)]
dp = [0] * (1<<N)
for S in range(1<<N):
    tmp = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if (S>>i)&1 and (S>>j)&1:
                tmp += a[i][j]
    dp[S] = max(0, tmp)
    T = (S-1)&S
    while T > 0:
        dp[S] = max(dp[S], dp[T]+dp[S^T])
        T = (T-1)&S
print(dp[(1<<N)-1])