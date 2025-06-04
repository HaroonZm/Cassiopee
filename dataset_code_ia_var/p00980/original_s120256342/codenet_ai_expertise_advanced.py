from sys import stdin, stdout
from collections import deque
from itertools import product

w, d, n = map(int, input().split())

SIZE = 55
LOW = -1000
mapper = [[LOW] * SIZE for _ in range(SIZE)]
directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

arr = [tuple(map(int, stdin.readline().split())) for _ in range(n)]

def is_compatible(points):
    return all(abs(x1 - x2) + abs(y1 - y2) >= abs(h1 - h2)
               for (x1, y1, h1), (x2, y2, h2) in product(points, repeat=2) if (x1, y1) != (x2, y2))

if not is_compatible(arr):
    stdout.write('No\n')
else:
    for x, y, h in arr:
        if mapper[x][y] < h:
            mapper[x][y] = h
        visited = [[0] * SIZE for _ in range(SIZE)]
        visited[x][y] = 1
        q = deque([(x, y, h)])
        while q:
            cx, cy, ch = q.popleft()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 1 <= nx <= w and 1 <= ny <= d and not visited[nx][ny]:
                    nh = ch - 1
                    if nh > mapper[nx][ny]:
                        mapper[nx][ny] = nh
                        q.append((nx, ny, nh))
                    visited[nx][ny] = 1
    ans = sum(mapper[i][j] for i in range(1, w + 1) for j in range(1, d + 1))
    stdout.write(f'{ans}\n')