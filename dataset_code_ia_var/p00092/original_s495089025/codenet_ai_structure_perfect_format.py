table = [''] * 1002
dp = [[0] * 1002 for _ in range(1002)]

while True:
    n = int(input())
    if n == 0:
        break
    for r in range(n):
        table[r] = input()
    ans = 0

    for r in range(n):
        for c in range(n):
            if table[r][c] == '*':
                dp[r][c] = 0
            else:
                t = dp[r - 1][c - 1]
                if dp[r][c - 1] < t:
                    t = dp[r][c - 1]
                if dp[r - 1][c] < t:
                    t = dp[r - 1][c]
                t += 1
                dp[r][c] = t
                if t > ans:
                    ans = t
    print(ans)