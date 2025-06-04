import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# 座標圧縮のためx座標を抽出してソート
xs = sorted(set(p[0] for p in points))
# x座標に対応する各y座標のリストを作成
ys = [[] for _ in range(len(xs))]

for x, y in points:
    xi = bisect.bisect_left(xs, x)
    ys[xi].append(y)

# 各リストのy座標をソート
for i in range(len(ys)):
    ys[i].sort()

# クエリ処理
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # x軸の圧縮座標の範囲を求める
    left = bisect.bisect_left(xs, x1)
    right = bisect.bisect_right(xs, x2)
    count = 0
    # x座標が条件を満たすものに対してy座標を二分探索
    for i in range(left, right):
        yl = bisect.bisect_left(ys[i], y1)
        yr = bisect.bisect_right(ys[i], y2)
        count += (yr - yl)
    print(count)