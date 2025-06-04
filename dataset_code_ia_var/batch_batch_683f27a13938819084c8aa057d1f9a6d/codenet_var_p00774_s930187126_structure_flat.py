while True:
    score = 0
    h = int(input())
    if h == 0:
        break
    w = 5
    field = []
    for x in range(h):
        field.append(list(map(int, input().split())))
    while True:
        flg = True
        for y in range(len(field)):
            row = field[y]
            target = None
            cnt = 0
            fs = []
            f = None
            t = None
            for i, cell in enumerate(row):
                if target is not None and cell == target:
                    cnt += 1
                else:
                    if cnt >= 2:
                        f = fs[-1]
                        t = i - 1
                    fs.append(i)
                    target = cell
                    cnt = 0
            if cnt >= 2:
                f = fs[-1]
                t = i
            if f is not None:
                score += (t - f + 1) * row[f]
                for k in range(f, t + 1):
                    row[k] = None
                flg = False
        if flg:
            break
        for y in range(len(field) - 2, -1, -1):  # du bas vers le haut sauf dernière ligne
            for x in range(w):
                if field[y + 1][x] is None:
                    n = y + 1
                    while n > 0 and field[n][x] is None:
                        field[n][x] = field[n - 1][x]
                        n -= 1
                    field[0][x] = None
    print(score)