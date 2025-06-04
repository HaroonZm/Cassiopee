from collections import deque

def solve():
    N, M, A = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    # Directions: 0=North,1=East,2=South,3=West
    dxy = [(-1,0),(0,1),(1,0),(0,-1)]
    # Find S and G
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                sx, sy = i, j
            elif grid[i][j] == 'G':
                gx, gy = i, j
    # We start from laser direction south = 2
    initial_dir = 2
    # visited[x][y][dir][p_used][q_used] = minimal mirrors used to reach
    # To limit memory, we avoid a 5D visited; instead track best mirrors used per state
    # Store minimal mirrors usage per position/direction/p_used/q_used:
    INF = 10**9
    from collections import defaultdict
    visited = dict()
    # Key: (x,y,dir,p_used,q_used) -> minimal mirrors used
    # BFS with deque, aim for minimal mirrors used
    dq = deque()
    # Initialize
    # mirrors used = p_used + q_used
    dq.append((0, sx, sy, initial_dir, 0, 0))
    visited[(sx, sy, initial_dir, 0, 0)] = 0

    while dq:
        mirrors, x, y, dir, p_used, q_used = dq.popleft()
        if (x, y) == (gx, gy):
            print(mirrors)
            return
        nx, ny = x + dxy[dir][0], y + dxy[dir][1]
        # Move forward until blocked or out of bounds
        if not (0 <= nx < N and 0 <= ny < M):
            continue
        if grid[nx][ny] == '#':
            continue
        # Move forward without placing mirror
        key = (nx, ny, dir, p_used, q_used)
        if key not in visited or visited[key] > mirrors:
            visited[key] = mirrors
            dq.appendleft((mirrors, nx, ny, dir, p_used, q_used))  # no new mirror: front of deque

        # We can place mirror here if cell is '.' (not S or G or '#')
        # but mirrors cannot be placed on S or G squares
        if grid[nx][ny] == '.':

            # Try place type P mirror if still available
            if p_used < A:
                # P mirror change direction as per:
                # dir 0->1, 1->0, 2->3, 3->2
                ndir = None
                if dir == 0: ndir = 1
                elif dir == 1: ndir = 0
                elif dir == 2: ndir = 3
                elif dir == 3: ndir = 2
                keym = (nx, ny, ndir, p_used+1, q_used)
                if keym not in visited or visited[keym] > mirrors+1:
                    visited[keym] = mirrors+1
                    dq.append((mirrors+1, nx, ny, ndir, p_used+1, q_used))

            # Try place type Q mirror if still available
            if q_used < A:
                # Q mirror change direction as per:
                # dir 0->3, 3->0, 1->2, 2->1
                ndir = None
                if dir == 0: ndir = 3
                elif dir == 3: ndir = 0
                elif dir == 1: ndir = 2
                elif dir == 2: ndir = 1
                keym = (nx, ny, ndir, p_used, q_used+1)
                if keym not in visited or visited[keym] > mirrors+1:
                    visited[keym] = mirrors+1
                    dq.append((mirrors+1, nx, ny, ndir, p_used, q_used+1))
    print(-1)

if __name__=="__main__":
    solve()