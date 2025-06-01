from sys import stdin

def in_bounds(y, x, h, w):
    return 0 <= y < h and 0 <= x < w

h, w = map(int, stdin.readline().split())
g = [list(map(int, stdin.readline().split())) for _ in range(h)]

pos = [None] * (h * w)
for i, row in enumerate(g):
    for j, val in enumerate(row):
        pos[val - 1] = (i, j)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
stop = [set() for _ in range(h * w)]
ans = 0

for i in range(h * w):
    y, x = pos[i]
    val = g[y][x]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if in_bounds(ny, nx, h, w):
            neighbor_val = g[ny][nx]
            if neighbor_val < val:
                stop[i].update(stop[neighbor_val - 1])
    cnt = len(stop[i])
    if cnt >= 2:
        ans += 1
    elif cnt == 0:
        stop[i].add(val)

print(ans)