def solve(n, w):
    dp = []
    for i in range(n+1):
        dp.append([0]*(n+1))
    for length in range(2, n+1):
        for left in range(n+1 - length):
            right = left + length
            if (length-2) % 2 == 0:
                if abs(w[left] - w[right-1]) <= 1 and dp[left+1][right-1] == right-left-2:
                    dp[left][right] = dp[left+1][right-1] + 2
                    continue
            for mid in range(left+1, right):
                total = dp[left][mid] + dp[mid][right]
                if dp[left][right] < total:
                    dp[left][right] = total
    return dp[0][n]

n = int(input())
while n != 0:
    w = list(map(int, input().split()))
    ans = solve(n, w)
    print(ans)
    n = int(input())