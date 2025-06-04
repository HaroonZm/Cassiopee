while True:
    line = input()
    if line == '':
        continue
    X_Y = line.split()
    if len(X_Y) != 2:
        continue
    X, Y = map(int, X_Y)
    if X == 0 and Y == 0:
        break
    grid = []
    for _ in range(Y):
        row = list(map(int, input().split()))
        grid.append(row)
    # dp[y][x] = number of ways to reach position (x,y)
    dp = [[0]*X for _ in range(Y+2)]  # +2 for jump landing possibility beyond last row

    # start positions at y=0 (y=1 in problem, index 0 here)
    for x in range(X):
        if grid[0][x] == 0:
            dp[0][x] = 1

    for y in range(Y):
        for x in range(X):
            if dp[y][x] == 0:
                continue
            # current position dp[y][x] has dp[y][x] ways
            # try to move to next positions
            for dx in [-1, 0, 1]:
                nx = x + dx
                if nx < 0 or nx >= X:
                    continue
                ny = y + 1
                if ny >= Y:
                    # over the bottom - count 1 way
                    dp[Y].append(dp[y][x])  # just to keep consistent length, no need
                    continue
                cell = grid[ny][nx]
                if cell == 1:
                    # obstacle
                    continue
                elif cell == 0:
                    dp[ny][nx] += dp[y][x]
                else:
                    # cell == 2 jump ramp
                    # can jump only from same x
                    # so dx must be 0
                    if dx == 0:
                        ny2 = y + 2
                        if ny2 >= Y:
                            # finish
                            # no dp beyond last row so just count ways
                            pass
                        else:
                            if grid[ny2][nx] != 1:
                                dp[ny2][nx] += dp[y][x]
    # sum ways reaching below bottom
    total = 0
    for x in range(X):
        total += dp[Y][x]
    # also add ways that went beyond bottom directly
    # but dp[Y] is only length X, no extension further
    # so check dp at y=Y and y=Y+1 as we did dp detail - since dp size is Y+2 only
    if Y+1 < len(dp):
        for x in range(X):
            total += dp[Y+1][x]
    # Add ways that finish by moving below last row directly in loop
    # Since in above loop we didn't store ways beyond dp arrays, so need another way
    # So reimplement above with counting directly finish ways

while True:
    line = input()
    if line == '':
        continue
    X_Y = line.split()
    if len(X_Y) != 2:
        continue
    X, Y = map(int, X_Y)
    if X == 0 and Y == 0:
        break
    grid = []
    for _ in range(Y):
        row = list(map(int, input().split()))
        grid.append(row)

    dp = [[0]*X for _ in range(Y+3)]
    for x in range(X):
        if grid[0][x] == 0:
            dp[0][x] = 1

    ans = 0
    for y in range(Y):
        for x in range(X):
            if dp[y][x] == 0:
                continue
            ways = dp[y][x]
            for dx in [-1,0,1]:
                nx = x + dx
                if nx < 0 or nx >= X:
                    continue
                ny = y + 1
                if ny >= Y:
                    ans += ways
                    continue
                cell = grid[ny][nx]
                if cell == 1:
                    continue
                elif cell == 0:
                    dp[ny][nx] += ways
                else:
                    # jump ramp
                    # only from same x
                    if dx == 0:
                        ny2 = y + 2
                        if ny2 >= Y:
                            ans += ways
                        else:
                            if grid[ny2][nx] != 1:
                                dp[ny2][nx] += ways
    print(ans)