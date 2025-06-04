import sys
sys.setrecursionlimit(10**7)

def dfs(x, y):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < w and 0 <= ny < h and grid[ny][nx] == 1:
                grid[ny][nx] = 0
                stack.append((nx, ny))

directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    count = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 1:
                count += 1
                grid[y][x] = 0
                dfs(x, y)
    print(count)