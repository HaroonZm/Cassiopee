while True:
    y1, m1, d1, y2, m2, d2 = map(int, raw_input().split())
    if y1 < 0 or m1 < 0 or d1 < 0 or y2 < 0 or m2 < 0 or d2 < 0:
        break

    if y1 == y2 and m1 == m2:
        print d2 - d1
        continue

    if y1 % 400 == 0 or (y1 % 4 == 0 and y1 % 100 != 0):
        fev1 = 29
    else:
        fev1 = 28

    t = 0
    if m1 in [4,6,9,11]:
        t += (30 - d1 + 1)
    elif m1 in [1,3,5,7,8,10,12]:
        t += (31 - d1 + 1)
    else:
        t += (fev1 - d1 + 1)

    if y1 == y2:
        if y2 % 400 == 0 or (y2 % 4 == 0 and y2 % 100 != 0):
            fev2 = 29
        else:
            fev2 = 28
        for m in range(m1+1, m2):
            if m in [4,6,9,11]:
                t += 30
            elif m in [1,3,5,7,8,10,12]:
                t += 31
            else:
                t += fev2
        t += (d2 - 1)
        print t
        continue

    for m in range(m1+1, 13):
        if m in [4,6,9,11]:
            t += 30
        elif m in [1,3,5,7,8,10,12]:
            t += 31
        else:
            t += fev1

    for y in range(y1+1, y2):
        if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
            t += 366
        else:
            t += 365

    if y2 % 400 == 0 or (y2 % 4 == 0 and y2 % 100 != 0):
        fev2 = 29
    else:
        fev2 = 28

    for m in range(1, m2):
        if m in [4,6,9,11]:
            t += 30
        elif m in [1,3,5,7,8,10,12]:
            t += 31
        else:
            t += fev2

    t += (d2 - 1)
    print t