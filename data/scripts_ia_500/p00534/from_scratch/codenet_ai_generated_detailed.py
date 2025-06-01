# 入力の受け取りと問題設定
N, M = map(int, input().split())  # 都市数と制限日数
D = [int(input()) for _ in range(N)]  # 距離のリスト D_i
C = [int(input()) for _ in range(M)]  # 天候の悪さのリスト C_j

# dp[i][j] を「j 日目までに都市 i にいるときの疲労度の最小値」と定義する
# 状態数は最大 1001*1001=約100万で十分効率的に計算可能
INF = 10**15
dp = [[INF] * (M + 1) for _ in range(N + 1)]

# 初期条件：都市0に初日にいる（移動も待機もしない）
dp[0][0] = 0

# 動的計画法で遷移を行う
for j in range(M):
    for i in range(N + 1):
        if dp[i][j] == INF:
            continue
        # 待機する場合：都市iにとどまる (疲労度変化なし)
        if j + 1 <= M:
            if dp[i][j + 1] > dp[i][j]:
                dp[i][j + 1] = dp[i][j]
        # 移動する場合：都市iから都市i+1へ進む（i < N の場合のみ）
        if i < N and j + 1 <= M:
            cost = dp[i][j] + D[i] * C[j]
            if dp[i + 1][j + 1] > cost:
                dp[i + 1][j + 1] = cost

# 答えは都市Nにいる可能な日(0~M)の最小値
ans = min(dp[N][1:])  # 1日目以降に都市Nに到達可能なので1日目からM日目の範囲で最小を探す
print(ans)