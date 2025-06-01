positions = {"A": (0, 0), "B": (0, 1), "C": (0, 2),
             "D": (1, 0), "E": (1, 1), "F": (1, 2),
             "G": (2, 0), "H": (2, 1), "I": (2, 2)}

while True:
    n = raw_input()  # number of steps
    if n == '0':
        break
    n = int(n)
    # 3D dp: steps x rows x cols
    dp = []
    for _ in range(n + 1):
        dp.append([[0] * 3 for _ in range(3)])
    
    s, t, b = raw_input().split()
    start_y, start_x = positions[s]
    target_y, target_x = positions[t]
    block_y, block_x = positions[b]

    dp[0][start_y][start_x] = 1  # starting position has probability 1

    directions = [(0,1), (-1,0), (0,-1), (1,0)]  # right, up, left, down

    for step in range(n):
        for y in range(3):
            for x in range(3):
                if dp[step][y][x] == 0:
                    continue  # no need to process if no ways to get here
                for dy, dx in directions:
                    ny, nx = y + dy, x + dx
                    # check boundaries and blocked cell
                    if ny < 0 or ny >= 3 or nx < 0 or nx >= 3 or (ny == block_y and nx == block_x):
                        # if move is not possible, stay put
                        dp[step + 1][y][x] += dp[step][y][x]
                    else:
                        dp[step + 1][ny][nx] += dp[step][y][x]

    # Compute final probability
    prob = float(dp[n][target_y][target_x]) / (4 ** n)
    # Not much precision needed but let's keep 8 decimal places anyway
    print "{:.8f}".format(prob)