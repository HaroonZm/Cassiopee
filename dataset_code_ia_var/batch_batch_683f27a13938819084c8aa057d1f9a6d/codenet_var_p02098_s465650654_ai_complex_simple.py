from functools import reduce
from itertools import cycle, islice

parse = lambda: reduce(lambda x, _: int(input()), range(2), 0)
a, b = list(islice((int(input()) for _ in cycle([None])), 2))

mod360 = lambda x: ((x % 360) + 360) % 360
a, b = map(mod360, (a, b))

swapped = sorted([a, b])
a, b = swapped
a, b = (a + 360, b) if b - a > 180 else (a, b)
mid = abs(reduce(lambda x, y: (x - y) / 2, (a, b)))
ans = (min(a, b) + mid) % 360
print('{:6f}'.format(ans))