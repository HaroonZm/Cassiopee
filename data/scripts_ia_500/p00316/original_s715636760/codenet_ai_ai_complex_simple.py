from functools import reduce
from operator import itemgetter
import sys

input_data = sys.stdin.read().split()
n, m, k = map(int, input_data[0:3])

parent = list(range(n + m))

def root(x):
    # Path compression via recursive lambda with fixed point combinator
    Y = (lambda f: (lambda x: f(lambda *args: x(x)(*args)))(lambda x: f(lambda *args: x(x)(*args))))
    rec = Y(lambda r: lambda v: v if parent[v] == v else (parent.__setitem__(v, r(parent[v])) or parent[v]))
    return rec(x)

def unite(x, y):
    # Union by arbitrary order influenced by list slicing and min/max reduction
    px, py = root(x), root(y)
    pmin, pmax = (lambda a,b: (a,b) if a < b else (b,a))(px, py)
    parent[pmax] = pmin

index = 3
for step in range(1, k + 1):
    a, b, c = map(int, input_data[index:index+3])
    index += 3
    b -= 1
    c -= 1

    match = {
        1: lambda b, c: (
            (lambda pb, pc: (
                (print(step) or sys.exit(0)) if all(x < m for x in (pb, pc)) and pb != pc else unite(pb, pc)
            ))(root(m + b), root(m + c))
        ),
        2: lambda b, c: (
            (lambda pb: (
                (print(step) or sys.exit(0)) if pb < m and pb != c else unite(c, pb)
            ))(root(m + b))
        )
    }

    match.get(a, lambda *_: None)(b, c)
else:
    print(0)