while True:
    m = int(input())
    if m == 0:
        break
    constellation = [tuple(map(int, input().split())) for _ in range(m)]
    n = int(input())
    photo = [tuple(map(int, input().split())) for _ in range(n)]
    constellation_set = set(constellation)
    shift = None
    c0 = constellation[0]
    for p in photo:
        dx = p[0] - c0[0]
        dy = p[1] - c0[1]
        translated = {(x + dx, y + dy) for (x, y) in constellation}
        if translated.issubset(photo):
            shift = (dx, dy)
            break
    print(shift[0], shift[1])