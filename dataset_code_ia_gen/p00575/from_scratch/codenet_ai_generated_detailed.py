# 入力値を取得する
A, B, C = map(int, input().split())

# A: 1回ログインで得られるコイン数
# B: 7日連続ログインでもらえる追加コイン数
# C: 目標コイン数

# 7回連続ログインしたときの1週間の合計コイン数
coins_per_week = 7 * A + B

# 最小の必要ログイン回数を大きい数から探索するよりも効率的に二分探索で求める方法もあるが、
# ここでは単純に数学的に求める。

# 目標コイン数に達するために必要な最小ログイン回数を初期化（大きめの値を仮置き）
min_logins = 10**9

# 以下の考え方：
# ログイン回数 n を考える
# n の中に整数個の「7日連続(w)」が含まれ、残りの日数 r (0 <= r < 7)
# とすると、n = 7w + r

# 得られるコイン数は、
# wセットごとに coins_per_week (7*A + B)
# 残り r日のそれぞれのログインで A 枚ずつ
# 合計 = w * coins_per_week + r * A

# これが C 以上となる最小の n を求める。

# w を0から、 C // A（最大でもこれくらいあれば十分） まで試す
# それぞれに対し、r を0～6で試し条件を満たす最小 n を記録

max_weeks = (C // coins_per_week) + 2  # 少し余裕を持ってループ回数を決める

for w in range(max_weeks):
    # w週間分のコイン
    coins_from_weeks = w * coins_per_week
    if coins_from_weeks >= C:
        # 7日連続ログインだけで達成可能ならば 7*w が回答候補
        min_logins = min(min_logins, 7 * w)
        break  # これ以上増やしても大きいだけなので探索終了
    else:
        # 残りの日数 r を0～6で探す
        for r in range(7):
            total_coins = coins_from_weeks + r * A
            if total_coins >= C:
                # 条件を満たす最小の n=w*7+r を記録
                min_logins = min(min_logins, 7 * w + r)
                break  # r は小さいほど良いので、見つかれば終了

print(min_logins)