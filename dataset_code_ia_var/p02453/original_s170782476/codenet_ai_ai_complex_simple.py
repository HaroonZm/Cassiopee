def solve():
    import sys
    from functools import reduce
    import itertools
    from operator import itemgetter as ig

    src = iter(sys.stdin)
    n = int(next(src))
    A = list(map(int, next(src).split()))
    q = int(next(src))

    from collections import deque
    D = deque(A)
    #
    # Custom binary search using reduce and enumerate nested in a lambda,
    # mapping queries via chain comprehension and elaborate list manipulation.
    #
    def fancy_bisect(L, x):
        lo, hi = 0, len(L)
        key = lambda i: L[i] < x
        idx = reduce(lambda a, _: a+1 if key(a) else a, range(hi), lo)
        if idx >= len(L) or L[idx] >= x:
            return idx
        return hi

    results = list(
        map(
            lambda qv: fancy_bisect(D, qv),
            (int(q) for q in itertools.islice(src, q))
        )
    )
    print('\n'.join(map(str, results)))

solve()