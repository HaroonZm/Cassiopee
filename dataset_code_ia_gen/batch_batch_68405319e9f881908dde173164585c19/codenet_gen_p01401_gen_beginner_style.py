from collections import deque

def solve(w, h, grid):
    # 宝珠の最大番号を探す
    max_seal = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j].isdigit():
                n = int(grid[i][j])
                if n > max_seal:
                    max_seal = n
    # 封印を順番に壊していくため、現在の座標を管理
    # 最初はSの位置からスタート
    start = None
    goal = None
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)

    # 封印の番号は1からmax_sealまで
    # 封印番号nの宝珠の位置をリストで持つ
    seals = [[] for _ in range(max_seal + 1)]
    for i in range(h):
        for j in range(w):
            c = grid[i][j]
            if c.isdigit():
                seals[int(c)].append((i, j))
    # 現在の座標をスタートにセット
    current = start
    time = 0

    def bfs_find(target_positions, start_pos):
        # start_posからtarget_positionsのいずれかに最短距離の経路を探す
        visited = [[False]*w for _ in range(h)]
        q = deque()
        q.append((start_pos[0], start_pos[1], 0))
        visited[start_pos[0]][start_pos[1]] = True
        while q:
            y, x, dist = q.popleft()
            # もし今いる位置が目標の宝珠位置なら距離を返す
            if (y, x) in target_positions:
                return dist, (y, x)
            for dy, dx in [(0,1),(0,-1),(1,0),(-1,0)]:
                ny, nx = y+dy, x+dx
                if 0 <= ny < h and 0 <= nx < w and not visited[ny][nx]:
                    if grid[ny][nx] != '#':  # 壁がないと仮定
                        visited[ny][nx] = True
                        q.append((ny, nx, dist+1))
        return None, None

    # 各封印を順番に壊す
    for seal_num in range(1, max_seal +1):
        # 封印の宝珠の位置に行く
        d, pos = bfs_find(seals[seal_num], current)
        time += d
        current = pos

    # 最後にGに行く
    d, pos = bfs_find([goal], current)
    time += d

    return time

while True:
    line = input().strip()
    if line == '':
        continue
    w, h = map(int, line.split())
    if w == 0 and h == 0:
        break
    grid = []
    for _ in range(h):
        row = input().split()
        grid.append(row)
    print(solve(w, h, grid))