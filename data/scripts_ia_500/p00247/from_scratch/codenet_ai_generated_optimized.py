from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        break
    maze = [list(input()) for _ in range(Y)]

    # グラフ上の氷の塊ごとにIDを付ける
    ice_id = [[-1]*X for _ in range(Y)]
    ice_groups = []
    id_count = 0

    for y in range(Y):
        for x in range(X):
            if maze[y][x] == 'X' and ice_id[y][x] == -1:
                q = deque()
                q.append((x,y))
                ice_id[y][x] = id_count
                positions = [(x,y)]
                while q:
                    cx, cy = q.popleft()
                    for d in range(4):
                        nx, ny = cx + dx[d], cy + dy[d]
                        if 0 <= nx < X and 0 <= ny < Y:
                            if maze[ny][nx] == 'X' and ice_id[ny][nx] == -1:
                                ice_id[ny][nx] = id_count
                                q.append((nx, ny))
                                positions.append((nx, ny))
                ice_groups.append(len(positions))
                id_count += 1

    # S,Gの座標も取得
    for y in range(Y):
        for x in range(X):
            if maze[y][x] == 'S':
                sx, sy = x, y
            if maze[y][x] == 'G':
                gx, gy = x, y

    # 各氷の塊をどれだけ踏んだか(カウント)をビット列や辞書でなくリストで持つ必要がある。
    # 状態空間は、座標＋各氷塊の使用回数(最大は氷塊の大きさの半分)
    # 実装上、各氷塊に対し踏んだ回数の上限は最大でhalf+1まででOK(それ以上は割れるため動けず)
    max_counts = [ (sz+1)//2 for sz in ice_groups ]

    from copy import deepcopy

    # 状態管理: (x,y)座標とアイスグループに対する使用回数リストをtupleにして記録
    # 状態数爆発を防ぐため、場所＋各氷塊での最低踏み数を記録する辞書や配列で管理
    # state_visited[y][x][tuple_of_counts] = True
    # ただし、tuple_of_countsの次元は最大(id_count<=12*12=144だが実際は少ない)
    # id_count最大12*12=144可能だが制限のため苦手。実際id_countは最大X*Y=144以下。
    # X,Y max12,なのでid_count max 144. 各カウント最大半数はX*Y/2 max 72程度。状態空間は爆発。
    # しかし、どの氷塊も使い切れないため実際の分岐は少ない。
    # Pythonで辞書メモ化とキューを使いBFSで解く。

    from collections import defaultdict

    visited = dict()
    start_counts = tuple(0 for _ in range(id_count))
    start_state = (sx, sy, start_counts)
    visited[start_state] = 0
    q = deque()
    q.append(start_state)

    ans = None
    while q:
        x, y, counts = q.popleft()
        step = visited[(x,y,counts)]
        if x == gx and y == gy:
            ans = step
            break
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < X and 0 <= ny < Y:
                c = counts
                cell = maze[ny][nx]
                if cell == '#':
                    continue
                # 氷上なら踏んだ回数を更新
                if cell == 'X':
                    gid = ice_id[ny][nx]
                    used = counts[gid]
                    if used + 1 > max_counts[gid]:
                        # 割れるため移動不可
                        continue
                    # countsはtupleなので更新用にリスト化
                    new_counts = list(counts)
                    new_counts[gid] = used + 1
                    new_counts = tuple(new_counts)
                else:
                    # 平原かS,G
                    new_counts = counts
                new_state = (nx, ny, new_counts)
                if new_state not in visited:
                    visited[new_state] = step + 1
                    q.append(new_state)

    print(ans)