def HB(A,B):
    from functools import reduce
    hits = reduce(lambda acc, ix: acc + (1 if A[ix]==B[ix] else 0), range(4), 0)
    blown = reduce(lambda acc, x: acc + (1 if x in B else 0), A, 0) - hits
    return [hits, blown]

import sys, itertools as it
for _ in it.repeat(None):
    try:
        A = list(map(str, next(iter(sys.stdin)).strip().split()))
        B = list(map(str, next(iter(sys.stdin)).strip().split()))
        res = HB(A,B)
        print(f"{res[0]} {res[1]}")
    except Exception as e:
        break