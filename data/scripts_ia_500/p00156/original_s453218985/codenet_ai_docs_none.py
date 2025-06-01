from heapq import heappush, heappop, heapify
from itertools import product

def solve():
    hq = [(0, y, x) for y, x in product(xrange(m), xrange(n))
          if not(0 < y < m - 1 and 0 < x < n - 1)]
    heapify(hq)
    while len(hq) != 0:
        cost, cy, cx = heappop(hq)
        if field[cy][cx] == "&":
            return cost
        if memo[cy][cx] <= cost:
            continue
        memo[cy][cx] = cost
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < m and 0 <= nx < n:
                if field[ny][nx] != "#" and field[cy][cx] == "#":
                    heappush(hq, (cost + 1, ny, nx))
                else:
                    heappush(hq, (cost, ny, nx))

while True:
    n, m = map(int, raw_input().split())
    if n | m == 0:
        break
    memo = [[1 << 20] * n for _ in xrange(m)]
    field = [raw_input() for _ in xrange(m)]
    print solve()