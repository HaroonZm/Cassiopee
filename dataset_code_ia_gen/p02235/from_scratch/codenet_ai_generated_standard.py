q = int(input())
for _ in range(q):
    X = input().strip()
    Y = input().strip()
    m, n = len(X), len(Y)
    dp = [0]*(n+1)
    for i in range(1, m+1):
        prev = 0
        for j in range(1, n+1):
            temp = dp[j]
            dp[j] = prev+1 if X[i-1] == Y[j-1] else max(dp[j], dp[j-1])
            prev = temp
    print(dp[n])