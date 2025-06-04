from sys import stdin
from itertools import islice

def matabi():
    input_iter = iter(stdin.read().split())
    n = int(next(input_iter))
    for _ in range(n):
        x, y = map(int, islice(input_iter, 2))
        dp = [[0]*(y+1) for _ in range(x+1)]
        m = int(next(input_iter))
        forbidden = set(tuple(map(int, islice(input_iter, 4))) for _ in range(m))
        # Set starting positions
        dp[0][0] = 1
        for i in range(1, x+1):
            seg = (i, 0, i-1, 0)
            if seg in forbidden or (i-1, 0, i, 0) in forbidden:
                break
            dp[i][0] = 1
        for i in range(1, y+1):
            seg = (0, i, 0, i-1)
            if seg in forbidden or (0, i-1, 0, i) in forbidden:
                break
            dp[0][i] = 1
        for i in range(1, x+1):
            for j in range(1, y+1):
                blk_h = (i, j-1, i, j) in forbidden or (i, j, i, j-1) in forbidden
                blk_v = (i-1, j, i, j) in forbidden or (i, j, i-1, j) in forbidden
                if blk_h and blk_v:
                    continue
                elif blk_v:
                    dp[i][j] = dp[i][j-1]
                elif blk_h:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print("Miserable Hokusai!" if dp[x][y] == 0 else dp[x][y])

matabi()