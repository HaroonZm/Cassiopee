def neighbors(x, y, m, n):
    # 隣接する六角形のブロックの座標を返す（範囲内のみ）
    result = []
    if y % 2 == 1:  # 奇数行
        candidates = [
            (x, y - 1), (x, y + 1),
            (x - 1, y), (x + 1, y),
            (x - 1, y + 1), (x - 1, y - 1)
        ]
    else:  # 偶数行
        candidates = [
            (x, y - 1), (x, y + 1),
            (x - 1, y), (x + 1, y),
            (x + 1, y + 1), (x + 1, y - 1)
        ]
    for cx, cy in candidates:
        if 1 <= cx <= m and 1 <= cy <= n:
            result.append((cx, cy))
    return result

import sys

for line in sys.stdin:
    if line.strip() == '':
        continue
    m, n = map(int, line.strip().split())
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
        px, py = map(int, sys.stdin.readline().split())
        candidates.append((px, py))

    # まず既存店での距離を計算し、どのブロックがどの店にカバーされているかを判定するため,
    # 幅優先探索で全ブロックの最短距離を求める。
    # ただし距離が同じ複数の店がある場合はカバーなしとする。
    def calc_coverage(stores_list):
        from collections import deque
        dist = [[-1]*(n+1) for _ in range(m+1)]  # 距離
        cover = [[-1]*(n+1) for _ in range(m+1)] # どの店にカバーされているか（複数最短距離は-2）
        queue = deque()
        # 初期値セット
        for i, (sx, sy) in enumerate(stores_list):
            dist[sx][sy] = 0
            cover[sx][sy] = i
            queue.append((sx, sy))
        while queue:
            cx, cy = queue.popleft()
            for nx, ny in neighbors(cx, cy, m, n):
                nd = dist[cx][cy] + 1
                if dist[nx][ny] == -1:
                    dist[nx][ny] = nd
                    cover[nx][ny] = cover[cx][cy]
                    queue.append((nx, ny))
                elif dist[nx][ny] == nd:
                    # 同じ距離で異なる店があるならカバーなしにする
                    if cover[nx][ny] != cover[cx][cy]:
                        cover[nx][ny] = -2
        return cover

    # 既存店でのカバー状況を計算する
    cover_exist = calc_coverage(stores)

    max_cover = 0
    for cpx, cpy in candidates:
        # この候補地を付け加えた店リストを作る
        new_stores = stores + [(cpx, cpy)]
        cover_new = calc_coverage(new_stores)
        # 新店の番号は s になるので、新店でカバーされているブロックを数える
        count = 0
        for x in range(1, m+1):
            for y in range(1, n+1):
                if cover_exist[x][y] == -1:
                    # 既存店にカバーされていなかった場所だけを対象
                    if cover_new[x][y] == s:
                        count += 1
        if count > max_cover:
            max_cover = count

    print(max_cover)