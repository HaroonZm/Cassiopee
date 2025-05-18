from datetime import date, timedelta

st = date(2012, 12, 21)
while True:
    s = input()
    if s == '#':
        break
    d = list(map(int, s.split('.')))
    if len(d) == 3:
        r = 0
        while d[0] > 3000:
            d[0] -= 400
            r += 365*400+97

        ed = date(d[0], d[1], d[2])
        r += (ed-st).days
        ki = r%20
        r//=20
        w = r%18
        r//=18
        t = r%20
        r//=20
        ka = r%20
        r//=20
        b = r%13
        print(str(b)+'.'+str(ka)+'.'+str(t)+'.'+str(w)+'.'+str(ki))
    else:
        r = d[0]
        r *= 20
        r += d[1]
        r *= 20
        r += d[2]
        r *= 18
        r += d[3]
        r *= 20
        r += d[4]
        ed = st+timedelta(days=r)
        print(str(ed.year)+'.'+str(ed.month)+'.'+str(ed.day))