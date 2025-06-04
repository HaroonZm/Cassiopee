def recursion(y, x, island, dp):
    if island[y][x].isdigit() and int(island[y][x]) in range(10):
        if y == 0 and x == 0:
            dp[y][x] = int(island[y][x])
        elif y == 0:
            if dp[y][x - 1] != -1:
                dp[y][x] = dp[y][x - 1] * 10 + int(island[y][x])
            else:
                dp[y][x] = int(island[y][x])
        elif x == 0:
            if dp[y - 1][x] != -1:
                dp[y][x] = dp[y - 1][x] * 10 + int(island[y][x])
            else:
                dp[y][x] = int(island[y][x])
        else:
            if dp[y - 1][x] == -1 and dp[y][x - 1] == -1:
                dp[y][x] = int(island[y][x])
            elif dp[y - 1][x] == -1:
                dp[y][x] = dp[y][x - 1] * 10 + int(island[y][x])
            elif dp[y][x - 1] == -1:
                dp[y][x] = dp[y - 1][x] * 10 + int(island[y][x])
            else:
                dp[y][x] = max(dp[y][x - 1] * 10 + int(island[y][x]), dp[y - 1][x] * 10 + int(island[y][x]))
    else:
        dp[y][x] = -1

def solve(w, h, island, dp):
    for i in range(h):
        for j in range(w):
            recursion(i, j, island, dp)
    print max(map(max, dp))

def func():
    while True:
        w, h = map(int, raw_input().split())
        if w == 0 and h == 0:
            break
        island = []
        for i in range(h):
            row = []
            line = raw_input()
            for j in line:
                row.append(j)
            island.append(row)
        dp = []
        for i in range(h):
            dp_row = []
            for j in range(w):
                dp_row.append(0)
            dp.append(dp_row)
        solve(w, h, island, dp)

if __name__ == '__main__':
    func()