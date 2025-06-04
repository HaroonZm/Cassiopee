from functools import partial
from collections import deque

def bfs(start_i, start_j):
    stack = deque([(start_i, start_j)])
    res, wc, bc = 1, 0, 0
    a[start_i][start_j] = "#"
    neighbors = [(-1,0), (1,0), (0,-1), (0,1)]
    while stack:
        i, j = stack.pop()
        for dy, dx in neighbors:
            ny, nx = i + dy, j + dx
            if 0 <= ny < h and 0 <= nx < w and a[ny][nx] != "#":
                cell = a[ny][nx]
                if cell == ".":
                    a[ny][nx] = "#"
                    stack.append((ny, nx))
                    res += 1
                elif cell == "W":
                    wc += 1
                elif cell == "B":
                    bc += 1
    return wc, bc, res

import sys
sys.setrecursionlimit(100_000)

while True:
    w, h = map(int, input().split())
    if not w and not h:
        break
    a = [list(input()) for _ in range(h)]
    wans = bans = 0
    for j in range(h):
        for i in range(w):
            if a[j][i] == ".":
                wc, bc, res = bfs(j, i)
                if wc and not bc:
                    wans += res
                elif bc and not wc:
                    bans += res
    print(bans, wans)