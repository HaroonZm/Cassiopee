while True:
    m = int(input())
    if m == 0:
        break
    target = []
    for _ in range(m):
        x, y = input().split()
        target.append((int(x), int(y)))

    bx = target[0][0]
    by = target[0][1]
    for x, y in target:
        if x < bx or (x == bx and y < by):
            bx, by = x, y

    norm_target = set()
    for x, y in target:
        norm_target.add((x - bx, y - by))

    n = int(input())
    sky = set()
    for _ in range(n):
        x, y = input().split()
        sky.add((int(x), int(y)))

    sky_list = list(sky)
    sky_list.sort()

    for x, y in sky_list:
        match = True
        for tx, ty in norm_target:
            if (x + tx, y + ty) not in sky:
                match = False
                break
        if match:
            print(x - bx, y - by)
            break