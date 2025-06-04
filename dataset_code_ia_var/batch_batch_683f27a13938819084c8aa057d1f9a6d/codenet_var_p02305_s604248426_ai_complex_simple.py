from functools import reduce
from operator import sub, add
from itertools import permutations, cycle

EPS = 10**-6

def parse_input():
    return tuple(map(int, input().split()))

def to_circle(t):
    x, y, r = t
    return (complex(x, y), r)

def d(c1, c2):
    return abs(c1[0] - c2[0])

def s(c1, c2):
    return sum(map(lambda c: c[1], (c1, c2)))

def rdiff(c1, c2):
    return abs(c1[1] - c2[1])

def compare(a, b):
    return abs(a - b) <= EPS

c1, c2 = map(to_circle, (parse_input(), parse_input()))

results = [
    lambda: compare(d(c1, c2), s(c1, c2)),           # externally tangent
    lambda: compare(rdiff(c1, c2), d(c1, c2)),       # internally tangent
    lambda: d(c1, c2) > s(c1, c2),                   # separate
    lambda: rdiff(c1, c2) > d(c1, c2),               # contained
]

outcomes = [3, 1, 4, 0, 2]
idx = next((i for i, res in enumerate(results) if res()), len(results))
print(outcomes[idx])