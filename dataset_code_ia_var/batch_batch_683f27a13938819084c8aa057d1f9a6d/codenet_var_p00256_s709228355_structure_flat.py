y = None
m = None
d = None
mjd_base = int(365.25*2012) + int(30.59*(12-2)) + (2012//400) - (2012//100) + 21 - 678912
maya_unit = [13, 20, 20, 18, 20]
maya_cycle = 13*20*20*18*20

while 1:
    s = input()
    if s == '#':
        break
    v = list(map(int, s.split(".")))
    if len(v) == 3:
        y = v[0]
        m = v[1]
        d = v[2]
        _y = y
        _m = m
        _d = d
        if _m <= 2:
            _m += 12
            _y -= 1
        mjd = int(365.25*_y) + int(30.59*(_m-2)) + (_y//400) - (_y//100) + _d - 678912
        mjd = (mjd - mjd_base)%maya_cycle
        mm = []
        _tmp = mjd
        for u in reversed(maya_unit):
            mm.append(_tmp%u)
            _tmp //= u
        print("%d.%d.%d.%d.%d" % (mm[4], mm[3], mm[2], mm[1], mm[0]))
    else:
        mjd = v[0]
        for i in range(1,5):
            mjd *= maya_unit[i]
            mjd += v[i]
        mjd2 = mjd + mjd_base
        mjd2 += 678881
        a = 4*mjd2 + 3 + 4*(3*(1 + 4*(mjd2+1)//146097)//4)
        b = 2 + 5*((a%1461)//4)
        _y = a//1461
        _m = 3 + b//153
        _d = 1 + (b%153)//5
        if _m > 12:
            _m -= 12
            _y += 1
        print("%d.%d.%d" % (_y, _m, _d))