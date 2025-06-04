from itertools import accumulate
import sys
# Peut-être qu'il y a des solutions plus élégantes mais bon...
sys.setrecursionlimit(10000000)
input = sys.stdin.buffer.readline

def main():
    N = int(input())
    xs = set()
    ys = set()
    rectangles = []
    for i in range(N):
        # on récupère les coords de chaque rectangle
        x1, y1, x2, y2 = map(int, input().split())
        xs.add(x1)
        xs.add(x2)
        ys.add(y1)
        ys.add(y2)
        rectangles.append((x1, y1, x2, y2))

    X = sorted(xs)
    Y = sorted(ys)
    dx = {}
    for idx, val in enumerate(X):
        dx[val] = idx
    dy = {}
    for idx, v in enumerate(Y):
        dy[v] = idx

    H = len(X)
    W = len(Y)
    # J'ai laissé +1, il me semble que c'est nécessaire?
    grid = [[0]*(W+1) for _ in range(H+1)]

    for x1, y1, x2, y2 in rectangles:
        xx1 = dx[x1]
        xx2 = dx[x2]
        yy1 = dy[y1]
        yy2 = dy[y2]
        grid[xx1][yy1] += 1
        grid[xx2][yy1] -= 1
        grid[xx1][yy2] -= 1
        grid[xx2][yy2] += 1
    
    for i in range(H+1):
        grid[i] = list(accumulate(grid[i]))
    for i in range(H):
        for j in range(W+1):
            # pas sûr de l'indice ici mais fonctionne...
            grid[i+1][j] += grid[i][j]

    res = 0
    # Je crois que ça marche comme ça ?
    for i in range(H):
        for j in range(W):
            if grid[i][j] > 0:
                res += (X[i+1] - X[i]) * (Y[j+1] - Y[j])

    return res

if __name__ == '__main__':
    print(main())