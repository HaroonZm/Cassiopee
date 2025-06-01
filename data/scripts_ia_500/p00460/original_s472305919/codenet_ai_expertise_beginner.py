DIV = 100000

while True:
    line = raw_input()
    n, m, s = map(int, line.split())
    if n == 0:
        break

    max_num = n * n
    dp = []
    for i in range(max_num + 1):
        dp.append([0] * (s + 1))

    dp[0][0] = 1

    for i in range(1, max_num + 1):
        for j in range(s + 1):
            val = dp[i - 1][j]
            if j - i >= 0:
                val = (val + dp[i][j - i]) % DIV
            if j - m - 1 >= 0:
                val = (val - dp[i - 1][j - m - 1] + DIV) % DIV
            dp[i][j] = val

    print dp[max_num][s]