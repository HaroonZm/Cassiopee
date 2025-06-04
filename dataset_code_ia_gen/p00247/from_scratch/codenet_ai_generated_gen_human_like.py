from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while True:
    X, Y = map(int, input().split())
    if X == 0 and Y == 0:
        break

    maze = [list(input()) for _ in range(Y)]

    # 探索前に氷の塊(connected components)を特定し、
    # 各氷の塊にIDを振り、サイズを記録する
    ice_id_map = [[-1]*X for _ in range(Y)]
    ice_sizes = []
    ice_id = 0

    for y in range(Y):
        for x in range(X):
            if maze[y][x] == 'X' and ice_id_map[y][x] == -1:
                # BFSで氷の塊のマスを調査
                queue = deque()
                queue.append((x,y))
                ice_id_map[y][x] = ice_id
                size = 0
                while queue:
                    cx, cy = queue.popleft()
                    size += 1
                    for dir in range(4):
                        nx = cx + dx[dir]
                        ny = cy + dy[dir]
                        if 0 <= nx < X and 0 <= ny < Y:
                            if maze[ny][nx] == 'X' and ice_id_map[ny][nx] == -1:
                                ice_id_map[ny][nx] = ice_id
                                queue.append((nx, ny))
                ice_sizes.append(size)
                ice_id += 1

    # スタートとゴールの位置を探す
    for y in range(Y):
        for x in range(X):
            if maze[y][x] == 'S':
                sx, sy = x, y
            elif maze[y][x] == 'G':
                gx, gy = x, y

    # 状態の扱い
    # 位置(x,y), 氷の塊ごとに現在までにその氷の塊で踏んだマスの数(0以上)
    # 氷の塊は最大でも12*12=144マスなので、id数は最大144未満だが実際はかなり少ない。
    # 各氷の塊の踏んだ回数をまとめて状態に入れるのは無理なので、
    # 重要なのは「各氷の塊で今までに踏んだ数が半数超えない」ことなので、
    # 状態は(x,y)座標と、各氷の塊の踏んだ回数の記録は実装しづらい。
    # そこで、各氷の塊の状況はID付きビットマップのように管理できない。
    # 最適アプローチは、「氷塊ごとに何回踏んだか」を状態の一部として持つ。
    # ただし、複数の氷の塊があると爆発条件判定が難しい。
    # そこで、探索状態に毎回の氷の塊への踏み回数を持った辞書を用いるのは計算量的に厳しい。
    # しかし、X, Yは最大12でデータ数40も大丈夫と判断して踏み回数を状態に含めてBFS実装。

    # 状態を(x,y, (氷塊ID毎の踏んだ数tuple))として扱う。
    # しかし、氷塊の最大個数はかなり小さいので、踏んだ回数を配列で持つ。
    # これは重いが解けるはず。

    from collections import defaultdict

    # idの数（氷塊の数）
    n_ice = len(ice_sizes)

    # 各氷塊で踏んだ数は0〜サイズまで。多くても12*12=144。
    # 状態の量軽減のため、サイズの半分以下までしか踏まないので踏んだ数は最大サイズ。
    # しかし全探索で解けるはず。

    start_ice = [0]*n_ice
    visited = dict()  # key=(x,y,タプル) value=歩数

    from copy import deepcopy

    q = deque()
    q.append( (sx, sy, tuple(start_ice), 0) )  # x,y,氷塊り踏んだ数のtuple, 歩数
    visited[(sx, sy, tuple(start_ice))] = 0

    while q:
        x, y, ice_count, step = q.popleft()
        if (x, y) == (gx, gy):
            print(step)
            break

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < X and 0 <= ny < Y:
                cell = maze[ny][nx]
                if cell == '#':
                    continue  # 山は進めない

                # 新しい氷のカウント配列を作る
                new_ice_count = list(ice_count)
                if cell == 'X':
                    iceblock_id = ice_id_map[ny][nx]
                    new_ice_count[iceblock_id] += 1
                    # 割れる条件チェック
                    if new_ice_count[iceblock_id] > ice_sizes[iceblock_id] // 2:
                        continue  # 割れたら動けないので進まない
                # '.' または S, G は普通に通れる

                new_ice_count_t = tuple(new_ice_count)
                state = (nx, ny, new_ice_count_t)
                if state not in visited:
                    visited[state] = step + 1
                    q.append((nx, ny, new_ice_count_t, step + 1))