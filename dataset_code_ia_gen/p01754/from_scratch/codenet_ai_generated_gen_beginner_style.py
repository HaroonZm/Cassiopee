N, P, Q = map(int, input().split())
C = [int(input()) for _ in range(N)]

# 状態を自炊パワーにて管理するが、値が大きく変動するため辞書でDPを行う
dp = {Q: 0}  # 自炊パワー: 最大幸福度

for i in range(N):
    new_dp = {}
    for power in dp:
        # 食堂に行く場合
        new_power = power - 1
        val = dp[power] + C[i]
        if new_power in new_dp:
            if new_dp[new_power] < val:
                new_dp[new_power] = val
        else:
            new_dp[new_power] = val

        # 自炊する場合
        new_power = power + 1
        val = dp[power] + P * power
        if new_power in new_dp:
            if new_dp[new_power] < val:
                new_dp[new_power] = val
        else:
            new_dp[new_power] = val

    dp = new_dp

print(max(dp.values()))