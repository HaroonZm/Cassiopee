from collections import deque

H, W = map(int, input().split())
Area0 = [list(input()) for _ in range(H)]

N = int(input())

# 時刻ごとのグリッド変化情報を格納
# 変化はT[i], Area[i]
times = [0]
areas = [Area0]
for _ in range(N):
    t = int(input())
    area = [list(input()) for _ in range(H)]
    times.append(t)
    areas.append(area)

# スタートとゴールの座標を初期状態から取得
for i in range(H):
    for j in range(W):
        if Area0[i][j] == 'S':
            start = (i, j)
        if Area0[i][j] == 'G':
            goal = (i, j)

# 与えられた時刻tにおけるグリッドを取得する関数
def get_area(t):
    # timesは昇順に並んでいるので、t以下の最大のtimesのインデックスを探す
    # 例えばバイナリサーチでもよいがNが小さいので線形探索でも十分
    idx = 0
    for i in range(len(times)):
        if times[i] <= t:
            idx = i
        else:
            break
    return areas[idx]

# BFSで探索 (状態: (y,x,time,steps歩数))
# 移動は上下左右か留まる(ただし留まるのは歩数増加しない)
# 移動後1秒経過し、1秒経過後にグリッドが更新されるため、
# t秒目に行動 -> t+1秒目のグリッドを使って障害物判定
# ステートは (y,x,t) で管理し、歩数は別途管理する
# 探索コストは歩数。留まる場合はcost0、それ以外はcost1
# BFSはキューで最小歩数を求めるが留まる行動は優先のため
# dequeにて、留まる行動は前に、移動は後ろに追加して0-1 BFSに近い形で実装する

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

from sys import maxsize

visited = [[[maxsize]*(201+1) for _ in range(W)] for __ in range(H)]
# 時間は最大200まで (制約より T_N ≤ 200)

# 初期状態: start位置、時間0、歩数0
q = deque()
q.append((start[0], start[1], 0, 0))
visited[start[0]][start[1]][0] = 0

while q:
    y, x, t, steps = q.popleft()
    # 現在位置がgoalならstepsを答える
    if (y, x) == goal:
        print(steps)
        break
    # 時間が200を超えたら探索しない
    if t >= 200:
        continue

    # 次の時刻のグリッド
    next_area = get_area(t+1)
    # 「留まる」行動(歩数増えない)
    if next_area[y][x] != '#':
        if visited[y][x][t+1] > steps:
            visited[y][x][t+1] = steps
            q.appendleft((y, x, t+1, steps))  # コスト0なので前に追加

    # 上下左右に動く
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if 0 <= ny < H and 0 <= nx < W:
            # 次のグリッドで移動後の場所が障害物でないか
            if next_area[ny][nx] != '#':
                # 歩数は1増える
                if visited[ny][nx][t+1] > steps + 1:
                    visited[ny][nx][t+1] = steps + 1
                    q.append((ny, nx, t+1, steps+1))
else:
    print(-1)