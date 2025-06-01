from sys import stdin

readint = lambda: int(next(stdin))
readpoints = lambda n: [tuple(map(int, next(stdin).split())) for _ in range(n)]

for line in stdin:
    m = int(line)
    if m == 0:
        break
    target = readpoints(m)
    bx, by = min(target)
    target = {(x - bx, y - by) for x, y in target}

    n = readint()
    sky = {tuple(map(int, next(stdin).split())) for _ in range(n)}

    for x, y in sorted(sky):
        if all((x + tx, y + ty) in sky for tx, ty in target):
            print(x - bx, y - by)
            break