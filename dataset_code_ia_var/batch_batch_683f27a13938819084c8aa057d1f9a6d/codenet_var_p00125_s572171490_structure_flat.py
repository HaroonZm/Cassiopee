import datetime
while 1:
    vals = input().split()
    y1 = int(vals[0])
    m1 = int(vals[1])
    d1 = int(vals[2])
    y2 = int(vals[3])
    m2 = int(vals[4])
    d2 = int(vals[5])
    if y1 < 0:
        break
    start = datetime.date(y1, m1, d1)
    end = datetime.date(y2, m2, d2)
    print((end - start).days)