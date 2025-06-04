import datetime

while True:
    y1, m1, d1, y2, m2, d2 = (int(x) for x in input().split())
    if y1 < 0:
        break
    start = datetime.date(y1, m1, d1)
    end = datetime.date(y2, m2, d2)
    print((end - start).days)