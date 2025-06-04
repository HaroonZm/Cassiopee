def neighbors(x, y, m, n):
    # 奇数行と偶数行で隣接ブロックの位置が変わる
    directions_even = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1)]
    directions_odd = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, -1), (1, 1)]
    result = []
    if y % 2 == 1:  # 奇数行
        for dx, dy in directions_odd:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= m and 1 <= ny <= n:
                result.append((nx, ny))
    else:  # 偶数行
        for dx, dy in directions_even:
            nx, ny = x + dx, y + dy
            if 1 <= nx <= m and 1 <= ny <= n:
                result.append((nx, ny))
    return result

import sys
from collections import deque

while True:
    line = ''
    while line.strip() == '':
        line = sys.stdin.readline()
        if not line:
            break
    if not line:
        break
    m_n = line.strip().split()
    if len(m_n) < 2:
        continue
    m, n = map(int, m_n)
    if m == 0 and n == 0:
        break
    s = int(sys.stdin.readline())
    stores = []
    for _ in range(s):
        x, y = map(int, sys.stdin.readline().split())
        stores.append((x, y))
    t = int(sys.stdin.readline())
    candidates = []
    for _ in range(t):
        p, q = map(int, sys.stdin.readline().split())
        candidates.append((p, q))

    # BFSで距離を求めるため、まず既設のコンビニすべてからの距離を求める
    # dist[i][x][y]: i番目のコンビニからの距離(1-based indexに注意)
    # ただし計算は効率化せず、各コンビニからの距離マップを個別に算出
    dist_list = []
    for i in range(s):
        dist = [[-1]*(n+1) for _ in range(m+1)]
        sx, sy = stores[i]
        dist[sx][sy] = 0
        que = deque()
        que.append((sx, sy))
        while que:
            x, y = que.popleft()
            for nx, ny in neighbors(x, y, m, n):
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    que.append((nx, ny))
        dist_list.append(dist)

    # 既設コンビニ＋候補1つずつのコンビニでのカバー数を計算
    max_cover = 0
    for candidate in candidates:
        # 候補を最後に追加した距離マップを作る
        dist_temp = []
        for d in dist_list:
            dist_temp.append([row[:] for row in d])
        # 候補の距離計算
        dist_cand = [[-1]*(n+1) for _ in range(m+1)]
        cx, cy = candidate
        dist_cand[cx][cy] = 0
        que = deque()
        que.append((cx, cy))
        while que:
            x, y = que.popleft()
            for nx, ny in neighbors(x, y, m, n):
                if dist_cand[nx][ny] == -1:
                    dist_cand[nx][ny] = dist_cand[x][y] + 1
                    que.append((nx, ny))
        dist_temp.append(dist_cand)

        cover_counts = [0]*(s+1)  # 既設s個＋候補1個＝s+1個のコンビニ

        # 各ブロックごとに最小距離のコンビニを調べる
        for x in range(1, m+1):
            for y in range(1, n+1):
                distances = []
                for i in range(s+1):
                    distances.append(dist_temp[i][x][y])
                # 距離が-1のものは無視
                valid = [(distances[i], i) for i in range(s+1) if distances[i] != -1]
                if not valid:
                    continue
                valid.sort()
                # 最短距離が一意か確認
                if len(valid) == 1 or valid[0][0] < valid[1][0]:
                    cover_counts[valid[0][1]] += 1
                # 同じ距離が複数あればどのコンビニにもカバーされない
        # 候補は最後のコンビニなのでindex s
        if cover_counts[s] > max_cover:
            max_cover = cover_counts[s]

    print(max_cover)