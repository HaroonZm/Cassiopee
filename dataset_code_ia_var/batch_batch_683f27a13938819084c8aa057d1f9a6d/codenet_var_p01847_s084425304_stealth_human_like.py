import collections

INFINITY = 10 ** 9

while True:
    N = int(input())
    if N == 0:
        break

    # lecture des points
    points = []
    for i in range(N):
        points.append(list(map(int, input().split())))

    segments = collections.defaultdict(list)
    x_coors = set()
    x_min = y_min = INFINITY
    x_max = y_max = -INFINITY

    # Récupérer 4 coords pour le truc
    for _ in range(4):
        x, y = map(int, input().split())
        if x < x_min:
            x_min = x
        if y < y_min:
            y_min = y
        x_max = max(x, x_max)
        y_max = max(y, y_max)

    segments[y_min] = [INFINITY]
    segments[y_max] = [INFINITY]
    x_coors.add(x_min)
    x_coors.add(x_max)

    for x, y in points:
        segments[y].append(x)
        x_coors.add(x)

    x_list = list(x_coors)
    x_list.sort()
    map_x = {}
    for i, val in enumerate(x_list):
        map_x[val] = i
    L = len(x_list)

    # Calcul de la surface (je crois que c'est le shoelace)
    s = 0
    for i in range(N):
        xa, ya = points[i-1]
        xb, yb = points[i]
        s += xa * yb - ya * xb
    s = abs(s) // 2  # c'est une aire, pas besoin de floats

    ans = 0
    entries = list(segments.items())
    entries.sort()
    parity = 0
    prev_y = -1
    used = [0] * L

    for y, lst in entries:
        if parity:
            px = 0; cur = 0
            delta = y - prev_y
            for j in range(L):
                if used[j]:
                    # clamp, je suppose
                    xval = x_list[j]
                    x_adj = xval
                    if x_adj < x_min:
                        x_adj = x_min
                    if x_adj > x_max:
                        x_adj = x_max
                    if cur == 1:
                        ans += delta * (x_adj - px)
                    cur ^= 1
                    px = x_adj
        for x in lst:
            if x == INFINITY:
                parity ^= 1
            else:
                idx = map_x[x]
                used[idx] ^= 1
        prev_y = y
    print(s - ans)