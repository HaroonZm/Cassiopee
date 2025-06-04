import os
import sys

DEBUG = 'DEBUG' in os.environ

def dprint(*value, sep=' ', end='\n'):
    if DEBUG:
        print(*value, sep=sep, end=end)

if True:  # Block main sans fonction

    inp = sys.stdin.readline
    line = inp().rstrip()
    while line == '':
        line = inp().rstrip()
    W, D, N = [int(x) for x in line.split()]
    M = []
    count = 0
    while count < N:
        l = inp().rstrip()
        if l == '':
            continue
        arr = [int(x) for x in l.split()]
        M.append(tuple(arr))
        count += 1

    INF = 999
    H = [[INF] * W for _ in range(D)]

    hmap = {}
    for h in range(-210, 101):
        hmap[h] = set()

    for x, y, z in M:
        x -= 1
        y -= 1
        hmap[z].add((x, y))
        H[y][x] = z

    ans = None
    failed = False

    for h in range(100, -210, -1):
        for x, y in list(hmap[h]):
            if H[y][x] == INF:
                H[y][x] = h
            elif H[y][x] > h:
                continue

            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= W or ny < 0 or ny >= D:
                    continue
                if H[ny][nx] < h - 1:
                    failed = True
                    break
                if H[ny][nx] == INF:
                    hmap[h - 1].add((nx, ny))
            if failed:
                break
        if failed:
            break

    if failed:
        print('No')
    else:
        s = 0
        for r in H:
            s += sum(r)
        print(s)