n = int(input())
movies = [tuple(map(int, input().split())) for _ in range(n)]

# 映画が上映されている日ごとのリストを作成（1～31日）
day_movies = [[] for _ in range(32)]
for i, (a, b) in enumerate(movies, start=1):
    for d in range(a, b + 1):
        day_movies[d].append(i)

# dp[i][j]: i日目にj番の映画を見た時の最大幸福度
# j=0 のときはまだ見ていない状態として使う
dp = [[-1] * (n + 1) for _ in range(32)]
dp[0][0] = 0

for day in range(1, 32):
    for movie_today in day_movies[day]:
        for movie_yesterday in range(n + 1):
            if dp[day - 1][movie_yesterday] < 0:
                continue
            # 初めて見る映画かどうかの判定はここではできないので別途管理する必要がある
            # しかし、dpで管理しているのは直前に見た映画だけで、
            # 過去に見た映画の記録が無いと幸福度を正しく計算できない
            # よってbitDPで管理する
            pass

# となるため、bitDPで実装し直す

# bitDP: day, watched_movies の状態をもつ
from collections import deque

# moviesの数は最大100なのでビットセット64ビットでは足りないが、
# 100ビットはPythonのintで問題ない
# ただし状態数は2^100使えないため、工夫が必要

# 問題の制約: 1 ≤ n ≤ 100, 日数は31日
# dp[day][watched_set]で状態数が膨大なので全探索は無理

# 別の解法
# 各日、上映されている映画の中から1本選ぶ
# 映画を初めて見たら100点、2回目以降は50点
# 映画を見る順番は日付順

# 貪欲に考えると、
# 初めて見る映画を優先して100点を得ることが有利だが、必ずしもそうとは限らない

# dp[day][movie_watched_set]はあきらめて、
# dp[day][j]: day日目にj番目の映画を見た時の最大幸福度を
# ただし初回なら100、2回目以降なら50
# そのために、どの映画を既に見たかを記録していく必要がある

# 状態としてはdp[day][last_movie][watched_movies_bitset]
# これも大きすぎる

# 制約を考慮すると日数31、n100でbitDPは難しいが
# 映画の数100にたいして日数31なので映画の閲覧回数は最大31回

# 試行錯誤のため、dp[day][movie_seen_set]で実装
# ただしmovie_seen_setはbitsetで100ビット

# ここでは映画の数が100なので、bitsetはintで扱う

dp = dict()
dp[(0, 0)] = 0  # (day, watched_bitset): happiness

for day in range(1, 32):
    new_dp = dict()
    # 今日上映している映画
    todays_movies = day_movies[day]
    for (prev_day, watched), val in dp.items():
        for m in todays_movies:
            bit = 1 << (m - 1)
            if watched & bit:
                # 既に見た映画
                score = 50
                new_watched = watched
            else:
                # 初めて見る映画
                score = 100
                new_watched = watched | bit
            key = (day, new_watched)
            if key not in new_dp or new_dp[key] < val + score:
                new_dp[key] = val + score
    dp = new_dp

print(max(dp.values()))