import sys
import numpy as np
input = sys.stdin.readline

def main():
    N, C = map(int, input().split())
    D = np.array([list(map(int, input().split())) for _ in range(C)])
    board = [list(map(int, input().split())) for _ in range(N)]
    cost = np.zeros((3, C), dtype=int)
    count = np.zeros((3, C), dtype=int)
    for i in range(N):
        for j in range(N):
            count[(i + j) % 3][board[i][j] - 1] += 1
    for i in range(3):
        for j in range(C):
            cost[i] += D[j] * count[i][j]
    ans = int(1e20)
    for i in range(C):
        for j in range(C):
            if i == j:
                continue
            for k in range(C):
                if k == i or k == j:
                    continue
                ans = min(ans, cost[0][i] + cost[1][j] + cost[2][k])
    print(ans)

if __name__ == "__main__":
    main()