# 入力された夜店の情報と制約条件から最大楽しさを求める問題
# 方針：
# ・ 夜店は番号順にしか訪れられないため、順にDPで検討
# ・ DP配列dp[i][t] : i番目までの夜店を考慮し、時刻tまでに遊び終えたときの最大楽しさ
# ・ 状態遷移では、i番目の夜店を選ぶか選ばないかを検討
# ・ 選ぶ場合は、遊ぶ時間帯が花火の時刻Sをまたがず、かつTを超えないことを確認し、時刻t-B_iに遡って状態を参照
# ・ 選ばない場合はdp[i-1][t]の最大値を引き継ぐ
# ・ 最終的にdp[N][t]の最大値を答えとする

import sys
input = sys.stdin.readline

N, T, S = map(int, input().split())
stores = [tuple(map(int, input().split())) for _ in range(N)]  # (A_i, B_i)

# dpは2次元配列だとメモリや計算量が大きいため、1次元dpで工夫する
# dp[t] := t時刻までに遊び終えたときの最大楽しさ
dp = [-1] * (T + 1)
dp[0] = 0  # 初期状態：0時刻で何も遊ばず楽しさ0

for i in range(N):
    A_i, B_i = stores[i]
    # 遊ぶ時間の制約：
    # 遊ぶ期間: [x, x + B_i)
    # この期間が花火時刻Sをまたがないための条件：
    # x + B_i <= S or x >= S
    # Tを超えない
    new_dp = dp[:]  # 今回の夜店を選ぶ場合の更新用

    for t in range(T - B_i +1):
        if dp[t] < 0:
            continue
        start = t  # 夜店iを時刻startから遊ぶ
        end = start + B_i
        # 花火の条件を満たすか確認
        if not (end <= S or start >= S):
            continue
        # Tを超えないか
        if end > T:
            continue
        # dpの更新
        if new_dp[end] < dp[t] + A_i:
            new_dp[end] = dp[t] + A_i
    dp = new_dp

# dp配列の最大値が答え
print(max(dp))