from sys import stdin
from collections import deque

def inputlist():
    return list(map(int, stdin.readline().split()))

dx = (1, 1, 0, -1, -1, -1, 0, 1)
dy = (0, 1, 1, 1, 0, -1, -1, -1)

def dfs_iter(x, y, w, h, grid):
    if grid[x][y] == 0:
        return 0
    stack = deque([(x, y)])
    grid[x][y] = 0
    while stack:
        cx, cy = stack.pop()
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny]:
                grid[nx][ny] = 0
                stack.append((nx, ny))
    return 1

def main():
    while True:
        w, h = inputlist()
        if w == 0 and h == 0:
            break
        grid = [inputlist() for _ in range(h)]
        print(sum(
            dfs_iter(x, y, w, h, grid)
            for x in range(h) for y in range(w)
        ))

if __name__ == "__main__":
    main()