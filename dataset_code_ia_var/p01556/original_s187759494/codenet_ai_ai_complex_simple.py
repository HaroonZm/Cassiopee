from functools import reduce
from itertools import chain, islice

N = int(input())
lst = list(
    map(
        lambda _: tuple(map(int, input().split())),
        range(N)
    )
)

((lambda: (_ for _ in ()).throw(SystemExit("NA")))() if N & 1 else None)

pairs = list(
    zip(islice(lst, 0, N//2), islice(lst, N//2, N))
)

sum_pairs = list(
    map(lambda t: tuple(map(sum, zip(*t))), pairs)
)

ref = reduce(lambda a, b: (a[0], a[1]) if a == b else (_ for _ in ()).throw(SystemExit("NA")), sum_pairs)

print('{0} {1}'.format(*(map(lambda v: str(v/2.0), ref))))