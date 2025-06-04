from functools import reduce
from itertools import count, takewhile

xx, yy = map(int, input().split())

def fib_gen():
    a, b = 1, 1
    yield a
    while True:
        yield b
        a, b = b, a + b

fib = list(takewhile(lambda x: x <= 10**7, fib_gen()))
fib = reduce(lambda acc, x: acc + [x], fib, [])

coords = [
    (lambda x, y, a: (x + y, y + x, a)),
    (lambda x, y, a: (x - a, y + a, a)),
    (lambda x, y, a: (x - a, y, a)),
    (lambda x, y, a: (x, y - a, a))
]

area = [[0, 0, 1]]
state = (0, 0, fib[0], fib[1])
for n in range(1, len(fib)):
    x, y, f1, f2 = state
    a = fib[n]
    idx = n % 4
    cx, cy, ca = coords[idx](x, y, a)
    area.append([cx, cy, a])
    state = (cx, cy, f2, a)

def is_inside(region, px, py):
    x, y, a = region
    return (lambda a, b, c, d: a <= c < a + b and d < py <= y)(x, a, px, y - a)

print(next((i % 3 + 1 for i, reg in enumerate(area) if is_inside(reg, xx, yy)), None))