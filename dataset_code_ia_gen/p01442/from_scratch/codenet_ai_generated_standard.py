import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

while True:
    H, W, N = map(int, input().split())
    if H == 0 and W == 0 and N == 0:
        break
    program = input().strip()
    maze = [list(input().strip()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if maze[i][j] == 'S':
                sx, sy = i, j
            if maze[i][j] == 'G':
                gx, gy = i, j

    # Directions: 0=N,1=E,2=S,3=W
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    # Precompute dir changes for each turn command
    turns = []
    for c in program:
        turns.append(-1 if c == 'L' else 1)

    from collections import deque
    visited = [[[False]*(N+1) for _ in range(W)] for __ in range(H)]
    # state: (x, y, dir, turn_idx)
    q = deque()
    q.append((sx, sy, 0, 0))
    visited[sx][sy][0] = True

    ans = False
    while q:
        x, y, dir, t = q.popleft()
        if x == gx and y == gy:
            ans = True
            break
        # Move forward if possible
        nx, ny = x+dx[dir], y+dy[dir]
        if 0<=nx<H and 0<=ny<W and maze[nx][ny] != '#':
            if not visited[nx][ny][t]:
                visited[nx][ny][t] = True
                q.append((nx, ny, dir, t))
        # Turn if commands remain
        if t < N:
            ndir = (dir + turns[t]) % 4
            if not visited[x][y][t+1]:
                visited[x][y][t+1] = True
                q.append((x, y, ndir, t+1))
    print("Yes" if ans else "No")