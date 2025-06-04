from sys import stdin, setrecursionlimit
from functools import partial

setrecursionlimit(10**6)

WALL = 100

# Lecture rapide, parsing, et padding en compréhension
w, h = map(int, stdin.readline().split())
pad = [WALL] * (w + 2)
lst = [pad, *([WALL, *map(int, stdin.readline().split()), WALL] for _ in range(h)), pad]
visited = [[0] * (w + 2) for _ in range(h + 2)]

# Adresses des voisins dans une grille de "hexagones"
EVEN_OFF = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0)]
ODD_OFF  = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1)]

hold = []

def search(x, y):
    stack = [(x, y)]
    stat, trail = 0, []
    while stack:
        x, y = stack.pop()
        if visited[x][y]: continue
        val = lst[x][y]
        if val == WALL:
            visited[x][y] = 3
            stat = max(stat, 3)
            continue
        if val == 1:
            visited[x][y] = 2
            stat = max(stat, 2)
            continue
        visited[x][y] = 1
        trail.append((x, y))
        offs = EVEN_OFF if not x & 1 else ODD_OFF
        for dx, dy in offs:
            tx, ty = x + dx, y + dy
            v = visited[tx][ty]
            if not v:
                stack.append((tx, ty))
            elif v > 1:
                stat = max(stat, v)
    for tx, ty in trail:
        visited[tx][ty] = stat
    trail.clear()
    return stat

def main():
    for x in range(1, h + 1):
        for y in range(1, w + 1):
            if not visited[x][y] and not lst[x][y]:
                search(x, y)

    ans = 0
    get_pairs = lambda x: (EVEN_OFF if not x & 1 else ODD_OFF)
    for x in range(1, h + 1):
        for y in range(1, w + 1):
            if lst[x][y]:
                for dx, dy in get_pairs(x):
                    tx, ty = x + dx, y + dy
                    if visited[tx][ty] in (0, 3) and lst[tx][ty] in (WALL, 0):
                        ans += 1
    print(ans)

main()