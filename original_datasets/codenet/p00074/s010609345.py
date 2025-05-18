#!/usr/bin/python

while True:
    h, m, s = map(int, raw_input().split())
    if h == m == s == -1:
        break

    full = 2 * 3600
    rest = full - (h * 3600 + m * 60 + s)

    h = int(rest / 3600)
    m = int((rest - h * 3600) / 60)
    s = rest - h * 3600 - m * 60 

    th = int(rest / 1200)
    tm = int((rest - th * 1200) / 20)
    ts = (rest - th * 1200 - tm * 20) * 3

    print "{:02d}:{:02d}:{:02d}".format(h, m, s)
    print "{:02d}:{:02d}:{:02d}".format(th, tm, ts)