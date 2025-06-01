import sys
import bisect

input = sys.stdin.readline

N, M = map(int, input().split())
paintings = [tuple(map(int, input().split())) for _ in range(N)]
frames = [int(input()) for _ in range(M)]

# フレームの大きさをソート
frames.sort()

# 絵を大きさ、価値の昇順にソート
paintings.sort(key=lambda x: (x[0], x[1]))

# dp[k]: 価値の昇順に並べた展示済みの絵の列の中で k 番目まで考えたときの
# 最小の額縁の大きさの並びのうち長さkのもののうち最小の終わりの額縁サイズのキャパシティ
# だが今回は価値を基にして連続非減少配列を作る問題と同じ形に帰着させる
# 「価値の非減少且つ額縁の大きさの非減少」でなければならないので
# まず絵を価値で昇順にソートしておく（既に上で大きさ、価値の順でソートしている）

# 価値の非減少を維持しながら額縁の大きさを対応させるため、
# 構築すべきは額縁大きさのLIS(最長非減少部分列)を、
# 用意された額縁の中でサイズが絵の大きさに対して条件を満たすものとマッチングさせて
# 長さの最大化となるようにする。

# ここで、本来は「フレームの大きさごとの在庫」があるので使えるフレームの並びを管理しながら、
# 絵の「価値」の増加に合せて、額縁のサイズを非減少に並べていく必要がある。
# 解決策として、framesをsorted listとし、絵を価値昇順に処理しつつ、対応可能なframeを利用する。
# 絵iが入る額縁はサイズC_j >= S_i.
# また、隣の絵より価値も額縁サイズも非減少なので、絵を価値昇順に処理し、
# 各絵に対し、サイズS_i以上の額縁で最も小さいものを割り当てていけば、そのまま列を作れる。

# framesはソート済みなので、bisectで絵のS_i以上の額縁を探して確保していく。

import collections

# multisetっぽく扱うため、配列と削除管理用配列で管理
frames_multiset = frames
frames_multiset.sort()

count = 0

for S_i, V_i in paintings:
    # S_i以上の額縁を二分探索
    idx = bisect.bisect_left(frames_multiset, S_i)
    if idx == len(frames_multiset):
        # 使える額縁がない
        continue
    # 額縁使用
    frames_multiset.pop(idx)
    count += 1

print(count)