from itertools import accumulate
import sys
input = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())
xs = set()
ys = set()
rect = []
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    xs.add(x1)
    xs.add(x2)
    ys.add(y1)
    ys.add(y2)
    rect.append((x1, y1, x2, y2))
X = sorted(xs)
Y = sorted(ys)
dx = {x: i for i, x in enumerate(X)}
dy = {y: i for i, y in enumerate(Y)}
H = len(xs)
W = len(ys)
grid = [[0] * (W + 1) for _ in range(H + 1)]
for x1, y1, x2, y2 in rect:
    grid[dx[x1]][dy[y1]] += 1
    grid[dx[x2]][dy[y1]] -= 1
    grid[dx[x1]][dy[y2]] -= 1
    grid[dx[x2]][dy[y2]] += 1
for i in range(H):
    grid[i] = list(accumulate(grid[i]))
for i in range(H):
    for j in range(W):
        grid[i + 1][j] += grid[i][j]
ans = 0
for i in range(H):
    for j in range(W):
        if grid[i][j]:
            ans += (X[i + 1] - X[i]) * (Y[j + 1] - Y[j])
print(ans)