from sys import stdin
from itertools import product

def parse():
    for line in stdin:
        yield line.strip()

lines = parse()
while True:
    n_h = next(lines)
    n, h = map(int, n_h.split())
    if n == 0:
        break
    hit = set()
    axis_map = {
        "xy": lambda a, b: ((int(a), int(b), z) for z in range(1, n + 1)),
        "xz": lambda a, b: ((int(a), y, int(b)) for y in range(1, n + 1)),
        "yz": lambda a, b: ((x, int(a), int(b)) for x in range(1, n + 1)),
    }
    for _ in range(h):
        c, a, b = next(lines).split()
        hit.update(axis_map[c](a, b))
    print(n ** 3 - len(hit))