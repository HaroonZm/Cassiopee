from collections import deque

def solve():
    N, M, A = map(int, input().split())
    grid = [list(input()) for _ in range(N)]

    # Find positions of S and G
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                sx, sy = i, j
            if grid[i][j] == 'G':
                gx, gy = i, j

    # Directions: 0=North,1=East,2=South,3=West
    # laser starts at S facing South (2)
    # Moves: dx, dy for N,E,S,W
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # Mirrors reflections:
    # P mirrors placed either at 45 or 225 degrees
    # Q mirrors placed either at 135 or 315 degrees
    #
    # Reflection rules, given direction and mirror type, 
    # return possible new directions if laser hits the mirror front side.
    #
    # The laser can only reflect if it hits the mirror front side:
    # For P mirror:
    # - if laser comes from North, it goes East
    # - if from East, it goes North
    # - if from South, it goes West
    # - if from West, it goes South
    #
    # For Q mirror:
    # - if laser comes from North, it goes West
    # - if from West, it goes North
    # - if from South, it goes East
    # - if from East, it goes South

    def reflect(direction, mirror_type):
        # returns new direction or None if no reflection
        if mirror_type == 'P':
            if direction == 0:
                return 1
            if direction == 1:
                return 0
            if direction == 2:
                return 3
            if direction == 3:
                return 2
        else: # 'Q'
            if direction == 0:
                return 3
            if direction == 3:
                return 0
            if direction == 2:
                return 1
            if direction == 1:
                return 2
        return None

    # We use BFS with states:
    # (x, y, direction, p_mirrors_left, q_mirrors_left)
    # We want to minimize total mirrors used = A - p_left + A - q_left = 2*A - (p_left + q_left)
    # We'll keep dist[x][y][direction][p_left][q_left] minimal mirrors used so far (or total mirrors placed)
    # But states are too big if we consider p_left and q_left separately (max 11 each).
    # Instead, since A <=10, and p + q = A, we can keep both separately since total states <= 100*100*4*11*11 ~ 4 840 000 acceptable.

    from heapq import heappush, heappop

    dist = [[[[[float('inf')] * (A+1) for _ in range(A+1)] for _ in range(4)] for _ in range(M)] for _ in range(N)]

    # start state
    # initial position at S, facing South (2), mirrors left: P = A, Q = A
    # mirrors used so far = 0
    # We'll store mirrors left, not mirrors used inside dist
    dist[sx][sy][2][A][A] = 0
    heap = []
    heappush(heap, (0, sx, sy, 2, A, A))  # (mirrors_used, x, y, direction, p_left, q_left)

    while heap:
        mirrors_used, x, y, d, p_left, q_left = heappop(heap)

        if dist[x][y][d][p_left][q_left] < mirrors_used:
            continue

        # If reached G, return mirrors_used
        if x == gx and y == gy:
            print(mirrors_used)
            return

        # Move forward in the current direction if possible
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#':
            # no mirror placement, just continue
            if dist[nx][ny][d][p_left][q_left] > mirrors_used:
                dist[nx][ny][d][p_left][q_left] = mirrors_used
                heappush(heap, (mirrors_used, nx, ny, d, p_left, q_left))

        # Try placing a mirror in current cell if empty and not S or G
        if grid[x][y] == '.':

            # Try P mirror if available
            if p_left > 0:
                nd = reflect(d, 'P')
                if nd is not None:
                    # The laser reflects, now moves in direction nd, so try to move in nd from current cell
                    nx, ny = x + dx[nd], y + dy[nd]
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#':
                        if dist[nx][ny][nd][p_left-1][q_left] > mirrors_used + 1:
                            dist[nx][ny][nd][p_left-1][q_left] = mirrors_used + 1
                            heappush(heap, (mirrors_used + 1, nx, ny, nd, p_left-1, q_left))

            # Try Q mirror if available
            if q_left > 0:
                nd = reflect(d, 'Q')
                if nd is not None:
                    nx, ny = x + dx[nd], y + dy[nd]
                    if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#':
                        if dist[nx][ny][nd][p_left][q_left-1] > mirrors_used + 1:
                            dist[nx][ny][nd][p_left][q_left-1] = mirrors_used + 1
                            heappush(heap, (mirrors_used + 1, nx, ny, nd, p_left, q_left-1))

    # If no path found
    print(-1)

if __name__ == "__main__":
    solve()