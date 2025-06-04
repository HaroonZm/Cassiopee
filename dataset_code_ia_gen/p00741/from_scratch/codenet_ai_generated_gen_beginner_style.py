def count_islands(w, h, grid):
    visited = [[False]*w for _ in range(h)]

    def dfs(x,y):
        stack = [(x,y)]
        while stack:
            cx, cy = stack.pop()
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < w and 0 <= ny < h:
                        if not visited[ny][nx] and grid[ny][nx] == 1:
                            visited[ny][nx] = True
                            stack.append((nx, ny))

    island_count = 0
    for y in range(h):
        for x in range(w):
            if grid[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                dfs(x,y)
                island_count += 1
    return island_count

while True:
    line = input()
    if line == "0 0":
        break
    w, h = map(int, line.split())
    grid = []
    for _ in range(h):
        row = list(map(int, input().split()))
        grid.append(row)
    print(count_islands(w,h,grid))