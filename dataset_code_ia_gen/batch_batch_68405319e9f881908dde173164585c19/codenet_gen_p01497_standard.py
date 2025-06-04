from collections import deque
def serialize(grid):
    return tuple(tuple(row) for row in grid)
def in_grid(r,c):
    return 0<=r<4 and 0<=c<4
def simulate(grid):
    # simulate chain reactions with waterdrops until stable
    grids = [list(row) for row in grid]
    dirs = [(-1,0),(1,0),(0,-1),(0,1)]
    while True:
        blow_positions = []
        for r in range(4):
            for c in range(4):
                if grids[r][c]>=5:
                    blow_positions.append((r,c))
        if not blow_positions:
            break
        # bubbles explode
        waterdrops_positions = dict()
        for r,c in blow_positions:
            grids[r][c]=0
            # initial waterdrops positions: 4 at (r,c)
            # at t=1 waterdrops move to neighbor squares
            for dr,dc in dirs:
                nr,nc=r+dr,c+dc
                if in_grid(nr,nc):
                    waterdrops_positions[(nr,nc)] = waterdrops_positions.get((nr,nc),0)+1
        # propagate waterdrops one second at a time until no more hits
        while waterdrops_positions:
            hits = dict()
            new_waterdrops = dict()
            for pos,count in waterdrops_positions.items():
                r,c=pos
                if grids[r][c]>0:
                    # waterdrops hit bubble
                    hits[pos] = hits.get(pos,0)+count
                else:
                    # waterdrops move on
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if in_grid(nr,nc):
                            new_waterdrops[(nr,nc)] = new_waterdrops.get((nr,nc),0)+count
            # apply hits
            for (r,c),num in hits.items():
                grids[r][c]+=num
            # waterdrops that hit bubbles disappear
            waterdrops_positions = new_waterdrops
    return grids
def all_empty(grid):
    for r in range(4):
        for c in range(4):
            if grid[r][c]>0:
                return False
    return True
def solve(init_grid):
    from collections import deque
    start = serialize(init_grid)
    if all_empty(init_grid):
        return 0
    q = deque()
    q.append((start,0))
    visited = set()
    visited.add(start)
    while q:
        grid,state_clicks = q.popleft()
        if state_clicks>5:
            continue
        if all_empty(grid):
            return state_clicks
        for r in range(4):
            for c in range(4):
                new_grid = [list(row) for row in grid]
                if new_grid[r][c]==0:
                    new_grid[r][c]=1
                else:
                    new_grid[r][c]+=1
                new_grid = simulate(new_grid)
                sg = serialize(new_grid)
                if sg not in visited:
                    visited.add(sg)
                    q.append((sg,state_clicks+1))
    return -1
grid = [list(map(int,input().split())) for _ in range(4)]
print(solve(grid))