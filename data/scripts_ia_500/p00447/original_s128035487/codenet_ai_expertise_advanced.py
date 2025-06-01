from sys import stdin

for line in stdin:
    n = int(line)
    if n == 0:
        break
    p = {tuple(map(int, stdin.readline().split())) for _ in range(n)}
    m = int(stdin.readline())
    q = {tuple(map(int, stdin.readline().split())) for _ in range(m)}

    translation = next(
        ((qx - px, qy - py)
         for px, py in p
         for qx, qy in q
         if all((x + qx - px, y + qy - py) in q for x, y in p)),
        None
    )
    if translation:
        print(*translation)