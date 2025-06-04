# 入力の読み込みと問題設定に基づくDP解法を実装する

# D日間、N種類の服の情報をもとに、
# 各日に適した服を選びながら、
# 連続する日の服の派手さの差の合計の最大値を求める。

# 方針：
# - 各日の服の候補を先に求める
# - dp[i][j] を「i日目にj番目の候補の服を着たときの最大派手さ差合計」と定義
# - dpはi=1から初期化し、i>1はdp[i-1]から遷移
# - 最終的にdp[D]の中の最大値が答え

# 計算量はO(D * N^2)でD,N最大200なので十分高速

D, N = map(int, input().split())
T = [int(input()) for _ in range(D)]

clothes = [tuple(map(int, input().split())) for _ in range(N)]
# clothes[j] = (A_j, B_j, C_j)

# 各日に着られる服のインデックスを記録
candidates = []
for day in range(D):
    temp = []
    t = T[day]
    for j in range(N):
        A, B, C = clothes[j]
        if A <= t <= B:
            temp.append(j)
    candidates.append(temp)

# dp[i][k]: i日目(iは0-based)にcandidates[i][k]の服を着たときの、
# 最大派手さ差合計
dp = []
# 1日目のdp初期化（差分は発生しないため0）
dp.append([0] * len(candidates[0]))

for i in range(1, D):
    dp.append([-1] * len(candidates[i]))
    for k, cur_cloth_idx in enumerate(candidates[i]):
        cur_C = clothes[cur_cloth_idx][2]
        max_val = -1
        for l, prev_cloth_idx in enumerate(candidates[i-1]):
            if dp[i-1][l] == -1:
                continue
            prev_C = clothes[prev_cloth_idx][2]
            cost = dp[i-1][l] + abs(cur_C - prev_C)
            if cost > max_val:
                max_val = cost
        dp[i][k] = max_val

# 最終日に着る服の派手さ差合計の最大値を出力
print(max(dp[D-1]))