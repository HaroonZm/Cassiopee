# 入力を受け取る
N, M = map(int, input().split())
D = [int(input()) for _ in range(N)]
C = [int(input()) for _ in range(M)]

# dp[i][j] := j日目までに都市iにいるときの疲労度の最小値
# iは都市の番号（0〜N）、jは日数（0〜M）
# 初期状態として、都市0に0日目にいる疲労度は0、それ以外は大きな値で初期化
INF = 10**15
dp = [[INF] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 0

# 都市0は初日にいるので、そこからスタートし
# 各日ごとに待機するか、移動するかを選択
for day in range(M):
    for city in range(N + 1):
        if dp[city][day] == INF:
            continue
        # 待機：都市を変えずに日数だけ1増やす。疲労度は変わらない
        if day + 1 <= M:
            if dp[city][day + 1] > dp[city][day]:
                dp[city][day + 1] = dp[city][day]
        # 移動：都市cityからcity+1へ移動（可能なら）
        if city < N and day + 1 <= M:
            cost = D[city] * C[day]
            if dp[city + 1][day + 1] > dp[city][day] + cost:
                dp[city + 1][day + 1] = dp[city][day] + cost

# 答えは都市NにM日以内にたどり着いたときの疲労度の最小値
# M日以内なのでM日目だけでなくそれ以下の日でもよい
answer = min(dp[N][:M + 1])
print(answer)