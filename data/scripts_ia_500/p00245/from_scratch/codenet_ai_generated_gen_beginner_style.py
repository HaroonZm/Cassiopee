import sys
sys.setrecursionlimit(10**7)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(start_x, start_y, grid, X, Y):
    dist = [[-1]*Y for _ in range(X)]
    dist[start_x][start_y] = 0
    queue = [(start_x, start_y)]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < X and 0 <= ny < Y:
                if dist[nx][ny] == -1 and grid[nx][ny] == '.':
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return dist

def can_reach(dist, points):
    # points: list of (x,y)
    d = []
    for x,y in points:
        d.append(dist[x][y])
    return d

def solve():
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        X,Y = map(int,line.split())
        if X == 0 and Y == 0:
            break
        grid_raw = []
        for _ in range(Y):
            row = sys.stdin.readline().strip().split()
            grid_raw.append(row)
        # grid_raw[y][x]
        # convert to grid with coord (x,y)
        grid = [['']*Y for _ in range(X)]
        pos_p = None
        shelves = dict()  # g -> list of positions
        for y in range(Y):
            for x in range(X):
                c = grid_raw[y][x]
                grid[x][y] = c
                if c == 'P':
                    pos_p = (x,y)
                elif c.isdigit():
                    g = int(c)
                    if g not in shelves:
                        shelves[g] = []
                    shelves[g].append((x,y))
        n = int(sys.stdin.readline())
        items = []
        for _ in range(n):
            g,d,s,e = map(int, sys.stdin.readline().split())
            items.append( (g,d,s,e) )
        # We have:
        # grid of size X*Y
        # pos_p start pos on passage
        # shelves[g] list of positions of the product g shelves
        # items: list of (g,d,s,e)

        # First compute distances from P to all passages
        dist_from_p = bfs(pos_p[0],pos_p[1],grid,X,Y)

        # For each product g, compute minimal distance from P to any shelf
        product_min_dist = dict()
        for g,lst in shelves.items():
            md = 10**9
            for (x,y) in lst:
                # can only pick from passage adjacent to shelf (x,y)
                # check 4 neighbors of shelf (x,y)
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < X and 0 <= ny < Y:
                        if grid[nx][ny] == '.':
                            d = dist_from_p[nx][ny]
                            if d != -1 and d < md:
                                md = d
            if md != 10**9:
                product_min_dist[g] = md
            else:
                product_min_dist[g] = -1

        # Also need distances between products (to reach new product from previous product)
        # For each product g, get list of positions of passages adjacent to shelf
        # For simplicity, get passage positions adjacent to each product shelf
        product_passages = dict()
        # build grid of passages only for BFS
        for g,lst in shelves.items():
            pos_passages = []
            for (x,y) in lst:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < X and 0 <= ny < Y:
                        if grid[nx][ny] == '.':
                            pos_passages.append( (nx, ny) )
            product_passages[g] = pos_passages

        # bfs distances between passages to find min distance between products
        # precompute distance from each product's adjacent passages to all passages
        dist_product_to_all = dict()
        for g in product_passages:
            dist_all = [[-1]*Y for _ in range(X)]
            from collections import deque
            q = deque()
            for (x,y) in product_passages[g]:
                dist_all[x][y] = 0
                q.append((x,y))
            while q:
                x,y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < X and 0 <= ny < Y:
                        if dist_all[nx][ny] == -1 and grid[nx][ny] == '.':
                            dist_all[nx][ny] = dist_all[x][y]+1
                            q.append((nx,ny))
            dist_product_to_all[g] = dist_all

        # Now distance from product g to product h is minimal dist between any passage adjacent to h from dist_product_to_all[g]
        def dist_g_h(g,h):
            md = 10**9
            for (x,y) in product_passages[h]:
                d = dist_product_to_all[g][x][y]
                if d != -1 and d < md:
                    md = d
            if md == 10**9:
                return -1
            return md

        # Prepare DP to find maximum discount sum
        # We can choose any subset of items without duplicates
        # and pick them in any order
        # State: bitmask of chosen items, last picked item index or -1 for start position
        # Transition from last product to next product if reachable in time

        # First, calculate distance from start to each item shelf minimal distance:
        start_to_item_dist = []
        for i in range(n):
            g,d,s,e = items[i]
            if g in product_min_dist:
                start_to_item_dist.append(product_min_dist[g])
            else:
                start_to_item_dist.append(-1)

        # Distance between items
        item_to_item_dist = [[-1]*n for _ in range(n)]
        for i in range(n):
            gi = items[i][0]
            for j in range(n):
                gj = items[j][0]
                if gi in product_passages and gj in product_passages:
                    item_to_item_dist[i][j] = dist_g_h(gi, gj)

        max_time = 100
        from collections import deque

        dp = [[-1]*(n) for _ in range(1<<n)]
        # dp[bitmask][last] = max discount sum
        # also keep arrival time to check feasibility
        # But time not stored in dp: we try all picking sequences with time constraints

        # We'll store states as (bitmask, last, time)
        # To avoid too big states, do BFS with pruning

        from collections import deque
        q = deque()
        # initial states: pick no items, at start pos time=0
        # try to pick each item first
        for i in range(n):
            d = start_to_item_dist[i]
            if d == -1:
                continue
            g,d_i,s,e = items[i]
            arrival_time = d
            if s <= arrival_time < e:
                dp[1<<i][i] = items[i][1]
                q.append( (1<<i, i, arrival_time)  )

        ans = 0
        for i in range(n):
            if dp[1<<i][i] > ans:
                ans = dp[1<<i][i]
        while q:
            bitmask, last, time_curr = q.popleft()
            val = dp[bitmask][last]
            if val == -1:
                continue
            if val > ans:
                ans = val
            for nxt in range(n):
                if (bitmask & (1<<nxt))==0:
                    d = item_to_item_dist[last][nxt]
                    if d == -1:
                        continue
                    g,d_n,s_n,e_n = items[nxt]
                    next_time = time_curr + d
                    if s_n <= next_time < e_n:
                        new_bitmask = bitmask | (1<<nxt)
                        new_val = val + d_n
                        if dp[new_bitmask][nxt] < new_val:
                            dp[new_bitmask][nxt] = new_val
                            q.append((new_bitmask,nxt,next_time))
        print(ans)

solve()