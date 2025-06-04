import sys
from functools import lru_cache
from itertools import product, chain
from operator import xor

stdin, stdout = sys.stdin, sys.stdout
def solve():
    H, W = map(int, next(iter(stdin)))
    trans = {".":0, "X":1}
    lst = (stdin.readline() for _ in range(H))
    S = [[trans[c] for c in row.strip()] for row in lst]

    def rectangles(px, py, qx, qy):
        # generator of all inner rectangles' (x, y) where S[y][x] == 0
        return ((x, y) for y, x in product(range(py, qy), range(px, qx)) if not S[y][x])

    @lru_cache(maxsize=None)
    def sprague(px, py, qx, qy):
        mex_set = set(
            xor(
                xor(*map(sprague, ( (px, py, x, y),
                                   (x+1, py, qx, y),
                                   (px, y+1, x, qy),
                                   (x+1, y+1, qx, qy))))
                for x, y in rectangles(px, py, qx, qy)
        )
        return next(k for k in range(H*W+1) if k not in mex_set)

    outcome = sprague(0, 0, W, H)
    stdout.write("First\n" if outcome else "Second\n")
solve()