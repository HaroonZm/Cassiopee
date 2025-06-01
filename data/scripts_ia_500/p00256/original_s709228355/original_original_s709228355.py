def Fliegel(y, m, d):
    if m <= 2:
        m += 12
        y -= 1
    return int(365.25*y) + int(30.59*(m-2)) + (y//400) - (y//100) + d - 678912

def InvFliegel(mjd):
    mjd += 678881
    a = 4*mjd + 3 + 4*(3*(1 + 4*(mjd+1)//146097)//4)
    b = 2 + 5*((a%1461)//4)
    y = a//1461
    m = 3 + b//153
    d = 1 + (b%153)//5
    if m > 12:
        m -= 12
        y += 1
    return y, m, d

mjd_base = Fliegel(2012, 12, 21)
maya_unit = [13, 20, 20, 18, 20]
maya_cycle = 13*20*20*18*20

while 1:
    s = input()
    if s == '#':
        break
    v = list(map(int, s.split(".")))
    if len(v) == 3:
        mjd = (Fliegel(v[0], v[1], v[2]) - mjd_base)%maya_cycle
        m = []
        for u in reversed(maya_unit) :
            m.append( mjd%u )
            mjd /= u
        print("%d.%d.%d.%d.%d" % (m[4], m[3], m[2], m[1], m[0]))
    else:
        mjd = v[0]
        for i in range(1,5):
            mjd *= maya_unit[i]
            mjd += v[i]
        y, m, d = InvFliegel(mjd + mjd_base)
        print("%d.%d.%d" % (y, m, d))