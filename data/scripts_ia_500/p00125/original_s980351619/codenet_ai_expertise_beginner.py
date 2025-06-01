import datetime

def days_between(y1, m1, d1, y2, m2, d2):
    date1 = datetime.date(y1, m1, d1)
    date2 = datetime.date(y2, m2, d2)
    difference = date2 - date1
    return difference.days

while True:
    parts = input().split()
    if len(parts) != 6:
        break
    y1, m1, d1, y2, m2, d2 = map(int, parts)
    try:
        print(days_between(y1, m1, d1, y2, m2, d2))
    except:
        break