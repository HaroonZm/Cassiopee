while True:
    line = input().strip()
    if line == "0 0":
        break
    X, Y = map(int, line.split())
    grid = []
    for _ in range(Y):
        row = list(map(int, input().split()))
        grid.append(row)
    # grid[y][x]: y from 0 to Y-1, x from 0 to X-1

    # find starting positions on y=0 (top row) where grid is 0 (no obstacle, no jump)
    start_positions = []
    for x in range(X):
        if grid[0][x] == 0:
            start_positions.append(x)

    # dp[y][x]: number of ways to reach cell (x,y)
    dp = [[0]*X for _ in range(Y)]
    for x in start_positions:
        dp[0][x] = 1

    for y in range(Y):
        for x in range(X):
            if dp[y][x] == 0:
                continue
            ways = dp[y][x]
            cell_value = grid[y][x]
            # if on jump cell, jump down two rows with same x (if valid)
            if cell_value == 2 and y+2 <= Y-1:
                ny = y + 2
                # can move to (x, ny) if no obstacle (1)
                if grid[ny][x] != 1:
                    dp[ny][x] += ways
            else:
                # move down one row: to (x-1,y+1), (x,y+1), (x+1,y+1) if valid and allowed
                ny = y + 1
                if ny >= Y:
                    # passed bottom edge, count ways as finishing
                    # To handle finish beyond bottom, we will sum after dp done
                    pass
                else:
                    for nx in [x-1, x, x+1]:
                        if 0 <= nx < X:
                            # check grid at (nx, ny)
                            nv = grid[ny][nx]
                            # no obstacle
                            if nv == 1:
                                continue
                            # if nv==2(jump), only allowed if nx==x (from same x)
                            if nv == 2 and nx != x:
                                continue
                            dp[ny][nx] += ways

    # count paths that finish by reaching y>=Y from last moves
    # two situations:
    # 1) at dp on y=Y-1, from there can go down beyond Y (y=Y), any move counts as finish
    # 2) from jump cell at y=Y-2 can jump 2 cells down beyond Y.
    result = 0
    for y in range(Y):
        for x in range(X):
            if dp[y][x] == 0:
                continue
            ways = dp[y][x]
            cell_value = grid[y][x]
            if y == Y-1:
                # from here, can go down one row beyond edge (finish)
                # moves to y+1 = Y or y+2 = Y+1 are finish
                result += ways  # all ways go finish
            elif cell_value == 2 and y == Y-2:
                # jump from y=Y-2 to y=Y (beyond bottom)
                # jumping 2 down from y=Y-2 reaches y=Y
                result += ways

    print(result)