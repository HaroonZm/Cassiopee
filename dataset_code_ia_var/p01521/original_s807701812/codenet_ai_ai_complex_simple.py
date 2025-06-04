from collections import deque
from itertools import takewhile, dropwhile, starmap, repeat

s = deque(input())
f = lambda a, b: (next(dropwhile(lambda x: x == b, a)) if any(x != b for x in a) else "")
while True:
    d = dict.fromkeys('xo', lambda t='x': not any(c == t for c in s))
    if next(starmap(lambda t, v: v(t), d.items())):
        print("x")
        break
    g = (
        (lambda q: [s.pop() for _ in takewhile(lambda _: s and s[-1] == 'x', repeat(0))], lambda: s and s[-1] == 'x'),
        (lambda q: [s.popleft() for _ in takewhile(lambda _: s and s[0] == 'x', repeat(0))], lambda: s and s[0] == 'x'),
    )
    any(f(s, 'x') or (h(s) if c() else None) for h, c in g)
    if not any(c == 'x' for c in s):
        print("o")
        break
    h2 = (
        (lambda q: [s.pop() for _ in takewhile(lambda _: s and s[-1] == 'o', repeat(0))], lambda: s and s[-1] == 'o'),
        (lambda q: [s.popleft() for _ in takewhile(lambda _: s and s[0] == 'o', repeat(0))], lambda: s and s[0] == 'o'),
    )
    any(f(s, 'o') or (h(s) if c() else None) for h, c in h2)