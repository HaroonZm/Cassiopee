from functools import reduce
from operator import add, mul
H, N = map(int, input().split())
A = list(map(int, input().split()))
result = ('Yes', 'No')[
    (lambda x, y: (y - x) > 0)(
        reduce(add, A, 0), H
    )
]
print(result)