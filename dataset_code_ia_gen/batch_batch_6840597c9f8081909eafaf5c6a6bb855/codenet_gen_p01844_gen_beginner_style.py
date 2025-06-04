H, W, N = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

# 累積和を計算する
acc = [[0]*(W+1) for _ in range(H+1)]
for i in range(H):
    for j in range(W):
        acc[i+1][j+1] = acc[i][j+1] + acc[i+1][j] - acc[i][j] + a[i][j]

# 区画 (top,left) から (bottom-1,right-1) までの長方形の合計価格を返す関数
def rect_sum(top, left, bottom, right):
    return acc[bottom][right] - acc[top][right] - acc[bottom][left] + acc[top][left]

res = 0

if N == 2:
    # 一方向に切るだけでいい
    for i in range(1, H):
        part1 = rect_sum(0, 0, i, W)
        part2 = rect_sum(i, 0, H, W)
        res = max(res, min(part1, part2))
    for j in range(1, W):
        part1 = rect_sum(0, 0, H, j)
        part2 = rect_sum(0, j, H, W)
        res = max(res, min(part1, part2))

elif N == 3:
    # 縦に2回、縦に1回と横に1回、横に2回の切り方を全部試す
    # 縦縦
    for i in range(1, H-1):
        for k in range(i+1, H):
            p1 = rect_sum(0, 0, i, W)
            p2 = rect_sum(i, 0, k, W)
            p3 = rect_sum(k, 0, H, W)
            res = max(res, min(p1,p2,p3))
    # 横横
    for j in range(1, W-1):
        for l in range(j+1, W):
            p1 = rect_sum(0, 0, H, j)
            p2 = rect_sum(0, j, H, l)
            p3 = rect_sum(0, l, H, W)
            res = max(res, min(p1,p2,p3))
    # 縦横
    for i in range(1, H):
        for j in range(1, W):
            # 左上、右上、下の3つ
            p1 = rect_sum(0, 0, i, j)
            p2 = rect_sum(0, j, i, W)
            p3 = rect_sum(i, 0, H, W)
            res = max(res, min(p1,p2,p3))
            # 上、左下、右下
            p1 = rect_sum(0, 0, i, W)
            p2 = rect_sum(i, 0, H, j)
            p3 = rect_sum(i, j, H, W)
            res = max(res, min(p1,p2,p3))

else:
    # N ==4 の場合は縦横2回ずつの切り方を試す
    for i in range(1, H-2):
        for k in range(i+1, H-1):
            for j in range(1, W-2):
                for l in range(j+1, W-1):
                    p1 = rect_sum(0, 0, i, j)
                    p2 = rect_sum(0, j, i, l)
                    p3 = rect_sum(i, 0, k, j)
                    p4 = rect_sum(i, j, k, l)
                    p5 = rect_sum(k, 0, H, W)  # これは5区画になるので使わない
                    # 4つに分ける
                    p1 = rect_sum(0, 0, i, j)
                    p2 = rect_sum(0, j, i, l)
                    p3 = rect_sum(i, 0, k, j)
                    p4 = rect_sum(i, j, k, l)
                    p5 = rect_sum(k, l, H, W)  # これも5区画なので使わない
                    # 実際に4つに分けるのは縦横2回の切り方で以下のように:
                    #  0---j---l---W (横切断位置)
                    #  |p1 | p2 |    |
                    # i|---|----|----|
                    # k|p3 | p4 |    |
                    # H|---|----|----|
                    # なのでp4までしか使わない
                    p1 = rect_sum(0, 0, i, j)
                    p2 = rect_sum(0, j, i, W)
                    p3 = rect_sum(i, 0, k, j)
                    p4 = rect_sum(i, j, k, W)
                    p5 = rect_sum(k, 0, H, W)
                    vals = [p1, p2, p3, p4, p5]
                    # p5は分割外で使えないので上のように範囲を考える
                    p1 = rect_sum(0, 0, i, j)
                    p2 = rect_sum(0, j, i, W)
                    p3 = rect_sum(i, 0, k, j)
                    p4 = rect_sum(i, j, k, W)
                    p5 = rect_sum(k, 0, H, W)
                    # ほんとうに4分割ならp5は0にしないといけないので使わない
                    vals = [p1, p2, p3, p4]
                    res = max(res, min(vals))
    # ほかに縦に3つ切るやり方と横に3つ切るやり方も試す
    # 縦3分割
    for i in range(1, H-2):
        for k in range(i+1, H-1):
            for m in range(k+1, H):
                p1 = rect_sum(0, 0, i, W)
                p2 = rect_sum(i, 0, k, W)
                p3 = rect_sum(k, 0, m, W)
                p4 = rect_sum(m, 0, H, W)
                res = max(res, min(p1,p2,p3,p4))
    # 横3分割
    for j in range(1, W-2):
        for l in range(j+1, W-1):
            for o in range(l+1, W):
                p1 = rect_sum(0, 0, H, j)
                p2 = rect_sum(0, j, H, l)
                p3 = rect_sum(0, l, H, o)
                p4 = rect_sum(0, o, H, W)
                res = max(res, min(p1,p2,p3,p4))

print(res)