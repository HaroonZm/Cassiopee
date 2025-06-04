import sys

def input():
    return sys.stdin.readline().strip()

def MAP():
    return map(int, input().split())

def main():
    sys.setrecursionlimit(10 ** 9)
    MOD = 10 ** 9 + 7
    INF = float('inf')

    H, W = MAP()

    # グリッドの周囲を壁で囲む
    grid = []
    grid.append(['#'] * (W + 2))
    for i in range(H):
        row = list(input())
        grid.append(['#'] + row + ['#'])
    grid.append(['#'] * (W + 2))

    # dpテーブルの初期化
    dp = []
    for i in range(H + 2):
        dp.append([0] * (W + 2))

    dp[1][1] = 1  # スタート地点

    for i in range(1, H + 1):
        for j in range(1, W + 1):
            if grid[i][j] == '#':
                continue
            if grid[i - 1][j] != '#':
                dp[i][j] += dp[i - 1][j]
            if grid[i][j - 1] != '#':
                dp[i][j] += dp[i][j - 1]
            dp[i][j] %= MOD

    print(dp[H][W])

if __name__ == "__main__":
    main()