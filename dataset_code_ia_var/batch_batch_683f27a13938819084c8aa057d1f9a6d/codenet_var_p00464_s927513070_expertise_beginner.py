import sys

def create_array(rows, cols, fill=0):
    array = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(fill)
        array.append(row)
    return array

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        hwn = line.strip().split()
        if not hwn or len(hwn) < 3:
            continue
        h = int(hwn[0])
        w = int(hwn[1])
        n = int(hwn[2])
        if h == 0 and w == 0 and n == 0:
            break

        grid = []
        for _ in range(h):
            row = list(map(int, sys.stdin.readline().strip().split()))
            grid.append(row)

        dp = create_array(h, w, 0)
        dp[0][0] = n - 1

        for i in range(h):
            for j in range(w):
                if i < h - 1:
                    if grid[i][j] == 0:
                        dp[i + 1][j] += (dp[i][j] + 1) // 2
                    if grid[i][j] == 1:
                        dp[i + 1][j] += dp[i][j] // 2
                if j < w - 1:
                    if grid[i][j] == 0:
                        dp[i][j + 1] += dp[i][j] // 2
                    if grid[i][j] == 1:
                        dp[i][j + 1] += (dp[i][j] + 1) // 2

        for i in range(h):
            for j in range(w):
                grid[i][j] = (grid[i][j] + dp[i][j]) % 2

        i = 0
        j = 0
        while i < h and j < w:
            if grid[i][j] == 0:
                i += 1
            else:
                j += 1
        print(i + 1, j + 1)

if __name__ == "__main__":
    main()