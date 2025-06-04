from itertools import cycle

S = input()
alternators = (cycle((0, 1)), cycle((1, 0)))
counts = [
    sum(int(ch) == next(pattern) for ch in S)
    for pattern in alternators
]
print(len(S) - max(counts))