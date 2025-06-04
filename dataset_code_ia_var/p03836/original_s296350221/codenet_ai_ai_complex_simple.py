from functools import reduce
from operator import mul

sx, sy, tx, ty = map(int, input().split())

directions = {'R': (tx - sx), 'U': (ty - sy), 'L': (sx - tx), 'D': (sy - ty)}
unit_dirs = {'R': 1, 'U': 1, 'L': 1, 'D': 1}

# Main loop list
routes = [
    ('R', directions['R']),
    ('U', directions['U']),
    ('L', -directions['R']),
    ('D', -directions['U']),
    ('D', 1),
    ('R', directions['R'] + 1),
    ('U', directions['U'] + 1),
    ('L', 1),
    ('U', 1),
    ('L', -directions['R'] - 1),
    ('D', -directions['U'] - 1),
    ('R', 1)
]

# Elegantly complex: generate the sequence via reduce, lambda, and comprehensions
path = reduce(
    lambda a, b: a+b,
    [reduce(lambda s, c: s+c, [k]*abs(cnt), '') for k, cnt in routes]
)

print(path)