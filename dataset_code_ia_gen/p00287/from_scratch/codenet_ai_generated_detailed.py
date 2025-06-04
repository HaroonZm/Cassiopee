import sys
sys.setrecursionlimit(10**7)

# 壁によって分割された領域(領域ごとにIDを割り当てる)を構築し、
# 各点がどの領域に属するか判定。点の属する領域が分かれば、
# 領域間の隣接関係（壁を1つ越えると別領域）をグラフとして表現できる。
# そのグラフ上で、始点と終点の領域ID間の最短距離を壁越え回数として求める。

# 1. 入力から水平壁と垂直壁に分ける。
# 2. 水平方向の座標で区切られた縦帯で管理し、垂直壁で分割する。（垂直壁はx座標で区切るライン）
# 3. 垂直方向の座標で区切られた横帯で管理し、水平壁で分割する。（水平壁はy座標で区切るライン）
# 4. 得られた区画をグラフのノードとし、壁1本越えで隣接（上下左右の区画）とする。
# 5. 各点の属する区画を座標の区間を参照し特定する。
# 6. 各クエリ毎にBFSで最小壁越え数を求めて出力。

# --------------------------------
# 実装詳細：
# 壁の端点を境界としてx座標、y座標の分割点の集合を作成。
# 区画はこれら区切り点の連続する区間ごとにできる矩形とみなす。
# 隣接区画の判定は区画同士が共有する辺が壁でない場合に隣接とする。
# 隣接関係は、区間の番号をノード番号として管理する。
# --------------------------------

# 入力読み込み
W, H, M = map(int, input().split())
h_walls = []  # 水平壁（y座標が一定）
v_walls = []  # 垂直壁（x座標が一定）
for _ in range(M):
    px, py, qx, qy = map(int, input().split())
    if py == qy:
        # 水平壁
        y = py
        x1, x2 = sorted([px, qx])
        h_walls.append((y, x1, x2))
    else:
        # 垂直壁
        x = px
        y1, y2 = sorted([py, qy])
        v_walls.append((x, y1, y2))
Q = int(input())
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# 壁の座標の分割点（座標圧縮用）
# 区画は壁の座標を境界とする
x_coords = set([0, W])
y_coords = set([0, H])

for y, x1, x2 in h_walls:
    y_coords.add(y)
for x, y1, y2 in v_walls:
    x_coords.add(x)

x_list = sorted(x_coords)
y_list = sorted(y_coords)

# 座標 -> インデックス変換用dict
x_idx = {x: i for i, x in enumerate(x_list)}
y_idx = {y: i for i, y in enumerate(y_list)}

# 区画数（矩形数）＝(x方向区間数) * (y方向区間数)
W_num = len(x_list) - 1
H_num = len(y_list) - 1

# 各区画の上下左右の境界に壁があるかどうかを管理する配列
# 壁は線の長さ(区間)の部分だけ存在するため、
# 隣接判定は壁の範囲に注意して行う。

# 便利にするために壁情報を2次元の区画境界にマッピングする。
# [i][j] に注目すると、x_list[i]～x_list[i+1], y_list[j]～y_list[j+1] の区画を表す。

# 垂直方向の壁：x=cの線分でy1～y2を分断
# この壁はx=cと一致する分割線のインデックスがkとして、
# x_list[k] == c であることを使う。
# 壁はx=c線の下にある区画(i-1,j)と上にある区画(i,j)の間にある。
# つまり垂直壁はx軸方向の区割り境界として現れる。

# 水平方向の壁：y=cの線分でx1～x2を分断
# y_list[l] == cであるとして
# 水平壁はy=c線の左の区画(i,j-1) と右の区画(i,j)の間にある。
# 水平壁はy軸方向の区割り境界として現れる。


# 垂直壁のマップ（x方向の区切り線数は len(x_list)）
# x_line_walls[k][j]: x_list[k]の線のうちy区切りjの位置に壁があるか
x_line_walls = [[False]*(H_num) for _ in range(len(x_list))]
for x, y1, y2 in v_walls:
    k = x_idx[x]  # 壁が存在するx分割線のindex
    # y1～y2にかかる区間jを特定（区画はy_list[j]～y_list[j+1]）
    # 壁はy1 <= y < y2 にかかる全区間を塞ぐ
    start_j = None
    end_j = None
    for j in range(H_num):
        # 区間 y_list[j]～y_list[j+1]
        # 区間が壁の範囲に重なれば塞ぐ
        if y_list[j+1] <= y1:
            continue
        if y_list[j] >= y2:
            break
        x_line_walls[k][j] = True

# 水平壁のマップ（y方向分割線数）
# y_line_walls[i][l]: y_list[l]の線のうちx区切りiの部分に壁があるか
y_line_walls = [[False]* (W_num) for _ in range(len(y_list))]
for y, x1, x2 in h_walls:
    l = y_idx[y]
    # x1～x2にかかる全区間iを塞ぐ
    for i in range(W_num):
        if x_list[i+1] <= x1:
            continue
        if x_list[i] >= x2:
            break
        y_line_walls[l][i] = True

# 区画のノードID = i*H_num + j
def node_id(i, j):
    return i*H_num + j

# グラフ作成（隣接リスト）
# 区画は W_num * H_num 個
N = W_num * H_num
graph = [[] for _ in range(N)]

# 隣接区画は上下左右
# ただし隣接区画間の境界に壁(線分)があれば移動不可
for i in range(W_num):
    for j in range(H_num):
        cur = node_id(i, j)
        # 上（j-1方向）と隣接
        if j > 0:
            # 区画(i, j)と(i, j-1)間の線は y_list[j] の水平境界
            # 水平壁の成否は y_line_walls[y_list_idx][i]
            if not y_line_walls[j][i]:
                graph[cur].append(node_id(i, j-1))
                graph[node_id(i, j-1)].append(cur)
        # 左（i-1方向）と隣接
        if i > 0:
            # 区画(i, j)と(i-1, j)間の線は x_list[i] の垂直境界
            # 垂直壁の成否は x_line_walls[i][j]
            if not x_line_walls[i][j]:
                graph[cur].append(node_id(i-1, j))
                graph[node_id(i-1, j)].append(cur)

# 点がどの区画に属するか判定
def find_section(x, y):
    # x_list, y_listは長さ順にソート済み
    # 区間x_list[i] < x < x_list[i+1]
    # 二分探索で高速化
    import bisect
    i = bisect.bisect_left(x_list, x)
    if x == x_list[i]:
        # 壁の上ではない(問題文より始点ゴールは壁上にないため)
        i -= 1
    j = bisect.bisect_left(y_list, y)
    if y == y_list[j]:
        j -= 1
    return node_id(i, j)

from collections import deque

# BFSで最短壁越え数を探索
def bfs(start, goal):
    if start == goal:
        return 0
    dist = [-1]*N
    dist[start] = 0
    que = deque([start])
    while que:
        u = que.popleft()
        if u == goal:
            return dist[u]
        for w in graph[u]:
            if dist[w] == -1:
                dist[w] = dist[u] + 1
                que.append(w)
    return -1  # 到達不可なら-1（問題条件下では無いはず）

for sx, sy, gx, gy in queries:
    start = find_section(sx, sy)
    goal = find_section(gx, gy)
    ans = bfs(start, goal)
    print(ans)