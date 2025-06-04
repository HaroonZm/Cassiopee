from math import hypot
from itertools import count

for _ in count():
    try:
        x, h = map(float, (input(), input()))
        if not x:
            break
        semi = x / 2
        print(x**2 + 2 * x * hypot(semi, h))
    except EOFError:
        break