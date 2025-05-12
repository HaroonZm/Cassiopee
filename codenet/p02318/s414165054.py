def levenshtein_dist(a,b):
    a_size = len(a)
    b_size = len(b)
    inf = float('inf')
    dp = [[a_size+b_size for i in range(a_size+1)] for _ in range(b_size+1)]
    for i in range(b_size+1):
        dp[i][0] = i
    for j in range(a_size+1):
        dp[0][j] = j

    for i in range(1,b_size+1):
        for j in range(1,a_size+1):
            if a[j-1] == b[i-1]:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]+1, dp[i][j-1]+1)
            else:
                dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j]+1, dp[i][j-1]+1)
    return dp

a = list(input())
b = list(input())
dp = levenshtein_dist(a,b)
print(dp[-1][-1])