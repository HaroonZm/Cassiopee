import sys
input = sys.stdin.readline

while True:
    n,m = map(int,input().split())
    if n == 0 and m == 0:
        break
    g = [list(map(float,input().split())) for _ in range(n)]
    if m == 1:
        print("1.00")
        continue
    dp = [[0.0]*n for _ in range(m+1)]
    # 1回目：どの肥料でも成長度1.0（ただし1回目は効果なし）
    for j in range(n):
        dp[1][j] = 1.0
    for i in range(2,m+1):
        for j in range(n):
            max_val = 0.0
            for k in range(n):
                val = dp[i-1][k]*g[k][j]
                if val > max_val:
                    max_val = val
            dp[i][j] = max_val
    ans = max(dp[m])
    print(f"{ans:.2f}")