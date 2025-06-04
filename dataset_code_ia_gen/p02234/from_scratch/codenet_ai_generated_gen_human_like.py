n = int(input())
dims = [tuple(map(int, input().split())) for _ in range(n)]

# dimensions array where p[i] = number of rows of matrix i,
# and p[i+1] = number of columns of matrix i
p = [dims[0][0]] + [dims[i][1] for i in range(n)]

dp = [[0]*(n) for _ in range(n)]

for length in range(2, n+1):
    for i in range(n-length+1):
        j = i + length - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + p[i]*p[k+1]*p[j+1]
            if cost < dp[i][j]:
                dp[i][j] = cost

print(dp[0][n-1])