import sys
sys.setrecursionlimit(10**7)

# 解説:
# この問題はN個の施設の位置が与えられ、それらを2つのテーマ (グループ) に分ける。
# 同じテーマ内での最大のマンハッタン距離 M の最小値を求める。
#
# 制約から分かること:
# - すべて同じテーマにするのは禁止 (条件より)
# - 2つのグループはそれぞれのテーマを割り当てる
# - 各テーマに属する施設間の最大マンハッタン距離をできるだけ小さくしたい
#
# マンハッタン距離とは |x1 - x2| + |y1 - y2|
#
# 解法:
# 1. まずマンハッタン距離は軸変換すると扱いやすい。
#    任意の2点 (x, y), (x', y') について
#    |x - x'| + |y - y'| = max(|(x+y)-(x'+y')|, |(x-y)-(x'-y')|)
#
# 2. この性質を利用し、2つのグループに分けたときの最大距離を小さくするには、
#    2つのグループのx+yとx-yの値の範囲をできるだけ狭くすれば良い。
#
# 3. 問題は各施設にテーマを割り当てること。
#    条件「すべて同じテーマはだめ」を考慮すると、必ず2つ以上のテーマに分ける必要がある。
#
# 4. すべての施設を2つのグループに分ける方法はいくつかあり、性能的には全探索は不可。
#
# 5. 集合を2つに分けたときのテーマ内の最大距離は、それぞれのグループで距離の最大値を求める。
#
# 6. 二分探索を用いて、M (最大距離の候補) を決め打ちして、「M以下にできるか？」を判定する。
#
# 7. 判定方法は次のとおり:
#    - 距離がM以下なら、マンハッタン距離の特性からx+yの最大値と最小値の差がM以下かつ
#      x-yの最大値と最小値の差がM以下でなければならない。
#    - 与えられたMで二分探索しながら、どのように分けるかを考える。
#
# 8. より効率的なアプローチ:
#    - 全施設中でx+yの最大値と最小値の範囲差、x-yの最大値と最小値の範囲差を求める
#    - 2つのグループに分けるため、「境界線」を決めて分割する
#    - x+yまたはx-yでソートし、候補分割点を試す
#
# 9. 実装方針:
#    - 施設の配列を x+y でソートして連続区間で2分割できるかチェック（距離条件M以下か）
#    - 同様に x-y でソートして2分割できるかチェック
#    - これをMの二分探索と組み合わせて判定
    
# 入力
n = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

# x+y と x-y の列を作成
sum_coords = []
diff_coords = []
for x, y in points:
    sum_coords.append(x + y)
    diff_coords.append(x - y)

# 最大値・最小値の候補計算用
max_sum = max(sum_coords)
min_sum = min(sum_coords)
max_diff = max(diff_coords)
min_diff = min(diff_coords)

# マンハッタン距離の最大値の範囲は0からmax範囲まで
# max範囲は座標差の最大で十分大きい値をとる（xとyの差の最大絶対値の和）
max_coord_abs = max(abs(x) for x, y in points) + max(abs(y) for x, y in points)
right = max_coord_abs * 2  # 十分大きい初期値
left = 0

# 判定関数 (M以下で分割可能か):
# M以下になるためには、2つのグループに分けて、それぞれのグループの
# |x+y|の範囲差 ≤ Mかつ|x-y|の範囲差 ≤ M になる必要がある。

# ここで、全点を2グループに分けるので、グループ1を指定された区間に限定したら、
# グループ2は残りの点である。
#
# よって "sum_coords" でソートしたとき、
# iで分割した時 (group1: i未満, group2: i以上) の
# group1 と group2 のそれぞれのmaxとminの差がM以下になるか確認。
#
# 同様のことを "diff_coords" でも行う。

def can_divide(M):
    # 各点にsumとdiffを加えた情報を得る
    pts = []
    for i in range(n):
        pts.append( (sum_coords[i], diff_coords[i]) )
    # sumでソートしてプレフィックスとサフィックスでmin,maxを求める
    pts_sum_sorted = sorted(pts, key=lambda x: x[0])
    # prefix 最小最大 diff
    prefix_min_diff = [0]*n
    prefix_max_diff = [0]*n
    prefix_min_diff[0] = pts_sum_sorted[0][1]
    prefix_max_diff[0] = pts_sum_sorted[0][1]
    for i in range(1,n):
        prefix_min_diff[i] = min(prefix_min_diff[i-1], pts_sum_sorted[i][1])
        prefix_max_diff[i] = max(prefix_max_diff[i-1], pts_sum_sorted[i][1])
    # suffix 最小最大 diff
    suffix_min_diff = [0]*n
    suffix_max_diff = [0]*n
    suffix_min_diff[-1] = pts_sum_sorted[-1][1]
    suffix_max_diff[-1] = pts_sum_sorted[-1][1]
    for i in range(n-2,-1,-1):
        suffix_min_diff[i] = min(suffix_min_diff[i+1], pts_sum_sorted[i][1])
        suffix_max_diff[i] = max(suffix_max_diff[i+1], pts_sum_sorted[i][1])
    # sumの最大と最小はpts_sum_sortedの両端で分かるのでチェック可能
    for i in range(1,n):
        # group1: [0..i-1], group2: [i..n-1]
        sum1 = pts_sum_sorted[i-1][0] - pts_sum_sorted[0][0]    # group1のx+y差分
        sum2 = pts_sum_sorted[-1][0] - pts_sum_sorted[i][0]     # group2のx+y差分
        diff1 = prefix_max_diff[i-1] - prefix_min_diff[i-1]
        diff2 = suffix_max_diff[i] - suffix_min_diff[i]
        # どちらもM以下ならばOK
        if sum1 <= M and diff1 <= M and sum2 <= M and diff2 <= M:
            # すべての施設が同じグループにならないので、2分割されている
            if i < n:
                return True

    # 同じことをdiffでソートしてやる
    pts_diff_sorted = sorted(pts, key=lambda x: x[1])
    prefix_min_sum = [0]*n
    prefix_max_sum = [0]*n
    prefix_min_sum[0] = pts_diff_sorted[0][0]
    prefix_max_sum[0] = pts_diff_sorted[0][0]
    for i in range(1,n):
        prefix_min_sum[i] = min(prefix_min_sum[i-1], pts_diff_sorted[i][0])
        prefix_max_sum[i] = max(prefix_max_sum[i-1], pts_diff_sorted[i][0])
    suffix_min_sum = [0]*n
    suffix_max_sum = [0]*n
    suffix_min_sum[-1] = pts_diff_sorted[-1][0]
    suffix_max_sum[-1] = pts_diff_sorted[-1][0]
    for i in range(n-2,-1,-1):
        suffix_min_sum[i] = min(suffix_min_sum[i+1], pts_diff_sorted[i][0])
        suffix_max_sum[i] = max(suffix_max_sum[i+1], pts_diff_sorted[i][0])
    for i in range(1,n):
        diff1 = pts_diff_sorted[i-1][1] - pts_diff_sorted[0][1]
        diff2 = pts_diff_sorted[-1][1] - pts_diff_sorted[i][1]
        sum1 = prefix_max_sum[i-1] - prefix_min_sum[i-1]
        sum2 = suffix_max_sum[i] - suffix_min_sum[i]
        if diff1 <= M and sum1 <= M and diff2 <= M and sum2 <= M:
            if i < n:
                return True

    return False

# 二分探索でMを決定
while left < right:
    mid = (left + right) // 2
    if can_divide(mid):
        right = mid
    else:
        left = mid + 1

print(left)