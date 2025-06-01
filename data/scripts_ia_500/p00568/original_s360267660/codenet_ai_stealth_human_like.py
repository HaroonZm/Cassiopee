#!/usr/bin/python3

import heapq
import os
import sys

def main():
    H, W = read_ints()
    matrix = [read_ints() for _ in range(H)]
    res = solve(H, W, matrix)
    print(res)  # just printing the result, simple

def solve(H, W, A):
    max_dist = H * W  # maximum steps possible
    # 3D list: for each cell, store costs at different distances
    costs = [[[None]*(max_dist+1) for _ in range(W)] for _ in range(H)]

    best_cost = 2**63  # big number, kinda infinity
    pq = []
    heapq.heappush(pq, (0, 0, 0, 0))  # cost, dist, x, y

    while pq:
        cost, dist, x, y = heapq.heappop(pq)

        if (x, y) == (W-1, H-1):
            best_cost = min(best_cost, cost - dist)

        if costs[y][x][dist] is not None:
            continue  # already visited this state, skip

        # mark all future distances from current dist as visited with this cost
        for d in range(dist, max_dist+1):
            if costs[y][x][d] is not None:
                break
            costs[y][x][d] = cost

        # some pruning to avoid useless work
        if cost - max_dist >= best_cost:
            break

        # try all neighbors
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < W and 0 <= ny < H):
                continue  # out of bounds, skip

            ndist = dist + 1
            if ndist > max_dist:
                continue  # too far, ignore

            # cost update formula, a bit weird but given
            ncost = cost + A[ny][nx] * (1 + dist*2) + 1

            if costs[ny][nx][ndist] is None:
                heapq.heappush(pq, (ncost, ndist, nx, ny))

    return best_cost

# -----------------------------------------------------

DEBUG = 'DEBUG' in os.environ

def inp():
    return sys.stdin.readline().rstrip()

def read_int():
    return int(inp())

def read_ints():
    return list(map(int, inp().split()))

def dprint(*args, sep=' ', end='\n'):
    if DEBUG:
        print(*args, sep=sep, end=end)

if __name__ == "__main__":
    main()