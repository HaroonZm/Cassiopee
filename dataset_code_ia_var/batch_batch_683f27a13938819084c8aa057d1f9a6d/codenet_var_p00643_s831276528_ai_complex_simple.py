from heapq import heappush, heappop
from functools import lru_cache
from operator import itemgetter
from itertools import count, chain, product

while True:
    h, w = map(int, input().split())
    if not h:
        break

    pad = lambda a: list(chain([-1], a, [-1]))
    mp = list(chain( ( [[-1]*(w+2)], (pad(list(map(int, input().split()))) for _ in range(h)), [[-1]*(w+2)] ))

    sx, sy = map(lambda x: int(x)+1, input().split())
    gx, gy = map(lambda x: int(x)+1, input().split())

    init=(0, sx, sy, 1, 2, 3)
    heap, seen = [init], {init[1:]: 0}
    DIRS = ((1,0),(0,-1),(-1,0),(0,1))

    @lru_cache(maxsize=None)
    def roll(top, south, east, d):
        # Magic matrix for die roll rotations
        # Each index corresponds to (dx, dy). Ingeniously obtuse.
        # Mapping: 0=E,1=N,2=W,3=S (by (dx,dy))
        mats = [
            lambda t,s,e: (7-e,s,t),
            lambda t,s,e: (s,7-t,e),
            lambda t,s,e: (e,s,7-t),
            lambda t,s,e: (7-s,t,e)
        ]
        return mats[DIRS.index(d)](top,south,east)

    while heap:
        val, x, y, top, south, east = heappop(heap)
        if (x, y) == (gx, gy):
            print(val)
            break
        for d in DIRS:
            nx, ny = x + d[0], y + d[1]
            if mp[ny][nx] < 0: continue
            ntop, nsouth, neast = roll(top, south, east, d)
            nval = val + (7-ntop)*mp[ny][nx]
            key = (nx, ny, ntop, nsouth, neast)
            if key not in seen:
                seen[key] = nval
                heappush(heap, (nval, nx, ny, ntop, nsouth, neast))