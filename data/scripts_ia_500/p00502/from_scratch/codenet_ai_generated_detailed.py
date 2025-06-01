# 入力を受け取って、この問題を解くPythonのプログラムを作成します。
# アプローチ：
# 1. 各日の最高気温から、その日に着られる服のリストを作成。
# 2. 動的計画法(DP)を用いて、最大の「派手さの差の絶対値の合計」を計算。
#    - dp[i][j]：i日目(0-index)にj番目の服を着たときの最大値
#    - i日目に着られる服の中で全てのkの日目(i-1)の服について遷移を考える
# 3. 最終日まで計算したら、dp[D-1]の最大値が答え。

D, N = map(int, input().split())  # 日数D、服の種類数N

T = [int(input()) for _ in range(D)]  # 各日の最高気温

clothes = [tuple(map(int, input().split())) for _ in range(N)]
# clothes[j] = (A_j, B_j, C_j)

# 1. 各日に着られる服を求める
available = []
for i in range(D):
    day_temp = T[i]
    candidates = []
    for j in range(N):
        A, B, C = clothes[j]
        if A <= day_temp <= B:
            candidates.append((j, C))
    available.append(candidates)

# 2. DP配列準備
# dp[i][j]: i日目に着る服がavailable[i][j]番目(の服)のときの最大派手さ差合計
# jはavailable[i]のインデックスなので注意！
# ここで、服の番号jはavailable[i][j][0]、派手さはavailable[i][j][1]
dp = []
for i in range(D):
    dp.append([-1]*len(available[i]))

# 3. 初日のdpは0（差分がないため）
for j in range(len(available[0])):
    dp[0][j] = 0

# 4. 状態遷移
for i in range(1, D):
    for j_curr, (c_curr_id, c_curr) in enumerate(available[i]):
        max_val = -1
        for j_prev, (c_prev_id, c_prev) in enumerate(available[i-1]):
            if dp[i-1][j_prev] < 0:
                continue
            val = dp[i-1][j_prev] + abs(c_prev - c_curr)
            if val > max_val:
                max_val = val
        dp[i][j_curr] = max_val

# 5. 最終日のdpの最大値が答え
print(max(dp[-1]))