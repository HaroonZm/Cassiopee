from datetime import date, timedelta

st = date(2012, 12, 21)
while True:
    s = input()
    if s == '#':
        break
    d = s.split('.')
    for i in range(len(d)):
        d[i] = int(d[i])
    if len(d) == 3:
        r = 0
        while d[0] > 3000:
            d[0] = d[0] - 400
            r = r + 365 * 400 + 97
        y = d[0]
        m = d[1]
        da = d[2]
        ed = date(y, m, da)
        days = (ed - st).days
        r = r + days
        ki = r % 20
        r = r // 20
        w = r % 18
        r = r // 18
        t = r % 20
        r = r // 20
        ka = r % 20
        r = r // 20
        b = r % 13
        print(str(b) + '.' + str(ka) + '.' + str(t) + '.' + str(w) + '.' + str(ki))
    else:
        r = d[0]
        r = r * 20 + d[1]
        r = r * 20 + d[2]
        r = r * 18 + d[3]
        r = r * 20 + d[4]
        ed = st + timedelta(days=r)
        print(str(ed.year) + '.' + str(ed.month) + '.' + str(ed.day))