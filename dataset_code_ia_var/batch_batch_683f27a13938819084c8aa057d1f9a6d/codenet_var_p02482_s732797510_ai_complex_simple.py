import operator
from functools import reduce

a, b = map(int, raw_input().split())

comparisons = [
    (operator.lt, "a < b"),
    (operator.gt, "a > b"),
    (operator.eq, "a == b")
]

print(
    next(
        result for pred, result in comparisons
        if reduce(lambda x, _: pred(a, b), [None], True)
    )
)