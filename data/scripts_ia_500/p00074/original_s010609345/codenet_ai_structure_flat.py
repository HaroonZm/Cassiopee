#!/usr/bin/python

while True:
    line = raw_input()
    h, m, s = map(int, line.split())
    if h == -1 and m == -1 and s == -1:
        break
    full = 7200
    rest = full - (h * 3600 + m * 60 + s)
    h = rest // 3600
    m = (rest - h * 3600) // 60
    s = rest - h * 3600 - m * 60
    th = rest // 1200
    tm = (rest - th * 1200) // 20
    ts = (rest - th * 1200 - tm * 20) * 3
    print "%02d:%02d:%02d" % (h, m, s)
    print "%02d:%02d:%02d" % (th, tm, ts)