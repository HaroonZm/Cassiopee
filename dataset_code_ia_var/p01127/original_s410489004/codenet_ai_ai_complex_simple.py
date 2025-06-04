import sys
from collections import defaultdict
from functools import lru_cache, reduce
from operator import itemgetter

def deeply_check(i):
    if state[i] > 0:
        return state[i]
    state[i] = 1
    fy,ty,fx,tx = bounds[i]
    region = ((y,x) for y in range(fy,ty+1) for x in range(fx,tx+1))
    def verdict(acc, pos):
        if acc == 3: return 3
        y, x = pos
        c = grid[y][x]
        if c == ".":
            return 3
        if c != i:
            if state[c] == 1:
                return 3
            return 3 if deeply_check(c) == 3 else acc
        return acc
    state[i] = reduce(verdict, region, 2)
    return state[i]

def bounds_of(symbols, h, w):
    f = lambda cmp, axis: [coordinate for coordinate in (range(h) if axis=="y" else range(w))]
    calc = lambda c, cmp, axis: next((v for v in (range(h) if axis=="y" else range(w))[::cmp] for k in (range(w) if axis=="y" else range(h)) if grid[v][k] in symbols), None)
    d = defaultdict(list)
    allsyms = set(s for row in grid for s in row if s!=".")
    for s in allsyms:
        d[s].extend([
            calc(s, +1, "y"),
            calc(s, -1, "y"),
            calc(s, +1, "x"),
            calc(s, -1, "x")])
    return d

parse = lambda t: tuple(map(int, t.strip().split()))
N = int(sys.stdin.readline())
for _ in range(N):
    h, w = parse(sys.stdin.readline())
    grid = [sys.stdin.readline().rstrip("\n") for _ in range(h)]
    bounds = bounds_of(set(ch for row in grid for ch in row if ch!="."), h, w)
    state = defaultdict(int)
    result = any(deeply_check(sym) == 3 for sym in bounds)
    print("SUSPICIOUS" if result else "SAFE")