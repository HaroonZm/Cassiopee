import sys
from bisect import bisect_left
from operator import itemgetter

def main():
    input = sys.stdin.buffer.readline

    N, M = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(N)]

    X = sorted(set(map(itemgetter(0), points)))
    Y = sorted(set(map(itemgetter(1), points)))

    x_id = {x: i for i, x in enumerate(X)}
    y_id = {y: i for i, y in enumerate(Y)}

    # Compress coordinates for efficient prefix sums
    grid = [[0] * len(Y) for _ in range(len(X))]
    for x, y in points:
        grid[x_id[x]][y_id[y]] += 1

    # Compute 2D prefix sums
    from itertools import accumulate
    # Horizontal prefix sums
    for row in grid:
        for j in range(1, len(Y)):
            row[j] += row[j - 1]
    # Vertical prefix sums
    for j in range(len(Y)):
        for i in range(1, len(X)):
            grid[i][j] += grid[i - 1][j]

    def rect_sum(xl, xr, yl, yr):
        res = grid[xr][yr]
        if xl > 0:
            res -= grid[xl - 1][yr]
        if yl > 0:
            res -= grid[xr][yl - 1]
        if xl > 0 and yl > 0:
            res += grid[xl - 1][yl - 1]
        return res

    min_area = float('inf')
    for l in range(len(X)):
        for r in range(l, len(X)):
            ys = []
            for k in range(len(Y)):
                c = rect_sum(l, r, 0, k)
                ys.append((k, c))
            prefix = [ys[0][1]] + [ys[i][1] - ys[i-1][1] for i in range(1, len(ys))]
            cum = 0
            d = 0
            for u in range(len(Y)):
                while d <= u and rect_sum(l, r, d, u) >= M:
                    area = (X[r] - X[l]) * (Y[u] - Y[d])
                    min_area = min(min_area, area)
                    d += 1
    print(min_area)

if __name__ == "__main__":
    main()