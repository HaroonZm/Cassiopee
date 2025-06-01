import datetime

while True:
    values = input()
    y1, m1, d1, y2, m2, d2 = values.split()
    y1 = int(y1)
    if y1 == -1:
        break
    m1 = int(m1)
    d1 = int(d1)
    y2 = int(y2)
    m2 = int(m2)
    d2 = int(d2)

    date1 = datetime.datetime(y1, m1, d1)
    date2 = datetime.datetime(y2, m2, d2)
    diff = date2 - date1
    print(diff.days)