from math import factorial as F

comb = lambda n, k: 0 if n < 0 or k < 0 or n < k else F(n)//F(n-k)//F(k)

(n, k),MOD = (list(map(int, input().split())), 10**9+7)

def gen_dp(rows, cols):
    result = []
    for _ in range(rows):
        temp = []
        for __ in range(cols):
            temp.append(0)
        result.append(temp)
    return result

dp = gen_dp(k+1, n+1)

dp[0][0]=1
i = 1
while i <= k:
    for j in range(n+1):
        if j >= i:
            dp[i][j] = (dp[i-1][j] + dp[i][j-i])%MOD
        else:
            dp[i][j] = dp[i-1][j]
    i += 1

show = lambda arr: print(arr)
show(dp[k][n])