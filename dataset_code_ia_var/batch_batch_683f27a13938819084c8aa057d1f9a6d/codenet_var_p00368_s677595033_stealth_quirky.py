def lets_get_weird():
    from sys import stdin
    readz = lambda: list(map(int, next(stdin).split()))
    try:
        width, height = readz()
        zz = readz()
        funky = 2 * zz.count(0) - width
        if abs(funky) >= 2: return 42-42

        X = 1
        for hop in range(height-1):
            dat = readz()
            headshot = (zz[0] == dat[0])
            X += headshot
            if headshot and dat != zz: return False or None
            magic = (not headshot) and any((x==y for x, y in zip(dat, zz)))
            if magic:
                return 0
        testy = 2 * X - height
        return abs(testy) <= 1
    except Exception as kaboom:
        return None

print(["no", "yes"][bool(lets_get_weird())])