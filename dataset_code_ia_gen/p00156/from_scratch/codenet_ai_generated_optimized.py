from sys import stdin
from collections import deque

def solve():
    input_iter = iter(stdin.read().split())
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    while True:
        n = int(next(input_iter))
        m = int(next(input_iter))
        if n == 0 and m == 0:
            break
        grid = [next(input_iter) for _ in range(m)]

        # Find edges outside the castle (outside is reachable from border outside '#')
        # We can start BFS from all positions on the border that are not moat (no '#'),
        # because the ninja is outside the castle.
        # But here, outside is outside the grid. We can start from all border cells that are not moat,
        # and consider that as outside.

        # We'll treat the outside as all cells on the border that are not '#'.
        # From these positions, we try to reach '&' minimizing the count of moat climbs.

        # For each cell, we will store the minimal number of moat climbs needed to reach cell.
        # We'll use 0-1 BFS because stepping onto a '#' means we have to increment cost by 1
        # only when we enter '#' from a '.' or another '#'.
        # But problem says "堀に入る回数", i.e. number of times we climb up the moat => number
        # of times we enter a moat from a non-moat cell.
        # Actually, climbing out from moat is costly, but problem counts number of moat entries.
        # But ninja can swim in moat, so moving inside '#' doesn't increase count.
        # Climbing out is not modeled, but the problem clearly says number of moat entries is minimized.
        # So going from '.' to '#' increases count by 1, '.' to '.' no cost, '#' to '#' no cost, '#' to '.' no cost.

        # We'll implement 0-1 BFS with cost increments only when moving '.' -> '#'.
        # We can start from outside positions: all border cells that are '.' (not '#'), cost=0
        # Then propagate.

        dist = [[-1]*n for _ in range(m)]
        dq = deque()
        # Add all border positions not moat with cost=0
        for i in range(m):
            for j in [0,n-1]:
                if grid[i][j] != '#':
                    dist[i][j] = 0
                    dq.appendleft((i,j))
        for j in range(n):
            for i in [0,m-1]:
                if grid[i][j] != '#':
                    dist[i][j] = 0
                    dq.appendleft((i,j))
        while dq:
            x,y = dq.popleft()
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and dist[nx][ny]==-1:
                    cost = dist[x][y]
                    # If moving from non '#' to '#', cost increases by 1
                    if grid[x][y] != '#' and grid[nx][ny] == '#':
                        cost += 1
                    dist[nx][ny] = cost
                    if grid[x][y] != '#' and grid[nx][ny] == '#':
                        dq.append((nx,ny))
                    else:
                        dq.appendleft((nx,ny))

        # Find position of '&'
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '&':
                    print(dist[i][j])
                    break

solve()