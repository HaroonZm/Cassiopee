dic = {"A": (0, 0), "B": (0, 1), "C": (0, 2),
       "D": (1, 0), "E": (1, 1), "F": (1, 2),
       "G": (2, 0), "H": (2, 1), "I": (2, 2)}

while True:
    n = input()
    if n == "0":
        break
    n = int(n)
    dp = []
    for i in range(n + 1):
        row = []
        for j in range(3):
            row.append([0] * 3)
        dp.append(row)

    s, t, b = input().split()

    start_y, start_x = dic[s]
    target_y, target_x = dic[t]
    block_y, block_x = dic[b]

    dp[0][start_y][start_x] = 1

    moves = [(0,1), (-1,0), (0,-1), (1,0)]

    for i in range(n):
        for y in range(3):
            for x in range(3):
                current = dp[i][y][x]
                if current == 0:
                    continue
                for dy, dx in moves:
                    ny = y + dy
                    nx = x + dx
                    if ny < 0 or ny >= 3 or nx < 0 or nx >= 3 or (ny == block_y and nx == block_x):
                        dp[i + 1][y][x] += current
                    else:
                        dp[i + 1][ny][nx] += current

    result = dp[n][target_y][target_x] / (4 ** n)
    print("{:.8f}".format(result))