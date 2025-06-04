from functools import reduce
from itertools import product, count
from operator import add, itemgetter
from collections import deque

def matrix_wrap(x, y, get_line):
    border = lambda: ["#"] * (x + 2)
    lines = [list("#" + get_line() + "#") for _ in range(y)]
    return [border()] + lines + [border()]

def explore_ice(mp, pos, tag, ice_dic, directions):
    stack = [pos]
    while stack:
        cx, cy = stack.pop()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if mp[ny][nx] == "X":
                mp[ny][nx] = tag
                ice_dic[tag] += 1
                stack.append((nx, ny))

def ice_count_and_positions(mp, y, x, directions):
    ices, remap, start, goal = [], lambda v: v, None, None
    for i, j in product(range(1, y + 1), range(1, x + 1)):
        v = mp[i][j]
        if v == "S":
            start = (j, i)
            mp[i][j] = "."
        elif v == "G":
            goal = (j, i)
            mp[i][j] = "."
        elif v == "X":
            tag = len(ices)
            mp[i][j] = tag
            ices.append(1)
            explore_ice(mp, (j, i), tag, ices, directions)
    return ices, start, goal

def hash_powers(n):
    return [pow(150, i) for i in range(n)]

for x, y in iter(lambda: tuple(map(int, input().split())), (0,)):
    mp = matrix_wrap(x, y, input)
    dirs = ((1,0),(0,-1),(-1,0),(0,1))
    ice_dic, st, gl = ice_count_and_positions(mp, y, x, dirs)
    q = deque([(0, *st, list(map(lambda z: z//2, ice_dic)), 0)])
    seen = {}
    powers = hash_powers(len(ice_dic))
    while q:
        dist, px, py, counters, hs = q.popleft()
        if (px, py) == gl:
            print(dist)
            break
        for dx, dy in dirs:
            nx, ny = px+dx, py+dy
            nxt = mp[ny][nx]
            key = (nx, ny, hs)
            if nxt == "#": continue
            elif nxt == ".":
                if key in seen: continue
                seen[key] = True
                q.append((dist+1, nx, ny, counters[:], hs))
            else:
                idx = nxt
                if counters[idx] <= 0: continue
                nc = counters[:]
                nc[idx] -= 1
                nhs = hs + powers[idx]
                nkey = (nx, ny, nhs)
                if nkey in seen: continue
                seen[nkey] = True
                q.append((dist+1, nx, ny, nc, nhs))