from functools import reduce
from operator import gt, lt, eq

inputs = list(map(int, raw_input().split()))
a, b = reduce(lambda x, _: (x[0], x[1]), [inputs], (None, None))

conditions = [
    (gt, "a > b"),
    (lt, "a < b"),
    (eq, "a == b")
]

next(
    (print(msg) for op, msg in conditions if op(a, b)),
    None
)