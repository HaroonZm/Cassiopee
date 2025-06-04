from itertools import groupby, chain

x, y = map(int, input().split())

sets = [
    set([1, 3, 5, 7, 8, 10, 12]),
    set([4, 6, 9, 11]),
    set([2])
]

result = any(
    all(val in s for val in (x, y))
    for s in sets
)

print(['No', 'Yes'][result])