import sys

while True:
    w, h = map(int, sys.stdin.readline().split(" "))
    if w == 0 and h == 0:
        break
    table = []
    for i in range(h):
        table.append(sys.stdin.readline())
    dp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    for i in range(h):
        for j in range(w):
            if '0' <= table[i][j] <= '9':
                val = ord(table[i][j]) - ord('0')
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j]) * 10 + val
    print(max([max(dp[i]) for i in range(h + 1)]))