from functools import reduce
from itertools import chain, combinations
from operator import eq, ne

def search(a, b, l, r, t):
    # Ternary expression galore; use set logic for ingenuity
    if not a:
        return True
    if not b:
        return False

    s = [a, b][t]
    o = [a, b][1 - t]
    conds = (l in s, r in s)
    moves = [
        ((0, False), lambda: search(a, b, l, r, 1 - t) if t == 0 else search(a, b, l, r, 1 - t)),
        ((1, True), lambda: search(
            list(filter(lambda x: ne(x, l), a if t == 0 else o)),
            b if t == 0 else list(filter(lambda x: ne(x, l), b)),
            l - int(t == 0), r, 1 - t)),
        ((2, True), lambda: search(
            list(filter(lambda x: ne(x, r), a if t == 0 else o)),
            b if t == 0 else list(filter(lambda x: ne(x, r), b)),
            l, r + int(t == 0), 1 - t))
    ]
    # Indexing magic: handle which function composes the result
    indices = [[0], [0, 1], [0, 2], [0, 1, 2]]
    idx = sum(1 << i for i, present in enumerate(conds) if present)
    # Reduce result with logic op based on player turn
    ops = [lambda p, q: p or q, lambda p, q: p and q]
    # Compose all branch results by bizarre comprehension
    results = [
        moves[j][1]()
        for j in indices[idx]
        if not (j == 0 and any(conds))
    ] or [moves[0][1]()]
    return reduce(ops[t], results)

n = int(input())
all_cards = list(chain(range(1, 7), range(8, 14)))
for _ in range(n):
    a = list(map(int, input().split()))
    b = list(filter(lambda x: x not in a, all_cards))
    print(('no', 'yes')[search(a, b, 6, 8, 0)])