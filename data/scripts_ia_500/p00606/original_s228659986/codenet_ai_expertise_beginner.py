while True:
    n = int(input())
    if n == 0:
        break

    s, t, b = input().split()
    base = ord("A")
    blank = ord(b) - base

    dp = []
    for i in range(n + 1):
        dp.append([0] * 9)

    dp[0][ord(s) - base] = 1

    to = {
        0: (0, 0, 1, 3),
        1: (0, 1, 2, 4),
        2: (1, 2, 2, 5),
        3: (0, 3, 4, 6),
        4: (1, 3, 5, 7),
        5: (2, 4, 5, 8),
        6: (3, 6, 6, 7),
        7: (4, 6, 7, 8),
        8: (5, 7, 8, 8)
    }

    def update(x, i):
        for nex in to[x]:
            if nex == blank:
                dp[i][x] = dp[i][x] + dp[i - 1][x] / 4
            else:
                dp[i][nex] = dp[i][nex] + dp[i - 1][x] / 4

    for i in range(1, n + 1):
        for x in range(9):
            update(x, i)

    print(dp[n][ord(t) - base])