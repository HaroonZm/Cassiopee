from sys import stdin

deltas = [(2, -1), (2, 0), (2, 1), (1, 2), (0, 2), (-1, 2), (-2, 1), (-2, 0), (-2, -1), (-1, -2), (0, -2), (1, -2)]

def within_bounds(x, y):
    return 0 <= x <= 9 and 0 <= y <= 9

def is_adjacent(x, y, sx, sy):
    return within_bounds(x, y) and abs(x - sx) < 2 and abs(y - sy) < 2

def solve(x, y, i):
    if i == 2 * n:
        return True
    sx, sy = xy[i], xy[i + 1]
    return any(
        is_adjacent(x + dx, y + dy, sx, sy) and solve(x + dx, y + dy, i + 2)
        for dx, dy in deltas
    )

for line in stdin:
    if not line.strip():
        continue
    x, y = map(int, line.split())
    if x == y == 0:
        break
    n = int(next(stdin))
    xy = list(map(int, next(stdin).split()))
    print("OK" if solve(x, y, 0) else "NA")