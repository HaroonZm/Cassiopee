from collections import deque
from bisect import bisect
import sys
input=sys.stdin.readline

W, H, M = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(M)]

X_coords = {0, W}
Y_coords = {0, H}
for px, py, qx, qy in segments:
    X_coords.update((px, qx))
    Y_coords.update((py, qy))

X_sorted = sorted(X_coords)
Y_sorted = sorted(Y_coords)

def make_mapping(coords):
    mp = {}
    idx = 0
    for c in coords:
        mp[c] = idx
        idx += 2
    return mp, idx - 1

Xm, X_len = make_mapping(X_sorted)
Ym, Y_len = make_mapping(Y_sorted)

grid = [[0]*X_len for _ in range(Y_len)]
region = [[-1]*X_len for _ in range(Y_len)]

# Mark borders as walls
for y in (0, Y_len-1):
    for x in range(X_len):
        grid[y][x] = 1
for x in (0, X_len-1):
    for y in range(Y_len):
        grid[y][x] = 1

# Mark walls from segments
for px, py, qx, qy in segments:
    if px == qx:
        y0, y1 = sorted((py, qy))
        x = Xm[px]
        for y in range(Ym[y0], Ym[y1]+1):
            grid[y][x] = 1
    else:
        x0, x1 = sorted((px, qx))
        y = Ym[py]
        for x in range(Xm[x0], Xm[x1]+1):
            grid[y][x] = 1

directions = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs_label():
    label = 0
    for y in range(Y_len):
        for x in range(X_len):
            if grid[y][x] or region[y][x] != -1:
                continue
            region[y][x] = label
            queue = deque([(x,y)])
            while queue:
                cx, cy = queue.popleft()
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < X_len and 0 <= ny < Y_len:
                        if grid[ny][nx] == 0 and region[ny][nx] == -1:
                            region[ny][nx] = label
                            queue.append((nx, ny))
            label += 1
    return label

N = bfs_label()

graph = [[] for _ in range(N)]
for y in range(1, Y_len-1):
    for x in range(1, X_len-1):
        for (a1, b1), (a2, b2) in [((y-1,x), (y+1,x)), ((y,x-1), (y,x+1))]:
            r1 = region[a1][b1]
            r2 = region[a2][b2]
            if r1 != -1 and r2 != -1 and r1 != r2:
                graph[r1].append(r2)
                graph[r2].append(r1)

Q = int(input())
for _ in range(Q):
    sx, sy, gx, gy = map(int, input().split())
    sx_idx = (bisect(X_sorted, sx)-1)*2 + 1
    sy_idx = (bisect(Y_sorted, sy)-1)*2 + 1
    gx_idx = (bisect(X_sorted, gx)-1)*2 + 1
    gy_idx = (bisect(Y_sorted, gy)-1)*2 + 1

    s_region = region[sy_idx][sx_idx]
    g_region = region[gy_idx][gx_idx]

    assert s_region != -1 and g_region != -1

    if s_region == g_region:
        print(0)
        continue

    dist = [-1] * N
    dist[s_region] = 0
    queue = deque([s_region])
    while queue and dist[g_region] == -1:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.append(v)
    print(dist[g_region])