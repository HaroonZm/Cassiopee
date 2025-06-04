import sys
import heapq

input = sys.stdin.readline

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    f, m, o = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(H)]
    # pos of oxygen cells
    oxy_cells = []
    for y in range(H):
        for x in range(W):
            if grid[y][x] > 0:
                oxy_cells.append((x, y))
    # initial row y=0, can start at any cell there
    # State: (cost, x, y, oxygen_left, masked_oxygen_mask)
    # For oxygen cells, need to track usage (once per cell)
    # Assign index for each oxygen cell
    oxy_id = dict()
    for i, (x,y) in enumerate(oxy_cells):
        oxy_id[(x,y)] = i
    max_mask = 1 << len(oxy_cells)

    # dist dictionary: key=(x,y,oxygen_left,mask), val=cost
    # To limit memory, keep dist only for states with oxygen_left>0
    from collections import deque,defaultdict
    dist = dict()

    hq = []
    # Start positions: y=0 (y=1 in problem, zero-based here)
    for x in range(W):
        start_o2 = o
        start_mask = 0
        cost = 0
        # if start cell is oxygen cell, must consume oxygen here once
        if grid[0][x] > 0:
            idx = oxy_id[(x,0)]
            # must consume oxygen from cell
            start_mask |= 1 << idx
            start_o2 = min(m, start_o2 + grid[0][x])
        else:
            # soil cell: pay cost to dig it
            cost = -grid[0][x]
            if cost > f:
                continue
        if start_o2 == 0:
            continue
        key = (x,0,start_o2,start_mask)
        dist[key] = cost
        heapq.heappush(hq,(cost,x,0,start_o2,start_mask))

    res = None
    # Moves: left, right, down (no up)
    dxs = [-1,1,0]
    dys = [0,0,1]

    while hq:
        cost,x,y,o2,mask = heapq.heappop(hq)
        key = (x,y,o2,mask)
        if dist.get(key, float('inf')) < cost:
            continue
        # check if at last row and o2>0 => success
        if y == H-1 and o2 > 0:
            if res is None or cost < res:
                res = cost
                # minimal cost found, but maybe better?
                # continue to find better cost
        for dir in range(3):
            nx = x + dxs[dir]
            ny = y + dys[dir]
            if not (0 <= nx < W and 0 <= ny < H):
                continue
            # moving costs 1 oxygen
            no2 = o2 - 1
            if no2 == 0:
                continue
            cell = grid[ny][nx]
            nmask = mask
            ncost = cost
            if cell > 0:
                # oxygen cell, must consume if not consumed yet
                idx = oxy_id[(nx,ny)]
                if (mask & (1<<idx)) == 0:
                    # consume oxygen here
                    nmask |= 1 << idx
                    no2 = min(m, no2 + cell)
                # digging cost is 0
            else:
                # soil cell, must dig (pay cost)
                ncost += -cell
                if ncost > f:
                    continue
            nkey = (nx, ny, no2, nmask)
            if dist.get(nkey, float('inf')) > ncost:
                dist[nkey] = ncost
                heapq.heappush(hq,(ncost,nx,ny,no2,nmask))
    print(res if res is not None else "NA")