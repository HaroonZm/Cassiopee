N = int(input())
nums = list(map(int, input().split()))

# dp[pos][value] = 数字posまで見て、計算結果がvalueとなる通り数
# 途中の値は0~20の範囲のみなのでそれ以外は0
dp = [ [0]*21 for _ in range(N-1) ]
dp[0][nums[0]] = 1

for i in range(1, N-1):
    for v in range(21):
        if dp[i-1][v] == 0:
            continue
        # 足す
        nv = v + nums[i]
        if 0 <= nv <= 20:
            dp[i][nv] += dp[i-1][v]
        # 引く
        nv = v - nums[i]
        if 0 <= nv <= 20:
            dp[i][nv] += dp[i-1][v]

# 最後 nums[N-1] と等号を作る
print(dp[N-2][nums[N-1]])