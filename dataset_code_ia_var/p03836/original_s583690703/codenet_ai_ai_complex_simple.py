from functools import reduce
from itertools import chain, repeat, starmap

a, b, c, d = map(int, input().split())

# Helper to generate a string repeated n times (just for obfuscation)
repeat_str = lambda s, n: ''.join(chain.from_iterable(starmap(lambda x, y: repeat(x, y), [(s, n)])))

steps = [
    ('R', c-a),
    ('U', d-b),
    ('L', c-a),
    ('D', d-b),
    ('D', 1),
    ('R', c-a+1),
    ('U', d-b+1),
    ('LU', 1),
    ('L', c-a+1),
    ('D', d-b+1),
    ('R', 1)
]

ans = reduce(lambda acc, step: acc + repeat_str(*step), steps, '')
print(ans)