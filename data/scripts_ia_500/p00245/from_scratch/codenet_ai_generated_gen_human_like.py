import sys
from collections import deque

input = sys.stdin.readline

def bfs_to_reach_paths(grid, start, X, Y):
    dist = [[-1]*X for _ in range(Y)]
    q = deque()
    q.append(start)
    dist[start[1]][start[0]] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<X and 0<=ny<Y:
                # can move only on '.' or 'P'
                if (grid[ny][nx] == '.' or grid[ny][nx] == 'P') and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x]+1
                    q.append((nx, ny))
    return dist

def main():
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        X, Y = map(int,line.split())
        if X == 0 and Y == 0:
            break
        grid = []
        start = None
        for _ in range(Y):
            while True:
                row = sys.stdin.readline().strip().split()
                if len(row) == X:
                    break
            # Each row has X elements (each '.' or 'P' or digit)
            grid.append(row)
        # find start position
        for y in range(Y):
            for x in range(X):
                if grid[y][x] == 'P':
                    start = (x,y)
                    grid[y][x] = '.'  # treat start as path also for movements

        n = int(sys.stdin.readline())
        items = []
        for _ in range(n):
            g,d,s,e = sys.stdin.readline().split()
            g = int(g)
            d = int(d)
            s = int(s)
            e = int(e)
            items.append((g,d,s,e))

        # Map each product number to list of shelf positions
        shelves = {}
        for y in range(Y):
            for x in range(X):
                c = grid[y][x]
                if c.isdigit():
                    g = int(c)
                    if g not in shelves:
                        shelves[g] = []
                    shelves[g].append((x,y))

        # For each item, find minimum distance from path start to adjacent path cell of shelves of that product
        # Because to pick product g at shelf pos, must go to adjacent path cell of shelf
        # We can move only on paths; shelves are obstacles except for picking from adjacent path cells
        # To get shelves adjacency, for each shelf pos, find adj path cells, choose minimal dist
        dist_map = bfs_to_reach_paths(grid, start, X, Y)

        # For each product in items, find possible minimal access time
        # precompute adjacency path cells for each shelf cell of each product
        adj_paths = {}
        for g in shelves:
            adj_list = []
            for (sx, sy) in shelves[g]:
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    ax, ay = sx+dx, sy+dy
                    if 0<=ax<X and 0<=ay<Y and (grid[ay][ax] == '.' or grid[ay][ax] == 'P'):
                        adj_list.append((ax,ay))
            adj_paths[g] = adj_list

        # For each item, find min dist to an adjacent path cell of its shelves
        min_dist_to_item = []
        for g,d,s,e in items:
            if g not in adj_paths or len(adj_paths[g]) == 0:
                # no way to access this product shelf
                min_dist_to_item.append(-1)
                continue
            md = -1
            for (ax,ay) in adj_paths[g]:
                if dist_map[ay][ax] != -1:
                    if md == -1 or dist_map[ay][ax] < md:
                        md = dist_map[ay][ax]
            min_dist_to_item.append(md)

        # State space search for max discount sum
        # We model DP with bitmask of taken items (n<=8)
        # Because we must consider movement times between items, we precompute minimal distances between items
        # including distance from start to each item position (minimal adjacent path cell of shelf)
        # To move between items, from one item's shelf adj cells to next item's shelf adj cells, must consider minimal path
        # Because we moved only on paths ('.' or 'P') and cannot enter shelf cells directly,
        # we need to precompute distances between all such adj path cells sets.

        # For each product g, we have adj_paths[g] list of path cells adjacent to shelves
        # We will compute a map from each adj_path cell set to each other adj_path cell set:
        # dist(g1,g2) = minimal distance between any cell in adj_paths[g1] to any cell in adj_paths[g2]

        # First, we create a list of only those products in this data set (indexed by item index)
        # We'll store g for each item in product_ids
        product_ids = [it[0] for it in items]

        # Precompute single shortest path distances between all pairs of path cells in the grid (only '.' or 'P')
        # Because max grid size is 20x20=400, we can do BFS from each adj_path cell sets to get minimal distances

        # But we need distances only between adj_path cells of shelves for the products involved and start pos

        # We'll compute distance from start to all cells: already have dist_map
        # Then BFS from all adj_path cells of each product g to get distance to other products' adj_path cells

        # To compute distances between products:
        # For each product, do BFS starting from all adj_path cells of its shelves,
        # record distance to all path cells,
        # then minimal distance to other products is minimal dist to any adj_path cell of other product

        # We'll create a dictionary: dists_products[p][q] = minimal distance from p to q

        max_state = 1 << n
        # Positions of adj_path cells per item
        position_sets = []
        for i in range(n):
            g = product_ids[i]
            position_sets.append(adj_paths.get(g,[]))

        # For BFS starting from multiple points
        def multi_bfs(starts):
            dist = [[-1]*X for _ in range(Y)]
            q = deque()
            for (sx,sy) in starts:
                dist[sy][sx] = 0
                q.append((sx,sy))
            while q:
                x,y = q.popleft()
                for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                    nx, ny = x+dx, y+dy
                    if 0<=nx<X and 0<=ny<Y:
                        if (grid[ny][nx]=='.' or grid[ny][nx]=='P') and dist[ny][nx]==-1:
                            dist[ny][nx] = dist[y][x]+1
                            q.append((nx,ny))
            return dist

        # distance from start position to each product adjacent path cell set minimal distance:
        # already computed in min_dist_to_item but better recompute from dist_map for consistency

        # we already did dist_map from start, min_dist_to_item[i] is minimal dist from start to adj_paths[product_ids[i]]

        # Now compute inter product distances:
        dist_p_p = [[-1]*n for _ in range(n)]
        dist_from_product = []
        for i in range(n):
            dist_i = multi_bfs(position_sets[i])
            dist_from_product.append(dist_i)

        for i in range(n):
            for j in range(n):
                if i == j:
                    dist_p_p[i][j] = 0
                else:
                    md = -1
                    for (x,y) in position_sets[j]:
                        d = dist_from_product[i][y][x]
                        if d != -1:
                            if md == -1 or d < md:
                                md = d
                    dist_p_p[i][j] = md

        # DP: dp[state][last] = minimal time to have taken items in 'state' finishing at item last
        # Initialize with INF, size: 2^n x n
        INF = 10**9
        dp = [[INF]*n for _ in range(max_state)]

        # Initialize dp for taking one item from start
        for i in range(n):
            md = min_dist_to_item[i]
            if md == -1:
                continue
            # time to arrive is md
            g,d,s,e = items[i]
            if md >= s and md < e:
                dp[1 << i][i] = md

        # DP transition
        for state in range(max_state):
            for last in range(n):
                if dp[state][last] == INF:
                    continue
                current_time = dp[state][last]
                for nxt in range(n):
                    if (state & (1 << nxt)) != 0:
                        continue
                    # move from last to nxt
                    dist_move = dist_p_p[last][nxt]
                    if dist_move == -1:
                        continue
                    next_time = current_time + dist_move
                    g,d,s,e = items[nxt]

                    # must arrive within time
                    if next_time < s:
                        next_time = s  # wait until sale starts
                    if next_time >= e:
                        continue

                    nstate = state | (1 << nxt)
                    if dp[nstate][nxt] > next_time:
                        dp[nstate][nxt] = next_time

        ans = 0
        # Calculate max discount sum for reachable dp states
        for state in range(max_state):
            for last in range(n):
                if dp[state][last] == INF:
                    continue
                # sum discount of items in state
                ssum = 0
                for i in range(n):
                    if (state & (1 << i)) != 0:
                        ssum += items[i][1]
                if ssum > ans:
                    ans = ssum

        print(ans)

if __name__ == '__main__':
    main()