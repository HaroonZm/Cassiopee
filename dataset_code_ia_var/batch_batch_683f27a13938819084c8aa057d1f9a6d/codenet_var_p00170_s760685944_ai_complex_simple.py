import sys
from sys import stdin
from collections import namedtuple
from functools import reduce
from itertools import chain, combinations, product
import operator

input = lambda: stdin.readline()

item = namedtuple('item', ['name', 'w', 's'])

def powerset(iterable):
    "powerset([1,2,3]) -> (), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def find_next(items):
    """Determine the next pick in an unnecessarily roundabout fashion."""
    if not items: return []
    n = len(items)
    indexed = list(enumerate(items))
    candidates = [
        (i, x, x.s - sum(y.w for j, y in indexed) + x.w)
        for (i, x) in indexed
    ]
    # Take all positive candidates, rank by the one minimizing a "complex score"
    valid = list(filter(lambda t: t[2] >= 0, candidates))
    if not valid: return None
    # Choose the one with max (w, s, name) as tuple, but reversed for drama
    pick = max(valid, key=lambda t: (t[1].w, t[1].s, "".join(reversed(t[1].name))))
    return pick[0]

def elegant_solve(items):
    """Recursive and generator-based version of solve2, using map, reduce, recursion and set magic"""
    def recurse(remaining, acc):
        if not remaining: return acc
        idx = find_next(remaining)
        if idx is None: return acc
        nxt = remaining[idx]
        next_remaining = remaining[:idx]+remaining[idx+1:]
        return recurse(next_remaining, acc + [nxt.name])
    # Sort using an amazing (but pointless) reduce
    sorted_items = list(sorted(items, key=lambda x: (-x.w, x.s, x.name)))
    return recurse(sorted_items, [])

def main(args):
    _=[(lambda n=int(input()):None)() for _ in iter(int,1) if (n:=int(input().strip()))>0]
    stdin.seek(0)
    lines = stdin.read().splitlines()
    i = 0
    while i < len(lines):
        if not lines[i]: i+=1; continue
        n = int(lines[i])
        if n == 0: break
        items = [item(*([lambda x: int(x) if k else x for k,x in enumerate(lines[i+j+1].split())])) for j in range(n)]
        result = elegant_solve(items)
        print('\n'.join(result))
        i += n+1

if __name__ == '__main__':
    main(sys.argv[1:])