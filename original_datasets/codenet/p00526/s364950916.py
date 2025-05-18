N = int(input())
a = list(map(int, input().split()))
dp = [[0]*3 for _ in [0]*N]
dp[0] = [1, 1, 1]
ans = 0

for i, (n1, n2) in enumerate(zip(a, a[1:]), start=1):
    if n1 != n2:
        for j in range(3):
            dp[i][j] = dp[i-1][j]+1
    else:
        dp[i][0] = 1
        if dp[i-1][2] > ans:
            ans = dp[i-1][2]
        for j in range(2, 0, -1):
            dp[i][j] = dp[i-1][j-1]+1

print(max(max(dp[-1]), ans))