import datetime

while True:
    y1, m1, d1, y2, m2, d2 = map(int, input().split())
    if y1 == -1:
        break
    delta = datetime.datetime(y2, m2, d2) - datetime.datetime(y1, m1, d1)
    print(delta.days)