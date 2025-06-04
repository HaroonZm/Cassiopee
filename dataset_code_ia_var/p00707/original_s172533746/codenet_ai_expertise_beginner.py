def recursion(y, x, island, dp):
    if island[y][x].isdigit():
        num = int(island[y][x])
        if y == 0 and x == 0:
            dp[y][x] = num
        elif y == 0:
            if dp[y][x-1] != -1:
                dp[y][x] = dp[y][x-1] * 10 + num
            else:
                dp[y][x] = num
        elif x == 0:
            if dp[y-1][x] != -1:
                dp[y][x] = dp[y-1][x] * 10 + num
            else:
                dp[y][x] = num
        else:
            if dp[y-1][x] == -1 and dp[y][x-1] == -1:
                dp[y][x] = num
            elif dp[y-1][x] == -1:
                dp[y][x] = dp[y][x-1] * 10 + num
            elif dp[y][x-1] == -1:
                dp[y][x] = dp[y-1][x] * 10 + num
            else:
                a = dp[y][x-1] * 10 + num
                b = dp[y-1][x] * 10 + num
                if a > b:
                    dp[y][x] = a
                else:
                    dp[y][x] = b
    else:
        dp[y][x] = -1

def solve(w, h, island, dp):
    for i in range(h):
        for j in range(w):
            recursion(i, j, island, dp)
    max_num = -1
    for row in dp:
        for val in row:
            if val > max_num:
                max_num = val
    print(max_num)

def func():
    while True:
        parts = input().split()
        w = int(parts[0])
        h = int(parts[1])
        if w == 0 and h == 0:
            break
        island = []
        for i in range(h):
            line = input()
            row = []
            for c in line:
                row.append(c)
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