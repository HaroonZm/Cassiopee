from sys import stdin
from collections import deque

def neighbors(x, y, h, w):
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1),
                   ( 0, -1),          ( 0, 1),
                   ( 1, -1), ( 1, 0), ( 1, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w:
            yield nx, ny

def count_islands(grid, h, w):
    islands = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j]:
                islands += 1
                queue = deque([(i, j)])
                grid[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    for nx, ny in neighbors(x, y, h, w):
                        if grid[nx][ny]:
                            grid[nx][ny] = 0
                            queue.append((nx, ny))
    return islands

def main():
    lines = iter(stdin.read().splitlines())
    while True:
        w_h = next(lines).split()
        w, h = map(int, w_h)
        if w == 0 and h == 0:
            break
        grid = [list(map(int, next(lines).split())) for _ in range(h)]
        print(count_islands(grid, h, w))

if __name__ == "__main__":
    main()