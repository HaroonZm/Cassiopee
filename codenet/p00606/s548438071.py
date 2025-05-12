dic = {"A":(0,0), "B":(0,1), "C":(0,2),
       "D":(1,0), "E":(1,1), "F":(1,2),
       "G":(2,0), "H":(2,1), "I":(2,2)}
while True:
    n = input()
    if n == 0:
        break
    dp = [[[0] * 3 for _ in xrange(3)] for _ in xrange(n + 1)]
    s, t, b = raw_input().split()
    dp[0][dic[s][0]][dic[s][1]] = 1
    for i in xrange(n):
        for y in xrange(3):
            for x in xrange(3):
                for dx, dy in ((0, 1), (-1, 0), (0, -1), (1, 0)):
                    if not(0 <= x + dx < 3 and 0 <= y + dy < 3) or dic[b] == (y + dy, x + dx):
                        dp[i + 1][y][x] += dp[i][y][x]
                    else:
                        dp[i + 1][y + dy][x + dx] += dp[i][y][x]
    print "{:.8f}".format(float(dp[n][dic[t][0]][dic[t][1]]) / 4.**n)