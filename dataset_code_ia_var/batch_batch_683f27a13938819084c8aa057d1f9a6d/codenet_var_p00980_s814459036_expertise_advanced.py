import sys
import heapq
from collections import defaultdict

sys.setrecursionlimit(10**7)

INF = float('inf')
EPS = 1e-10
MOD = 10**9 + 7

D4 = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def readints(): return list(map(int, sys.stdin.readline().split()))
def read_matrix(n): return [readints() for _ in range(n)]

def main():
    w, h, n = readints()
    given = [readints() for _ in range(n)]
    grid = [[None] * w for _ in range(h)]
    heap = []
    for x, y, z in given:
        grid[y - 1][x - 1] = z
        heapq.heappush(heap, (-z, y - 1, x - 1))

    visited = defaultdict(bool)
    while heap:
        neg_val, y, x = heapq.heappop(heap)
        if visited[(y, x)]:
            continue
        visited[(y, x)] = True
        val = -neg_val
        for dy, dx in D4:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and not visited[(ny, nx)]:
                if grid[ny][nx] is None:
                    grid[ny][nx] = val - 1
                    heapq.heappush(heap, (-(val - 1), ny, nx))
                elif abs(grid[ny][nx] - val) > 1:
                    print('No')
                    return

    print(sum(sum(row) for row in grid))

if __name__ == '__main__':
    main()