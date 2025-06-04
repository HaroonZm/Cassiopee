import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

# Directions: 0=N,1=E,2=S,3=W
# movement offsets by direction
dx = [0,1,0,-1]
dy = [-1,0,1,0]

while True:
    H,W,N = map(int,input().split())
    if H==0 and W==0 and N==0:
        break
    program = input().strip()
    maze = [list(input().rstrip('\n')) for _ in range(H)]

    # find start and goal positions
    for y in range(H):
        for x in range(W):
            if maze[y][x] == 'S':
                start = (x,y)
            elif maze[y][x] == 'G':
                goal = (x,y)

    # precompute direction after i-th turn
    # turn commands may be very long. direction after i turns:
    # 0-based; before any turn direction is North=0
    # L turn: direction = (direction + 3) %4 (or -1 mod4)
    # R turn: direction = (direction + 1) %4
    # We'll store dir_after_turn[i] = direction after i turns (i in [0..N])
    # dir_after_turn[0]=0 (initial)
    dir_after_turn = [0]*(N+1)
    d = 0
    for i, c in enumerate(program):
        if c == 'L':
            d = (d+3)%4
        else:
            d = (d+1)%4
        dir_after_turn[i+1] = d

    from collections import deque

    # State: (x,y,turns_used)
    # we can move forward without using turn.
    # When we want to turn, we must consume a turn command from program (if any left)
    # only if turns_used<N we can turn following that command, otherwise no turn possible
    visited = [[-1]*W for _ in range(H)]
    # We'll track visited by (x,y,turns_used)
    # But turns_used up to 1,000,000 and maze up to 1000x1000 is too big for 3d visited
    # Optimize:
    # The facing direction at turns_used is fixed by dir_after_turn[turns_used]
    # Since only turn_allowed in order, the facing direction is function of turns_used.
    # The state can be (x,y,turns_used)
    # We'll keep visited as a dict {(x,y,turns_used):True}
    # but too big, we optimize by combining visited states for the same (x,y) for minimal turns_used
    # Because turns_used is non-decreasing along a path; going back with more turns_used is useless
    # So we keep visited[x][y] = minimal turns_used found so far
    # and only process states with smaller turns_used for same cell

    from heapq import heappush, heappop
    # Use a priority queue by turns_used to process states with lower turns first
    # This ensures if we visit a cell with higher turns_used later, we can skip

    # visited[y][x] = minimal turns_used reached here
    visited = [[-1]*W for _ in range(H)]

    hq = []
    heappush(hq, (0, start[1], start[0])) # turns_used,y,x
    visited[start[1]][start[0]] = 0

    ans = False
    while hq:
        turns_used,y,x = heappop(hq)
        if (x,y) == goal:
            ans = True
            break
        # current facing direction after turns_used turns
        ddir = dir_after_turn[turns_used]

        # 1) Move forward if possible
        nx = x + dx[ddir]
        ny = y + dy[ddir]
        if 0<=nx<W and 0<=ny<H and maze[ny][nx] != '#':
            if visited[ny][nx] == -1 or visited[ny][nx] > turns_used:
                visited[ny][nx] = turns_used
                heappush(hq,(turns_used, ny, nx))
        # 2) Turn next command if any commands remain
        if turns_used < N:
            ndir = dir_after_turn[turns_used+1]
            # after turn, direction is ndir
            # Now can move forward (if possible) or wait
            # We only enqueue the turning action and let next loop move forward
            # State after turn: same cell, turns_used+1
            if visited[y][x]==-1 or visited[y][x] > turns_used+1:
                visited[y][x] = turns_used+1
                heappush(hq,(turns_used+1,y,x))
    print("Yes" if ans else "No")