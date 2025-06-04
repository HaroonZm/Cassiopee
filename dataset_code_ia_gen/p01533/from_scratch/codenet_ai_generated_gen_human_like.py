from collections import deque
import sys

sys.setrecursionlimit(10**7)

W, H = map(int, input().split())
grid = [list(input()) for _ in range(H)]

# 移動方向
directions = [(1,0),(-1,0),(0,1),(0,-1)]

# 穴の位置リスト
holes = [(r,c) for r in range(H) for c in range(W) if grid[r][c] == '#']

# 穴までの距離を全マスについて計算する BFS
dist_to_hole = [[float('inf')] * W for _ in range(H)]
queue = deque()

for hr, hc in holes:
    dist_to_hole[hr][hc] = 0
    queue.append((hr, hc))

while queue:
    r, c = queue.popleft()
    for dr, dc in directions:
        nr, nc = r+dr, c+dc
        if 0 <= nr < H and 0 <= nc < W:
            nd = dist_to_hole[r][c] + 1
            if nd < dist_to_hole[nr][nc]:
                dist_to_hole[nr][nc] = nd
                queue.append((nr,nc))

# 位置情報の取得
points = []  # S, M..., G の順で格納
pos_dict = {}
for r in range(H):
    for c in range(W):
        ch = grid[r][c]
        if ch == 'S':
            pos_dict['S'] = (r,c)
        elif ch == 'G':
            pos_dict['G'] = (r,c)
        elif ch == 'M':
            if 'M' not in pos_dict:
                pos_dict['M'] = []
            pos_dict['M'].append((r,c))

points.append(pos_dict['S'])
if 'M' in pos_dict:
    points.extend(pos_dict['M'])
points.append(pos_dict['G'])

N = len(points)

# 2点間の移動コスト計算を BFS で行う関数
def bfs_cost(start_r, start_c):
    costs = [[float('inf')] * W for _ in range(H)]
    costs[start_r][start_c] = 0
    q = deque()
    q.append((start_r, start_c))
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r+dr, c+dc
            if 0 <= nr < H and 0 <= nc < W:
                if grid[nr][nc] == '#':
                    continue
                # 移動時間計算
                d = dist_to_hole[nr][nc]
                if d == 0:
                    time_cost = 1
                elif d == 1:
                    time_cost = 2
                elif d == 2:
                    time_cost = 3
                else:
                    time_cost = 1
                ncost = costs[r][c] + time_cost
                if ncost < costs[nr][nc]:
                    costs[nr][nc] = ncost
                    q.append((nr,nc))
    return costs

# 各拠点間の移動コストの計算
dist = [[0]*N for _ in range(N)]
cost_maps = []
for i in range(N):
    r,c = points[i]
    cost_map = bfs_cost(r,c)
    cost_maps.append(cost_map)

for i in range(N):
    for j in range(N):
        if i == j:
            dist[i][j] = 0
        else:
            rj, cj = points[j]
            dist[i][j] = cost_maps[i][rj][cj]

# TSP DP
# Sはindex 0、Gはindex N-1、Mは1~N-2
M_num = N - 2
INF = float('inf')
dp = [[INF]*(N) for _ in range(1<<M_num)]
# 初期状態: 巻物未取得状態0でS位置
dp[0][0] = 0

for mask in range(1<<M_num):
    for u in range(N):
        if dp[mask][u] == INF:
            continue
        # 巻物をまだ取ってないものに行く
        for m_idx in range(M_num):
            if not (mask & (1<<m_idx)):
                v = m_idx+1
                nmask = mask | (1<<m_idx)
                nd = dp[mask][u] + dist[u][v]
                if nd < dp[nmask][v]:
                    dp[nmask][v] = nd
        # 全巻物集めたらGに行ける
        if mask == (1<<M_num) - 1:
            v = N-1
            nd = dp[mask][u] + dist[u][v]
            if nd < dp[mask][v]:
                dp[mask][v] = nd

print(int(dp[(1<<M_num)-1][N-1]))