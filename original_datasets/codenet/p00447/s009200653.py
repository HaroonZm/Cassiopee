while True:
    m = int(input())
    if not m:
        break
    target = [tuple(map(int, input().split())) for _ in range(m)]
    bx, by = min(target)
    target = {(x - bx, y - by) for x, y in target}

    n = int(input())
    sky = {tuple(map(int, input().split())) for _ in range(n)}
    sky_s = sorted(sky)

    for x, y in sky_s:
        for tx, ty in target:
            if (x + tx, y + ty) not in sky:
                break
        else:
            print(x - bx, y - by)
            break