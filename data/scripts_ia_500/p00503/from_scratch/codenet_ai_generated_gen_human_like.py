N, K = map(int, input().split())
boxes = [list(map(int, input().split())) for _ in range(N)]

# 座標圧縮用のリスト
xs = set()
ys = set()
ds = set()

for x1, y1, d1, x2, y2, d2 in boxes:
    xs.add(x1)
    xs.add(x2)
    ys.add(y1)
    ys.add(y2)
    ds.add(d1)
    ds.add(d2)

xs = sorted(xs)
ys = sorted(ys)
ds = sorted(ds)

# 座標圧縮した座標の長さ
len_x = len(xs)
len_y = len(ys)
len_d = len(ds)

# 圧縮座標での各区間の長さ
dx = [xs[i+1] - xs[i] for i in range(len_x - 1)]
dy = [ys[i+1] - ys[i] for i in range(len_y - 1)]
dd = [ds[i+1] - ds[i] for i in range(len_d - 1)]

# 各体素がいくつの魚の生息範囲に含まれているかを管理する3次元配列を作るのはメモリ的にきついので
# 代わりに差分加算する方式を使う（3Dの差分は実装が複雑なので、鯖コンのN<=50の特性を活かして
# 範囲を走査して直接カウントする方法にする）

# 座標圧縮したインデックスを調べる関数
def find_index(arr, val):
    # valは必ずarrに含まれているはずなのでbinary searchで見つける
    from bisect import bisect_left
    return bisect_left(arr, val)

# 重なりを管理する3D配列としてはサイズが大きすぎるため、
# すべての体素を走査するのではなく、各体素を一つずつ走査してカウントするのは無理
# 代わりに差分積分的に考え、各生息範囲ごとに1を足す差分範囲加算を3D BITや3D差分配列で行い、
# 最後に各体素について、何匹の魚が含まれているか計算する
#
# しかし3D差分配列をサイズ(<=100)の座標圧縮結果で作成し、合算し、
# 最後に集計する方法が現実的。

# 3D差分配列
count = [[[0]*(len_d) for _ in range(len_y)] for __ in range(len_x)]

# 各生息範囲に対して差分を加える関数
def add_range(x1i, y1i, d1i, x2i, y2i, d2i):
    # 差分配列に立方体を加算
    # 差分配列は (x,y,d) の座標で前方含めて加算・減算して使う
    count[x1i][y1i][d1i] += 1
    if x2i < len_x:
        count[x2i][y1i][d1i] -= 1
    if y2i < len_y:
        count[x1i][y2i][d1i] -= 1
    if d2i < len_d:
        count[x1i][y1i][d2i] -= 1
    if x2i < len_x and y2i < len_y:
        count[x2i][y2i][d1i] += 1
    if x2i < len_x and d2i < len_d:
        count[x2i][y1i][d2i] += 1
    if y2i < len_y and d2i < len_d:
        count[x1i][y2i][d2i] += 1
    if x2i < len_x and y2i < len_y and d2i < len_d:
        count[x2i][y2i][d2i] -= 1

for x1, y1, d1, x2, y2, d2 in boxes:
    x1i = find_index(xs, x1)
    x2i = find_index(xs, x2)
    y1i = find_index(ys, y1)
    y2i = find_index(ys, y2)
    d1i = find_index(ds, d1)
    d2i = find_index(ds, d2)
    add_range(x1i, y1i, d1i, x2i, y2i, d2i)

# 3D累積和をとって重なり数を求める
for x in range(len_x):
    for y in range(len_y):
        for d in range(1, len_d):
            count[x][y][d] += count[x][y][d-1]

for x in range(len_x):
    for y in range(1, len_y):
        for d in range(len_d):
            count[x][y][d] += count[x][y-1][d]

for x in range(1, len_x):
    for y in range(len_y):
        for d in range(len_d):
            count[x][y][d] += count[x-1][y][d]

# 条件を満たす体素の体積を合計
result = 0
for x in range(len_x - 1):
    for y in range(len_y - 1):
        for d in range(len_d - 1):
            if count[x][y][d] >= K:
                vol = dx[x] * dy[y] * dd[d]
                result += vol

print(result)