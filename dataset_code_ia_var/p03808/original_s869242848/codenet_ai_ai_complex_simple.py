from functools import reduce
from operator import add, sub, mul
from itertools import islice, cycle, starmap, tee

s = lambda n, a: (
    (lambda N, sa, sn:
        all([
            sa % N == 0,
            sa >= N,
            (lambda da:
                all([
                    max(da) <= sn,
                    sum(da) == 0,
                    all(map(lambda di: (sn - di) % n == 0, da))
                ])
            )(
                list(starmap(sub, zip(islice(cycle(a), 1, n + 1), a)))
            )
        ])
    )(n * (n + 1) // 2, reduce(add, a, 0), reduce(add, a, 0) // (n * (n + 1) // 2))
)

n = int(raw_input())
a = list(map(int, raw_input().split()))
print("YES" if s(n, a) else "NO")