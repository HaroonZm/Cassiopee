while True:
    n, c = map(int, input().split())
    if n == 0 and c == 0:
        break

    light = [list(map(int, input().split())) for _ in range(n)]
    press = [list(map(int, input().split())) for _ in range(c)]

    # Convert each light and press line to bitmask for efficiency
    light_mask = []
    for row in light:
        mask = 0
        for i, b in enumerate(row):
            if b:
                mask |= 1 << i
        light_mask.append(mask)

    press_mask = []
    for row in press:
        mask = 0
        for i, b in enumerate(row):
            if b:
                mask |= 1 << i
        press_mask.append(mask)

    # DP: dp[i][s] = max score after i-th beat with lit buttons s (bitmask)
    # s's bits set => buttons currently lit
    # initialized with -1 meaning impossible state
    dp = [[-1] * (1 << 16) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        for s in range(1 << 16):
            if dp[i][s] < 0:
                continue
            # new lights appear on top of current lit buttons
            new_light = s | light_mask[i]

            # try each pressing pattern
            for p in press_mask:
                # buttons pressed that are currently lit (to turn off)
                off = new_light & p
                off_count = bin(off).count("1")

                # next lit buttons after pressing
                next_s = new_light & (~p)

                # update dp
                val = dp[i][s] + off_count
                if dp[i + 1][next_s] < val:
                    dp[i + 1][next_s] = val

    print(max(dp[n]))