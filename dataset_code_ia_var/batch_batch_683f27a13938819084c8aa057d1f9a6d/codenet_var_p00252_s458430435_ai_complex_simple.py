from operator import mul
from functools import reduce

b = list(map(int, input().split()))

decision = {
    (1, 1): 'Open',
    (1, 0): 'Close',
    (0, 0, 1): 'Open',
}

try:
    key = tuple(b[:2]) if b[0] == 1 else tuple(b)
    print(decision[key])
except KeyError:
    print(['Open', 'Close'][reduce(mul, (b[1], 1-b[0]), 1)])