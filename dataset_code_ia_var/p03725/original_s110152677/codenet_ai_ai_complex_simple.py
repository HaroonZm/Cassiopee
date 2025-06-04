from functools import reduce
from itertools import product, count
from operator import add, itemgetter
import sys

sys.setrecursionlimit(1 << 25)

parse = lambda: list(map(int, input().split()))
h, w, k = parse()
A = [input() for _ in range(h)]
coords = lambda: ((i, j) for i, row in enumerate(A) for j, c in enumerate(row))
start = next(filter(lambda ij: A[ij[0]][ij[1]] == 'S', coords()))
inf = float('inf')
d = [[inf] * w for _ in range(h)]
d[start[0]][start[1]] = 0
que = [start]
mv = [(-1,0), (1,0), (0,-1), (0,1)]

def neighbors(x, y):
    return filter(lambda pos: 0 <= pos[0] < h and 0 <= pos[1] < w, ((x + dx, y + dy) for dx, dy in mv))

ans = inf

for px, py in iter(que.pop, None):
    que += [(nx, ny) for nx, ny in neighbors(px, py) 
            if d[nx][ny] == inf and A[nx][ny] == '.' and not d[nx][ny]]
    for nx, ny in neighbors(px, py):
        if A[nx][ny] == '.' and d[nx][ny] == inf:
            d[nx][ny] = d[px][py] + 1
            if d[nx][ny] <= k:
                que.insert(0, (nx, ny))
    edge_dist = min(px, py, h-px-1, w-py-1)
    ans = min(ans, 1 + (max(0, edge_dist + k - 2) // k))

ans = min(ans, 1 + (max(0, min(start[0], start[1], h-start[0]-1, w-start[1]-1) + k - 2) // k))
print(ans)