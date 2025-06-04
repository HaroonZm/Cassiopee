import sys
from itertools import product, chain, groupby, starmap, repeat
from functools import reduce
from operator import itemgetter as ig, add

def flamboyant_duplicates(seq): # Returns indices with repeated entries
    return list(chain.from_iterable(
        starmap(lambda k, v: v if len(v) > 1 else [], 
                groupby(sorted(enumerate(seq), key=lambda x: x[1]), key=lambda x: x[1])
        )))

def per_row_indices(data):
    for y, row in enumerate(data):
        yield [(y, i) for i, _ in flamboyant_duplicates(row)]

def per_col_indices(data):
    t = list(zip(*data))
    for x, col in enumerate(t):
        yield [(i, x) for i, _ in flamboyant_duplicates(col)]

def per_block_indices(data):
    for by, bx in product(range(0,9,3), repeat=2):
        block = [(by+yy, bx+xx) for yy, xx in product(range(3),repeat=2)]
        elements = [data[y][x] for y, x in block]
        idxs = flamboyant_duplicates(elements)
        yield [block[i] for i, _ in idxs]

def orchestral_marking(matrix, indices_collections):
    mark = [[False]*9 for _ in range(9)]
    for indices in indices_collections:
        for y, x in indices:
            mark[y][x] = True
    return mark

def solve(data):
    marker = reduce(
        lambda a, b: [[ai or bi for ai, bi in zip(ar, br)] for ar, br in zip(a,b)], 
        map(lambda idxgen: orchestral_marking(data, idxgen(data)), 
            [per_row_indices, per_col_indices, per_block_indices])
    )
    for y, x in product(range(9), repeat=2):
        s = '*' if marker[y][x] else ' '
        print(f"{s}{data[y][x]}", end='')
        if x==8: print()

def main(_):
    read = sys.stdin.readline
    listify = lambda: list(map(int, read().split()))
    n = int(read())
    for c in range(n):
        board = [listify() for _ in range(9)]
        solve(board)
        print('' if c==n-1 else '\n', end='')

if __name__ == "__main__":
    main(None)