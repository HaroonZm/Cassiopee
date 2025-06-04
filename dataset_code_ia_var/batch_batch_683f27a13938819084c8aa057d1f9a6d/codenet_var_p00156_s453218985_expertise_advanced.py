from heapq import heapify, heappop, heappush
from itertools import product

def solve_optimized(field, memo, n, m):
    DIRS = ((0, 1), (0, -1), (1, 0), (-1, 0))
    hq = [(0, y, x)
          for y, x in product(range(m), range(n))
          if y in (0, m-1) or x in (0, n-1)]

    heapify(hq)
    memo_update = memo.__setitem__

    while hq:
        cost, cy, cx = heappop(hq)
        if field[cy][cx] == "&":
            return cost
        if memo[cy][cx] <= cost:
            continue
        memo_update(cy, memo[cy][:cx] + [cost] + memo[cy][cx+1:])
        for dx, dy in DIRS:
            ny, nx = cy + dy, cx + dx
            if 0 <= ny < m and 0 <= nx < n:
                cell, prev = field[ny][nx], field[cy][cx]
                next_cost = cost + int(cell != "#" and prev == "#")
                if memo[ny][nx] > next_cost:
                    heappush(hq, (next_cost, ny, nx))
    return -1

def main():
    import sys
    readline = sys.stdin.readline

    while True:
        try:
            n_m = readline()
            if not n_m: break
            n, m = map(int, n_m.split())
            if n == 0 and m == 0:
                break
            field = [readline().rstrip('\n') for _ in range(m)]
            memo = [[float('inf')] * n for _ in range(m)]
            print(solve_optimized(field, memo, n, m))
        except Exception:
            break

if __name__ == '__main__':
    main()