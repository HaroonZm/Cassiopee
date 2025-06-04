N, K = map(int, input().split())
fish = [tuple(map(int, input().split())) for _ in range(N)]

# 座標を分割するための座標圧縮用のリストを作る
xs = set()
ys = set()
ds = set()
for x1, y1, d1, x2, y2, d2 in fish:
    xs.add(x1)
    xs.add(x2)
    ys.add(y1)
    ys.add(y2)
    ds.add(d1)
    ds.add(d2)

xs = sorted(xs)
ys = sorted(ys)
ds = sorted(ds)

# 座標をindexに変換するための辞書を作成
x_id = {v:i for i,v in enumerate(xs)}
y_id = {v:i for i,v in enumerate(ys)}
d_id = {v:i for i,v in enumerate(ds)}

# 3次元グリッドのサイズ
X = len(xs)
Y = len(ys)
D = len(ds)

# グリッド初期化
# 3D配列は巨大なので3段階に分けて実装する：差分配列を使う
# 差分配列を用いて重なりのカウントを効率的に計算
diff = [[[0]*(D) for _ in range(Y)] for __ in range(X)]

for x1, y1, d1, x2, y2, d2 in fish:
    xi1, xi2 = x_id[x1], x_id[x2]
    yi1, yi2 = y_id[y1], y_id[y2]
    di1, di2 = d_id[d1], d_id[d2]
    diff[xi1][yi1][di1] += 1
    if xi2 < X:
        diff[xi2][yi1][di1] -= 1
    if yi2 < Y:
        diff[xi1][yi2][di1] -= 1
    if di2 < D:
        diff[xi1][yi1][di2] -= 1
    if xi2 < X and yi2 < Y:
        diff[xi2][yi2][di1] += 1
    if xi2 < X and di2 < D:
        diff[xi2][yi1][di2] += 1
    if yi2 < Y and di2 < D:
        diff[xi1][yi2][di2] += 1
    if xi2 < X and yi2 < Y and di2 < D:
        diff[xi2][yi2][di2] -= 1

# 累積和をとる
for xi in range(X):
    for yi in range(1, Y):
        for di in range(D):
            diff[xi][yi][di] += diff[xi][yi-1][di]

for xi in range(X):
    for yi in range(Y):
        for di in range(1, D):
            diff[xi][yi][di] += diff[xi][yi][di-1]

for xi in range(1, X):
    for yi in range(Y):
        for di in range(D):
            diff[xi][yi][di] += diff[xi-1][yi][di]

volume = 0
for xi in range(X-1):
    dx = xs[xi+1] - xs[xi]
    for yi in range(Y-1):
        dy = ys[yi+1] - ys[yi]
        for di in range(D-1):
            dz = ds[di+1] - ds[di]
            if diff[xi][yi][di] >= K:
                volume += dx * dy * dz

print(volume)