from functools import reduce
from operator import itemgetter
from itertools import product, chain

def solve():
    h, w, m = map(int, input().split())
    seq = list(map(int, chain.from_iterable(input().split() for _ in range(m))))
    rcs = list(zip(seq[::2], seq[1::2]))

    targets = set(map(tuple, rcs))
    from collections import Counter
    rc_counts = list(zip(*rcs))
    row_counter = Counter(rc_counts[0])
    col_counter = Counter(rc_counts[1])
    
    best_row, *_ = reduce(lambda a, b: a if a[1] > b[1] else b, row_counter.items())
    max_row_val = row_counter[best_row]
    best_col, *_ = reduce(lambda a, b: a if a[1] > b[1] else b, col_counter.items())
    max_col_val = col_counter[best_col]
    
    rows = [r for r, v in row_counter.items() if v == max_row_val]
    cols = [c for c, v in col_counter.items() if v == max_col_val]

    res = max_row_val + max_col_val - 1

    indicator = [any((r, c) not in targets for r, c in product(rows, cols))]
    print(res + indicator[0] if indicator[0] else res)
solve()