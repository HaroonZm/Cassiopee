import os
import sys
from collections import defaultdict
from itertools import product

def main():
    W, D, N = map(int, sys.stdin.readline().split())
    M = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
    result = solve(W, D, N, M)
    print(result if result is not None else 'No')

def solve(W, D, N, M):
    INF = float('inf')
    H = [[INF] * W for _ in range(D)]
    hmap = defaultdict(set)
    for x, y, z in M:
        H[y-1][x-1] = z
        hmap[z].add((x-1, y-1))
    for h in range(100, -210, -1):
        for x, y in hmap[h]:
            cur = H[y][x]
            if cur < h:
                continue
            if cur == INF:
                H[y][x] = h
            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < W and 0 <= ny < D:
                    neighbor = H[ny][nx]
                    if neighbor < h - 1:
                        return None
                    if neighbor == INF:
                        hmap[h-1].add((nx, ny))
    if any(H[y][x] is INF for y in range(D) for x in range(W)):
        return None
    return sum(map(sum, H))

if __name__ == '__main__':
    main()