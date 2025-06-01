MOD = 100000

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    # dp[i][j][d] = number of ways to reach (i,j)
    # d = 0 if last move was east (horizontal), d = 1 if last move was north (vertical)
    # to avoid consecutive turns, if last move was east, next move is east or north without consecutive turns
    dp = [[[0, 0] for _ in range(h + 1)] for __ in range(w + 1)]

    # Starting at (1,1), no move taken yet, but we treat as if last move was both directions allowed
    # To initiate, we can move east or north from (1,1)
    dp[1][1][0] = 1
    dp[1][1][1] = 1

    for i in range(1, w + 1):
        for j in range(1, h + 1):
            if i == 1 and j == 1:
                continue
            # moving east to (i,j) means coming from (i-1,j) with last move east or from (i-1,j) with last move north (if allowed)
            # constraint: no two consecutive turns, so if last move was north, we cannot turn again immediately
            # To move east at (i,j), last move must have been east at (i-1,j)
            if i > 1:
                dp[i][j][0] = (dp[i - 1][j][0] + dp[i - 1][j][1]) % MOD
                # But turning from north to east is a turn, so we must check if it's allowed:
                # "After turning, cannot turn again next immediately" means no two consecutive turns
                # So if at previous step we just turned, next move can't turn.
                # Actually, we must avoid consecutive turns.
                # But our dp as is counts all, need to track if last move was a turn or not?

                # The problem states:
                # - You can't turn at two consecutive intersections.
                # So "turn" means changing direction compared to previous move.
                # So we must differentiate between "came straight" and "just turned".
                # We need to track three states:
                # 0: last move east, and no turn just made
                # 1: last move north, and no turn just made
                # 2: last move just turned

    # The above dp is insufficient, let's adjust the states:
    # dp[i][j][direction][turn_flag]
    # direction: 0 = east, 1 = north
    # turn_flag: 0 = last move was straight, 1 = last move was a turn
    # The rule: if last move was a turn (turn_flag=1), then the next move cannot be a turn.

    dp = [[[[0, 0] for _ in range(2)] for __ in range(h + 1)] for ___ in range(w + 1)]
    # Initialization at (1,1): no moves yet, so we can start moving east or north without turn flag.
    dp[1][1][0][0] = 1
    dp[1][1][1][0] = 1

    for i in range(1, w + 1):
        for j in range(1, h + 1):
            for d in [0,1]:  # current direction
                for t in [0,1]: # turn_flag at current state
                    ways = dp[i][j][d][t]
                    if ways == 0:
                        continue
                    # Move east (direction 0)
                    if i + 1 <= w:
                        # determine if next move is turn or straight
                        turn_next = 0 if d == 0 else 1
                        if t == 1 and turn_next == 1:
                            # cannot turn twice consecutively
                            pass
                        else:
                            dp[i+1][j][0][turn_next] = (dp[i+1][j][0][turn_next] + ways) % MOD
                    # Move north (direction 1)
                    if j + 1 <= h:
                        turn_next = 0 if d == 1 else 1
                        if t == 1 and turn_next == 1:
                            pass
                        else:
                            dp[i][j+1][1][turn_next] = (dp[i][j+1][1][turn_next] + ways) % MOD

    ans = 0
    for d in [0,1]:
        for t in [0,1]:
            ans = (ans + dp[w][h][d][t]) % MOD
    print(ans)