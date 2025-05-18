import sys
import numpy as np
from numba import njit, void, i8

def main():
    R, C, K = map(int, readline().split())
    items = np.array(read().split(), dtype=np.int64)
    print(calc(R, C, K, items))

@njit(i8(i8, i8, i8, i8[:]), cache=True)
def calc(R, C, K, items):
    cell = np.zeros((R, C), dtype=np.int64)
    for i in range(0, K*3, 3):
        x, y, c = items[i:i+3]
        cell[x-1, y-1] = c
    L_INF = int(1e17)
    dp = np.full((R+1, C+1, 4), -L_INF, dtype=np.int64)
    dp[0, 1, 0] = dp[1, 0, 0] = 0
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            for k in range(4):
                dp[i, j, k] = max(dp[i, j, k], dp[i, j-1, k])
                if k > 0:
                    dp[i, j, k] = max(dp[i, j, k], dp[i, j, k-1])
                    dp[i, j, k] = max(dp[i, j, k], dp[i, j-1, k-1] + cell[i-1, j-1])
                if k == 1:
                    dp[i, j, 1] = max(dp[i, j, 1], dp[i-1, j, 3] + cell[i-1, j-1])
    return dp[R, C, 3]

if __name__ == "__main__":
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline

    if __file__=="test.py":
        f = open("./in_out/input.txt", "r", encoding="utf-8")
        read = f.read
        readline = f.readline

    main()