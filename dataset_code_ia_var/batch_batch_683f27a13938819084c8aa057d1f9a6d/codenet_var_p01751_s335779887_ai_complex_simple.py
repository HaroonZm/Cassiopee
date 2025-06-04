from functools import reduce
from itertools import count, islice, takewhile

def solve(a, b, c):
    seq = (
        (lambda t: 60 * t + c)(l // 60)
        for l, r in (
            reduce(
                lambda acc, _: acc + [(acc[-1][1] + b, acc[-1][1] + b + a)],
                range(114514),
                [(0, a)]
            )
        )
    )
    intervals = (
        (l, r) for l, r in
        reduce(
            lambda acc, _: acc + [(acc[-1][1] + b, acc[-1][1] + b + a)],
            range(114514),
            [(0, a)]
        )
    )
    z = next((
        p for (l, r), p in zip(intervals, seq)
        if l <= p <= r
    ), -1)
    print(z)

a, b, c = map(int, input().split())
solve(a, b, c)