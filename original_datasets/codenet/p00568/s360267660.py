#!/usr/bin/python3

import heapq
import os
import sys

def main():
    H, W = read_ints()
    A = [read_ints() for _ in range(H)]
    print(solve(H, W, A))

def solve(H, W, A):
    dmax = H * W
    D = [[[None] * (dmax + 1) for _ in range(W)] for _ in range(H)]

    best = 2 ** 63
    q = []
    heapq.heappush(q, (0, 0, 0, 0))
    while q:
        cost, dist, x, y = heapq.heappop(q)
        if (x, y) == (W - 1, H - 1):
            best = min(best, cost - dist)
        if D[y][x][dist] is not None:
            continue
        for d in range(dist, dmax + 1):
            if D[y][x][d] is not None:
                break
            D[y][x][d] = cost
        if cost - dmax >= best:
            break
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= W or ny < 0 or ny >= H:
                continue
            ndist = dist + 1
            ncost = cost + A[ny][nx] * (1 + dist * 2) + 1
            if ndist > dmax:
                continue
            if D[ny][nx][ndist] is None:
                heapq.heappush(q, (ncost, ndist, nx, ny))

    return best

###############################################################################

DEBUG = 'DEBUG' in os.environ

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return [int(e) for e in inp().split()]

def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

if __name__ == '__main__':
    main()