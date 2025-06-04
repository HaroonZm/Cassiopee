import sys
from collections import deque

def solve():
    W, H = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(H):
        grid.append(sys.stdin.readline().strip())

    R = []
    for i in range(H):
        R.append([0] * W)
    star_list = []
    free_cnt = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 's':
                sx = j
                sy = i
                R[i][j] = 1
                free_cnt += 1
            elif grid[i][j] == 'g':
                gx = j
                gy = i
            elif grid[i][j] == '*':
                star_list.append((j, i))
            elif grid[i][j] == '.':
                R[i][j] = 1
                free_cnt += 1

    moves = [(-1,0), (0,-1), (1,0), (0,1)]
    INF = 10 ** 18

    dist1 = []
    for i in range(H):
        dist1.append([INF] * W)
    q = deque()
    for (x, y) in star_list:
        dist1[y][x] = 0
        q.append((x, y))
    while q:
        x, y = q.popleft()
        c = dist1[y][x] + 1
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < W and 0 <= ny < H:
                if grid[ny][nx] == '*' or grid[ny][nx] == '#' or dist1[ny][nx] != INF:
                    continue
                dist1[ny][nx] = c
                q.append((nx, ny))

    dist2 = []
    for i in range(H):
        dist2.append([INF] * W)
    q = deque()
    dist2[gy][gx] = 0
    q.append((gx, gy))
    while q:
        x, y = q.popleft()
        c = dist2[y][x] + 1
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < W and 0 <= ny < H:
                if grid[ny][nx] == '*' or grid[ny][nx] == '#' or dist2[ny][nx] != INF:
                    continue
                dist2[ny][nx] = c
                q.append((nx, ny))

    left = 0
    right = 10 ** 21
    BASE = 10 ** 9
    for _ in range(71):
        mid = (left + right) // 2
        total = 0
        for i in range(H):
            for j in range(W):
                if R[i][j] == 0:
                    continue
                t1 = dist1[i][j] * BASE + mid
                t2 = dist2[i][j] * BASE
                total += min(t1, t2)
        if mid * free_cnt > total:
            right = mid
        else:
            left = mid

    ans = min(dist1[sy][sx] + left / BASE, dist2[sy][sx])
    sys.stdout.write("%.16f\n" % ans)

solve()