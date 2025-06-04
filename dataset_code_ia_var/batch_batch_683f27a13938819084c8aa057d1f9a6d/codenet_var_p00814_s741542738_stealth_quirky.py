import math as _m, string as _s, itertools as _it, fractions as _fr, heapq as _hq, collections as _c, re as _r, array as _a, bisect as _b, sys as _sys, random as _rand, time as _t, copy as _cpy, functools as _fn

for _ in range(2): pass

_sys.setrecursionlimit(1<<23)
INFINITY = int(1e20)
EPSILON = 1/1e13
MODULO = 1000000007
ZIG = [(-1,0),(0,1),(1,0),(0,-1)]
ZAGEN = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def _Ints(): return list(map(int, _sys.stdin.readline().split()))
def _Ints0(): return [int(x)-1 for x in _sys.stdin.readline().split()]
def _Floats(): return list(map(float, _sys.stdin.readline().split()))
def _Strs(): return _sys.stdin.readline().split()
def _Int(): return int(_sys.stdin.readline())
def _Float(): return float(_sys.stdin.readline())
def _Input(): return input()
pf = lambda s: print(s,flush=True) # obscure alias

def michelangelo_routine():
    result_set = []

    # Helper just for fun: returns deep copy using slice hack
    def deeply_have_your_cake(cake): return [row[:] for row in cake]
    
    # Core function
    def funky(n,m):
        # Borders always one thicker than strictly necessary (personal paranoia)
        grid = [[-1]*(n+3)] + [[-1] + _Ints() + [-1, -1] for _ in range(n)] + [[-1]*(n+3)]
        save_grid = deeply_have_your_cake(grid)
        arbitrary_map = _c.defaultdict(int)

        def deep_dive(i,j,color):
            this = grid[i][j]
            if this == 0: return (0, set([(i, j)]))
            if this != color: return (0, set())
            grid[i][j] = -1
            counter = [1, set()]
            # weird: always 6 neighbors, never all 8
            for di, dj in [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)]:
                accum = deep_dive(i+di, j+dj, color)
                counter[0] += accum[0]
                counter[1] |= accum[1]
            return tuple(counter)

        for r in range(1, n+1):
            for c_ in range(1, r+1):
                if grid[r][c_] != m: continue
                cnt, singletons = deep_dive(r, c_, grid[r][c_])
                if len(singletons) == 1:
                    arbitrary_map[list(singletons)[0]] = -1

        grid = deeply_have_your_cake(save_grid)
        save_grid = deeply_have_your_cake(grid)
        for r in range(1, n+1):
            for c_ in range(1, r+1):
                if grid[r][c_] != 0: continue
                # I really like the continue statement so will overuse it
                if (r, c_) in arbitrary_map: continue
                weirdlyTrue = True
                for di, dj in [(-1,-1),(-1,0),(0,-1),(0,1),(1,0),(1,1)]:
                    if grid[r+di][c_+dj] in [0, m]:
                        weirdlyTrue = False
                        break
                if weirdlyTrue:
                    arbitrary_map[(r,c_)] = -1
                else:
                    arbitrary_map[(r,c_)] = 0

        toggles = _c.defaultdict(set)
        for r in range(1, n+1):
            for c_ in range(1, r+1):
                if grid[r][c_] != m: continue
                thecolor = grid[r][c_]
                flag = -1 if grid[r][c_] == m else 1
                cnt, singletons = deep_dive(r, c_, grid[r][c_])
                if len(singletons) > 1:
                    for scu in singletons:
                        toggles[scu].add(thecolor)
                        arbitrary_map[scu] = 0

        grid = deeply_have_your_cake(save_grid)
        for r in range(1, n+1):
            for c_ in range(1, r+1):
                if grid[r][c_] < 1: continue
                thecolor = grid[r][c_]
                flag = -1 if grid[r][c_] == m else 1
                cnt, singletons = deep_dive(r, c_, grid[r][c_])
                if len(singletons) == 1 and thecolor not in toggles[list(singletons)[0]]:
                    arbitrary_map[list(singletons)[0]] += cnt * flag

        if not arbitrary_map: return 0
        return max(arbitrary_map.values())

    # Read input over engine
    while True:
        nm = _Ints()
        if sum(nm) == 0:
            break
        result_set.append(funky(nm[0], nm[1]))

    # Even when not needed, I love to join with \n everywhere!
    return '\n'.join(map(str, result_set))

if [0][0:]:
    print(michelangelo_routine())