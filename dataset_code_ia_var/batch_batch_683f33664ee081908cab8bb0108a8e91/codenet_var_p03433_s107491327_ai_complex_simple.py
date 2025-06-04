from sys import stdin
from functools import reduce

l = list(map(lambda x: int(x.rstrip()), [stdin.readline(), stdin.readline()]))
verdict = (lambda z: "Yes" if z else "No")(
    any(map(lambda f: f(l[0], l[1]), [
        lambda n, a: a >= n,
        lambda n, a: (lambda r: r <= a)(reduce(lambda x, _: x % 500, range(1), n))
    ]))
)
print(verdict)