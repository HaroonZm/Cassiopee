n,k,m = map(int, input().split())

# 全体で使う数字は 1 から 2n まで
# 2行n列のグリッド
# 条件:
# ・右隣とは数値差の絶対値は k 以下
# ・下隣とは数値差の絶対値は k 以下
# ・右に隣がある時、左の数は右の数より小さい
# ・下に隣がある時、上の数は下の数より小さい

# 興味深いことに、番号を書くために1から2nまでの数字を全て使い、かつ
# 左から右、上から下で値は増加する必要があるから
# 実質的には2行n列のグリッドに小さい数字から順に割り振る順列のうち
# 隣接差がk以下になる場合を考える問題

# ただし数字の配置はすべての数字の全順列を探すと2n=最大200で爆発的なので難しい
# しかし、問題は初心者向けなので簡単に考える単純解を作るだけにする。
# ここでは、単純に 2行n列のグリッドに割り当てるすべての「増加する」配置を列挙し、隣接差の条件を調べる。
# 増加する配置は (必ず左から右、上から下で値が増加)→ 1から2nまでの数字が並ぶ順列で、
# かつ g[0][j] < g[0][j+1], g[1][j] < g[1][j+1], g[0][j] < g[1][j] を満たす.
# これはつまり、上段と下段でそれぞれ昇順の並びで、各列で上段の値が下段の値より小さい

# つまり、g[0]は1から2nまでの数字の昇順なn個の組み合わせ、g[1]は残りのn個の数字の昇順な組み合わせで、
# かつ g[0][j] < g[1][j] が成り立つ

# これだけでも combinations の数が大きいので、単純に枚挙は不可能だが、初期コードを書く。

import itertools

nums = list(range(1,2*n+1))
count = 0

for upper in itertools.combinations(nums, n):
    lower = [x for x in nums if x not in upper]
    upper = sorted(upper)
    lower = sorted(lower)
    # 条件 g[0][j] < g[1][j]
    if all(upper[j] < lower[j] for j in range(n)):
        # 隣接するセルの差をチェック
        ok = True
        for j in range(n):
            # 縦
            if abs(upper[j] - lower[j]) > k:
                ok = False
                break
            # 横 上段
            if j < n-1 and abs(upper[j] - upper[j+1]) > k:
                ok = False
                break
            # 横 下段
            if j < n-1 and abs(lower[j] - lower[j+1]) > k:
                ok = False
                break
        if ok:
            count += 1

print(count % m)