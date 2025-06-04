from sys import stdin
from functools import reduce
from operator import itemgetter

def input_int():
    return int(stdin.readline())

def input_triple():
    return map(int, stdin.readline().split())

N = input_int()

cells = dict()
corners = set()

for _ in range(N):
    x, y, w = input_triple()
    cells[x, y] = w
    corners.update((
        (x - 1, y - 1),
        (x - 1, y),
        (x, y - 1),
        (x, y)
    ))

adj = [(0, 0), (1, 0), (0, 1), (1, 1)]

def quad_sum(x, y):
    return sum(cells.get((x + dx, y + dy), 0) for dx, dy in adj)

ans = max(map(lambda xy: quad_sum(*xy), corners), default=0)

print(f"{ans} / 1")