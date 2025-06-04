import sys
from collections import deque

W, H = map(int, sys.stdin.readline().split())
room = [list(sys.stdin.readline().rstrip()) for _ in range(H)]

# 探索用の方向ベクトル(上下左右)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 穴の位置を集める
holes = []
for y in range(H):
    for x in range(W):
        if room[y][x] == '#':
            holes.append((x, y))

# 穴からの距離を算出（穴から各タイルまでの距離の最小値を使う）
# 各タイルについて最短距離を求めるため、複数の穴を全てスタートとしたBFSを実施
dist_from_hole = [[-1]*W for _ in range(H)]
q = deque()
for (hx, hy) in holes:
    dist_from_hole[hy][hx] = 0
    q.append((hx, hy))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < W and 0 <= ny < H:
            if room[ny][nx] != '#' and dist_from_hole[ny][nx] == -1:
                dist_from_hole[ny][nx] = dist_from_hole[y][x] + 1
                q.append((nx, ny))

# 始点・終点・巻物の場所を特定
points = []
for y in range(H):
    for x in range(W):
        if room[y][x] == 'S':
            start = (x, y)
        if room[y][x] == 'G':
            goal = (x, y)
        if room[y][x] == 'M':
            points.append((x,y))

# 始点・巻物・終点のリスト
all_points = [start] + points + [goal]

# 移動コストの計算関数
def move_cost(px, py, nx, ny):
    # dist_from_holeが-1（穴からの距離なし）は1秒
    # それ以外は穴からの距離に応じて時間がかかる
    dist = dist_from_hole[ny][nx]
    if dist == -1 or dist >= 3:
        return 1
    else:
        return 4 - dist

# ある点から他の点への最短時間をBFSで計算
def bfs_cost(sx, sy):
    cost_map = [[-1]*W for _ in range(H)]
    cost_map[sy][sx] = 0
    q = deque()
    q.append((sx, sy))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < W and 0 <= ny < H:
                if room[ny][nx] != '#':
                    c = move_cost(x, y, nx, ny)
                    nc = cost_map[y][x] + c
                    if cost_map[ny][nx] == -1 or cost_map[ny][nx] > nc:
                        cost_map[ny][nx] = nc
                        q.append((nx, ny))
    return cost_map

# 各ポイント間の距離を求める
N = len(all_points)
dist_points = [[0]*N for _ in range(N)]
for i in range(N):
    x, y = all_points[i]
    cost_map = bfs_cost(x, y)
    for j in range(N):
        tx, ty = all_points[j]
        dist_points[i][j] = cost_map[ty][tx]

# 巻物の数
M_cnt = len(points)

# 巻物集めの巡回問題(スタート(0)からゴール(N-1)までに全M巻物を通る最短経路)
# bitDPの準備
INF = 10**9
dp = [[INF]*(N) for _ in range(1<<M_cnt)]

# 始点から巻物を持っていない状態
dp[0][0] = 0

for mask in range(1<<M_cnt):
    for pos in range(N):
        # dp[mask][pos]がまだ更新されていなければスキップ
        if dp[mask][pos] == INF:
            continue
        # 巻物を集める
        for nxt in range(1, M_cnt+1):
            if (mask >> (nxt-1)) & 1 == 0:  # 未収集の場合
                nmask = mask | (1<<(nxt-1))
                ndist = dp[mask][pos] + dist_points[pos][nxt]
                if dp[nmask][nxt] > ndist:
                    dp[nmask][nxt] = ndist
        # すべて集めたらゴールに行く
        if mask == (1<<M_cnt)-1:
            ndist = dp[mask][pos] + dist_points[pos][N-1]
            if dp[mask][N-1] > ndist:
                dp[mask][N-1] = ndist

# 結果
print(dp[(1<<M_cnt)-1][N-1])