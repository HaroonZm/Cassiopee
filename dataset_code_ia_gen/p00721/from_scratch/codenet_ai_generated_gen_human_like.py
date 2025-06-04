from collections import deque
import sys

def bfs(start, grid, w, h):
    dist = [[-1]*w for _ in range(h)]
    dist[start[1]][start[0]] = 0
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0 <= nx < w and 0 <= ny < h:
                if grid[ny][nx] != 'x' and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((nx, ny))
    return dist

def main():
    input = sys.stdin.readline
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        
        grid = [list(input().rstrip('\n')) for _ in range(h)]
        dirty = []
        start = None
        
        for y in range(h):
            for x in range(w):
                if grid[y][x] == 'o':
                    start = (x, y)
                elif grid[y][x] == '*':
                    dirty.append((x, y))
        
        points = [start] + dirty
        n = len(points)
        
        # Compute distances between every pair of points
        dist_map = []
        for p in points:
            dist_map.append(bfs(p, grid, w, h))
        
        dist = [[-1]*n for _ in range(n)]
        possible = True
        for i in range(n):
            for j in range(n):
                d = dist_map[i][points[j][1]][points[j][0]]
                dist[i][j] = d
                if i != j and d == -1:
                    # No path between dirty tiles or start
                    if i == 0 or j == 0 or (i > 0 and j > 0):
                        if i == 0 or j == 0 or dist[i][j] == -1:
                            # If any dirty tile not reachable, no solution
                            if i == 0 or j == 0:
                                # From start to dirty tile
                                if j != 0 and dist[i][j] == -1:
                                    possible = False
                            else:
                                # Between dirty tiles
                                if dist[i][j] == -1:
                                    # May be OK, but keep consistent check
                                    pass
        
        if not possible:
            print(-1)
            continue
        
        # DP: bitmask over dirty tiles (max 10)
        # dp[mask][i]: min moves to have cleaned tiles in mask ending at point i
        SIZE = 1 << (n-1)
        dp = [[-1]*n for _ in range(SIZE)]
        dp[0][0] = 0
        
        for mask in range(SIZE):
            for i in range(n):
                if dp[mask][i] == -1:
                    continue
                for j in range(1, n):
                    if (mask & (1 << (j-1))) == 0 and dist[i][j] != -1:
                        new_mask = mask | (1 << (j-1))
                        val = dp[mask][i] + dist[i][j]
                        if dp[new_mask][j] == -1 or dp[new_mask][j] > val:
                            dp[new_mask][j] = val
        
        res = -1
        full_mask = SIZE - 1
        for i in range(n):
            if dp[full_mask][i] != -1:
                if res == -1 or res > dp[full_mask][i]:
                    res = dp[full_mask][i]
        print(res)

if __name__ == '__main__':
    main()