import sys
from functools import partial

sys.setrecursionlimit(10**5)

def parse_grid(h):
    return [list(map(int, input().split())) for _ in range(h)]

def adjacent(w, h, x, y):
    return (
        (nx, ny)
        for dx in (-1, 0, 1)
        for dy in (-1, 0, 1)
        if (dx or dy)
        and 0 <= (nx := x + dx) < w
        and 0 <= (ny := y + dy) < h
    )

def dfs(grid, w, h, x, y, visited):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if visited[cy][cx]:
            continue
        visited[cy][cx] = True
        for nx, ny in adjacent(w, h, cx, cy):
            if grid[ny][nx] and not visited[ny][nx]:
                stack.append((nx, ny))

def main():
    while True:
        w, h = map(int, input().split())
        if not (w or h):
            break
        grid = parse_grid(h)
        visited = [[False]*w for _ in range(h)]
        count = 0
        for y in range(h):
            for x in range(w):
                if grid[y][x] and not visited[y][x]:
                    dfs(grid, w, h, x, y, visited)
                    count += 1
        print(count)

if __name__ == "__main__":
    main()