from sys import stdin
from itertools import product

def main():
    N = int(stdin.readline())
    for _ in range(N):
        gx, gy = map(int, stdin.readline().split())
        T = [[0]*(gy+1) for _ in range(gx+1)]
        left = [[0]*(gy+1) for _ in range(gx+1)]
        upper = [[0]*(gy+1) for _ in range(gx+1)]
        p = int(stdin.readline())
        for _ in range(p):
            x1, y1, x2, y2 = map(int, stdin.readline().split())
            if x1 == x2:
                upper[x1][max(y1, y2)] = 1
            if y1 == y2:
                left[max(x1, x2)][y1] = 1
        for i in range(gx+1):
            left[i][0] = 1
        for j in range(gy+1):
            upper[0][j] = 1
        T[0][0] = 1
        for i, j in product(range(gx+1), range(gy+1)):
            if i == 0 and j == 0:
                continue
            if left[i][j] and upper[i][j]:
                T[i][j] = 0
            elif not left[i][j] and upper[i][j]:
                T[i][j] = T[i-1][j]
            elif left[i][j] and not upper[i][j]:
                T[i][j] = T[i][j-1]
            else:
                T[i][j] = (T[i-1][j] if i > 0 else 0) + (T[i][j-1] if j > 0 else 0)
        print(T[gx][gy] if T[gx][gy] else "Miserable Hokusai!")

if __name__ == "__main__":
    main()