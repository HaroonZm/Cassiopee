while True:
    score = 0
    h = int(input())
    if h == 0: break
    w = 5

    field = [list(map(int, input().split())) for x in range(h)]

    def delete(field):
        flg = True
        for row in field:
            target = None
            cnt = 0
            fs = []
            f = None
            t = None
            for i, cell in enumerate(row):
                if target != None and cell == target:
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

            if f != None:
                global score
                score += (t - f + 1) * row[f]
                for i in range(f, t + 1):
                    row[i] = None
                flg = False
        if flg: return flg
        return field

    def drop(field):
        for y, row in enumerate(field[:-1]):
            for x, cell in enumerate(row):
                if field[y + 1][x] == None:
                    for n in range(y + 1, 0, -1):
                        field[n][x] = field[n - 1][x]
                    else:
                        field[0][x] = None
        return field

    while True:
        field = delete(field)
        if field == True:
            break
        field = drop(field)
        # for x in field: print(*map(lambda x: "X" if x == None else x, x))
        # print("===========")
    print(score)