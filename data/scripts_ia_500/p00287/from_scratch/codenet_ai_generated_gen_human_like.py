import sys
sys.setrecursionlimit(10**7)

W, H, M = map(int, sys.stdin.readline().split())
walls = []
for _ in range(M):
    px, py, qx, qy = map(int, sys.stdin.readline().split())
    # Normalize segment so px, py is smaller point
    if (px, py) > (qx, qy):
        px, py, qx, qy = qx, qy, px, py
    walls.append((px, py, qx, qy))

Q = int(sys.stdin.readline())
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(Q)]

# グラフの各頂点は壁セグメントを越えた領域（壁ごとに分割される領域）
# 壁の交点を越えられないので、領域の分割は縦横の壁の交差点で分割される。
# 壁内部の相互関係を考えると、壁が遮る領域を区切り、点がどの領域にいるかを特定し、
# 領域間を移動するには壁を一つ越える必要がある。
# 問題は始点と終点のいる領域番号を求め、その間の壁数の最短を調べることに帰着。

# 壁はxまたはy軸に平行なので、縦壁と横壁に分類できる
vertical = []
horizontal = []
for px, py, qx, qy in walls:
    if px == qx:
        vertical.append((px, py, qx, qy))
    else:
        horizontal.append((px, py, qx, qy))

# 壁の座標による分割点を得る（壁の端点座標）
x_cuts = set([0, W])
y_cuts = set([0, H])
for px, py, qx, qy in walls:
    x_cuts.add(px)
    x_cuts.add(qx)
    y_cuts.add(py)
    y_cuts.add(qy)

# 座標圧縮
x_list = sorted(x_cuts)
y_list = sorted(y_cuts)

x_id = {x:i for i,x in enumerate(x_list)}
y_id = {y:i for i,y in enumerate(y_list)}

# 領域はx_list[i]～x_list[i+1], y_list[j]～y_list[j+1]の長方形
# 領域の数は (len(x_list)-1)*(len(y_list)-1)
# 領域番号をi*(Y-1)+jとする

Wn = len(x_list)-1
Hn = len(y_list)-1

# 領域間の壁(辺)設定
# 隣接領域同士が壁で遮られているか判定し、
# 遮られていなければ0コストで移動できる。
# 遮られているときは1コストで移動（壁を越える）

# まず、壁で遮られている領域間の辺を求める
# 隣接領域同士を全部チェックすると計算量多そうだが、
# M<=100なので縦横の壁の線分の位置だけ見ればよい。

# 隣接領域は横方向の隣と縦方向の隣のみ：
# - 水平方向：i, j と i+1, j が隣接
# - 垂直方向：i, j と i, j+1 が隣接

# 壁がある場合1か0で判定

# まず、壁の存在を2Dグリッドの横軸・縦軸方向の壁位置としてマークする
# 横方向の壁：y=?? のライン上を遮るx区間
# 縦方向の壁：x=?? のライン上を遮るy区間

# ある2つの隣接領域間を隔てる境界線（垂直または水平）上に
# 壁があるかどうかを判定し、あれば1、なければ0となる。

# 水平方向の境界線はy_list[j+1], 区間 [x_list[i], x_list[i+1])
# 縦方向の境界線はx_list[i+1], 区間 [y_list[j], y_list[j+1])

# 壁はそのラインにかかっているか判定

# 壁の座標圧縮の区間上を使いやすくするため、
# 壁をセット化して判定に用いる

# 便宜上、x_listとy_listの区間の中間座標を考えて動作確認

# 関数定義：2つの領域を遮る壁があるか判定

def has_wall_between(i1, j1, i2, j2):
    # 領域(i1,j1)と(i2,j2)は必ず隣接
    # i2 = i1 + 1, j2 = j1 または i2 = i1, j2 = j1 + 1
    if i1 == i2 and j2 == j1 + 1:
        # 垂直方向の隣接上下
        # 区間の境界は y_list[j2]
        # この境界線上に壁があるか
        line_y = y_list[j2]
        x_left = x_list[i1]
        x_right = x_list[i1 + 1]

        for px, py, qx, qy in walls:
            if py == qy and py == line_y:
                # 水平線分が境界線上にある場合
                # これが境界線と一致し、区間がかぶっていたら壁あり
                # check interval overlap
                seg_left = min(px, qx)
                seg_right = max(px, qx)
                if not (seg_right <= x_left or seg_left >= x_right):
                    return True
        return False

    elif j1 == j2 and i2 == i1 + 1:
        # 水平方向の隣接左右
        # 境界線は x_list[i2]
        line_x = x_list[i2]
        y_bottom = y_list[j1]
        y_top = y_list[j1 + 1]

        for px, py, qx, qy in walls:
            if px == qx and px == line_x:
                # 垂直線分が境界線上にある場合
                seg_bottom = min(py, qy)
                seg_top = max(py, qy)
                if not (seg_top <= y_bottom or seg_bottom >= y_top):
                    return True
        return False

    else:
        # 非隣接はここでは使わないはず
        return True  # safety

# 領域の番号変換関数
def node(i, j):
    return i*(Hn)+j

# グラフの構築 (0コストまたは1コストの辺)
# 各領域の隣接領域との壁越えコスト格納
from collections import deque

graph = [[] for _ in range(Wn*Hn)]

for i in range(Wn):
    for j in range(Hn):
        u = node(i, j)
        # 右側隣接
        if i+1 < Wn:
            v = node(i+1, j)
            cost = 1 if has_wall_between(i, j, i+1, j) else 0
            graph[u].append((v, cost))
            graph[v].append((u, cost))
        # 上側隣接
        if j+1 < Hn:
            v = node(i, j+1)
            cost = 1 if has_wall_between(i, j, i, j+1) else 0
            graph[u].append((v, cost))
            graph[v].append((u, cost))

# 点がどの領域にあるか判定
def find_area(x,y):
    # x_listと y_listの区間に含まれるindexを検索
    # x_list, y_listは昇順
    import bisect
    i = bisect.bisect_right(x_list, x) - 1
    j = bisect.bisect_right(y_list, y) - 1
    return node(i, j)

# 0-1 BFSを使い、壁越え回数の最小値を求める
def zero_one_bfs(start, goal):
    dist = [float('inf')] * (Wn*Hn)
    dist[start] = 0
    dq = deque()
    dq.append(start)
    while dq:
        u = dq.popleft()
        if u == goal:
            return dist[u]
        for v, cost in graph[u]:
            nd = dist[u] + cost
            if dist[v] > nd:
                dist[v] = nd
                if cost == 0:
                    dq.appendleft(v)
                else:
                    dq.append(v)
    return dist[goal]

for sx, sy, gx, gy in queries:
    start = find_area(sx, sy)
    goal = find_area(gx, gy)
    ans = zero_one_bfs(start, goal)
    print(ans)