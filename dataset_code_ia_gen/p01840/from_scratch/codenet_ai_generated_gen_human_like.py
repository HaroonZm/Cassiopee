N, M, T = map(int, input().split())
a = list(map(int, input().split()))

# 太郎君は0時に書斎にいる
# 宅配便が届くたびに玄関へ移動（移動時間M往復）
# 勉強時間は書斎にいる時間の合計

max_study = 0

# 最初に玄関へ行く前までの勉強時間
max_study += a[0] - M  # 書斎にいてから玄関に向かう時間差分

# 次の宅配便までの間の勉強時間
for i in range(N - 1):
    max_study += a[i + 1] - a[i]

# 最後の宅配便からTまでの勉強時間
max_study += T - a[-1]

print(max_study)