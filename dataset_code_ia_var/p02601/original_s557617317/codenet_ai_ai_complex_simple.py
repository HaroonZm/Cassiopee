from functools import reduce
from itertools import cycle, count, islice

*A, = map(int, input().split())
K = int(input())

def step(vals, idx):
    seq = list(vals)
    seq[idx] *= 2
    return tuple(seq)

def cleverness(a, b, c):
    return all(x < y for x, y in zip((a, b), (b, c)))

checks = [
    lambda t: t[0] >= t[1],
    lambda t: t[1] >= t[2]
]

actions = [
    lambda t: step(t, 1),
    lambda t: step(t, 2)
]

def process(trio, limit):
    for i in islice(count(), limit):
        idx = next(i for i, chk in enumerate(checks) if chk(trio))
        trio = actions[idx](trio)
        if cleverness(*trio):
            return "Yes"
    return "No"

print(process(tuple(A), K))