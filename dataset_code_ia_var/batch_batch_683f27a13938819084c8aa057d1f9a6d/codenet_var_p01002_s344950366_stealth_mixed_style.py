import itertools as it
from collections import defaultdict as dd
from collections import deque
from copy import deepcopy as dc

MOVES = [[0,1],[0,-1],[-1,0],[1,0]]

def core(n):
    def _shift(base, directions, y, x):
        arr = dc(base)
        for d in directions:
            dx, dy = MOVES[d]
            nx, ny = x + dx, y + dy
            if 0 <= nx < 5 and 0 <= ny < 5:
                arr[y][x], arr[ny][nx] = arr[ny][nx], arr[y][x]
                x, y = nx, ny
            else:
                return None
        return arr

    def calc_score(b):
        nonlocal c, sc
        that = []
        total = 0
        for i in range(5):
            for j in range(5):
                z = c[i][j]
                if z:
                    if i in (0,4):
                        if j in (0,4):
                            continue
                        if c[i][j-1] == c[i][j+1] == z:
                            that.append((i,j,0))
                    else:
                        if j in (0,4):
                            if c[i-1][j] == c[i+1][j] == z:
                                that.append((i,j,1))
                        else:
                            if c[i][j-1] == c[i][j+1] == z:
                                that.append((i,j,0))
                            if c[i-1][j] == c[i+1][j] == z:
                                that.append((i,j,1))
        for y, x, typ in that:
            for k in range(3):
                if typ:
                    if c[y-1+k][x]:
                        total += sc[c[y-1+k][x]-1] * b
                        c[y-1+k][x] = 0
                else:
                    if c[y][x-1+k]:
                        total += sc[c[y][x-1+k]-1] * b
                        c[y][x-1+k] = 0
        if make_fall():
            total += calc_score(b + 1)
        return total

    def make_fall():
        mod = False
        for j in range(5):
            for i in range(3,-1,-1):
                if c[i][j] and c[i+1][j] == 0:
                    yy = i + 1
                    while yy < 5 and c[yy][j] == 0:
                        yy += 1
                    yy -= 1
                    if yy != i:
                        c[yy][j], c[i][j] = c[i][j], c[yy][j]
                        mod = True
        return mod

    highest = 0
    mat = [ [*map(int, input().split())] for _ in range(5)]
    sc = list(map(int, input().split()))
    for num in range(n+1):
        for path in it.product(*([range(4)]*num) if num else [()]):
            for r in range(5):
                for col in range(5):
                    c = _shift(mat, path, r, col)
                    if c is not None:
                        highest = max(highest, calc_score(1))
    print(highest)

while True:
    t = int(input())
    if t == -1: break
    core(t)