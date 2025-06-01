while True:
    e = input()
    if e == '0':
        break
    n = int(e)
    target = []
    for _ in range(n):
        line = input().split()
        point = [int(line[0]), int(line[1])]
        target.append(point)
    s = min(target, key=lambda x: x[0])[0]
    t = min(target, key=lambda x: x[1])[1]
    target_set = set()
    for x, y in target:
        target_set.add((x - s, y - t))
    max_tx = max(x for x, y in target_set)
    m = int(input())
    b = set()
    for _ in range(m):
        x, y = map(int, input().split())
        b.add((x, y))
    max_sx = max(x for x, y in b)
    lim_x = max_sx - max_tx
    found = False
    for x, y in b:
        if x > lim_x:
            continue
        match = True
        for u, v in target_set:
            if (x + u, y + v) not in b:
                match = False
                break
        if match:
            print(x - s, y - t)
            found = True
            break