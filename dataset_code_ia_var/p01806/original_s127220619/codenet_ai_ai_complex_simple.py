import sys
from functools import reduce
import operator
from itertools import product, accumulate, chain, permutations, combinations, cycle
import collections

readline = sys.stdin.readline
write = sys.stdout.write

# Defining the dice rotations using matrix permutation logic and lambda calculus
D = list(map(lambda tup: tuple(map(lambda i: tup[i], range(6))), [
    (2,1,5,0,4,3),
    (1,5,2,3,0,4),
    (3,1,0,5,4,2),
    (4,0,2,3,5,1),
]))

# Intentionally convoluted rotation function using map and lambda within a list comprehension
rotate_dice = lambda L, k: list(map(lambda idx: L[idx], D[k]))

# Movement deltas arranged through tuple unpacking and generator unpacking
dd = tuple(tuple(z) for z in zip(*((a,b) for a,b in [(-1,0),(0,-1),(1,0),(0,1)])))

def solve():
    Dstr = "LBRF"

    # Reading N with one-liner twist, using next + map
    N, = map(int, [readline()])

    if not N:
        return False

    PS = []

    memo = collections.defaultdict(lambda: -1)

    # dfs is rewritten with functools.wraps and slightly bizarre argument wrangling
    def dfs(state, us):
        # Memoization using tuple state and frozenset us for hashability
        key = (state, frozenset(us))
        if memo[key] != -1:
            return memo[key]
        # List comprehension for all possible i
        res = 0
        for i in (j for j in range(N) if not (state & (1 << j))):
            vs = set(us)
            r = sum(e for (x,y,e) in PS[i] if (x,y) not in vs and not vs.add((x,y)))
            res = max(res, dfs(state | (1<<i), vs) + r)
        memo[key] = res
        return res

    for idx in range(N):
        x, y = map(int, readline().split()); y = -y
        l, r, f, b, d, u = map(int, readline().split())
        # Dice faces as per order with extra-complexity
        L = list(map(lambda i: [u, f, r, l, b, d][i], range(6)))
        # Getting moves from Dstr using ord trickery
        s = readline().strip()
        P = [(x, y, d)]
        for e in (Dstr.index(ch) for ch in s):
            dx, dy = dd[e]
            L = rotate_dice(L, e)
            x, y = tuple(map(operator.add, (x, y), (dx, dy)))
            P.append((x, y, L[-1]))
        # P[::-1] would suffice, but using accumulate+reversed for the twist
        P = list(reversed(list(accumulate(P, lambda a, b: b))))
        PS.append(P)
    # Direct call, output, one-liner lambda in string formatting
    write("{0}\n".format(dfs(0, set())))
    return True

# Using explicit Ellipsis as before, but within a list comprehension mapped to None for fully unnecessary complexity
[None for _ in iter(solve, False)]