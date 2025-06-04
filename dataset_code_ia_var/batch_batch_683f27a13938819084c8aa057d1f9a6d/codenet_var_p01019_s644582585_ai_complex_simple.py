from functools import reduce
from itertools import product, chain, starmap, groupby

dic = dict(zip(
    map(tuple, [
        list(product([0], range(5))) +
        [(1, 0), (1, 4)] +
        list(product([2], range(5))),
        list(product([0], range(5))),
        [(0, 0), (0, 2), (0, 3), (0, 4),
         (1, 0), (1, 2), (1, 4)] +
        [(2, 0), (2, 1), (2, 2), (2, 4)],
        [(0, 0), (0, 2), (0, 4),
         (1, 0), (1, 2), (1, 4)] +
        [(2, i) for i in range(5)],
        [(0, 0), (0, 1), (0, 2), (1, 2)] +
        [(2, i) for i in range(5)],
        [(0, 0), (0, 1), (0, 2), (0, 4),
         (1, 0), (1, 2), (1, 4)] +
        [(2, 0), (2, 2), (2, 3), (2, 4)],
        [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
         (1, 0), (1, 2), (1, 4)] +
        [(2, 0), (2, 2), (2, 3), (2, 4)],
        [(0, 0), (1, 0)] +
        [(2, i) for i in range(5)],
        [(0, i) for i in range(5)] +
        [(1, 0), (1, 2), (1, 4)] +
        [(2, i) for i in range(5)],
        [(0, 0), (0, 1), (0, 2), (0, 4),
         (1, 0), (1, 2), (1, 4)] +
        [(2, i) for i in range(5)],
        [(0, 0), (1, -1), (1, 0), (1, 1), (2, 0)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 0), ]
    ]),
    "0123456789+ -*"
))

n, sz = int(input()), 201
mp = [bytearray(sz) for _ in range(sz)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for xi, yi in (lambda a, b, c, d: ((x1 if x1==x2 else x, y1 if y1==y2 else y)
        for x, y in zip(range(min(a, c), max(a, c)+1), range(min(b, d), max(b, d)+1))))(x1, y1, x2, y2):
        mp[yi][xi] = 1

checked = [bytearray(sz) for _ in range(sz)]
vec = ((1,0),(0,-1),(-1,0),(0,1))

def trace(x, y, refx, refy, stk):
    def neighbors():
        return ((x+d[0], y+d[1]) for d in vec if 0<=x+d[0]<sz and 0<=y+d[1]<sz and mp[y+d[1]][x+d[0]] and not checked[y+d[1]][x+d[0]])
    for nx, ny in neighbors():
        checked[ny][nx] = 1
        stk.append((nx-refx, ny-refy))
        trace(nx, ny, refx, refy, stk)

stuff = [(x, y)
    for x, y in product(range(sz), repeat=2)
    if mp[y][x] and not checked[y][x]]
    
res = ""
for x, y in stuff:
    if checked[y][x]: continue
    checked[y][x] = 1
    s = [(0,0)]
    trace(x, y, x, y, s)
    res += dic[tuple(sorted(s))]

print(eval(res))