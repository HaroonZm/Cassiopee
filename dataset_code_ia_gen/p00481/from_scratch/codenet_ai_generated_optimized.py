import sys
from collections import deque

def main():
    input = sys.stdin.readline
    H, W, N = map(int, input().split())
    grid = [input().rstrip() for _ in range(H)]

    positions = [None] * (N + 1)
    for i in range(H):
        for j in range(W):
            c = grid[i][j]
            if c == 'S':
                positions[0] = (i, j)
            elif c.isdigit():
                positions[int(c)] = (i, j)

    def bfs(start, goal):
        dist = [[-1]*W for _ in range(H)]
        dist[start[0]][start[1]] = 0
        q = deque([start])
        while q:
            x, y = q.popleft()
            if (x, y) == goal:
                return dist[x][y]
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x+dx, y+dy
                if 0 <= nx < H and 0 <= ny < W and dist[nx][ny] == -1 and grid[nx][ny] != 'X':
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    total_time = 0
    current_pos = positions[0]
    for cheese_level in range(1, N+1):
        total_time += bfs(current_pos, positions[cheese_level])
        current_pos = positions[cheese_level]

    print(total_time)

if __name__ == "__main__":
    main()