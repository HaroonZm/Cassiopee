import sys

while True:
    w_h = sys.stdin.readline()
    w, h = map(int, w_h.strip().split(" "))
    if w == 0 and h == 0:
        break

    table = []
    for i in range(h):
        row = sys.stdin.readline()
        table.append(row)

    dp = []
    for i in range(h + 1):
        dp.append([0] * (w + 1))

    for i in range(h):
        for j in range(w):
            char = table[i][j]
            if char >= '0' and char <= '9':
                val = int(char)
                max_before = max(dp[i][j + 1], dp[i + 1][j])
                dp[i + 1][j + 1] = max_before * 10 + val

    max_num = 0
    for i in range(h + 1):
        row_max = max(dp[i])
        if row_max > max_num:
            max_num = row_max
    print(max_num)