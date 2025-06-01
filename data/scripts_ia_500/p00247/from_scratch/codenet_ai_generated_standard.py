from collections import deque
import sys

sys.setrecursionlimit(10**7)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def parse_ice_groups(grid, X, Y):
    group_id = [[-1]*X for _ in range(Y)]
    groups = []
    gid = 0
    for y in range(Y):
        for x in range(X):
            if grid[y][x] == 'X' and group_id[y][x] == -1:
                q = deque()
                q.append((x,y))
                group_id[y][x] = gid
                cells = [(x,y)]
                while q:
                    cx, cy = q.popleft()
                    for d in range(4):
                        nx, ny = cx+dx[d], cy+dy[d]
                        if 0 <= nx < X and 0 <= ny < Y and grid[ny][nx]=='X' and group_id[ny][nx]==-1:
                            group_id[ny][nx] = gid
                            q.append((nx, ny))
                            cells.append((nx, ny))
                groups.append(cells)
                gid +=1
    return group_id, groups

for line in sys.stdin:
    if not line.strip():
        continue
    X, Y = map(int,line.split())
    if X == 0 and Y == 0:
        break
    grid = [list(sys.stdin.readline().rstrip('\n')) for _ in range(Y)]
    start = None
    goal = None
    for y in range(Y):
        for x in range(X):
            if grid[y][x]=='S':
                start = (x,y)
                grid[y][x] = '.'
            elif grid[y][x]=='G':
                goal = (x,y)
                grid[y][x] = '.'

    group_id, groups = parse_ice_groups(grid,X,Y)
    group_sizes = [len(cells) for cells in groups]
    half_sizes = [size//2 for size in group_sizes]

    # State: (x,y,(ice_visited_counts_tuple))
    # To reduce size, keep ice_visited counts only for groups with at least 1 cell visited.
    # Use BFS, track minimal steps.

    from collections import defaultdict

    # Because each group visits count can be up to group size, and counts > half_size cannot proceed further
    # We'll store tuple of counts by group_id in visited, but only for groups actually visited

    # Since max group count <= X*Y, but typically less than 144, and groups less ~ less,
    # and each count max group_size, we can store counts as tuple of counts per group

    # For efficiency encode as a tuple of count per group (0 if not visited)
    # BFS queue holds (x,y, counts_tuple)
    # To avoid huge state space, prune states exceeding half counts

    init_counts = tuple(0 for _ in groups)
    visited = dict()
    visited[(start[0],start[1],init_counts)] = 0
    q = deque()
    q.append((start[0],start[1],init_counts))

    while q:
        x,y,counts = q.popleft()
        step = visited[(x,y,counts)]
        if (x,y) == goal:
            print(step)
            break
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if 0 <= nx < X and 0 <= ny < Y:
                c = grid[ny][nx]
                if c == '#':
                    continue
                ncounts = list(counts)
                gid = group_id[ny][nx]
                if gid == -1:
                    # not ice
                    key = (nx, ny, counts)
                    if key not in visited:
                        visited[key] = step+1
                        q.append((nx, ny, counts))
                else:
                    # ice
                    ncounts[gid] += 1
                    if ncounts[gid] <= half_sizes[gid]:
                        key = (nx, ny, tuple(ncounts))
                        if key not in visited:
                            visited[key] = step+1
                            q.append((nx, ny, tuple(ncounts)))
                    # else ice breaks, cannot continue