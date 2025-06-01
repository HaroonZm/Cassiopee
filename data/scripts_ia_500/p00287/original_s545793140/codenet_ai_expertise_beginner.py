from collections import deque

W, H, M = map(int, input().split())
lines = []
for _ in range(M):
    px, py, qx, qy = map(int, input().split())
    lines.append((px, py, qx, qy))

# Collect all unique x and y coordinates including borders
XS = [0, W]
YS = [0, H]
for px, py, qx, qy in lines:
    if px not in XS:
        XS.append(px)
    if qx not in XS:
        XS.append(qx)
    if py not in YS:
        YS.append(py)
    if qy not in YS:
        YS.append(qy)

XS.sort()
YS.sort()

# Create a dictionary to convert coordinates to indexes on a grid
def make_map(coords):
    mp = {}
    val = 0
    for c in coords:
        mp[c] = val
        val += 2
    val -= 1
    return mp, val

XM, max_x = make_map(XS)
YM, max_y = make_map(YS)

# Make a grid for walls and visited status
C = [[0]*(max_x) for _ in range(max_y)]
D = [[-1]*(max_x) for _ in range(max_y)]

# Mark the borders as walls
for i in range(max_y):
    C[i][0] = 1
    C[i][max_x-1] = 1
for j in range(max_x):
    C[0][j] = 1
    C[max_y-1][j] = 1

# Mark the lines as walls on the grid
for px, py, qx, qy in lines:
    if px == qx:
        if py > qy:
            py, qy = qy, py
        x = XM[px]
        for y in range(YM[py], YM[qy]+1):
            C[y][x] = 1
    else:
        if px > qx:
            px, qx = qx, px
        y = YM[py]
        for x in range(XM[px], XM[qx]+1):
            C[y][x] = 1

# Directions for BFS
directions = [(-1,0), (1,0), (0,-1), (0,1)]

# Group empty cells into areas using BFS
area_id = 0
for i in range(max_y):
    for j in range(max_x):
        if C[i][j] == 1 or D[i][j] != -1:
            continue
        queue = deque()
        queue.append((j, i))
        D[i][j] = area_id
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < max_x and 0 <= ny < max_y:
                    if C[ny][nx] == 0 and D[ny][nx] == -1:
                        D[ny][nx] = area_id
                        queue.append((nx, ny))
        area_id += 1

N = area_id

# Build graph connecting adjacent areas
G = [[] for _ in range(N)]
for i in range(1, max_y-1):
    for j in range(1, max_x-1):
        a = D[i-1][j]
        b = D[i+1][j]
        if a != -1 and b != -1 and a != b:
            G[a].append(b)
            G[b].append(a)
        a = D[i][j-1]
        b = D[i][j+1]
        if a != -1 and b != -1 and a != b:
            G[a].append(b)
            G[b].append(a)

Q = int(input())
from bisect import bisect

for _ in range(Q):
    sx, sy, gx, gy = map(int, input().split())
    # Find cell indexes for start and goal
    x0 = (bisect(XS, sx)-1)*2 + 1
    y0 = (bisect(YS, sy)-1)*2 + 1
    x1 = (bisect(XS, gx)-1)*2 + 1
    y1 = (bisect(YS, gy)-1)*2 + 1
    s = D[y0][x0]
    t = D[y1][x1]
    # BFS on graph to find shortest distance between areas
    dist = [-1]*N
    dist[s] = 0
    que = deque([s])
    while que:
        v = que.popleft()
        for w in G[v]:
            if dist[w] == -1:
                dist[w] = dist[v] + 1
                que.append(w)
    print(dist[t])